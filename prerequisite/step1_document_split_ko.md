# Step 1 — Document 식별, 분할, 정규화

> **정합 기준.** 이 문서를 수정할 때는 반드시 [pre_specification.md](pre_specification.md)에 부합해야 한다. 단계 번호, 산출물 번호, 워크플로우 순서 등이 상위 명세와 일치하는지 확인할 것.

> **목적.** 대상 파일을 읽고, 독립적인 Document 단위를 식별하며, 필요 시 다중 문서 파일을 분할하고, 모든 입력을 일관된 정규화 형식으로 변환한다. 이를 통해 제목 추출(Step 2.1)을 위한 입력을 준비한다.

---

## 1.0 작업 명세서

### 목적

대상 파일을 읽고, 독립적인 Document 단위를 식별하며, 필요 시 다중 문서 파일을 분할하고, 모든 입력을 일관된 정규화 형식으로 변환한다. 이를 통해 제목 추출(Step 2)을 위한 입력을 준비한다.

### 입력

- 대상 문서 (사용자 제공: 단일 파일, 복수 파일, 또는 폴더)
- 공통 정의서 (`shared/` 디렉토리)
- (선택) 특별 지시

### 작업 절차

| 순서 | 단계 | 작업 | 입력 | 출력 |
|:---:|:---|:---|:---|:---|
| 1 | Step 1.0 | 사용자 요청 확인 | 사용자 입력 (파일/폴더/특별 지시) | 확정된 대상 파일 목록 |
| 2 | Step 1.1 | 입력 정규화 | 대상 파일 목록 | 정규화된 `.md` + `meta.json` |
| 3 | Step 1.2.0 | 소스 패밀리 탐지 | 파일명, 경로, 내부 메타데이터 | Source Family 판별 |
| 4 | Step 1.2 | Document 식별 및 분할 | 정규 입력 파일 + Source Family | Document 목록 + split 파일 |
| 5 | Step 1.2.2 | 소규모 인접 문서 병합 | Document 목록 + 토큰 추정 | 병합된 처리 단위 (≤ {{merge_threshold:32K}}) |
| 6 | — | 매니페스트 작성 | 확정된 Document 목록 | `corpus__pre__document_manifest.jsonl` |

### 최종 산출물

> 파일 명명 규칙과 전체 산출물 카탈로그는 [pre_specification_ko.md](pre_specification_ko.md) §파일 명명 규칙 및 §산출물 카탈로그를 참조한다.

- `file-{source_file_key}__pre__meta.json` — 파일 메타데이터 (원본 입력 파일 단위) ← #3
- `file-{source_file_key}__pre__normalised.md` — 정규화된 텍스트 (비`.md` 형식, 원본 입력 파일 단위) ← #4
- `corpus__pre__document_manifest.jsonl` — 영구 문서별 레지스트리 ← #7a
- `doc-{doc_instance_key}__pre__split.md` — Document별 분할본 (다중 문서 파일만 해당) ← #4a

### 완료 기준

- 모든 대상 파일에 대해 `meta.json`이 생성되었다
- 다중 문서 파일에서 모든 Document가 식별·분할되었다
- `unassigned_lines = 0` 이거나 사용자에게 에스컬레이션되었다
- `corpus__pre__document_manifest.jsonl`이 생성되어 Stage 2에서 소비 가능하다
- 소규모 문서 병합(§1.2.2)이 적용되었다

### 다음 단계

→ Step 2: Heading Structure Extraction (`step2_heading_extraction.md`)

---

## Step 1.0 — 사용자 요청 확인

사용자가 대상 문서 경로(파일 또는 폴더)를 제공했는지 확인한다. 누락 시 요청한다. 폴더인 경우 지원 형식(`.md`, `.pdf`, `.html`, `.xml`, `.json`)만 스캔하며, `results/`, 숨김 디렉토리, 심볼릭 링크는 제외한다.

---

## Step 1.1 — 입력 정규화

모든 입력 파일은 제목 분석 전에 정규 정규화 마크다운 형식으로 검증 및 변환된다. 이를 통해 원본 파일 형식에 관계없이 안정적인 줄 번호와 일관된 제목 탐지가 보장된다.

