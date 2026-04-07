# Phase 1 — 사전 준비 절차 (PRE)

> **목적.** 이질적인 소스 문서를 Document 단위로 정규화하고, 검증된 제목 구조 및 청크 계획을 생성하며, 다운스트림 추출을 위한 Work Unit을 할당한다. PRE는 Instruction 수준의 추출(TD, APP, CT)을 수행하지 않는다 — 이는 별도로 처리된다.
> **사용자.** 이 문서는 LLM 실행 지시서(System Prompt)입니다. Claude Code 등 에이전트 런타임이 이 파일을 읽고 절차를 자동 수행합니다. 사람이 직접 실행하는 매뉴얼이 아닙니다.
---

## 입력

| # | 입력물 | 필수 여부 | 설명 |
|:---:|:---|:---:|:---|
| 1 | 대상 문서 | 필수 | IMO, IACS, KR 등 기타 선급의 협약, 규정, 지침서 등 처리 대상 소스 문서 (`.md`, `.pdf`, `.html`, `.xml`, `.json`). 단일 파일, 복수 파일, 또는 폴더 경로로 제공 |
| 2 | 공통 정의서 | 필수 | `shared/` 디렉토리의 용어·식별자·명명규칙·분류체계 (`project_definitions.md`, `naming_convention.md`, `document_classification.md`, `thresholds.yaml`) |
| 3 | 단계별 지침서 | 필수 | 각 Stage의 실행 규칙 (`step1_document_split.md`, `step2_heading_extraction.md`, `step3_workunit_packing.md`) |

> **진입 조건:** PRE는 대상 문서 제공 즉시 시작되며, Step 1.0에서 처리 범위를 확정한다.

---

## 산출물 카탈로그

### 프로모션 산출물 (영구 — 승인 후 `results/`로 이동)

| # | 산출물 | 파일명 | 생성 단계 | 설명 |
|:---:|:---|:---|:---|:---|
| 1 | 제목 구조 TSV | `doc-{doc_instance_key}__heading__structure.tsv` | Step 2 | 토큰 측정값(포함 + 배타)이 포함된 최종 검증된 제목 목록 |
| 2 | 제목 정규식 사양 | `doc-{doc_instance_key}__heading__regex_spec.json` | Step 2 | 확정된 정규식 사양; 동일 DocType 문서에 재사용 가능 |
| 3 | 파일 메타데이터 | `file-{source_file_key}__pre__meta.json` | Step 1.1 | 원본 경로, 형식, 변환 날짜, 문자 수, 토큰 수, 파서 버전, 줄바꿈 정책, grammar_version (제목 추출 후 설정) |
| 4 | 정규화된 텍스트 | `file-{source_file_key}__pre__normalised.md` | Step 1.1 | 정규화된 문서 텍스트 (`.md` 원본에는 생성하지 않음) |
| 4a | 문서 분할 | `doc-{doc_instance_key}__pre__split.md` | Step 1.2 | 다중 문서 소스 파일에서 추출된 개별 문서 분할 파일 |
| 5 | 제목 문법 | `doctype-{DocType}__heading__grammar_v{NN}.md` | Step 2 | DocType별 재사용 가능한 제목 문법 (Coordinator가 관리) |
| 6 | WU 메타데이터 | `wu-{wu_key}__pre__meta.json` | Step 3.2 | WU 구성, 구성 문서, 토큰 수 |
| 7 | **PRE 매니페스트** | `corpus__pre__manifest.json` | Step 3.3 | 모든 PRE 출력의 마스터 인덱스 — 다운스트림 단일 진입점 |
| 7a | Document 매니페스트 | `corpus__pre__document_manifest.jsonl` | Step 1.2 | 문서별 레지스트리: 소스 경로, 분할 경로, 정규화 경로, 해시, 상태 |
| 7b | 청크 계획 | `doc-{doc_instance_key}__heading__chunk_plan.json` | Step 3.1 | 청크 경계, 토큰 크기; 제목 구조 TSV와 별도. 항상 프로모션됨. |
| 7c | 최종 불일치 로그 | `doc-{doc_instance_key}__heading__discrepancy_final.tsv` | Step 2 | 승인 후 감사 추적을 위해 보존된 Warning/Info 항목 |
| 8 | 커버리지 보고서 | `doc-{doc_instance_key}__heading__coverage.json` | Step 2 Pass 4 | 줄 수준 분류 감사 (제목 vs 비제목). 조건부 프로모션 (사용자 요청 시). |
| 9 | 정규식 러너 스크립트 | `scripts/step2_regex_runner.py` | Step 2 | 정규식 사양을 정규 입력에 대해 실행하는 고정 러너. Pass 2–4에서 전수 매치 셋을 생성. 모든 문서에 재사용. |

