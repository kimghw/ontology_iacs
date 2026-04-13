#!/usr/bin/env python3
"""
Stage 1-2 of md2wu pipeline:
- Heading extraction (ignore headings inside code blocks)
- Token measurement using tiktoken cl100k_base
- Compute Est_Tokens_Inclusive and Est_Tokens_Exclusive
- Verify additivity
- Write TSV output
"""

import re
import sys
import os
import tiktoken

ENCODING = tiktoken.get_encoding("cl100k_base")

def slugify(text: str) -> str:
    """Apply slug rule: lowercase, replace spaces/hyphens/slashes/dots with _, remove non [a-z0-9_], collapse _, strip."""
    s = text.lower()
    s = re.sub(r'[ \-/\.]+', '_', s)
    s = re.sub(r'[^a-z0-9_]', '', s)
    s = re.sub(r'_+', '_', s)
    s = s.strip('_')
    return s

def count_tokens(text: str) -> int:
    return len(ENCODING.encode(text))

def extract_revision_from_filename(filename: str) -> str:
    """Extract revision from filename like ur-z25rev1.md -> rev1, ur-z29.md -> rev0, ur-z24corr1.md -> corr1"""
    base = os.path.splitext(os.path.basename(filename))[0]
    # Look for rev\d+
    m = re.search(r'rev(\d+)', base, re.IGNORECASE)
    if m:
        return f"rev{m.group(1)}"
    # Look for corr\d+
    m = re.search(r'corr(\d+)', base, re.IGNORECASE)
    if m:
        return f"corr{m.group(1)}"
    return "rev0"

def extract_document_key_from_heading(title: str) -> str:
    """
    Extract UR identifier from L1 heading title.
    E.g., 'UR Z25 Rev 1 ...' -> 'z25'
         'UR Z7.2 ...' -> 'z7_2'
         'Requirement Z21 ...' -> 'z21'
    """
    # Look for Z followed by number (and optional .number)
    m = re.search(r'\bZ(\d+(?:\.\d+)?)\b', title, re.IGNORECASE)
    if m:
        raw = m.group(0)  # e.g., Z25, Z7.2
        return slugify(raw)
    # Fallback: use slugified title words
    return slugify(title)[:20]

def parse_headings(lines: list[str]) -> list[dict]:
    """
    Parse markdown headings, ignoring those inside code blocks.
    Returns list of dicts: {level, line_no (1-based), title}
    """
    headings = []
    in_code_block = False
    for i, line in enumerate(lines, 1):
        # Detect code block boundaries (``` or ~~~)
        stripped = line.strip()
        if stripped.startswith('```') or stripped.startswith('~~~'):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        m = re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            headings.append({'level': level, 'line_no': i, 'title': title})
    return headings

def build_heading_rows(headings: list[dict], lines: list[str], doc_key: str) -> list[dict]:
    """
    Assign end lines, parent IDs, Heading_IDs, compute tokens.
    Returns list of row dicts matching TSV schema.
    """
    total_lines = len(lines)
    n = len(headings)
    rows = []

    # Assign end lines:
    # End_Line for heading[i] = last line before the next heading of SAME OR HIGHER level.
    # This ensures Inclusive tokens cover the full subtree under the heading.
    for i, h in enumerate(headings):
        end_line = total_lines  # default: extends to end of document
        for j in range(i + 1, n):
            if headings[j]['level'] <= h['level']:
                end_line = headings[j]['line_no'] - 1
                break
        h['end_line'] = end_line

    # Assign Heading_IDs
    for i, h in enumerate(headings):
        h['heading_id'] = f"{doc_key}_HD_{i+1:03d}"

    # Build parent stack: maintain stack of (level, heading_id)
    stack = []  # list of (level, heading_id)
    for h in headings:
        # Pop stack entries with level >= current level
        while stack and stack[-1][0] >= h['level']:
            stack.pop()
        if stack:
            h['parent_id'] = stack[-1][1]
        else:
            h['parent_id'] = ''
        stack.append((h['level'], h['heading_id']))

    # Compute token counts
    # For each heading, "its text" = lines[start-1 : end] (inclusive, 0-indexed)
    for h in headings:
        section_text = ''.join(lines[h['line_no']-1 : h['end_line']])
        h['tokens_inclusive'] = count_tokens(section_text)

    # Est_Tokens_Exclusive = Inclusive - sum of direct children's Inclusive
    # Build children mapping
    children_map = {h['heading_id']: [] for h in headings}
    for h in headings:
        if h['parent_id']:
            children_map[h['parent_id']].append(h['heading_id'])

    id_to_h = {h['heading_id']: h for h in headings}

    for h in headings:
        child_ids = children_map[h['heading_id']]
        children_inclusive_sum = sum(id_to_h[cid]['tokens_inclusive'] for cid in child_ids)
        h['tokens_exclusive'] = h['tokens_inclusive'] - children_inclusive_sum

    return headings

