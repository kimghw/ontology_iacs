# Phase 1: APPLICABILITY 통제어휘 작업 지침서

> **Pre-SKOS 단계**: Phase 2에서 SKOS `skos:broader` / `skos:related` 계층적·연관적 관계를 구축하기 위한 준비 단계이다. Phase 1은 출처 충실한 적용범위 추출과 플랫 테이블 목록화에 집중하며, 공식 SKOS 의미 관계는 후속 단계에서 구축한다.

> **범위**: **IMO 협약/코드, IACS UR 문서, KR 규칙/지침, EU 지침/규정**에서 적용범위/범위 진술을 추출하고 구조화한다.
> 목표는 각 규정 문서가 **무엇에, 누구에게, 어떤 조건에서, 언제** 적용되는지를 적용범위 전용 컬럼이 포함된 플랫 테이블 형식으로 포착하는 것이다.
> 전체 교차 소스 추론(superseded_by, overrides_if, hybrid_split 등)은 Phase 2로 이연한다.
> **작업 절차**: 모든 소스 텍스트를 순차적으로 읽고 처리한다.
> **작업 준비**: 사용자가 검토를 요청하면 대상 자료를 약 100K 토큰 단위로 분할하여 순차적으로 처리한다.
---

## 0. 사전 준비

LLM과 사용자가 함께 대상 문서를 검토하고 기초 데이터(baseline data)를 추출하는 준비 단계이다. 각 instruction(TRUE_DEF, APPLICABILITY, CONTROLLED_TERM)은 독립적으로 수행한다.

1. **문서 검토(Document review)** — 대상 문서를 읽고 적용범위 진술이 어떤 구조로 되어 있는지 식별한다(예: Application 섹션, 규정 전문(preamble), Part/Chapter 범위 조항).
2. **추출 범위 설정(Extraction scoping)** — 관련 섹션에서 적용범위/범위 문장만 추출한다. 추출된 문장은 중간 디렉터리(`results/temp/`)에 저장한다.
3. **패턴 카탈로그 작성(Pattern cataloguing)** — Step 2에서 추출된 문장을 분석하여 패턴 카탈로그(`results/temp/extraction_patterns_applicability.tsv`)를 작성한다. 반복되는 문장 구조를 기록한다(예: `"This UR applies to..."`, `"of [N] GT and above"`, `"not applicable to..."`, `"ships contracted for construction on or after..."`). 이 카탈로그는 두 가지 용도로 활용된다: (a) 분리 스크립트가 패턴을 사용하여 나머지(remainder)에서 **누락 후보를 자동 플래깅**하고, (b) **교차 instruction 분류 검사**(예: TRUE_DEF 유형 문장이 APPLICABILITY 추출에 잘못 포함된 경우 탐지)에 재사용할 수 있다.
4. **추출 분리(Extraction separation)** — 분리 스크립트를 실행하여 소스 문서와 `results/temp/`의 추출 문장을 대조하고 두 가지 산출물을 생성한다: (a) **추출된 문장**(매칭된 것)과 (b) **미추출 문장**(매칭되지 않은 나머지). 스크립트는 Step 3의 패턴 카탈로그를 적용하여 알려진 적용범위 패턴과 일치하는 나머지 문장을 **누락 후보**로 플래깅한다. LLM이 초기 추출(Step 2)을 수행하고, 분리 및 패턴 매칭은 스크립트가 수행하여 기계적 완전성을 보장한다.
5. **추출 검증(Extraction verification)** — LLM이 미추출 문장(Step 4의 매칭되지 않은 나머지)을 검토하되, 스크립트가 플래깅한 누락 후보를 우선 검토하여 필요한 적용범위 문장이 누락되지 않았는지 확인한다. 누락이 발견되면 추출 세트에 추가하고, 새로운 패턴이 식별되면 패턴 카탈로그를 갱신한 후 분리 스크립트를 재실행한다.

---

## 1. 채택 규칙(Admission Rule)

| 조건 | 포함 | 제외 (Phase 2 백로그) |
|:---|:---|:---|
| 소스 위치 | "Application", "Scope", "General" 섹션; 적용범위를 명시하는 서두 문단; 규정 전문(IMO); Part/Chapter 범위 조항(KR) | 상세 기술 요건(산식, 부재 치수, 시험 절차) |
| 레코드 유형 | **APPLICABILITY**만 | TRUE_DEF 레코드(별도 instruction에서 처리) |
| 소스 | **IMO**: 협약, 강제/권고 코드, 결의서, 회람(유효 문서만 — Source_Doc_Type 열거형의 전체 목록은 Section 3.6 참조); **IACS**: UR, UI, Rec, PR(유효 문서만); **KR**: 규칙, 기술 규칙, 지침, 해석(현행 판만); **EU**: 지침, 규정, 결정(시행 중) | 시행 전 철회/대체된 문서 |
| 언어 | 영어만(데이터 셀) | 한국어 텍스트는 영어로 대체 |
| 세분도 | **규정 단위별 1건**(또는 소스에 독립적인 범위 블록이 여러 개인 경우 각각 1건). IMO의 경우 규정 단위는 통상 장(chapter) 내 규칙(regulation)이다. IACS의 경우 통상 문서 1건(UR, UI, Rec 또는 PR). KR의 경우 가장 낮은 자율적 적용범위 조항 — KR의 Part–Chapter–Section–Article–Paragraph 계층 구조에서 실제 적용범위 진술이 다양한 수준에 위치하므로, 흔히 Section 수준의 범위 조항(예: `Sec.1 101 Application`)이 된다. EU의 경우 규정 단위는 통상 지침 또는 규정 내 조문(article) 수준의 범위 조항이다. | 하위 조항 수준 요건 |

**한 줄 판단**: 이 텍스트가 해당 문서가 어떤 대상/선종/조건에 적용되는지 명시하는가? — **예 → 채택**, 아니오 → 건너뜀.

---

## 2. 핵심 원칙: 출처 충실 추출(Source-Faithful Extraction)

- **먼저 원문 그대로(verbatim) 추출한 후 분해한다.** `Applicability_Text@en` 컬럼은 원문 산문을 보존한다. 구조화 컬럼은 이 앵커 텍스트에서 파생된다.
- **하나의 소스 단위에서 여러 적용범위 레코드가 생성될 수 있다** — 소스에 별개의 범위 블록이 포함된 경우(예: UR A2에 "normal towing"과 "other towing"이 별도 범위로 존재; SOLAS II-1/Reg.3과 II-1/Reg.3-8이 별도 범위를 가짐).
- **텍스트에 명시되지 않은 조건을 추론하지 않는다.** 소스에 선종 제한이 언급되지 않으면 `Ship_Type`을 비워둔다 — "all ships"로 기본값을 채우지 않는다.
- **앵커 추적성 규칙(Anchor traceability rule)**: 구조화 컬럼의 모든 값은 `Applicability_Text@en`의 문구로 추적 가능해야 한다. 값이 소스 문서의 다른 섹션(주 적용범위 진술이 아닌 곳)에서 온 경우, 앵커 텍스트를 확장하여 해당 구절을 포함하거나, `Editor_Note`에 `[source: Section X.X]` 태그로 소스를 기록해야 한다.

---

## 3. 대상 스키마(Target Schema)

```
Concept_ID | Record_Type | Scheme | Source_Doc_Type | Applicability_Text@en | Target_Entity | Target_Role | Target_Object@en | Ship_Type | Size_Threshold | Qual_Predicate@en | Geographic_Scope@en | Cargo_Substance@en | Normative_Basis | Implements_Requirement | Exclusion@en | Trigger_Event | Trigger_Date | Normative_Status | Applicability_Status | Source_Doc | Source_Locator | Editor_Note
```

### 3.1 컬럼 정의 및 의무 수준

