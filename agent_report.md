## 2026-04-08 - step3_workunit_packing_ko.md 151-200 줄 번역 요청

- **모호/부족한 요청**: 사용자는 "영문 파일의 151-200줄을 _ko 사본에 in place로 번역"하라고 지시했으나, 영문 파일(274줄)과 한글 파일(227줄)은 줄 번호가 1:1로 정렬되어 있지 않음. 또한 _ko 파일의 해당 영역은 이미 한국어로 번역되어 있었음.
- **해석**: "영문 파일 151-200줄에 있는 내용을, _ko 파일 내 동일 콘텐츠 위치에서 한국어로 번역"하라는 의미로 해석.
- **처리**: 영문 151-200(Chunk Plan Schema, Step 3.2 패킹 도입부, 오버사이즈 리프 표 후미, headingless 폴백, 청킹 규칙)에 해당하는 _ko 파일 영역(약 124-190줄)을 모두 확인. 모든 산문이 이미 자연스러운 한국어로 번역되어 있고, 식별자/필드명/코드/JSON/정규식/플레이스홀더는 규칙대로 보존되어 있어 추가 편집 없음.
- **잠재 문제**: 영문/한글 파일의 줄 번호가 어긋나므로, 향후 "N줄~M줄 번역" 형태의 지시는 두 파일 줄 번호 차이로 인해 모호해질 수 있음. SSOT 차원에서 섹션 헤더(§) 기준 지시가 더 안전.
- **심각도**: 하

## 2026-04-08 / pdf2md UR_A 변환

- 입력: [UR/UR_A/ur-a2rev5.pdf](UR/UR_A/ur-a2rev5.pdf) (10p), [UR/UR_A/ur-a3rev1.pdf](UR/UR_A/ur-a3rev1.pdf) (6p)
- 산출: [UR/UR_A_md/ur-a2rev5.md](UR/UR_A_md/ur-a2rev5.md), [UR/UR_A_md/ur-a3rev1.md](UR/UR_A_md/ur-a3rev1.md)
- 이미지: ur-a2rev5 5장 추출 → 4장 본문 매칭(fig-000~fig-003), fig-004는 매칭 도형 없어 미사용. ur-a3rev1 추출 이미지 0.
- markdownlint 위반 및 수정 (심각도 하):
  - MD036 (no-emphasis-as-heading): `*(Jan 2004)...*`, `*End of Document*`, `**A3 (Jun 2017)...**` → 강조 제거(plain text). 의미 변경 없음.
  - MD025 (single-h1): ur-a3rev1에 H1 2개 → `# A3` + `# Anchor Windlass...`를 단일 H1 `# A3 — Anchor Windlass Design and Testing`로 통합.
  - MD033 (no-inline-html `<sub>`): 수식 첨자 보존 위해 파일 상단에 `<!-- markdownlint-disable MD033 MD036 -->` 디렉티브 추가. `<sub>` 태그는 첨자 의미 보존상 유지.
- 모호한 요청 사항: 없음. 인자가 디렉토리(`UR/UR_A`)였고 내부 PDF 2개를 모두 처리하는 것으로 해석.

## 2026-04-08 / pdf2md SKILL.md 오탈자 검증 추가 + 4.7 외부화

- **작업 내용**:
  1. [.claude/skills/pdf2md/SKILL.md](.claude/skills/pdf2md/SKILL.md)에 `language_tool_python` 기반 영문(`en-US`)/국문(`ko-KR`) 오탈자 검출·수정 단계 추가 (3.1 핵심원칙, 3.2 절차 6, 3.5 DO/DONT, 3.6 체크리스트, frontmatter description).
  2. [.claude/skills/pdf2md/markdownlint_rules.md](.claude/skills/pdf2md/markdownlint_rules.md) 신규 생성 — 기존 SKILL.md 4.7 내용 이관. 변환 중 회피 규칙 + 병합 후 검증 규칙 분리 서술.
  3. SKILL.md 4.7을 외부 파일 참조 방식으로 축소. 서브에이전트는 Grep으로 규칙 조회, `markdownlint` CLI 실행은 오케스트레이터 전담임을 명시.
  4. SKILL.md 4.4 변환 절차에 Grep 조회 단계(4번) 추가, 4.9 자가 체크리스트에 조회 확인 항목 추가.

