# Phase 1: TRUE_DEF 통제 어휘 작업 지침서

> **Pre-SKOS 단계**: 이 단계는 Phase 2에서 SKOS `skos:broader` / `skos:related` 계층 및 연관 관계를 구축하기 위한 준비 단계입니다. Phase 1에서는 원문 충실 정의 추출 및 플랫 테이블 목록화에 집중하며, 정식 SKOS 의미 관계는 후속 단계에서 구축됩니다.

> **범위**: 정식 정의 섹션(TRUE_DEF)에서 직접 확인된 정의만 추출 및 정제합니다.
> DESCRIPTION, PARAPHRASE, 기술 용어, 약어 등록부 및 JSON/OWL 변환의 분류는 Phase 2 이후로 연기됩니다.
> **작업 절차**: 모든 원문 텍스트를 순차적으로 읽고 처리합니다.
> **작업 준비**: 사용자가 검토를 요청할 때, 대상 자료를 약 100K 토큰 단위의 세그먼트로 분할하여 순차적으로 처리합니다.
---

## 0. 사전 준비

LLM과 사용자가 대상 문서를 공동으로 검토하고 기준 데이터를 추출하는 준비 단계입니다. 각 지침서(TRUE_DEF, APPLICABILITY, CONTROLLED_TERM)는 독립적으로 실행됩니다.

1. **문서 검토** — 대상 문서를 읽고 용어 정의 패턴을 식별합니다 (예: "means", 굵은 글씨 서식, 정의 목록).
2. **추출 범위 설정** — 정의 섹션에서 용어 관련 문장만 추출합니다. 추출된 문장은 중간 디렉토리(`results/temp/`)에 저장합니다.
3. **패턴 목록화** — 2단계에서 추출된 문장을 분석하고 패턴 카탈로그(`results/temp/extraction_patterns_true_def.tsv`)를 작성합니다. 반복되는 문장 구조를 기록합니다 (예: `"X means..."`, `"X is defined as..."`, `"For the purpose of this..."`, 굵은 글씨 표제어 뒤에 정의 텍스트). 이 카탈로그는 두 가지 목적으로 사용됩니다: (a) 분리 스크립트가 패턴을 사용하여 나머지 부분에서 **잠재적 누락을 자동 표시**할 수 있고, (b) 패턴을 **교차 지침서 분류 점검**에 재사용할 수 있습니다 (예: APPLICABILITY 유형 문장이 TRUE_DEF 추출에 실수로 포함된 경우 감지).
4. **추출 분리** — 원본 문서와 `results/temp/`의 추출 문장에 대해 분리 스크립트를 실행하여 두 가지 출력을 생성합니다: (a) **추출된 문장** (매칭됨) 및 (b) **미추출 문장** (매칭되지 않은 나머지). 스크립트는 3단계의 패턴 카탈로그를 적용하여 알려진 정의 패턴과 일치하는 나머지 문장을 **누락 후보**로 표시합니다. LLM이 초기 추출(2단계)을 수행하고, 분리 및 패턴 매칭은 기계적 완전성을 보장하기 위해 스크립트가 수행합니다.
5. **추출 검증** — LLM이 미추출 문장(4단계의 매칭되지 않은 나머지)을 검토하며, 스크립트가 표시한 누락 후보를 우선적으로 확인하여 필요한 정의 문장이 누락되지 않았는지 검증합니다. 누락이 발견되면 추출 세트에 추가하고, 새로운 패턴이 식별되면 패턴 카탈로그를 업데이트한 후 분리 스크립트를 재실행합니다.

---

## 1. 채택 규칙

| 조건 | 포함 | 제외 (Phase 2 백로그) |
|:---|:---|:---|
| 출처 위치 | 정식 "정의" 섹션 (본문 또는 명시적 정의를 포함하거나 정의적 권한으로 명시적으로 편입된 규범적 부속서에 한함) | 본문, 각주, 참고 부속서 |
| 기록 유형 | **TRUE_DEF**만 해당 | DESCRIPTION, PARAPHRASE |
| 출처 | IMO 협약/코드/결의/회보, IACS UR/UI/Rec/PR, KR 규칙/기술규칙/지침/해석, EU 지침/규정/결정 (현행 문서 — 전체 목록은 3.6절의 Source_Doc_Type 열거 참조) | ISO/IEC 순수 위임 ("ISO X에서 정의된 바와 같이") |
| 문서 | 현행 문서만 해당 | 발효 전 폐지된 문서 |
| 언어 | 영어만 해당 (데이터 셀) | 한국어 텍스트는 영어로 대체 |

