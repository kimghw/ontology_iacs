# Step 2 — 제목 구조 추출

> **목적.** LLM-스크립트 협력 프로세스(Pass 1–4)를 사용하여 정규 입력 문서에서 완전한 제목 구조를 추출하고, 제목별 토큰 수를 측정한다. 이 결과는 청킹 및 Work Unit 할당(Step 3)의 기초가 된다.

---

## 2.0 작업 명세서

### 목적

정규 입력 문서에서 완전한 제목 구조를 추출하고, 제목별 토큰 수를 측정한다.
이 결과는 Step 3의 청킹 및 Work Unit 할당의 입력으로 사용한다.

### 입력

- 정규 입력 문서 (Step 1에서)
- (선택) 기존 DocType 문법

### 핵심 분기

| 조건 | 처리 모드 |
|:---|:---|
| Document ≤ {{split_threshold:64K}} 토큰 | 1 Document = 1 에이전트, Pass 1–4 수행 → 토큰 측정 |
| Document > {{split_threshold:64K}} 토큰 | documentSplit 사전 분할 → documentSplit별 Pass 1–3 → Coordinator 병합 → 문서 수준 Pass 4 → 토큰 측정 |

### 최종 산출물

> 파일 명명 규칙과 전체 산출물 카탈로그는 [pre_specification_ko.md](pre_specification_ko.md) §파일 명명 규칙 및 §산출물 카탈로그를 참조한다.

- #1 `doc-{doc_instance_key}__heading__structure.tsv` — 최종 제목 트리 (Heading_ID, 계층, 줄 범위, 토큰 수). Step 3 청킹의 직접 입력.
- #2 `doc-{doc_instance_key}__heading__regex_spec.json` — Pass 2–4에서 사용된 정규식 패턴 배열. 동일 DocType 후속 문서에 재사용.
- #5 `doctype-{DocType}__heading__grammar_v{NN}.md` — DocType별 제목 문법 정의 (계층 구조, 번호 체계, 패턴). 버전 관리됨.
- #8 `doc-{doc_instance_key}__heading__coverage.json` — 문서 전체 줄의 제목/비제목 분류. 누락 검증용.
- #7c `doc-{doc_instance_key}__heading__discrepancy_final.tsv` — Pass 4 후 남은 Warning/Info 항목. 승인 시 감사 추적용.
- #9 `scripts/step2_regex_runner.py` — 고정 정규식 실행 스크립트 (모든 문서에서 재사용 가능). §정규식 실행기 참조.

### 완료 기준

- Error = 0
- Warning ≤ max(3, ⌈total_headings × 0.02⌉)
- **평가 시점:** Pass 4 완료 후 최종 `structure.tsv` 기준으로 평가. Pass 3 반복 중의 Error는 수렴 기준(§2.4)에서 관리.

### 다음 단계

→ Step 3: Work Unit Packing (`step3_workunit_packing.md`)

---

## 2.1 용어 및 처리 단위

| 단위 | 성격 | 조건 | 키 형식 | 예시 |
|:---|:---|:---|:---|:---|
| **documentSplit** | 대형 Document의 임시 줄 기반 사전 분할. 제목 추출에만 사용; 병합 후 폐기. 인접 documentSplit 간 {{split_overlap:100}}줄 겹침. | Document > {{split_threshold:64K}} 토큰 | `{doc_instance_key}_s{NNN}` | `ur_a2_rev5_en_s001` |
| **Chunk** | 최종 제목 정렬 세그먼트 (목표 ≤ {{chunk_max:32K}} 토큰). 검증된 제목 구조가 있어야만 생성. | 모든 Document (≤ {{chunk_max:32K}} → 단일 Chunk = 1 Document; > {{chunk_max:32K}} → 재귀적 분할) | `{doc_instance_key}_ch{NNN}` | `ur_a2_rev5_en_ch001` |

> **documentSplit vs Chunk:** documentSplit는 추출 전 임시 분할이고, Chunk는 추출 후 최종 분할이다.
>
> **기본 동작:** Document ≤ {{chunk_max:32K}} 토큰 → 단일 Chunk = 1 Document. Document > {{chunk_max:32K}} 토큰 → 제목 경계에서 재귀적 분할. Document > {{split_threshold:64K}} 토큰 → 제목 추출 전 documentSplit 사전 분할.

