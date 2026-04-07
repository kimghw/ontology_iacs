# Phase 1: TRUE_DEF Controlled Vocabulary Work Instruction

> **Pre-SKOS Phase**: This is a preparatory step for building SKOS `skos:broader` / `skos:related` hierarchical and associative relationships in Phase 2. Phase 1 focuses on source-faithful definition extraction and flat-table cataloguing; formal SKOS semantic relations are constructed in the subsequent phase.

> **Scope**: Extract and refine only the definitions directly confirmed in the Formal Definitions section (TRUE_DEF).
> Classification of DESCRIPTION, PARAPHRASE, Technical Terms, Abbreviation registry, and JSON/OWL conversion are deferred to Phase 2 and beyond.
> **Work Procedure**: : Read and process all source texts sequentially.
> **Work Preparation:** : When the user requests a review, divide the target material into segments of approximately 100K tokens and process them sequentially. 
---

## 0. Prerequisites

A preparatory step where the LLM and user jointly review the target document and extract baseline data. Each instruction (TRUE_DEF, APPLICABILITY, CONTROLLED_TERM) is executed independently.

1. **Document review** — Read the target document and identify term definition patterns (e.g., "means", bold formatting, definition lists).
2. **Extraction scoping** — Extract only term-related sentences from the Definitions section. Save extracted sentences to the intermediate directory (`results/temp/`).
3. **Pattern cataloguing** — Analyse the extracted sentences from Step 2 and compile a pattern catalogue (`results/temp/extraction_patterns_true_def.tsv`). Record recurring sentence structures (e.g., `"X means..."`, `"X is defined as..."`, `"For the purpose of this..."`, bold-formatted headwords followed by definition text). This catalogue serves two purposes: (a) the separation script can use the patterns to **auto-flag potential omissions** in the remainder, and (b) patterns can be reused for **cross-instruction classification checks** (e.g., detecting an APPLICABILITY-type sentence mistakenly included in TRUE_DEF extraction).
4. **Extraction separation** — Run a separation script against the source document and the extracted sentences in `results/temp/` to produce two outputs: (a) **extracted sentences** (matched) and (b) **non-extracted sentences** (unmatched remainder). The script also applies the pattern catalogue from Step 3 to flag remainder sentences that match known definition patterns as **omission candidates**. The LLM performs the initial extraction (Step 2); the separation and pattern matching are performed by script to ensure mechanical completeness.
5. **Extraction verification** — The LLM reviews the non-extracted sentences (unmatched remainder from Step 4), with priority on script-flagged omission candidates, to verify that no required definition sentences were missed. If omissions are found, add them to the extracted set, update the pattern catalogue if a new pattern is identified, and re-run the separation script.

---

## 1. Admission Rule

| Condition | Include | Exclude (Phase 2 backlog) |
|:---|:---|:---|
| Source location | Formal "Definitions" section (body text or normative Annex only when it contains explicit definitions or is expressly incorporated as definitional authority) | Body text, footnotes, informative annex |
| Record type | **TRUE_DEF** only | DESCRIPTION, PARAPHRASE |
| Source | IMO Conventions/Codes/Resolutions/Circulars, IACS UR/UI/Rec/PR, KR Rules/Technical Rules/Guidance/Interpretations, EU Directives/Regulations/Decisions (active instruments — see Source_Doc_Type enum in Section 3.6 for full list) | ISO/IEC pure delegation ("as defined in ISO X") |
| Document | Active documents only | Withdrawn-before-effective documents |
| Language | English only (data cells) | Replace Korean text with English |

**One-line decision**: Is the term explicitly defined in the Definitions section of the document? — **Yes → adopt**, No → backlog.

---

## 2. Core Principle: Source-Specific Concept

Even when IMO/IACS/KR/EU use the same headword, their definitions and scopes may differ.

- **In Phase 1, register each source as a separate concept.** Do not merge into a single common concept.
- Cross-source mapping (closeMatch/exactMatch) is performed in Phase 2.
- Even within the same document, if definitions differ by section, separate them into distinct concepts.

---

## 3. Target Schema

```
Concept_ID | Record_Type | Scheme | Source_Doc_Type | prefLabel@en | altLabel@en | Definition@en | Scope_Note@en | Example@en | Source_Doc | Source_Locator | Editor_Note
```

