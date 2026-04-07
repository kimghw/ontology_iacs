#!/usr/bin/env python3
"""Step 1.1–1.2: Split multi-document UR chunk file into individual documents,
generate per-file meta.json and corpus document manifest."""

import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone

import tiktoken

# ── Config ──
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RESULTS_DIR = os.path.join(ROOT, "results", "temp", "pre")
ENC = tiktoken.get_encoding("cl100k_base")

FILE_BOUNDARY_RE = re.compile(r"^# FILE:\s+(.+)$")

def slug(name: str) -> str:
    """DocumentKey slug rule (naming_convention.md)."""
    s = name.lower()
    s = re.sub(r"[\s\-/.]", "_", s)
    s = re.sub(r"[^a-z0-9_]", "", s)
    s = re.sub(r"_+", "_", s)
    return s.strip("_")


def parse_ur_filename(filepath: str):
    """Extract document info from UR filename like ur-a2rev5.md."""
    basename = os.path.splitext(os.path.basename(filepath))[0]
    # Normalise: lowercase, replace hyphens
    name = basename.lower()

    # Try to extract UR letter+number and revision
    # Patterns: ur-a2rev5, UR-E26-Rev.1-Nov-2023-CLN, UR-M56-Rev.4-Corr.3-Sep-2025-CLN
    m = re.match(r"ur[-_]?([a-z])(\d+)", name)
    if not m:
        return None, None, None, None

    letter = m.group(1).upper()
    number = m.group(2)
    doc_name = f"UR {letter}{number}"
    doc_key = slug(doc_name)  # e.g. ur_a2

    # Extract revision
    rev_match = re.search(r"rev\.?(\d+)", name)
    if rev_match:
        revision = f"rev{rev_match.group(1)}"
    else:
        # Check for corr only
        corr_match = re.search(r"corr\.?(\d+)", name)
        if corr_match:
            revision = f"corr{corr_match.group(1)}"
        else:
            # Check for "del" (deleted)
            if "del" in name:
                revision = "del"
            elif "new" in name:
                revision = "new"
            else:
                revision = "v1"

    doc_instance_key = f"{doc_key}_{revision}_en"
    return doc_name, doc_key, revision, doc_instance_key