**한 줄 판정**: 해당 용어가 문서의 정의 섹션에서 명시적으로 정의되어 있는가? — **예 → 채택**, 아니오 → 백로그.

---

## 2. 핵심 원칙: 출처별 개념

IMO/IACS/KR/EU가 동일한 표제어를 사용하더라도 정의와 범위가 다를 수 있습니다.

- **Phase 1에서는 각 출처를 별도의 개념으로 등록합니다.** 하나의 공통 개념으로 병합하지 않습니다.
- 출처 간 매핑(closeMatch/exactMatch)은 Phase 2에서 수행합니다.
- 동일 문서 내에서도 정의가 섹션별로 다르면 별도의 개념으로 분리합니다.

---

## 3. 목표 스키마

```
Concept_ID | Record_Type | Scheme | Source_Doc_Type | prefLabel@en | altLabel@en | Definition@en | Scope_Note@en | Example@en | Source_Doc | Source_Locator | Editor_Note
```

### 3.1 의무 수준별 컬럼 정의

| # | 컬럼 | 의무 수준 | SKOS 매핑 | 데이터 유형 | 카디널리티 | 규칙 |
|:---:|:---|:---:|:---|:---|:---|:---|
| 1 | **Concept_ID** | **필수** | URI 프래그먼트 | ID | 단일 | 형식: `{Scheme}_{SourceKey}_TD_{SeqNo}`. 예: `IACS_S11A_TD_001`, `IMO_SOLAS_II_1_TD_012`, `KR_PT3_CH1_TD_005`. **한번 부여된 Concept_ID는 재번호 부여 불가; 번호 갭은 허용됩니다.** 식별자의 점, 괄호 및 기타 특수 문자는 정규화를 위해 제거하거나 밑줄(`_`)로 대체합니다 (예: `Pt.3 Ch.1` → `Pt3_Ch1`). `_TD_` 삽입어는 TRUE_DEF 레코드를 APPLICABILITY(`_APP_`) 및 CONTROLLED_TERM(`_CT_`) 레코드와 구별합니다. |
| 2 | **Record_Type** | **필수** | `dct:type` | 열거형 | 단일 | `TRUE_DEF`로 고정. TRUE_DEF와 APPLICABILITY 레코드가 하나의 시트에 공존할 수 있도록 하는 구별자입니다. |
| 3 | **Scheme** | **필수** | `skos:inScheme` | 열거형 | 단일 | `IMO`, `IACS`, `KR`, `EU` 중 하나. 출처 기관을 식별합니다. |
| 4 | **Source_Doc_Type** | **필수** | `dct:type` (부차적) | 열거형 | 단일 | 문서 장르를 분류합니다. 닫힌 목록의 값 (3.6절). APPLICABILITY 및 CONTROLLED_TERM 지침서와 공유됩니다. |
| 5 | **prefLabel@en** | **필수** | `skos:prefLabel` | 텍스트 | 단일 | 언어당 하나. 문장형 대문자(Sentence case). 기본적으로 단수형 (예외: scantlings, bilges) |
| 6 | **altLabel@en** | 선택 | `skos:altLabel` | 텍스트-다중 | 다중 | 약어, 두문자어, 정당한 변형. 세미콜론(`;`)으로 구분 |
| 7 | **Definition@en** | **필수** | `skos:definition` | 텍스트 | 단일 | 분리 패턴(4절)에 의해 식별된 비정의적 부속 요소 분리 후 정의 핵심만 원문 그대로 유지. 편집이나 의역 금지 |
| 8 | **Scope_Note@en** | 조건부 | `skos:scopeNote` | 텍스트 | 단일 | 적용 범위, 도메인 제한, 제외 사항 (원문에서 추출). **원문 정의에 범위 제한 또는 제외 표현이 포함된 경우 기입. APPLICABILITY 레코드의 경우, 이 역할은 `Applicability_Text@en`이 수행합니다 (APPLICABILITY 지침서 참조).** |
| 9 | **Example@en** | 조건부 | `skos:example` | 텍스트 | 단일 | "예: Type A, B, C" 및 기타 열거/예시 꼬리문. 하위 유형을 나타내는 경우, Editor_Note에 `[narrower candidate]`로 표시. **원문에 예시 또는 열거 표현이 포함된 경우 기입.** |
| 10 | **Source_Doc** | **필수** | `dcterms:source` | 텍스트 | 단일 | UR/IMO/KR/EU 문서 식별자. 예: `UR S11A`, `SOLAS II-1`, `KR Rules Pt.3`, `Directive 2009/45/EC` |
| 11 | **Source_Locator** | **필수** | (dcterms:source 내 위치자) | 텍스트 | 단일 | 절/표/부속서 위치. 예: `1.2.1`, `Table 3`, `Annex II` |
| 12 | **Editor_Note** | 선택 | `skos:editorialNote` | 텍스트 | 단일 | 추출 근거, QA 코멘트, 패턴 플래그, 이전 버전 이력 |

