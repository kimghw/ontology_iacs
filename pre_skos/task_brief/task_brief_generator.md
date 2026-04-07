# Phase 1 — Task Brief 생성 지침 (LLM용)

> 이 문서는 **LLM이 Work Unit(WU)별 Task Brief를 자동 생성**할 때 따르는 메타 지침입니다.
> 사람이 대상 WU와 추출 범위(TRUE_DEF / APPLICABILITY / CONTROLLED_TERM)를 지정하면,
> LLM이 마스터 지침서와 원문을 읽고 이 문서의 절차에 따라 Task Brief를 생성합니다.
>
> **WU_Key 형식**:
> - Standalone (1 doc = 1 WU): `{doc_key}` (예: `ur_e26`)
> - Split (1 doc → N WUs): `{doc_key}_wu{NNN}` (예: `ur_z10_2_wu001`)
> - Merged (N docs → 1 WU): `{doc_key1}+{doc_key2}+...` (예: `ur_f1+ur_f2+ur_f3`)

---

## 1. 입력

LLM은 다음을 입력으로 받습니다:

| # | 입력 | 설명 |
|:---|:---|:---|
| 1 | **마스터 지침서** | 아래 3개 파일 (전문 또는 지정 섹션) |
|   | `pre_skos/phase1_true_def_instruction.md` | TRUE_DEF 추출 규칙 (12열 스키마) |
|   | `pre_skos/phase1_applicability_instruction.md` | APPLICABILITY 추출 규칙 (23열 스키마) |
|   | `pre_skos/phase1_controlled_term_instruction.md` | CONTROLLED_TERM 추출 규칙 (16열 스키마) |
| 2 | **대상 문서** | 추출할 원문 파일 (MD 또는 PDF) |
| 3 | **사용자 지시** | 추출 범위 (TD / APP / CT 중 택), 특별 주의사항 등 |

---

## 2. Task Brief 생성 절차

### Step 1 — 문서 식별

원문을 읽고 아래 항목을 결정합니다:

| 항목 | 결정 기준 |
|:---|:---|
| **Document** | 문서 식별자 (예: `UR A2`, `SOLAS II-1`, `KR Rules Pt.3 Ch.1`, `Directive 2009/45/EC`) |
| **Authority** | 발행 체계: `IMO` / `IACS` / `KR` / `EU` |
| **DocType** | 마스터 지침서 Section 3.6 (또는 3.2a)의 닫힌 목록에서 선택 |
| **DocumentKey** | Concept_ID용 정규화 키 (정규화 규칙 Step 1~7 적용) |
| **문서 버전** | 개정 번호, 날짜 |

> **용어 대응표**: `Document` = 구 `Source_Doc`, `Authority` = 구 `Scheme`, `DocType` = 구 `Source_Doc_Type`, `DocumentKey` = 구 `SourceKey`. 마스터 지침서(TD/APP/CT)의 스키마 컬럼명(`Scheme`, `Source_Doc`, `Source_Doc_Type`)은 TSV 출력 시 그대로 사용하되, 본 절차서의 개념 참조에는 새 용어를 사용합니다.

### Step 2 — 문서 구조 분석

원문의 섹션 구조를 파악하고, 각 섹션이 어떤 Instruction에 해당하는지 매핑합니다:

| 섹션 유형 | 해당 Instruction | 판별 기준 |
|:---|:---|:---|
| "Definitions" / "For the purpose of this..." | **TRUE_DEF** | 용어를 명시적으로 정의하는 섹션 |
| "Application" / "Scope" / "General" / 적용범위 전문 | **APPLICABILITY** | 적용 대상, 제외, 시행일을 기술하는 섹션 |
| 본문 요건 (위 두 섹션 이외) | **CONTROLLED_TERM** | 규범적 행위, 장비, 절차, 역할 등을 기술하는 섹션 |

각 섹션에 대해 기록합니다:
- 위치 (섹션 번호)
- 내용 요약 (1줄)
- 예상 레코드 수 (추정)
- 예상 토큰 수 (추정)

### Step 2a — Work Unit 라우팅 테이블

