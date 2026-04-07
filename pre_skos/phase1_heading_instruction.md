# Phase 1: HEADING Controlled Vocabulary Work Instruction

> **Pre-SKOS Phase**: This is a preparatory step for building SKOS `skos:broader` / `skos:related` hierarchical and associative relationships in Phase 2. Phase 1 focuses on source-faithful heading extraction and flat-table cataloguing; formal SKOS semantic relations (document hierarchy as `skos:broader`) are constructed in the subsequent phase.

> **Scope**: Extract all section headings (titles) from maritime regulatory documents at every structural level — Part, Chapter, Section, Article, Regulation, Annex, Paragraph, and any other numbered or titled subdivision.
> The goal is to capture **the complete document structure vocabulary** as controlled terms, enabling document navigation, cross-document structural alignment, and future SKOS/OWL modelling.
> Hierarchical relationships between headings (parent-child nesting) are deferred to Phase 2.
> **Work Procedure**: Read and process all source texts sequentially.
> **Work Preparation**: When the user requests a review, divide the target material into segments of approximately 100K tokens and process them sequentially.
---

## 0. Prerequisites — LLM-Script Cooperative Extraction

A preparatory step where the LLM and script cooperate in alternating passes to extract and validate heading data. Each instruction (TRUE_DEF, APPLICABILITY, CONTROLLED_TERM, HEADING) is executed independently.

> **Design principle**: LLM excels at semantic understanding (recognising heading intent, resolving ambiguity, handling non-standard structures). Script excels at mechanical completeness (pattern matching every line, format consistency, coverage checking). The procedure alternates between the two so each compensates for the other's blind spots.

### Pass 1 — LLM Initial Extraction

1. **Document review** — The LLM reads the target document and identifies:
   - The source family (IACS / IMO / KR / EU) and document type
   - The structural hierarchy pattern (e.g., Part > Chapter > Section > Article > Paragraph)
   - Any non-standard structural features (e.g., unnumbered headings, mixed numbering schemes, Annex-first structure like MARPOL)
2. **LLM heading extraction** — The LLM extracts all headings from the entire document, assigning a tentative `Heading_Level` and `Heading_Number` to each. Output: `results/temp/heading_extraction_llm_{Source_Doc}.tsv` with columns: `Line_No | Heading_Level | Heading_Number | Heading_Text | LLM_Note`.
   - The LLM uses its semantic understanding to handle ambiguous cases: unnumbered headings, headings that look like table headers, bold text that may or may not be structural.
   - The LLM also drafts an initial heading grammar describing the document's hierarchy pattern.

### Pass 2 — Script Formal Verification

3. **Script pattern scan** — A verification script runs independently against the source document, using:
   - (a) **Regex-based heading detection** — Known heading signatures (numbering schemes, keyword prefixes like `Part`, `Chapter`, `Reg.`, `Art.`, formatting cues) applied to every line of the document.
   - (b) **The LLM's draft heading grammar** (from Step 2) — Loaded as additional patterns to catch document-specific structures the generic patterns might miss.
   - Output: `results/temp/heading_extraction_script_{Source_Doc}.tsv` with columns: `Line_No | Heading_Level | Heading_Number | Heading_Text | Confidence`. `Confidence` values: `high` (exact pattern match), `medium` (partial/ambiguous), `low` (heuristic only).

4. **Cross-comparison (script)** — The script compares the LLM extraction (Step 2) against the script extraction (Step 3) and produces a **discrepancy report** (`results/temp/heading_discrepancy_{Source_Doc}.tsv`):

   | Discrepancy Type | Meaning | Action |
   |:---|:---|:---|
   | `LLM_only` | LLM found it, script did not | Script may have missed a non-standard heading — **LLM likely correct**, verify in Pass 3 |
   | `Script_only` | Script found it, LLM did not | LLM may have missed a heading — **high-priority review** in Pass 3 |
   | `Level_mismatch` | Both found it, but assigned different `Heading_Level` | Resolve in Pass 3 based on context |
   | `Number_mismatch` | Both found it, but `Heading_Number` differs | Typically a normalisation issue — resolve in Pass 3 |
   | `Agreed` | Both found it with same level and number | No action needed — **confirmed** |

### Pass 3 — LLM Discrepancy Resolution

5. **LLM review of discrepancies** — The LLM reviews the discrepancy report (Step 4), resolving each item:
   - `Script_only` items: Confirm as genuine headings (LLM missed) or reject as false positives (table headers, captions, etc.)
   - `LLM_only` items: Confirm as genuine headings (script missed due to non-standard format) or withdraw if incorrect
   - `Level_mismatch` / `Number_mismatch`: Determine the correct value based on document context
   - Output: a **validated heading list** (`results/temp/heading_validated_{Source_Doc}.tsv`)

6. **Grammar finalisation** — The LLM finalises the heading grammar based on the validated heading list, incorporating any structural patterns newly discovered during discrepancy resolution.
   - Output: `results/temp/grammars/heading_grammar_{Source_Doc_Type}_v{NN}.md`

### Pass 4 — Script Final Validation

7. **Completeness check (script)** — The script runs a final pass against the source document using the finalised heading grammar:
   - (a) **Coverage**: Every line in the document is classified as either "heading (extracted)" or "non-heading". Any unclassified line matching heading patterns is flagged as an **omission candidate**.
   - (b) **Grammar conformance**: The validated heading list is checked against the heading grammar — any `Heading_Level` sequence that violates the grammar's hierarchy rules is flagged.
   - (c) **Format consistency**: Heading_Number formats, prefLabel normalisation, and Source_Locator coherence are machine-checked.
   - Output: `results/temp/heading_final_check_{Source_Doc}.tsv` (flagged items only)

