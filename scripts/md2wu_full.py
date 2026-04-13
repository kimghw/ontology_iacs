#!/usr/bin/env python3
"""
md2wu 통합 파이프라인 (Phase A/B/C)
- Phase A: S1-2 전량 스캔 (기계적 헤딩 추출 + 토큰 측정)
- Phase B: 600K 토큰 기준 배치 계획
- Phase C: 배치 단위 S3-7 (분류 → 청크 → WU → 매니페스트)

산출물 배치:
  skill_md2wu/                    → 최종 (WU .md, manifest, issue report)
  skill_md2wu/temp/pre/           → 중간 (TSV, chunk plan, classification, etc.)
  skill_md2wu/queue/locks/        → 글로벌 락
  skill_md2wu/queue/sessions/     → 세션별 scan_index, batch_plan
"""

import os
import re
import sys
import json
import math
import hashlib
from datetime import datetime, timezone

import tiktoken

# ── Config ──
SRC_DIR = sys.argv[1] if len(sys.argv) > 1 else "/home/kimghw/ontology_iacs/UR/UR_Z_md"
BASE_DIR = "/mnt/c/shared_wk/ontology_iacs"
SKILL_DIR = os.path.join(BASE_DIR, "skill_md2wu")
TEMP_PRE = os.path.join(SKILL_DIR, "temp", "pre")
QUEUE_DIR = os.path.join(SKILL_DIR, "queue")
LOCKS_DIR = os.path.join(QUEUE_DIR, "locks")
SESSIONS_DIR = os.path.join(QUEUE_DIR, "sessions")

CHUNK_MAX = 32000
CHUNK_EXCEPTION = 48000
WU_MIN = 16000
BATCH_TOKEN_LIMIT = 600000  # 600K tokens per batch

# Source identity — 입력 경로에서 자동 추출하거나 수동 지정
AUTHORITY = 'IACS'
DOC_TYPE = 'UR'
SERIES = 'z'  # UR Z series. UR A series → 'a', UI → 변경
STALE_THRESHOLD_HOURS = 4

ENC = tiktoken.get_encoding("cl100k_base")


# ════════════════════════════════════════════
# Helpers
# ════════════════════════════════════════════

def slugify(text: str) -> str:
    s = text.lower()
    s = re.sub(r'[\s\-/\.]+', '_', s)
    s = re.sub(r'[^a-z0-9_]', '', s)
    s = re.sub(r'_+', '_', s)
    return s.strip('_')


def count_tokens(text: str) -> int:
    return len(ENC.encode(text))


def extract_z_number(title: str, filename: str) -> str:
    """Z번호 추출: L1 헤딩 우선 (Z10.4 등 dot 포함), 실패 시 파일명."""
    m = re.search(r'[Zz](\d+(?:\.\d+)*)', title)
    if m:
        return f"z{m.group(1).replace('.', '_')}"
    base = os.path.splitext(filename)[0]
    m = re.search(r'[Zz](\d+(?:\.\d+)*)', base)
    if m:
        return f"z{m.group(1).replace('.', '_')}"
    return slugify(title)[:20]


def extract_revision(filename: str, preamble_lines: list[str]) -> str:
    """Revision 추출: 파일명 우선, 실패 시 preamble 마지막 Rev."""
    base = os.path.splitext(filename)[0]
    rev_m = re.search(r'[Rr]ev\.?\s*(\d+)', base)
    rev = f"rev{rev_m.group(1)}" if rev_m else ""
    corr_m = re.search(r'[Cc]orr\.?\s*(\d+)', base)
    corr = f"_corr{corr_m.group(1)}" if corr_m else ""
    if rev or corr:
        return f"{rev}{corr}" if rev else corr.lstrip('_')
    preamble = "\n".join(preamble_lines[:40])
    revs = re.findall(r'\(Rev\.?\s*(\d+)', preamble)
    if revs:
        return f"rev{revs[-1]}"
    return "rev0"