---

## 수행 절차

| 스테이지 | 단계 | 작업 | 상세 | 입력 | 출력 |
|:---:|:---|:---|:---|:---|:---|
| **1** | Step 1.0 | 사용자 요청 확인 | [step1_document_split.md](step1_document_split.md) §Step 1.0 | 사용자 입력(파일/폴더/특별 지시) | 확정된 대상 파일 목록 |
| **1** | Step 1.1 | 입력 정규화 | [step1_document_split.md](step1_document_split.md) §1.1 | 대상 파일 목록 | 정규화된 `.md` + `meta.json` |
| **1** | Step 1.2 | 소스 패밀리 탐지, Document 식별 및 분할 | [step1_document_split.md](step1_document_split.md) §1.2 | 정규화된 Document 파일 | Document 목록 + split 파일 |
| **1** | Step 1.2.2 | 소규모 인접 문서 병합 | [step1_document_split.md](step1_document_split.md) §1.2.2 | Document 목록 + 토큰 추정 | 병합된 처리 단위 (≤ {{merge_threshold:32K}}) + `corpus__pre__document_manifest.jsonl` |
| **2** | Step 2.1 | 제목 추출 (에이전트별 Pass 1–3; 병합 후 문서 수준 Pass 4) | [step2_heading_extraction.md](step2_heading_extraction.md) §2.1 | 정규 입력 문서 | `doc-{doc_instance_key}__heading__structure.tsv`, `doc-{doc_instance_key}__heading__regex_spec.json`, `doctype-{DocType}__heading__grammar_v{NN}.md` |
| **2** | Step 2.2 | 토큰 측정 | [step2_heading_extraction.md](step2_heading_extraction.md) §2.2 | 제목 구조 TSV | 제목별 Est_Tokens(포함/배타) |
| **3** | Step 3.1 | 컨텍스트 윈도우 청킹 | [step3_workunit_packing.md](step3_workunit_packing.md) §3.1 | 제목 구조 TSV + 토큰 측정값 | 청크 계획 |
| **3** | Step 3.2 | Work Unit 패킹 | [step3_workunit_packing.md](step3_workunit_packing.md) §3.2 | 청크 계획 + Document 메타데이터 | WU 목록 + `wu-{wu_key}__pre__meta.json` |
| **3** | Step 3.3 | 승인 및 산출물 프로모션 | [step3_workunit_packing.md](step3_workunit_packing.md) §3.3 | 청킹 계획 + WU 패킹 계획 + Document 목록 | 승인 → 산출물 프로모션 → `corpus__pre__manifest.json` |

---

## 완료 조건

다음 조건이 **모두** 충족되면 PRE가 완료된다.

| # | 조건 | 근거 |
|:---:|:---|:---|
| 1 | 모든 대상 문서에 대해 `doc-{doc_instance_key}__heading__structure.tsv`가 생성되었다 | Step 2 |
| 2 | 제목 추출 수렴 기준을 충족한다: Error 0건, Warning ≤ max(3, ⌈총 제목 수 × 0.02⌉) | Step 2 §Convergence Criteria |
| 3 | 모든 문서에 대해 토큰 측정(Inclusive/Exclusive)이 완료되었다 | Step 2 C |
| 4 | 청크 계획과 WU 패킹 계획이 생성되었다 | Step 3.1–3.2 |
| 5 | 사용자가 `approve_all` 또는 `approve_partial`로 승인하였다 | Step 3.3 |
| 6 | 승인된 산출물이 `results/`로 프로모션되었다 | Step 3.3 §Artefact Promotion |
| 7 | `corpus__pre__manifest.json`이 생성되어 다운스트림에서 소비 가능하다 | Step 3.3 |

