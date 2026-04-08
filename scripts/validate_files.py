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
SCAN_DIRS = [PROJECT_ROOT / "prerequisite", PROJECT_ROOT / "shared"]
SCAN_EXT = {".md"}

# ── 추출 정규식 (명시적 컨텍스트만) ─────────────────────
RE_MD_LINK   = re.compile(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
RE_BACKTICK  = re.compile(r"`([^`\n]+)`")

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


def load_registry() -> dict:
    with REGISTRY_PATH.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    artifacts = list(data.get("artifacts", []))
    paths     = list(data.get("paths", []))
    docs      = list(data.get("docs", []))
    examples  = list(data.get("examples", []))
    # examples 는 artifact/doc 양쪽에서 매칭 가능하도록 docs 에 병합
    all_docs = docs + examples
    return {
        "artifacts_norm":  {normalize_placeholders(x) for x in artifacts},
        "paths_norm":      {normalize_placeholders(x) for x in paths},
        "docs_norm":       {normalize_placeholders(x) for x in all_docs},
        "artifacts_regex": [template_to_regex(x) for x in artifacts],
        "paths_regex":     [template_to_regex(x) for x in paths],
        "docs_regex":      [template_to_regex(x) for x in all_docs],
        "docs_basenames":  {normalize_placeholders(x).rsplit("/", 1)[-1] for x in all_docs},
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
    return missing


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