### 중간 산출물 (처리 후 폐기)

> 최종 산출물은 §2.0 작업 명세서를 참조한다.

- `doc-{doc_instance_key}__heading__extraction_llm.tsv` — Pass 1에서 LLM이 추출한 제목 목록. 잠정 Heading_ID, Heading_Level, Heading_Number, 줄 번호를 포함. Pass 2 교차 확인의 기준선.
- `doc-{doc_instance_key}__heading__extraction_script.tsv` — Pass 2에서 정규식 러너가 전수 스캔한 전체 매치 결과. 제목 추출의 **기준선**.
- `doc-{doc_instance_key}__heading__discrepancy.tsv` — Pass 3에서 LLM이 스크립트 기준선을 검토·보정한 결과. 오탐/누락/수준 보정 판정과 Severity(Error/Warning/Info)를 기록. 반복별 `_iter{N}` 접미사로 판단 이력 보존.
- `doc-{doc_instance_key}__heading__validated.tsv` — Pass 3에서 보정 완료된 확정 제목 목록. 오탐 제거, 비정형 제목 추가, 수준/번호 수정이 반영된 상태. Pass 4 및 병합의 입력.
- `doc-{doc_instance_key}__heading__grammar_candidate.md` — 에이전트가 제출하는 문법 업데이트 제안. 새로 발견된 구조 패턴(번호 체계, 키워드 접두사)을 diff 형태로 기술. `results/grammars/staging/`에 저장되며 Coordinator가 병합 전까지 다른 에이전트가 재사용 불가.

---

## 2.2 전체 처리 흐름

> Step 1의 에이전트는 Document 목록 확정 후 종료되었다. 이 단계에서는 Document 또는 documentSplit 수준의 **새 에이전트**를 할당한다.

| Document 크기 | 처리 모드 |
|:---|:---|
| **≤ {{split_threshold:64K}} 토큰** | 1 Document = 1 에이전트. 단일 에이전트가 Pass 1–4와 토큰 측정을 실행. |
| **> {{split_threshold:64K}} 토큰** | 임시 documentSplit로 사전 분할. documentSplit 에이전트는 **Pass 1–3만** 실행. Coordinator가 결과와 문법 후보를 병합한 후 **문서 수준 Pass 4 에이전트**를 생성. |

가용 에이전트 수만큼 병렬로 할당. 항목이 에이전트 수를 초과하면 배치로 실행.

### 일반 Document (≤ {{split_threshold:64K}} 토큰)

1. **할당** — Document당 하나의 에이전트. 각 에이전트가 Pass 1–3을 실행 → 문법 후보를 `results/grammars/staging/`에 제출. Coordinator가 해당 DocType의 모든 후보를 수집하고, 확정된 문법으로 병합하며, 버전을 증가시킨다. 그런 다음 동일 에이전트(또는 새 에이전트)가 확정된 문법으로 Pass 4를 실행 → 토큰 측정.
2. **결과 보고** — 제목 구조 TSV 출력.

### 대형 Document (> {{split_threshold:64K}} 토큰)

1. **documentSplit로 사전 분할** — 에이전트가 컨텍스트 윈도우와 문서 크기를 고려하여 임시 documentSplit로 분할한다.
2. **documentSplit별 Pass 1–3** — 에이전트를 병렬 할당하여 각 documentSplit에서 독립적으로 Pass 1–3을 수행한다.
3. **병합** — Coordinator가 documentSplit 결과를 줄 번호 순서로 병합하고, 겹침 중복을 제거하며, 문서 수준 Heading_ID를 재할당한다.
4. **문서 수준 Pass 4** — 병합된 결과에 대해 Pass 4를 수행한다.
5. **documentSplit 폐기** — 모든 documentSplit 범위 중간 산출물을 폐기한다.

---

## 2.3 Pass 상세

각 에이전트가 할당된 Document(또는 대형 문서의 경우 documentSplit, Pass 1–3만)에 대해 스크립트 기반 추출 + LLM 보정 프로세스를 수행한다. **스크립트(정규식) 전수 스캔 결과가 기준선**이며, LLM은 문법 설계와 결과 보정을 담당한다.