8. **LLM final review** — The LLM reviews any items flagged in Step 7. If new headings are discovered, they are added and the grammar is updated (version increment). If no issues remain, the validated heading list is promoted to the extraction result.

### 0.1 Iteration and Convergence

The Pass 2-3 cycle (script verify → LLM resolve) may be repeated if Pass 4 reveals significant new issues. In practice:

| Scenario | Expected Iterations |
|:---|:---|
| Standard document structure (matches existing grammar) | 1 pass (Pass 1-4 straight through) |
| Minor variations from existing grammar | 1-2 passes |
| First document of a new Source_Doc_Type (no grammar yet) | 2-3 passes |
| Highly non-standard structure | 3+ passes (flag for user review) |

**Convergence criterion**: Pass 4 produces zero `Error`-severity flags and fewer than 3 `Warning`-severity flags. If not met after 3 iterations, escalate to the user with the remaining discrepancy report.

### 0.2 Heading Grammar as Reusable Validator

The heading grammar produced through the cooperative process serves as a **reusable validation asset**:

- **Within the current extraction run**: During Verification (Section 8), the heading grammar is applied to the final result TSV to check that every record's `Heading_Level` conforms to the grammar's hierarchy rules. Violations are flagged as **Warning** in the verification log.
- **Across documents of the same Source_Doc_Type**: Once a heading grammar is validated for a given Source_Doc_Type (e.g., `UR`, `Convention`, `Rule`), it is loaded as a **pre-validator** for subsequent documents. The script applies the existing grammar to the new document in Pass 2, flagging deviations that may indicate either (a) extraction errors or (b) a document with a non-standard structure requiring grammar extension.
- **Grammar versioning**: Each grammar file is named `heading_grammar_{Source_Doc_Type}_v{NN}.md` and stored in `results/temp/grammars/`. When a new document reveals a structural variation, the grammar is extended (not overwritten) and the version number is incremented.

| Grammar File | Description | Hierarchy |
|:---|:---|:---|
| `heading_grammar_UR_v01.md` | IACS UR heading hierarchy rules | Clause > Paragraph > Sub_Paragraph |
| `heading_grammar_Convention_v01.md` | IMO Convention heading hierarchy rules | Part > Chapter > Regulation > Paragraph > Sub_Paragraph |
| `heading_grammar_Mandatory_Code_v01.md` | IMO Mandatory Code heading hierarchy rules | Part > Chapter > Section > Paragraph |
| `heading_grammar_Rule_v01.md` | KR Rule heading hierarchy rules | Part > Chapter > Section > Article > Paragraph |
| `heading_grammar_Directive_v01.md` | EU Directive heading hierarchy rules | Title > Chapter > Section > Article > Paragraph > Point |

### 0.3 Intermediate File Summary

| File | Producer | Description |
|:---|:---|:---|
| `heading_extraction_llm_{Source_Doc}.tsv` | LLM (Pass 1) | LLM initial heading extraction |
| `heading_extraction_script_{Source_Doc}.tsv` | Script (Pass 2) | Script independent heading detection |
| `heading_discrepancy_{Source_Doc}.tsv` | Script (Pass 2) | Cross-comparison discrepancy report |
| `heading_validated_{Source_Doc}.tsv` | LLM (Pass 3) | Validated heading list after discrepancy resolution |
| `heading_grammar_{Source_Doc_Type}_v{NN}.md` | LLM (Pass 3) | Generalised heading grammar |
| `heading_final_check_{Source_Doc}.tsv` | Script (Pass 4) | Final validation flags |

---

## 1. Admission Rule

| Condition | Include | Exclude |
|:---|:---|:---|
| Source location | **Entire document** — all sections including Definitions, Application/Scope, body text, normative annexes, and informative annexes | None (HEADING extraction covers all document sections) |
| Record type | **HEADING** only | TRUE_DEF, APPLICABILITY, CONTROLLED_TERM |
| What qualifies | Numbered or titled subdivisions that organise document structure: Part titles, Chapter titles, Section titles, Article titles, Regulation titles, Annex titles, numbered paragraph headings | Inline bold text that is emphasis (not a structural heading), table headers, figure captions, footnote markers |
| Source | IMO Conventions/Codes/Resolutions/Circulars, IACS UR/UI/Rec/PR, KR Rules/Technical Rules/Guidance/Interpretations, EU Directives/Regulations/Decisions (active instruments) | Withdrawn-before-effective documents |
| Language | English only (data cells) | Replace Korean text with English |

### 1.1 One-Line Decision

Is the text a structural subdivision heading (numbered or titled) that organises the document? — **Yes -> adopt**, No -> skip.

### 1.2 Heading vs Non-Heading Discrimination

| Heading (adopt) | Not a heading (skip) |
|:---|:---|
| Has a section number (e.g., `1.2.3`, `Reg. 13`) | Inline bold for emphasis within a paragraph |
| Is a titled subdivision (e.g., `Part A — General`) | Table column header |
| Appears as a standalone line preceding body text | Figure/table caption (e.g., `Table 3 — Minimum thickness`) |
| Matches document's structural hierarchy pattern | Footnote or endnote marker |
| Annex titles (e.g., `Annex I — Intact Stability`) | List item labels (e.g., `.1`, `.2` within a paragraph) |