# ════════════════════════════════════════════
# Stage 1-2: Heading Extraction + Token Measurement
# ════════════════════════════════════════════

def parse_headings(lines: list[str]) -> list[dict]:
    headings = []
    in_code = False
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if s.startswith('```') or s.startswith('~~~'):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            headings.append({'level': len(m.group(1)), 'line_no': i, 'title': m.group(2).strip()})
    return headings


def process_file_stage12(filepath: str) -> dict:
    """Stage 1-2 for a single file."""
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.splitlines(keepends=True)
    lines_plain = content.splitlines()
    total_lines = len(lines)
    total_tokens = count_tokens(content)

    # Parse headings
    headings = parse_headings(lines)

    # L1 title
    l1 = [h for h in headings if h['level'] == 1]
    title = l1[0]['title'] if l1 else os.path.splitext(filename)[0]

    # Doc key & revision
    doc_key = extract_z_number(title, filename)
    revision = extract_revision(filename, lines_plain)
    doc_instance_key = f"{doc_key}_{revision}_en"
    is_deleted = 'del' in filename.lower() and total_lines < 15

    if not headings:
        return {
            'filepath': filepath, 'filename': filename,
            'doc_key': doc_key, 'doc_instance_key': doc_instance_key,
            'title': title, 'revision': revision, 'is_deleted': is_deleted,
            'total_lines': total_lines, 'total_tokens': total_tokens,
            'headings': [], 'additivity_errors': [],
        }

    n = len(headings)

    # End lines
    for i, h in enumerate(headings):
        h['end_line'] = total_lines
        for j in range(i + 1, n):
            if headings[j]['level'] <= h['level']:
                h['end_line'] = headings[j]['line_no'] - 1
                break

    # Heading IDs
    for i, h in enumerate(headings):
        h['heading_id'] = f"{doc_key}_HD_{i+1:03d}"

    # Parent IDs
    stack = []
    for h in headings:
        while stack and stack[-1][0] >= h['level']:
            stack.pop()
        h['parent_id'] = stack[-1][1] if stack else ''
        stack.append((h['level'], h['heading_id']))

    # Tokens inclusive
    for h in headings:
        span = ''.join(lines[h['line_no']-1 : h['end_line']])
        h['tokens_inclusive'] = count_tokens(span)

    # Tokens exclusive
    children_map = {h['heading_id']: [] for h in headings}
    for h in headings:
        if h['parent_id']:
            children_map[h['parent_id']].append(h['heading_id'])
    id_map = {h['heading_id']: h for h in headings}
    for h in headings:
        csum = sum(id_map[c]['tokens_inclusive'] for c in children_map[h['heading_id']])
        h['tokens_exclusive'] = h['tokens_inclusive'] - csum

    # Additivity check
    errors = []
    for h in headings:
        cids = children_map[h['heading_id']]
        if cids:
            computed = h['tokens_exclusive'] + sum(id_map[c]['tokens_inclusive'] for c in cids)
            if computed != h['tokens_inclusive']:
                errors.append(f"{h['heading_id']}: {computed} != {h['tokens_inclusive']}")

    return {
        'filepath': filepath, 'filename': filename,
        'doc_key': doc_key, 'doc_instance_key': doc_instance_key,
        'title': title, 'revision': revision, 'is_deleted': is_deleted,
        'total_lines': total_lines, 'total_tokens': total_tokens,
        'headings': headings, 'additivity_errors': errors,
    }


def write_tsv(doc: dict, out_dir: str) -> str:
    path = os.path.join(out_dir, f"doc-{doc['doc_instance_key']}__heading__structure.tsv")
    with open(path, 'w', encoding='utf-8') as f:
        f.write("Heading_ID\tLevel\tStart_Line\tEnd_Line\tTitle\tParent_ID\tEst_Tokens_Inclusive\tEst_Tokens_Exclusive\n")
        for h in doc['headings']:
            f.write(f"{h['heading_id']}\t{h['level']}\t{h['line_no']}\t{h['end_line']}\t"
                    f"{h['title']}\t{h['parent_id']}\t{h['tokens_inclusive']}\t{h['tokens_exclusive']}\n")
    return path