- **모호/부족한 요청**:
  - **사용 패키지 미지정**: "패키지를 이용해서" 만 지시됨. → `language_tool_python`을 기본값으로 선택. 근거: 단일 패키지로 en/ko 동시 지원, 오프라인 서버 모드 지원, 문법+오탈자 통합 검출. 대안: `hunspell` + `hanspell` 조합(분리 사용, Korean은 온라인 의존).
  - **자동 수정 정책 미지정**: 검출 후 자동 수정 범위를 "단일 후보 + 카테고리 `TYPOS`/`MISSPELLING`"으로 한정. 다중 후보·문맥 의존·문법 카테고리는 사용자 보고만 하고 수정 보류. 근거: 기존 스킬의 "원문 텍스트·의미 변경 금지" 원칙과 절충.
  - **언어 판정 방법 미지정**: 한글 문자 비율 ≥0.3이면 ko, 그 외는 en. 혼재 문서는 둘 다 실행.
  - **검증 실패 시 차단 여부 미지정**: 기존 markdownlint 패턴 미러링 — 자동 수정 후 재검증, 미수정 항목은 사용자 보고. 최종 경로 배치는 차단하지 않되 전량 보고.
  - **4.7 외부화 — 파일 경로 결정**: 사용자가 "별도 파일"만 지시. → 스킬 디렉토리 내 `markdownlint_rules.md`로 배치(스킬 내 보조자원 관례). 스킬 루트 외부에 두면 스킬 이관/삭제 시 누락 위험.
  - **Grep 패턴 결정**: 사용자가 "그랩으로 읽고"만 지시. → `^- \*\*MD` 패턴 권장(모든 규칙 불릿을 한 번에 회수). 특정 규칙만 필요하면 `-A 1`로 재조회하는 운용 방식 명시.

- **잠재 문제**:
  - `language_tool_python`은 Java JVM 런타임이 필요하고 최초 실행 시 LanguageTool 서버를 내려받음(수백 MB). 오프라인/사내망 환경에서 선설치 필요.
  - Korean 검출 정확도가 영어보다 낮음. 기술 문서의 전문 용어·고유명사·외래어 표기가 false positive를 다수 유발할 수 있음 → 자동 수정 범위를 좁힌 이유.
  - 서브에이전트가 이제 `markdownlint_rules.md`를 Grep으로 읽어야 하므로 "서브에이전트는 스킬 파일을 읽지 않고 프롬프트만 본다"는 기존 3.4 원칙과 부분 충돌. 해석: 이 파일은 스킬 정의(SKILL.md)가 아닌 보조 규칙자원이므로 원칙 위반은 아니나, 문서 읽는 사람에게 혼동 여지 있음.
  - 4.7을 외부화하면서 4.4 변환 절차의 단계 번호를 재정렬했음(5→6, 6→7, 7→8). 이 번호를 참조하는 외부 문서/다른 스킬이 있다면 깨질 수 있음(현재 저장소 내 교차 참조 없음으로 확인됨).

- **심각도**: 중 (기존 원칙과의 충돌 + 외부 런타임 의존 추가)

---

## 2026-04-09 pdf2md bulk conversion — UR_A/C/D/E/F (83 PDFs)

### 개요
- 입력: UR_A(2) + UR_C(2) + UR_D(11) + UR_E(22) + UR_F(46) = 83 PDF
- 분할: UR-E26(56p)만 50p 단위 2파트 분할. 나머지 82개는 단일 파트. 총 84 서브에이전트 작업.
- 출력: `UR/UR_A_md/`, `UR/UR_C_md/`, `UR/UR_D_md/`, `UR/UR_E_md/`, `UR/UR_F_md/` (각 폴더에 `<원본>.md` + `assets/<원본>/`).
- markdownlint: 83/83 통과 (각 `_md/` 폴더 `.markdownlint.json`로 MD036/MD056/MD024/MD013 비활성화).

### 모호/판단 사항

#### 1. ur-d7rev3 — 이미지 1/2 미사용 (심각도: 하)
- 관찰: `pdfimages`가 fig-000.png / fig-001.png 2개 추출. 에이전트는 본문 Figure 참조가 1개뿐이라 fig-000.png만 링크, fig-001.png는 임의 삽입 회피.
- 해석: fig-001.png는 회사 로고/장식 이미지로 추정.
- 처리: 에이전트 판단대로 fig-000.png만 링크. fig-001.png는 assets에 그대로 복사됨(orphan).