| # | 컬럼 | 의무 | SKOS/DC 매핑 | 데이터 유형 | 카디널리티 | 규칙 |
|:---:|:---|:---:|:---|:---|:---|:---|
| 1 | **Concept_ID** | **필수** | URI fragment | ID | single | 형식: `{Scheme}_{SourceKey}_APP_{SeqNo}`. 소스 패밀리별 Concept_ID 설계 규칙은 Section 3.5 참조. **한 번 부여된 Concept_ID는 재번호 매기기 불가; 결번 허용.** |
| 2 | **Record_Type** | **필수** | `dct:type` | enum | single | `APPLICABILITY`로 고정. 두 레코드 유형이 하나의 시트에 공존하도록 하는 판별자(discriminator). |
| 3 | **Scheme** | **필수** | `skos:inScheme` | enum | single | `IMO`, `IACS`, `KR`, `EU` 중 하나. 규정 문서의 소스 패밀리를 식별한다. |
| 4 | **Source_Doc_Type** | **필수** | `dct:type` (보조) | enum | single | 문서 장르를 분류한다. 폐쇄형 목록(Section 3.6)에서 선택. |
| 5 | **Applicability_Text@en** | **필수** | `skos:scopeNote` | text | single | 소스 섹션에서 가져온 원문 그대로 또는 경미하게 정규화된 적용범위 진술. 이것이 **앵커 필드** — 모든 구조화 컬럼은 이 텍스트에서 파생된다. 구조화 컬럼 값이 추출된 모든 구절을 포함해야 한다. Section 2 앵커 추적성 규칙 참조. |
| 6 | **Target_Entity** | **필수** | `mreg:targetEntity` | enum-multi | multi | 최상위 규제 대상. 폐쇄형 목록(Section 3.3)에서 선택. 세미콜론 구분. |
| 7 | **Target_Role** | 선택 | `mreg:targetRole` | enum-multi | multi | 대상 엔터티의 특정 규제 역할. 폐쇄형 목록(Section 3.3a)에서 선택. 세미콜론 구분. 적용범위가 역할(기국, 항만국, 회사, 선장)을 지정하는 IMO 문서에서 특히 관련성이 높다. |
| 8 | **Target_Object@en** | 선택 | `dcterms:subject` | text-multi | multi | 특정 규제 대상 객체. 자유 텍스트, 소스 원문 그대로. 예: `"shipboard fittings and supporting hull structures"`. 세미콜론 구분. |
| 9 | **Ship_Type** | 조건부 | `mreg:shipType` | enum-multi | multi | 폐쇄형 목록(Section 3.4)의 선종/유닛 유형. 세미콜론 구분. **소스가 선종을 명시적으로 제한하는 경우에만 기입; 그렇지 않으면 비워둔다.** |
| 10 | **Size_Threshold** | 조건부 | `mreg:threshold` | structured-text-multi | multi | 정량적 적용 한계. 형식: `param op value unit`. 예: `GT >= 500`; `L >= 90 m`. 세미콜론 구분. **소스가 정량적 임계값을 명시한 경우에만 기입.** |
| 11 | **Qual_Predicate@en** | 선택 | `mreg:qualPredicate` | text-multi | multi | Size_Threshold, Geographic_Scope, Cargo_Substance로 포착되지 않는 정성적 조건. 자유 텍스트. 예: `"crosshead type engines"`. 세미콜론 구분. |
| 12 | **Geographic_Scope@en** | 조건부 | `mreg:geographicScope` | text-multi | multi | 항해 유형, 항행 구역, 또는 관할 범위. 소스에서 거의 원문 그대로. 예: `"international voyage"`; `"polar waters"`; `"ships in ports of a Party"`. 세미콜론 구분. **소스가 항해 유형, 지리적 구역 또는 관할 범위로 명시적으로 제한하는 경우에만 기입; 그렇지 않으면 비워둔다.** |
| 13 | **Cargo_Substance@en** | 조건부 | `mreg:cargoSubstance` | text-multi | multi | 적용범위를 정의하거나 제한하는 화물 유형 또는 물질. 소스에서 거의 원문 그대로. 예: `"dangerous goods in packaged form"`; `"noxious liquid substances in bulk"`; `"liquefied gases"`. 세미콜론 구분. **소스가 운반 화물 또는 물질로 적용범위를 정의하는 경우에만 기입; 그렇지 않으면 비워둔다.** |
| 14 | **Normative_Basis** | 선택 | `dct:conformsTo` | text-multi | multi | 요건을 의무화하거나 범위를 설정하는 외부 규정 문서. 예: `SOLAS II-1/3-8`; `IGC Code`; `MARPOL Annex VI`. 세미콜론 구분. IMO 문서의 경우, 상위 협약 또는 근거 결의서를 참조할 수 있다. |
| 15 | **Implements_Requirement** | 선택 | `mreg:implementsRequirement` | text-multi | multi | 방향성 있는 교차 소스 이행 링크. 이 적용범위 레코드가 어떤 상위 요건을 구체화하는지 기록한다. 예: IACS UR 레코드는 `SOLAS II-1/3-8`을 열거할 수 있고, KR 규칙 레코드는 `IACS UR A2` 또는 `SOLAS II-1/3-8`을 열거할 수 있다. 세미콜론 구분. IMO → IACS → KR 규범 계층을 포착한다. **소스 문서에 명시적이고 개별 조문 수준의 상호 참조(예: "in compliance with SOLAS II-1/3-8")가 포함된 경우에만 기입한다. 규칙 체계가 국제 협약을 "반영한다(reflects)" 또는 "기반으로 한다(is based on)"는 일반적 진술에서 이행 링크를 추론하지 않는다. 명시적 상호 참조가 없으면 비워두고 Editor_Note에 `[Phase 2: implements_mapping]`을 태그한다.** |
| 16 | **Exclusion@en** | 조건부 | `xkos:exclusionNote` | text-multi | multi | 명시적 제외 조항, 거의 원문 그대로. 예: `"high speed craft"`. 세미콜론 구분. **소스에 명시적 제외 표현이 포함된 경우에만 기입.** |
| 17 | **Trigger_Event** | 조건부 | `mreg:triggerEvent` | text | single | 이행 기점(milestone). 예: `"ships contracted for construction on or after [date]"`. **소스에 명시된 경우에만 기입.** |
| 18 | **Trigger_Date** | 조건부 | `dct:temporal` | date (ISO 8601) | single | Trigger_Event에서 추출한 날짜. 예: `2024-07-01`. **Trigger_Event에서 날짜를 추출할 수 있는 경우에만 기입.** |
| 19 | **Normative_Status** | 선택 | `mreg:normativeStatus` | enum | single | `mandatory`, `recommendatory`, `guidance`, `interpretive`, `discretionary`. 정의는 Section 3.7, Source_Doc_Type 기반 기본값 매핑은 Section 3.7a 참조. 소스 텍스트에 명시적 집행 단서(예: "shall", "should", "may", "for guidance only")가 포함된 경우 해당 단서가 기본값을 우선한다. CONTROLLED_TERM instruction과 공유하는 값 집합. |
| 20 | **Applicability_Status** | **필수** | (custom QA) | enum | single | 추출 신뢰도: `explicit`(소스에 명확하고 자족적인 적용범위 진술 존재), `partial`(소스에 일부 적용범위 정보만 있음; 누락 요소는 비워둠), `unclear`(소스 표현이 모호하거나 모순적), `composite`(앵커 텍스트가 여러 소스 섹션에서 조합됨 — 각 섹션은 Editor_Note에 `[source: Section X.X]`로 기록). **`inferred`는 Phase 1에서 허용되지 않음** — 추론된 적용범위는 Phase 2 추론에 해당. |
| 21 | **Source_Doc** | **필수** | `dcterms:source` | text | single | 소스 패밀리별 문서 식별자. 명명 규칙은 Section 3.8 참조. |
| 22 | **Source_Locator** | **필수** | (locator) | text | single | 섹션/문단/규정 위치. 예: `A2.0`, `Reg.3-4`, `Pt.3 Ch.1 Sec.1`. |
| 23 | **Editor_Note** | 선택 | `skos:editorialNote` | text | single | 추출 근거, QA 코멘트, 모호성 플래그, Phase 2를 위한 교차 소스 참조. 구조화 컬럼 값이 Applicability_Text 외부 섹션에서 온 경우 여기에 `[source: Section X.X]`를 기록한다. |

> **의무 수준**: **필수(Required)** = 항상 기입; **조건부(Conditional)** = 소스에 해당 정보가 있을 때 기입; **선택(Optional)** = 가능하면 기입.

### 3.2 TRUE_DEF 및 CONTROLLED_TERM 레코드와의 상호운용성