### 3.1 Column Definitions with Obligation

| # | Column | Obligation | SKOS Mapping | Data Type | Cardinality | Rule |
|:---:|:---|:---:|:---|:---|:---|:---|
| 1 | **Concept_ID** | **Required** | URI fragment | ID | single | Format: `{Scheme}_{SourceKey}_TD_{SeqNo}`. E.g., `IACS_S11A_TD_001`, `IMO_SOLAS_II_1_TD_012`, `KR_PT3_CH1_TD_005`. **Once assigned, a Concept_ID shall never be renumbered; gaps in sequence are permitted.** Dots, parentheses, and other special characters in identifiers shall be removed or replaced with underscores (`_`) for normalization (e.g., `Pt.3 Ch.1` → `Pt3_Ch1`). The `_TD_` infix distinguishes TRUE_DEF records from APPLICABILITY (`_APP_`) and CONTROLLED_TERM (`_CT_`) records. |
| 2 | **Record_Type** | **Required** | `dct:type` | enum | single | Fixed to `TRUE_DEF`. Discriminator so that TRUE_DEF and APPLICABILITY records can coexist in one sheet. |
| 3 | **Scheme** | **Required** | `skos:inScheme` | enum | single | One of `IMO`, `IACS`, `KR`, `EU`. Identifies the source authority. |
| 4 | **Source_Doc_Type** | **Required** | `dct:type` (secondary) | enum | single | Classifies the document genre. Values from closed list (Section 3.6). Shared with APPLICABILITY and CONTROLLED_TERM instructions. |
| 5 | **prefLabel@en** | **Required** | `skos:prefLabel` | text | single | One per language. Sentence case. Singular by default (exceptions: scantlings, bilges) |
| 6 | **altLabel@en** | Optional | `skos:altLabel` | text-multi | multi | Abbreviations, acronyms, legitimate variants. Semicolon-separated (`;`) |
| 7 | **Definition@en** | **Required** | `skos:definition` | text | single | Retain only the definitional core, verbatim, after separation of non-definitional adjuncts identified by the Separation Patterns (Section 4). No editing or paraphrasing |
| 8 | **Scope_Note@en** | Conditional | `skos:scopeNote` | text | single | Applicability scope, domain restrictions, exclusion statements (extracted from source). **Fill if the source definition contains scope-limiting or exclusion language. For APPLICABILITY records, this role is performed by `Applicability_Text@en` (see APPLICABILITY instruction).** |
| 9 | **Example@en** | Conditional | `skos:example` | text | single | "e.g., Type A, B, C" and other enumeration/example tails. If representing subtypes, flag with `[narrower candidate]` in Editor_Note. **Fill if the source contains example or enumeration language.** |
| 10 | **Source_Doc** | **Required** | `dcterms:source` | text | single | UR/IMO/KR/EU document identifier. E.g., `UR S11A`, `SOLAS II-1`, `KR Rules Pt.3`, `Directive 2009/45/EC` |
| 11 | **Source_Locator** | **Required** | (locator within dcterms:source) | text | single | Section/Table/Annex location. E.g., `1.2.1`, `Table 3`, `Annex II` |
| 12 | **Editor_Note** | Optional | `skos:editorialNote` | text | single | Extraction rationale, QA comments, Pattern flags, previous version history |

#### Obligation Legend

| Obligation | Meaning |
|:---|:---|
| **Required** | Must always be filled. Record is invalid without it. |
| **Conditional** | Must be filled if the source text contains the relevant information. Leave blank if not stated. |
| **Optional** | Fill if available and useful. Record remains valid without it. |

### 3.2 Interoperability with APPLICABILITY and CONTROLLED_TERM Records

When TRUE_DEF and APPLICABILITY records coexist in one sheet:

| Aspect | TRUE_DEF | APPLICABILITY | Resolution |
|:---|:---|:---|:---|
| **Discriminator** | `Record_Type` = `TRUE_DEF` | `Record_Type` = `APPLICABILITY` | `Record_Type` is the single discriminator field for both types |
| **Source_Doc_Type** | Present (Section 3.6) | Present (APPLICABILITY Section 3.6) | Both record types share the same Source_Doc_Type closed list |
| **Scope text** | `Scope_Note@en` (scope extracted from definition) | `Applicability_Text@en` (verbatim applicability statement, anchor field) | Both map to `skos:scopeNote` but serve different roles: Scope_Note captures scope embedded within a definition; Applicability_Text is the standalone anchor for structured decomposition |
| **Scheme** | `IMO`, `IACS`, `KR`, or `EU` | `IMO`, `IACS`, `KR`, or `EU` | Both record types share the same Scheme value set |
| **APPLICABILITY-only columns** | Left blank (Target_Entity, Ship_Type, etc.) | Filled per APPLICABILITY instruction | Validation must be conditional on Record_Type |

When TRUE_DEF and CONTROLLED_TERM records coexist:

| Aspect | TRUE_DEF | CONTROLLED_TERM | Resolution |
|:---|:---|:---|:---|
| **Discriminator** | `Record_Type` = `TRUE_DEF` | `Record_Type` = `CONTROLLED_TERM` | `Record_Type` is the single discriminator |
| **Definition** | `Definition@en` (verbatim formal definition) | `Definition_Context@en` (usage context, not formal definition) | TRUE_DEF definitions take precedence if a term has both |
| **Source location** | Formal Definitions section | Body text (normative requirements) | Non-overlapping source locations |
| **Scheme** | `IMO`, `IACS`, `KR`, or `EU` | `IMO`, `IACS`, `KR`, or `EU` | All four Scheme values shared |
| **CONTROLLED_TERM-only columns** | Left blank (Term_Category, Term_Subclass, etc.) | Filled per CONTROLLED_TERM instruction | Validation must be conditional on Record_Type |

### 3.3 Concept_ID/URI Design

- **General pattern**: `{Scheme}_{SourceKey}_TD_{SeqNo}`
  - `Scheme`: `IMO`, `IACS`, `KR`, or `EU`
  - `SourceKey`: Normalized source unit key (document-level)
  - `_TD_`: Fixed infix distinguishing TRUE_DEF records
  - `SeqNo`: Three-digit sequence number, local within that source unit

#### Examples by Source Family

| Source Family | Source Document | Concept_ID Example |
|:---|:---|:---|
| **IACS** | UR S11A | `IACS_S11A_TD_001` |
| **IACS** | UR Z10.1 | `IACS_Z10_1_TD_001` |
| **IMO** | SOLAS Ch.II-1 | `IMO_SOLAS_II_1_TD_001` |
| **IMO** | MARPOL Annex I | `IMO_MARPOL_AI_TD_001` |
| **KR** | Rules Pt.3 Ch.1 | `KR_PT3_CH1_TD_001` |
| **EU** | Directive 2009/45/EC | `EU_DIR_2009_45_TD_001` |
| **EU** | Regulation (EU) 2015/757 | `EU_REG_2015_757_TD_001` |

#### SourceKey Normalization Rules

> **Steps 1–5** are the shared core rules, identical across all three instructions (TRUE_DEF / APPLICABILITY / CONTROLLED_TERM). Apply them uniformly to ensure Concept_IDs are predictable and cross-linkable. **Steps 6–7** handle source-family-specific abbreviation patterns for IMO Codes and EU legislation.

| Step | Rule | Example |
|:---:|:---|:---|
| 1 | Replace dots, parentheses, and commas with underscores (or remove if at word boundary) | `Z10.1` → `Z10_1`; `Pt.3 Ch.1` → `Pt3_Ch1` |
| 2 | Replace `/` and `-` with `_` | `II-1/3-8` → `II_1_3_8` |
| 3 | Collapse consecutive underscores | `II__1` → `II_1` |
| 4 | Use UPPERCASE | `Pt3_Ch1` → `PT3_CH1` |
| 5 | Remove document-type prefix (already in pattern) | `UR S11A` → `S11A` |
| 6 | IMO Codes: use standard abbreviation | `FSS Code` → `FSS`, `ISM Code` → `ISM` |
| 7 | EU: year + number pattern | `Directive 2009/45/EC` → `DIR_2009_45` |

- Base URI pattern: `https://{domain}/maritime-cv/{Concept_ID}` — `{Concept_ID}` is the full value including the Scheme prefix
- E.g., `https://example.org/maritime-cv/IACS_S11A_TD_001`
- In Phase 1, only the local ID (`Concept_ID`) is finalized; HTTP URI publication will follow once infrastructure is ready

