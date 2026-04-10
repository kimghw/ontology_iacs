# pdf2md — markdownlint 규칙 가이드

본 파일은 pdf2md 스킬의 **단일 출처(SSOT)**로서 서브에이전트가 변환 중 준수해야 할 markdownlint 규칙과 오케스트레이터가 병합 후 실행할 검증 대상 규칙을 함께 정의한다. 규칙은 상시 갱신될 수 있다.

- **서브에이전트**: 변환 시작 전 이 파일을 Grep으로 조회하여 전환 시점에 피할 수 있는 위반을 미리 피한다. 권장 조회: `Grep pattern='^- \*\*MD' path='.claude/skills/pdf2md/markdownlint_rules.md' output_mode='content'`.
- **오케스트레이터**: 병합 후 `markdownlint` CLI를 실행하여 위반 목록을 얻고, 본 파일의 규칙 설명을 참조하여 자가 수정 방향을 결정한다. 수정·재검증·사용자 보고·`agent_report.md` append는 오케스트레이터 책임이다.

## 변환 시점에 피할 수 있는 규칙 (서브에이전트 사전 회피)

규칙 ID는 `MD###` 형식.

- **MD022** (blanks-around-headings): 모든 제목 위/아래에 빈 줄 1줄을 둔다.
- **MD031** (blanks-around-fences): 코드 펜스 위/아래에 빈 줄 1줄을 둔다.
- **MD040** (fenced-code-language): 코드 펜스에 언어를 명시한다. 모르면 `text`.
- **MD041** (first-line-h1): `is_first_part=true`인 경우 파일 첫 줄은 H1이어야 한다. `false`면 해당 없음(오케스트레이터가 병합 후 판단).
- **MD025** (single-h1): H1은 문서 전체에 1개. `is_first_part=false`면 H1을 찍지 않는다.
- **MD036** (no-emphasis-as-heading): 강조(`**굵게**`)를 제목 대용으로 쓰지 않는다. 진짜 제목이면 `##`~`######`로. 개정이력·문서 종료 표식 등은 평문으로.
- **MD024** (no-duplicate-heading): 원문에 동일 제목이 여럿이면 원문 그대로 두되, 번호·맥락으로 구분되도록 유지한다.
- **MD033** (no-inline-html): 첨자(`<sub>`/`<sup>`)는 원문 의미 보존상 **삭제하지 않는다**. disable 디렉티브는 오케스트레이터가 병합 후 1회 주입한다(서브에이전트 금지).

## 병합 후 검증 대상 규칙 (오케스트레이터 사후 검증)

오케스트레이터는 `markdownlint <file>` 실행 후 아래 규칙 위반을 우선 처리한다.

- **MD001** (heading-increment): 제목 계층이 한 단계씩 증가.
- **MD029** (ol-prefix): 번호 매기기 증가 규칙.
- **MD024** (no-duplicate-heading): 중복 제목.
- **MD042** (no-empty-links): 링크 유효성.
- **MD025** (single-h1): H1 1개.
- **MD041** (first-line-h1): 문서 첫 줄 H1.
- 표 형식·빈 줄·공백 정리 등 구조·포맷 수정(원문 텍스트·의미는 변경 금지).

## 갱신 규칙

- 본 파일을 수정하면 `SKILL.md`의 4.7은 참조만 유지한다(규칙 재이식 금지).
- 규칙 추가·삭제 시 해당 규칙의 "회피 시점(변환 중/병합 후)" 구분을 명시한다.
- 갱신 이력은 git history로 관리한다(파일 내 changelog 섹션 두지 않음).

### 피드백 갱신 절차 (오케스트레이터용)

`markdownlint` 실행 결과를 본 파일에 반영할 때의 병합 정책.