APPLICABILITY와 TRUE_DEF 레코드가 하나의 시트에 공존하는 경우:

| 측면 | TRUE_DEF | APPLICABILITY | 해결 방법 |
|:---|:---|:---|:---|
| **판별자** | `Record_Type` = `TRUE_DEF` | `Record_Type` = `APPLICABILITY` | `Record_Type`이 두 유형의 단일 판별자 |
| **범위 텍스트** | `Scope_Note@en` (정의에서 추출한 범위) | `Applicability_Text@en` (원문 적용범위 진술, 앵커 필드) | 둘 다 `skos:scopeNote`에 매핑되지만 역할이 다름: Scope_Note는 정의 내 포함된 범위를 포착; Applicability_Text는 구조화 분해를 위한 독립형 앵커 |
| **Scheme** | `IMO`, `IACS`, `KR`, `EU` | `IMO`, `IACS`, `KR`, `EU` | 두 레코드 유형이 동일한 Scheme 값 집합을 공유 |
| **TRUE_DEF 전용 컬럼** | prefLabel, altLabel, Definition, Scope_Note, Example 기입 | 비워둠 | 검증은 Record_Type에 따라 조건부 |
| **APPLICABILITY 전용 컬럼** | 비워둠 | Target_Entity, Target_Role, Ship_Type, Size_Threshold, Geographic_Scope, Cargo_Substance 등 기입 | 검증은 Record_Type에 따라 조건부 |

APPLICABILITY와 CONTROLLED_TERM 레코드가 공존하는 경우:

| 측면 | APPLICABILITY | CONTROLLED_TERM | 해결 방법 |
|:---|:---|:---|:---|
| **판별자** | `Record_Type` = `APPLICABILITY` | `Record_Type` = `CONTROLLED_TERM` | `Record_Type`이 단일 판별자 |
| **소스 위치** | Application/Scope 섹션 | 본문(규범 요건) | 비중복 소스 위치 |
| **Scheme** | `IMO`, `IACS`, `KR`, `EU` | `IMO`, `IACS`, `KR`, `EU` | 4개 Scheme 값 공유 |
| **CONTROLLED_TERM 전용 컬럼** | 비워둠(Term_Category, Term_Subclass 등) | CONTROLLED_TERM instruction에 따라 기입 | 검증은 Record_Type에 따라 조건부 |

### 3.3 Target_Entity 통제값

| 값 | 설명 | 예시 소스 |
|:---|:---|:---|
| `Ship` | 선박/유닛 설계, 건조, 검사 | IACS UR A2, SOLAS II-1, KR Pt.3 |
| `Equipment` | 장비 형식 승인, 시험, 인증 | IACS UR A3, SOLAS II-2, KR Pt.6 |
| `Material` | 재료 제조, 시험, 인증 | IACS UR W7, KR Pt.2 |
| `Engine` | 기관 형식 승인, 인증, 시험 | IACS UR M44, MARPOL Annex VI |
| `System` | 통합 선내 시스템 | IACS UR E26, SOLAS V |
| `Personnel` | 용접사 및 인력 자격 | IACS UR W32, STCW |
| `Software` | 선내 소프트웨어 승인 | IACS UR L5 |
| `Service_Supplier` | NDT 업체, 서비스 공급자 승인 | IACS UR W35 |
| `Certification_Scheme` | 제조자 인증 체계 | IACS UR Z26 |
| `Administration` | 정부 해사 당국(기국, 항만국 또는 연안국으로서의 규제 역할) | SOLAS I, MARPOL I |
| `Organization` | 회사, 인정 기관, 항만 시설 | ISM Code, ISPS Code |
| `Cargo` | 화물 관련 요건(위험물, 곡물, 산적화물) | IMDG Code, IMSBC Code |
| `Document_Record` | 증서, 계획서, 기록, 매뉴얼 | SOLAS I/Reg.12, ISM Code |

### 3.3a Target_Role 통제값

대상 엔터티가 특정 규제 역할로 행동하는 경우 `Target_Role`을 사용한다. IMO 문서에서 특히 흔하다.

| 값 | 상위 엔터티 | 설명 | 예시 소스 |
|:---|:---|:---|:---|
| `Flag_State` | Administration | 선박이 국기를 게양하는 국가 | SOLAS I, MARPOL I |
| `Port_State` | Administration | 항만국 통제를 시행하는 국가 | SOLAS XI-1, MOU 문서 |
| `Coastal_State` | Administration | 연안 관할권을 가진 국가 | MARPOL I/Reg.6 |
| `Shipowner` | Organization | 선박의 등록 소유자 | MLC 2006 |
| `Company_ISM` | Organization | ISM Code에서 정의하는 회사 | ISM Code |
| `Master` | Personnel | 선장 | SOLAS V, STCW |
| `Seafarer` | Personnel | STCW/MLC에서 정의하는 선원 | STCW, MLC 2006 |
| `Officer` | Personnel | 인증 사관(갑판/기관) | STCW Ch.II/III |
| `RO` | Organization | 인정 기관(기국을 대리하는 선급 협회) | SOLAS XI-1, RO Code |
| `Port_Facility` | Organization | 항만 시설(ISPS 맥락) | ISPS Code |
| `Training_Provider` | Organization | 해사 훈련 기관 | STCW |
| `Manufacturer` | Organization | 장비/재료 제조자 | IACS UR Z26, KR Pt.2 |

### 3.4 Ship_Type 통제값

IMO는 보편적으로 적용 가능한 선종 정의를 제공하지 않는다; 각 문서가 고유한 설명을 사용한다. 상충하는 분류를 피하기 위해, 공통 핵심 목록은 IMO 협약, IACS UR, 선급 규칙에서 일관되게 나타나는 **규제 범주 유형**으로 제한한다. 설계/운항 하위 유형은 확장 분류체계(Section 3.4a)에 배치한다.

#### 3.4 핵심 목록 (규제 범주)

| 값 | 설명 |
|:---|:---|
| `All_Ships` | 선종 제한 없음(명시적으로 언급된 경우에만 사용) |
| `Passenger_Ship` | 12명 초과 여객을 운반하는 선박(SOLAS I/Reg.2(f)) |
| `Cargo_Ship` | 여객선이 아닌 선박(SOLAS I/Reg.2(g)); 참고: 각 협약이 GT 임계값과 항해 유형으로 추가 한정 가능 |
| `Oil_Tanker` | MARPOL Annex I에서 정의하는 유조선 |
| `Bulk_Carrier` | SOLAS XII 및 IACS UR S에서 정의하는 산적화물선 |
| `Gas_Carrier` | IGC Code 적용 선박 |
| `Chemical_Tanker` | IBC Code 적용 선박 |
| `HSC` | HSC Code 적용 고속선 |
| `MODU` | MODU Code 적용 이동식 해양 시추 유닛 |
| `Offshore_Unit` | 비시추 해양 유닛(일반 규제 범주) |
| `Fishing_Vessel` | Torremolinos Protocol / Cape Town Agreement 적용 어선 |
| `Special_Purpose_Ship` | 특수 목적에 종사하는 선박(SPS Code) |
| `Conventional_Ship` | 배수량형 선박(특정 IACS UR, 예: UR A2에서 정의) |
| `Nuclear_Ship` | 원자력 추진 선박(SOLAS VIII) |

#### 3.4a 확장 분류체계 (설계/운항 하위 유형)

다음 값은 **공통 핵심의 일부가 아니다**. 소스 문서가 이 특정 용어를 명시적으로 사용하는 경우에만 사용하고, `Qual_Predicate@en`에 기록한다(Phase 1에는 별도의 `Ship_Type_Ext` 컬럼이 없음). Phase 2에서 이들은 적절한 핵심 유형 하위의 `skos:narrower`로 공식화된다.

| 값 | 상위 핵심 유형 | 설명 |
|:---|:---|:---|
| `Container_Ship` | Cargo_Ship | 전용 컨테이너 운반선 |
| `General_Cargo` | Cargo_Ship | 전문 화물 시스템이 없는 일반 건화물선 |
| `RoRo` | Cargo_Ship (RoPax의 경우 Passenger_Ship) | Ro-Ro 화물선 및 Ro-Ro 여객선 |
| `Offshore_Support_Vessel` | Cargo_Ship | 플랫폼 보급선, 앵커 핸들링 선박 등 |
| `FPSO` | Offshore_Unit | 부유식 생산·저장·하역 유닛 |
| `FSU` | Offshore_Unit | 부유식 저장 유닛 |
| `Pleasure_Yacht` | — | 요트 및 유람선 |
| `Barge` | — | 비자항 바지선 |