> `approve_partial`인 경우, 승인된 WU만 프로모션되고 나머지는 `held` 상태로 유지된다. `held` WU가 남아 있어도 승인된 WU에 대해서는 다운스트림 진행이 가능하다.

---

# 공통 규칙

| shared 파일 | 내용 |
|:---|:---|
| [`project_definitions.md`](../shared/project_definitions.md) | 용어(HD/TD/APP/CT), 식별자 체인(DocumentKey → Heading_ID), 토큰 측정 기준(Inclusive/Exclusive, 임계값), 승인 상태 |
| [`naming_convention.md`](../shared/naming_convention.md) | 파일명 3-part 패턴, scope/phase/artifact 분류, 저장 경로, DocumentKey slug 규칙 |
| [`document_classification.md`](../shared/document_classification.md) | 도메인 분류 체계 — Authority, DocType, Source Family, Heading Level |
| [`thresholds.yaml`](../shared/thresholds.yaml) | 모든 수치 임계값과 제한값을 하나의 파일에 집약. Md 파일은 `{{key:value}}` 플레이스홀더로 값을 참조; `scripts/update_thresholds.py`로 변경 전파. |

## 에이전트 수명 주기

| # | 스테이지 | 단계 | 할당 에이전트 수 | 생성 시점 | 종료 시점 |
|:---|:---|:---|:---|:---|:---|
| 1 | **Stage 1** | Step 1.2 | 파일당 1개 | 파일 목록 확정 시 | Document 목록 취합 직후 |
| 2 | **Stage 2** | Step 2 | Document 또는 documentSplit당 1개 | Document 목록 확정 후 | 소형: 제목 구조 TSV 완료 후. 대형(documentSplit): Pass 3 완료 후 |
| 3 | **Stage 2** | Step 2 (대형 문서 Pass 4 전용) | Document당 1개 | Coordinator가 documentSplit 결과와 문법을 병합한 후 | 문서 수준 Pass 4 완료 후 |
| — | **Stage 3** | Step 3 | Coordinator 전용 (작업 에이전트 없음) | 해당 없음 | 해당 없음 |

> 각 스테이지는 이전 스테이지와 독립적인 **새 에이전트**를 생성한다. 에이전트는 가용 에이전트 수만큼 병렬로 할당되며, 초과 항목은 배치로 실행된다.

> **참고:** Step 1.1(정규화)은 비`.md` 문서에 대해 각 Step 1.2 에이전트 내에서 분할 전 내부 전처리로 실행된다. Step 1.1을 위한 별도 에이전트는 생성되지 않는다.

## Coordinator 역할

Coordinator는 모든 스테이지에 걸쳐 에이전트 수명 주기를 관리하는 **단일 오케스트레이션 프로세스**이다. 작업 에이전트가 **아니며** — 제목 추출이나 콘텐츠 분석을 수행하지 않는다.

| 책임 | 설명 |
|:---|:---|
| 배치 스케줄링 | 대기 항목을 가용 에이전트 수에 맞게 배치로 분할 |
| 상태 관리 | 각 처리 항목의 수명 주기 상태 추적 |
| 문법 버전 잠금 | 동시 문법 후보 업데이트 직렬화(단일 기록자). 문법 후보는 `staging/`에 저장; Coordinator만이 `results/grammars/`로 프로모션. |
| documentSplit 병합 | documentSplit 제목 결과 병합, 경계 충돌 해결, Heading_ID 재할당 |
| 조상 컨텍스트 | 각 documentSplit에 대해 활성 조상 스택(documentSplit 시작점의 상위 제목 체인)을 제공하여 계층 연속성 유지 |
| 재시도 | 실패 항목을 백오프와 함께 재큐잉; 최대 3회 재시도 후 에스컬레이션 |
| 승인 | 통합 결과를 사용자 승인에 제시; 승인 시 산출물 프로모션 |
| WU 패킹 | WU 토큰 범위 규칙 적용, WU_Key 할당, WU 메타데이터 생성 |

## 오류 처리

