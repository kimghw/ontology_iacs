#!/usr/bin/env python3
# ruff: noqa: W605
r"""
validate_files.py — 문서 내 파일명·경로가 shared/files_registry.yaml 에 등록되어 있는지 검증.

SSOT 원칙: 모든 산출물 파일명·저장 경로·참조 문서는 shared/files_registry.yaml 한 곳에서 정의한다.
이 스크립트는 prerequisite/ 와 shared/ 디렉토리의 md 파일을 스캔하여 registry에 없는 파일·경로
참조가 있는지 확인한다. (등록 확인만 수행 — 파일 실제 존재 여부는 검증하지 않는다.)

사용법:
  python scripts/validate_files.py              # 전체 검증 (미등록 발견 시 exit 1)
  python scripts/validate_files.py --verbose    # 매칭된 항목도 모두 출력
  python scripts/validate_files.py path/to/x.md # 특정 파일만 검증

추출 대상 (명시적 컨텍스트만):
  - 마크다운 링크 타겟: `](target)` — 내부 상대경로만 (http/# 제외)
  - 인라인 코드: `` `token` `` — 파일 확장자를 가진 토큰만
  (산문 본문의 partial mention 은 과검출을 피하기 위해 스캔하지 않는다)

분류:
  - artifact : 토큰에 `__` 3-part 패턴이 포함되고 확장자가 있음
  - path     : `/` 로 끝나거나 디렉토리 형태
  - doc      : 파일명/상대경로

매칭 규칙:
  - 레지스트리 항목의 `{placeholder}` 는 임의의 `[A-Za-z0-9_\-]+` 세그먼트와 매칭된다
    (예: `doc-{doc_instance_key}__pre__split.md` ↔ `doc-ur_a2_rev5_en__pre__split.md`)
  - path 의 경우 후보가 레지스트리 경로의 prefix 인지도 함께 확인
  - doc 은 경로 prefix 유무와 basename 모두 허용
"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML 필요: pip install pyyaml")
    sys.exit(1)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = PROJECT_ROOT / "shared" / "files_registry.yaml"
THRESHOLDS_PATH = PROJECT_ROOT / "shared" / "thresholds.yaml"
SCAN_DIRS = [PROJECT_ROOT / "prerequisite", PROJECT_ROOT / "shared"]
SCAN_EXT = {".md"}

# ── 추출 정규식 (명시적 컨텍스트만) ─────────────────────
RE_MD_LINK   = re.compile(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
RE_BACKTICK  = re.compile(r"`([^`\n]+)`")

# `[A05]` 또는 `**[A05]**` 다음에 백틱 파일명 또는 마크다운 링크가 오는 페어
# 예: **[A05]** `doc-...tsv`  /  **[D02]** [pre_specification_ko.md](...)
RE_ID_PAIR = re.compile(
    r"\*{0,2}\[([ADP]\d{2,})\]\*{0,2}"   # [A05] 또는 **[A05]**
    r"\s*"
    r"(?:`([^`\n]+)`"                     # 백틱 파일명
    r"|\[[^\]]+\]\(([^)\s]+)\))"          # 또는 [text](target)
)

# 임계값 참조: `{{key:value}}` 형식 (key 만 캡처). value 는 update_thresholds.py 가 동기화.
RE_THRESHOLD_REF = re.compile(r"\{\{([a-z][a-z0-9_]*)\s*:[^}]*\}\}")

# 코드 영역 (인라인 / 펜스) — 임계값 참조 검증 시 제외 (update_thresholds.py 와 동일 정책)
RE_CODE_SPAN = re.compile(r"```.*?```|`[^`\n]*`", re.DOTALL)

# 파일스러운 토큰인지 판단
RE_FILEISH   = re.compile(r"\.[A-Za-z0-9]{1,8}(/)?$|/$")
# 확장자 리스트
FILE_EXT = {"md", "yaml", "yml", "py", "json", "jsonl", "tsv", "pdf", "html", "xml"}

# 외부 링크/앵커/섹션 링크는 스킵
SKIP_PREFIX = ("http://", "https://", "mailto:", "#")


def normalize_placeholders(token: str) -> str:
    """`{anything}` → `{}` 통일, 인접 placeholder(`{}_s{}`) 는 단일 `{}` 로 축약.

    축약은 문서에서 `{...}` 같은 약식 placeholder 를 registry 의 완전한 템플릿
    (`{doc_instance_key}_s{NNN}`) 과 매칭시키기 위함.
    """
    s = re.sub(r"\{[^{}]*\}", "{}", token)
    # 인접 placeholder: `{}_s{}`, `{}_{}` 등 short linker 로 연결된 경우 한 번에 축약
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r"\{\}[A-Za-z0-9_\-]{0,6}\{\}", "{}", s)
    return s


def template_to_regex(template: str) -> re.Pattern:
    r"""레지스트리 템플릿을 인스턴스 매칭용 regex 로 변환.

    `{placeholder}` → `[A-Za-z0-9_\-]+` 로 바꾸고 나머지는 리터럴 이스케이프.
    """
    parts = re.split(r"(\{[^{}]*\})", template)
    out = []
    for p in parts:
        if p.startswith("{") and p.endswith("}"):
            out.append(r"[A-Za-z0-9_\-]+")
        else:
            out.append(re.escape(p))
    return re.compile(r"\A" + "".join(out) + r"\Z")


def _values(section) -> list:
    """artifacts/paths/docs 섹션을 리스트로 정규화. dict({ID: 템플릿}) 또는 list 둘 다 허용."""
    if section is None:
        return []
    if isinstance(section, dict):
        return list(section.values())
    return list(section)


def load_registry() -> dict:
    with REGISTRY_PATH.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    artifacts_map = data.get("artifacts") or {}
    paths_map     = data.get("paths") or {}
    docs_map      = data.get("docs") or {}
    artifacts = _values(artifacts_map)
    paths     = _values(paths_map)
    docs      = _values(docs_map)
    examples  = list(data.get("examples", []))
    # examples 는 artifact/doc 양쪽에서 매칭 가능하도록 docs 에 병합
    all_docs = docs + examples

    # ID → 정규화 템플릿 매핑 ([A05]/[P01]/[D02] 검증용)
    id_to_norm: dict[str, str] = {}
    if isinstance(artifacts_map, dict):
        for k, v in artifacts_map.items():
            id_to_norm[k] = normalize_placeholders(v)
    if isinstance(paths_map, dict):
        for k, v in paths_map.items():
            id_to_norm[k] = normalize_placeholders(v)
    if isinstance(docs_map, dict):
        for k, v in docs_map.items():
            id_to_norm[k] = normalize_placeholders(v)

    # 임계값 키 로드 (`**[key]**` 참조 검증용)
    threshold_keys: set[str] = set()
    if THRESHOLDS_PATH.exists():
        with THRESHOLDS_PATH.open(encoding="utf-8") as f:
            tdata = yaml.safe_load(f) or {}
        if isinstance(tdata, dict):
            threshold_keys = {str(k) for k in tdata.keys()}

    return {
        "artifacts_norm":  {normalize_placeholders(x) for x in artifacts},
        "paths_norm":      {normalize_placeholders(x) for x in paths},
        "docs_norm":       {normalize_placeholders(x) for x in all_docs},
        "artifacts_regex": [template_to_regex(x) for x in artifacts],
        "paths_regex":     [template_to_regex(x) for x in paths],
        "docs_regex":      [template_to_regex(x) for x in all_docs],
        "docs_basenames":  {normalize_placeholders(x).rsplit("/", 1)[-1] for x in all_docs},
        "id_to_norm":      id_to_norm,
        "threshold_keys":  threshold_keys,
    }


SCOPE_PREFIX = ("file-", "doc-", "doctype-", "wu-", "corpus", "documentSplit-")


def classify(token: str) -> str | None:
    """토큰을 artifact/path/doc 으로 분류. 해당 없음이면 None.

    - 확장자만 있는 토큰(`.md`, `.json`) → None (확장자 예시)
    - `/` 로 끝 → path
    - 3-part artifact 패턴(`__` 2회 이상) → artifact
    - 경로 prefix 가 있거나(`shared/x.md`) 정확한 docs 매칭 가능 → doc
    - 단순 basename(path prefix·`__`·scope prefix 모두 없음) → None (산문 약식)
    """
    if not token or token.startswith(SKIP_PREFIX):
        return None
    clean = token.split("#", 1)[0]
    if not clean:
        return None
    if clean.endswith("/"):
        return "path"
    base = clean.rsplit("/", 1)[-1]
    # 확장자만 있는 토큰 (base == ".md")
    if base.startswith(".") and base.count(".") == 1:
        return None
    if "." not in base:
        return None
    ext = base.rsplit(".", 1)[-1].lower()
    if ext not in FILE_EXT:
        return None
    # 3-part artifact pattern
    if base.count("__") >= 2:
        return "artifact"
    # 경로 prefix 또는 scope prefix 가 있으면 명시적 참조로 간주
    if "/" in clean:
        return "doc"
    if any(base.startswith(p) for p in SCOPE_PREFIX):
        return "doc"
    # 그 외 단순 basename 은 산문 약식으로 간주하고 스킵
    return None


def extract_candidates(text: str) -> list[str]:
    tokens: list[str] = []
    for m in RE_MD_LINK.finditer(text):
        tokens.append(m.group(1))
    for m in RE_BACKTICK.finditer(text):
        tok = m.group(1).strip()
        # 인라인 코드는 파일스러운 경우만
        if "/" in tok or re.search(r"\.[A-Za-z0-9]{1,8}\Z", tok) or tok.endswith("/"):
            tokens.append(tok)
    return tokens


def strip_relative(token: str) -> str:
    """`../shared/x.md` → `shared/x.md`, `./x` → `x`."""
    t = token
    while t.startswith("../"):
        t = t[3:]
    if t.startswith("./"):
        t = t[2:]
    return t


def is_registered(category: str, token: str, registry: dict) -> bool:
    # 앵커/쿼리 제거 후 정규화
    clean = strip_relative(token.split("#", 1)[0])
    norm = normalize_placeholders(clean)

    if category == "artifact":
        if norm in registry["artifacts_norm"]:
            return True
        base = norm.rsplit("/", 1)[-1]
        if base in {x.rsplit("/", 1)[-1] for x in registry["artifacts_norm"]}:
            return True
        # 템플릿 인스턴스 매칭 (basename)
        return any(rx.match(base) for rx in registry["artifacts_regex"])

    if category == "path":
        # 정확 매칭
        if norm in registry["paths_norm"]:
            return True
        # 템플릿 인스턴스 매칭
        if any(rx.match(norm) for rx in registry["paths_regex"]):
            return True
        # prefix 매칭 (레지스트리 경로의 하위 디렉토리 허용)
        for p in registry["paths_norm"]:
            if norm.startswith(p):
                return True
        return False

    if category == "doc":
        if norm in registry["docs_norm"]:
            return True
        base = norm.rsplit("/", 1)[-1]
        if base in registry["docs_basenames"]:
            return True
        return any(rx.match(norm) or rx.match(base) for rx in registry["docs_regex"])

    return False


def _rel(path: Path) -> Path:
    try:
        return path.relative_to(PROJECT_ROOT)
    except ValueError:
        return path


def scan_id_pairs(path: Path, text: str, registry: dict, verbose: bool) -> list[str]:
    """`[ID] filename` 페어의 ID와 파일명이 registry와 일치하는지 확인."""
    mismatches: list[str] = []
    id_to_norm = registry["id_to_norm"]
    rel = _rel(path)
    for lineno, line in enumerate(text.splitlines(), 1):
        for m in RE_ID_PAIR.finditer(line):
            ref_id = m.group(1)
            token = m.group(2) or m.group(3) or ""
            if not token:
                continue
            actual_norm = normalize_placeholders(strip_relative(token.split("#", 1)[0]))
            expected_norm = id_to_norm.get(ref_id)
            if expected_norm is None:
                mismatches.append(f"{rel}:{lineno}  [{ref_id}] 미등록 ID — registry에 없음")
                continue
            # basename 비교 (registry가 경로 prefix를 포함하는 경우 허용)
            actual_base = actual_norm.rsplit("/", 1)[-1]
            expected_base = expected_norm.rsplit("/", 1)[-1]
            if actual_norm == expected_norm or actual_base == expected_base:
                if verbose:
                    print(f"  OK   [id-pair] {rel}:{lineno}  [{ref_id}] {token}")
                continue
            mismatches.append(
                f"{rel}:{lineno}  [{ref_id}] 파일명 불일치 — 본문={token!r}, registry={expected_norm!r}"
            )
    return mismatches


def scan_file(path: Path, registry: dict, verbose: bool) -> list[str]:
    text = path.read_text(encoding="utf-8")
    missing: list[str] = []
    seen: set[tuple[str, str]] = set()
    for lineno, line in enumerate(text.splitlines(), 1):
        for token in extract_candidates(line):
            category = classify(token)
            if category is None:
                continue
            key = (category, normalize_placeholders(strip_relative(token.split("#", 1)[0])))
            if key in seen:
                continue
            seen.add(key)
            if is_registered(category, token, registry):
                if verbose:
                    rel = _rel(path)
                    print(f"  OK   [{category:8s}] {rel}:{lineno}  {token}")
                continue
            rel = _rel(path)
            missing.append(f"{rel}:{lineno}  [{category}] {token}")
    # ID↔파일명 페어 검증
    missing.extend(scan_id_pairs(path, text, registry, verbose))
    # 임계값 키 참조 검증
    missing.extend(scan_threshold_refs(path, text, registry, verbose))
    return missing


def scan_threshold_refs(path: Path, text: str, registry: dict, verbose: bool) -> list[str]:
    """`{{key:value}}` 참조의 key가 thresholds.yaml에 등록된 키인지 확인.

    코드 영역(`...`, ```...```) 안의 placeholder 는 제외 — update_thresholds.py
    가 동일 정책으로 치환을 건너뛰므로 (메타 예시 보호) validator 도 같이 무시한다.
    """
    mismatches: list[str] = []
    keys = registry["threshold_keys"]
    rel = _rel(path)
    code_spans = [(m.start(), m.end()) for m in RE_CODE_SPAN.finditer(text)]

    def in_code_span(pos: int) -> bool:
        return any(s <= pos < e for s, e in code_spans)

    for m in RE_THRESHOLD_REF.finditer(text):
        if in_code_span(m.start()):
            continue
        lineno = text.count("\n", 0, m.start()) + 1
        key = m.group(1)
        if key in keys:
            if verbose:
                print(f"  OK   [threshold] {rel}:{lineno}  {{{{{key}:...}}}}")
            continue
        mismatches.append(f"{rel}:{lineno}  {{{{{key}:...}}}} 미등록 임계값 키 — thresholds.yaml에 없음")
    return mismatches


def main() -> int:
    args = sys.argv[1:]
    verbose = "--verbose" in args
    args = [a for a in args if a != "--verbose"]

    registry = load_registry()

    if args:
        targets = [Path(a).resolve() for a in args]
    else:
        targets = []
        for d in SCAN_DIRS:
            targets.extend(sorted(p for p in d.rglob("*") if p.suffix in SCAN_EXT))

    all_missing: list[str] = []
    for t in targets:
        if not t.exists() or t.suffix not in SCAN_EXT:
            continue
        missing = scan_file(t, registry, verbose)
        all_missing.extend(missing)

    if all_missing:
        print("=== 미등록 파일/경로 참조 ===")
        for m in all_missing:
            print("  " + m)
        print(f"\n총 {len(all_missing)}건 미등록. shared/files_registry.yaml 에 추가하거나 문서를 수정하세요.")
        return 1

    print(f"OK — {len(targets)}개 파일 스캔, 모든 참조가 registry에 등록되어 있습니다.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