#### 의무 수준 범례

| 의무 수준 | 의미 |
|:---|:---|
| **필수** | 항상 기입해야 합니다. 이 항목 없이는 레코드가 유효하지 않습니다. |
| **조건부** | 원문 텍스트에 관련 정보가 포함된 경우 기입해야 합니다. 기재되지 않은 경우 빈칸으로 둡니다. |
| **선택** | 가용하고 유용한 경우 기입합니다. 이 항목 없이도 레코드는 유효합니다. |

### 3.2 APPLICABILITY 및 CONTROLLED_TERM 레코드와의 상호운용성

TRUE_DEF와 APPLICABILITY 레코드가 하나의 시트에 공존할 때:

| 측면 | TRUE_DEF | APPLICABILITY | 해결 방안 |
|:---|:---|:---|:---|
| **구별자** | `Record_Type` = `TRUE_DEF` | `Record_Type` = `APPLICABILITY` | `Record_Type`이 두 유형의 단일 구별자 필드 |
| **Source_Doc_Type** | 있음 (3.6절) | 있음 (APPLICABILITY 3.6절) | 두 레코드 유형 모두 동일한 Source_Doc_Type 닫힌 목록을 공유 |
| **범위 텍스트** | `Scope_Note@en` (정의에서 추출된 범위) | `Applicability_Text@en` (원문 그대로의 적용성 기술, 앵커 필드) | 둘 다 `skos:scopeNote`에 매핑되지만 역할이 다름: Scope_Note는 정의 내에 포함된 범위를 포착; Applicability_Text는 구조적 분해를 위한 독립 앵커 |
| **Scheme** | `IMO`, `IACS`, `KR` 또는 `EU` | `IMO`, `IACS`, `KR` 또는 `EU` | 두 레코드 유형 모두 동일한 Scheme 값 집합을 공유 |
| **APPLICABILITY 전용 컬럼** | 빈칸 (Target_Entity, Ship_Type 등) | APPLICABILITY 지침서에 따라 기입 | 검증은 Record_Type에 따라 조건부로 수행 |

TRUE_DEF와 CONTROLLED_TERM 레코드가 공존할 때:

| 측면 | TRUE_DEF | CONTROLLED_TERM | 해결 방안 |
|:---|:---|:---|:---|
| **구별자** | `Record_Type` = `TRUE_DEF` | `Record_Type` = `CONTROLLED_TERM` | `Record_Type`이 단일 구별자 |
| **정의** | `Definition@en` (원문 그대로의 정식 정의) | `Definition_Context@en` (사용 맥락, 정식 정의 아님) | 용어에 둘 다 있는 경우 TRUE_DEF 정의가 우선 |
| **출처 위치** | 정식 정의 섹션 | 본문 (규범적 요건) | 겹치지 않는 출처 위치 |
| **Scheme** | `IMO`, `IACS`, `KR` 또는 `EU` | `IMO`, `IACS`, `KR` 또는 `EU` | 네 가지 Scheme 값 모두 공유 |
| **CONTROLLED_TERM 전용 컬럼** | 빈칸 (Term_Category, Term_Subclass 등) | CONTROLLED_TERM 지침서에 따라 기입 | 검증은 Record_Type에 따라 조건부로 수행 |