### Pass 1 — LLM 문법 설계

LLM이 정규 입력 문서를 읽고 제목 문법과 정규식 사양을 설계한다.

1. **문서 분석** — 소스 패밀리, 구조적 계층 패턴(예: Part > Chapter > Regulation > Paragraph), 비표준 구조적 특징을 식별한다.
2. **제목 문법 초안 작성** — 계층 구조, 번호 체계, 키워드 접두사 등을 정리한다. 기존 DocType 문법이 있으면 이를 기반으로 보완한다.
3. **정규식 사양 생성** — 문법 초안에서 정규식 패턴을 도출한다. 러너가 실행할 수 있는 형식으로 출력한다.(note: heading은 문장을 포함하지 않음)

출력: `doc-{doc_instance_key}__heading__extraction_llm.tsv` (또는 `documentSplit-{...}__heading__extraction_llm.tsv`)

### Pass 2 — 스크립트 전수 스캔 및 누락 탐지

> 여기서 "스크립트"는 사전에 존재하는 외부 프로그램이 아니다. LLM이 Pass 1 결과와 문법 초안을 분석하여 **정규식 사양**(JSON 형식)을 생성하고, **고정 러너 스크립트**(`scripts/step2_regex_runner.py`)가 정규식 패턴을 정규 입력 문서에 대해 실행한다. 스크립트는 누락 후보뿐 아니라 **전체 매치 셋**을 생성한다. 불일치는 정렬(alignment)을 통해 산출한다.

4. **정규식 사양 생성 및 전수 스캔** — LLM이 Pass 1 결과와 문법 초안에서 정규식 패턴(번호 체계, `Part`, `Chapter`, `Reg.`, `Art.` 등 키워드 접두사)을 도출하여 **JSON 배열**로 출력한다. Coordinator(또는 러너 스크립트)가 각 패턴을 컴파일하고(`re.error` 발생 시 `Warning` 기록, 무시하지 않음), 정규 입력에 대해 실행하여 **전수 스크립트 매치 셋**을 생성한다.

   **러너 스크립트:** `scripts/step2_regex_runner.py`

   **정규식 사양 JSON 스키마:**

   ```json
   [
     {
       "pattern": "<명명된 캡처 그룹 포함 정규식>",
       "expected_level": "<HeadingLevel>",
       "number_group": "<제목 번호 캡처 그룹명 또는 null>",
       "text_group": "<제목 텍스트 캡처 그룹명 또는 null>",
       "flags": ["IGNORECASE"],
       "priority": 1,
       "notes": "선택적 설명"
     }
   ]
   ```

   > `number_group`과 `text_group`은 정규식 패턴 내 명명된 캡처 그룹을 가리킨다. 이를 통해 `Number_mismatch` 탐지가 가능하다. `number_group`이 null이면 `Number_mismatch`를 판정하지 않는다.
   >
   > 허용 `flags` 값: `IGNORECASE`, `MULTILINE`만 가능. 러너 이식성을 위해 다른 Python `re` 플래그는 허용하지 않는다.

   **다중 매치 해소:** 같은 줄에 여러 패턴이 매치되면, 러너는 `priority` 값이 가장 작은(1 = 최우선) 매치를 선택한다. 동순위 시 가장 긴 매치가 우선한다. 그래도 동순위이면 사양 배열에서 먼저 나오는 패턴이 우선한다. 해당 줄에는 선택된 매치만 전수 매치 셋에 포함한다.

5. **LLM 교차 검증** — LLM이 Pass 1 제목 목록을 스크립트의 전수 매치 셋과 정렬하여 각 항목을 분류한다:
   - `Agreed`: LLM과 스크립트 모두 같은 줄에서 제목을 식별
   - `LLM_only`: LLM이 추출했으나 스크립트 패턴에 매치되지 않음 (잠재적 오탐 또는 비정형 형식)
   - `Script_only`: 스크립트에 매치되었으나 LLM이 추출하지 않음 (잠재적 누락)
   - `Level_mismatch`: 양측 모두 제목으로 식별했으나 수준이 다름 (LLM 수준 vs 스크립트의 `expected_level`)
   - `Number_mismatch`: 양측 모두 제목으로 식별했으나 캡처된 번호가 다름 (정규식 사양에 `number_group` 필요; `number_group`이 null이면 판정하지 않음)

