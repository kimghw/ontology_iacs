# Step 3 — 청킹, Work Unit 패킹, 승인

> **목적.** 제목 구조 TSV와 토큰 측정값을 기반으로 컨텍스트 윈도우 Chunk를 결정하고, Work Unit으로 패킹하며, 모든 산출물을 확정(프로모션)하기 위한 사용자 승인을 받는다. 이것이 PRE의 최종 스테이지이다.

---

## 출력물

> 파일 명명 규칙과 전체 산출물 카탈로그는 [pre_specification_ko.md](pre_specification_ko.md) §파일 명명 규칙 및 §산출물 카탈로그를 참조한다.

이 단계에서는 카탈로그의 산출물 #6, #7, #7b를 생성한다:
- #6 `wu-{wu_key}__pre__meta.json` — WU 메타데이터 (구성, 구성 문서, 토큰 수)
- #7 `corpus__pre__manifest.json` — PRE 마스터 인덱스 (승인 후 생성)
- #7b `doc-{doc_instance_key}__heading__chunk_plan.json` — Chunk 경계와 토큰 크기 (항상 생성 및 프로모션)

이 단계에서는 **산출물 프로모션**도 수행한다 — 모든 프로모션 산출물(#1–#7c)을 `results/temp/pre/`에서 `results/`로 이동.

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
| **상한 변경** | Step 3.1 (청킹) **및** Step 3.2 (패킹) 재실행 — 청크 경계가 상한에 의존하므로 |
| **슬라이딩 윈도우 매개변수 (window_size, overlap) 변경** | Step 3.1 및 3.2 재실행 |

> 슬라이딩 윈도우 매개변수는 상한에서 파생된다. 상한을 변경하면 이 매개변수가 자동으로 변경된다.

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
| `wu_key` | string | 고유 WU 식별자 | `merge_a3f7c2b1` |
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

| 총 문서 크기 | 청킹 전략 |
|:---|:---|
| **≤ 상한 (≤ {{chunk_max:32K}} 토큰)** | 청킹 불필요 — 단일 Chunk (= 1 Document). **WU 결정은 Step 3.2로 보류** (standalone 또는 merge 후보가 될 수 있음). |
| **> 상한 (> {{chunk_max:32K}} 토큰)** | 제목 경계에서 필수 재귀적 분할; 각 Chunk는 ≤ 상한 토큰 목표 |

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

> 초과 크기 리프 분할은 승인 시 사용자 검토를 위해 청크 계획에 `split_method = "oversize_paragraph"` 또는 `"oversize_window"`로 기록된다.

> **청크 계획 산출물**: `doc-{doc_instance_key}__heading__chunk_plan.json`은 **항상 프로모션**된다. 제목 구조 TSV가 구조적 계층을 제공하지만, 청크 계획은 모든 청크 경계를 확정적으로 기록하며, 이는 초과 크기 리프 분할을 재구성하는 데 특히 중요하다.

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
- 제목 구조 TSV가 모든 후속 처리의 주요 **청크 맵** 역할. 항상 프로모션되는 `chunk_plan.json`이 모든 청크 경계를 기록하고 제목 구조 TSV를 보완한다.

### 청크 계획 스키마

`doc-{doc_instance_key}__heading__chunk_plan.json`:

**예시 A — 제목 기반 문서:**

```json
{
  "doc_instance_key": "ur_a2_rev5_en",
  "chunks": [
    {
      "chunk_key": "ur_a2_rev5_en_ch001",
      "heading_range": {"first": "ur_a2_HD_001", "last": "ur_a2_HD_045"},
      "heading_level": "Part",
      "start_line": 1,
      "end_line": 890,
      "est_tokens": 28000,
      "split_method": "recursive",
      "measure_method": "tiktoken",
      "sub_chunks": null
    },
    {
      "chunk_key": "ur_a2_rev5_en_ch002",
      "heading_range": {"first": "ur_a2_HD_046", "last": "ur_a2_HD_046"},
      "heading_level": "Regulation",
      "start_line": 891,
      "end_line": 1720,
      "est_tokens": 35000,
      "split_method": "oversize_paragraph",
      "measure_method": "tiktoken",
      "sub_chunks": [
        {"sub_chunk_key": "ur_a2_rev5_en_ch002_p001", "start_line": 891, "end_line": 1300, "est_tokens": 17000},
        {"sub_chunk_key": "ur_a2_rev5_en_ch002_p002", "start_line": 1301, "end_line": 1720, "est_tokens": 18000}
      ]
    }
  ]
}
```

**예시 B — 제목 없는 문서:**

```json
{
  "doc_instance_key": "ur_x1_rev1_en",
  "chunks": [
    {
      "chunk_key": "ur_x1_rev1_en_ch001",
      "heading_range": null,
      "heading_level": null,
      "start_line": 1,
      "end_line": 1200,
      "est_tokens": 42000,
      "split_method": "headingless",
      "measure_method": "tiktoken",
      "sub_chunks": [
        {"sub_chunk_key": "ur_x1_rev1_en_ch001_p001", "start_line": 1, "end_line": 600, "est_tokens": 21000},
        {"sub_chunk_key": "ur_x1_rev1_en_ch001_p002", "start_line": 601, "end_line": 1200, "est_tokens": 21000}
      ]
    }
  ]
}
```

---

## Step 3.2 — Work Unit 패킹

컨텍스트 윈도우 Chunk가 결정된 후, Chunk(또는 Chunk = Document인 전체 문서)를 §Work Unit 토큰 범위에 정의된 임계값에 따라 **Work Unit(WU)**으로 패킹한다.

### 패킹 로직

| 문서 청킹 결과 | WU 패킹 조치 |
|:---|:---|
| **단일 청크, > 상한 (A 이후 불가능)** | 오류 — 발생해서는 안 됨. 에스컬레이션. |
| **동일 문서의 다중 청크** | 각 청크(또는 인접 청크의 병합 그룹)가 **split WU**가 됨, 각각 {{wu_range:16K–32K}} 목표. 동일 문서의 인접 청크는 결합 시 ≤ 상한이면 하나의 WU로 병합 가능. |
| **단일 청크, {{wu_range:16K–32K}} 범위 내** | **Standalone** — 1 Document = 1 WU. |
| **단일 청크, < 하한** | **Merge 후보** — §병합 제약 조건에 따라 문서 간 병합 가능. |

> **Split WU 나머지**: 분할 문서의 마지막 WU가 하한 미만이면 그대로 수용. 분할 문서 조각을 다른 문서와 병합하지 않는다.

### Coordinator 실행

Coordinator는 모든 제목 구조 TSV, 토큰 측정, 청크 계획이 완료된 후(Step 2 에이전트 종료 후) 즉시 WU 패킹을 수행한다:

1. 모든 문서 메타데이터, 제목 구조 TSV, 청크 계획 읽기
2. 병합 적격성 확인과 함께 WU 토큰 범위 규칙(split/standalone/merge) 적용
3. 명명 규칙에 따라 WU_Key 할당
4. 각 WU에 대해 `wu-{wu_key}__pre__meta.json` 생성
5. 사용자 승인(Step 3.3)을 위한 WU 패킹 계획 준비

---

## Step 3.3 — 청킹 계획 및 Document 목록 승인

통합 청킹 계획과 대상 문서 목록을 단일 사용자 승인으로 함께 제시한다.

### 청킹 계획 (예시)

| Chunk Key | 문서 | 제목 범위 | Heading_Level | Split_Method | 추정 토큰 | Measure_Method |
|:---|:---|:---|:---|:---|:---|:---|
| `ur_a2_rev5_en_ch001` | UR A2 | Part A–C | Part | `recursive` | 30K | tiktoken |
| `solas_ii_1_rev2024_en_ch001` (분할 없음) | SOLAS II-1 | 전체 문서 | — | `no_split` | 28K | tiktoken |
| `marpol_annex_i_rev2024_en_ch001` | MARPOL Annex I | Regulations 1–8 | Part | `recursive` | 30K | tiktoken |
| `marpol_annex_i_rev2024_en_ch002` | MARPOL Annex I | Regulations 9–16 | Part | `recursive` | 27K | tiktoken |
| `marpol_annex_i_rev2024_en_ch003` | MARPOL Annex I | Regulations 17–28 | Part | `recursive` | 31K | tiktoken |

### WU 패킹 계획 (예시)

| WU_Key | WU_Type | 구성 문서 | 추정 토큰 | 제목 수 |
|:---|:---|:---|:---|:---|
| `ur_e26_rev1_en` | standalone | UR E26 | 30K | 205 |
| `ur_z10_2_rev3_en_wu001` | split | UR Z10.2 (ch001–ch002) | 24K | 147 |
| `ur_z10_2_rev3_en_wu002` | split | UR Z10.2 (ch003–ch004) | 24K | 147 |
| `merge_a3f7c2b1` | merged | UR F1 (5K) + UR F2 (7K) + UR F3 (4K) | 16K | 12 |

### 대상 Document 목록 (예시)

| # | 파일 경로 | 문서 | Authority | DocType | DocumentKey | InstanceKey | 총 토큰 | Chunk 수 | WU 수 | 제목 수 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | `{경로}` | `{문서명}` | `{IACS/IMO/KR/EU}` | `{UR/SOLAS/...}` | `{doc_key}` | `{doc_instance_key}` | `{n}K` | `{n 또는 1}` | `{n}` | `{n}` |

### 실행 요약 (예시)

| 지표 | 값 |
|:---|:---|
| 총 Document 수 | `{n}` |
| 총 Chunk 수 | `{n}` |
| 총 Work Unit 수 | `{n}` |
| 미결 Warning | `{n}` (최종 불일치 TSV에서) |
| 문법 버전 | `{DocType 문법 버전 목록}` |
| 초과 크기 예외 | `{n 또는 "없음"}` |
| 병합 적격성 위반 | `{n 또는 "없음"}` |

### 승인 상태

| 사용자 응답 | 조치 |
|:---|:---|
| **`approve_all`** | 모든 산출물 프로모션. PRE 완료. |
| **`approve_partial`** | 지정된 WU만 프로모션. 나머지 WU는 추후 수정을 위해 `held` 상태로 보류. |
| **`revise_and_rerun`** | 사용자가 임계값 변경 또는 재처리 범위를 지정. Coordinator가 §임계값 변경 재실행 규칙에 따라 영향받는 단계를 재실행. |
| **`reject`** | PRE 중단. 프로모션 없음. 디버깅을 위해 모든 임시 산출물 보존. |

### 부분 승인 후 작업 흐름

`approve_partial` 선택 시:
1. 승인된 WU는 즉시 프로모션. 승인된 WU만 포함하는 **부분** `corpus__pre__manifest.json` 생성.
2. 보류된 WU는 `held` 상태로 `results/temp/pre/`에 유지.
3. 재개: 사용자가 Step 3.3을 다시 호출. Coordinator가 보류된 WU만 재승인을 위해 제시.
4. 재승인 시, Coordinator가 새로 승인된 WU로 기존 `corpus__pre__manifest.json`을 **업데이트**(upsert).
5. 보류된 WU 산출물은 승인 라운드 간 불변 — 사용자가 `revise_and_rerun`을 선택하지 않는 한 재처리되지 않음.

→ **사용자 승인을 받는다.** 승인되면 Coordinator가 산출물을 프로모션한다.

---

## 산출물 프로모션

승인 후, Coordinator가 `results/temp/pre/` → `results/`로 산출물을 프로모션한다:

**항상 프로모션:**
- #1 `doc-{doc_instance_key}__heading__structure.tsv`
- #2 `doc-{doc_instance_key}__heading__regex_spec.json`
- #3 `file-{source_file_key}__pre__meta.json`
- #4 `file-{source_file_key}__pre__normalised.md` (해당 시)
- #4a `doc-{doc_instance_key}__pre__split.md` (다중 문서 소스 파일에만 해당)
- #5 `doctype-{DocType}__heading__grammar_v{NN}.md`
- #6 `wu-{wu_key}__pre__meta.json`
- #7 `corpus__pre__manifest.json`
- #7a `corpus__pre__document_manifest.jsonl`
- #7b `doc-{doc_instance_key}__heading__chunk_plan.json`
- #7c `doc-{doc_instance_key}__heading__discrepancy_final.tsv` (감사를 위해 보존)

**프로모션 후 폐기:**
- Step 2 중간 산출물 (extraction_llm.tsv, extraction_script.tsv, discrepancy 작업 사본, validated.tsv, grammar_candidate.md — 카탈로그에 번호 미부여)
- #8 `doc-{doc_instance_key}__heading__coverage.json` — 조건부 프로모션 (사용자 요청 시)

전체 목록은 [pre_specification_ko.md](pre_specification_ko.md) §산출물 카탈로그를 참조한다.

**PRE 매니페스트** (`results/corpus__pre__manifest.json`)는 최종 단계로 생성된다 — 모든 문서 항목, WU_Key, 프로모션된 파일 경로, 문법 버전, 미결 warning 수, 초과 크기 예외 수를 기록한다. 다운스트림 소비자(`commands/agents.md`, `task_brief_generator.md`)를 위한 단일 진입점 역할을 한다.

> **인터페이스 contract**: PRE 매니페스트는 [pre_specification_ko.md](pre_specification_ko.md) §PRE 매니페스트 — 다운스트림 인터페이스 contract에 정의된 필수 필드를 채워야 한다. 다운스트림 단계(TD/APP/CT)는 이 필드들이 존재한다고 가정한다.

> 파일 명명 규칙과 저장 경로는 [pre_specification_ko.md](pre_specification_ko.md) §파일 명명 규칙을 참조한다.
