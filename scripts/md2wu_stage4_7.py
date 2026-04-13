#!/usr/bin/env python3
"""md2wu Stage 4-7: Classification, Chunk Plan, WU Packing, Issue Gate & Manifest."""

import os
import re
import sys
import json
import math
import hashlib
from datetime import datetime, timezone

# ── Config ──
SRC_DIR = sys.argv[1] if len(sys.argv) > 1 else "/home/kimghw/ontology_iacs/UR/UR_Z_md"
OUT_DIR = "/mnt/c/shared_wk/ontology_iacs/results"
CHUNK_MAX = 32000
CHUNK_EXCEPTION = 48000  # 1.5x
WU_MIN = 16000
WU_RANGE = (16000, 32000)

# ── Helpers ──
def slugify(text: str) -> str:
    s = text.lower()
    s = re.sub(r'[\s\-/\.]+', '_', s)
    s = re.sub(r'[^a-z0-9_]', '', s)
    s = re.sub(r'_+', '_', s)
    return s.strip('_')

def extract_z_number(filename: str, title: str) -> str:
    """Extract Z number from title first (has dots), then filename."""
    # Try title first — has proper formatting like Z10.4
    m = re.search(r'[Zz](\d+(?:\.\d+)*)', title)
    if m:
        return f"z{m.group(1).replace('.', '_')}"
    # Try filename — may lack dots (ur_z104 = Z10.4)
    base = os.path.splitext(os.path.basename(filename))[0]
    m = re.search(r'[Zz](\d+(?:\.\d+)*)', base)
    if m:
        return f"z{m.group(1).replace('.', '_')}"
    return slugify(title)[:20]

def extract_revision(filename: str, lines: list[str]) -> str:
    """Extract revision from filename, then preamble."""
    base = os.path.splitext(os.path.basename(filename))[0]
    # Filename patterns: Rev.10, Rev21, rev25, Rev.29
    m = re.search(r'[Rr]ev\.?\s*(\d+)', base)
    rev = f"rev{m.group(1)}" if m else ""
    # Corr
    m = re.search(r'[Cc]orr\.?\s*(\d+)', base)
    corr = f"_corr{m.group(1)}" if m else ""
    if rev or corr:
        return f"{rev}{corr}" if rev else corr.lstrip('_')
    # Check preamble for last revision
    preamble = "\n".join(lines[:40])
    revs = re.findall(r'\(Rev\.?\s*(\d+)', preamble)
    if revs:
        return f"rev{revs[-1]}"
    return "rev0"

def parse_tsv(tsv_path: str) -> list[dict]:
    """Parse heading structure TSV."""
    rows = []
    with open(tsv_path, 'r', encoding='utf-8') as f:
        header = f.readline().strip().split('\t')
        for line in f:
            vals = line.strip().split('\t')
            if len(vals) >= 8:
                rows.append({
                    'heading_id': vals[0],
                    'level': int(vals[1]),
                    'start_line': int(vals[2]),
                    'end_line': int(vals[3]),
                    'title': vals[4],
                    'parent_id': vals[5],
                    'tokens_inclusive': int(vals[6]),
                    'tokens_exclusive': int(vals[7]),
                })
    return rows

