# Step 3 — 청킹, Work Unit 패킹, 이슈 게이트

> **목적.** 헤딩 구조 TSV와 토큰 측정값을 기반으로 컨텍스트 윈도우 청크를 결정하고, 이를 워크 유닛으로 패킹하며, 모든 산출물을 `results/`에 직접 기록한다. 사용자는 이슈가 발동된 경우에만 개입한다(§Step 3.3). 이것이 PRE의 최종 스테이지이다.

> **에이전트.** 종합적인 계획은 코디네이터가 담당하고, 실제 실행 (예로: 쓰기)은 에이전트 최대 사용 수 및 업무 분할 계획을 수립한 후 새로운 서브에이전트에 할당한다. 

---

## 출력물

Step 3가 새로 생성하는 산출물:

- #6 `wu-{wu_key}__pre__meta.json` — WU 메타데이터(구성, 구성 문서, 토큰 수)
- #7 `corpus__pre__manifest.json` — PRE 마스터 인덱스(최종 단계로 생성)
- #7b `doc-{doc_instance_key}__heading__chunk_plan.json` — 청크 경계와 토큰 크기

> 파일 명명 규칙과 전체 산출물 카탈로그는 [pre_specification.md](pre_specification.md) §File Naming Convention 및 §Artefact Catalogue에 정의되어 있다.

---

## 워크 유닛 토큰 범위

| 구간 | 토큰 범위 | 조치 |
|:---|:---|:---|
| **> 상한** | > **{{chunk_max:32K}}** | **Split** — 헤딩 경계에서 여러 WU로 분할하며, 각 WU는 `wu_range` 범위 내에 있어야 함 |
| **`wu_range`** (하한 ≤ 크기 ≤ 상한) | **{{wu_range:16K–32K}}** | **Standalone** — 1 Document = 1 WU |
| **< 하한** | < **16K** | **Merge 후보** — `wu_range`에 도달할 때까지 다른 전체 문서와 병합 가능 |

### 병합 제약 조건

> 전제: Step 3.1에서 상한(`chunk_max`)을 초과하는 문서는 이미 분할되었으므로, 이 절은 **`< 하한`(< 16K) 문서**를 합쳐 상한을 넘지 않도록 묶는 규칙만 다룬다.

- **대상**: `< 하한` 문서만 병합 후보이다. 상한 초과로 이미 분할된 문서의 조각은 standalone WU로 유지되며 다른 문서와 **병합되지 않는다**.
- **상한 준수**: 병합된 WU의 합계 토큰은 상한(`chunk_max`)을 초과할 수 없다.
- **병합 적격성**: 다음 조건을 **모두** 충족하는 문서만 동일한 WU로 병합할 수 있다:
  - 동일한 `Authority`, `DocType`, 언어, `grammar_version`, `measure_method` (토큰 측정 방식이 다르면 상한 판정이 불가)
- **병합 순서**: DocumentKey 순서(ASCII 사전식 — slug 규칙에 의해 `[a-z0-9_]` 문자만 생성되도록 보장됨)로 적격 문서를 추가하다가, 다음 추가가 상한을 초과하게 되면 현재 WU를 닫고 새 WU를 시작한다.
- **잔여 수용**: 마지막 WU가 하한 미만이라도 그대로 수용한다(강제 병합 금지).

---

## WU_Key 명명 규칙

| WU 유형 | WU_Key 형식 | 예시 |
|:---|:---|:---|
| **Standalone** (1 Doc = 1 WU) | `{doc_instance_key}` | `ur_e26_rev1_en` |
| **Split** (1 Doc → N WU) | `{doc_instance_key}_wu{NNN}` | `ur_z10_2_rev3_en_wu001` |
| **Merged** (N Docs → 1 WU) | `merge_{short_hash}` (정렬된 구성 키의 SHA-256 중 처음 8자) | `merge_a3f7c2b1` |

### Split WU 인덱싱

- **`_wu{NNN}`**: 0 패딩 3자리. 소스 `doc_instance_key`별로 청크 순서대로 순번 부여 (가장 낮은 `_ch{NNN}`를 포함하는 WU가 `_wu001`).

> 서브청크 키(`_p{NNN}` / `_w{NNN}`)는 청크 계획의 `sub_chunks` 필드에서 정의된다 (§청크 계획 스키마 참조).

### WU 헤더 메타데이터