### 3.5 Concept_ID / URI 설계

**일반 패턴**: `{Scheme}_{SourceKey}_APP_{SeqNo}`

- `Scheme`: `IMO`, `IACS`, `KR` 또는 `EU`
- `SourceKey`: 정규화된 소스 단위 키(문서 수준 또는 주요 단위 수준)
- `_APP_`: 적용범위 레코드를 정의 레코드와 구별하는 고정 접미사
- `SeqNo`: 3자리 일련번호, 해당 소스 단위 내 로컬

**정규화 규칙** (3개 instruction — TRUE_DEF / APPLICABILITY / CONTROLLED_TERM 공유). **Step 1–5**는 공유 핵심 규칙. **Step 6–7**은 IMO 코드 및 EU 법률에 대한 소스 패밀리 특화 약어 패턴 처리:

| 단계 | 규칙 | 예시 |
|:---:|:---|:---|
| 1 | 마침표, 괄호, 쉼표를 밑줄로 대체(또는 단어 경계에 있으면 제거) | `Z10.1` → `Z10_1`; `Pt.3 Ch.1` → `Pt3_Ch1` |
| 2 | `/`와 `-`를 `_`로 대체 | `II-1/3-8` → `II_1_3_8` |
| 3 | 연속 밑줄 축소 | `II__1` → `II_1` |
| 4 | 대문자 사용 | `Pt3_Ch1` → `PT3_CH1` |
| 5 | 문서 유형 접두사 제거(이미 패턴에 포함됨) | `UR S11A` → `S11A` |
| 6 | IMO 코드: 표준 약어 사용 | `FSS Code` → `FSS`, `ISM Code` → `ISM` |
| 7 | EU: 연도 + 번호 패턴 | `Directive 2009/45/EC` → `DIR_2009_45` |

#### 소스 패밀리별 예시

| 소스 패밀리 | 소스 문서 | Concept_ID 예시 |
|:---|:---|:---|
| **IACS** | UR A2 | `IACS_A2_APP_001` |
| **IACS** | UR S11A | `IACS_S11A_APP_001` |
| **IACS** | UI SC123 | `IACS_UI_SC123_APP_001` |
| **IACS** | Rec 87 | `IACS_REC_87_APP_001` |
| **IACS** | PR 38 | `IACS_PR_38_APP_001` |
| **IMO** | SOLAS Ch.II-1, Reg.3-8 | `IMO_SOLAS_II_1_R3_8_APP_001` |
| **IMO** | MARPOL Annex VI | `IMO_MARPOL_AVI_APP_001` |
| **IMO** | IGC Code | `IMO_IGC_APP_001` |
| **IMO** | IBC Code Ch.1 | `IMO_IBC_CH1_APP_001` |
| **IMO** | STCW Ch.II | `IMO_STCW_II_APP_001` |
| **IMO** | ISM Code | `IMO_ISM_APP_001` |
| **IMO** | Load Line Convention | `IMO_LL_APP_001` |
| **KR** | Rules for Steel Ships, Pt.3 Ch.1 | `KR_STEEL_PT3_CH1_APP_001` |
| **KR** | Rules for FRP Ships, Pt.2 | `KR_FRP_PT2_APP_001` |
| **KR** | Guidance for Classification of Steel Ships | `KR_GSTEEL_APP_001` |
| **KR** | Rules for Mobile Offshore Units | `KR_MOU_APP_001` |
| **EU** | Directive 2009/45/EC | `EU_DIR_2009_45_APP_001` |
| **EU** | Regulation (EU) 2015/757 | `EU_REG_2015_757_APP_001` |

- Phase 1에서는 로컬 ID(`Concept_ID`)만 확정한다. 기본 URI 패턴 및 네임스페이스 구성은 **Appendix B** 참조.

### 3.6 Source_Doc_Type 통제값

| 값 | 설명 | 대표 소스 패밀리 |
|:---|:---|:---|
| `Convention` | 국제 협약(SOLAS, MARPOL, Load Line, STCW 등) | IMO |
| `Mandatory_Code` | 협약 하 강제 코드(IGC, IBC, ISM, ISPS 등) | IMO |
| `Recommendatory_Code` | 권고 코드 및 지침 | IMO |
| `Resolution` | IMO 총회 또는 MSC/MEPC 결의서 | IMO |
| `Circular` | MSC/MEPC 회람 및 통일 해석 | IMO |
| `UR` | 통일 요건(Unified Requirements) | IACS |
| `UI` | 통일 해석(Unified Interpretations) | IACS |
| `Rec` | 권고(Recommendations) | IACS |
| `PR` | 절차 요건(Procedural Requirements) | IACS |
| `Rule` | 선급 규칙(강제 요건) | KR |
| `Guidance` | 기술 지침(권고 사항) | KR |
| `Interpretation` | 규칙의 공식 해석 | KR |
| `Technical_Rule` | 특정 선종 또는 시스템에 대한 기술 규칙 | KR |
| `Directive` | 국내 법률 전환이 필요한 EU 지침 | EU |
| `Regulation_EU` | 직접 구속력 있는 EU 규정 | EU |
| `Decision` | 특정 수신자에게 구속력 있는 EU 결정 | EU |

### 3.7 Normative_Status 정의 (CONTROLLED_TERM과 공유)

| 값 | 정의 | 대표 소스 맥락 |
|:---|:---|:---|
| `mandatory` | 법적 구속력 있는 요건; 준수가 의무 | IMO 협약, IACS UR, KR 규칙 |
| `recommendatory` | 규제 기관이 공식적으로 권고; 법적 구속력 없음 | IMO 결의서, IACS Rec |
| `guidance` | 자문 또는 모범 관행 지침 | KR 지침, IACS 지침 노트 |
| `interpretive` | 강제 요건의 공식 해석; 적용을 명확화 | IACS UI, KR 해석, IMO 통일 해석 |
| `discretionary` | 주관청, 선급 협회 또는 검사원의 재량에 위임 | "may", "at society's discretion" 조항 |

### 3.7a Source_Doc_Type별 Normative_Status 기본값

전역 기본값 `mandatory`는 제거됨. 대신 기본값은 `Source_Doc_Type`에서 도출된다. 소스 텍스트에 명시적 집행 단서가 포함된 경우 아래 기본값을 우선한다.

| Source_Doc_Type | 기본 Normative_Status | 근거 |
|:---|:---|:---|
| `Convention` | `mandatory` | 비준 및 발효 시 구속력 |
| `Mandatory_Code` | `mandatory` | 상위 협약에 의해 강제화 |
| `Recommendatory_Code` | `recommendatory` | IMO가 채택한 자문 코드 |
| `Resolution` | *(비워둠)* | 사안별: 강제 코드 개정을 채택하거나 순수 권고일 수 있음. Editor_Note에 근거 기록 |
| `Circular` | `recommendatory` | MSC/MEPC 회람은 일반적으로 비구속 지침 |
| `UR` | `mandatory` | 회원 선급 규칙에 반영할 최소 요건 |
| `UI` | `interpretive` | 기존 요건의 조화된 해석 |
| `Rec` | `recommendatory` | 산업계 자문; 회원 선급에 구속력 없음 |
| `PR` | `mandatory` | 회원 선급에 구속력 있는 절차 요건 |
| `Rule` | `mandatory` | 구속력 있는 선급 규칙 |
| `Technical_Rule` | `mandatory` | 특정 선종/시스템에 대한 구속력 있는 기술 규칙 |
| `Guidance` | `guidance` | 권고 사항; 비강제 |
| `Interpretation` | `interpretive` | 규칙의 해석; KR이 명시적으로 비강제로 표시 |

> **우선 규칙(Override rule)**: 소스 텍스트에 명시적 조동사 표현("shall" → `mandatory`, "should" / "is recommended" → `recommendatory`, "may" / "at society's discretion" → `discretionary`, "for guidance only" → `guidance`)이 포함된 경우, 해당 단서가 Source_Doc_Type 기본값을 우선한다. 우선 근거를 Editor_Note에 기록한다.