def build_doc_info(filepath: str) -> dict:
    """Build corrected document info."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    filename = os.path.basename(filepath)
    base = os.path.splitext(filename)[0]

    # Parse headings to get L1 title
    title = base
    for line in lines:
        m = re.match(r'^#\s+(.*)', line)
        if m:
            title = m.group(1).strip()
            break

    z_num = extract_z_number(filename, title)
    revision = extract_revision(filename, lines)
    doc_key = z_num
    doc_instance_key = f"{doc_key}_{revision}_en"

    # Detect deleted
    is_deleted = 'del' in base.lower() and len(lines) < 15

    # Total tokens from TSV or approximate
    total_tokens = sum(1 for _ in lines) * 5  # rough, will be overridden by TSV

    return {
        'filepath': filepath,
        'filename': filename,
        'doc_key': doc_key,
        'doc_instance_key': doc_instance_key,
        'title': title,
        'revision': revision,
        'is_deleted': is_deleted,
        'total_lines': len(lines),
    }

# ── Stage 4: Classification ──
def stage4_classify(docs: list[dict]) -> dict:
    """Extract Authority, DocType, Heading Level for all documents."""
    classification = {
        'authority': 'IACS',
        'doc_type': 'UR',
        'source_family': 'IACS UR/UI/Rec/PR',
        'heading_levels': {
            'L1': 'Document',
            'L2': 'Section',
            'L3': 'Subsection',
            'L4': 'Paragraph',
            'L5': 'Sub-paragraph',
            'L6': 'Sub-sub-paragraph',
        },
        'documents': [],
    }
    for doc in docs:
        classification['documents'].append({
            'doc_instance_key': doc['doc_instance_key'],
            'doc_key': doc['doc_key'],
            'title': doc['title'],
            'authority': 'IACS',
            'doc_type': 'UR',
            'language': 'en',
            'is_deleted': doc['is_deleted'],
        })
    return classification

# ── Stage 5: Chunk Planning ──
def stage5_chunk_plan(doc: dict, headings: list[dict], total_tokens: int) -> list[dict]:
    """Generate chunk plan for a document."""
    dik = doc['doc_instance_key']

    # If total tokens <= chunk_exception, single chunk
    if total_tokens <= CHUNK_EXCEPTION:
        split_method = 'recursive'
        if not headings:
            split_method = 'headingless'
        heading_range = None
        heading_level = None
        if headings:
            heading_range = {'first': headings[0]['heading_id'], 'last': headings[-1]['heading_id']}
            heading_level = 'Document'
        return [{
            'chunk_key': f"{dik}_ch001",
            'heading_range': heading_range,
            'heading_level': heading_level,
            'start_line': 1,
            'end_line': doc['total_lines'],
            'est_tokens': total_tokens,
            'split_method': split_method,
            'measure_method': 'tiktoken',
            'sub_chunks': None,
        }]

    # Need to split at L2 boundaries
    l2_spans = []
    for h in headings:
        if h['level'] == 2:
            l2_spans.append(h)

    if not l2_spans:
        # No L2 headings, try L3
        l2_spans = [h for h in headings if h['level'] == 3]

    if not l2_spans:
        # Headingless-like, single chunk with oversize
        return [{
            'chunk_key': f"{dik}_ch001",
            'heading_range': {'first': headings[0]['heading_id'], 'last': headings[-1]['heading_id']} if headings else None,
            'heading_level': 'Document',
            'start_line': 1,
            'end_line': doc['total_lines'],
            'est_tokens': total_tokens,
            'split_method': 'headingless',
            'measure_method': 'tiktoken',
            'sub_chunks': None,
        }]

    # Split by L2 spans, grouping to target size
    n_chunks = math.ceil(total_tokens / CHUNK_MAX)
    target_per_chunk = total_tokens / n_chunks

    chunks = []
    current_spans = []
    current_tokens = 0
    chunk_idx = 1

    for span in l2_spans:
        span_tokens = span['tokens_inclusive']

        if current_spans and current_tokens + span_tokens > target_per_chunk * 1.3:
            # Close current chunk
            first_span = current_spans[0]
            last_span = current_spans[-1]
            chunks.append({
                'chunk_key': f"{dik}_ch{chunk_idx:03d}",
                'heading_range': {'first': first_span['heading_id'], 'last': last_span['heading_id']},
                'heading_level': 'Section',
                'start_line': first_span['start_line'],
                'end_line': last_span['end_line'],
                'est_tokens': current_tokens,
                'split_method': 'recursive',
                'measure_method': 'tiktoken',
                'sub_chunks': None,
            })
            chunk_idx += 1
            current_spans = []
            current_tokens = 0

        current_spans.append(span)
        current_tokens += span_tokens

    # Close last chunk
    if current_spans:
        first_span = current_spans[0]
        last_span = current_spans[-1]
        chunks.append({
            'chunk_key': f"{dik}_ch{chunk_idx:03d}",
            'heading_range': {'first': first_span['heading_id'], 'last': last_span['heading_id']},
            'heading_level': 'Section',
            'start_line': first_span['start_line'],
            'end_line': last_span['end_line'],
            'est_tokens': current_tokens,
            'split_method': 'recursive',
            'measure_method': 'tiktoken',
            'sub_chunks': None,
        })

    # Handle preamble (content before first L2)
    if headings and l2_spans:
        preamble_end = l2_spans[0]['start_line'] - 1
        if preamble_end > 0 and chunks:
            # Count preamble tokens from L1 exclusive
            l1_headings = [h for h in headings if h['level'] == 1]
            preamble_tokens = l1_headings[0]['tokens_exclusive'] if l1_headings else 0
            if preamble_tokens > 0:
                # Add preamble tokens to first chunk
                chunks[0]['start_line'] = 1
                chunks[0]['est_tokens'] += preamble_tokens

    # Merge undersized chunks (< WU_MIN)
    merged_chunks = []
    for ch in chunks:
        if merged_chunks and ch['est_tokens'] < WU_MIN and merged_chunks[-1]['est_tokens'] + ch['est_tokens'] <= CHUNK_MAX:
            # Merge with previous
            merged_chunks[-1]['end_line'] = ch['end_line']
            merged_chunks[-1]['est_tokens'] += ch['est_tokens']
            merged_chunks[-1]['heading_range']['last'] = ch['heading_range']['last']
        else:
            merged_chunks.append(ch)

    # Re-number
    for i, ch in enumerate(merged_chunks):
        ch['chunk_key'] = f"{dik}_ch{i+1:03d}"

    return merged_chunks

# ── Stage 6: WU Packing ──
def stage6_wu_packing(docs_with_chunks: list[dict]) -> list[dict]:
    """Pack chunks into Work Units."""
    wus = []
    merge_candidates = []

    for doc_info in docs_with_chunks:
        doc = doc_info['doc']
        chunks = doc_info['chunks']
        total_tokens = doc_info['total_tokens']

        if doc['is_deleted'] and total_tokens < 100:
            # Deleted/trivial documents → merge candidates
            merge_candidates.append(doc_info)
            continue

        if total_tokens > CHUNK_MAX:
            # Split WU — multiple chunks
            if len(chunks) > 1:
                for i, ch in enumerate(chunks):
                    wu_key = f"{doc['doc_instance_key']}_wu{i+1:03d}"
                    wus.append({
                        'wu_key': wu_key,
                        'wu_type': 'split',
                        'authority': 'IACS',
                        'doc_type': 'UR',
                        'language': 'en',
                        'grammar_version': 'v01',
                        'measure_method': 'tiktoken',
                        'constituent_docs': [{
                            'doc_instance_key': doc['doc_instance_key'],
                            'document_key': doc['doc_key'],
                            'start_line': ch['start_line'],
                            'end_line': ch['end_line'],
                            'est_tokens': ch['est_tokens'],
                            'heading_range': ch['heading_range'],
                        }],
                        'est_tokens_total': ch['est_tokens'],
                        'chunk_keys': [ch['chunk_key']],
                        'status': 'planned',
                        'output_files': [],
                        'created_at': datetime.now(timezone.utc).isoformat(),
                    })
            else:
                # Single chunk but oversize — still standalone
                wu_key = doc['doc_instance_key']
                wus.append({
                    'wu_key': wu_key,
                    'wu_type': 'standalone',
                    'authority': 'IACS',
                    'doc_type': 'UR',
                    'language': 'en',
                    'grammar_version': 'v01',
                    'measure_method': 'tiktoken',
                    'constituent_docs': [{
                        'doc_instance_key': doc['doc_instance_key'],
                        'document_key': doc['doc_key'],
                        'start_line': 1,
                        'end_line': doc['total_lines'],
                        'est_tokens': total_tokens,
                        'heading_range': chunks[0]['heading_range'] if chunks else None,
                    }],
                    'est_tokens_total': total_tokens,
                    'chunk_keys': [ch['chunk_key'] for ch in chunks],
                    'status': 'planned',
                    'output_files': [],
                    'created_at': datetime.now(timezone.utc).isoformat(),
                })
        elif total_tokens >= WU_MIN:
            # Standalone WU
            wu_key = doc['doc_instance_key']
            wus.append({
                'wu_key': wu_key,
                'wu_type': 'standalone',
                'authority': 'IACS',
                'doc_type': 'UR',
                'language': 'en',
                'grammar_version': 'v01',
                'measure_method': 'tiktoken',
                'constituent_docs': [{
                    'doc_instance_key': doc['doc_instance_key'],
                    'document_key': doc['doc_key'],
                    'start_line': 1,
                    'end_line': doc['total_lines'],
                    'est_tokens': total_tokens,
                    'heading_range': chunks[0]['heading_range'] if chunks else None,
                }],
                'est_tokens_total': total_tokens,
                'chunk_keys': [ch['chunk_key'] for ch in chunks],
                'status': 'planned',
                'output_files': [],
                'created_at': datetime.now(timezone.utc).isoformat(),
            })
        else:
            # Below WU_MIN → merge candidate
            merge_candidates.append(doc_info)

    # Process merge candidates
    if merge_candidates:
        # Sort by doc_key for deterministic ordering
        merge_candidates.sort(key=lambda x: x['doc']['doc_key'])

        current_merge = []
        current_tokens = 0

        for mc in merge_candidates:
            mc_tokens = mc['total_tokens']
            if current_merge and current_tokens + mc_tokens > CHUNK_MAX:
                # Close current merge WU
                _create_merge_wu(wus, current_merge, current_tokens)
                current_merge = []
                current_tokens = 0

            current_merge.append(mc)
            current_tokens += mc_tokens

        # Close last merge WU
        if current_merge:
            _create_merge_wu(wus, current_merge, current_tokens)

    return wus

def _create_merge_wu(wus: list, merge_group: list, total_tokens: int):
    """Create a merged WU from a group of small documents."""
    # Generate short hash
    keys_str = "|".join(m['doc']['doc_instance_key'] for m in merge_group)
    short_hash = hashlib.sha256(keys_str.encode()).hexdigest()[:8]
    wu_key = f"merge_{short_hash}"

    constituent_docs = []
    chunk_keys = []
    for m in merge_group:
        constituent_docs.append({
            'doc_instance_key': m['doc']['doc_instance_key'],
            'document_key': m['doc']['doc_key'],
            'start_line': 1,
            'end_line': m['doc']['total_lines'],
            'est_tokens': m['total_tokens'],
            'heading_range': m['chunks'][0]['heading_range'] if m['chunks'] else None,
        })
        chunk_keys.extend([ch['chunk_key'] for ch in m['chunks']])

    wus.append({
        'wu_key': wu_key,
        'wu_type': 'merged',
        'authority': 'IACS',
        'doc_type': 'UR',
        'language': 'en',
        'grammar_version': 'v01',
        'measure_method': 'tiktoken',
        'constituent_docs': constituent_docs,
        'est_tokens_total': total_tokens,
        'chunk_keys': chunk_keys,
        'status': 'planned',
        'output_files': [],
        'created_at': datetime.now(timezone.utc).isoformat(),
    })

# ── Stage 7: Issue Gate & Manifest ──
def stage7_issue_gate(wus: list[dict]) -> tuple[list[dict], list[dict]]:
    """Check for issues and generate manifest."""
    issues = []
    for wu in wus:
        tok = wu['est_tokens_total']
        if tok > CHUNK_EXCEPTION:
            issues.append({
                'wu_key': wu['wu_key'],
                'issue_type': 'oversize_hard',
                'severity': 'HIGH',
                'est_tokens': tok,
                'threshold': CHUNK_EXCEPTION,
                'message': f"WU tokens ({tok}) > 1.5× upper bound ({CHUNK_EXCEPTION})",
            })
        elif tok > CHUNK_MAX:
            issues.append({
                'wu_key': wu['wu_key'],
                'issue_type': 'oversize_exception',
                'severity': 'INFO',
                'est_tokens': tok,
                'threshold': CHUNK_MAX,
                'message': f"WU tokens ({tok}) > upper bound ({CHUNK_MAX}) but ≤ 1.5× — exception allowed",
            })
            wu['status'] = 'processed'
        elif tok < WU_MIN and wu['wu_type'] in ('standalone', 'split'):
            issues.append({
                'wu_key': wu['wu_key'],
                'issue_type': 'undersized',
                'severity': 'LOW',
                'est_tokens': tok,
                'threshold': WU_MIN,
                'message': f"WU tokens ({tok}) < lower bound ({WU_MIN})",
            })
            wu['status'] = 'processed'
        else:
            wu['status'] = 'processed'

    return issues, wus

def main():
    import tiktoken
    enc = tiktoken.get_encoding("cl100k_base")

    src_dir = SRC_DIR
    md_files = sorted([
        os.path.join(src_dir, f) for f in os.listdir(src_dir)
        if f.endswith('.md')
    ])

    print("=" * 80)
    print("md2wu Stage 4-7: Classification → Chunk → WU → Manifest")
    print("=" * 80)

    # Build doc info and load TSVs
    docs_with_data = []

    for fp in md_files:
        doc = build_doc_info(fp)
        dik = doc['doc_instance_key']

        # Find matching TSV (may have old key)
        tsv_candidates = [
            f for f in os.listdir(OUT_DIR)
            if f.startswith('doc-') and f.endswith('__heading__structure.tsv')
        ]

        # Match by Z number
        z_num = doc['doc_key']
        matched_tsv = None
        for tc in tsv_candidates:
            # Extract key from filename
            tc_key = tc.replace('doc-', '').replace('__heading__structure.tsv', '')
            if z_num in tc_key:
                matched_tsv = os.path.join(OUT_DIR, tc)
                break

        headings = []
        if matched_tsv and os.path.exists(matched_tsv):
            headings = parse_tsv(matched_tsv)

        # Compute total tokens
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()
        total_tokens = len(enc.encode(content))

        # Regenerate TSV with corrected doc_instance_key if needed
        if headings:
            # Update heading IDs to use corrected doc_key
            for idx, h in enumerate(headings):
                h['heading_id'] = f"{doc['doc_key']}_HD_{idx+1:03d}"
            # Reassign parent IDs
            stack = []
            for h in headings:
                while stack and stack[-1][0] >= h['level']:
                    stack.pop()
                h['parent_id'] = stack[-1][1] if stack else ''
                stack.append((h['level'], h['heading_id']))

            # Write corrected TSV
            tsv_path = os.path.join(OUT_DIR, f"doc-{dik}__heading__structure.tsv")
            with open(tsv_path, 'w', encoding='utf-8') as f:
                f.write("Heading_ID\tLevel\tStart_Line\tEnd_Line\tTitle\tParent_ID\tEst_Tokens_Inclusive\tEst_Tokens_Exclusive\n")
                for h in headings:
                    f.write(f"{h['heading_id']}\t{h['level']}\t{h['start_line']}\t{h['end_line']}\t"
                            f"{h['title']}\t{h['parent_id']}\t{h['tokens_inclusive']}\t{h['tokens_exclusive']}\n")

        docs_with_data.append({
            'doc': doc,
            'headings': headings,
            'total_tokens': total_tokens,
        })

    # ── Stage 4 ──
    print("\n── Stage 4: Classification ──")
    docs_list = [d['doc'] for d in docs_with_data]
    classification = stage4_classify(docs_list)
    class_path = os.path.join(OUT_DIR, "corpus__md2wu__classification_result.json")
    with open(class_path, 'w', encoding='utf-8') as f:
        json.dump(classification, f, indent=2, ensure_ascii=False)
    print(f"  Authority: {classification['authority']}")
    print(f"  DocType: {classification['doc_type']}")
    print(f"  Source Family: {classification['source_family']}")
    print(f"  Documents: {len(classification['documents'])}")
    print(f"  Output: {class_path}")

    # ── Stage 5 ──
    print("\n── Stage 5: Chunk Planning ──")
    docs_with_chunks = []
    for d in docs_with_data:
        chunks = stage5_chunk_plan(d['doc'], d['headings'], d['total_tokens'])
        docs_with_chunks.append({
            'doc': d['doc'],
            'headings': d['headings'],
            'chunks': chunks,
            'total_tokens': d['total_tokens'],
        })
        # Write chunk plan
        dik = d['doc']['doc_instance_key']
        chunk_path = os.path.join(OUT_DIR, f"doc-{dik}__heading__chunk_plan.json")
        with open(chunk_path, 'w', encoding='utf-8') as f:
            json.dump(chunks, f, indent=2, ensure_ascii=False)

        n_chunks = len(chunks)
        tag = "[DEL]" if d['doc']['is_deleted'] else ""
        print(f"  {dik:40s} | {d['total_tokens']:6d}tok | {n_chunks:2d} chunks {tag}")

    # ── Stage 6 ──
    print("\n── Stage 6: WU Packing ──")
    wus = stage6_wu_packing(docs_with_chunks)

    for wu in wus:
        wu_path = os.path.join(OUT_DIR, f"wu-{wu['wu_key']}__pre__meta.json")
        wu['output_files'].append(wu_path)
        with open(wu_path, 'w', encoding='utf-8') as f:
            json.dump(wu, f, indent=2, ensure_ascii=False)

    print(f"\n  WU Summary:")
    standalone = [w for w in wus if w['wu_type'] == 'standalone']
    split = [w for w in wus if w['wu_type'] == 'split']
    merged = [w for w in wus if w['wu_type'] == 'merged']
    print(f"    Standalone: {len(standalone)}")
    print(f"    Split: {len(split)} (from {len(set(w['constituent_docs'][0]['doc_instance_key'] for w in split))} docs)")
    print(f"    Merged: {len(merged)} (containing {sum(len(w['constituent_docs']) for w in merged)} docs)")
    print(f"    Total WUs: {len(wus)}")

    for wu in wus:
        doc_list = ", ".join(d['doc_instance_key'] for d in wu['constituent_docs'])
        print(f"    {wu['wu_key']:40s} | {wu['wu_type']:10s} | {wu['est_tokens_total']:6d}tok | {doc_list}")

    # ── Stage 7 ──
    print("\n── Stage 7: Issue Gate & Manifest ──")
    issues, wus = stage7_issue_gate(wus)

    if issues:
        print(f"\n  Issues found: {len(issues)}")
        issue_path = os.path.join(OUT_DIR, "corpus__md2wu__issue_gate_report.json")
        with open(issue_path, 'w', encoding='utf-8') as f:
            json.dump(issues, f, indent=2, ensure_ascii=False)
        for iss in issues:
            print(f"    [{iss['severity']}] {iss['wu_key']}: {iss['message']}")
    else:
        print("  No issues found.")

    # Generate manifest
    manifest = {
        'pipeline': 'md2wu',
        'source_dir': src_dir,
        'source_family': 'IACS UR/UI/Rec/PR',
        'authority': 'IACS',
        'doc_type': 'UR',
        'total_source_files': len(md_files),
        'total_documents': len(docs_with_data),
        'total_wus': len(wus),
        'wu_breakdown': {
            'standalone': len(standalone),
            'split': len(split),
            'merged': len(merged),
        },
        'issues': issues,
        'wus': [{
            'wu_key': w['wu_key'],
            'wu_type': w['wu_type'],
            'est_tokens_total': w['est_tokens_total'],
            'status': w['status'],
            'constituent_docs': [d['doc_instance_key'] for d in w['constituent_docs']],
            'chunk_keys': w['chunk_keys'],
        } for w in wus],
        'created_at': datetime.now(timezone.utc).isoformat(),
    }

    manifest_path = os.path.join(OUT_DIR, "corpus__pre__manifest.json")
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(f"\n  Manifest: {manifest_path}")

    # Source family report
    sf_report = f"""# Source Family Report — UR Z Series