---

## 2. Core Principles

### 2.1 Source-Faithful Extraction

- **Extract heading text verbatim** as it appears in the source document (`Source_Form@en`).
- **Normalise to a preferred label** (`prefLabel@en`) per the Label Policy (Section 5).
- Both forms are preserved.

### 2.2 Complete Coverage

- Extract headings at **every structural level** of the document. Do not skip lower-level headings.
- Unlike CONTROLLED_TERM (which skips Definitions/Scope sections), HEADING extraction covers the **entire document**.

### 2.3 Flat Extraction in Phase 1

- **Do not encode parent-child relationships** in Phase 1. Each heading is a flat record.
- Hierarchical nesting (e.g., `Part 3 > Chapter 1 > Section 1`) will be constructed as `skos:broader` in Phase 2.
- The `Heading_Level` and `Heading_Number` fields provide sufficient information to reconstruct hierarchy in Phase 2.

### 2.4 Source-Specific Registration

- Even when different documents use the same heading text (e.g., "Application", "Definitions"), register each as a separate record with its own Concept_ID.
- Cross-document heading alignment is performed in Phase 2.

---

## 3. Target Schema

```
Concept_ID | Record_Type | Scheme | Source_Doc_Type | Heading_Level | Heading_Number | prefLabel@en | altLabel@en | Source_Form@en | Source_Doc | Source_Locator | Editor_Note
```

### 3.1 Column Definitions with Obligation

| # | Column | Obligation | SKOS/DC Mapping | Data Type | Cardinality | Rule |
|:---:|:---|:---:|:---|:---|:---|:---|
| 1 | **Concept_ID** | **Required** | URI fragment | ID | single | Format: `{Scheme}_{SourceKey}_HD_{SeqNo}`. See Section 3.5 for source-family patterns. **Once assigned, never renumbered; gaps permitted.** Normalisation: remove dots/parentheses, replace `/` with `_`. |
| 2 | **Record_Type** | **Required** | `dct:type` | enum | single | Fixed to `HEADING`. Discriminator for coexistence with TRUE_DEF, APPLICABILITY, and CONTROLLED_TERM records. |
| 3 | **Scheme** | **Required** | `skos:inScheme` | enum | single | One of: `IMO`, `IACS`, `KR`, `EU`. Identifies the source authority. |
| 4 | **Source_Doc_Type** | **Required** | `dct:type` (secondary) | enum | single | Classifies the document genre. Values from closed list (Section 3.2a). Shared with TRUE_DEF, APPLICABILITY, and CONTROLLED_TERM instructions. |
| 5 | **Heading_Level** | **Required** | `mreg:headingLevel` | enum | single | Structural level of the heading within the document hierarchy. Values from Section 3.3. |
| 6 | **Heading_Number** | **Conditional** | `mreg:headingNumber` | text | single | Original numbering as it appears in the source document. E.g., `2.1.3`, `Reg. 13`, `Art. 5`, `Part A`. **Fill if the heading has a number or letter designation; leave blank for unnumbered headings.** |
| 7 | **prefLabel@en** | **Required** | `skos:prefLabel` | text | single | Normalised heading text. Sentence case. English only. Excludes the heading number (number is in `Heading_Number`). **The singular-default rule (TRUE_DEF/CONTROLLED_TERM) does not apply to headings** — preserve the original number form (e.g., "General provisions" stays plural if the source uses plural). |
| 8 | **altLabel@en** | Optional | `skos:altLabel` | text-multi | multi | Abbreviated or alternate form of the heading, if commonly used. E.g., `"Ch. II-1"` for `"Chapter II-1"`. Semicolon-separated. |
| 9 | **Source_Form@en** | **Required** | `mreg:sourceForm` | text | single | Heading text as it appears verbatim in the source document, including original casing. Excludes the heading number. |
| 10 | **Source_Doc** | **Required** | `dcterms:source` | text | single | Source document identifier. See Section 3.6 for format per source family. |
| 11 | **Source_Locator** | **Required** | (locator) | text | single | Location of the heading within the document. For numbered headings, this is typically the heading number itself or the section path. E.g., `Pt.3 Ch.1 Sec.1`, `Reg. 13`, `Art. 2`. **For unnumbered headings**, use the nearest parent heading's locator followed by the heading text in brackets. E.g., `Pt.3 Ch.1 [Foreword]`. |
| 12 | **Editor_Note** | Optional | `skos:editorialNote` | text | single | Extraction rationale, QA comments, ambiguity flags. For headings with no body text (empty sections): `[empty section]`. For headings whose level is ambiguous: `[level uncertain]`. |

#### Obligation Legend

| Obligation | Meaning |
|:---|:---|
| **Required** | Must always be filled. Record is invalid without it. |
| **Conditional** | Must be filled if the source text contains the relevant information. Leave blank if not stated. |
| **Optional** | Fill if available and useful. Record remains valid without it. |

### 3.2 Interoperability with Other Record Types