PRE 산출물(`wu-{wu_key}__pre__meta.json`)의 Work Unit 정보를 Task Brief에 통합합니다. Task Brief는 **WU 단위로 1개씩** 생성되므로, 이 테이블에는 해당 WU의 행만 포함됩니다. 이 테이블은 WU가 어떤 Instruction에 해당하는지, 어떤 추출 계획을 따르는지를 매핑합니다.

| WU_ID | Chunk_Key | Heading Range | Start_Line | End_Line | Est_Tokens | Instructions | Extraction Focus |
|:---|:---|:---|:---|:---|:---|:---|:---|
| `{wu_id}` | `{chunk_key}` | `{heading range}` | `{n}` | `{n}` | `{n}` | `{TD;APP;CT}` | `{해당 WU에서 주로 추출할 내용 요약}` |

각 WU에 대해 기록:
- **Instructions**: 이 WU에서 실행할 Instruction 목록 (Step 2의 섹션-Instruction 매핑에서 파생)
- **Extraction Focus**: 이 WU에서 주의할 패턴, 특이사항, 경계 조건
- **SeqNo Range**: `wu-{wu_key}__pre__meta.json`에서 가져온 예약 범위 (wu_key로 매핑)

> 이 테이블이 `commands/agents.md` §1.2의 에이전트 패킷 생성 시 참조됩니다. 서브에이전트는 자신의 WU_ID에 해당하는 행만 읽으면 작업 범위를 파악할 수 있습니다.

#### 대용량 문서 분할 규칙

문서 전체가 **~64K token을 초과**하는 경우, Chapter/Annex 단위로 분할합니다 (documentSplit 임계값 = 64K; Chunk 목표 ≤ 32K; see `prerequisite.md` §1.3.2 A):

1. **분할 기준**: Chapter, Part, Annex 등 문서의 자연스러운 구조적 경계를 따름
2. **분할 키(Chunk Key)**: SourceKey 뒤에 분할 식별자를 추가
   - 예: `SOLAS_II_1` → chunk 1: `SOLAS_II_1_CH1`, chunk 2: `SOLAS_II_1_CH2`
   - 예: `KR_PT3_CH1` → (분할 불필요 시 그대로 유지)
3. **Task Brief 분할 여부**: Task Brief는 **WU 단위 1개**로 생성하며, 해당 WU가 포함하는 chunk 구간을 내부에 표기
4. **출력 파일은 chunk 단위로 분리하지 않음** — 문서 단위 TSV 1개에 통합 (SeqNo로 구분)
5. **에이전트 처리**: chunk 단위로 순차 처리하되, 결과는 동일 TSV에 append

### Step 3 — Instruction별 추출 계획

사용자가 지정한 Instruction 각각에 대해, 아래 내용을 작성합니다:

#### TRUE_DEF 계획 (해당 시)

1. **추출 위치**: 정의 섹션의 정확한 위치
2. **추출 대상 용어 목록**: 문서에서 식별된 정의 용어를 표로 나열 (prefLabel 후보 + 위치)
3. **주요 정의 패턴**: "X means...", bold headword 등 이 문서에서 사용되는 패턴
4. **분리 패턴 주의사항**: 마스터 지침서 Section 4의 분리 패턴 중 이 문서에서 해당되는 것
   - 내장 하위 정의 → `[Phase 2: extract]`
   - 범위 제한 꼬리문 → Scope_Note 분리
   - 예시/열거 → Example 분리
   - 약어 → altLabel
5. **스키마 확인**: 12열, 고정값 명시 (Record_Type=`TRUE_DEF`, Scheme=`{값}`, Source_Doc_Type=`{값}`, Source_Doc=`{값}`)

#### APPLICABILITY 계획 (해당 시)

1. **추출 위치**: 적용범위 섹션의 정확한 위치
2. **Scope Block 분리**: 독립적 적용범위 문장을 식별하여 블록 단위로 나눔 (1건 = 1 scope block)
3. **블록별 분해 계획**: 각 scope block에 대해 23열 중 해당 컬럼의 예상 값
   - Target_Entity, Ship_Type, Size_Threshold, Exclusion, Trigger 등
4. **Normative_Status**: Source_Doc_Type 기반 기본값 + 원문 override 여부
5. **Applicability_Status**: `explicit` / `partial` / `unclear` / `composite` 판정
6. **Implements_Requirement**: 명시적 조항 수준 교차 참조 유무 확인
   - 있으면 → 기입
   - 일반적 "reflects/incorporates" 수준이면 → 비우고 `[Phase 2: implements_mapping]` 태그