# ════════════════════════════════════════════
# Stage 5: Chunk Planning
# ════════════════════════════════════════════

def stage5_chunk(doc: dict) -> list[dict]:
    dik = doc['doc_instance_key']
    headings = doc['headings']
    total_tokens = doc['total_tokens']

    # Single chunk if fits exception
    if total_tokens <= CHUNK_EXCEPTION:
        method = 'headingless' if not headings else 'recursive'
        hr = None
        if headings:
            hr = {'first': headings[0]['heading_id'], 'last': headings[-1]['heading_id']}
        return [{
            'chunk_key': f"{dik}_ch001", 'heading_range': hr,
            'heading_level': 'Document' if headings else None,
            'start_line': 1, 'end_line': doc['total_lines'],
            'est_tokens': total_tokens, 'split_method': method,
            'measure_method': 'tiktoken', 'sub_chunks': None,
        }]

    # Split at L2 boundaries
    l2 = [h for h in headings if h['level'] == 2]
    if not l2:
        l2 = [h for h in headings if h['level'] == 3]
    if not l2:
        return [{
            'chunk_key': f"{dik}_ch001", 'heading_range': None,
            'heading_level': None, 'start_line': 1, 'end_line': doc['total_lines'],
            'est_tokens': total_tokens, 'split_method': 'headingless',
            'measure_method': 'tiktoken', 'sub_chunks': None,
        }]

    n_chunks = math.ceil(total_tokens / CHUNK_MAX)
    target = total_tokens / n_chunks

    chunks = []
    cur_spans, cur_tok = [], 0
    for span in l2:
        stok = span['tokens_inclusive']
        if cur_spans and cur_tok + stok > target * 1.3:
            chunks.append(_close_chunk(cur_spans, cur_tok, dik, len(chunks) + 1))
            cur_spans, cur_tok = [], 0
        cur_spans.append(span)
        cur_tok += stok
    if cur_spans:
        chunks.append(_close_chunk(cur_spans, cur_tok, dik, len(chunks) + 1))

    # Add preamble to first chunk
    l1 = [h for h in headings if h['level'] == 1]
    if l1 and l2 and chunks:
        preamble_tok = l1[0]['tokens_exclusive']
        if preamble_tok > 0:
            chunks[0]['start_line'] = 1
            chunks[0]['est_tokens'] += preamble_tok

    # Merge undersized adjacent
    merged = []
    for ch in chunks:
        if merged and ch['est_tokens'] < WU_MIN and merged[-1]['est_tokens'] + ch['est_tokens'] <= CHUNK_MAX:
            merged[-1]['end_line'] = ch['end_line']
            merged[-1]['est_tokens'] += ch['est_tokens']
            merged[-1]['heading_range']['last'] = ch['heading_range']['last']
        else:
            merged.append(ch)
    for i, ch in enumerate(merged):
        ch['chunk_key'] = f"{dik}_ch{i+1:03d}"

    return merged


def _close_chunk(spans, tokens, dik, idx):
    return {
        'chunk_key': f"{dik}_ch{idx:03d}",
        'heading_range': {'first': spans[0]['heading_id'], 'last': spans[-1]['heading_id']},
        'heading_level': 'Section', 'start_line': spans[0]['line_no'],
        'end_line': spans[-1]['end_line'], 'est_tokens': tokens,
        'split_method': 'recursive', 'measure_method': 'tiktoken', 'sub_chunks': None,
    }


# ════════════════════════════════════════════
# Stage 6: WU Packing
# ════════════════════════════════════════════