### 3.3 Concept_ID/URI 설계

- **일반 패턴**: `{Scheme}_{SourceKey}_TD_{SeqNo}`
  - `Scheme`: `IMO`, `IACS`, `KR` 또는 `EU`
  - `SourceKey`: 정규화된 원문 단위 키 (문서 수준)
  - `_TD_`: TRUE_DEF 레코드를 구별하는 고정 삽입어
  - `SeqNo`: 해당 원문 단위 내 지역적 3자리 일련번호

#### 출처 계열별 예시

| 출처 계열 | 원문 문서 | Concept_ID 예시 |
|:---|:---|:---|
| **IACS** | UR S11A | `IACS_S11A_TD_001` |
| **IACS** | UR Z10.1 | `IACS_Z10_1_TD_001` |
| **IMO** | SOLAS Ch.II-1 | `IMO_SOLAS_II_1_TD_001` |
| **IMO** | MARPOL Annex I | `IMO_MARPOL_AI_TD_001` |
| **KR** | Rules Pt.3 Ch.1 | `KR_PT3_CH1_TD_001` |
| **EU** | Directive 2009/45/EC | `EU_DIR_2009_45_TD_001` |
| **EU** | Regulation (EU) 2015/757 | `EU_REG_2015_757_TD_001` |

#### SourceKey 정규화 규칙

> **1~5단계**는 세 가지 지침서(TRUE_DEF / APPLICABILITY / CONTROLLED_TERM) 모두에서 동일한 공유 핵심 규칙입니다. Concept_ID가 예측 가능하고 교차 연결 가능하도록 일관되게 적용합니다. **6~7단계**는 IMO 코드 및 EU 법규에 대한 출처 계열별 약어 패턴을 처리합니다.

| 단계 | 규칙 | 예시 |
|:---:|:---|:---|
| 1 | 점, 괄호, 쉼표를 밑줄로 대체 (단어 경계에 있으면 제거) | `Z10.1` → `Z10_1`; `Pt.3 Ch.1` → `Pt3_Ch1` |
| 2 | `/` 및 `-`를 `_`로 대체 | `II-1/3-8` → `II_1_3_8` |
| 3 | 연속 밑줄 축약 | `II__1` → `II_1` |
| 4 | 대문자 사용 | `Pt3_Ch1` → `PT3_CH1` |
| 5 | 문서 유형 접두사 제거 (이미 패턴에 포함) | `UR S11A` → `S11A` |
| 6 | IMO 코드: 표준 약어 사용 | `FSS Code` → `FSS`, `ISM Code` → `ISM` |
| 7 | EU: 연도 + 번호 패턴 | `Directive 2009/45/EC` → `DIR_2009_45` |

- 기본 URI 패턴: `https://{domain}/maritime-cv/{Concept_ID}` — `{Concept_ID}`는 Scheme 접두사를 포함한 전체 값
- 예: `https://example.org/maritime-cv/IACS_S11A_TD_001`
- Phase 1에서는 로컬 ID(`Concept_ID`)만 확정하며, HTTP URI 발행은 인프라가 준비된 후 진행

### 3.6 Source_Doc_Type 통제 값

| 값 | 설명 | 일반 출처 계열 |
|:---|:---|:---|
| `Convention` | 국제 협약 (SOLAS, MARPOL, Load Line, STCW 등) | IMO |
| `Mandatory_Code` | 협약 하의 강제 코드 (IGC, IBC, ISM, ISPS 등) | IMO |
| `Recommendatory_Code` | 권고 코드 및 지침 | IMO |
| `Resolution` | IMO 총회 또는 MSC/MEPC 결의 | IMO |
| `Circular` | MSC/MEPC 회보 및 통일 해석 | IMO |
| `UR` | 통일규칙 (Unified Requirements) | IACS |
| `UI` | 통일해석 (Unified Interpretations) | IACS |
| `Rec` | 권고 (Recommendations) | IACS |
| `PR` | 절차 요건 (Procedural Requirements) | IACS |
| `Rule` | 선급규칙 (강제 요건) | KR |
| `Guidance` | 기술 지침 (권고 관행) | KR |
| `Interpretation` | 규칙의 공식 해석 | KR |
| `Technical_Rule` | 특정 선종 또는 시스템에 대한 기술규칙 | KR |
| `Directive` | 국내법 전환이 필요한 EU 지침 | EU |
| `Regulation_EU` | 직접 적용되는 EU 규정 | EU |
| `Decision` | 특정 수범자에게 구속력 있는 EU 결정 | EU |

