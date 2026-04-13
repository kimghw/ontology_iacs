#!/usr/bin/env python3
"""Emit actual WU .md files from WU meta + source documents.
- Standalone/Split: extract line range from source
- Merged: concatenate multiple sources with separators
- Rename merge keys to include iacs_ur_ prefix
- Move meta JSONs to temp/pre, place .md in results/
"""

import os
import re
import json
import hashlib
import shutil

RESULTS = "/mnt/c/shared_wk/ontology_iacs/results"
TEMP_PRE = os.path.join(RESULTS, "temp", "pre")
SRC_DIR = "/home/kimghw/ontology_iacs/UR/UR_Z_md"

os.makedirs(TEMP_PRE, exist_ok=True)

# ── Load doc_instance_key → source file mapping ──
with open("/tmp/dik_mapping.json") as f:
    DIK_MAP = json.load(f)


def read_source_lines(doc_instance_key: str) -> list[str]:
    """Read source file lines for a doc_instance_key."""
    fp = DIK_MAP.get(doc_instance_key)
    if not fp or not os.path.exists(fp):
        print(f"  WARNING: source not found for {doc_instance_key}")
        return []
    with open(fp, "r", encoding="utf-8") as f:
        return f.readlines()


def extract_lines(lines: list[str], start: int, end: int) -> str:
    """Extract lines [start, end] (1-based inclusive)."""
    return "".join(lines[start - 1 : end])


def main():
    # Find all WU meta files
    wu_files = sorted([
        f for f in os.listdir(RESULTS)
        if f.startswith("wu-") and f.endswith("__pre__meta.json")
    ])

    print(f"Found {len(wu_files)} WU meta files")
    print("=" * 80)

    new_manifest_wus = []

    for wf in wu_files:
        wu_path = os.path.join(RESULTS, wf)
        with open(wu_path, "r", encoding="utf-8") as f:
            wu = json.load(f)

        old_key = wu["wu_key"]
        wu_type = wu["wu_type"]
        authority = wu.get("authority", "IACS").lower()
        doc_type = wu.get("doc_type", "UR").lower()

        # ── Compute new WU key ──
        if wu_type == "merged":
            # Add authority_doctype prefix
            keys_str = "|".join(d["doc_instance_key"] for d in wu["constituent_docs"])
            short_hash = hashlib.sha256(keys_str.encode()).hexdigest()[:8]
            new_key = f"{authority}_{doc_type}_merge_{short_hash}"
        else:
            # Standalone/Split: add authority_doctype prefix
            new_key = f"{authority}_{doc_type}_{old_key}"

        wu["wu_key"] = new_key

        # ── Generate WU .md content ──
        md_parts = []

        if wu_type == "merged":
            for doc in wu["constituent_docs"]:
                dik = doc["doc_instance_key"]
                lines = read_source_lines(dik)
                if lines:
                    content = extract_lines(lines, doc["start_line"], doc["end_line"])
                    md_parts.append(content)
                else:
                    md_parts.append(f"<!-- Source not found: {dik} -->\n")
        else:
            # Standalone or Split
            doc = wu["constituent_docs"][0]
            dik = doc["doc_instance_key"]
            lines = read_source_lines(dik)
            if lines:
                content = extract_lines(lines, doc["start_line"], doc["end_line"])
                md_parts.append(content)
            else:
                md_parts.append(f"<!-- Source not found: {dik} -->\n")

        # Write WU .md file
        md_filename = f"wu-{new_key}__pre__content.md"
        md_path = os.path.join(RESULTS, md_filename)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write("\n".join(md_parts))

        # Update meta with new key and output path
        wu["output_files"] = [md_path]
        new_meta_filename = f"wu-{new_key}__pre__meta.json"
        new_meta_path = os.path.join(TEMP_PRE, new_meta_filename)
        with open(new_meta_path, "w", encoding="utf-8") as f:
            json.dump(wu, f, indent=2, ensure_ascii=False)

        # Remove old meta from results/
        if os.path.exists(wu_path):
            os.remove(wu_path)

        doc_list = ", ".join(d["doc_instance_key"] for d in wu["constituent_docs"])
        print(f"  {new_key:50s} | {wu_type:10s} | {wu['est_tokens_total']:6d}tok")
        print(f"    → {md_filename}")
        print(f"    docs: {doc_list}")

        new_manifest_wus.append({
            "wu_key": new_key,
            "wu_type": wu_type,
            "est_tokens_total": wu["est_tokens_total"],
            "status": wu["status"],
            "constituent_docs": [d["doc_instance_key"] for d in wu["constituent_docs"]],
            "chunk_keys": wu["chunk_keys"],
            "content_file": md_filename,
        })

    # ── Update manifest ──
    manifest_path = os.path.join(RESULTS, "corpus__pre__manifest.json")
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    manifest["wus"] = new_manifest_wus
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 80)
    print(f"WU .md files: {len(new_manifest_wus)} → results/")
    print(f"WU meta JSONs: {len(new_manifest_wus)} → results/temp/pre/")
    print(f"Manifest updated: {manifest_path}")

    # Final listing
    print("\n=== results/ (최종 산출물) ===")
    for f in sorted(os.listdir(RESULTS)):
        if os.path.isfile(os.path.join(RESULTS, f)):
            size = os.path.getsize(os.path.join(RESULTS, f))
            print(f"  {size:>8d}  {f}")


if __name__ == "__main__":
    main()