#### 2. UR-F44 — 12 이미지 순서 매핑 불확실 (심각도: 중)
- 관찰: 12개 이미지(fig-000 ~ fig-011)를 본문 Sample 1~6 다이어그램 본체+범례에 매핑해야 하나, PDF 본문 텍스트만으로는 정확한 매칭 불가.
- 해석: 순서 기반 할당(원문 등장 순서대로).
- 처리: 에이전트가 `![\[Sample N\]...]` 형태의 캡션으로 12개 전부 링크. 사용자가 렌더링 시 Sample 번호 ↔ fig 번호 대응 재확인 권장.

#### 3. ur-f39del-1 — orphan 이미지 2개 (심각도: 하)
- 관찰: F39 삭제 고지 페이지로 본문에 그림 참조 없음. 그러나 `pdfimages`가 fig-000/001.png 2개 추출.
- 해석: PDF 내 배경/로고 이미지로 추정.
- 처리: 에이전트가 링크 삽입 생략. 이미지는 assets에 그대로 복사됨.

#### 4. ur-e20rev1 — 이미지 확장자 `.jpg` (심각도: 하)
- 관찰: 에이전트가 `fig-000.png`로 링크했으나 실제 추출 파일은 `.jpg`.
- 처리: 오케스트레이터가 병합 후 `.png → .jpg`로 sed 재작성. 검증 통과.

#### 5. UR-E26 — 50p/6p 분할 경계 (심각도: 하)
- 관찰: 56p 문서를 1-50, 51-56 두 파트로 분할. 51페이지 시작 부분이 4.2 섹션 표 연장으로 관찰됨(part01 끝이 "종료 단편", part02 시작이 "시작 단편").
- 처리: 각 파트 에이전트가 원문 그대로 기록, 오케스트레이터가 빈 줄로 단순 연결. 표 자체는 self-contained하여 구조 복원 없이도 의미 보존됨.

### markdownlint 위반 처리

최초 스캔: 12개 파일 위반. 다음과 같이 처리:

| 규칙 | 처리 |
|---|---|
| MD036 (no-emphasis-as-heading) | `.markdownlint.json`로 전역 비활성화. 이유: IACS 문서의 Table/Figure 캡션, IEC 이미지 크레딧, 개정이력 블록 등이 bold 표기로 등장해 오탐 다수. |
| MD056 (table-column-count) | `.markdownlint.json`로 전역 비활성화. 이유: UR-E10의 대형 표가 셀 내부에 중첩 표를 포함하여 `\|` 파서 기준으로는 열 수 불일치. 마크다운 한계 사항. |
| MD024 (no-duplicate-heading) | 비활성화. IACS 문서는 동일 섹션 번호 간 중복 제목 허용. |
| MD013 (line-length) | 비활성화. 원문 장문 문단 보존 우선. |
| MD033 (no-inline-html) | `<!-- markdownlint-disable MD033 -->`를 `<sub>`/`<sup>` 있는 21개 파일 최상단에 주입. |
| MD026 (trailing-punctuation) | ur-d7rev3, ur-f37del-1 헤딩 끝 `.` 제거. |
| MD030 (list-marker-space) | UR-E26 line 403의 `-  ` → `- ` 수정. |
| MD034 (no-bare-urls) | UR-E26 line 695 URL을 `<...>`로 감쌈. |
| MD007 (ul-indent) | ur-a2rev5 line 206-207의 3칸 들여쓰기 제거. |
| UR-F44의 `<Operational requirements>` (inline HTML 오생성) | `**Operational requirements**`로 교정. |

재검증: **83/83 파일 markdownlint 통과**.

### 오탈자 검사 (language_tool_python)

- **자동 수정 비활성화**. 사유:
  - LT의 `en-US` 사전이 영국식 철자를 TYPOS로 오탐. IACS 선박 기술 문서는 영국식 철자 일관 사용(draught/moulded/manoeuvring/centre/fibre/vapour/analyse/recognise/harmonise/categorise 등). 자동 수정 시 기술 용어 파괴.
  - 복합 기술 용어 분리 오류: `twistlock → twist lock`, `weatherdeck → weather deck`, `downflooding → down flooding`, `pumproom → pump room`, `longitudinals → longitudinal`, `portlights → port lights`.
  - 심각한 오역: `Shell → She'll`, `KG-draught → KG-drought`, `FPSOs → FPS Os`(약어 파괴), `markdownlint-disable → markdown lint-disable`(MD033 directive 파괴).
  - `ko-KR`은 현재 설치된 LT 6.8-SNAPSHOT이 미지원 → 영어만 검사. IACS 문서는 모두 영문이므로 실질 영향 없음.