### 3.8 Source_Doc 명명 규칙

| 소스 패밀리 | 패턴 | 예시 |
|:---|:---|:---|
| **IMO** | `{협약/코드} {장/부속서/편}` | `SOLAS II-1`, `MARPOL Annex VI`, `IGC Code`, `STCW Ch.II`, `ISM Code`, `LL Convention` |
| **IACS** | `{문서유형} {시리즈}{번호}` 또는 `{문서유형} {번호}` | `UR A2`, `UR S11A`, `UI SC123`, `Rec 87`, `PR 38` |
| **KR** | `KR {규칙집} {편/장}` | `KR Rules Pt.3 Ch.1`, `KR Guidance Pt.7`, `KR FRP Rules Pt.2` |
| **EU** | `{문서유형} {연도}/{번호}/{접미사}` | `Directive 2009/45/EC`, `Regulation (EU) 2015/757`, `Decision 2009/17/EC` |

---

## 4. 추출 패턴 — 적용범위 분해

`Applicability_Text@en` 필드가 앵커이다. 다음 패턴이 구조화 컬럼으로의 분해를 안내한다.

### 4.1 기본 추출 패턴

| # | 패턴 | 트리거 표현 | 대상 컬럼 |
|:---:|:---|:---|:---|
| A1 | 대상 식별 | "This UR applies to...", "Requirements for...", "These regulations apply to...", "This Part applies to..." | Target_Entity, Target_Object |
| A1a | 역할 식별 | "The Administration shall...", "Each Contracting Government...", "The Company shall ensure..." | Target_Role |
| A2 | 선종 제한 | "all [ship type]", "ships of type...", "every oil tanker..." | Ship_Type |
| A3 | 정량적 임계값 | "of [N] [unit] and above", ">= [N]", "[N] or more" | Size_Threshold |
| A4 | 정성적 조건 | "where [condition]", "fitted with...", "intended for..." | Qual_Predicate |
| A4a | 지리적/항해 범위 | "engaged in international voyages", "operating in polar waters", "in ports of a Party", "within special areas" | Geographic_Scope |
| A4b | 화물/물질 범위 | "carrying dangerous goods", "noxious liquid substances in bulk", "liquefied gases", "INF cargo" | Cargo_Substance |
| A5 | 규범 참조 | "per SOLAS...", "subject to [Convention]", "as required by..." | Normative_Basis |
| A5a | 이행 링크 | "implements [Regulation]", "in compliance with [UR]", "as required by [Convention]" | Implements_Requirement |
| A6 | 제외 조항 | "not applicable to...", "excluding...", "does not apply to...", "other than..." | Exclusion |
| A7 | 이행 조항 | "ships contracted for construction on or after...", "keel laid on or after...", "entry into force [date]" | Trigger_Event + Trigger_Date |
| A8 | 집행 한정어 | "guidance only", "at society's discretion", "may be considered", "should", "is recommended" | Normative_Status |

### 4.2 Phase 1 포착 / Phase 2 추론 패턴

다음 패턴은 소스 내부의 적용범위 의미론을 포함하며, Phase 1에서 **포착**(구조화 컬럼 또는 Editor_Note에 기록)해야 하지만, 전체 교차 소스 **추론**은 Phase 2로 이연된다.

| # | 패턴 | Phase 1 행동 |
|:---:|:---|:---|
| A11 | 조건부 무효화 | "unless the flag Administration determines otherwise" → `Qual_Predicate@en`에 무효화 조건을 기록하고 Editor_Note에 `[Phase 2: unless]` 태그 |
| A12 | 소급 적용 | "existing ships built before [date]" → "existing ships" 한정어와 함께 `Trigger_Event` / `Trigger_Date`에 기록하고 Editor_Note에 `[Phase 2: retrospective]` 태그 |
| A15 | 경과 규정 | "ships complying with [old regulation] need not comply until [date]" → `Trigger_Event` / `Trigger_Date`에 경과 일자를 기록하고 Editor_Note에 `[Phase 2: transitional]` 태그 |

### 4.3 완전 이연 패턴 (Phase 2)

Phase 2에 해당하는 패턴(A9, A10, A13, A14: 대체, 하이브리드 분할, 대안 규칙, 동등성)을 발견하면 Editor_Note에 `[Phase 2: {tag}]` 형식으로 기록하고 넘어간다. 상세 패턴 표는 **Appendix D** 참조.

---

## 5. 다중값 인코딩

모든 다중값 컬럼은 **세미콜론(`;`)**을 구분자로 사용한다.

```
Size_Threshold:        GT >= 500; L >= 90 m; Cb 0.55-0.90
Geographic_Scope@en:   international voyage; polar waters
Cargo_Substance@en:    dangerous goods in packaged form; noxious liquid substances in bulk
Exclusion@en:          CSR bulk carriers; high speed craft; special purpose ships
Ship_Type:             Oil_Tanker; Chemical_Tanker
Implements_Requirement:  SOLAS II-1/3-8; IMO Res.MSC.474(102)
```

`Size_Threshold`에는 두 가지 형식이 허용된다:
- **비교 형식**: `{parameter} {operator} {value} {unit}` — 단일 경계 임계값
- **범위 형식**: `{parameter} {low}-{high} {unit}` — 한정 범위

두 형식 모두 유효하며, 동일 레코드 내에 공존할 수 있다(세미콜론 구분).

| 파라미터 | 약어 | 예시 |
|:---|:---|:---|
| 총톤수 | `GT` | `GT >= 500` |
| 길이 | `L` | `L >= 90 m` |
| 실린더 내경 | `bore` | `bore >= 200 mm` |
| 출력 | `kW` | `kW > 37` |
| 크랭크케이스 용적 | `V_cc` | `V_cc >= 0.6 m3` |
| 판 두께 | `t` | `t > 50 mm` |
| 화물 밀도 | `rho_c` | `rho_c >= 1.0 t/m3` |
| 범위 | — | `L 90-500 m` |
| 재화중량톤수 | `DWT` | `DWT >= 20000` |
| 인원 수 | `N_persons` | `N_persons > 12` |

---

## 6. 편집 규칙 (Phase 1 요약)

| 규칙 | 내용 |
|:---|:---|
| 언어 | 영어만(데이터 셀). 한국어는 내부 노트에서만 허용 |
| 철자법 | 영국식 영어(moulded, vapour, draught, centre, programme). **TSV 컬럼 헤더는 간결성을 위해 `@en`을 사용. RDF 변환 시 모든 영어 리터럴은 `@en-GB` 태그(BCP 47 준수)를 부여한다.** 이 이중 계층 방식은 헤더의 장황함을 피하면서 최종 RDF 출력에서 방언 정밀도를 유지한다 |
| Applicability_Text | 원문 표현을 보존한다. 경미한 정규화 허용(줄바꿈 제거, OCR 아티팩트 수정). 구조화 컬럼 값이 추출된 모든 구절을 포함해야 한다 |
| 구조화 컬럼 | Applicability_Text에서 파생. 앵커 텍스트로 추적 가능해야 한다 |
| 출처 인용 | Source_Doc과 Source_Locator를 분리한다. `§` 기호를 사용하지 않는다. Section 3.8의 명명 규칙을 따른다 |
| 열거형 값 | Section 3.3, 3.3a, 3.4, 3.6, 3.7의 정확한 값을 사용한다. 일치하는 값이 없으면 가장 가까운 값 + Editor_Note에 플래그 |
| 빈 셀 | 정보가 없으면 비워둔다. 기본값을 넣거나 추론하지 않는다 |
| 교차 소스 연결 | 방향성 계층 링크에 `Implements_Requirement`를 사용한다. `Normative_Basis`와 `Implements_Requirement`에 동일 정보를 중복하지 않는다 — 인용된 외부 참조에는 `Normative_Basis`를, 방향성 이행 관계에는 `Implements_Requirement`를 사용한다. **Implements_Requirement는 소스 텍스트의 명시적 조문 수준 상호 참조에 의해 뒷받침되어야 한다. 규칙 체계가 국제 협약을 "반영한다(reflects)" 또는 "포함한다(incorporates)"는 일반적 진술은 해당하지 않는다 — 비워두고 Phase 2 매핑으로 이연한다** |