7. **스키마 확인**: 23열, 고정값 명시

#### CONTROLLED_TERM 계획 (해당 시)

1. **추출 위치**: 본문 요건 섹션 범위 (정의/적용범위 섹션 제외)
2. **예상 Term_Category 분포**: 이 문서에서 주로 등장할 카테고리 (예: Test, Manufacturing, Safety_Equipment 등)
3. **주요 추출 패턴**: 마스터 지침서 Section 4.1~4.2의 패턴 중 이 문서에 해당하는 것
4. **TRUE_DEF 중복 배제**: 정의 섹션에서 이미 TRUE_DEF로 추출된 용어는 CONTROLLED_TERM에서 제외
5. **Normative_Status**: Source_Doc_Type 기반 기본값
6. **스키마 확인**: 16열, 고정값 명시

### Step 4 — 문서 특이사항

이 문서에서만 발생하는 특수한 상황을 기록합니다:
- 한국어 텍스트 혼재 여부
- 다른 문서에 대한 명시적 교차 참조
- 개정 이력에서 주의할 점
- 정의 섹션과 본문의 경계가 모호한 경우
- 하나의 섹션이 여러 Instruction에 걸치는 경우

### Step 5 — 검증 체크리스트 생성

마스터 지침서의 검증 규칙(TRUE_DEF Section 10.2 / APPLICABILITY Section 8.2 / CONTROLLED_TERM 해당 절)에서 **이 문서에 적용되는 항목만** 추출하여 체크리스트를 작성합니다. 고정값(Scheme, Source_Doc_Type 등)을 미리 채워 넣습니다.

### Step 6 — 출력 사양

결과 파일의 경로와 형식을 지정합니다.

---

## 3. Task Brief 출력 양식

아래 양식에 따라 Task Brief를 생성합니다.
`{...}` 부분을 Step 1~6의 결과로 채웁니다.

---

````markdown
# Phase 1 — Task Brief: {Document} (WU: `{wu_key}`)

> 마스터 지침서: `pre_skos/phase1_true_def_instruction.md`, `pre_skos/phase1_applicability_instruction.md`, `pre_skos/phase1_controlled_term_instruction.md`

---

## 0. WU 정보

| 항목 | 값 |
|:---|:---|
| **WU_Key** | `{wu_key}` |
| **WU Type** | `{standalone / split / merged}` |
| **Document** | `{Document}` |
| **Authority** | `{Authority}` |
| **DocType** | `{DocType}` |
| **DocumentKey** | `{DocumentKey}` |
| **추출 대상** | {TRUE_DEF / APPLICABILITY / CONTROLLED_TERM — 해당하는 것} |
| **문서 파일** | `{파일 경로}` |
| **문서 버전** | {버전 정보} |
| **문서 언어** | {영어 / 영어+한국어 혼용} |

> TSV 출력 시 컬럼명은 마스터 지침서 스키마를 따름: `Scheme`={Authority}, `Source_Doc`={Document}, `Source_Doc_Type`={DocType}

### Split WU인 경우 (1 doc → N WUs)

> 이 섹션은 WU Type이 `split`인 경우에만 포함합니다.

| 항목 | 값 |
|:---|:---|
| **Parent Document** | `{doc_key}` |
| **WU 범위** | Lines `{start_line}`–`{end_line}` |
| **Heading Range** | `{시작 heading}` ~ `{끝 heading}` |
| **전체 WU 수** | `{N}` (이 문서의 총 split WU 수) |

### Merged WU인 경우 (N docs → 1 WU)

> 이 섹션은 WU Type이 `merged`인 경우에만 포함합니다.

**Constituent Documents:**

| # | Doc_Key | Document | Lines | 비고 |
|:---|:---|:---|:---|:---|
| 1 | `{doc_key1}` | `{Document1}` | `{start}`–`{end}` | {비고} |
| 2 | `{doc_key2}` | `{Document2}` | `{start}`–`{end}` | {비고} |
| ... | ... | ... | ... | ... |

---

## 1. 문서 구조