def stage6_pack(docs_chunks: list[dict]) -> list[dict]:
    prefix = f"{AUTHORITY.lower()}_{DOC_TYPE.lower()}"
    wus = []
    merge_candidates = []

    for dc in docs_chunks:
        doc, chunks, total_tok = dc['doc'], dc['chunks'], dc['doc']['total_tokens']
        if doc['is_deleted'] and total_tok < 100:
            merge_candidates.append(dc)
            continue
        if total_tok > CHUNK_MAX and len(chunks) > 1:
            # Split WU
            for i, ch in enumerate(chunks):
                wus.append(_make_wu(
                    f"{prefix}_{doc['doc_instance_key']}_wu{i+1:03d}", 'split',
                    AUTHORITY, DOC_TYPE, doc, ch['start_line'], ch['end_line'],
                    ch['est_tokens'], ch['heading_range'], [ch['chunk_key']]))
        elif total_tok >= WU_MIN:
            # Standalone
            hr = chunks[0]['heading_range'] if chunks else None
            wus.append(_make_wu(
                f"{prefix}_{doc['doc_instance_key']}", 'standalone',
                AUTHORITY, DOC_TYPE, doc, 1, doc['total_lines'],
                total_tok, hr, [ch['chunk_key'] for ch in chunks]))
        else:
            merge_candidates.append(dc)

    # Merge candidates
    if merge_candidates:
        merge_candidates.sort(key=lambda x: x['doc']['doc_key'])
        cur_group, cur_tok = [], 0
        for mc in merge_candidates:
            mt = mc['doc']['total_tokens']
            if cur_group and cur_tok + mt > CHUNK_MAX:
                wus.append(_make_merge_wu(prefix, AUTHORITY, DOC_TYPE, cur_group, cur_tok))
                cur_group, cur_tok = [], 0
            cur_group.append(mc)
            cur_tok += mt
        if cur_group:
            wus.append(_make_merge_wu(prefix, AUTHORITY, DOC_TYPE, cur_group, cur_tok))

    return wus


def _make_wu(key, wtype, auth, dtype, doc, sl, el, tok, hr, ckeys):
    return {
        'wu_key': key, 'wu_type': wtype,
        'authority': auth, 'doc_type': dtype, 'language': 'en',
        'grammar_version': 'v01', 'measure_method': 'tiktoken',
        'constituent_docs': [{
            'doc_instance_key': doc['doc_instance_key'],
            'document_key': doc['doc_key'],
            'start_line': sl, 'end_line': el,
            'est_tokens': tok, 'heading_range': hr,
        }],
        'est_tokens_total': tok, 'chunk_keys': ckeys,
        'status': 'planned', 'output_files': [],
        'created_at': datetime.now(timezone.utc).isoformat(),
    }


def _make_merge_wu(prefix, auth, dtype, group, total_tok):
    keys_str = "|".join(m['doc']['doc_instance_key'] for m in group)
    short_hash = hashlib.sha256(keys_str.encode()).hexdigest()[:8]
    wu_key = f"{prefix}_merge_{short_hash}"
    cdocs, ckeys = [], []
    for m in group:
        d = m['doc']
        cdocs.append({
            'doc_instance_key': d['doc_instance_key'], 'document_key': d['doc_key'],
            'start_line': 1, 'end_line': d['total_lines'],
            'est_tokens': d['total_tokens'],
            'heading_range': m['chunks'][0]['heading_range'] if m['chunks'] else None,
        })
        ckeys.extend(ch['chunk_key'] for ch in m['chunks'])
    return {
        'wu_key': wu_key, 'wu_type': 'merged',
        'authority': auth, 'doc_type': dtype, 'language': 'en',
        'grammar_version': 'v01', 'measure_method': 'tiktoken',
        'constituent_docs': cdocs, 'est_tokens_total': total_tok,
        'chunk_keys': ckeys, 'status': 'planned', 'output_files': [],
        'created_at': datetime.now(timezone.utc).isoformat(),
    }


