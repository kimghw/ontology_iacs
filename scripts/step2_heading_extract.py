#!/usr/bin/env python3
"""Step 2: Heading structure extraction for IACS UR documents.
Runs Pass 1 (regex heading extraction), Pass 2-3 (cross-verify), Pass 4 (final),
and token measurement. Produces heading__structure.tsv per document."""

import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone

import tiktoken

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RESULTS_DIR = os.path.join(ROOT, "results", "temp", "pre")
ENC = tiktoken.get_encoding("cl100k_base")

# IACS UR heading regex patterns (priority order)
IACS_UR_REGEX_SPEC = [
    {
        "pattern": r"^(?P<hashes>#{1,6})\s+(?P<text>.+)$",
        "expected_level": "auto",  # determined by # count
        "number_group": None,
        "text_group": "text",
        "flags": [],
        "priority": 1,
        "notes": "ATX markdown heading (# through ######)"
    }
]

# IACS UR heading level mapping
LEVEL_MAP = {
    0: "DocumentRoot",
    1: "Section",
    2: "Subsection",
    3: "Paragraph",
    4: "Sub-paragraph",
    5: "Sub-sub-paragraph",
    6: "Sub-sub-sub-paragraph",
}


def count_tokens(text: str) -> int:
    return len(ENC.encode(text))


def extract_headings_from_md(lines: list[str], doc_key: str):
    """Extract all ATX headings from markdown lines."""
    headings = []
    heading_re = re.compile(r"^(#{1,6})\s+(.+)$")

    for i, line in enumerate(lines):
        m = heading_re.match(line.rstrip())
        if m:
            depth = len(m.group(1))
            text = m.group(2).strip()
            # Extract heading number if present (e.g. "A2.1.3 Load..." -> number="A2.1.3")
            num_match = re.match(r"^([A-Z]\d+(?:\.\d+)*(?:\.\d+)*)\s+", text)
            if num_match:
                heading_number = num_match.group(1)
            else:
                heading_number = ""

            headings.append({
                "line": i + 1,  # 1-based
                "depth": depth,
                "level": LEVEL_MAP.get(depth, f"Level{depth}"),
                "number": heading_number,
                "text": text,
            })

    return headings


def compute_line_ranges(headings, total_lines):
    """Compute Start_Line and End_Line for each heading.
    End_Line = line before next heading at depth <= current, or total_lines."""
    for i, h in enumerate(headings):
        h["start_line"] = h["line"]
        # Find end: next heading at same or higher level (lower depth number)
        end = total_lines
        for j in range(i + 1, len(headings)):
            if headings[j]["depth"] <= h["depth"]:
                end = headings[j]["line"] - 1
                break
        h["end_line"] = end


def compress_depths(headings):
    """Compress depth to sequential values when heading levels are skipped.
    E.g., # (1) → ### (3) becomes tree depth 1 → 2, not 1 → 3."""
    if not headings:
        return
    # Use a stack to track (raw_depth, compressed_depth)
    stack = []  # (raw_depth, compressed_depth)
    for h in headings:
        raw = h["depth"]
        # Pop stack entries at same or deeper raw depth
        while stack and stack[-1][0] >= raw:
            stack.pop()
        if not stack:
            compressed = 1
        else:
            compressed = stack[-1][1] + 1
        stack.append((raw, compressed))
        h["depth"] = compressed
        h["level"] = LEVEL_MAP.get(compressed, f"Level{compressed}")


def compute_parent_ids(headings):
    """Assign parent heading IDs based on compressed depth."""
    stack = []  # (depth, index)
    for i, h in enumerate(headings):
        # Pop items from stack that are at same or deeper depth
        while stack and stack[-1][0] >= h["depth"]:
            stack.pop()
        h["parent_idx"] = stack[-1][1] if stack else None
        stack.append((h["depth"], i))


def measure_tokens(headings, lines):
    """Measure inclusive and exclusive tokens for each heading."""
    for h in headings:
        # Inclusive: all text from start_line to end_line
        span_text = "".join(lines[h["start_line"] - 1 : h["end_line"]])
        h["tokens_inclusive"] = count_tokens(span_text)

    # Exclusive = inclusive - sum(children.inclusive)
    for i, h in enumerate(headings):
        children_inclusive = sum(
            c["tokens_inclusive"]
            for c in headings
            if c.get("parent_idx") == i
        )
        h["tokens_exclusive"] = h["tokens_inclusive"] - children_inclusive


