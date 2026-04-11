# pdf2md — markdownlint rule guide

This file serves as the **single source of truth (SSOT)** for the pdf2md skill, defining the markdownlint rules that sub-agents must observe during conversion, and the rules the orchestrator validates after merging. Rules may be updated at any time.

- **Sub-agent**: before starting conversion, Grep this file to proactively avoid violations that can be avoided during conversion. Recommended query: `Grep pattern='^- \*\*MD' path='.claude/skills/pdf2md/markdownlint_rules.md' output_mode='content'`.
- **Orchestrator**: after merge, run the `markdownlint` CLI to get a list of violations, and reference the rule descriptions in this file to decide the self-correction direction. Correction, re-validation, user reporting, and `agent_report.md` append are the orchestrator's responsibility.

## Rules avoidable during conversion (sub-agent proactive avoidance)

Rule IDs follow the `MD###` format.

- **MD022** (blanks-around-headings): Place one blank line above and below every heading.
- **MD031** (blanks-around-fences): Place one blank line above and below every code fence.
- **MD040** (fenced-code-language): Specify a language on every code fence. If unknown, use `text`.
- **MD041** (first-line-h1): When `is_first_part=true`, the first line of the file must be an H1. If `false`, N/A (determined by the orchestrator after merge).
- **MD025** (single-h1): Exactly one H1 per document. Do not emit H1 when `is_first_part=false`.
- **MD036** (no-emphasis-as-heading): Do not use emphasis (`**bold**`) as a heading substitute. If it is an actual heading, use `##`~`######`. Revision history, document-end markers, etc., in plain text.
- **MD024** (no-duplicate-heading): If the source has multiple identical headings, keep as in the source, but retain distinctions via numbering/context.
- **MD033** (no-inline-html): Subscripts (`<sub>`/`<sup>`) **are not removed**, to preserve source meaning. The disable directive is injected once by the orchestrator after merge (sub-agent must not).

## Rules validated after merge (orchestrator post-validation)

After running `markdownlint <file>`, the orchestrator handles violations of the following rules first.

- **MD001** (heading-increment): Heading hierarchy increases by one level at a time.
- **MD029** (ol-prefix): Ordered-list numbering rule.
- **MD024** (no-duplicate-heading): Duplicate heading.
- **MD042** (no-empty-links): Link validity.
- **MD025** (single-h1): Exactly one H1.
- **MD041** (first-line-h1): First line of document is H1.
- Table format, blank lines, whitespace cleanup, and other structure / format fixes (do not change source text or meaning).

## Update rules

- When modifying this file, 4.7 of `SKILL.md` keeps a reference only (no rule re-embedding).
- When adding or removing a rule, state its "avoidance phase (during conversion / after merge)" classification.
- Update history is managed via git history (no in-file changelog section).

### Feedback update procedure (for the orchestrator)

Merge policy when reflecting `markdownlint` results into this file.

1. **Consider existing data first**: first Read the current rule list, classification, and descriptions, then draft the change.
2. **No duplication**: do not re-register an already-registered `MD###`. If additional description is needed, add only within a range that does not overturn the meaning of existing sentences.
3. **New rules**: append to the end of the relevant section (avoidance / validation) in the same format.
4. **Major changes (move to the consultation section at the bottom)**: if any of the following apply, do not modify the body section, and append in the format `- [YYYY-MM-DD] <input_file>: <observation> / <suggestion>` to the `## User consultation required` section at the bottom of the file and await the user's decision.
   - Three or more new rules appear at once
   - An existing rule's classification (avoidance ↔ validation) must be changed
   - An interpretation conflicting with the existing description is needed
   - The project-wide lint policy (`.markdownlint.json`) and this file diverge
5. Do not mix direct body modification and consultation-section append **in the same run** (to avoid confusion in change tracking).

## User consultation required

- [2026-04-09] UR_A/C/D/E/F (83 PDFs): 5 new rules observed in this run — exceeding the threshold of 3, record in the consultation section instead of modifying the body directly.
  - **MD007** (ul-indent): Observed case — in ur-a2rev5, placed a bullet list three spaces indented below the paragraph (`(1) For strength...`). User fix: remove indentation. Suggestion: to the "avoidance during conversion" section `- **MD007** (ul-indent): if the list's parent is not a list, use zero-space indentation for bullets. Bullets below a paragraph start without leading spaces.`
  - **MD026** (no-trailing-punctuation): Observed case — period at the end of a heading in ur-d7rev3, ur-f37del-1. Suggestion: to the "avoidance during conversion" section `- **MD026** (no-trailing-punctuation): remove sentence-final punctuation (`.`, `;`, `:`, `!`, `?`) from headings. Write heading lines without a period since they are not prose sentences.`
  - **MD030** (list-marker-space): Observed case — UR-E26 line 403 `-  ` (two spaces). Suggestion: to the "avoidance during conversion" section `- **MD030** (list-marker-space): exactly one space after a list marker (`- item`, `1. item`). No tabs or double spaces.`
  - **MD034** (no-bare-urls): Observed case — `https://us-cert.cisa.gov/...` in UR-E26 line 695. Suggestion: to the "after-merge validation" section `- **MD034** (no-bare-urls): wrap source URLs in `<...>` angle brackets. The orchestrator can handle this in bulk with `sed` after merge.`
  - **MD056** (table-column-count): Observed case — large table (including a nested table inside a cell) in UR-E10. Suggestion: when `|` appears inside a cell, the parser misreads it as a column separator. Hard to avoid (a markdown limitation). Recommended: disable `.markdownlint.json` MD056 at the file level. To the "after-merge validation" section `- **MD056** (table-column-count): allow disabling when a nested table contains pipe characters in cells (prioritize source-structure restoration).`

- [2026-04-09] Typo auto-fix policy issue: The default dictionary `language_tool_python` + `en-US` treats British spellings in IACS ship technical documents (draught/moulded/manoeuvring/centre/fibre/vapour/recognise/analyse/categorise, etc.) and compound technical terms (twistlock/weatherdeck/downflooding/pumproom/portlights/longitudinals) as **single-candidate TYPOS**, so auto-fix destroys content (e.g., `FPSOs → FPS Os`, `Shell → She'll`, `markdownlint-disable → markdown lint-disable`). Suggestion:
  - ✅ **Applied** (2026-04-10): exclude the `BRITISH_ENGLISH_DETECTOR` rule from the SKILL.md typo auto-fix scope. British spellings are preserved as in the source.
  - In this run, 1,386 items were stored in `reports/pdf2md_typo_report_2026-04-09.json` as report-only.