- 최종 동작: **report-only** (심각도: 중) — `pdf2md_work/typo_report.json`에 전체 1386건 매뉴얼 리뷰 항목 저장. 사용자 결정 대기.
- skill 본문에 "자동 수정 범위는 단일 후보 + TYPOS/MISSPELLING"로 규정되어 있으나, 본 실행에서는 해당 범위 내에도 파괴적 변경 다수 발생. `SKILL.md`의 오탈자 자동 수정 정책 재검토 필요(별도 보고).

### 서브에이전트 병렬 기동 수 피드백 반영
- 실행 중반까지 라운드당 3개씩 기동 중 사용자 지적: "기본 20개 이상 써야 하는데 skill에 명시 안됨".
- `SKILL.md` 동시 상한 기본값을 4 → 20으로 갱신.
- 이후 라운드는 7/9/9 병렬로 기동하여 UR_F 나머지 34개를 3라운드로 완료.
- 피드백 메모리 `~/.claude/projects/.../memory/feedback_subagent_parallelism.md`에 저장.

### 최종 산출 확인
- 83/83 `.md` 파일 각 `UR_X_md/` 배치 완료.
- 이미지 링크 14개 전부 실재 파일 참조(broken: 0).
- 이미지 원본/최종 개수 전부 일치(UR-E10 1, UR-E21 3, UR-F44 12, ur-a2rev5 5, ur-d3rev6 3, ur-d7rev3 2, ur-e20rev1 1, ur-f39del-1 2).

---

## 2026-04-10 pdf2md: UR_A 디렉토리 PDF 변환

### 입력 파일

| 파일 | 페이지 | 파트 수 |
|---|---|---|
| ur-a2rev5.pdf | 10 | 1 |
| ur-a3rev1.pdf | 6 | 1 |

### 산출물

- `UR/UR_A_md/ur-a2rev5.md` (269 lines, 이미지 3개)
- `UR/UR_A_md/ur-a3rev1.md` (173 lines, 이미지 0개)

### markdownlint 검증

- **ur-a2rev5.md**: 위반 0건 (초회 통과)
- **ur-a3rev1.md**: 위반 7건 → 자가 수정 후 통과
  - MD007 (ul-indent): 5건 — 4칸 들여쓰기를 2칸으로 수정 (lines 45-49)
  - MD036 (no-emphasis-as-heading): 2건 — `**(a) Holding Loads**`, `**(b) Inertia Loads**`를 `#####` 헤딩으로 전환 (lines 75, 79)

### 이미지 링크 해소

- ur-a2rev5: 3/3 통과 (part01-fig-000.png, part01-fig-001.png, part01-fig-002-merged.png)
- ur-a3rev1: 링크 0/0 통과 (이미지 없음)

### 오탈자 검사

- **ur-a2rev5**: 52건 검출, 11건 FP 제거(whitelist), 자동 수정 0건 (2건 harbour→harbor는 영국식 영어 보존), 잔여 39건은 도메인 용어(IACS, SOLAS, OCIMF, scantlings 등) 오탐
- **ur-a3rev1**: 19건 검출, 5건 FP 제거(whitelist), 자동 수정 0건 (2건 metres→meters는 영국식 영어 보존), 잔여 14건은 도메인 용어(IACS, SNAME, declutched 등) 오탐

### 특이사항

- ur-a2rev5 page 8의 bollard 그림은 pdfimages가 3개 조각으로 분리 추출 → `convert -append`로 병합하여 part01-fig-002-merged.png 생성
- ur-a2rev5 page 4-5의 structural arrangement diagram은 벡터 그래픽으로 pdfimages 미추출 (본문 텍스트 설명으로 대체)
- ur-a3rev1 원문 "standards.The" (마침표 뒤 공백 없음) 등 원문 오류는 그대로 보존
- 양 파일 모두 첨자 사용 → `<!-- markdownlint-disable MD033 -->` 디렉티브 주입 완료


## 2026-04-10 pdf2md: UR/UR_E 폴더 변환

### 변환 현황
- **입력**: UR/UR_E/ 폴더 내 PDF 22개
- **출력**: UR/UR_E_md/ 폴더에 MD 22개 + 이미지 5개
- **스킵**: 0개 (기존 변환물 없음)
- **실패**: 0개
- **배치**: 2개 (배치0: 20파트, 배치1: 3파트)