| 오류 유형 | 조치 |
|:---|:---|
| **일시적** (API 타임아웃, 429/503) | 최대 3회 자동 재시도, 지수 백오프 (30초, 60초, 120초) |
| **복구 가능** (컨텍스트 윈도우 초과) | 더 작은 콘텐츠 예산으로 자동 재샤딩; 재시도. 2회 재샤딩 실패 후 에스컬레이션. |
| **치명적** (파일 미발견, 지원되지 않는 형식, 지속적 파싱 실패) | 즉시 `escalated`로 표시; 사용자에게 보고 |

## Work Unit 수명 주기 상태

```
planned → running → completed → validated → approved → promoted
                                           ↘ held (부분 승인) → approved (재승인)
                  ↘ failed → retryable → running (재시도)
                             ↘ escalated (최대 재시도 초과)
```

> `merged`는 WU 수명 주기 상태가 아니다 — WU_Type (`standalone`, `split`, `merged`)이다. `promoted`는 산출물이 `results/temp/pre/`에서 `results/`로 이동되었음을 의미한다.

## PRE 매니페스트 — 다운스트림 인터페이스 계약

`corpus__pre__manifest.json`은 PRE와 다운스트림(TD/APP/CT) 간의 **인터페이스 계약**이다. PRE는 아래 필드를 반드시 채워서 넘기고, 다운스트림은 이 필드가 존재한다고 가정하고 소비한다. 최소 필수 필드:

| 필드 | 설명 |
|:---|:---|
| `run_id` | 고유 실행 식별자 |
| `created_at` | ISO 8601 타임스탬프 |
| `documents[]` | 문서 항목 배열 |
| `documents[].doc_instance_key` | DocumentInstanceKey |
| `documents[].document_key` | DocumentKey |
| `documents[].authority` | 발행 기관 |
| `documents[].doc_type` | DocType |
| `documents[].language` | 언어 코드 (ISO 639-1) |
| `documents[].source_path` | 원본 파일 경로 |
| `documents[].source_hash` | 원본 파일의 SHA-256 |
| `documents[].normalised_path` | 정규화 파일 경로 (`.md` 원본이면 null) |
| `documents[].canonical_input_path` | 다운스트림 원본 소스 파일 경로 |
| `documents[].document_split_path` | Document 분할 파일 경로 (단일 문서면 null) |
| `documents[].heading_count` | 추출된 제목 수 |
| `documents[].est_tokens` | 총 문서 토큰 수 |
| `documents[].grammar_version` | 사용된 DocType 문법 버전 |
| `documents[].status` | `approved`, `held`, `escalated` |
| `work_units[]` | WU 항목 배열 |
| `work_units[].wu_key` | WU_Key |
| `work_units[].wu_type` | `standalone`, `split`, `merged` |
| `work_units[].constituent_doc_instance_keys[]` | DocumentInstanceKey 목록 |
| `work_units[].est_tokens_total` | 총 WU 토큰 수 |
| `work_units[].status` | `approved`, `held`, `escalated` |
| `work_units[].promoted_files[]` | 프로모션된 파일 경로 목록 |
| `open_warnings` | 미해결 Warning 심각도 항목 수 |
| `oversize_exceptions` | 초과 크기 리프 예외 수 |
| `token_method` | `tiktoken` 또는 `char_approx` |
| `tokenizer_version` | 토크나이저 식별자 |

> **참고:** `documents[].status`는 `corpus__pre__document_manifest.jsonl`의 `confirmed`에서 승인 단계 후 `corpus__pre__manifest.json`의 `approved`/`held`/`escalated`로 전환된다.

---

*관련 문서:*
- *[step1_document_split.md](step1_document_split.md) — Document 식별, 분할, 정규화*
- *[step2_heading_extraction.md](step2_heading_extraction.md) — 제목 추출 에이전트별 Pass 1–3, 문서 수준 Pass 4, TSV 스키마*
- *[step3_workunit_packing.md](step3_workunit_packing.md) — 청킹, WU 패킹, 승인*
- *제목 명령어: `pre_skos/phase1_heading_instruction.md`*
- *Task Brief 생성기: `pre_skos/task_brief/task_brief_generator.md`*
- *추출 에이전트 운영: `commands/agents.md`*