---

## 7. 절차

```
Step 1   대상 소스 문서를 연다
         - IACS: UR/UI/Rec/PR 문서(해당 청크 디렉터리에서)
         - IMO: 협약/코드 장 또는 규정 텍스트
         - KR: 규칙/지침 편 또는 장
Step 2   "Application", "Scope" 또는 "General" 섹션을 찾는다
         - IMO: 규정 전문 또는 "Application" 조문
         - KR: Part/Chapter 범위 조항(통상 Section 1)
Step 3   전체 적용범위 진술을 복사 -> Applicability_Text@en
         (범위, 임계값, 제외, 이행 일자 정보를 포함하는
          모든 문단을 포함한다)
Step 4   채택 규칙을 적용 — 이것이 적용범위 진술인지 확인
Step 5   Section 3.5 규칙에 따라 Concept_ID를 부여
         Record_Type = APPLICABILITY로 설정
         Scheme = IMO | IACS | KR | EU (적절하게)로 설정
         Section 3.6에 따라 Source_Doc_Type 설정
Step 6   패턴 A1-A8(Section 4.1)을 사용하여 Applicability_Text를 분해
         -> Target_Entity, Target_Role, Target_Object, Ship_Type,
            Size_Threshold, Qual_Predicate, Geographic_Scope,
            Cargo_Substance, Normative_Basis, Implements_Requirement,
            Exclusion, Trigger_Event, Trigger_Date, Normative_Status를 기입
Step 7   앵커 추적성을 검증 — 모든 구조화 값이 Applicability_Text@en의
         문구로 추적 가능해야 한다. 불가능한 경우 앵커 텍스트를 확장하거나
         Editor_Note에 [source: Section X.X]를 기록
Step 8   A11/A12/A15 패턴을 구조화 컬럼 + Editor_Note에 포착(Section 4.2);
         완전 이연 패턴 A9/A10/A13/A14는 Editor_Note에만 태그(Section 4.3)
Step 9   Applicability_Status를 부여(explicit/partial/unclear/composite)
Step 10  Section 3.8에 따라 Source_Doc / Source_Locator를 기록
Step 11  검증(Section 8)
```

---

## 8. 검증

### 8.1 2-Pass 검토

| 패스 | 초점 | 점검 항목 |
|:---|:---|:---|
| **구조적** | 테이블 무결성 | 컬럼 수 일관성(23열), 필수 필드 빈 셀 점검(선택/조건부 필드는 의무 규칙에 따라 비어 있을 수 있음), Concept_ID 중복 없음, 유효한 열거형 값, `_APP_` 접미사 존재, Record_Type = `APPLICABILITY`, Scheme이 소스 패밀리와 일치 |
| **의미적** | 내용 정확성 | Applicability_Text = 출처 충실, 구조화 컬럼이 앵커 텍스트로 추적 가능, 정보 날조 없음, Size_Threshold 형식 유효, Trigger_Date가 ISO 8601, Implements_Requirement가 올바른 계층 방향을 포착 |

### 8.2 교차 점검 규칙

| 규칙 | 점검 | 심각도 |
|:---|:---|:---|
| 앵커 추적성 | 비어 있지 않은 모든 구조화 컬럼 값이 Applicability_Text@en의 문구로 추적 가능해야 한다. 다른 곳에서 온 경우 Editor_Note에 `[source: Section X.X]` 포함 필요 | **오류** |
| 열거형 검증 | Target_Entity 값이 Section 3.3 목록에 포함 | **오류** |
| Target_Role 검증 | Target_Role 값이 Section 3.3a 목록에 포함 | **오류** |
| Ship_Type 검증 | Ship_Type 값이 Section 3.4 핵심 목록에 포함. 확장 유형(Section 3.4a)은 Ship_Type 컬럼에 나타나면 안 됨 — 대신 Qual_Predicate@en에 기록 | **오류** |
| Source_Doc_Type 검증 | Source_Doc_Type 값이 Section 3.6 목록에 포함 | **오류** |
| Normative_Status 검증 | Normative_Status 값이 Section 3.7 목록에 포함 | **오류** |
| 임계값 형식 | Size_Threshold가 비교 형식(`param op value unit`) 또는 범위 형식(`param low-high unit`)(Section 5)과 일치 | **경고** |
| 날짜 형식 | Trigger_Date가 ISO 8601(YYYY-MM-DD) | **오류** |
| Geographic_Scope 조건부 기입 | 소스에 항해 유형, 지리적 구역 또는 관할 범위 문구가 포함된 경우 Geographic_Scope를 기입해야 함 | **경고** |
| Cargo_Substance 조건부 기입 | 소스가 화물 또는 물질로 적용범위를 정의하는 경우 Cargo_Substance를 기입해야 함 | **경고** |
| 완전성 | 최소한 Concept_ID + Record_Type + Scheme + Source_Doc_Type + Applicability_Text + Target_Entity + Source_Doc + Source_Locator + Applicability_Status가 기입되어야 함 | **오류** |
| 제외 소스 점검 | 모든 Exclusion 항목이 소스의 명시적 "not applicable" / "excluding" 문구에 대응해야 함 | **오류** |
| 중복 탐지 | 동일 Source_Doc + Source_Locator에서 별개의 범위 블록이 아닌 한 중복 레코드가 생성되면 안 됨 | **경고** |
| 조건부 기입 점검 | Applicability_Text에 해당 트리거 표현(Section 4.1)이 존재하면 조건부 컬럼이 기입되어야 함 | **경고** |
| Record_Type 조건부 검증 | APPLICABILITY 전용 컬럼이 TRUE_DEF 레코드에 나타나면 안 됨; TRUE_DEF 전용 컬럼이 APPLICABILITY 레코드에 나타나면 안 됨 | **오류** |
| Concept_ID 접두사 점검 | Concept_ID 접두사가 Scheme 값과 일치(`IMO_`, `IACS_`, `KR_`, `EU_`) | **오류** |
| 소스 패밀리 일관성 | Scheme 값이 Source_Doc 명명과 일관(예: Scheme=`IMO`는 IMO 스타일 Source_Doc을 가져야 함) | **오류** |
| Implements 방향성 | Implements_Requirement는 상위 소스(IMO/EU > IACS > KR)를 참조해야 하며, 하위를 참조하면 안 됨 | **경고** |
| Implements 명시적 근거 | Implements_Requirement는 소스 텍스트의 명시적 조문 수준 상호 참조에 의해 뒷받침되어야 하며, 일반적 "반영/포함" 진술에서 추론하면 안 됨 | **오류** |

> **SHACL 참고**: Section 8.2 교차 점검 규칙이 규범적 검증 사양이다. 자동화된 검증을 위한 SHACL 셰이프는 Phase 2에서 이 규칙들로부터 생성될 예정 — 이 문서에 별도 SHACL 표를 유지하지 않는다.

---

## 9. 네임스페이스 접두사

컬럼-속성 매핑은 Section 3.1의 SKOS/DC Mapping 열에 명시되어 있다. Turtle 접두사 선언 및 상세 설명은 **Appendix B** 참조.

---

## 10. 작업 예시 (빠른 참조)

아래는 핵심 흐름만 보여주는 축약 예시이다. IACS/IMO/KR 각 소스 패밀리별 상세 예시(전체 23-column 포함)는 **Appendix C** 참조.

### IACS UR A2 — 축약

| 컬럼 | 값 |
|:---|:---|
| Concept_ID | `IACS_A2_APP_001` |
| Scheme / Source_Doc_Type | `IACS` / `UR` |
| Applicability_Text@en | *(A2.0–A2.2의 원문: 대상, 임계값, 제외, 시행일 포함)* |
| Target_Entity | `Ship` |
| Ship_Type | `Conventional_Ship` |
| Size_Threshold | `GT >= 500` |
| Exclusion@en | `high speed craft; special purpose ships; offshore units` |
| Trigger_Date | `2022-01-01` |
| Source_Doc / Source_Locator | `UR A2` / `A2.0, A2.1, A2.2` |

> **포인트**: Applicability_Text에서 entity(A1) → ship type(A2) → threshold(A3) → exclusion(A6) → trigger(A7) 순으로 패턴을 적용한다.