`wu-{wu_key}__pre__meta.json`에 기록:

| 필드 | 타입 | 설명 | 예시 |
|:---|:---|:---|:---|
| `wu_key` | string | §WU_Key 명명 규칙 참조 | `merge_a3f7c2b1` |
| `wu_type` | string | `standalone`, `split`, `merged` | `merged` |
| `authority` | string | 발행 기관 (모든 구성 문서 동일) | `IACS` |
| `doc_type` | string | 문서 카테고리 (모든 구성 문서 동일) | `UR` |
| `language` | string | 언어 코드 | `en` |
| `grammar_version` | string | 사용된 헤딩 문법 버전 (구성 문서 전체에서 균일 — 병합 제약 조건으로 강제) | `v02` |
| `measure_method` | string | `tiktoken` 또는 `char_approx` (구성 문서 전체에서 균일 — 병합 제약 조건으로 강제) | `tiktoken` |
| `constituent_docs` | array | 구성 문서 항목 목록 | 아래 참조 |
| `constituent_docs[].doc_instance_key` | string | DocumentInstanceKey | `ur_f1_rev2_en` |
| `constituent_docs[].document_key` | string | DocumentKey | `ur_f1` |
| `constituent_docs[].grammar_version` | string | 문서별 문법 버전 (WU 수준 `grammar_version`과 동일해야 함) | `v02` |
| `constituent_docs[].measure_method` | string | 문서별 측정 방법 (WU 수준 `measure_method`와 동일해야 함) | `tiktoken` |
| `constituent_docs[].start_line` | int | 정규 입력의 첫 줄 (포함) | `1` |
| `constituent_docs[].end_line` | int | 정규 입력의 마지막 줄 (포함) | `27` |
| `constituent_docs[].est_tokens` | int | 이 문서의 토큰 수 | `5200` |
| `constituent_docs[].heading_range` | object | 이 구성 문서의 첫/마지막 Heading_ID | {"first": "..._HD_NNN", "last": "..._HD_NNN"} |
| `est_tokens_total` | int | WU 전체 토큰 수 | `18450` |
| `split_part` | int\|null | 분할(split) WU의 경우: 1부터 시작하는 인덱스 | `1` |
| `split_total` | int\|null | 분할(split) WU의 경우: 전체 파트 수 | `2` |
| `chunk_keys` | array | 이 WU에 포함된 ChunkKey 목록 | `["ur_f1_rev2_en_ch001"]` |
| `status` | string | 라이프사이클 상태 — [pre_specification.md](pre_specification.md) §Work Unit Lifecycle States 참조. 초기값은 `planned`이며, 매니페스트 생성 이전 §3.3 이슈 게이트 처리 후 Coordinator가 `processed`/`proceeded`/`revised`/`aborted`로 갱신한다. | `processed` |
| `output_files` | array | 해당 WU에 대해 `results/` 하위에 생성된 산출물 파일 경로(청크 플랜, 태스크 브리프 등). §3.3 매니페스트 최종화 단계에서 채워진다. | `["results/wu-..._meta.json", ...]` |
| `created_at` | string | ISO 8601 타임스탬프 | `2026-04-05T10:30:00Z` |

> PRE 매니페스트 `work_units[]`로의 필드 매핑 contract는 [pre_specification_ko.md](pre_specification_ko.md) §PRE 매니페스트 — 다운스트림 인터페이스 계약을 정본으로 한다.

---

## Step 3.1 — Context-Window Chunking

**Coordinator**는 헤딩 레벨 토큰 측정값을 사용하여 **재귀적 하향식 분할(recursive top-down splitting)**을 통해 청킹 전략을 결정한다. 이 단계는 **헤딩 정렬 청크(heading-aligned Chunks)**를 생성하며, 각 청크는 Upper Bound 토큰 이하다. WU 할당은 Step 3.2로 미뤄진다.

| 전체 문서 크기 | 청킹 전략 |
|:---|:---|
| **≤ Upper Bound** | 청킹 불필요 — 단일 청크 = 1 문서; WU 결정은 §3.2로 연기 |
| **> Upper Bound** | 헤딩 경계에서 재귀 분할 필수; 각 청크는 Upper Bound 토큰 이하를 목표로 함 |

### 재귀 분할 알고리즘