> 이 닫힌 목록은 TRUE_DEF, APPLICABILITY, CONTROLLED_TERM 지침서 전체에서 공유됩니다.

---

## 4. 정의 셀 정제 — 분리 패턴

정의 셀에는 **정의 핵심만** 포함되어야 합니다. 다음 패턴에 해당하는 비정의적 부속 요소는 지정된 컬럼으로 분리하며, 나머지 정의 핵심은 원문 그대로 보존합니다.

| # | 패턴 | 식별 기준 | 대상 컬럼 |
|:---:|:---|:---|:---|
| 1 | 법적/기술적 해설 | "but the two roles are legally distinct" | Editor_Note |
| 2 | 대체 명칭 | "Also called...", "Also known as..." | altLabel |
| 3 | 한국어 텍스트 | 한국어 문자 | 영어로 대체 |
| 4 | 참조 주석 | `[-> see UR XX]`, `as defined in` | Editor_Note (교차 참조 기록) |
| 5 | 적용 범위 | `[Note: applies primarily to...]` | Scope_Note |
| 6 | 수식 + 적용 꼬리문 | "Applicable to TM and QT steels..." | Scope_Note |
| 7 | 제외/부정적 범위 | "does not cover...", "does not apply to..." | Scope_Note |
| 10 | 범위 제한 꼬리문 | "This is for all synthetic cordage materials." | Scope_Note |
| 11 | 예시/열거 꼬리문 | "e.g., Type A, B, C" | Example. 하위 유형을 나타내는 경우 `[narrower candidate]`로 표시 |

**Phase 1에서 표시되었으나 연기된 패턴:**

| # | 패턴 | 조치 |
|:---:|:---|:---|
| 8 | 순수 리다이렉트 ("See UR Z18") | `[Phase 2: PARAPHRASE]` 태그 부여 → 백로그 |
| 9 | 내장 하위 정의 | `[Phase 2: extract]` 태그 부여 → 백로그 |

---

## 5. 레이블 정책

| 레이블 유형 | 용도 | 예시 |
|:---|:---|:---|
| `skos:prefLabel` | 기본 레이블. **언어당 하나만** | "ballast water management system"@en |
| `skos:altLabel` | 약어, 두문자어, 정당한 변형 | "BWMS"@en |
| `skos:hiddenLabel` | OCR 변형, 오타, 점 표기 형식 (검색 전용) | "B.W.M.S."@en |

- "Type A, B, C"가 실제 하위 유형인 경우, altLabel로 추가하지 않고 → `[narrower candidate]`로 표시하여 Phase 2에서 별도 개념으로 처리하고 narrower 관계를 부여합니다.
- 약어가 전체 명칭과 동일한 개념을 지칭하는 경우, 독립 개념이 아닌 altLabel로 처리합니다.

---

## 6. 편집 규칙 (Phase 1 요약)

| 규칙 | 내용 |
|:---|:---|
| 언어 | 영어만 해당 (데이터 셀). 한국어는 작업 지침서/내부 노트에서만 허용 |
| 철자법 | 영국식 영어 (moulded, vapour, draught, centre, programme). **TSV 컬럼 헤더는 편의상 `@en`을 사용. RDF로 변환 시, 모든 영어 리터럴은 `@en-GB` 태그(BCP 47 준수)를 사용합니다.** 이 이중 레이어 방식은 헤더의 장황함을 피하면서 최종 RDF 출력에서 방언 정밀도를 보존합니다 |
| 정의 셀 | 비정의적 부속 요소 분리 후 정의 핵심을 원문 그대로 유지. 편집이나 의역 금지 |
| 표제어 대소문자 | 문장형 대문자(Sentence case) |
| 표제어 수 | 기본적으로 단수형. 예외: 관례적으로 복수형인 용어 (scantlings, bilges) |
| 출처 인용 | Source_Doc과 Source_Locator를 분리. `§` 기호를 사용하지 않음 |
| 이중 레이어 | 원문 충실 필드는 원문 텍스트를 보존; 정규화 필드는 사내 스타일을 따름 |