---

## 11. 소스 패밀리 빠른 참조

| 측면 | IMO | IACS | KR | EU |
|:---|:---|:---|:---|:---|
| **Source_Doc_Type** | Convention, Mandatory_Code, Resolution, Circular | UR, UI, Rec, PR | Rule, Guidance, Interpretation | Directive, Regulation_EU, Decision |
| **기본 집행력** | Source_Doc_Type별(Section 3.7a): Convention/Mandatory_Code → `mandatory`; Recommendatory_Code/Circular → `recommendatory`; Resolution → 비워둠 | Source_Doc_Type별(Section 3.7a): UR/PR → `mandatory`; UI → `interpretive`; Rec → `recommendatory` | Source_Doc_Type별(Section 3.7a): Rule/Technical_Rule → `mandatory`; Guidance → `guidance`; Interpretation → `interpretive` | Directive/Regulation_EU → `mandatory`; Decision → 맥락 의존 |
| **Target_Role 사용** | 높음(Flag_State, Port_State, Company, Master) | 낮음 | 낮음 | 중간(Flag_State, Shipowner, Company) |
| **Implements_Requirement** | 통상 비워둠(최상위) | IMO 참조(명시적 조문 수준 상호 참조만) | 명시적 조문 수준 상호 참조가 있을 때만 기입; 그렇지 않으면 Phase 2로 이연 | 해당 시 IMO 협약 참조 |
| **세분도** | 규정 또는 조문 | 문서 1건(UR, UI, Rec 또는 PR) | 가장 낮은 자율적 적용범위 조항(흔히 Section 수준, 예: `Sec.1 101 Application`) | 조문 수준 범위 조항 |

---

## 12. 출력 사양

모든 최종 출력 파일은 instruction이 실행되는 작업 디렉터리 하의 **`results/`** 하위 디렉터리에 저장된다. 청크별 중간 파일(분할 처리 중 생성된 부분 TSV 및 로그 파일)은 **`results/temp/`**에 저장된다. 두 디렉터리는 존재하지 않을 경우 자동으로 생성된다. 각 추출 실행은 `results/`에 정확히 **3개의 최종 파일**을 생성한다: 결과 파일 1개, 요약 파일 1개, 로그 파일 1개. `results/temp/`의 중간 파일은 추적성을 위해 보존되지만 산출물로 간주되지 않는다.

### 12.1 파일 명명 규칙

| 파일 | 명명 패턴 | 설명 |
|:---|:---|:---|
| **결과** | `phase1_applicability_result.tsv` | TSV 형식(탭 구분 값)의 최종 추출 테이블. Section 3의 대상 스키마에 부합하는 모든 추출 레코드를 포함. 헤더 행 1개 + 데이터 행. UTF-8 with BOM. |
| **요약** | `phase1_applicability_summary.md` | Markdown 형식의 추출 요약 보고서. |
| **로그** | `phase1_applicability_log.md` | Markdown 형식의 처리 로그. |

### 12.2 결과 파일 (`phase1_applicability_result.tsv`)

- **형식**: TSV (탭 구분 값), UTF-8 with BOM
- **헤더 행**: Section 3.1에 정의된 컬럼명을 정확히 그대로, 탭으로 구분
- **컬럼 순서**: `Concept_ID	Record_Type	Scheme	Source_Doc_Type	Applicability_Text@en	Target_Entity	Target_Role	Target_Object@en	Ship_Type	Size_Threshold	Qual_Predicate@en	Geographic_Scope@en	Cargo_Substance@en	Normative_Basis	Implements_Requirement	Exclusion@en	Trigger_Event	Trigger_Date	Normative_Status	Applicability_Status	Source_Doc	Source_Locator	Editor_Note`
- **빈 셀**: 비워둔다("N/A" 또는 "-" 같은 자리 표시자 사용 금지)
- **다중값 구분자**: 셀 내 세미콜론(`;`), Section 3.1에 따름
- **인용**: 탭, 줄바꿈 또는 큰따옴표를 포함하는 필드는 큰따옴표로 감싸야 한다. 내장된 큰따옴표는 `""`로 이스케이프
- **정렬 순서**: `Source_Doc`(오름차순), 그 다음 `Source_Locator`(문서 순서)

### 12.3 요약 파일 (`phase1_applicability_summary.md`)

요약 파일은 다음 섹션을 포함해야 한다:

```markdown
# Phase 1 APPLICABILITY 추출 요약

## 실행 정보
- 날짜: {YYYY-MM-DD}
- 처리된 소스 문서: {수}
- 총 추출 레코드: {수}

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

## Applicability_Status별 레코드
| 상태 | 건수 |
|:---|---:|
| explicit | {n} |
| partial | {n} |
| unclear | {n} |
| composite | {n} |

## 품질 플래그
- Phase 2 백로그 항목: {수}
- Editor_Note 플래그: {수}
- 앵커 추적성 오류: {수}

## 이슈 / 관찰 사항
- {자유 텍스트: 주목할 결정, 모호함, 이연 항목}
```

### 12.4 로그 파일 (`phase1_applicability_log.md`)

로그 파일은 순차 처리 추적을 기록한다:

```markdown
# Phase 1 APPLICABILITY 처리 로그

## {Source_Doc} — {Section/Chapter}
- **세그먼트**: {세그먼트 번호} / {총 세그먼트}
- **토큰 (약)**: {n}K
- **추출 레코드**: {수}
- **결정사항**:
  - {소스 조항}: 채택 / 제외 — {사유}
  - ...
- **플래그**:
  - {Concept_ID}: {플래그 설명}
  - ...
```

### 12.5 덮어쓰기 규칙

각 신규 추출 실행은 `results/`의 이전 최종 출력 파일과 `results/temp/`의 모든 중간 파일을 **덮어쓴다**. 점진적 보존이 필요한 경우, 사용자가 새로운 실행을 시작하기 전에 이전 파일을 이름 변경하거나 보관해야 한다.

---

## 13. Phase 1.1 — 검증 예외 관리

Phase 1 산출물의 반복 검증 과정에서 반복되는 코멘트가 식별되면 체계적 해결을 위해 Phase 1.1로 에스컬레이션한다. Phase 1.1은 추가 추출 단계가 **아니라** QA 예외 계층이다.

**전체 사양**: [`phase1_1_validation_exception_guide.md`](phase1_1_validation_exception_guide.md) 참조(3개 Phase 1 instruction 공유).

**에스컬레이션 기준(요약)**:
- 코멘트가 2회 이상 반복되거나 2개 이상 문서/레코드에서 발생
- 이슈가 검증 패스를 차단
- 현 가이드 텍스트가 모호 — 검토자 간 올바른 행동에 대해 의견 불일치
- Phase 1 / Phase 2 경계가 불분명

**Phase 1 덮어쓰기 규칙과의 주요 차이점**: Phase 1.1 이슈 레지스터는 **버전 관리되며 절대 덮어쓰지 않는다**(`results/phase1_1/phase1_1_issue_register_{date}_v{NN}.tsv`).

---

## 14. Phase 2 미리보기

Phase 2 이연 항목의 전체 목록은 **Appendix A** 참조. Section 4.2의 이연 태그(`[Phase 2: ...]`)가 Phase 2 진입점이 된다. Phase 1.1의 `defer_phase2` 처분 항목도 Phase 2 진입 후보가 된다.

| 항목 | 설명 |
|:---|:---|
| Broader/Related 부여 | `skos:broader` 및 `skos:related` 관계 부여 |
| 빈도/적합성 평가 | 용어 빈도 및 통제어휘 적합성 평가 |

---

*Phase 1 범위: **IMO, IACS, KR, EU** 문서에서 출처 충실한 적용범위 추출, 23개 컬럼(Geographic_Scope 및 Cargo_Substance 포함)으로 구조화 분해, `{Scheme}_..._APP_` 패턴의 안정적 ID, 전체 추적성을 갖춘 원문 앵커 텍스트, Record_Type 판별자, Source_Doc_Type 분류, Target_Role 식별, 교차 소스 계층을 위한 Implements_Requirement, A11/A12/A15 패턴(무효화, 소급, 경과)의 Phase 1 포착. 출력: `results/`에 3개 최종 파일(결과 TSV + 요약 MD + 로그 MD), `results/temp/`에 중간 청크 파일.*