## Detected Source Family
- **Source Family**: IACS UR/UI/Rec/PR
- **Authority**: IACS
- **DocType**: UR
- **User Approval**: Approved (2026-04-13)

## Detection Basis
- Path pattern: `UR/UR_Z_md/`
- L1 heading pattern: `Z{{N}}` or `Z{{N}}.{{N}}` + descriptive title
- Heading hierarchy: Document → Section → Subsection → Paragraph → Sub-paragraph
- All 35 files match existing IACS UR/UI/Rec/PR definition

## Token Statistics
- Total documents: {len(docs_with_data)}
- Total tokens: {sum(d['total_tokens'] for d in docs_with_data):,}
- Average: {sum(d['total_tokens'] for d in docs_with_data) // len(docs_with_data):,} tokens/doc
- Min: {min(d['total_tokens'] for d in docs_with_data):,} tokens
- Max: {max(d['total_tokens'] for d in docs_with_data):,} tokens
- Documents > 32K: {sum(1 for d in docs_with_data if d['total_tokens'] > CHUNK_MAX)}
- Documents < 16K: {sum(1 for d in docs_with_data if d['total_tokens'] < WU_MIN)}
"""
    sf_path = os.path.join(OUT_DIR, "corpus__md2wu__source_family_report.md")
    with open(sf_path, 'w', encoding='utf-8') as f:
        f.write(sf_report)

    # Re-write WU meta files with updated status
    for wu in wus:
        wu_path = os.path.join(OUT_DIR, f"wu-{wu['wu_key']}__pre__meta.json")
        with open(wu_path, 'w', encoding='utf-8') as f:
            json.dump(wu, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 80)
    print("PIPELINE COMPLETE")
    print("=" * 80)

if __name__ == '__main__':
    main()