---

## 7. 출처 인용

| 범주 | Source_Doc | Source_Locator 예시 |
|:---|:---|:---|
| IACS UR | `UR S11A` | `2.1.3`, `Table 7`, `Annex III` |
| IACS UI | `UI SC123` | `1.1` |
| IACS Rec | `Rec 87` | `2.3` |
| IACS PR | `PR 38` | `3.1` |
| SOLAS | `SOLAS II-1` | `3.30` |
| IMO 결의 | `IMO Res. MSC.370(93)` | |
| KR 규칙 | `KR Rules Pt.3` | `Ch.1 1.2` |
| EU 지침 | `Directive 2009/45/EC` | `Art.2` |
| EU 규정 | `Regulation (EU) 2015/757` | `Art.3` |

---

## 8. 그룹화 규칙

- 문서 수준, 챕터 수준, 출처 수준 그룹화에 `broader/narrower`를 사용하지 않습니다.
- 출처 수준 그룹화는 `skos:ConceptScheme` (IMO / IACS / KR / EU)으로 처리합니다.
- 문서 수준 또는 주제 수준 하위 그룹화에는 `skos:Collection`을 사용합니다.

---

## 9. 절차

```
1단계  대상 문서의 정의 섹션 확인
2단계  정의 섹션에서 용어 + 정의 추출
3단계  채택 규칙 적용 — TRUE_DEF 적격성 판정
4단계  Concept_ID 부여 (_TD_ 삽입어 포함), Scheme 기록, Source_Doc_Type 설정, Record_Type = TRUE_DEF 설정
5단계  정의 셀 정제 — 패턴 1-7, 10-11 분리
6단계  패턴 8, 9 태그 부여 → Phase 2 백로그
7단계  prefLabel / altLabel 확정
8단계  Source_Doc / Source_Locator 분리 기록
9단계  검증 (10절)
```

---

## 10. 검증

### 10.1 2-Pass 검토

| 검토 | 초점 | 점검 항목 |
|:---|:---|:---|
| **구조적** | 테이블 무결성 | 컬럼 수 일관성 (12개 컬럼), 필수 필드 빈 셀 점검 (조건부/선택 필드는 의무 수준 규칙에 따라 빈칸 가능), Concept_ID 중복 없음, 유효한 Scheme 값, 유효한 Source_Doc_Type 값, `_TD_` 삽입어 존재, Record_Type = `TRUE_DEF` |
| **의미적** | 내용 정확성 | 정의 = 원문 그대로, 정의 내용이 Scope_Note에 혼입되지 않음, 언어당 prefLabel 하나, Record_Type = `TRUE_DEF`만 해당 |

### 10.2 교차 점검 규칙