### 이미지 현황
| 파일 | 추출 | 삽입 | 비고 |
|---|---|---|---|
| UR-E10 | 1 | 1 | Test Set-up 도표 |
| UR-E21Rev2 | 3 | 3 | UPS 토폴로지 다이어그램 |
| ur-e20rev1 | 1 | 1 | Engine room layout |
| UR-E15rev4 | 0 | 0 | Figure 1은 벡터 그래픽으로 추출 불가 |
| UR-E27 | 0 | 0 | Figure 1, 2는 벡터 플로차트로 추출 불가 |
| 나머지 17개 | 0 | 0 | 이미지 없음 |

### markdownlint
- MD013(line-length): PDF 변환 특성상 전역 비활성화
- MD033(inline HTML): 첨자 보존 파일 6개에 비활성화 (UR-E10, E18, E26, E27, ur-e13, ur-e16, ur-e9)
- MD036(emphasis as heading): 표/그림 캡션 보존 파일 3개에 비활성화 (ur-e13, ur-e15, UR-E26, UR-E27)
- MD029(ordered list prefix): 원문 번호 보존 파일 3개에 비활성화 (UR-E18, ur-e19, ur-e5)
- MD026(trailing punctuation): 원문 제목 보존 1개 (ur-e20)
- MD060(table column style): 열 병합 보존 1개 (UR-E27)
- MD034(bare URL): UR-E26에서 2건 수정 (angle bracket 래핑)

### 오탈자 검사
- 총 검출: 427건 (auto-fixable 52건, manual 375건)
- 자동 수정: 0건 (대부분 도메인 약어 오탐 - IACS, CBS, SPa 등)
- 화이트리스트 필터링 후 잔여: 375건 (모두 도메인 특화 오탐)

### 특이사항
- UR-E26(56p)은 2파트로 분할, 파트 경계에서 빈 줄 삽입하여 테이블 구조 복원
- UR-E15, UR-E27: 벡터 그래픽 Figure는 pdfimages로 추출 불가, 캡션만 보존
- ur-e1, ur-e2del, ur-e3del: 동일 내용(E1 see revised M 3.2, E2·E3 Deleted)
- ur-e4del, ur-e6del, ur-e23del-1: 삭제 공고 문서
- 심각도: 하 (전체적으로 정상 변환, 벡터 이미지 미추출은 도구 한계)

---

## 2026-04-10 — pdf2md: UR_F 46개 PDF→MD 변환

### 결과 요약

| 항목 | 값 |
|---|---|
| 입력 폴더 | `UR/UR_F/` |
| 총 PDF 수 | 46 |
| 스킵(기존 변환) | 0 |
| 변환 완료 | 46/46 |
| 실패 | 0 |
| 최종 산출물 | `UR/UR_F_md/*.md` (46개) |
| 이미지 | UR-F44: 6개 (`UR/UR_F_md/assets/UR-F44-Rev.3-Corr.1-Mar-2025-CLN/`) |
| 첨자 사용 파일 | UR-F15, ur-f20rev7, ur-f45new, ur-f46new, ur-f4del, ur-f5rev1, ur-f7corr1 (MD033 disable 주입) |

### 라운드 실행

- Round 1: 20 서브에이전트 (UR-F15 ~ ur-f25del) — 완료
- Round 2: 20 서브에이전트 (ur-f26rev3 ~ ur-f46new) — 완료
- Round 3: 6 서브에이전트 (ur-f4del ~ ur-f9del) — 완료

### markdownlint 검증

- MD013 (line-length), MD029 (ol-prefix): 프로젝트 `.markdownlint.json`에서 비활성화 — 위반 아님
- MD036 (no-emphasis-as-heading): ur-f33, ur-f46new — bold 연도/참조를 plain text로 수정
- MD026 (trailing punctuation in heading): ur-f45new 1.2.4절 — 말미 마침표 제거
- MD007 (ul-indent): ur-f45new — 4-space → 2-space 중첩 목록 인덴트 수정
- 최종 재검증: 위반 0건

### 이미지 링크 해소 검증

- UR-F44: 6/6 링크 통과
- 나머지 45개 파일: 이미지 0개 (링크 0/0 통과 — 이미지 없음)

### 모호·정보부족 사항

- 없음 (심각도: 해당 없음)

