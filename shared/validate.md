# PRE 문서 검증

대상:

- `prerequisite/` — pre_specification.md, step1_document_split.md, step2_heading_extraction.md, step3_workunit_packing.md
- `shared/` — naming_convention.md, project_definitions.md, document_classification.md

> `prerequisite/` 문서는 용어, 식별자, 분류 정의를 자체적으로 포함하지 않으며, `shared/`를 참조합니다. 검증 시 `shared/` 원본과 `prerequisite/` 참조 간의 일관성을 확인하세요.

---

## 모드 선택

| 인수 | 실행 범위 |
|:---|:---|
| `lint` | A만 실행 |
| `script` | B만 실행 |
| `llm` | C만 실행 |
| `semantic` | B + C 실행 |
| (없음) | A + B + C 전체 실행 |

인수: $ARGUMENTS

---

## A. markdownlint

`prerequisite/.markdownlint.json` 설정을 사용하여 4개 파일을 린트합니다. 오류가 0건이면 PASS; 그렇지 않으면 테이블로 요약하고, 자동 수정 후 재실행합니다.

---

## B. 스크립트 기반 검증 (Script — 6개 항목)

regex, 패턴 매칭, 집합 비교를 통해 기계적으로 판정할 수 있는 항목입니다. 각 항목은 PASS/FAIL/WARN으로 판정합니다.

### B1 식별자 형식 일관성

4개 `prerequisite/` 문서 + `shared/project_definitions.md`에서 regex로 식별자 패턴을 추출하여 비교합니다.

### B2 파일 명명 규칙 준수

모든 파일명 예시를 추출하고 스크립트를 작성하여 형식에 맞는지 검증한다.

### B3 산출물 번호 매핑

제공된 문서에서의 산출물 번호를 확인하고 산출물 결과와 비교한다.

### B5 상호 참조 유효성

대상 문서 전체에서 참조 패턴을 추출하고, 참조 대상의 실재 여부를 검증한다.

1. **참조 추출**: `§`, `[...](...)` 형태의 모든 참조를 수집한다.
2. **섹션 참조 검증**: `§` 뒤에 명시된 제목이 대상 문서의 실제 헤딩(`##`, `###` 등)과 일치하는지 대조한다.
3. **파일 경로 검증**: 링크에 포함된 상대/절대 경로가 실제 파일을 가리키는지 확인한다.
4. **판정**: 무효 참조(깨진 링크, 존재하지 않는 섹션)가 1건 이상이면 FAIL

### B9 승인 상태 목록 일관성

4개 상태 `approve_all`, `approve_partial`, `revise_and_rerun`, `reject`를 추출하고 다음을 비교한다.

### B10 스키마 필드 교차 검증

대상 문서에 정의된 모든 스키마를 식별하고, 스키마 간 필드 일관성을 검증한다.

1. **스키마 식별**: 각 문서에서 스키마 정의(JSON Schema, 테이블, 필드 목록 등)를 추출하고 목록화한다.
2. **공통 필드 탐지**: 2개 이상의 스키마에 동일 필드명이 등장하는 경우를 수집한다.
3. **존재 일관성**: 공통 필드가 관련된 모든 스키마에 빠짐없이 존재하는지 확인한다.
4. **값 도메인 정합성**: 동일 필드의 허용값(enum, 상태값 등)이 스키마 간에 호환되는지, 전이 관계가 논리적인지 검증한다.
5. **명명 일관성**: 동일 개념을 지칭하는 필드가 스키마마다 다른 이름을 사용하고 있지 않은지 확인한다.
6. **판정**: 불일치 또는 누락이 1건 이상이면 FAIL

---

## C. LLM 기반 검증 (의미론적 — 4개 항목)

문맥 이해와 논리적 일관성 판단이 필요한 항목으로, LLM이 수행한다. 각 항목은 PASS/FAIL/WARN으로 판정한다.

### C1 Token 지표 일관성

`shared/project_definitions.md`의 token 정의가 `prerequisite/` 문서들에서의 사용과 의미적으로 일관되는지 검증한다.

- Inclusive/Exclusive 정의가 step2 §C에서의 사용과 일관되는지 여부
- 덧셈 공식(`parent.Exclusive + Σ(children.Inclusive) = parent.Inclusive`)이 모든 문서에서 동일하게 기술되어 있는지 여부
- `char_approx ×1.1` 안전 마진이 일관되게 적용되는지 여부
- 임계값(documentSplit 64K, Chunk 32K, WU 16K-32K)이 상호 논리적인지 여부 (documentSplit > Chunk ≥ WU Upper)

### C2 Promotion 규칙 일관성

pre_specification.md §Artefact Catalogue와 step3 §Artefact Promotion의 promotion 분류가 일치하는지 검증한다.

- `chunk_plan`: "항상 promote됨"으로 일관되게 기술되는지
- `coverage`: "조건부 promote(사용자 요청 시)"로 일관되게 기술되는지
- `discrepancy_final`: promote됨(감사 추적)으로 일관되게 기술되는지
- Step 2 중간 산출물(카탈로그 번호 없음): "promote 후 폐기"로 일관되게 기술되는지

### C3 Agent 및 Coordinator 생명주기

pre_specification.md §Agent Lifecycle/§Coordinator Role과 step1/step2의 기술 내용이 논리적으로 일관되는지 검증한다.

- Step 1.2가 Step 1.1 agent 내부의 전처리로 실행되는지 여부 (별도 agent 없음)
- Stage 3이 Coordinator 단독으로 수행되는지 여부 (worker agent 없음)
- agent 생성/종료 시점이 step 문서와 pre_specification.md 간에 일치하는지 여부
- documentSplit agent → Coordinator merge → Pass 4 agent 흐름이 step2와 pre_specification.md 간에 일치하는지 여부

### C4 Grammar 생명주기 연속성

Grammar의 전체 생명주기가 step2/step3/pre_specification.md 전반에 걸쳐 빈틈 없이 연결되는지 검증한다.

- staging/ 저장 → Coordinator merge → 버전 증가 → promotion → Pass 4에서의 사용
- Pass 4 이후 grammar 갱신 → 재병합 → 최종 promotion
- `meta.json`의 `grammar_version` 필드가 최종 promote된 버전을 기록하는지 여부
- merge 적격성 판단 시 `grammar_version` 일치가 필요한지 여부 (step3 §Merge Constraints)

---

## 보고서 형식

```
## 검증 결과

| 검증 항목 | 결과 |
|:---|:---|
| A. markdownlint | ?/4 PASS |
| B. Script-Based Validation | ?/6 PASS |
| C. LLM-Based Validation | ?/4 PASS |

종합: PASS 또는 FAIL
```

FAIL 시 상세 발견 사항과 조치 방안을 우선순위 순으로 나열한다.