| 섹션 | 위치 | 해당 Instruction | 내용 요약 |
|:---|:---|:---|:---|
| {섹션명} | {위치} | {TD/APP/CT} | {요약} |
| ... | ... | ... | ... |

---

## 1a. Work Unit 라우팅 테이블

> PRE 산출물(`wu-{wu_key}__pre__meta.json`)에서 이 WU(`{wu_key}`)에 해당하는 정보. Task Brief가 WU 단위이므로 이 테이블에는 해당 WU의 정보만 포함됩니다.

| WU_Key | Chunk_Key | Heading Range | Lines | Est_Tokens | Instructions | SeqNo Range (TD/APP/CT) | Extraction Focus |
|:---|:---|:---|:---|:---|:---|:---|:---|
| `{wu_key}` | `{chunk_key}` | `{heading range}` | `{start}–{end}` | `{n}` | `{TD;APP;CT}` | `{range}` | `{focus}` |
| ... | ... | ... | ... | ... | ... | ... | ... |

---

## 2. Concept_ID 규칙

| 항목 | 값 |
|:---|:---|
| **DocumentKey** | `{정규화된 키}` |
| **TRUE_DEF** | `{Authority}_{DocumentKey}_TD_{SeqNo}` |
| **APPLICABILITY** | `{Authority}_{DocumentKey}_APP_{SeqNo}` |
| **CONTROLLED_TERM** | `{Authority}_{DocumentKey}_CT_{SeqNo}` |

> TSV 출력 시 Concept_ID의 `{Authority}` 부분은 마스터 지침서의 `Scheme` 값과 동일합니다.

### SeqNo 할당 전략

- SeqNo는 DocumentKey 내에서 단조 증가하며, **한 번 할당된 번호는 재번호하지 않음** (gaps 허용)
- **Work Unit별 SeqNo 범위 사전 예약**: `wu-{wu_key}__pre__meta.json`의 `SeqNo_Range_{TD,APP,CT}` 필드에 기록된 범위를 사용
  - 예: WU001 → `001`~`049`, WU002 → `050`~`099`, WU003 → `100`~`199`
  - 예약 범위를 초과할 경우 다음 빈 범위로 확장
- 병렬 에이전트(TD/APP/CT)는 각각 독립 시퀀스이므로 충돌 없음 (`_TD_001`과 `_APP_001`은 별개)

---

## 3. TRUE_DEF 추출 지침

> (해당하지 않으면 "이 문서에서는 TRUE_DEF 추출 대상 없음" 또는 "사용자가 미지정"으로 기재)

### 추출 위치
{정의 섹션 위치}

### 추출 대상 용어

| # | prefLabel 후보 | altLabel 후보 | 위치 |
|:---|:---|:---|:---|
| 1 | {용어} | {약어 등} | {위치} |
| ... | ... | ... | ... |

### 정의 패턴
- {이 문서에서 사용되는 정의 패턴}

### 분리 패턴 주의사항
- {해당되는 분리 패턴과 처리 방법}

### 스키마 (12열)
```
Concept_ID | Record_Type(=TRUE_DEF) | Scheme(={Authority}) | Source_Doc_Type(={DocType}) | prefLabel@en | altLabel@en | Definition@en | Scope_Note@en | Example@en | Source_Doc(={Document}) | Source_Locator | Editor_Note
```
**필수**: Concept_ID, Record_Type, Scheme, Source_Doc_Type, prefLabel@en, Definition@en, Source_Doc, Source_Locator

---

## 4. APPLICABILITY 추출 지침

> (해당하지 않으면 "이 문서에서는 APPLICABILITY 추출 대상 없음" 또는 "사용자가 미지정"으로 기재)

### 추출 위치
{적용범위 섹션 위치}

### Scope Block 분리

| # | Block ID | 적용 대상 요약 | 핵심 분해 |
|:---|:---|:---|:---|
| 1 | APP_001 | {요약} | Target_Entity=`{값}`, Ship_Type=`{값}`, ... |
| ... | ... | ... | ... |

### Normative_Status
- 기본값: `{Source_Doc_Type 기반 기본값}`
- Override: {있으면 기재}

### Applicability_Status
- {각 블록별 판정}