산출물: `doc-{doc_instance_key}__heading__extraction_script.tsv` (전수 매치 셋), `doc-{doc_instance_key}__heading__discrepancy.tsv`

`heading__extraction_script.tsv`는 `heading__extraction_llm.tsv`와 동일한 열 구조에 추가 열을 갖는다: `Matched_Pattern_Index` (int, 정규식 사양 배열 인덱스), `Matched_Text` (string, 패턴이 캡처한 텍스트).

### Pass 3 — 교차 검증 및 보정

Pass1과 Pass2를 교차검증하고 보정한다.

6. **교차 검증**
   - **문자열 매칭**  스크립트 기반으로 Pass1과 Pass2 결과를 매칭하여 판정
   - **LLM 결과 판별**  미스 매치 부분을 LLM 판별 후 보완(오탐 제거, 비정형 제목 보완, 수준/번호 보정)
   - **로그** 미스 매칭 및 처리 결과를 로그로 남김
7. **정규식 사양 업데이트** — 새로 발견된 구조적 패턴이 있으면 정규식 패턴을 추가하고, 문법 업데이트 제안을 `results/grammars/staging/`에 저장한다.

> **단일 기록자 원칙:** Coordinator만이 확정 문법 파일에 쓴다. 에이전트는 문법 후보를 staging에 저장하며, Coordinator가 병합 전까지 다른 에이전트가 재사용할 수 없다.

### Pass 4 — 최종 검증 및 보고

확정된 문법으로 재스캔하여 최종 누락을 확인하고, 커버리지를 검증한다.

8. **확정 문법으로 재스캔** — Coordinator가 프로모션한 확정 문법을 기반으로 정규식 사양을 업데이트하고, 러너가 전체 문서에 대해 재실행한다.
9. **LLM 최종 검토** — 플래그된 잔여 후보를 검토하고 최종 판정. 새 제목이 확정되면 추가하고 grammar candidate를 갱신. 다음을 수행:
   - **Coverage 점검**: 모든 줄을 제목 또는 비제목으로 분류. `doc-{doc_instance_key}__heading__coverage.json`을 생성하여 줄 범위와 분류를 기록.
   - **형식 일관성 검증**: 모든 제목이 확정 grammar 패턴을 따르는지 확인.
10. **최종 불일치 로그** — 작업 중인 discrepancy TSV에서 모든 잔여 Warning/Info 항목을 `doc-{doc_instance_key}__heading__discrepancy_final.tsv`로 추출. 이 파일은 승인 후 감사 추적을 위해 **프로모션**된다 (폐기되지 않음).

출력: `doc-{doc_instance_key}__heading__structure.tsv` (final), `doc-{doc_instance_key}__heading__regex_spec.json` (final; 동일 DocType 문서에서 재사용을 위해 프로모션됨), `doc-{doc_instance_key}__heading__coverage.json`, `doc-{doc_instance_key}__heading__discrepancy_final.tsv`

> **Pass 4 이후 grammar 업데이트:** Pass 4가 갱신된 grammar candidate를 생성하면, 에이전트가 이를 `results/grammars/staging/`에 저장한다. Coordinator가 최종 머지를 수행하고 grammar 버전을 증가시킨 후 이 DocType의 확정 grammar로 프로모션한다. 완전히 프로모션된 grammar는 동일 DocType의 후속 문서에서 재사용된다.

> **대형 문서의 Pass 4:** documentSplit 수준이 아닌 Coordinator 병합 후 문서 수준에서 실행된다.

---

## 2.4 수렴 기준 및 불일치 처리

### 반복 트리거 조건

- **반복 대상:** Pass 3 완료 시점에서 `Error > 0`이면 반복을 트리거한다. `Warning`만 남은 경우는 반복하지 않는다.
- **반복 범위:** Pass 2(정규식 사양 업데이트 포함)부터 Pass 3까지 재실행한다.
- **최대 반복 횟수:** 2회. 2번째 반복 후에도 `Error`가 남으면 에스컬레이션한다.

