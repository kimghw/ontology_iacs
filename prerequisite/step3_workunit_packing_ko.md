# Step 3 — 청킹, Work Unit 패킹, 이슈 게이트

> **목적.** 제목 구조 TSV와 토큰 측정값을 기반으로 컨텍스트 윈도우 Chunk를 결정하고, Work Unit으로 패킹하며, 모든 산출물을 `results/`에 직접 저장한다. 사용자는 이슈 트리거가 발생한 경우에만 개입한다(§Step 3.3). 이것이 PRE의 최종 스테이지이다.

---

## 출력물

Step 3가 새로 생성하는 산출물:

- #6 `wu-{wu_key}__pre__meta.json` — WU 메타데이터 (구성, 구성 문서, 토큰 수)
- #7 `corpus__pre__manifest.json` — PRE 마스터 인덱스 (최종 단계로 생성)
- #7b `doc-{doc_instance_key}__heading__chunk_plan.json` — Chunk 경계와 토큰 크기

> 파일 명명 규칙과 전체 산출물 카탈로그는 [pre_specification_ko.md](pre_specification_ko.md) §파일 명명 규칙 및 §산출물 카탈로그를 참조한다.

---

## Work Unit 토큰 범위

| 매개변수 | 값 |
|:---|:---|
| **WU 목표 범위** | **{{wu_range:16K–32K}}** 토큰 |

| 문서 크기 | 조치 |
|:---|:---|
| **> 상한 (> {{chunk_max:32K}} 토큰)** | **Split** — 제목 경계에서 여러 WU로 분할, 각각 {{wu_range:16K–32K}} 범위 내 |
| **하한 ≤ 크기 ≤ 상한** | **Standalone** — 1 Document = 1 WU |
| **< 하한** | **Merge 후보** — {{wu_range:16K–32K}}에 도달할 때까지 다른 전체 문서와 병합 가능 |

### 병합 제약 조건

- **전체 문서만** — 문서는 전체가 포함되거나 포함되지 않음
- **병합 적격성**: 다음의 **모든** 조건을 충족하는 문서만 동일 WU에 병합 가능:
  - 동일 `Authority`
  - 동일 `DocType`
  - 동일 언어
  - 동일 `grammar_version` (추출 시 사용된 제목 문법 버전)
  - 동일 `Measure_Method` (tiktoken 또는 char_approx) — 병합된 WU 내에서 측정 방법을 혼합하지 않음
- 상한을 초과하는 문서는 분할되며; 각 조각은 standalone WU이고 다른 문서와 **병합되어서는 안 됨**
- 병합 시, DocumentKey 순서(ASCII 사전식 순서 — slug 규칙에 의해 `[a-z0-9_]` 문자만 생성됨이 보장)로 적격 문서를 추가하여 다음 추가가 상한을 초과할 때까지 진행; 그런 다음 현재 WU를 닫고 새 WU를 시작
- 마지막 WU가 하한 아래이면 그대로 수용 (분할 경계를 넘어 강제 병합하지 않음)

### 임계값 변경 재실행 규칙

| 변경 | 재실행 범위 |
|:---|:---|
| **하한만 변경** | Step 3.2만 재실행 (WU 패킹) |
| **상한 변경** | Step 3.1 (청킹) **및** Step 3.2 (패킹) 재실행 — 청크 경계와 슬라이딩 윈도우 매개변수(window_size, overlap)가 상한에서 파생되므로 자동 재계산된다 |

> 이 임계값은 조정 가능하다. 값을 조정하고 위 표에 따라 적절한 단계를 재실행한다.

---

## WU_Key 명명 규칙

| WU 유형 | WU_Key 형식 | 예시 |
|:---|:---|:---|
| **Standalone** (1 Doc = 1 WU) | `{doc_instance_key}` | `ur_e26_rev1_en` |
| **Split** (1 Doc → N WU) | `{doc_instance_key}_wu{NNN}` | `ur_z10_2_rev3_en_wu001` |
| **Merged** (N Docs → 1 WU) | `merge_{short_hash}` (정렬된 구성 키의 SHA-256 중 처음 8자) | `merge_a3f7c2b1` |

> 병합된 WU의 경우, 짧은 해시가 과도하게 긴 파일명을 방지한다. 전체 구성 목록은 WU 메타데이터 JSON에 기록된다.

### WU 헤더 메타데이터

`wu-{wu_key}__pre__meta.json`에 기록:

| 필드 | 타입 | 설명 | 예시 |
|:---|:---|:---|:---|
| `wu_key` | string | §WU_Key 명명 규칙 참조 | `merge_a3f7c2b1` |
| `wu_type` | string | `standalone`, `split`, `merged` | `merged` |
| `authority` | string | 발행 기관 (모든 구성 문서 동일) | `IACS` |
| `doc_type` | string | 문서 카테고리 (모든 구성 문서 동일) | `UR` |
| `language` | string | 언어 코드 | `en` |
| `grammar_version` | string | 사용된 제목 문법 버전 | `v02` |
| `constituent_docs` | array | 구성 문서 항목 목록 | 아래 참조 |
| `constituent_docs[].doc_instance_key` | string | DocumentInstanceKey | `ur_f1_rev2_en` |
| `constituent_docs[].document_key` | string | DocumentKey | `ur_f1` |
| `constituent_docs[].start_line` | int | 정규 입력의 첫 줄 (포함) | `1` |
| `constituent_docs[].end_line` | int | 정규 입력의 마지막 줄 (포함) | `27` |
| `constituent_docs[].est_tokens` | int | 이 문서의 토큰 수 | `5200` |
| `constituent_docs[].heading_range` | object | 이 구성 문서의 첫/마지막 Heading_ID | {"first": "..._HD_NNN", "last": "..._HD_NNN"} |
| `est_tokens_total` | int | 총 WU 토큰 수 | `18450` |
| `split_part` | int\|null | Split WU의 경우: 1 기반 인덱스 | `1` |
| `split_total` | int\|null | Split WU의 경우: 총 부분 수 | `2` |
| `chunk_keys` | array | 이 WU에 포함된 ChunkKey 목록 | `["ur_f1_rev2_en_ch001"]` |
| `created_at` | string | ISO 8601 타임스탬프 | `2026-04-05T10:30:00Z` |

> Standalone 및 Split WU의 경우 `constituent_docs`에 단일 항목이 있다. Merged WU의 경우 각 구성 문서가 자체 제목 범위를 가진다.

> 모든 다운스트림 산출물은 파일 scope 접두사로 `wu-{wu_key}`를 사용한다. 문서 수준 집계는 WU 수준 처리 후 `constituent_docs` 필드를 읽어 수행한다.

---

## Step 3.1 — 컨텍스트 윈도우 청킹

제목 수준 토큰 측정값을 사용하여 **재귀적 하향 분할**을 통해 청킹 전략을 결정한다. 이 단계에서는 **제목 정렬 Chunk**를 생성한다 — 각 Chunk ≤ 상한 토큰. WU 할당은 Step 3.2로 보류한다.

- **≤ 상한** → 청킹 불필요(단일 Chunk = 1 Document, WU 결정은 §3.2로 위임)
- **> 상한** → 제목 경계에서 재귀적 분할 필수, 각 Chunk ≤ 상한 토큰 목표

### 재귀적 분할 알고리즘

1. 최상위 제목 수준에서 시작 (하향)
2. 현재 수준의 형제 범위를 **`Est_Tokens_Inclusive`**를 사용하여 검토
3. 형제 범위의 `Est_Tokens_Inclusive`가 ≤ 상한이면 → Chunk로 채택
4. 형제 범위가 상한을 초과하면 → 하위 제목으로 재귀, 단계 2부터 반복
5. **리프 제목**(자식 없음)이 상한을 초과하면 → **초과 크기 리프 예외** 적용 (아래 참조)
6. 여러 형제 범위로 구성된 Chunk의 총 토큰을 계산할 때, 각각의 `Est_Tokens_Inclusive` 값을 합산한다 (형제는 겹치지 않으므로 이중 계산 없음).

> **제목 줄 포함 규칙**: 제목 줄 자체가 범위의 토큰 수에 포함된다. 형제 합산을 계산할 때 각 형제 범위의 `Est_Tokens_Inclusive`를 사용한다 (겹치지 않는 형제는 안전하게 합산 가능).

> **선택적 병합**: 재귀 패스 후, 연속 형제 범위의 결합된 `Est_Tokens_Inclusive`가 ≤ 상한으로 유지되면 단일 Chunk로 병합하여 파편화를 줄일 수 있다.

### 초과 크기 리프 예외

리프 제목이 상한 토큰을 초과하고 제목 경계에서 분할할 수 없는 경우:

| 옵션 | 사용 시점 | 병합 규칙 |
|:---|:---|:---|
| **단락/목록항목 분할** | 콘텐츠에 ≥ 3개의 구조적 분할 경계(빈 줄 구분자 `\n\n`, 또는 줄 시작 항목 마커 `^\s*(?:\.\d+\|\d+[.)]\|\(\d+\)\|[A-Za-z][.)]\|[-*+])\s` 일치)가 있고 해당 경계에서 분할하면 모든 세그먼트 ≤ 상한 | 단락 경계에서 분할; 합성 서브청크 ID(`{ChunkKey}_p{NNN}`) 할당. 단락 순서로 결과 병합; 겹침에서 중복 제거. |
| **슬라이딩 추출 윈도우** | 단락/목록항목 분할 실패 (구조적 경계 < 3개, 또는 분할 후 세그먼트 > 상한) | `window_size = floor(Upper_Bound × 0.875)`, `overlap = floor(window_size × 0.21)`, `unique = window_size - overlap`. 상한 변경 시 자동 조정. Coordinator가 병합 및 중복 제거. 합성 서브청크 ID(`{ChunkKey}_w{NNN}`) 할당. |
| **사용자 에스컬레이션** | 슬라이딩 윈도우가 목표 대비 > 20% 토큰 분산을 가진 세그먼트를 생성하거나, 콘텐츠 구조가 모호한 경우 | 권장 사항과 함께 초과 크기 리프를 사용자에게 제시 |

> 초과 크기 리프 분할은 청크 계획에 `split_method = "oversize_paragraph"` 또는 `"oversize_window"`로 기록되며, 사용자 에스컬레이션이 발생한 경우 §3.3 이슈 게이트 보고에 포함된다.

> **청크 계획 산출물**: `doc-{doc_instance_key}__heading__chunk_plan.json`은 모든 청크 경계를 확정적으로 기록하며, 이는 초과 크기 리프 분할을 재구성하는 데 특히 중요하다. 제목 구조 TSV가 구조적 계층을 제공하는 한편, 청크 계획은 이를 보완한다. (저장 정책은 §산출물 저장 참조.)

### 초과 크기 배타 세그먼트

**비리프 제목의 자체 배타 콘텐츠**(첫 자식 제목 이전의 서문)가 상한을 초과하면, 합성 리프로 취급하고 위의 초과 크기 리프 예외 규칙을 적용한다. 청크 계획에 `split_method = "oversize_preamble"`로 기록.

### 제목 없는 문서 폴백

문서에 제목이 전혀 없는 경우(또는 자식 제목 없는 DocumentRoot만 있는 경우):

1. ≤ 상한이면 → 단일 Chunk = 1 Document (WU 패킹으로 진행)
2. > 상한이면 → 단락/목록항목 분할 또는 슬라이딩 윈도우 적용 (초과 크기 리프 예외와 동일), 전체 문서를 단일 리프로 취급
3. 청크 계획에 `split_method = "headingless"`로 기록

### 청킹 규칙

- **분할 경계는 제목 경계에 정렬되어야 한다** (초과 크기 리프 예외와 제목 없는 폴백 제외)
- Chunk 키 규칙: `{doc_instance_key}_ch{NNN}` — 0 패딩, 문서별 순번
- Task Brief는 **Work Unit별**로 생성; Chunk 경계와 토큰 크기가 내부에 기록
- 제목 구조 TSV가 모든 후속 처리의 주요 **청크 맵** 역할. `chunk_plan.json`이 모든 청크 경계를 기록하고 제목 구조 TSV를 보완한다.

### 청크 계획 스키마

`doc-{doc_instance_key}__heading__chunk_plan.json`은 문서별로 `doc_instance_key`와 `chunks[]` 배열을 포함한다. 각 청크 항목의 필드:

- `chunk_key`: ChunkKey (`{doc_instance_key}_ch{NNN}`)
- `heading_range`: `{"first": "<Heading_ID>", "last": "<Heading_ID>"}` 또는 `null` (제목 없는 문서)
- `heading_level`: 청크 경계가 끊긴 제목 수준명 또는 `null`
- `start_line`, `end_line`: 정규 입력 파일 기준 줄 범위 (포함)
- `est_tokens`: 청크 토큰 수
- `split_method`: `recursive` / `oversize_paragraph` / `oversize_window` / `oversize_preamble` / `headingless`
- `measure_method`: `tiktoken` 또는 `char_approx`
- `sub_chunks`: 초과 크기 리프 예외나 제목 없는 폴백으로 추가 분할된 경우의 서브청크 배열, 그 외 `null`. 각 서브청크는 `sub_chunk_key`(`{ChunkKey}_p{NNN}` 또는 `{ChunkKey}_w{NNN}`), `start_line`, `end_line`, `est_tokens`를 포함.

토큰 임계값(상한/하한) 및 분할 규칙은 §Work Unit 토큰 범위와 §Step 3.1을 따른다. 실제 JSON 구조는 위 필드 정의를 기반으로 Coordinator가 생성한다.

---