# ════════════════════════════════════════════
# Stage 7: Issue Gate + Emit
# ════════════════════════════════════════════

def stage7_issues(wus):
    issues = []
    for wu in wus:
        tok = wu['est_tokens_total']
        if tok > CHUNK_EXCEPTION:
            issues.append({'wu_key': wu['wu_key'], 'issue_type': 'oversize_hard',
                           'severity': 'HIGH', 'est_tokens': tok, 'threshold': CHUNK_EXCEPTION,
                           'message': f"WU tokens ({tok}) > 1.5× upper bound ({CHUNK_EXCEPTION})"})
        elif tok > CHUNK_MAX:
            issues.append({'wu_key': wu['wu_key'], 'issue_type': 'oversize_exception',
                           'severity': 'INFO', 'est_tokens': tok, 'threshold': CHUNK_MAX,
                           'message': f"WU tokens ({tok}) > upper bound ({CHUNK_MAX}) but ≤ 1.5× — exception allowed"})
            wu['status'] = 'processed'
        elif tok < WU_MIN and wu['wu_type'] in ('standalone', 'split'):
            issues.append({'wu_key': wu['wu_key'], 'issue_type': 'undersized',
                           'severity': 'LOW', 'est_tokens': tok, 'threshold': WU_MIN,
                           'message': f"WU tokens ({tok}) < lower bound ({WU_MIN})"})
            wu['status'] = 'processed'
        else:
            wu['status'] = 'processed'
    return issues