| Aspect | HEADING | TRUE_DEF / APPLICABILITY / CONTROLLED_TERM | Resolution |
|:---|:---|:---|:---|
| **Discriminator** | `Record_Type` = `HEADING` | `Record_Type` = `TRUE_DEF` / `APPLICABILITY` / `CONTROLLED_TERM` | `Record_Type` is the single discriminator |
| **Source location** | Entire document (all sections) | Section-specific (see each instruction) | HEADING overlaps all three; no conflict because Record_Type differs |
| **Scheme** | `IMO`, `IACS`, `KR`, `EU` | Same | All four Scheme values shared |
| **Source_Doc_Type** | Same closed list | Same closed list | Shared across all four instructions |
| **HEADING-only columns** | `Heading_Level`, `Heading_Number` filled | Left blank | Validation must be conditional on Record_Type |
| **Other instruction columns** | Left blank (Definition, Term_Category, Target_Entity, etc.) | Filled per respective instruction | Validation must be conditional on Record_Type |

> **Overlap clarification**: A section heading such as "Definitions" will be extracted as a HEADING record (structural element) and will also serve as the source location for TRUE_DEF records extracted from that section. Similarly, "Application" may appear as both a HEADING record and a source section for APPLICABILITY records. These are **not duplicates** — the HEADING record captures the document structural element; the other record types capture the semantic content within that section. Same `Source_Doc` and overlapping `Source_Locator` values across record types are expected and valid.

### 3.2a Source_Doc_Type Controlled Values

| Value | Description | Typical Source Family |
|:---|:---|:---|
| `Convention` | International convention (SOLAS, MARPOL, Load Line, STCW, etc.) | IMO |
| `Mandatory_Code` | Mandatory codes under conventions (IGC, IBC, ISM, ISPS, etc.) | IMO |
| `Recommendatory_Code` | Recommendatory codes and guidelines | IMO |
| `Resolution` | IMO Assembly or MSC/MEPC resolutions | IMO |
| `Circular` | MSC/MEPC circulars and unified interpretations | IMO |
| `UR` | Unified Requirements | IACS |
| `UI` | Unified Interpretations | IACS |
| `Rec` | Recommendations | IACS |
| `PR` | Procedural Requirements | IACS |
| `Rule` | Classification rules (mandatory requirements) | KR |
| `Guidance` | Technical guidance (recommended practice) | KR |
| `Interpretation` | Official interpretation of rules | KR |
| `Technical_Rule` | Technical rules for specific ship types or systems | KR |
| `Directive` | EU directive requiring national transposition | EU |
| `Regulation_EU` | Directly binding EU regulation | EU |
| `Decision` | EU decision binding on specific addressees | EU |

> This closed list is shared across TRUE_DEF, APPLICABILITY, CONTROLLED_TERM, and HEADING instructions.

### 3.3 Heading_Level Controlled Values

| Value | Description | Typical Source |
|:---|:---|:---|
| `Part` | Top-level division (Part, Volume) | KR Rules (`Pt.3`), SOLAS (`Part A/B/C`) |
| `Title` | Title-level division (above Chapter in EU legislation) | EU Directives (`Title III`), EU Regulations |
| `Chapter` | Chapter-level division | KR Rules (`Ch.1`), SOLAS (`Chapter II-1`) |
| `Section` | Section-level division | KR Rules (`Sec.1`), IMO Codes |
| `Article` | Article within a section | KR Rules (`101`, `201`), EU Directives (`Art. 2`) |
| `Regulation` | Regulation within a chapter (IMO convention structure) | SOLAS (`Reg. 3`), MARPOL (`Reg. 13`) |
| `Clause` | Top-level numbered subdivision within IACS UR/UI/Rec/PR documents (e.g., `1. General`, `2. Application`) | IACS UR (`1.`, `2.`, `3.`) |
| `Annex` | Annex | All sources (`Annex I`) |
| `Appendix` | Appendix (distinguished from Annex where the source uses both) | IMO Codes, IACS UR |
| `Paragraph` | Numbered paragraph within an article/regulation/clause | All sources (`1.2.3`, `3.8.1`) |
| `Sub_Paragraph` | Sub-paragraph (lowest level with a heading) | All sources (`.1`, `.2` with heading text) |
| `Point` | Lettered or numbered point within a paragraph (EU legislation) | EU Directives (`(a)`, `(b)`, `(i)`, `(ii)`) |
| `Schedule` | Schedule (EU legislation, some IMO instruments) | EU Directives, IMO Conventions |

> **Normalisation notes:**
> - `Appendix` is distinguished from `Annex` when the source document uses both terms. If the source uses only one, follow the source terminology.
> - The same numbering format (e.g., `1.`, `2.`) may correspond to different `Heading_Level` values depending on the source family. Always determine `Heading_Level` based on the document's structural hierarchy, not solely on the numbering format.
> - EU `Recital` headings (preamble items such as `(1) Whereas...`) are **excluded** from HEADING extraction. Recitals are motivational preamble text, not structural body headings.
> - If a heading level does not match any value above, use the closest match and flag `[level uncertain: original={description}]` in Editor_Note.

### 3.4 Source-Family Heading Structure Reference

> This section provides reference patterns for each source family to assist consistent `Heading_Level` assignment. These are typical structures; individual documents may vary.

#### IACS UR/UI/Rec/PR

| Document Level | Heading_Level | Example |
|:---|:---|:---|
| Top-level numbered clause | `Clause` | `1. General` |
| Sub-section | `Paragraph` | `1.1 Scope` |
| Sub-sub-section | `Sub_Paragraph` | `1.1.1 Application` |
| Annex | `Annex` | `Annex 1 — Test Methods` |
| Appendix | `Appendix` | `Appendix A — Calculation Examples` |