### 3.6 Source_Doc_Type Controlled Values

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

> This closed list is shared across TRUE_DEF, APPLICABILITY, and CONTROLLED_TERM instructions.

---

## 4. Definition Cell Refinement — Separation Patterns

The Definition cell must contain **only the definitional core**. Non-definitional adjuncts matching the following patterns shall be separated into the designated columns; the remaining definitional core is preserved verbatim.

| # | Pattern | Identification trigger | Target Column |
|:---:|:---|:---|:---|
| 1 | Legal/technical commentary | "but the two roles are legally distinct" | Editor_Note |
| 2 | Alternative name | "Also called...", "Also known as..." | altLabel |
| 3 | Korean text | Korean characters | Replace with English |
| 4 | Reference annotation | `[-> see UR XX]`, `as defined in` | Editor_Note (record cross-reference) |
| 5 | Applicability scope | `[Note: applies primarily to...]` | Scope_Note |
| 6 | Formula + applicability tail | "Applicable to TM and QT steels..." | Scope_Note |
| 7 | Exclusion/negative scope | "does not cover...", "does not apply to..." | Scope_Note |
| 10 | Scope-limiting tail | "This is for all synthetic cordage materials." | Scope_Note |
| 11 | Example/enumeration tail | "e.g., Type A, B, C" | Example. If representing subtypes, flag with `[narrower candidate]` |

**Patterns flagged but deferred in Phase 1:**

| # | Pattern | Action |
|:---:|:---|:---|
| 8 | Pure redirect ("See UR Z18") | Tag with `[Phase 2: PARAPHRASE]` → backlog |
| 9 | Embedded sub-definition | Tag with `[Phase 2: extract]` → backlog |

---

## 5. Label Policy

| Label type | Purpose | Example |
|:---|:---|:---|
| `skos:prefLabel` | Primary label. **One per language only** | "ballast water management system"@en |
| `skos:altLabel` | Abbreviations, acronyms, legitimate variants | "BWMS"@en |
| `skos:hiddenLabel` | OCR variants, typos, dotted forms (search only) | "B.W.M.S."@en |

- If "Type A, B, C" are actual subtypes, do not add as altLabel → flag with `[narrower candidate]` and process in Phase 2 as separate concepts with narrower relations.
- If an abbreviation refers to the same concept as the full name, treat it as altLabel, not an independent concept.

---

## 6. Editorial Rules (Phase 1 Summary)

| Rule | Content |
|:---|:---|
| Language | English only (data cells). Korean is permitted only in work instructions/internal notes |
| Spelling | British English (moulded, vapour, draught, centre, programme). **TSV column headers use `@en` for simplicity. When converting to RDF, all English-language literals shall carry the `@en-GB` tag (BCP 47 compliant).** This two-layer approach avoids header verbosity while preserving dialect precision in the final RDF output |
| Definition cell | Retain the definitional core verbatim after separating non-definitional adjuncts. No editing or paraphrasing |
| Headword casing | Sentence case |
| Headword number | Singular by default. Exceptions: conventionally plural terms (scantlings, bilges) |
| Source citation | Separate Source_Doc and Source_Locator. Do not use `§` symbol |
| Two-layer | Source-faithful fields preserve the original text; normalized fields follow house style |

---

## 7. Source Citation

| Category | Source_Doc | Source_Locator example |
|:---|:---|:---|
| IACS UR | `UR S11A` | `2.1.3`, `Table 7`, `Annex III` |
| IACS UI | `UI SC123` | `1.1` |
| IACS Rec | `Rec 87` | `2.3` |
| IACS PR | `PR 38` | `3.1` |
| SOLAS | `SOLAS II-1` | `3.30` |
| IMO Resolution | `IMO Res. MSC.370(93)` | |
| KR Rules | `KR Rules Pt.3` | `Ch.1 1.2` |
| EU Directive | `Directive 2009/45/EC` | `Art.2` |
| EU Regulation | `Regulation (EU) 2015/757` | `Art.3` |

---

## 8. Grouping Rule

- Do not use `broader/narrower` for document-level, chapter-level, or source-level grouping.
- Source-level grouping is handled by `skos:ConceptScheme` (IMO / IACS / KR / EU).
- For document-level or topic-level sub-grouping, use `skos:Collection`.