def verify_additivity(rows: list[dict]) -> list[str]:
    """Verify: parent.Exclusive + sum(children.Inclusive) == parent.Inclusive"""
    issues = []
    id_to_row = {r['heading_id']: r for r in rows}
    children_map = {r['heading_id']: [] for r in rows}
    for r in rows:
        if r['parent_id']:
            children_map[r['parent_id']].append(r['heading_id'])

    for r in rows:
        child_ids = children_map[r['heading_id']]
        if not child_ids:
            continue
        computed = r['tokens_exclusive'] + sum(id_to_row[cid]['tokens_inclusive'] for cid in child_ids)
        if computed != r['tokens_inclusive']:
            issues.append(f"  Additivity FAIL: {r['heading_id']} inclusive={r['tokens_inclusive']} exclusive={r['tokens_exclusive']} computed={computed}")
    return issues

def process_file(filepath: str, output_dir: str) -> dict:
    """Process a single markdown file. Returns summary dict."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.splitlines(keepends=True)

    filename = os.path.basename(filepath)
    revision = extract_revision_from_filename(filename)

    # Parse headings
    headings = parse_headings(lines)

    # Find L1 heading for document title and doc key
    l1_headings = [h for h in headings if h['level'] == 1]
    if l1_headings:
        doc_title = l1_headings[0]['title']
        doc_key = extract_document_key_from_heading(doc_title)
    else:
        # Fallback: use filename
        base = os.path.splitext(filename)[0]
        doc_title = base
        # Try to extract Z number from filename
        m = re.search(r'z(\d+(?:\.\d+)?)', base, re.IGNORECASE)
        if m:
            doc_key = slugify(f"Z{m.group(1)}")
        else:
            doc_key = slugify(base)

    doc_instance_key = f"{doc_key}_{revision}_en"

    # Build rows
    rows = build_heading_rows(headings, lines, doc_key)

    # Verify additivity
    issues = verify_additivity(rows)

    # Total tokens (full document)
    total_tokens = count_tokens(content)

    # Write TSV
    tsv_filename = f"doc-{doc_instance_key}__heading__structure.tsv"
    tsv_path = os.path.join(output_dir, tsv_filename)

    header = "Heading_ID\tLevel\tStart_Line\tEnd_Line\tTitle\tParent_ID\tEst_Tokens_Inclusive\tEst_Tokens_Exclusive"
    tsv_lines = [header]
    for r in rows:
        tsv_lines.append(
            f"{r['heading_id']}\t{r['level']}\t{r['line_no']}\t{r['end_line']}\t{r['title']}\t{r['parent_id']}\t{r['tokens_inclusive']}\t{r['tokens_exclusive']}"
        )

    with open(tsv_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(tsv_lines) + '\n')

    return {
        'filepath': filepath,
        'filename': filename,
        'doc_instance_key': doc_instance_key,
        'doc_title': doc_title,
        'doc_key': doc_key,
        'revision': revision,
        'heading_count': len(rows),
        'total_tokens': total_tokens,
        'tsv_path': tsv_path,
        'additivity_issues': issues,
    }

def main():
    src_dir = sys.argv[1] if len(sys.argv) > 1 else '/home/kimghw/ontology_iacs/UR/UR_Z_md'
    files = sorted([
        os.path.join(src_dir, f)
        for f in os.listdir(src_dir)
        if f.endswith('.md')
    ])
    output_dir = '/mnt/c/shared_wk/ontology_iacs/results'
    os.makedirs(output_dir, exist_ok=True)

    print("=" * 70)
    print("Stage 1-2: Heading Extraction + Token Measurement")
    print("=" * 70)

    summaries = []
    for fp in files:
        print(f"\nProcessing: {os.path.basename(fp)}")
        result = process_file(fp, output_dir)
        summaries.append(result)
        print(f"  doc_instance_key : {result['doc_instance_key']}")
        print(f"  doc_title        : {result['doc_title']}")
        print(f"  heading_count    : {result['heading_count']}")
        print(f"  total_tokens     : {result['total_tokens']}")
        print(f"  tsv_path         : {result['tsv_path']}")
        if result['additivity_issues']:
            print(f"  ADDITIVITY ISSUES:")
            for issue in result['additivity_issues']:
                print(issue)
        else:
            print(f"  additivity       : OK")

    print("\n" + "=" * 70)
    print("SUMMARY TABLE")
    print("=" * 70)
    print(f"{'doc_instance_key':<35} {'headings':>8} {'total_tokens':>12} {'issues':>6}")
    print("-" * 70)
    for r in summaries:
        issue_count = len(r['additivity_issues'])
        print(f"{r['doc_instance_key']:<35} {r['heading_count']:>8} {r['total_tokens']:>12} {issue_count:>6}")
    print("=" * 70)

if __name__ == '__main__':
    main()