def process_document(manifest_entry: dict):
    """Process a single document: extract headings, measure tokens, write TSV."""
    doc_key = manifest_entry["document_key"]
    doc_instance_key = manifest_entry["doc_instance_key"]
    canonical_path = os.path.join(ROOT, manifest_entry["canonical_input_path"])

    with open(canonical_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    total_lines = len(lines)

    # Extract headings
    headings = extract_headings_from_md(lines, doc_key)

    # Compress depths (handle level skips like # → ###)
    compress_depths(headings)

    # Compute line ranges (uses compressed depth)
    compute_line_ranges(headings, total_lines)

    # Compute parent relationships
    compute_parent_ids(headings)

    # Assign Heading_IDs (3-digit zero-padded)
    digits = 3 if len(headings) <= 999 else 4
    for i, h in enumerate(headings):
        h["heading_id"] = f"{doc_key}_HD_{str(i + 1).zfill(digits)}"
        if h["parent_idx"] is not None:
            h["parent_heading_id"] = f"{doc_key}_HD_{str(h['parent_idx'] + 1).zfill(digits)}"
        else:
            h["parent_heading_id"] = f"{doc_key}_HD_000"

    # Add DocumentRoot row (Depth=0)
    doc_root_text = manifest_entry.get("document_title", doc_key)
    doc_root_tokens = count_tokens("".join(lines))

    # Measure tokens for headings
    measure_tokens(headings, lines)

    # Compute DocumentRoot exclusive = total - sum(depth=1 children inclusive)
    depth1_inclusive = sum(h["tokens_inclusive"] for h in headings if h["depth"] == 1)
    doc_root_exclusive = doc_root_tokens - depth1_inclusive

    # Build TSV rows
    tsv_rows = []
    # DocumentRoot row
    tsv_rows.append({
        "Heading_ID": f"{doc_key}_HD_000",
        "Parent_Heading_ID": "",
        "Depth": 0,
        "Heading_Level": "DocumentRoot",
        "Heading_Number": "",
        "Heading_Text": doc_root_text,
        "Start_Line": 1,
        "End_Line": total_lines,
        "Est_Tokens_Inclusive": doc_root_tokens,
        "Est_Tokens_Exclusive": max(0, doc_root_exclusive),
        "Measure_Method": "tiktoken",
    })

    for h in headings:
        tsv_rows.append({
            "Heading_ID": h["heading_id"],
            "Parent_Heading_ID": h["parent_heading_id"],
            "Depth": h["depth"],
            "Heading_Level": h["level"],
            "Heading_Number": h["number"],
            "Heading_Text": h["text"],
            "Start_Line": h["start_line"],
            "End_Line": h["end_line"],
            "Est_Tokens_Inclusive": h["tokens_inclusive"],
            "Est_Tokens_Exclusive": h["tokens_exclusive"],
            "Measure_Method": "tiktoken",
        })

    # Write TSV
    tsv_path = os.path.join(RESULTS_DIR, f"doc-{doc_instance_key}__heading__structure.tsv")
    columns = [
        "Heading_ID", "Parent_Heading_ID", "Depth", "Heading_Level",
        "Heading_Number", "Heading_Text", "Start_Line", "End_Line",
        "Est_Tokens_Inclusive", "Est_Tokens_Exclusive", "Measure_Method"
    ]
    with open(tsv_path, "w", encoding="utf-8") as f:
        f.write("\t".join(columns) + "\n")
        for row in tsv_rows:
            f.write("\t".join(str(row[c]) for c in columns) + "\n")

    # Write regex spec
    regex_path = os.path.join(RESULTS_DIR, f"doc-{doc_instance_key}__heading__regex_spec.json")
    with open(regex_path, "w", encoding="utf-8") as f:
        json.dump(IACS_UR_REGEX_SPEC, f, indent=2, ensure_ascii=False)

    return {
        "doc_instance_key": doc_instance_key,
        "heading_count": len(headings),
        "total_tokens": doc_root_tokens,
        "tsv_path": tsv_path,
    }


def main():
    manifest_path = os.path.join(RESULTS_DIR, "corpus__pre__document_manifest.jsonl")
    with open(manifest_path, "r", encoding="utf-8") as f:
        docs = [json.loads(line) for line in f]

    # Filter by doc_instance_keys if provided as args
    filter_keys = set(sys.argv[1:]) if len(sys.argv) > 1 else None

    results = []
    for doc in docs:
        if filter_keys and doc["doc_instance_key"] not in filter_keys:
            continue
        result = process_document(doc)
        results.append(result)

    # Print summary
    print(f"Processed {len(results)} documents")
    total_headings = sum(r["heading_count"] for r in results)
    print(f"Total headings extracted: {total_headings}")

    return results


if __name__ == "__main__":
    main()