1. **기존 데이터 우선 고려**: 먼저 현재 파일의 규칙 목록·분류·설명을 Read로 확인한 뒤 변경안을 만든다.
2. **중복 금지**: 이미 등록된 `MD###`는 재등록하지 않는다. 설명 보강이 필요하면 기존 문장 의미를 뒤집지 않는 범위에서만 추가한다.
3. **신규 규칙**: 해당 섹션(회피/검증) 끝에 동일 형식으로 append.
4. **차이가 큰 변경(하단 협의 섹션으로 이동)**: 아래 중 하나라도 해당하면 본문 섹션을 수정하지 말고, 파일 하단 `## 사용자 협의 필요` 섹션에 `- [YYYY-MM-DD] <입력파일>: <관찰 내용> / <제안>` 형식으로 append하고 사용자 결정 대기.
   - 신규 규칙이 3개 이상 한꺼번에 등장
   - 기존 규칙의 분류(회피 ↔ 검증)를 바꿔야 함
   - 기존 설명과 상충하는 해석이 필요
   - 프로젝트 전역 린트 정책(`.markdownlint.json`)과 본 파일이 어긋남
5. 본문 직접 수정과 협의 섹션 append는 **동일 실행에서 혼용하지 않는다**(변경 추적 혼선 방지).

## 사용자 협의 필요

- [2026-04-09] UR_A/C/D/E/F (83 PDFs): 이번 실행에서 관찰된 신규 규칙 5종 — 3개 임계 초과로 본문 직접 수정 대신 협의 섹션에 기록.
  - **MD007** (ul-indent): 관찰 사례 — ur-a2rev5에서 단락(`(1) For strength...`) 아래 불릿 목록을 3칸 들여쓰기로 배치. 사용자 측 수정: 들여쓰기 제거. 제안: "변환 시점 회피" 섹션에 `- **MD007** (ul-indent): 목록 상위가 목록이 아니면 불릿 들여쓰기 0칸. 단락 하위 불릿은 공백 없이 시작.`
  - **MD026** (no-trailing-punctuation): 관찰 사례 — ur-d7rev3, ur-f37del-1의 헤딩 끝 마침표. 제안: "변환 시점 회피" 섹션에 `- **MD026** (no-trailing-punctuation): 헤딩 끝 문장부호(`.`, `;`, `:`, `!`, `?`) 제거. 본문 문장이 아닌 제목 라인은 마침표 없이 작성.`
  - **MD030** (list-marker-space): 관찰 사례 — UR-E26 line 403 `-  ` (공백 2). 제안: "변환 시점 회피" 섹션에 `- **MD030** (list-marker-space): 목록 마커 다음 공백은 정확히 1칸(`- item`, `1. item`). 탭·이중공백 금지.`
  - **MD034** (no-bare-urls): 관찰 사례 — UR-E26 line 695의 `https://us-cert.cisa.gov/...`. 제안: "병합 후 검증" 섹션에 `- **MD034** (no-bare-urls): 원문 URL은 `<...>` 각괄호로 감싼다. 오케스트레이터가 병합 후 `sed`로 일괄 처리 가능.`
  - **MD056** (table-column-count): 관찰 사례 — UR-E10의 대형 표(셀 내부 중첩 표 포함). 제안: 셀 내부에 `|` 등장 시 파서가 열 분리로 오인. 회피 어려움(마크다운 한계). 권장: 해당 파일 단위로 `.markdownlint.json` MD056 비활성화. "병합 후 검증" 섹션에 `- **MD056** (table-column-count): 셀 내부 파이프 문자가 포함된 중첩 표가 있으면 비활성화 허용(원문 구조 복원 우선).`

- [2026-04-09] 오탈자 자동 수정 정책 이슈: `language_tool_python` + `en-US` 기본 사전이 IACS 선박 기술 문서의 영국식 철자(draught/moulded/manoeuvring/centre/fibre/vapour/recognise/analyse/categorise 등)와 복합 기술 용어(twistlock/weatherdeck/downflooding/pumproom/portlights/longitudinals)를 **단일 후보 TYPOS**로 반환하여 자동 수정 시 내용 파괴(예: `FPSOs → FPS Os`, `Shell → She'll`, `markdownlint-disable → markdown lint-disable`). 제안:
  - ✅ **반영 완료** (2026-04-10): SKILL.md 오탈자 자동 수정 범위에서 `BRITISH_ENGLISH_DETECTOR` 룰을 제외. 영국식 철자는 원문 그대로 보존한다.
  - 본 실행에서는 report-only로 1386건을 `reports/pdf2md_typo_report_2026-04-09.json`에 저장.