def split_chunk_file(chunk_path: str):
    """Split a multi-document chunk file by '# FILE:' boundaries."""
    with open(chunk_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    documents = []
    current_doc = None

    for i, line in enumerate(lines, start=1):
        # Check for separator line pattern
        m = FILE_BOUNDARY_RE.match(line.strip())
        if m:
            if current_doc is not None:
                current_doc["end_line"] = i - 1
                # strip trailing separator lines
                while current_doc["lines"] and current_doc["lines"][-1].startswith("=" * 10):
                    current_doc["lines"].pop()
                    current_doc["end_line"] -= 1
                documents.append(current_doc)

            filepath = m.group(1).strip()
            current_doc = {
                "source_filepath": filepath,
                "start_line": i,
                "lines": [],
            }
            continue

        # Skip separator lines (=====)
        if line.strip().startswith("=" * 10):
            if current_doc is not None and not current_doc["lines"]:
                current_doc["start_line"] = i + 1
            continue

        if current_doc is not None:
            current_doc["lines"].append(line)

    # Last document
    if current_doc is not None:
        current_doc["end_line"] = len(lines)
        while current_doc["lines"] and current_doc["lines"][-1].strip() == "":
            current_doc["lines"].pop()
            current_doc["end_line"] -= 1
        documents.append(current_doc)

    return documents, lines


def process_chunk(chunk_path: str):
    """Main processing: split, generate meta, manifest."""
    print(f"Processing: {chunk_path}")
    source_file_key = slug(os.path.splitext(os.path.basename(chunk_path))[0])

    # Compute source hash
    with open(chunk_path, "rb") as f:
        source_hash = hashlib.sha256(f.read()).hexdigest()

    documents, all_lines = split_chunk_file(chunk_path)
    print(f"  Found {len(documents)} documents")

    # Generate file-level meta.json
    full_text = "".join(all_lines)
    file_meta = {
        "source_path": os.path.relpath(chunk_path, ROOT),
        "source_hash": source_hash,
        "source_format": "md",
        "parser": None,
        "parser_version": None,
        "line_ending": "LF",
        "char_count": len(full_text),
        "est_tokens": len(ENC.encode(full_text)),
        "token_method": "tiktoken",
        "grammar_version": None,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

    meta_path = os.path.join(RESULTS_DIR, f"file-{source_file_key}__pre__meta.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(file_meta, f, indent=2, ensure_ascii=False)
    print(f"  Written: {meta_path}")

    # Process each document
    manifest_entries = []
    seen_keys = {}

    for doc in documents:
        doc_name, doc_key, revision, doc_instance_key = parse_ur_filename(doc["source_filepath"])
        if doc_name is None:
            print(f"  WARNING: Could not parse filename: {doc['source_filepath']}")
            doc_key = slug(os.path.splitext(os.path.basename(doc["source_filepath"]))[0])
            doc_instance_key = f"{doc_key}_en"
            doc_name = doc_key
            revision = "unknown"

        # Handle duplicate keys by appending suffix
        if doc_instance_key in seen_keys:
            seen_keys[doc_instance_key] += 1
            doc_instance_key = f"{doc_instance_key}_{seen_keys[doc_instance_key]}"
        else:
            seen_keys[doc_instance_key] = 1

        # Write split file
        doc_text = "".join(doc["lines"])
        split_filename = f"doc-{doc_instance_key}__pre__split.md"
        split_path = os.path.join(RESULTS_DIR, split_filename)
        with open(split_path, "w", encoding="utf-8") as f:
            f.write(doc_text)

        # Token count
        est_tokens = len(ENC.encode(doc_text))

        # Manifest entry
        entry = {
            "doc_instance_key": doc_instance_key,
            "document_key": doc_key,
            "authority": "IACS",
            "doc_type": "UR",
            "revision": revision,
            "language": "en",
            "document_title": doc_name,
            "source_family": "IACS UR",
            "source_path": os.path.relpath(chunk_path, ROOT),
            "source_hash": source_hash,
            "document_split_path": os.path.relpath(split_path, ROOT),
            "normalised_path": None,
            "canonical_input_path": os.path.relpath(split_path, ROOT),
            "start_line_in_source": doc["start_line"],
            "end_line_in_source": doc["end_line"],
            "shared_front_matter_lines": 0,
            "discarded_boilerplate_lines": 0,
            "unassigned_lines": 0,
            "shared_back_matter_lines": 0,
            "est_tokens": est_tokens,
            "token_method": "tiktoken",
            "status": "confirmed",
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        manifest_entries.append(entry)

    # Write manifest
    manifest_path = os.path.join(RESULTS_DIR, "corpus__pre__document_manifest.jsonl")
    with open(manifest_path, "w", encoding="utf-8") as f:
        for entry in manifest_entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(f"  Written: {manifest_path} ({len(manifest_entries)} entries)")

    # Print summary
    total_tokens = sum(e["est_tokens"] for e in manifest_entries)
    print(f"\n  Summary:")
    print(f"    Documents: {len(manifest_entries)}")
    print(f"    Total tokens: {total_tokens:,}")
    print(f"    Avg tokens/doc: {total_tokens // len(manifest_entries):,}")

    # Small doc merge check
    small_docs = [e for e in manifest_entries if e["est_tokens"] < 32000]
    large_docs = [e for e in manifest_entries if e["est_tokens"] >= 32000]
    print(f"    Small docs (< 32K): {len(small_docs)}")
    print(f"    Large docs (>= 32K): {len(large_docs)}")

    return manifest_entries


if __name__ == "__main__":
    chunk_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        ROOT, "UR_MD", "UR_MD_chunks_5", "UR_chunk_01.md"
    )
    process_chunk(chunk_path)
