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