### 에스컬레이션 절차

- **대상:** 사용자(프로젝트 운영자).
- **형식:** 최종 불일치 TSV(`discrepancy_final.tsv`)와 함께 잔존 Error 목록을 첨부하여 보고한다.
- **후속 처리:** 에스컬레이션 후 해당 Document의 처리는 **일시 중단**한다. 사용자가 수동 보정 또는 추가 지시를 제공한 뒤 재개한다.

### 심각도 분류

- 정규식 매칭 결과 중 LLM이 제목 여부를 확정하기 어려운 항목(`Warning`)은 **최종 불일치 TSV**에 기록하고, 사용자 승인 시 검토를 요청한다.

| 심각도 | 기준 |
|:---|:---|
| `Error` | 누락 또는 명백한 오류 → **0건** 허용 |
| `Warning` | 판단 모호 → **≤ max(3, ⌈total_headings × 0.02⌉)** 허용, 초과 시 사용자 확인 |
| `Info` | 형식 차이 (구조 무관) → 기록만 |

### Coordinator 문법 병합 충돌 해소 규칙

- **동일 패턴에 다른 level 할당:** 해당 패턴을 매칭한 문서 내 출현 빈도가 높은 쪽을 채택한다. 빈도가 동일하면 더 낮은(상위) level을 채택한다.
- **패턴 중복:** 두 에이전트가 동일 제목을 다른 정규식으로 매칭한 경우, 더 구체적인(매칭 범위가 좁은) 패턴을 채택하고 나머지는 폐기한다.
- **해소 불가 충돌:** 자동 해소가 불가능한 경우, 충돌 내역을 사용자에게 보고하고 수동 결정을 요청한다.

---

## 2.5 제목별 토큰 측정

각 제목이 포함하는 하위 내용의 토큰 수를 측정한다. 열 정의는 §2.6 출력 스키마를 참조한다.

- **측정 방법**: `tiktoken` (`cl100k_base` 인코딩) 사용. 프로젝트 전체에서 동일 인코딩을 적용하여 Step 3 청킹 임계값과의 일관성을 보장한다.
- **대체 방법**: `tiktoken` 설치가 불가능한 환경에서는 `char_approx`(`ceil(char_count / {{approx_divisor:4}} × {{approx_multiplier:1.1}})`)를 사용한다. 이 경우 `Measure_Method` 열에 `char_approx`로 기록한다.
- **측정 시점**: Pass 4 완료 후, 최종 `heading__structure.tsv` 생성 시 수행.

---

## 2.6 출력 스키마

`doc-{doc_instance_key}__heading__structure.tsv`:

| 열 | 타입 | 필수 | 설명 |
|:---|:---|:---:|:---|
| `Heading_ID` | string | Yes | `{DocumentKey}_HD_{NNN}` — 최소 3자리, 0 패딩. 제목 수가 999를 초과하면 4자리 이상으로 확장. 000부터 시작 (DocumentRoot 행). |
| `Parent_Heading_ID` | string\|null | Yes | 부모 노드의 `Heading_ID`; DocumentRoot 행(Depth=0)은 빈 문자열. **TSV null 규약:** 빈 필드 (열 구분자 사이에 문자 없음). TSV에서 이는 행 중간 필드의 경우 인접한 두 탭, 마지막 열의 경우 탭 다음 줄바꿈을 의미한다. |
| `Depth` | int | Yes | 트리 깊이: DocumentRoot = 0(가상 행), 첫 번째 제목 수준 = 1 등. Depth는 원시 마크다운 제목 레벨이 **아니라** 문서 트리 계층에서의 위치에 의해 결정된다. Step 1.1 Markdown Lint(HL001)가 제목 레벨이 정확히 1씩 증가하도록 보장하므로, 린트 적용 후 Depth = 마크다운 `#` 개수 − 1이다. 린트가 적용되지 않아 레벨이 건너뛰어진 경우, 깊이를 순차 값으로 압축한다(예: `#` → `###`에 `##`가 없으면 Depth 1 → 2로 매핑, 1 → 3이 아님). |
| `Heading_Level` | string | Yes | 문서의 계층 수준 이름 (예: `DocumentRoot`, `Chapter`, `Part`, `Regulation`, `Paragraph`). Depth=0 행은 `DocumentRoot` 사용. |
| `Heading_Number` | string\|null | Yes | 문서에 나타나는 원본 번호 (예: `II-1`, `A`, `1.1.3`). DocumentRoot 행과 번호 없는 제목은 빈 문자열. |
| `Heading_Text` | string | Yes | 전체 제목 텍스트 |
| `Start_Line` | int | Yes | 정규 입력 파일에서 이 제목 범위의 첫 줄 (**포함**). DocumentRoot 행: 1줄. |
| `End_Line` | int | Yes | 이 제목 범위의 마지막 줄 (**포함**). 정의: 깊이 ≤ 현재 깊이인 다음 제목 바로 앞 줄. DocumentRoot 및 마지막 제목: 문서의 최종 줄 번호. |
| `Est_Tokens_Inclusive` | int | Yes | 하위를 포함한 전체 범위 `[Start_Line, End_Line]`의 토큰 수. **비가산.** |
| `Est_Tokens_Exclusive` | int | Yes | 자체 콘텐츠만의 토큰 수 (하위 제외). 서브트리 내에서 **가산**. 불변식: `parent.exclusive + Σ(children.inclusive) = parent.inclusive`. |
| `Measure_Method` | string | Yes | `tiktoken` 또는 `char_approx` |

> **TSV null 규약:** 빈 필드 사용 (열 구분자 사이에 문자 없음). TSV에서 이는 행 중간 필드의 경우 인접한 두 탭, 마지막 열의 경우 탭 다음 줄바꿈을 의미한다. 리터럴 문자열 `null`이나 `\N`을 쓰지 않는다.
>
> **첫 번째 행**(Depth=0)은 문서 자체를 나타내는 **가상 DocumentRoot 행**이다. 텍스트에서 추출한 제목이 아니다. 모든 실제 제목은 Depth ≥ 1. DocumentRoot의 `Est_Tokens_Inclusive`는 총 문서 토큰 수와 같고, `Est_Tokens_Exclusive`는 첫 번째 Depth=1 제목 이전의 콘텐츠(서문 텍스트)만 포함한다.

```tsv
Heading_ID	Parent_Heading_ID	Depth	Heading_Level	Heading_Number	Heading_Text	Start_Line	End_Line	Est_Tokens_Inclusive	Est_Tokens_Exclusive	Measure_Method
solas_ii_1_HD_000		0	DocumentRoot		SOLAS Chapter II-1	1	2830	38200	320	tiktoken
solas_ii_1_HD_001	solas_ii_1_HD_000	1	Part	A	General	47	312	4100	200	tiktoken
solas_ii_1_HD_002	solas_ii_1_HD_001	2	Regulation	1	Application	48	89	620	620	tiktoken
...
```

---

`doc-{doc_instance_key}__heading__regex_spec.json`:

| 필드 | 타입 | 필수 | 설명 |
|:---|:---|:---:|:---|
| `pattern` | string | Yes | 명명된 캡처 그룹 포함 정규식. Python `re` 호환. |
| `expected_level` | string | Yes | 매칭된 줄의 제목 수준 (예: `Chapter`, `Regulation`). |
| `number_group` | string\|null | Yes | 제목 번호를 캡처하는 명명된 그룹명. 해당 없으면 `null`. |
| `text_group` | string\|null | Yes | 제목 텍스트를 캡처하는 명명된 그룹명. 해당 없으면 `null`. |
| `flags` | string[] | Yes | 허용 값: `IGNORECASE`, `MULTILINE`만 가능. |
| `priority` | int | Yes | 다중 매칭 시 우선순위: 값이 작을수록 우선 (1 = 최우선) → 가장 긴 매치 → 배열 순서. |
| `notes` | string | No | 선택적 설명. |

---

> 파일 명명 규칙과 저장 경로는 [pre_specification_ko.md](pre_specification_ko.md) §파일 명명 규칙을 참조한다.