> IACS UI, Rec, and PR documents generally follow the same pattern as UR. Where an individual document has a simpler or different structure, assign the closest `Heading_Level` value and flag `[level uncertain]` in Editor_Note if needed.

#### IMO Conventions (SOLAS, MARPOL, ICLL, etc.)

| Document Level | Heading_Level | Example |
|:---|:---|:---|
| Part | `Part` | `Part A — General` |
| Chapter | `Chapter` | `Chapter II-1 — Construction` |
| Regulation | `Regulation` | `Regulation 3 — Definitions` |
| Paragraph within regulation | `Paragraph` | `3.1`, `3.2` |
| Sub-paragraph (titled) | `Sub_Paragraph` | `30.1 Rudder body` |
| Annex (MARPOL top-level) | `Annex` | `Annex I — Regulations for the Prevention of Pollution by Oil` |

> In MARPOL, `Annex` functions as the top-level structural division (analogous to Part), with `Regulation` headings nested within each Annex.

#### IMO Codes (ISM, ISPS, FSS, IGC, IBC, etc.)

| Document Level | Heading_Level | Example |
|:---|:---|:---|
| Part | `Part` | `Part A — Implementation` |
| Chapter | `Chapter` | `Chapter 7 — Fire detection and fire alarm systems` |
| Section | `Section` | `Section 7 — Shipboard Operations` |
| Paragraph | `Paragraph` | `7.1`, `7.2` |
| Annex | `Annex` | `Annex — Guidance on the ISM Code` |
| Appendix | `Appendix` | `Appendix — Test Procedures` |

> Some IMO Codes use both Chapter and Section levels; others use only one. Assign based on the individual Code's structure.

#### KR Rules/Guidance/Technical Rules

| Document Level | Heading_Level | Example |
|:---|:---|:---|
| Part | `Part` | `Pt.3 Hull Structures` |
| Chapter | `Chapter` | `Ch.1 General` |
| Section | `Section` | `Sec.1 General` |
| Article | `Article` | `101. Application` |
| Paragraph | `Paragraph` | `1.`, `2.` (within an article) |

> KR Guidance, Interpretation, and Technical Rule documents generally follow the Part > Chapter > Section > Article pattern. Where the structure differs, apply the closest mapping.

#### EU Directives/Regulations/Decisions

| Document Level | Heading_Level | Example |
|:---|:---|:---|
| Title | `Title` | `Title III — Safety Rules and Standards` |
| Chapter | `Chapter` | `Chapter I — General Provisions` |
| Section | `Section` | `Section 2 — Safety requirements` |
| Article | `Article` | `Article 2 — Definitions` |
| Paragraph within article | `Paragraph` | `(1)`, `(2)` |
| Point within paragraph | `Point` | `(a)`, `(b)`, `(i)`, `(ii)` |
| Annex | `Annex` | `Annex I — Safety requirements for new and existing passenger ships` |
| Schedule | `Schedule` | `Schedule 1` |

> EU Recitals (preamble items) are **excluded** — see Section 3.3 normalisation notes.

### 3.5 Concept_ID / URI Design

- **General Pattern**: `{Scheme}_{SourceKey}_HD_{SeqNo}`
- `Scheme`: Must match column 3 value
- `SourceKey`: Normalised source identifier (shared rules with other instructions)
- `_HD_`: Fixed infix distinguishing HEADING records
- `SeqNo`: Three-digit sequence number, local within that source unit

#### Source-Family Concept_ID Patterns

| Source Family | Scheme | Pattern | Examples |
|:---|:---|:---|:---|
| IACS UR | `IACS` | `IACS_{URKey}_HD_{SeqNo}` | `IACS_S11A_HD_001`, `IACS_Z10_1_HD_001` |
| IACS UI | `IACS` | `IACS_UI_SC123_HD_{SeqNo}` | `IACS_UI_SC123_HD_001` |
| IACS Rec | `IACS` | `IACS_REC_{RecNo}_HD_{SeqNo}` | `IACS_REC_87_HD_001` |
| IACS PR | `IACS` | `IACS_PR_{PRNo}_HD_{SeqNo}` | `IACS_PR_38_HD_001` |
| IMO Convention | `IMO` | `IMO_{ConvChapter}_HD_{SeqNo}` | `IMO_SOLAS_II_1_HD_001` |
| IMO Code | `IMO` | `IMO_{CodeAbbr}_HD_{SeqNo}` | `IMO_ISM_HD_001`, `IMO_FSS_HD_001` |
| IMO Resolution | `IMO` | `IMO_RES_{CommitteeNo}_HD_{SeqNo}` | `IMO_RES_MSC396_HD_001` |
| IMO Circular | `IMO` | `IMO_CIRC_{CommitteeNo}_HD_{SeqNo}` | `IMO_CIRC_MSC1040_HD_001` |
| KR Rule | `KR` | `KR_{PartChapter}_HD_{SeqNo}` | `KR_PT3_CH1_HD_001` |
| KR Guidance | `KR` | `KR_GD_{PartChapter}_HD_{SeqNo}` | `KR_GD_PT1_HD_001` |
| KR Interpretation | `KR` | `KR_INT_{PartChapter}_HD_{SeqNo}` | `KR_INT_PT3_CH1_HD_001` |
| KR Technical_Rule | `KR` | `KR_TR_{Key}_HD_{SeqNo}` | `KR_TR_FRP_PT2_HD_001` |
| EU Directive | `EU` | `EU_DIR_{Year}_{No}_HD_{SeqNo}` | `EU_DIR_2009_45_HD_001` |
| EU Regulation | `EU` | `EU_REG_{Year}_{No}_HD_{SeqNo}` | `EU_REG_2015_757_HD_001` |
| EU Decision | `EU` | `EU_DEC_{Year}_{No}_HD_{SeqNo}` | `EU_DEC_2012_757_HD_001` |