---

## 9. Procedure

```
Step 1  Locate the Definitions section of the target document
Step 2  Extract term + definition from the Definitions section
Step 3  Apply Admission Rule — determine TRUE_DEF eligibility
Step 4  Assign Concept_ID (with _TD_ infix), record Scheme, set Source_Doc_Type, set Record_Type = TRUE_DEF
Step 5  Refine Definition cell — separate Patterns 1-7, 10-11
Step 6  Tag Patterns 8, 9 → Phase 2 backlog
Step 7  Finalize prefLabel / altLabel
Step 8  Record Source_Doc / Source_Locator separately
Step 9  Verify (Section 10)
```

---

## 10. Verification

### 10.1 2-Pass Review

| Pass | Focus | Check items |
|:---|:---|:---|
| **Structural** | Table integrity | Column count consistency (12 columns), Required-field empty cell check (Conditional/Optional fields may be blank per obligation rules), no duplicate Concept_ID, valid Scheme values, valid Source_Doc_Type values, `_TD_` infix present, Record_Type = `TRUE_DEF` |
| **Semantic** | Content correctness | Definition = source verbatim, no definition content mixed into Scope_Note, one prefLabel per language, Record_Type = `TRUE_DEF` only |

### 10.2 Cross-Check Rules

| Rule | Check | Severity |
|:---|:---|:---|
| Required fields | Concept_ID, Record_Type, Scheme, Source_Doc_Type, prefLabel, Definition, Source_Doc, Source_Locator must be filled | **Error** |
| Record_Type value | Must be `TRUE_DEF` | **Error** |
| Valid Scheme | Must be one of `IMO`, `IACS`, `KR`, `EU` | **Error** |
| Source_Doc_Type value | Must be from closed list (Section 3.6) | **Error** |
| Concept_ID format | Must conform to `{Scheme}_{SourceKey}_TD_{SeqNo}` pattern with `_TD_` infix | **Error** |
| Concept_ID prefix check | Concept_ID prefix must match Scheme value (`IMO_`, `IACS_`, `KR_`, `EU_`) | **Error** |
| Source family consistency | Scheme value must be consistent with Source_Doc naming (e.g., Scheme=`IMO` must have IMO-style Source_Doc) | **Error** |
| No Korean in English fields | Definition, Scope_Note, and Example must not contain Korean characters | **Error** |
| Duplicate prefLabel review | Same-language prefLabel collision within the same Scheme + same Source_Doc triggers review (warning, not automatic failure) | **Warning** |
| `[narrower candidate]` flag | Presence of subtype flag requires Phase 2 review | **Warning** |
| Abbreviation collision | Same altLabel used across different concepts triggers review | **Warning** |
| Record_Type-conditional validation | If Record_Type = `TRUE_DEF`, APPLICABILITY-only columns (Target_Entity, Ship_Type, etc.) must be blank | **Error** |
| Definition verbatim check | Definition@en must match the definitional core from the source after pattern separation; no paraphrasing or editorial changes | **Error** |

> **SHACL note**: Section 10.2 cross-check rules are the normative validation specification. SHACL shapes for automated validation will be generated from these rules in Phase 2 — no separate SHACL table is maintained in this document.

---

## 11. Output Specification

All final output files are saved to the **`results/`** subdirectory under the working directory from which the instruction is executed. Per-chunk intermediate files (partial TSV and log files produced during segmented processing) are saved to **`results/temp/`**. Both directories shall be created automatically if they do not exist. Each extraction run produces exactly **3 final files** in `results/`: one result file, one summary file, and one log file. Intermediate files in `results/temp/` are retained for traceability but are not considered deliverables.

### 11.1 File Naming Convention

| File | Name Pattern | Description |
|:---|:---|:---|
| **Result** | `phase1_true_def_result.tsv` | Final extraction table in TSV format (Tab-Separated Values). Contains all extracted records conforming to the Target Schema (Section 3). One header row + data rows. UTF-8 with BOM. |
| **Summary** | `phase1_true_def_summary.md` | Extraction summary report in Markdown format. |
| **Log** | `phase1_true_def_log.md` | Processing log in Markdown format. |

### 11.2 Result File (`phase1_true_def_result.tsv`)

