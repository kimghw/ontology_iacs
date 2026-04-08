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
