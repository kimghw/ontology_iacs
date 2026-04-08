#!/usr/bin/env python3
"""
update_thresholds.py — shared/thresholds.yaml의 값을 md 파일의 {{key:value}} 플레이스홀더에 반영.

사용법:
  python scripts/update_thresholds.py                    # 전체 대상 파일 갱신
  python scripts/update_thresholds.py --dry-run          # 변경 내용만 출력 (파일 수정 안 함)
  python scripts/update_thresholds.py --check            # 불일치 여부만 확인 (CI용, exit code 1 = 불일치)
  python scripts/update_thresholds.py path/to/file.md    # 특정 파일만 갱신

플레이스홀더 문법:
  {{key:current_value}}
  - key: thresholds.yaml의 키
  - current_value: 현재 md에 표시된 값 (스크립트가 yaml 값으로 교체)
"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML 필요: pip install pyyaml")
    sys.exit(1)

# ── 설정 ──────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
THRESHOLDS_PATH = PROJECT_ROOT / "shared" / "thresholds.yaml"

# 대상 md 파일 목록 (프로젝트 루트 기준 상대 경로)
DEFAULT_TARGETS = [
    "prerequisite/pre_specification.md",
    "prerequisite/pre_specification_ko.md",
    "prerequisite/step1_document_split.md",
    "prerequisite/step1_document_split_ko.md",
    "prerequisite/step2_heading_extraction.md",
    "prerequisite/step2_heading_extraction_ko.md",
    "prerequisite/step3_workunit_packing.md",
    "prerequisite/step3_workunit_packing_ko.md",
    "prerequisite/step3_chunking_packing.md",
    "prerequisite/step3_chunking_packing_ko.md",
    "shared/splitting_stages.md",
    "shared/splitting_stages_ko.md",
]

# {{key:value}} 패턴
PLACEHOLDER_RE = re.compile(r"\{\{([a-zA-Z_][a-zA-Z0-9_]*):([^}]*)\}\}")

# 인라인 코드 (`...`) 와 펜스 코드 블록 (```...```) — 매치 보호용
# 펜스를 먼저 매치하여 인라인 정규식이 펜스 내부를 잘못 잡지 않도록 한다.
CODE_SPAN_RE = re.compile(r"```.*?```|`[^`\n]*`", re.DOTALL)


def load_thresholds() -> dict:
    with open(THRESHOLDS_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return {k: str(v) for k, v in data.items()}


def update_content(content: str, thresholds: dict) -> tuple[str, list[dict]]:
    """플레이스홀더를 thresholds 값으로 교체. (변경된 내용, 변경 로그) 반환.

    인라인/펜스 코드 영역(`...`, ```...```)은 placeholder 치환에서 제외한다 (메타
    문장 보호). yaml에 정의되지 않은 키는 silent 무시 — 본문 예시가 잘못 치환되는
    것을 막기 위함.
    """
    changes = []

    # 코드 영역 위치를 미리 수집해 두고 매치가 그 안에 있으면 건너뛴다.
    code_spans = [(m.start(), m.end()) for m in CODE_SPAN_RE.finditer(content)]

    def in_code_span(pos: int) -> bool:
        for start, end in code_spans:
            if start <= pos < end:
                return True
        return False

    def replacer(m: re.Match) -> str:
        if in_code_span(m.start()):
            return m.group(0)
        key = m.group(1)
        old_val = m.group(2)
        if key not in thresholds:
            # yaml에 없는 키는 placeholder가 아닌 것으로 간주하고 그대로 둔다.
            return m.group(0)
        new_val = thresholds[key]
        if old_val != new_val:
            changes.append({"key": key, "old": old_val, "new": new_val, "status": "updated"})
        return f"{{{{{key}:{new_val}}}}}"

    result = PLACEHOLDER_RE.sub(replacer, content)
    return result, changes


def process_file(filepath: Path, thresholds: dict, dry_run: bool = False) -> list[dict]:
    """파일 하나 처리. 변경 로그 반환."""
    if not filepath.exists():
        return []

    content = filepath.read_text(encoding="utf-8")
    new_content, changes = update_content(content, thresholds)

    if changes and not dry_run:
        filepath.write_text(new_content, encoding="utf-8")

    return changes


def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    check_only = "--check" in args
    args = [a for a in args if not a.startswith("--")]

    thresholds = load_thresholds()

    if args:
        targets = [Path(a) for a in args]
    else:
        targets = [PROJECT_ROOT / t for t in DEFAULT_TARGETS]
        targets = [t for t in targets if t.exists()]

    if not targets:
        print("대상 파일 없음.")
        return

    total_changes = 0

    for filepath in targets:
        changes = process_file(filepath, thresholds, dry_run=dry_run or check_only)
        if changes:
            rel = filepath.relative_to(PROJECT_ROOT) if filepath.is_relative_to(PROJECT_ROOT) else filepath
            for c in changes:
                total_changes += 1
                action = "→" if not (dry_run or check_only) else "→ (예정)"
                print(f"  {rel}: {{{{{c['key']}}}}} {c['old']} {action} {c['new']}")

    mode = "[DRY-RUN]" if dry_run else "[CHECK]" if check_only else ""
    print(f"\n{mode} 파일 {len(targets)}개 스캔, {total_changes}건 변경")

    if check_only and total_changes > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