1. 가장 높은 헤딩 레벨에서 시작(하향식)
2. 현재 레벨의 형제(sibling) 스팬을 검사하며, 스팬 크기 산정에는 **`Est_Tokens_Inclusive`**를 사용
3. 형제 스팬의 `Est_Tokens_Inclusive`가 Upper Bound 이하이면 → 청크로 채택
4. 형제 스팬이 Upper Bound를 초과하면 → 자식 헤딩으로 재귀하여 step 2부터 반복
5. **리프 헤딩(leaf heading)**(자식 없음)이 Upper Bound를 초과하면 → **오버사이즈 리프 예외(oversize leaf exception)** 적용(아래 참조)
6. 여러 형제 스팬으로 구성된 청크의 전체 토큰을 계산할 때는 각 스팬의 `Est_Tokens_Inclusive` 값을 합산한다(형제는 서로 겹치지 않으므로 중복 계산이 발생하지 않는다).

> **헤딩 라인 포함 규칙**: 헤딩 라인 자체는 해당 스팬의 토큰 수에 포함된다. 형제 합계를 계산할 때는 각 형제 스팬의 `Est_Tokens_Inclusive`를 사용한다(겹치지 않는 형제는 안전하게 합산 가능).

> **선택적 병합(Optional coalesce)**: 재귀 패스 이후, 합친 `Est_Tokens_Inclusive`가 여전히 Upper Bound 이하인 연속된 형제 스팬들은 단편화를 줄이기 위해 단일 청크로 병합할 수 있다.

### 오버사이즈 리프 예외(Oversize Leaf Exception)

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

> 분기 기준: §Work Unit 토큰 범위 참조. 아래 표는 청킹 결과를 WU 패킹 조치에만 매핑한다.

| 청킹 결과 | WU 패킹 조치 |
|:---|:---|
| **단일 청크, > 상한** | 오류 — Step 3.1 이후에는 발생해서는 안 됨. 에스컬레이션. |
| **동일 문서에서 발생한 다중 청크** | **인접 병합 필수**: 결합된 `est_tokens` ≤ 상한인 한 연속 청크(청크 순서대로)를 탐욕적으로 병합한 후, 해당 그룹을 하나의 **split WU**로 닫는다. 모든 청크가 할당될 때까지 반복한다. 이는 하한 미만인 split WU의 수를 최소화한다. |
| **단일 청크, WU 목표 범위 내** | **Standalone** — 1 Document = 1 WU. |
| **단일 청크, WU 목표 범위 미만** | **Merge 후보** — §병합 제약 조건에 따라 문서 간 병합 적격. |

> **Split WU 나머지**: 분할 문서의 마지막 WU가 인접 병합 필수 적용 후에도 여전히 하한 미만이면 그대로 수용한다. 분할 문서 조각을 다른 문서와 병합하지 않는다.

> **단일 초과 크기 병합 후보**: 작은 문서가 하한 미만이지만 병합 적격인 다른 문서가 없는 경우(예: Authority/DocType/언어/grammar_version/measure_method를 공유하는 문서가 없음), 해당 문서는 하한 미만의 standalone WU로 남는다. 이는 수용되며, §3.3 이슈 게이트가 Info로 표면화할 수 있다.

> **Split WU 내 Measure_Method**: 분할 문서의 모든 청크는 동일한 `measure_method`를 공유해야 한다 (Step 2가 문서별로 균일한 `Measure_Method`를 생성하므로 보장됨 — §Step 2 Completion 참조). split WU 내에서 혼합하는 것은 오류이다.

### 코디네이터 실행

코디네이터는 모든 제목 구조 TSV, 토큰 측정, 청크 계획이 완료된 직후(Step 2 에이전트 종료 후) WU 패킹을 수행한다:

1. 모든 문서 메타데이터, 제목 구조 TSV, 청크 계획을 읽는다
2. 병합 적격성 확인과 함께 WU 토큰 범위 규칙(split/standalone/merge)을 적용하고, 명명 규칙에 따라 WU_Key를 할당한다
3. WU 메타데이터를 생성하고 WU 패킹 계획을 제시한다 (§Outputs 및 §3.3 참조)

---

## Step 3.3 — 이슈 게이트 및 자동 완료