#### SourceKey Normalisation Rules

> **Steps 1-5** are the shared core rules, identical across all four instructions (TRUE_DEF / APPLICABILITY / CONTROLLED_TERM / HEADING). **Steps 6-7** handle source-family-specific abbreviation patterns.

| Step | Rule | Scope | Example |
|:---:|:---|:---|:---|
| 1 | Replace dots, parentheses, and commas with underscores (or remove if at word boundary) | Shared | `Z10.1` -> `Z10_1`; `Pt.3 Ch.1` -> `Pt3_Ch1` |
| 2 | Replace `/` and `-` with `_` | Shared | `II-1/3-8` -> `II_1_3_8` |
| 3 | Collapse consecutive underscores | Shared | `II__1` -> `II_1` |
| 4 | Use UPPERCASE | Shared | `Pt3_Ch1` -> `PT3_CH1` |
| 5 | Remove document-type prefix (already in pattern) | Shared | `UR S11A` -> `S11A` |
| 6 | IMO Codes: standard abbreviation | Shared | `FSS Code` -> `FSS`, `ISM Code` -> `ISM` |
| 7 | EU: year + number | Shared | `Directive 2009/45/EC` -> `DIR_2009_45` |

- Base URI pattern: `https://{domain}/maritime-cv/{Concept_ID}` — `{Concept_ID}` is the full value including the Scheme prefix
- In Phase 1, only the local ID (`Concept_ID`) is finalised.

### 3.6 Source Citation Formats

| Category | Source_Doc | Source_Locator example |
|:---|:---|:---|
| IACS UR | `UR S11A` | `1.1`, `Annex 1` |
| IACS UI | `UI SC123` | `1.1` |
| IACS Rec | `Rec 87` | `2.3` |
| IACS PR | `PR 38` | `3.1` |
| SOLAS | `SOLAS II-1` | `Reg. 3`, `Part B` |
| IMO Code | `ISM Code` | `Section 7`, `7.1` |
| IMO Resolution | `IMO Res. MSC.370(93)` | `Part A` |
| KR Rules | `KR Rules Pt.3` | `Ch.1 Sec.1 101` |
| EU Directive | `Directive 2009/45/EC` | `Art. 2`, `Annex I` |
| EU Regulation | `Regulation (EU) 2015/757` | `Art. 3`, `Chapter II` |

---

## 4. Extraction Patterns

### 4.1 Heading Identification Patterns

| # | Pattern | Trigger | Target Columns |
|:---:|:---|:---|:---|
| HD1 | Numbered section heading | Standalone line with number prefix + title text (e.g., `1.2.3 Title`, `Reg. 13 Title`) | Heading_Number, prefLabel, Heading_Level |
| HD2 | Named structural division | `Part A —`, `Chapter II-1 —`, `Section 7 —`, `Annex I —` | Heading_Level = corresponding level, prefLabel |
| HD3 | Article heading | `Article N — Title` or `Art. N Title` (EU), `101. Title` (KR) | Heading_Level = Article, Heading_Number |
| HD4 | Regulation heading | `Regulation N — Title` (IMO conventions) | Heading_Level = Regulation, Heading_Number |
| HD5 | Unnumbered structural heading | Standalone bold or uppercase line that introduces a new section without a number | prefLabel (flag `[unnumbered]` in Editor_Note) |
| HD6 | Annex/Appendix heading | `Annex N`, `Appendix N`, with or without title | Heading_Level = Annex |
| HD7 | Schedule heading | `Schedule N` (EU, some IMO) | Heading_Level = Schedule |

### 4.2 Non-Heading Exclusion Patterns

| # | Pattern | Action |
|:---:|:---|:---|
| EX1 | Table header row | Skip — not a structural heading |
| EX2 | Figure/table caption | Skip — `Table 3 — Minimum thickness` is a caption, not a heading |
| EX3 | Inline bold emphasis | Skip — bold text within a paragraph body |
| EX4 | List item numbering | Skip — `.1`, `.2` within a paragraph without heading-level significance |
| EX5 | Footnote/endnote marker | Skip |

---

## 5. Label Policy

| Label type | Purpose | Example |
|:---|:---|:---|
| `skos:prefLabel` | Normalised heading text. **One per language.** | "Structural fire protection"@en |
| `mreg:sourceForm` | Verbatim heading text from source (provenance) | "Structural Fire Protection"@en |

### Naming Conventions

| Rule | Content |
|:---|:---|
| Case | Sentence case (lowercase unless proper noun) |
| Number exclusion | **Exclude the heading number from prefLabel and Source_Form.** The number is recorded in `Heading_Number`. E.g., source `"Regulation 13 — Structural fire protection"` -> prefLabel = `"Structural fire protection"`, Heading_Number = `Reg. 13` |
| Dash/colon removal | Remove structural separators (`—`, `:`, `-`) between number and title |
| Trimming | Remove leading/trailing whitespace |
| Proper nouns | Preserve capitalisation for proper nouns (e.g., `"MARPOL"`, `"IMO"`) |

---

## 6. Editorial Rules (Phase 1 Summary)

