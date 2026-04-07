#!/usr/bin/env python3
"""Step 1.2 — Parse UR_chunk file, identify document boundaries, extract metadata,
split into individual files, and write document manifest."""

import json
import re
import hashlib
import os
from datetime import datetime, timezone
from pathlib import Path

# Paths
BASE = Path(__file__).resolve().parent.parent
CHUNK_PATH = BASE / "UR_MD" / "UR_MD_chunks_5" / "UR_chunk_01.md"
OUT_DIR = BASE / "results" / "temp" / "pre"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SEPARATOR_RE = re.compile(r'^={5,}$')
FILE_HEADER_RE = re.compile(r'^# FILE:\s*(.+)$')

# Patterns to extract UR document code from filename
# e.g. ur-a2rev5.md -> A2, rev5
# e.g. UR-E26-Rev.1-Nov-2023-CR.md -> E26, Rev.1
FILENAME_RE = re.compile(
    r'(?:ur|UR)[_-]?([A-Za-z]\d+)'      # doc code like A2, E26, M56
    r'(?:[_-]?(?:rev|Rev)\.?(\d+))?'     # optional revision
    r'(?:[_-]?(?:corr|Corr)\.?(\d+))?',  # optional corrigendum
    re.IGNORECASE
)

# More specific pattern for newer filename format: UR-E26-Rev.1-Nov-2023-CR.md
FILENAME_NEW_RE = re.compile(
    r'(?:ur|UR)[_-]?([A-Za-z]\d+)'
    r'(?:[_-]Rev\.?(\d+))?'
    r'(?:[_-]Corr\.?(\d+))?',
    re.IGNORECASE
)

def slug(text):
    """DocumentKey slug rule from naming_convention.md"""
    s = text.lower()
    s = re.sub(r'[\s\-/\.]', '_', s)
    s = re.sub(r'[^a-z0-9_]', '', s)
    s = re.sub(r'_+', '_', s)
    return s.strip('_')


def parse_filename(filepath_str):
    """Extract document code, revision, corrigendum from the FILE: header path."""
    basename = os.path.basename(filepath_str).replace('.md', '')

    # Check for 'del' (deleted) documents
    is_deleted = bool(re.search(r'del', basename, re.IGNORECASE))

    m = FILENAME_NEW_RE.search(basename) or FILENAME_RE.search(basename)
    if not m:
        return None, None, None, is_deleted

    doc_code = m.group(1).upper()  # e.g. A2, E26
    rev = m.group(2)  # e.g. 5, 1
    corr = m.group(3) if len(m.groups()) >= 3 else None

    # Build revision label
    rev_label = None
    if rev:
        rev_label = f"rev{rev}"
        if corr:
            rev_label += f"_corr{corr}"
    elif corr:
        rev_label = f"corr{corr}"

    # Try to also extract revision from more complex patterns
    if not rev:
        rev_m = re.search(r'rev\.?(\d+)', basename, re.IGNORECASE)
        if rev_m:
            rev = rev_m.group(1)
            rev_label = f"rev{rev}"
        corr_m = re.search(r'corr\.?(\d+)', basename, re.IGNORECASE)
        if corr_m:
            corr = corr_m.group(1)
            if rev_label:
                rev_label += f"_corr{corr}"
            else:
                rev_label = f"corr{corr}"

    return doc_code, rev_label, corr, is_deleted


def extract_document_title(lines):
    """Extract the first markdown heading from document content as title."""
    for line in lines[:20]:
        line = line.strip()
        if line.startswith('# ') and not line.startswith('# FILE:'):
            return line[2:].strip()
    return None


