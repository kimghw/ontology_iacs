#!/usr/bin/env python3
"""PDF→MD 변환 정확도 비교 지표 산출."""
import re
import sys
from pathlib import Path
from collections import Counter

BASE = Path("/home/kimghw/ontology_iacs/UR/_compare/metrics")

def tokenize(text):
    # 영문/숫자 단어 단위 토큰 (lowercased)
    return re.findall(r"[A-Za-z][A-Za-z0-9]+", text.lower())

def count_structure(md):
    lines = md.splitlines()
    h1 = sum(1 for l in lines if re.match(r"^# [^#]", l))
    h2 = sum(1 for l in lines if re.match(r"^## [^#]", l))
    h3 = sum(1 for l in lines if re.match(r"^### [^#]", l))
    h4 = sum(1 for l in lines if re.match(r"^#### [^#]", l))
    tables = sum(1 for l in lines if re.match(r"^\|.*\|", l))
    img_links = len(re.findall(r"!\[[^\]]*\]\([^)]+\)", md))
    code_blocks = md.count("```") // 2
    math_inline = len(re.findall(r"(?<!\$)\$[^$\n]+\$(?!\$)", md))
    math_block = md.count("$$") // 2
    sub_tags = md.count("<sub>")
    sup_tags = md.count("<sup>")
    return {
        "lines": len(lines),
        "chars": len(md),
        "H1": h1, "H2": h2, "H3": h3, "H4": h4,
        "table_rows": tables,
        "img_links": img_links,
        "code_blocks": code_blocks,
        "math_inline": math_inline,
        "math_block": math_block,
        "sub_tags": sub_tags,
        "sup_tags": sup_tags,
    }

def coverage_vs_baseline(md_tokens, baseline_tokens):
    """baseline에 있는 토큰 중 md에도 등장하는 비율 (type 기준)."""
    bt = set(baseline_tokens)
    mt = set(md_tokens)
    intersect = bt & mt
    return {
        "baseline_unique_types": len(bt),
        "md_unique_types": len(mt),
        "intersect_types": len(intersect),
        "type_recall": len(intersect) / len(bt) if bt else 0,
    }

def token_count_ratio(md_tokens, baseline_tokens):
    """토큰 총량 비율 (md / baseline)."""
    bc = Counter(baseline_tokens)
    mc = Counter(md_tokens)
    # 공통 토큰에 대해 min/baseline 합산
    overlap = sum(min(mc[t], bc[t]) for t in bc)
    return {
        "baseline_total_tokens": sum(bc.values()),
        "md_total_tokens": sum(mc.values()),
        "overlap_tokens": overlap,
        "token_recall": overlap / sum(bc.values()) if bc else 0,
    }

def analyze(name, md_path, baseline_tokens):
    md = Path(md_path).read_text(encoding="utf-8", errors="replace")
    struct = count_structure(md)
    md_tokens = tokenize(md)
    cov = coverage_vs_baseline(md_tokens, baseline_tokens)
    tr = token_count_ratio(md_tokens, baseline_tokens)
    return {"name": name, "path": str(md_path), **struct, **cov, **tr}

def main():
    baseline_text = (BASE / "baseline.txt").read_text(encoding="utf-8", errors="replace")
    baseline_tokens = tokenize(baseline_text)

    groups = [
        ("50p  (6 workers, 6/6 success)", BASE / "merged_50p.md"),
        ("200p (2 workers, 1/2 part failed)", BASE / "merged_200p_PARTIAL.md"),
        ("260p (1 worker, failed mid-way)",  BASE / "merged_260p_PARTIAL.md"),
    ]

    results = [analyze(n, p, baseline_tokens) for n, p in groups]

    # 출력
    print("=" * 80)
    print("PDF→MD 변환 정확도 비교 (master_260p.pdf 기준)")
    print(f"baseline (pdftotext): {sum(Counter(baseline_tokens).values())} tokens, "
          f"{len(set(baseline_tokens))} unique types")
    print("=" * 80)

    headers = ["metric", "50p", "200p*", "260p*"]
    rows = []
    keys = ["lines", "chars", "H1", "H2", "H3", "H4",
            "table_rows", "img_links", "code_blocks",
            "math_inline", "math_block", "sub_tags", "sup_tags",
            "md_total_tokens", "md_unique_types",
            "overlap_tokens", "token_recall", "type_recall"]
    for k in keys:
        r = [k]
        for res in results:
            v = res[k]
            if isinstance(v, float):
                r.append(f"{v*100:.2f}%")
            else:
                r.append(f"{v:,}")
        rows.append(r)

    widths = [max(len(str(row[i])) for row in ([headers] + rows)) for i in range(len(headers))]
    def fmt(row):
        return "  ".join(str(c).rjust(widths[i]) for i, c in enumerate(row))
    print(fmt(headers))
    print("-" * (sum(widths) + 2 * (len(widths) - 1)))
    for r in rows:
        print(fmt(r))

    print()
    print("* 200p part01 (200p) worker가 단일 응답 한도 초과로 중단 → part02(60p)만 산출.")
    print("* 260p worker는 Request too large(>20MB) 도달 전까지만 변환 → 전체의 약 1/2 커버.")
    print()
    print("해석:")
    print("- token_recall: baseline(pdftotext) 토큰 중 MD에 포함된 비율. 100%에 가까울수록 무손실.")
    print("- type_recall : baseline 고유 단어 중 MD에 존재하는 비율. 어휘 커버리지.")

if __name__ == "__main__":
    main()
