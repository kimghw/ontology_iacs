#!/usr/bin/env python3
"""
filter_typo_report.py — LanguageTool 오탈자 리포트에서 False Positive 제거

사용법:
    python3 scripts/filter_typo_report.py <input_report.json> [--output <filtered.json>]
    python3 scripts/filter_typo_report.py <input_report.json> --summary

화이트리스트: shared/typo_whitelist.yaml (SSOT)

출력:
    --output 지정 시 필터링된 JSON 저장
    --summary 지정 시 통계만 출력 (기본: 둘 다)
"""
import argparse
import json
import re
import sys
from pathlib import Path

import yaml


def load_whitelist(whitelist_path: Path) -> dict:
    with open(whitelist_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_matchers(wl: dict) -> tuple[set[str], list[re.Pattern], set[str]]:
    """화이트리스트에서 exact 집합, pattern 리스트, ignored_rules 집합을 구축."""
    exact = set()
    patterns = []
    ignored_rules = set(wl.get("ignored_rules", []))

    for key, val in wl.items():
        if key == "ignored_rules":
            continue
        if not isinstance(val, dict):
            continue
        for word in val.get("exact", []):
            exact.add(str(word))
        for pat in val.get("pattern", []):
            patterns.append(re.compile(pat))

    return exact, patterns, ignored_rules


def is_whitelisted(entry: dict, exact: set, patterns: list, ignored_rules: set) -> bool:
    text = entry.get("text", "")
    rule = entry.get("rule", "")

    if rule in ignored_rules:
        return True
    if text in exact:
        return True
    for pat in patterns:
        if pat.search(text):
            return True
    return False


def main():
    parser = argparse.ArgumentParser(description="LanguageTool 오탈자 리포트 False Positive 필터")
    parser.add_argument("input", help="입력 리포트 JSON 경로")
    parser.add_argument("--output", "-o", help="필터링된 리포트 출력 경로 (미지정 시 _filtered 접미사)")
    parser.add_argument("--whitelist", "-w", default=None, help="화이트리스트 YAML 경로 (기본: shared/typo_whitelist.yaml)")
    parser.add_argument("--summary", "-s", action="store_true", help="통계만 출력")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"ERROR: {input_path} 파일을 찾을 수 없습니다.", file=sys.stderr)
        sys.exit(1)

    # 화이트리스트 경로 결정
    if args.whitelist:
        wl_path = Path(args.whitelist)
    else:
        wl_path = Path(__file__).resolve().parent.parent / "shared" / "typo_whitelist.yaml"

    if not wl_path.exists():
        print(f"ERROR: 화이트리스트 {wl_path} 를 찾을 수 없습니다.", file=sys.stderr)
        sys.exit(1)

    # 로드
    wl = load_whitelist(wl_path)
    exact, patterns, ignored_rules = build_matchers(wl)

    with open(input_path, encoding="utf-8") as f:
        report = json.load(f)

    original = report.get("manual_review", [])
    auto_fixed = report.get("auto_fixed", [])

    # 필터링
    kept = []
    removed = []
    for entry in original:
        if is_whitelisted(entry, exact, patterns, ignored_rules):
            removed.append(entry)
        else:
            kept.append(entry)

    # 통계
    print(f"=== 오탈자 리포트 필터링 결과 ===")
    print(f"  원본 manual_review: {len(original)}건")
    print(f"  제거 (False Positive): {len(removed)}건")
    print(f"  잔여 (검토 필요):     {len(kept)}건")
    print(f"  auto_fixed:           {len(auto_fixed)}건 (변경 없음)")

    if removed:
        # 제거 사유 통계
        from collections import Counter
        rule_counts = Counter(e["rule"] for e in removed)
        print(f"\n  === 제거 사유 (룰별) ===")
        for rule, cnt in rule_counts.most_common(10):
            print(f"    {rule}: {cnt}건")

    if args.summary:
        return

    # 출력
    if args.output:
        out_path = Path(args.output)
    else:
        out_path = input_path.with_name(input_path.stem + "_filtered.json")

    filtered_report = {
        "auto_fixed": auto_fixed,
        "manual_review": kept,
        "_filter_meta": {
            "original_count": len(original),
            "removed_count": len(removed),
            "whitelist": str(wl_path),
        },
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(filtered_report, f, ensure_ascii=False, indent=2)

    print(f"\n  필터링 결과 저장: {out_path}")


if __name__ == "__main__":
    main()