> **실행 시점**: Step 1.1는 각 Step 1.2 에이전트 **내부**에서 내부 전처리로 실행된다. `.md` 원본의 경우, 메타데이터 생성 전에 마크다운 린트 검증 및 자동 수정이 적용된다. 비`.md` 형식의 경우, 에이전트가 식별 및 분할 전에 파일을 정규화한다. 다중 문서 비`.md` 파일의 경우, 순서는: **정규화 → 린트 → 정규 텍스트에서 경계 식별 → 분할**이다. 이를 통해 줄 범위가 원시 소스 형식이 아닌 안정적인 정규 텍스트에서 결정된다.

### 다운스트림 입력 우선순위

모든 후속 단계는 **정규 입력 파일**을 원본 소스로 사용한다. 해결 순서:

1. `doc-{doc_instance_key}__pre__split.md` (다중 문서 파일에서 분할된 경우)
2. `file-{source_file_key}__pre__normalised.md` (비`.md` 형식에서 변환된 경우)
3. 원본 `.md` 파일 (소스가 이미 마크다운인 경우)

이는 문서 매니페스트에 `canonical_input_path`로 기록된다.

### 형식별 정규화

| 입력 형식 | 정규화 방법 | 변환 주체 | 출력 |
|:---|:---|:---|:---|
| `.md` | 텍스트 변환 불필요. 마크다운 린트 검증(§마크다운 린트)을 실행하고 제목 수준 위반을 자동 수정. 메타데이터 파일 생성. | **린트** | 원본 파일(또는 린트 수정본)을 정규 입력으로 사용; `file-{source_file_key}__pre__meta.json` |
| `.pdf` | {{pdf_pages:50}}페이지 단위로 분할하여 에이전트에 할당. 각 에이전트가 해당 페이지 범위를 마크다운으로 변환하고 페이지 마커(`<!-- PAGE NNN -->`)를 삽입. Coordinator가 에이전트 결과를 순서대로 병합하여 최종 `.md` 생성. | **에이전트** ({{pdf_pages:50}}페이지/에이전트) | `file-{source_file_key}__pre__normalised.md` + `meta.json` |
| `.html` | 변환 스크립트로 태그 제거, 구조적 요소(`<h1>`–`<h6>`, `<section>`)를 마크다운 제목으로 보존 | **스크립트** | `file-{source_file_key}__pre__normalised.md` + `meta.json` |
| `.xml` | 변환 스크립트로 구조 파싱, 요소 계층을 제목 수준으로 매핑 | **스크립트** | `file-{source_file_key}__pre__normalised.md` + `meta.json` |
| `.json` | 변환 스크립트로 키 계층 파싱, 제목 수준으로 매핑, 텍스트 값 추출 | **스크립트** | `file-{source_file_key}__pre__normalised.md` + `meta.json` |

### PDF 정규화 상세

1. **분할 단위**: 원본 PDF를 {{pdf_pages:50}}페이지 단위로 분할하여 각 범위를 하나의 서브에이전트에 할당한다. **서브에이전트는 PDF당 최대 {{pdf_agents:20}}개**까지 사용한다.
2. **에이전트 작업**: 각 에이전트는 할당된 페이지 범위의 텍스트를 원본의 텍스트 및 구조를 유지하면서 마크다운으로 변환한다.
   - 페이지 경계에 `<!-- PAGE NNN -->` 마커 삽입
3. **병합**: Coordinator가 모든 에이전트의 결과를 페이지 순서대로 병합하여 단일 `normalised.md`를 생성한다.
   - 경계 페이지에서 끊어진 문장/제목이 있으면 병합 시 복원
4. **meta.json**: `parser` 필드에 `agent` 기록, `pages_per_agent` 필드에 `{{pdf_pages:50}}` 기록

### 스크립트 기반 정규화 (HTML/XML/JSON)