- **Format**: TSV (Tab-Separated Values), UTF-8 with BOM
- **Header row**: Column names exactly as defined in Section 3.1, tab-delimited
- **Column order**: `Concept_ID	Record_Type	Scheme	Source_Doc_Type	prefLabel@en	altLabel@en	Definition@en	Scope_Note@en	Example@en	Source_Doc	Source_Locator	Editor_Note`
- **Empty cells**: Leave blank (no placeholder text such as "N/A" or "-")
- **Multi-value delimiter**: Semicolon (`;`) within a cell, as per Section 3.1
- **Quoting**: Fields containing tabs, newlines, or double quotes must be enclosed in double quotes. Embedded double quotes are escaped as `""`
- **Sort order**: By `Source_Doc` (ascending), then by `Source_Locator` (document order)

### 11.3 Summary File (`phase1_true_def_summary.md`)

The summary file shall contain the following sections:

```markdown
# Phase 1 TRUE_DEF Extraction Summary

## Run Info
- Date: {YYYY-MM-DD}
- Source documents processed: {count}
- Total records extracted: {count}

## Records by Scheme
| Scheme | Count |
|:---|---:|
| IMO | {n} |
| IACS | {n} |
| KR | {n} |
| EU | {n} |

## Records by Source_Doc
| Source_Doc | Count |
|:---|---:|
| {doc} | {n} |
| ... | ... |

## Quality Flags
- Phase 2 backlog items: {count}
- Editor_Note flags: {count}
- [narrower candidate] flags: {count}

## Issues / Observations
- {free text: notable decisions, ambiguities, deferred items}
```

### 11.4 Log File (`phase1_true_def_log.md`)

The log file records the sequential processing trace:

```markdown
# Phase 1 TRUE_DEF Processing Log

## {Source_Doc} — {Section/Chapter}
- **Segment**: {segment number} / {total segments}
- **Tokens (approx)**: {n}K
- **Records extracted**: {count}
- **Decisions**:
  - {term}: Admitted / Excluded — {reason}
  - ...
- **Flags**:
  - {Concept_ID}: {flag description}
  - ...
```

### 11.5 Overwrite Rule

Each new extraction run **overwrites** the previous final output files in `results/` and all intermediate files in `results/temp/`. If incremental preservation is needed, the user must rename or archive prior files before initiating a new run.

---

## 12. Phase 1.1 — Validation Exception Management

When recurring comments are identified during iterative validation of Phase 1 outputs, they are escalated to Phase 1.1 for systematic resolution. Phase 1.1 is **not** an additional extraction phase — it is a QA exception layer.

**Full specification**: See [`phase1_1_validation_exception_guide.md`](phase1_1_validation_exception_guide.md) (shared across all three Phase 1 instructions).

**Escalation criteria (summary)**:
- Comment recurs 2+ times or across 2+ documents/records
- Issue blocks validator pass
- Current guide text is ambiguous — reviewers disagree on correct action
- Phase 1 / Phase 2 boundary is unclear

**Key difference from Phase 1 overwrite rule**: The Phase 1.1 issue register is **versioned and never overwritten** (`results/phase1_1/phase1_1_issue_register_{date}_v{NN}.tsv`).

---

## 13. Phase 2 Preview (Reference Only — Outside the Scope of This Document)

| Item | Description |
|:---|:---|
| Add DESCRIPTION / PARAPHRASE | Promote from backlog |
| Technical Terms classification | descriptor / search / rule_bound |
| Abbreviation registry | Abbreviation normalization registry |
| Broader/Related assignment | Assign `skos:broader` and `skos:related` relationships |
| Frequency/Fitness assessment | Assess term frequency and controlled-vocabulary fitness |
| Cross-source mapping | closeMatch by default, exactMatch only when certain. owl:sameAs prohibited |
| JSON conversion | terms.json as single source of truth |
| SKOS-XL | Label-to-label relations (acronym-of, etc.) |
| OWL conversion | Formal ontology generation |

---

*Phase 1 scope: TRUE_DEF only, source-specific concept, definition/note separation, stable ID with `{Scheme}_..._TD_` pattern, Source_Doc_Type classification, Record_Type as single discriminator. Output: 3 final files (result TSV + summary MD + log MD) in `results/`, intermediate chunk files in `results/temp/`.*