---
---

# 부록

## Appendix A — Phase 2 미리보기 (이연 항목)

Phase 2로 이연된 항목: 교차 소스 추론(`superseded_by`, `overrides_if`, `hybrid_split`), 교차 소스 매핑(`skos:closeMatch`/`exactMatch`), 공식 불리언 적용범위 논리, 시간적 체인 해결, 전체 소급/경과/무효화 **추론**(Phase 1은 Section 4.2에 따라 원시 데이터를 포착; Phase 2가 체인 해결을 수행), 열거형을 위한 SKOS ConceptScheme URI, 동등성/면제, SHACL 자동화 검증, TRUE_DEF-APPLICABILITY 연결, `Interprets_Requirement` 컬럼, Normative_Force/Decision_Modality 분리, **`Applicability_Status = inferred`**(맥락에서 도출된 적용범위는 Phase 2 추론 후에만 허용).

---

## Appendix B — 기본 URI 패턴 및 네임스페이스 접두사

### 기본 URI

- 패턴: `https://{domain}/maritime-cv/{Concept_ID}`
- `{Concept_ID}`는 Scheme 접두사를 포함한 **전체** Concept_ID 값이다(예: `IACS_A2_APP_001`, `A2_APP_001`이 아님). Scheme 접두사는 전역 고유성을 보장하기 위해 URI의 일부이다.
- 예: `https://example.org/maritime-cv/IACS_A2_APP_001`
- 예: `https://example.org/maritime-cv/IMO_SOLAS_II_1_R3_8_APP_001`
- 예: `https://example.org/maritime-cv/KR_STEEL_PT3_CH1_APP_001`

### 네임스페이스 접두사

```turtle
@prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
@prefix dct:   <http://purl.org/dc/terms/> .
@prefix xkos:  <http://rdf-vocabulary.ddialliance.org/xkos#> .
@prefix mreg:  <https://example.org/maritime-cv/> .
```

> 컬럼-속성 매핑은 Section 3.1의 SKOS/DC Mapping 열에 명시되어 있다.
> `xkos:exclusionNote`는 `skos:scopeNote`의 하위 속성이다. `mreg:` (maritime regulation) 접두사는 모든 출처 계열(IMO, IACS, KR, EU)을 포괄하는 프로젝트 공통 커스텀 네임스페이스이다.

---

## Appendix C — 작업 예시 (상세)

아래에는 **핵심 차별화 컬럼**만 표시한다. 기본값이거나 비어 있는 컬럼은 생략한다. 전체 23-column 레코드는 Section 3.1을 따른다.

### C.1 IACS UR A2 (소스: A2.0–A2.2)

> "This UR is to apply to design and construction of shipboard fittings and supporting structures used for the normal towing and mooring operations of conventional ships. Conventional ships means new displacement-type ships of 500 GT and above, excluding high speed craft, special purpose ships, and offshore units of all types. This UR applies to ships subject to SOLAS regulation II-1/3-4. Ships contracted for construction on or after 1 January 2022..."

| 컬럼 | 값 |
|:---|:---|
| Concept_ID | `IACS_A2_APP_001` |
| Scheme / Source_Doc_Type | `IACS` / `UR` |
| Target_Entity | `Ship` |
| Target_Object@en | `shipboard fittings and supporting hull structures` |
| Ship_Type | `Conventional_Ship` |
| Size_Threshold | `GT >= 500` |
| Normative_Basis | *(비워둠 — 동일 참조가 Implements_Requirement에 기록됨; Section 6 규칙에 따라 중복하지 않음)* |
| Implements_Requirement | `SOLAS II-1/3-4` |
| Exclusion@en | `high speed craft; special purpose ships; offshore units; escort towing; canal transit towing; emergency towing for tankers` |
| Trigger_Date | `2022-01-01` |
| Source_Doc / Source_Locator | `UR A2` / `A2.0, A2.1, A2.2` |
| Editor_Note | `UR A2 Rev.5 (Sep 2020) 원문은 "SOLAS regulation II-1/3-4"를 인용 — 출처 충실 원칙에 따라 원문 그대로 유지. 그러나 II-1/3-4는 유조선의 비상 예인 장치를 다루고, 예인 및 계선 장비(GT >= 3000, 2024-01-01)에 대한 안전 계선 규정은 MSC.474(102)에 의해 추가된 II-1/3-8이다. [Phase 2: A2 후속 개정이 SOLAS 상호 참조를 II-1/3-4에서 II-1/3-8로 갱신하는지 확인; 비상 예인 범위를 별도 APP 레코드로 분리 고려]` |

### C.2 IMO SOLAS II-1/Reg.3-8

> "Ships of 3,000 gross tonnage and above, constructed on or after 1 January 2024, shall be provided with arrangements for towing and mooring equipment..."

| 컬럼 | 값 |
|:---|:---|
| Concept_ID | `IMO_SOLAS_II_1_R3_8_APP_001` |
| Scheme / Source_Doc_Type | `IMO` / `Convention` |
| Target_Entity | `Ship` |
| Target_Object@en | `towing and mooring equipment; shipboard fittings and supporting hull structures` |
| Size_Threshold | `GT >= 3000` |
| Trigger_Date | `2024-01-01` |
| Source_Doc / Source_Locator | `SOLAS II-1` / `Reg.3-8` |
| Editor_Note | `MSC.474(102)에 의해 추가 — 안전 계선 규정. II-1/3-4는 유조선의 비상 예인 장치를 다루는 별도 규정. [Phase 2: IACS_A2_APP_001과 교차 소스 연결]` |

### C.3 KR Rules for Steel Ships (Pt.3 Ch.1 Sec.1)

> "The requirements in this Chapter apply to the hull structural design and construction of steel ships of 90 m in length and above, intended for unrestricted ocean service..."

| 컬럼 | 값 |
|:---|:---|
| Concept_ID | `KR_STEEL_PT3_CH1_APP_001` |
| Scheme / Source_Doc_Type | `KR` / `Rule` |
| Target_Entity | `Ship` |
| Target_Object@en | `hull structural design and construction` |
| Size_Threshold | `L >= 90 m` |
| Qual_Predicate@en | `steel ships; unrestricted ocean service` |
| Source_Doc / Source_Locator | `KR Rules Pt.3 Ch.1` / `Sec.1` |
| Editor_Note | `90m 미만 선박은 Pt.11로 안내. [Phase 2: alternative_rule] [Phase 2: implements_mapping — KR은 규칙이 SOLAS 및 IACS UR을 반영한다고 명시하나, 이 범위 조항에 조문 수준 상호 참조 없음]` |

---

## Appendix D — 이연 패턴 상세 (A9–A15)

| # | 패턴 | 행동 |
|:---:|:---|:---|
| A9 | 교차 소스 대체 | "supersedes UR X", "replaces UR Y", "amends Regulation Z" → Editor_Note에 `[Phase 2: superseded_by]` 태그 |
| A10 | 하이브리드 분할 | "for single skin holds apply Z10.2, for double skin holds apply Z10.5" → `[Phase 2: hybrid_split]` 태그 |
| A11 | 조건부 무효화 | "unless the flag Administration determines otherwise" → **Phase 1 포착**: `Qual_Predicate@en`에 무효화 조건 기록 + Editor_Note에 `[Phase 2: unless]` 태그 |
| A12 | 소급 적용 | "existing ships built before [date]" → **Phase 1 포착**: "existing ships" 한정어와 함께 `Trigger_Event`/`Trigger_Date`에 기록 + Editor_Note에 `[Phase 2: retrospective]` 태그 |
| A13 | 대안 규칙 | "if excluded, apply IGC Code requirements instead" → Editor_Note에 `[Phase 2: alternative_rule]` 태그 |
| A14 | 동등성 / 면제 | "equivalent arrangement as accepted by the Administration" → Editor_Note에 `[Phase 2: equivalence]` 태그 |
| A15 | 경과 규정 | "ships complying with [old regulation] need not comply until [date]" → **Phase 1 포착**: `Trigger_Event`/`Trigger_Date`에 경과 일자 기록 + Editor_Note에 `[Phase 2: transitional]` 태그 |