### Implements_Requirement
- {명시적 교차 참조 유무 및 처리 방법}

### 스키마 (23열)
```
Concept_ID | Record_Type(=APPLICABILITY) | Scheme(={Authority}) | Source_Doc_Type(={DocType}) | Applicability_Text@en | Target_Entity | Target_Role | Target_Object@en | Ship_Type | Size_Threshold | Qual_Predicate@en | Geographic_Scope@en | Cargo_Substance@en | Normative_Basis | Implements_Requirement | Exclusion@en | Trigger_Event | Trigger_Date | Normative_Status(={기본값}) | Applicability_Status | Source_Doc(={Document}) | Source_Locator | Editor_Note
```
**필수**: Concept_ID, Record_Type, Scheme, Source_Doc_Type, Applicability_Text@en, Target_Entity, Applicability_Status, Source_Doc, Source_Locator

---

## 5. CONTROLLED_TERM 추출 지침

> (해당하지 않으면 "이 문서에서는 CONTROLLED_TERM 추출 대상 없음" 또는 "사용자가 미지정"으로 기재)

### 추출 위치
{본문 요건 섹션 범위 — 정의/적용범위 섹션 제외}

### 예상 Term_Category 분포

| Term_Category | 예상 빈도 | 예시 용어 |
|:---|:---|:---|
| {카테고리} | {高/中/低} | {예시} |
| ... | ... | ... |

### 주요 추출 패턴
- {이 문서에 해당하는 CT 패턴}

### TRUE_DEF 중복 배제
- {정의 섹션에서 이미 추출된 용어 목록 — 이 용어들은 CT에서 제외}

### Normative_Status
- 기본값: `{Source_Doc_Type 기반 기본값}`

### 스키마 (16열)
```
Concept_ID | Record_Type(=CONTROLLED_TERM) | Scheme(={Authority}) | Source_Doc_Type(={DocType}) | Term_Category | Term_Subclass | Domain_Facet | prefLabel@en | altLabel@en | Source_Form@en | Definition_Context@en | Deontic_Pattern@en | Normative_Status(={기본값}) | Source_Doc(={Document}) | Source_Locator | Editor_Note
```
**필수**: Concept_ID, Record_Type, Scheme, Source_Doc_Type, Term_Category, Term_Subclass, Domain_Facet, prefLabel@en, Source_Form@en, Definition_Context@en, Normative_Status, Source_Doc, Source_Locator

---

## 6. 문서 특이사항

- {특이사항 목록}

---

## 7. 검증 체크리스트

### 공통
- [ ] 필수 필드 빈 셀 없음
- [ ] Concept_ID 접두사 `{Authority}_` = Scheme `{Authority}`
- [ ] Source_Doc_Type = `{DocType}`
- [ ] 영어 필드에 한국어 없음
- [ ] Concept_ID 중복 없음 (WU 내 + Cross-WU)
- [ ] SeqNo가 해당 WU의 예약 범위 내

### TRUE_DEF (해당 시)
- [ ] Concept_ID: `{Authority}_{DocumentKey}_TD_{SeqNo}`
- [ ] Record_Type = `TRUE_DEF`
- [ ] Definition = 원문 정의 핵심 (verbatim)
- [ ] 정의 내용이 Scope_Note에 혼입되지 않음
- [ ] APPLICABILITY 전용 컬럼 빈칸

### APPLICABILITY (해당 시)
- [ ] Concept_ID: `{Authority}_{DocumentKey}_APP_{SeqNo}`
- [ ] Record_Type = `APPLICABILITY`
- [ ] Applicability_Text = 원문 충실
- [ ] 구조화 컬럼 → Applicability_Text에서 추적 가능
- [ ] Size_Threshold 형식: `param op value unit`
- [ ] Trigger_Date: ISO 8601
- [ ] TRUE_DEF 전용 컬럼 빈칸

### CONTROLLED_TERM (해당 시)
- [ ] Concept_ID: `{Authority}_{DocumentKey}_CT_{SeqNo}`
- [ ] Record_Type = `CONTROLLED_TERM`
- [ ] Term_Category 값이 닫힌 목록에 포함
- [ ] Term_Subclass 값이 해당 Category의 닫힌 목록에 포함
- [ ] Domain_Facet 값이 닫힌 목록에 포함
- [ ] TRUE_DEF/APPLICABILITY 전용 컬럼 빈칸