기본 동작은 자동 완료이다. 코디네이터는 각 섹션에 정의된 트리거에 따라 이슈를 자동으로 감지한다 ([step2_heading_extraction.md](step2_heading_extraction.md) §2.4, §초과 크기 리프 예외, §병합 제약 조건, §Work Unit 토큰 범위 등). 트리거가 발동되지 않으면 코디네이터는 아래 표를 제시하지 않고 산출물을 직접 `results/`에 기록한다 (§산출물 저장 참조). 트리거가 발동되면 코디네이터는 다음 보고서를 표면화하고 결정을 요청한다.

### 이슈 보고서

트리거가 발동되면 코디네이터는 **최소한** 다음 필드를 포함하는 이슈 보고서를 표면화한다 (이슈 유형에 따라 추가 컨텍스트가 첨부될 수 있다):

| 필드 | 설명 |
|:---|:---|
| `issue_type` | 예: `oversize_leaf`, `merge_eligibility_violation`, `warning_overflow`, `single_chunk_overflow`, `headingless_oversize` |
| `trigger_rule` | 발동된 정확한 규칙/섹션 (예: "§초과 크기 리프 예외 → 사용자 에스컬레이션") |
| `affected_doc_instance_keys` | 영향받은 DocumentInstanceKey 배열 |
| `affected_wu_keys` | 영향받은 WU_Key 배열 (WU 패킹이 이미 시도된 경우) |
| `summary` | 실행 요약: 총 Document/Chunk/WU 수, 미결 Warning 수, 문법 버전, 초과 크기 예외 수, 병합 위반 |
| `suggested_action` | 코디네이터가 권장하는 `proceed` / `revise` / `abort` 선택 및 근거 |
| `attached_plan` | 영향받은 항목에 대한 청킹 계획 및 WU 패킹 계획 슬라이스 |

### 사용자 응답

> WU 라이프사이클 상태(`planned → running → completed → validated → processed/proceeded/revised/aborted`)는 [pre_specification.md](pre_specification.md) §Work Unit Lifecycle States에 정의되어 있다. 아래 매핑은 WU 메타데이터(`status` 필드)의 종료 상태를 설정한다.

| 사용자 응답 | 조치 | 결과 WU `status` |
|:---|:---|:---|
| **`proceed`** | 이슈를 인지하고 계속 진행 (예: Warning 초과 수용). 코디네이터가 자동 완료를 재개한다. | `proceeded` |
| **`revise`** | 임계값 조정 또는 재실행 범위 지정. Coordinator가 영향받은 단계를 재실행한다. | `revised` (재실행 후 → `processed`) |
| **`abort`** | 해당 Document(들)의 처리를 중단. 임시 사본을 `results/aborted/{doc_instance_key}/`로 격리 보존. 중단된 문서와 그 WU는 **`corpus__pre__manifest.json`에서 제외**된다. | `aborted` |

> 자동 완료된(트리거가 발생하지 않은) WU에는 `status = processed`가 부여된다.

---

## 산출물 저장

Step 1–3에서 생성된 모든 결과물은 처음부터 `results/`에 직접 저장된다. 임시 폴더 개념은 사용하지 않는다.

단계 종료 시, 다음 중간 산출물은 자동 삭제된다: Step 2의 `extraction_llm.tsv`, `extraction_script.tsv`, discrepancy 작업 사본, `validated.tsv`, `grammar_candidate.md`.

이슈로 `abort`된 경우에 한해 디버깅용 임시 사본을 `results/aborted/{doc_instance_key}/`로 격리 보존한다.

`coverage.json`(#8)은 항상 생성된다.

전체 결과물 카탈로그와 파일 명명 규칙은 [pre_specification_ko.md](pre_specification_ko.md) §산출물 카탈로그를 정본으로 한다.

**PRE 매니페스트** (`results/corpus__pre__manifest.json`)는 최종 단계로 생성된다 — 모든 문서 항목, WU_Key, 저장된 파일 경로, 문법 버전, 미결 warning 수, 초과 크기 예외 수를 기록한다. 다운스트림 소비자(`commands/agents.md`, `task_brief_generator.md`)를 위한 단일 진입점 역할을 한다.

> **인터페이스 contract**: PRE 매니페스트는 [pre_specification_ko.md](pre_specification_ko.md) §PRE 매니페스트 — 다운스트림 인터페이스 contract에 정의된 필수 필드를 채워야 한다. 다운스트림 단계(TD/APP/CT)는 이 필드들이 존재한다고 가정한다.