HTML, XML, JSON 형식은 구조가 프로그래밍적으로 파싱 가능하므로, 에이전트 대신 **변환 스크립트**를 사용하여 자동 변환한다.
- 스크립트는 `scripts/` 디렉토리에 위치하며, 형식별 변환기(`html_to_md.py`, `xml_to_md.py`, `json_to_md.py`)로 구성한다.
- 스크립트 실행 결과는 에이전트 변환과 동일한 출력 형식(`normalised.md` + `meta.json`)을 생성한다.
- `meta.json`의 `parser` 필드에 스크립트명과 버전을 기록한다.

### 정규화 요구사항 (비`.md` 형식)

- **안정적 줄 맵**: 정규화 파일의 모든 줄은 동일 파서 버전 및 구성에서 실행 간 변하지 않는 고정 줄 번호를 가진다
- **제목 마커 보존**: 원본 형식의 구조적 요소를 마크다운 제목(`#`, `##` 등)으로 변환하여 정규식 기반 제목 탐지가 균일하게 작동하도록 함
- **모든 후속 단계는 정규 입력 파일에서 작동**, 원시 소스 형식이 아님
- **줄바꿈 정책**: `\n` (LF)으로 정규화. 메타데이터에 기록.
- **페이지 마커**: PDF의 경우 페이지 경계에 `<!-- PAGE NNN -->` 주석 삽입. 제목 추출에서 제외되는 비콘텐츠 줄이지만 추적성을 위해 보존.

### 마크다운 린트 (`.md` 포함 모든 형식)

모든 형식에 대해 제목 구조를 검증한다. `HL001`(수준 건너뛰기 → 자동 강등), `HL002`(Setext → ATX 자동 변환), `HL003`(빈 제목 → 에스컬레이션). 자동 수정이 적용된 경우 `normalised.md`로 출력하고 `canonical_input_path`를 업데이트한다. 린트 결과는 `meta.json`에 기록한다.

### 정규화 재현성

재현성을 보장하기 위해 `file-{source_file_key}__pre__meta.json`에 다음을 기록한다:

| 필드 | 설명 | 예시 |
|:---|:---|:---|
| `source_path` | 원본 파일 경로 | `UR_MD/ur-a2rev5.pdf` |
| `source_hash` | 원본 파일의 SHA-256 | `a1b2c3...` |
| `source_format` | 원본 형식 | `pdf` |
| `parser` | 사용된 파서/라이브러리 또는 변환 주체 | `agent` (PDF) / `html_to_md.py` (HTML) |
| `parser_version` | 파서/스크립트 버전 | `1.0.0` |
| `pages_per_agent` | 에이전트당 페이지 수 (PDF만 해당) | `{{pdf_pages:50}}` |
| `agent_count` | 할당된 에이전트 수 (PDF만 해당) | `5` |
| `line_ending` | 정규화된 줄바꿈 | `LF` |
| `page_marker_format` | 페이지 마커 형식 (PDF만 해당) | `<!-- PAGE NNN -->` |
| `ligature_handling` | 합자 처리 방식 | `expanded` |
| `char_count` | 총 문자 수 | `45230` |
| `est_tokens` | 추정 토큰 수 | `11307` |
| `token_method` | 사용된 토크나이저 | `tiktoken` |
| `grammar_version` | 사용된 제목 문법 버전 (제목 추출 후 설정, 초기값 null) | `v02` |
| `created_at` | 변환 타임스탬프 | `2026-04-05T10:30:00Z` |

### 매니페스트 확정

모든 정규화가 완료된 후, Coordinator가 `corpus__pre__document_manifest.jsonl`을 업데이트한다:
- 각 비`.md` 문서에 대해 `normalised_path` 설정
- 우선순위 체인(`document_split_path → normalised_path → source_path`, 첫 번째 non-null)을 사용하여 `canonical_input_path` 산출
- 매니페스트가 확정되어 Stage 2에서 사용 가능.

> **`grammar_version` 업데이트:** 제목 추출(Stage 2) 완료 후, Coordinator가 각 문서의 `file-{source_file_key}__pre__meta.json`과 매니페스트의 `grammar_version` 필드를 Pass 4에서 사용된 최종 프로모션된 문법 버전으로 업데이트한다. 이 버전이 병합 적격성을 위해 WU 메타데이터에 기록된다.