### Cross-Instruction 검증
- [ ] TD와 CT 간 용어 중복 없음 (정의 섹션에서 TD로 추출된 용어가 CT에 재등록되지 않음)
- [ ] APP 전용 컬럼(Target_Entity, Ship_Type 등)이 TD/CT 레코드에 혼입되지 않음
- [ ] TD 전용 컬럼(prefLabel, Definition 등)이 APP 레코드에 혼입되지 않음
- [ ] CT 전용 컬럼(Term_Category, Term_Subclass 등)이 TD/APP 레코드에 혼입되지 않음
- [ ] 패턴 카탈로그 cross-check: TD 패턴이 APP/CT 추출에 혼입되지 않았는지, 그 반대도 확인

---

## 8. 출력

### 실행 단위 산출물 (WU 단위)

> 모든 실행 수준 산출물은 `wu-{wu_key}` 접두사를 사용합니다.

| 파일 | 경로 |
|:---|:---|
| TRUE_DEF 결과 | `results/wu-{wu_key}__true_def__result.tsv` |
| APPLICABILITY 결과 | `results/wu-{wu_key}__applicability__result.tsv` |
| CONTROLLED_TERM 결과 | `results/wu-{wu_key}__controlled_term__result.tsv` |
| 요약 | `results/wu-{wu_key}__{instruction}__summary.md` |
| WU 로그 | `results/wu-{wu_key}__{instruction}__log.md` |

### 보조 산출물

| 파일 | 경로 | 비고 |
|:---|:---|:---|
| 추출 문장 (TD) | `results/wu-{wu_key}__true_def__extracted_segments.md` | WU별 |
| 추출 문장 (APP) | `results/wu-{wu_key}__applicability__extracted_segments.md` | WU별 |
| 추출 문장 (CT) | `results/wu-{wu_key}__controlled_term__extracted_segments.md` | WU별 |
| 패턴 카탈로그 (TD) | `results/corpus__true_def__patterns.tsv` | **Instruction별 통합** |
| 패턴 카탈로그 (APP) | `results/corpus__applicability__patterns.tsv` | **Instruction별 통합** |
| 패턴 카탈로그 (CT) | `results/corpus__controlled_term__patterns.tsv` | **Instruction별 통합** |
| 미추출 문장 (remainder) | `results/wu-{wu_key}__{instruction}__remainder.md` | WU별 |

> **파일명 규칙**: `prerequisite.md`의 3-part 패턴(`{scope}__{phase}__{artifact}`)을 따릅니다. 실행 수준 산출물의 scope는 `wu-{wu_key}`, PRE 단계 산출물의 scope는 `doc-{doc_instance_key}`입니다. 마스터 지침서(TD §11, APP §12)의 고정 파일명은 standalone 실행 시 기본값이며, Task Brief 기반 실행 시에는 본 문서의 규칙이 우선합니다.
````

---

## 4. 생성 규칙

1. **마스터 지침서를 읽되 전문을 복사하지 않는다.** Task Brief에는 이 문서에 해당하는 핵심만 포함한다.
2. **원문을 반드시 읽는다.** 원문을 읽지 않고 추측으로 Task Brief를 채우지 않는다.
3. **사용자가 지정하지 않은 Instruction은 "미지정"으로 기재한다.** 임의로 추가하지 않는다.
4. **고정값을 미리 채운다.** Authority(→Scheme), DocType(→Source_Doc_Type), Document(→Source_Doc), Record_Type 등 이 문서에서 변하지 않는 값은 스키마 라인에 `(={값})`으로 표기한다.
5. **추출 대상 용어/블록을 사전 식별한다.** TRUE_DEF는 용어 목록, APPLICABILITY는 scope block 분리, CONTROLLED_TERM은 예상 카테고리 분포를 미리 제시한다.
6. **Instruction 간 경계를 명확히 한다.** 정의 섹션 → TD, 적용범위 섹션 → APP, 나머지 본문 → CT. 경계가 모호한 경우 문서 특이사항에 기록한다.
7. **검증 체크리스트에 고정값을 삽입한다.** 범용 체크리스트가 아닌, 이 문서에 특화된 체크리스트를 생성한다.
8. **파일명은 3-part 패턴을 따른다.** `{scope}__{phase}__{artifact}` 형식. 실행 수준 scope는 `wu-{wu_key}`, PRE 수준 scope는 `doc-{doc_instance_key}`. `prerequisite.md`의 File Naming Conventions 참조.
9. **Work Unit 라우팅 테이블을 반드시 포함한다.** PRE의 `wu-{wu_key}__pre__meta.json`에서 해당 WU 메타데이터를 Task Brief §1a에 통합하여, 서브에이전트가 자신의 작업 범위를 즉시 파악할 수 있게 한다.
10. **모든 실행 산출물은 `wu-{wu_key}` 접두사를 사용한다.** 병렬 에이전트 실행 시 파일 충돌을 방지한다.
11. **Split WU는 Parent Document 범위를 명시한다.** Task Brief §0에서 이 WU가 커버하는 라인 범위와 heading 범위를 기재한다.
12. **Merged WU는 Constituent Documents를 명시한다.** Task Brief §0에서 병합된 doc_key 목록과 각각의 라인 범위를 기재한다.