| Rule | Content |
|:---|:---|
| Language | English only (data cells). Korean permitted only in internal notes |
| Spelling | British English (normalising, vapour, centre, programme). **TSV column headers use `@en` for simplicity. When converting to RDF, all English-language literals shall carry the `@en-GB` tag (BCP 47 compliant).** |
| Source_Form | Verbatim from source, excluding heading number |
| Heading_Number | Preserve original numbering format from source (e.g., `Reg. 13`, `1.2.3`, `Art. 5`) |
| Source citation | Separate Source_Doc and Source_Locator. Do not use special character symbols |
| Empty cells | Leave blank if information not present. Do not default or infer |
| Deduplication | **Phase 1 rule: register every source-document occurrence as a separate record.** If the same heading text (e.g., "Application") appears in multiple documents of the same Scheme, each gets its own record. Tag `[same_scheme_dup: {other Concept_ID}]` in Editor_Note for Phase 2 consolidation. **Cross-Scheme**: Always register separately; tag `[equivalent: {Scheme}_{Concept_ID}]` in Editor_Note for Phase 2 alignment |

---

## 7. Procedure

```
Step 1   Identify the source family (IACS / IMO / KR / EU) and document type
Step 2   Run LLM-Script Cooperative Extraction (Section 0):
         Pass 1  LLM reads document, extracts all headings, drafts grammar
         Pass 2  Script independently scans, cross-compares with LLM result
         Pass 3  LLM resolves discrepancies, finalises grammar
         Pass 4  Script runs final validation; LLM reviews remaining flags
         (Repeat Pass 2-3 if needed — see Section 0.1 convergence criteria)
Step 3   From the validated heading list (Section 0, Pass 3 output),
         confirm each heading against Identification Patterns (HD1-HD7)
         and Exclusion Patterns (EX1-EX5)
         Note: the ENTIRE document is in scope, including Definitions and
         Application/Scope sections (unlike CONTROLLED_TERM)
Step 4   Confirm Heading_Level per Section 3.3, using the Source-Family
         Heading Structure Reference (Section 3.4) and the finalised
         heading grammar as guides
Step 5   Record Heading_Number (verbatim from source)
Step 6   Assign Concept_ID per Section 3.5 rules
         Set Record_Type = HEADING
         Set Scheme per source family
         Set Source_Doc_Type per document genre
Step 7   Normalise prefLabel per Label Policy (Section 5)
         Record Source_Form@en (verbatim, excluding number)
         Record altLabel@en if an abbreviated form exists
Step 8   Record Source_Doc / Source_Locator per Section 3.6
Step 9   Verify (Section 8) — including heading grammar validation pass
```

---

## 8. Verification

### 8.1 3-Pass Review

| Pass | Focus | Check items |
|:---|:---|:---|
| **Structural** | Table integrity | Column count consistency (12 columns), no duplicate Concept_ID, valid enum values (Scheme, Source_Doc_Type, Heading_Level), `_HD_` infix present, Record_Type = `HEADING` |
| **Semantic** | Content correctness | prefLabel = normalised heading text (no number prefix), Source_Form = verbatim (no number prefix), Heading_Level consistent with source document structure, Heading_Number matches source, no non-heading items included |
| **Grammar** | Heading grammar validation | Apply the heading grammar (Section 0.2) for the document's Source_Doc_Type against the result TSV. Verify that every record's `Heading_Level` conforms to the grammar's hierarchy rules (e.g., a `Paragraph` must not appear outside a parent `Clause`/`Regulation`/`Article` context). Flag violations as **Warning**. If no grammar exists yet for this Source_Doc_Type, skip this pass and note `[grammar: not yet available]` in the log |

### 8.2 Cross-Check Rules

| Rule | Check | Severity |
|:---|:---|:---|
| Required fields | Concept_ID, Record_Type, Scheme, Source_Doc_Type, Heading_Level, prefLabel, Source_Form, Source_Doc, Source_Locator must be filled | **Error** |
| Record_Type value | Must be `HEADING` | **Error** |
| Scheme value | Must be one of `IMO`, `IACS`, `KR`, `EU` | **Error** |
| Source_Doc_Type value | Must be from closed list (Section 3.2a) | **Error** |
| Concept_ID format | Must match `{Scheme}_{SourceKey}_HD_{SeqNo}` pattern | **Error** |
| Concept_ID-Scheme coherence | Concept_ID prefix must match Scheme value | **Error** |
| Heading_Level validation | Must be from Section 3.3 list | **Error** |
| Heading grammar conformance | `Heading_Level` sequence must conform to the heading grammar for the document's Source_Doc_Type (Section 0.2). E.g., for `UR`: Clause > Paragraph > Sub_Paragraph. A `Sub_Paragraph` appearing before any `Clause` is a violation | **Warning** |
| No number in prefLabel | prefLabel must not start with a section number or regulation number | **Error** |
| Heading_Number conditional | If source heading has a number, Heading_Number must be filled | **Warning** |
| Record_Type-conditional validation | HEADING records must not contain TRUE_DEF-only, APPLICABILITY-only, or CONTROLLED_TERM-only columns | **Error** |
| Concept_ID global uniqueness | No duplicate Concept_ID across all Scheme values | **Error** |
| Source_Locator-Heading_Number coherence | Source_Locator should be consistent with or derivable from Heading_Number | **Warning** |
| Completeness check | For each source document, verify that the extracted heading count is plausible relative to the heading structure model (Section 0, Step 2c) or the document's table of contents (if available) | **Warning** |
| No Korean in English fields | prefLabel, Source_Form, and Editor_Note must not contain Korean characters | **Error** |