> 파일 명명 규칙과 저장 경로는 [pre_specification_ko.md](pre_specification_ko.md) §파일 명명 규칙을 참조한다.

---

## Step 1.2 — 소스 패밀리 탐지, Document 단위 식별 및 분할

단일 파일에 하나 이상의 독립 문서가 포함될 수 있다. 소스 패밀리 기준을 사용하여 Document 경계를 결정한다.

### 1.2.0 소스 패밀리 탐지

식별 및 분할 전에 각 파일의 **소스 패밀리**를 결정한다. 소스 패밀리는 분할 기준, 제목 문법 선택, 정규화 규칙을 결정한다.

| 탐지 우선순위 | 신호 | 예시 |
|:---|:---|:---|
| 1 (최고) | 사용자 제공 명시적 매핑 | "이 폴더는 모두 IACS UR" |
| 2 | 문서 내부 제목/메타데이터 | 제목에 "SOLAS" 포함 → IMO 협약 |
| 3 | 파일명 패턴 | `ur-a2rev5.md` → IACS UR |
| 4 | 상위 디렉토리 경로 패턴 | `UR_MD/` → IACS UR |

모든 가용 신호를 수집한다. 서로 다른 우선순위 수준의 신호가 충돌하면, 가장 높은 우선순위의 비모호 신호를 사용한다. 동일 우선순위 수준의 신호가 충돌하면, `unknown`을 할당하고 사용자에게 에스컬레이션한다.

- 탐지가 모호하거나 모순되면 → `unknown`을 할당하고 **사용자에게 에스컬레이션**.
- 파일에 혼합 패밀리가 포함되면 → `mixed`를 할당하고 **사용자에게 에스컬레이션** (패밀리 간 자동 분할 금지).

### Document 식별

> Authority, DocType, Source Family 분류는 [`shared/document_classification.md`](../shared/document_classification.md)를 참조한다.
> 식별자 체인(DocumentKey, DocumentInstanceKey 등)과 slug 규칙은 [`shared/project_definitions.md`](../shared/project_definitions.md) §Identifier Chain 및 [`shared/naming_convention.md`](../shared/naming_convention.md) §DocumentKey Slug Rule을 참조한다.

**Step 1.2에서의 식별 흐름:** file → Source Family 판별 → Document 경계 식별 → Authority + DocType + DocumentKey + DocumentInstanceKey 도출.

> **키 사용 원칙:**
> - **DocumentKey** (`ur_a2`): cross-revision 참조, concept grouping, Heading_ID prefix
> - **DocumentInstanceKey** (`ur_a2_rev5_en`): 파일 경로, 산출물 명명, Concept_ID prefix, WU ID

### DocumentRoot vs. Heading 계층

Document는 heading level이 **아니다** — heading tree의 관리 컨테이너이다. Heading 계층은 DocumentRoot 아래 Level 1부터 시작한다. Source family별 heading level 명칭은 [`shared/document_classification.md`](../shared/document_classification.md) §Heading Level을 참조한다.

```
DocumentRoot (UR A2, SOLAS II-1)    ← 관리 단위; TSV Depth=0 행
  └─ Heading L1 (Part A, ...)        ← heading 계층 시작 (Depth=1)
       └─ Heading L2 (Reg. 1, ...)   ← Depth=2
            └─ Heading L3 (1.1, ...) ← Depth=3
```

> TSV의 첫 번째 행(Depth=0)은 문서 자체를 나타내는 **가상 DocumentRoot 행**이다. 텍스트에서 추출한 heading이 아니며, 실제 heading은 모두 Depth ≥ 1이다.

### 소스 패밀리 분할 기준

> Source Family별 문서 경계 기준은 [`shared/document_classification.md`](../shared/document_classification.md) §Source Family를 참조한다.