| 규칙 | 점검 | 심각도 |
|:---|:---|:---|
| 필수 필드 | Concept_ID, Record_Type, Scheme, Source_Doc_Type, prefLabel, Definition, Source_Doc, Source_Locator가 기입되어야 함 | **오류** |
| Record_Type 값 | `TRUE_DEF`여야 함 | **오류** |
| 유효한 Scheme | `IMO`, `IACS`, `KR`, `EU` 중 하나여야 함 | **오류** |
| Source_Doc_Type 값 | 닫힌 목록(3.6절)에서 선택되어야 함 | **오류** |
| Concept_ID 형식 | `{Scheme}_{SourceKey}_TD_{SeqNo}` 패턴에 `_TD_` 삽입어를 포함하여 준수해야 함 | **오류** |
| Concept_ID 접두사 점검 | Concept_ID 접두사가 Scheme 값과 일치해야 함 (`IMO_`, `IACS_`, `KR_`, `EU_`) | **오류** |
| 출처 계열 일관성 | Scheme 값이 Source_Doc 명명과 일관되어야 함 (예: Scheme=`IMO`는 IMO 스타일 Source_Doc을 가져야 함) | **오류** |
| 영어 필드 내 한국어 없음 | Definition, Scope_Note, Example에 한국어 문자가 포함되어서는 안 됨 | **오류** |
| 중복 prefLabel 검토 | 동일 Scheme + 동일 Source_Doc 내에서 같은 언어의 prefLabel이 충돌하면 검토 필요 (경고, 자동 실패 아님) | **경고** |
| `[narrower candidate]` 플래그 | 하위 유형 플래그가 있으면 Phase 2 검토 필요 | **경고** |
| 약어 충돌 | 동일 altLabel이 다른 개념에 사용되면 검토 필요 | **경고** |
| Record_Type 조건부 검증 | Record_Type = `TRUE_DEF`인 경우, APPLICABILITY 전용 컬럼 (Target_Entity, Ship_Type 등)은 빈칸이어야 함 | **오류** |
| 정의 원문 점검 | Definition@en은 패턴 분리 후 원문의 정의 핵심과 일치해야 함; 의역이나 편집 변경 불가 | **오류** |

> **SHACL 참고**: 10.2절 교차 점검 규칙이 규범적 검증 사양입니다. 자동화 검증을 위한 SHACL 셰이프는 Phase 2에서 이 규칙들로부터 생성됩니다 — 이 문서에는 별도의 SHACL 테이블을 유지하지 않습니다.

---

## 11. 출력 사양

모든 최종 출력 파일은 지침서가 실행되는 작업 디렉토리 하위의 **`results/`** 서브디렉토리에 저장됩니다. 청크별 중간 파일(세그먼트 처리 중 생성된 부분 TSV 및 로그 파일)은 **`results/temp/`**에 저장됩니다. 두 디렉토리는 존재하지 않으면 자동으로 생성됩니다. 각 추출 실행은 `results/`에 정확히 **3개의 최종 파일**을 생성합니다: 결과 파일 1개, 요약 파일 1개, 로그 파일 1개. `results/temp/`의 중간 파일은 추적 가능성을 위해 유지되지만 산출물로 간주되지 않습니다.

### 11.1 파일 명명 규칙

| 파일 | 명명 패턴 | 설명 |
|:---|:---|:---|
| **결과** | `phase1_true_def_result.tsv` | TSV 형식(탭 구분 값)의 최종 추출 테이블. 목표 스키마(3절)에 부합하는 모든 추출 레코드를 포함. 헤더 행 1개 + 데이터 행. UTF-8 with BOM. |
| **요약** | `phase1_true_def_summary.md` | 마크다운 형식의 추출 요약 보고서. |
| **로그** | `phase1_true_def_log.md` | 마크다운 형식의 처리 로그. |

### 11.2 결과 파일 (`phase1_true_def_result.tsv`)

- **형식**: TSV (탭 구분 값), UTF-8 with BOM
- **헤더 행**: 3.1절에서 정의된 것과 정확히 동일한 컬럼명, 탭으로 구분
- **컬럼 순서**: `Concept_ID	Record_Type	Scheme	Source_Doc_Type	prefLabel@en	altLabel@en	Definition@en	Scope_Note@en	Example@en	Source_Doc	Source_Locator	Editor_Note`
- **빈 셀**: 빈칸으로 둠 ("N/A" 또는 "-"와 같은 자리 표시 텍스트 사용 금지)
- **다중 값 구분자**: 3.1절에 따라 셀 내에서 세미콜론(`;`) 사용
- **인용 부호**: 탭, 줄바꿈 또는 큰따옴표를 포함하는 필드는 큰따옴표로 감싸야 함. 내장된 큰따옴표는 `""`로 이스케이프
- **정렬 순서**: `Source_Doc` (오름차순), 그 다음 `Source_Locator` (문서 순서)

### 11.3 요약 파일 (`phase1_true_def_summary.md`)

요약 파일은 다음 섹션을 포함해야 합니다:

```markdown
# Phase 1 TRUE_DEF 추출 요약

## 실행 정보
- 날짜: {YYYY-MM-DD}
- 처리된 원문 문서: {건수}
- 총 추출 레코드: {건수}

## Scheme별 레코드
| Scheme | 건수 |
|:---|---:|
| IMO | {n} |
| IACS | {n} |
| KR | {n} |
| EU | {n} |

## Source_Doc별 레코드
| Source_Doc | 건수 |
|:---|---:|
| {doc} | {n} |
| ... | ... |

## 품질 플래그
- Phase 2 백로그 항목: {건수}
- Editor_Note 플래그: {건수}
- [narrower candidate] 플래그: {건수}

## 이슈 / 관찰사항
- {자유 텍스트: 주요 결정, 모호한 사항, 연기된 항목}
```

### 11.4 로그 파일 (`phase1_true_def_log.md`)

로그 파일은 순차적 처리 추적을 기록합니다:

```markdown
# Phase 1 TRUE_DEF 처리 로그

## {Source_Doc} — {절/장}
- **세그먼트**: {세그먼트 번호} / {총 세그먼트}
- **토큰 (약)**: {n}K
- **추출 레코드**: {건수}
- **결정 사항**:
  - {용어}: 채택 / 제외 — {사유}
  - ...
- **플래그**:
  - {Concept_ID}: {플래그 설명}
  - ...
```

### 11.5 덮어쓰기 규칙

각 신규 추출 실행은 `results/`의 이전 최종 출력 파일 및 `results/temp/`의 모든 중간 파일을 **덮어씁니다**. 점진적 보존이 필요한 경우, 사용자가 새 실행을 시작하기 전에 이전 파일의 이름을 변경하거나 보관해야 합니다.

---

## 12. Phase 1.1 — 검증 예외 관리

Phase 1 산출물의 반복 검증 중 반복적 코멘트가 식별되면, 체계적 해결을 위해 Phase 1.1로 에스컬레이션됩니다. Phase 1.1은 추가 추출 단계가 **아니라** QA 예외 레이어입니다.

**전체 사양**: [`phase1_1_validation_exception_guide.md`](phase1_1_validation_exception_guide.md) (세 가지 Phase 1 지침서 전체에서 공유) 참조.

**에스컬레이션 기준 (요약)**:
- 코멘트가 2회 이상 또는 2개 이상의 문서/레코드에서 반복
- 이슈가 검증 패스를 차단
- 현재 지침서 텍스트가 모호하여 검토자 간 올바른 조치에 대한 의견 불일치
- Phase 1 / Phase 2 경계가 불분명

**Phase 1 덮어쓰기 규칙과의 주요 차이**: Phase 1.1 이슈 등록부는 **버전 관리되며 덮어쓰이지 않습니다** (`results/phase1_1/phase1_1_issue_register_{date}_v{NN}.tsv`).

---

## 13. Phase 2 미리보기 (참고용 — 이 문서의 범위 밖)

| 항목 | 설명 |
|:---|:---|
| DESCRIPTION / PARAPHRASE 추가 | 백로그에서 승격 |
| 기술 용어 분류 | descriptor / search / rule_bound |
| 약어 등록부 | 약어 정규화 등록부 |
| Broader/Related 부여 | `skos:broader` 및 `skos:related` 관계 부여 |
| 빈도/적합성 평가 | 용어 빈도 및 통제 어휘 적합성 평가 |
| 출처 간 매핑 | 기본적으로 closeMatch, 확실한 경우에만 exactMatch. owl:sameAs 사용 금지 |
| JSON 변환 | terms.json을 단일 진실 공급원(single source of truth)으로 |
| SKOS-XL | 레이블 간 관계 (acronym-of 등) |
| OWL 변환 | 정식 온톨로지 생성 |

---

*Phase 1 범위: TRUE_DEF만 해당, 출처별 개념, 정의/노트 분리, `{Scheme}_..._TD_` 패턴의 안정적 ID, Source_Doc_Type 분류, Record_Type을 단일 구별자로. 출력: `results/`에 3개 최종 파일 (결과 TSV + 요약 MD + 로그 MD), `results/temp/`에 중간 청크 파일.*