---

## 5. 워크플로우 요약

```
사용자: "UR A2에서 TRUE_DEF, APPLICABILITY 추출해줘"
    │
    ▼
prerequisite.md: PRE 실행 → heading 구조, Work Unit 등록, 메타데이터
    │
    ▼
LLM: 마스터 지침서 3개 읽기 (필요 섹션만)
    │
    ▼
LLM: 대상 문서 (ur-a2rev5.md) 읽기
    │
    ▼
LLM: Step 1~6 수행 → Task Brief 생성 (§1a Work Unit 라우팅 포함)
    │
    ▼
LLM: Task Brief를 pre_skos/tasks/wu-{wu_key}__pre__task_brief.md 에 저장
    │
    ▼
사용자: Task Brief 검토/승인
    │
    ▼
agents.md: WU별 에이전트 패킷 생성 → 서브에이전트에 배분
    │
    ▼
서브에이전트: WU 범위 내 추출 실행 → results/ 에 wu-{wu_key} TSV
    │
    ▼
agents.md §6: 계층 병합 (WU → Chunk → Document → Master)
    │
    ▼
Phase 1 완료 → Phase 2
```

### Aggregation 단계

> 상세 병합 절차는 `commands/agents.md` §6 참조. 여기서는 요약만 기술합니다.

**계층 병합 흐름:**

1. **WU → Chunk**: 같은 Chunk 내 WU 결과(`wu-{wu_key}__*__result.tsv`)를 heading 순서로 합치고, 경계 중복 제거
2. **Chunk → Document**: Chunk 결과를 문서 순서로 합치고, Cross-WU/Cross-Instruction 검증
3. **Document → Master**: 검증 완료된 Document 결과를 corpus 마스터 TSV로 합산

| 마스터 파일 | 병합 대상 |
|:---|:---|
| `results/corpus__true_def__master.tsv` | `results/wu-*__true_def__result.tsv` |
| `results/corpus__applicability__master.tsv` | `results/wu-*__applicability__result.tsv` |
| `results/corpus__controlled_term__master.tsv` | `results/wu-*__controlled_term__result.tsv` |

- Concept_ID 전역 중복 검사
- 헤더 행 1회만 유지
- Sort: `Document` (ascending) → `WU_Key` (ascending) → `Source_Locator` (document order)

---

*마스터 지침서 위치:*
- *`pre_skos/phase1_true_def_instruction.md`*
- *`pre_skos/phase1_applicability_instruction.md`*
- *`pre_skos/phase1_controlled_term_instruction.md`*

*Task Brief Generator 정본: `pre_skos/task_brief/task_brief_generator.md` (본 문서)*
*Task Brief 저장 위치: `pre_skos/tasks/` (파일명: `wu-{wu_key}__pre__task_brief.md`)*

> **주의**: `pre_skos/phase1_task_brief_generator.md`는 본 문서의 이전 사본입니다. 본 문서(`pre_skos/task_brief/task_brief_generator.md`)를 정본으로 사용하고, 이전 사본은 삭제하거나 본 문서로의 참조로 대체하십시오.