def emit_wu_md(wu, src_map):
    """Extract WU content from source files → .md"""
    parts = []
    for doc in wu['constituent_docs']:
        dik = doc['doc_instance_key']
        fp = src_map.get(dik)
        if not fp or not os.path.exists(fp):
            parts.append(f"<!-- Source not found: {dik} -->\n")
            continue
        with open(fp, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        content = ''.join(lines[doc['start_line']-1 : doc['end_line']])
        parts.append(content)
    return '\n'.join(parts)


# ════════════════════════════════════════════
# Lock Management
# ════════════════════════════════════════════

def get_session_id() -> str:
    sid = os.environ.get('CLAUDE_SESSION_ID', '')
    if sid:
        return sid
    import uuid
    return str(uuid.uuid4())[:8]


def acquire_lock(corpus_scope: str, session_id: str, state: str = "scanning") -> bool:
    os.makedirs(LOCKS_DIR, exist_ok=True)
    lock_path = os.path.join(LOCKS_DIR, f"{corpus_scope}.lock")
    lock_data = json.dumps({"owner": session_id, "state": state,
                            "claimed_at": datetime.now(timezone.utc).isoformat()})
    try:
        fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(fd, lock_data.encode())
        os.close(fd)
        return True
    except FileExistsError:
        try:
            age_h = (datetime.now().timestamp() - os.path.getmtime(lock_path)) / 3600
            with open(lock_path) as f:
                ex = json.load(f)
            if age_h > STALE_THRESHOLD_HOURS and ex.get('state') != 'failed':
                print(f"  WARNING: Stale lock ({age_h:.1f}h, owner={ex.get('owner')})")
            else:
                print(f"  Lock held: owner={ex.get('owner')}, state={ex.get('state')}")
        except Exception:
            pass
        return False


def update_lock_state(corpus_scope: str, session_id: str, new_state: str):
    lock_path = os.path.join(LOCKS_DIR, f"{corpus_scope}.lock")
    tmp = f"{lock_path}.tmp.{os.getpid()}"
    with open(tmp, 'w') as f:
        f.write(json.dumps({"owner": session_id, "state": new_state,
                             "claimed_at": datetime.now(timezone.utc).isoformat()}))
    os.rename(tmp, lock_path)


def release_lock(corpus_scope: str):
    lock_path = os.path.join(LOCKS_DIR, f"{corpus_scope}.lock")
    if os.path.exists(lock_path):
        os.unlink(lock_path)


# ════════════════════════════════════════════
# Phase A — Scan (S1-2)
# ════════════════════════════════════════════

def phase_a_scan(md_files: list, session_dir: str) -> dict:
    print("\n══ Phase A: 전량 스캔 (S1-2) ══")
    docs, total_errors = [], 0
    for fp in md_files:
        d = process_file_stage12(fp)
        docs.append(d)
        write_tsv(d, TEMP_PRE)
        tag = "[DEL]" if d['is_deleted'] else ""
        err = f"ERR({len(d['additivity_errors'])})" if d['additivity_errors'] else "OK"
        print(f"  {d['doc_instance_key']:42s} | {d['total_tokens']:6d}tok | {len(d['headings']):3d}HD | {err} {tag}")
        total_errors += len(d['additivity_errors'])

    total_tokens = sum(d['total_tokens'] for d in docs)
    print(f"  총 {len(docs)} 파일, {total_tokens:,} 토큰, 가산성 오류 {total_errors}")

    scan_index = {
        'scan_id': datetime.now(timezone.utc).isoformat(), 'source_dir': SRC_DIR,
        'files': [{'doc_instance_key': d['doc_instance_key'], 'doc_key': d['doc_key'],
                    'filepath': d['filepath'], 'title': d['title'],
                    'total_tokens': d['total_tokens'], 'heading_count': len(d['headings']),
                    'is_deleted': d['is_deleted'],
                    'tsv_path': f"doc-{d['doc_instance_key']}__heading__structure.tsv",
                    } for d in docs],
        'total_tokens': total_tokens, 'total_files': len(docs),
    }
    with open(os.path.join(session_dir, "scan_index.json"), 'w', encoding='utf-8') as f:
        json.dump(scan_index, f, indent=2, ensure_ascii=False)
    return {'scan_index': scan_index, 'docs': docs}


# ════════════════════════════════════════════
# Phase B — Batch Planning
# ════════════════════════════════════════════

def phase_b_batch_plan(scan_index: dict, session_dir: str) -> dict:
    print("\n══ Phase B: 배치 계획 (600K/batch) ══")
    files = sorted(scan_index['files'], key=lambda f: f['doc_key'])
    batches, cur, cur_tok, idx = [], [], 0, 1

    for f in files:
        if cur and cur_tok + f['total_tokens'] > BATCH_TOKEN_LIMIT:
            batches.append({'batch_id': f"batch_{idx:03d}", 'files': [x['doc_instance_key'] for x in cur],
                            'est_tokens': cur_tok, 'file_count': len(cur), 'status': 'pending'})
            idx += 1
            cur, cur_tok = [], 0
        cur.append(f)
        cur_tok += f['total_tokens']
    if cur:
        batches.append({'batch_id': f"batch_{idx:03d}", 'files': [x['doc_instance_key'] for x in cur],
                        'est_tokens': cur_tok, 'file_count': len(cur), 'status': 'pending'})

    plan = {'created_at': datetime.now(timezone.utc).isoformat(),
            'batch_token_limit': BATCH_TOKEN_LIMIT, 'total_batches': len(batches),
            'total_tokens': scan_index['total_tokens'], 'total_files': scan_index['total_files'],
            'batches': batches}
    with open(os.path.join(session_dir, "batch_plan.json"), 'w', encoding='utf-8') as f:
        json.dump(plan, f, indent=2, ensure_ascii=False)

    for b in batches:
        print(f"  {b['batch_id']}: {b['file_count']} files, {b['est_tokens']:,} tok")
    return plan


# ════════════════════════════════════════════
# Phase C — Batch Execution (S3-7)
# ════════════════════════════════════════════

def phase_c_execute_batch(batch: dict, all_docs: list, corpus_scope: str, session_dir: str):
    bid = batch['batch_id']
    diks = set(batch['files'])
    batch_docs = [d for d in all_docs if d['doc_instance_key'] in diks]

    print(f"\n  ── {bid}: S3-4 분류 ──")
    with open(os.path.join(TEMP_PRE, f"{corpus_scope}__{bid}__classification.json"), 'w', encoding='utf-8') as f:
        json.dump({'authority': AUTHORITY, 'doc_type': DOC_TYPE,
                    'documents': [{'doc_instance_key': d['doc_instance_key'], 'doc_key': d['doc_key'],
                                   'title': d['title']} for d in batch_docs]}, f, indent=2, ensure_ascii=False)
    print(f"    {AUTHORITY}/{DOC_TYPE}, {len(batch_docs)} docs")

    print(f"  ── {bid}: S5-6 청크+WU ──")
    docs_chunks = []
    for d in batch_docs:
        chunks = stage5_chunk(d)
        docs_chunks.append({'doc': d, 'chunks': chunks})
        with open(os.path.join(TEMP_PRE, f"doc-{d['doc_instance_key']}__heading__chunk_plan.json"), 'w', encoding='utf-8') as f:
            json.dump(chunks, f, indent=2, ensure_ascii=False)

    wus = stage6_pack(docs_chunks)
    for wu in wus:
        with open(os.path.join(TEMP_PRE, f"wu-{wu['wu_key']}__pre__meta.json"), 'w', encoding='utf-8') as f:
            json.dump(wu, f, indent=2, ensure_ascii=False)

    st = [w for w in wus if w['wu_type'] == 'standalone']
    sp = [w for w in wus if w['wu_type'] == 'split']
    mg = [w for w in wus if w['wu_type'] == 'merged']
    print(f"    WU: {len(st)} standalone, {len(sp)} split, {len(mg)} merged = {len(wus)} total")

    print(f"  ── {bid}: S7 이슈+출력 ──")
    issues = stage7_issues(wus)
    for iss in issues:
        print(f"    [{iss['severity']}] {iss['wu_key']}: {iss['message']}")

    src_map = {d['doc_instance_key']: d['filepath'] for d in batch_docs}
    for wu in wus:
        md_content = emit_wu_md(wu, src_map)
        md_path = os.path.join(SKILL_DIR, f"wu-{wu['wu_key']}__pre__content.md")
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        wu['output_files'] = [md_path]
        with open(os.path.join(TEMP_PRE, f"wu-{wu['wu_key']}__pre__meta.json"), 'w', encoding='utf-8') as f:
            json.dump(wu, f, indent=2, ensure_ascii=False)

    # Batch status
    bd = os.path.join(session_dir, "batches", bid)
    os.makedirs(bd, exist_ok=True)
    with open(os.path.join(bd, "status.json"), 'w', encoding='utf-8') as f:
        json.dump({'batch_id': bid, 'status': 'done', 'wus': len(wus), 'issues': len(issues),
                   'completed_at': datetime.now(timezone.utc).isoformat()}, f, indent=2)

    return {'wus': wus, 'issues': issues}


# ════════════════════════════════════════════
# Main
# ════════════════════════════════════════════

def main():
    os.makedirs(SKILL_DIR, exist_ok=True)
    os.makedirs(TEMP_PRE, exist_ok=True)

    corpus_scope = f"{AUTHORITY.lower()}_{DOC_TYPE.lower()}_{SERIES}"
    session_id = get_session_id()
    session_dir = os.path.join(SESSIONS_DIR, session_id)
    os.makedirs(session_dir, exist_ok=True)

    md_files = sorted([os.path.join(SRC_DIR, f) for f in os.listdir(SRC_DIR) if f.endswith('.md')])

    print(f"md2wu 파이프라인")
    print(f"  대상: {SRC_DIR} ({len(md_files)} files)")
    print(f"  corpus: {corpus_scope}, session: {session_id}")
    print(f"  출력: {SKILL_DIR}")
    print("=" * 80)

    if not acquire_lock(corpus_scope, session_id):
        print(f"\nERROR: Lock acquisition failed for {corpus_scope}. Aborting.")
        sys.exit(1)
    print(f"  Lock acquired: {corpus_scope}")

    try:
        result_a = phase_a_scan(md_files, session_dir)
        update_lock_state(corpus_scope, session_id, "batching")

        batch_plan = phase_b_batch_plan(result_a['scan_index'], session_dir)
        update_lock_state(corpus_scope, session_id, "processing")

        print("\n══ Phase C: 배치 실행 (S3-7) ══")
        all_wus, all_issues = [], []
        for batch in batch_plan['batches']:
            r = phase_c_execute_batch(batch, result_a['docs'], f"corpus-{corpus_scope}", session_dir)
            all_wus.extend(r['wus'])
            all_issues.extend(r['issues'])

        # ── Final outputs ──
        print("\n══ 최종 산출물 ══")
        cs = f"corpus-{corpus_scope}"
        with open(os.path.join(SKILL_DIR, f"{cs}__md2wu__issue_gate_report.json"), 'w', encoding='utf-8') as f:
            json.dump(all_issues, f, indent=2, ensure_ascii=False)

        docs = result_a['docs']
        sf = f"# Source Family Report — {DOC_TYPE} {SERIES.upper()}\n\n" \
             f"- Authority: {AUTHORITY}, DocType: {DOC_TYPE}\n" \
             f"- Documents: {len(docs)}, Tokens: {sum(d['total_tokens'] for d in docs):,}\n" \
             f"- Batches: {batch_plan['total_batches']}\n"
        with open(os.path.join(TEMP_PRE, f"{cs}__md2wu__source_family_report.md"), 'w', encoding='utf-8') as f:
            f.write(sf)

        standalone = [w for w in all_wus if w['wu_type'] == 'standalone']
        split_wus = [w for w in all_wus if w['wu_type'] == 'split']
        merged = [w for w in all_wus if w['wu_type'] == 'merged']
        manifest = {
            'pipeline': 'md2wu', 'source_dir': SRC_DIR,
            'authority': AUTHORITY, 'doc_type': DOC_TYPE,
            'total_source_files': len(md_files), 'total_documents': len(docs),
            'total_wus': len(all_wus),
            'wu_breakdown': {'standalone': len(standalone), 'split': len(split_wus), 'merged': len(merged)},
            'batches': batch_plan['total_batches'], 'issues': all_issues,
            'wus': [{'wu_key': w['wu_key'], 'wu_type': w['wu_type'],
                      'est_tokens_total': w['est_tokens_total'], 'status': w['status'],
                      'constituent_docs': [d['doc_instance_key'] for d in w['constituent_docs']],
                      'content_file': f"wu-{w['wu_key']}__pre__content.md"} for w in all_wus],
            'created_at': datetime.now(timezone.utc).isoformat(),
        }
        with open(os.path.join(SKILL_DIR, f"{cs}__pre__manifest.json"), 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)

        print(f"\n=== skill_md2wu/ ===")
        for fn in sorted(os.listdir(SKILL_DIR)):
            fp = os.path.join(SKILL_DIR, fn)
            if os.path.isfile(fp):
                print(f"  {os.path.getsize(fp):>8d}  {fn}")
        print(f"\n  temp/pre/: {len(os.listdir(TEMP_PRE))} 개")
        print(f"  session: {session_dir}")

        release_lock(corpus_scope)
        print(f"  Lock released: {corpus_scope}")
        print("DONE")

    except Exception as e:
        update_lock_state(corpus_scope, session_id, "failed")
        print(f"\nERROR: {e}")
        print(f"  Lock → failed. Manual: rm {os.path.join(LOCKS_DIR, corpus_scope + '.lock')}")
        raise


if __name__ == '__main__':
    main()