분할 예시:
- **IACS UR/UI/Rec/PR**: `ur-a2rev5.md` → `UR A2` (1 파일 = 1 Document)
- **IMO 협약**: `solas_consolidated.md` → `SOLAS II-1`, `SOLAS II-2` (Chapter/Annex 단위)
- **KR 규칙**: `kr_rules_pt3.md` → `KR Rules Pt.3 Ch.1`, `Pt.3 Ch.2` (Part+Chapter 단위)
- **EU 법규**: `directive_2009_45_ec.md` → `Directive 2009/45/EC` (Directive/Regulation 단위)
### 1.2.1 파일별 에이전트 병렬화

> **Coordinator 역할:** 배치 구성, 에이전트 할당·모니터링, Step 1.2 종료 시 에이전트 종료.

1. **배치 구성** — 파일 목록을 가용 에이전트 수(N)의 배치로 분할. 1 에이전트 = 1 파일.
2. **소스 패밀리 탐지** — §1.2.0 우선순위 규칙으로 소스 패밀리 결정.
3. **식별** — 소스 패밀리 기준에 따라 Document 경계 식별.
4. **분할** — 다중 문서 파일의 경우 Document별 시작/종료 줄 범위 결정, 분할 파일 생성(`doc-{doc_instance_key}__pre__split.md`), 콘텐츠 전량 배분 검증.
5. **취합** — 확정된 Document 목록 통합 → `corpus__pre__document_manifest.jsonl` 작성.
6. **에이전트 종료** — Step 1.2 에이전트는 여기서 종료. 이후 단계에서 새 에이전트 할당.

### 1.2.2 소규모 문서 병합

분할 및 토큰 추정 후, 동일 소스 파일·동일 소스 패밀리 내에서 {{merge_threshold:32K}} 토큰 미만인 인접 문서를 하나의 처리 단위(합계 ≤ {{merge_threshold:32K}})로 병합하여 Step 2의 에이전트 수를 줄인다.

### Document 매니페스트 스키마

`corpus__pre__document_manifest.jsonl` — 줄당 하나의 JSON 객체, Document당 한 줄:

| 필드 | 타입 | 설명 |
|:---|:---|:---|
| `doc_instance_key` | string | DocumentInstanceKey |
| `document_key` | string | DocumentKey |
| `authority` | string | 발행 기관 |
| `doc_type` | string | DocType |
| `revision` | string | 리비전 라벨 (예: rev5, 2024) |
| `language` | string | 언어 코드 (ISO 639-1, 예: en, ko) |
| `document_title` | string | DocumentRoot 행 생성을 위한 전체 문서 제목 |
| `source_family` | string | 탐지된 소스 패밀리 |
| `source_path` | string | 원본 파일 경로 |
| `source_hash` | string | 원본 파일의 SHA-256 |
| `document_split_path` | string\|null | 분할 파일 경로 (1 파일 = 1 문서이면 null) |
| `normalised_path` | string\|null | 정규화 파일 경로 (`.md` 원본이면 null) |
| `canonical_input_path` | string | **다운스트림 원본 소스**: document_split_path → normalised_path → source_path (첫 번째 non-null) |
| `start_line_in_source` | int\|null | 원본 파일의 시작 줄 (다중 문서 파일의 경우) |
| `end_line_in_source` | int\|null | 원본 파일의 종료 줄 (다중 문서 파일의 경우) |
| `shared_front_matter_lines` | int | 공유 앞부분으로 분류된 줄 수 |
| `discarded_boilerplate_lines` | int | 보일러플레이트로 분류된 줄 수 |
| `unassigned_lines` | int | 어떤 Document에도 할당되지 않은 줄 수 (0이거나 에스컬레이션되어야 함) |
| `shared_back_matter_lines` | int | 공유 뒷부분으로 분류된 줄 수 |
| `est_tokens` | int\|null | 문서 총 토큰 수 (Step 1.1 meta.json 생성 전까지 null) |
| `token_method` | string\|null | tiktoken 또는 char_approx (측정 전까지 null) |
| `status` | string | `confirmed`, `escalated`, `skipped` |
| `created_at` | string | ISO 8601 타임스탬프 |