## Step 3.2 — Work Unit 패킹

컨텍스트 윈도우 Chunk가 결정된 후, Chunk(또는 Chunk = Document인 전체 문서)를 §Work Unit 토큰 범위에 정의된 임계값에 따라 **Work Unit(WU)**으로 패킹한다.

### 패킹 로직

분기 기준은 §Work Unit 토큰 범위 참조.

| 청킹 결과 | WU 패킹 조치 |
|:---|:---|
| **단일 청크** | 해당 문서에 §Work Unit 토큰 범위의 분기(Standalone / Merge 후보) 적용. |
| **다중 청크** | 각 청크(또는 인접 청크의 병합 그룹)가 **split WU**가 됨. 동일 문서의 인접 청크는 결합 가능 범위 내에서 하나의 WU로 병합 가능. |
| **오류** | 발생해서는 안 됨 — 에스컬레이션. |

> **Split WU 나머지**: 분할 문서의 마지막 WU가 하한 미만이면 그대로 수용. 분할 문서 조각을 다른 문서와 병합하지 않는다.

### Coordinator 실행

Coordinator는 모든 제목 구조 TSV, 토큰 측정, 청크 계획이 완료된 후(Step 2 에이전트 종료 후) 즉시 WU 패킹을 수행한다:

1. 모든 입력 파일(문서 메타데이터, 제목 구조 TSV, 청크 계획) 읽기
2. 병합 적격성 확인과 함께 WU 토큰 범위 규칙(split/standalone/merge) 적용 및 명명 규칙에 따라 WU_Key 할당
3. WU 메타데이터 생성 및 §3.3에 패킹 계획 제시

---

## Step 3.3 — 이슈 게이트 및 자동 완료

기본 동작은 자동 완료. 이슈 발생 여부는 Coordinator가 자동으로 판정한다 (각 트리거 정의는 §2.4, §초과 크기 리프 예외, §병합 제약 조건, §Work Unit 토큰 범위 등 해당 출처에 정의됨). 이슈가 발생한 경우에만 아래 형식으로 사용자에게 보고하고 결정을 요청한다.

### 이슈 발생 시 보고

이슈 발생 시 Coordinator는 사용자가 원인을 진단할 수 있도록 청킹 계획, WU 패킹 계획, 대상 Document 목록, 실행 요약(총 Document/Chunk/WU 수, 미결 Warning 수, 문법 버전, 초과 크기 예외, 병합 적격성 위반 등)을 제공한다. 보고 형식과 포함 항목은 이슈 종류와 컨텍스트에 따라 Coordinator가 결정한다.

### 사용자 응답

| 사용자 응답 | 조치 |
|:---|:---|
| **`proceed`** | 이슈를 인지하고 그대로 진행 (예: Warning 초과 수용). Coordinator가 산출물을 자동 프로모션. |
| **`revise`** | 임계값 조정 또는 재처리 범위 지정 후 재실행. §임계값 변경 재실행 규칙 참조. |
| **`abort`** | 해당 Document/문서군 처리 중단. 임시 사본을 `results/aborted/{doc_instance_key}/`로 격리 보존. |

---

## 산출물 저장

Step 1–3에서 생성된 모든 결과물은 처음부터 `results/`에 직접 저장된다. 임시 폴더 개념은 사용하지 않는다.

단계 종료 시, 다음 중간 산출물은 자동 삭제된다: Step 2의 `extraction_llm.tsv`, `extraction_script.tsv`, discrepancy 작업 사본, `validated.tsv`, `grammar_candidate.md`.

이슈로 `abort`된 경우에 한해 디버깅용 임시 사본을 `results/aborted/{doc_instance_key}/`로 격리 보존한다.

`coverage.json`(#8)은 항상 생성된다.

전체 결과물 카탈로그와 파일 명명 규칙은 [pre_specification_ko.md](pre_specification_ko.md) §산출물 카탈로그를 정본으로 한다.

**PRE 매니페스트** (`results/corpus__pre__manifest.json`)는 최종 단계로 생성된다 — 모든 문서 항목, WU_Key, 저장된 파일 경로, 문법 버전, 미결 warning 수, 초과 크기 예외 수를 기록한다. 다운스트림 소비자(`commands/agents.md`, `task_brief_generator.md`)를 위한 단일 진입점 역할을 한다.

> **인터페이스 contract**: PRE 매니페스트는 [pre_specification_ko.md](pre_specification_ko.md) §PRE 매니페스트 — 다운스트림 인터페이스 contract에 정의된 필수 필드를 채워야 한다. 다운스트림 단계(TD/APP/CT)는 이 필드들이 존재한다고 가정한다.