---

## 9. Output Specification

All final output files are saved to the **`results/`** subdirectory under the working directory from which the instruction is executed. Per-chunk intermediate files (partial TSV and log files produced during segmented processing) are saved to **`results/temp/`**. Both directories shall be created automatically if they do not exist. Each extraction run produces exactly **3 final files** in `results/`: one result file, one summary file, and one log file. Intermediate files in `results/temp/` are retained for traceability but are not considered deliverables.

### 9.1 File Naming Convention

| File | Name Pattern | Description |
|:---|:---|:---|
| **Result** | `phase1_heading_result.tsv` | Final extraction table in TSV format. Contains all extracted records conforming to the Target Schema (Section 3). One header row + data rows. UTF-8 with BOM. |
| **Summary** | `phase1_heading_summary.md` | Extraction summary report in Markdown format. |
| **Log** | `phase1_heading_log.md` | Processing log in Markdown format. |

### 9.2 Result File (`phase1_heading_result.tsv`)

- **Format**: TSV (Tab-Separated Values), UTF-8 with BOM
- **Header row**: Column names exactly as defined in Section 3.1, tab-delimited
- **Column order**: `Concept_ID	Record_Type	Scheme	Source_Doc_Type	Heading_Level	Heading_Number	prefLabel@en	altLabel@en	Source_Form@en	Source_Doc	Source_Locator	Editor_Note`
- **Empty cells**: Leave blank (no placeholder text such as "N/A" or "-")
- **Quoting**: Fields containing tabs, newlines, or double quotes must be enclosed in double quotes. Embedded double quotes are escaped as `""`
- **Sort order**: By `Source_Doc` (ascending), then by `Source_Locator` (document order)

### 9.3 Summary File (`phase1_heading_summary.md`)

```markdown
# Phase 1 HEADING Extraction Summary

## Run Info
- Date: {YYYY-MM-DD}
- Source documents processed: {count}
- Total headings extracted: {count}

## Headings by Scheme
| Scheme | Count |
|:---|---:|
| IMO | {n} |
| IACS | {n} |
| KR | {n} |
| EU | {n} |

## Headings by Source_Doc
| Source_Doc | Count |
|:---|---:|
| {doc} | {n} |
| ... | ... |

## Headings by Heading_Level
| Heading_Level | Count |
|:---|---:|
| Part | {n} |
| Chapter | {n} |
| Section | {n} |
| Article | {n} |
| Regulation | {n} |
| Rule | {n} |
| Annex | {n} |
| Paragraph | {n} |
| Sub_Paragraph | {n} |
| ... | ... |

## Quality Flags
- Unnumbered headings: {count}
- Level-uncertain headings: {count}
- Editor_Note flags: {count}

## Issues / Observations
- {free text: notable decisions, ambiguities, structural anomalies}
```

### 9.4 Log File (`phase1_heading_log.md`)

```markdown
# Phase 1 HEADING Processing Log

## {Source_Doc} — {Part/Chapter}
- **Segment**: {segment number} / {total segments}
- **Tokens (approx)**: {n}K
- **Headings extracted**: {count}
- **Heading_Level distribution**: Part={n}, Chapter={n}, Section={n}, ...
- **Decisions**:
  - {heading text}: Adopted / Excluded — {reason}
  - ...
- **Flags**:
  - {Concept_ID}: {flag description}
  - ...
```

### 9.5 Overwrite Rule

Each new extraction run **overwrites** the previous final output files in `results/` and all intermediate files in `results/temp/`. If incremental preservation is needed, the user must rename or archive prior files before initiating a new run.

---

## 10. Phase 1.1 — Validation Exception Management

When recurring comments are identified during iterative validation of Phase 1 outputs, they are escalated to Phase 1.1 for systematic resolution. Phase 1.1 is **not** an additional extraction phase — it is a QA exception layer.

**Full specification**: See [`phase1_1_validation_exception_guide.md`](phase1_1_validation_exception_guide.md) (shared across all four Phase 1 instructions).

**Escalation criteria (summary)**:
- Comment recurs 2+ times or across 2+ documents/records
- Issue blocks validator pass
- Current guide text is ambiguous — reviewers disagree on correct action
- Phase 1 / Phase 2 boundary is unclear

---

## 11. Phase 2 Preview (Reference Only — Outside the Scope of This Document)

| Item | Description |
|:---|:---|
| Heading hierarchy | Reconstruct parent-child nesting as `skos:broader` relationships |
| Cross-document alignment | Align structurally equivalent headings across documents (e.g., all "Definitions" sections) |
| `skos:Collection` mapping | Group headings into document-structure collections |
| Heading-to-content linking | Link headings to the TRUE_DEF / APPLICABILITY / CONTROLLED_TERM records extracted from their sections |
| OWL document ontology | Model document structure as OWL classes (Document > Part > Chapter > Section > ...) |

---

*Phase 1 scope: HEADING only, source-specific registration, flat extraction (no hierarchy), stable ID with `{Scheme}_..._HD_` pattern, Source_Doc_Type classification, Record_Type = HEADING as single discriminator. Output: 3 final files (result TSV + summary MD + log MD) in `results/`, intermediate chunk files in `results/temp/`. Schema: 12 columns.*