def main():
    with open(CHUNK_PATH, 'r', encoding='utf-8') as f:
        all_lines = f.readlines()

    total_lines = len(all_lines)

    # Find all document boundaries (lines with "# FILE: ...")
    boundaries = []
    i = 0
    while i < total_lines:
        line = all_lines[i].rstrip('\n')
        m = FILE_HEADER_RE.match(line)
        if m:
            # Separator line is typically 2 lines before (=== line then # FILE:)
            # Find the start of separator block
            sep_start = i
            for j in range(max(0, i - 3), i):
                if SEPARATOR_RE.match(all_lines[j].rstrip('\n')):
                    sep_start = j
                    break
            boundaries.append({
                'file_path': m.group(1).strip(),
                'header_line': i + 1,  # 1-based
                'sep_start_line': sep_start + 1,  # 1-based
                'content_start': None,  # will be set to line after === below header
            })
        i += 1

    # Determine content ranges
    for idx, b in enumerate(boundaries):
        # Content starts after the second === line (or after FILE header + === line)
        header_idx = b['header_line'] - 1  # 0-based
        # Look for closing === line after header
        content_start = header_idx + 1
        for j in range(header_idx + 1, min(header_idx + 3, total_lines)):
            if SEPARATOR_RE.match(all_lines[j].rstrip('\n')):
                content_start = j + 1
                break
        b['content_start'] = content_start + 1  # 1-based

        if idx + 1 < len(boundaries):
            b['content_end'] = boundaries[idx + 1]['sep_start_line'] - 1  # 1-based
        else:
            b['content_end'] = total_lines  # 1-based

    # Shared front matter: lines before first document boundary
    shared_front_matter_lines = boundaries[0]['sep_start_line'] - 1 if boundaries else 0

    # Boilerplate: separator lines for each document
    total_boilerplate = 0
    for b in boundaries:
        total_boilerplate += (b['content_start'] - b['sep_start_line'])

    print(f"Found {len(boundaries)} documents in {CHUNK_PATH.name}")
    print(f"Shared front matter: {shared_front_matter_lines} lines")
    print(f"Boilerplate (separators): {total_boilerplate} lines")

    # Process each document
    manifest_entries = []
    source_hash = "5c53ff87dce25f84b0ce88a6d9e9a19d54a14dd19af1899be03fc97901c810ec"
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    for idx, b in enumerate(boundaries):
        filepath = b['file_path']  # e.g. UR_A/ur-a2rev5.md
        doc_code, rev_label, corr, is_deleted = parse_filename(filepath)

        if not doc_code:
            print(f"  WARNING: Could not parse filename: {filepath}")
            continue

        # Build keys
        document_name = f"UR {doc_code}"
        document_key = slug(document_name)  # e.g. ur_a2

        # DocumentInstanceKey: doc_key + revision + language
        parts = [document_key]
        if rev_label:
            parts.append(rev_label)
        parts.append("en")
        doc_instance_key = "_".join(parts)

        # Extract content lines (0-based indexing)
        content_start_0 = b['content_start'] - 1
        content_end_0 = b['content_end']
        content_lines = all_lines[content_start_0:content_end_0]

        # Strip trailing empty lines
        while content_lines and content_lines[-1].strip() == '':
            content_lines.pop()

        title = extract_document_title(content_lines)
        if not title:
            title = document_name

        # Estimate tokens (chars / 4)
        content_text = ''.join(content_lines)
        char_count = len(content_text)
        est_tokens = char_count // 4

        # Write split file
        split_filename = f"doc-{doc_instance_key}__pre__split.md"
        split_path = OUT_DIR / split_filename
        with open(split_path, 'w', encoding='utf-8') as f:
            f.writelines(content_lines)

        # Manifest entry
        entry = {
            "doc_instance_key": doc_instance_key,
            "document_key": document_key,
            "authority": "IACS",
            "doc_type": "UR",
            "revision": rev_label if rev_label else "",
            "language": "en",
            "document_title": title,
            "source_family": "IACS UR",
            "source_path": f"UR_MD/UR_MD_chunks_5/UR_chunk_01.md",
            "source_hash": source_hash,
            "document_split_path": f"results/temp/pre/{split_filename}",
            "normalised_path": None,
            "canonical_input_path": f"results/temp/pre/{split_filename}",
            "start_line_in_source": b['content_start'],
            "end_line_in_source": b['content_end'],
            "shared_front_matter_lines": shared_front_matter_lines if idx == 0 else 0,
            "discarded_boilerplate_lines": b['content_start'] - b['sep_start_line'],
            "unassigned_lines": 0,
            "shared_back_matter_lines": 0,
            "est_tokens": est_tokens,
            "token_method": "char_approx",
            "status": "confirmed",
            "created_at": now,
        }
        manifest_entries.append(entry)

        status_tag = " [DELETED]" if is_deleted else ""
        print(f"  [{idx+1:3d}] {doc_instance_key} — L{b['content_start']}–{b['content_end']} ({char_count} chars){status_tag}")

    # Write manifest
    manifest_path = OUT_DIR / "corpus__pre__document_manifest.jsonl"
    with open(manifest_path, 'w', encoding='utf-8') as f:
        for entry in manifest_entries:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')

    print(f"\nManifest written: {manifest_path}")
    print(f"Split files written: {len(manifest_entries)} files in {OUT_DIR}")

    # Verification: account for all lines
    content_lines_total = sum(
        e['end_line_in_source'] - e['start_line_in_source'] + 1
        for e in manifest_entries
    )
    boilerplate_total = sum(e['discarded_boilerplate_lines'] for e in manifest_entries)
    accounted = shared_front_matter_lines + boilerplate_total + content_lines_total
    print(f"\nVerification: {shared_front_matter_lines} front + {boilerplate_total} boilerplate + {content_lines_total} content = {accounted} / {total_lines} total")
    if accounted != total_lines:
        print(f"  WARNING: {total_lines - accounted} lines unaccounted for!")
    else:
        print("  All lines accounted for.")


if __name__ == '__main__':
    main()
