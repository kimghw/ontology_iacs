# Maritime Controlled Vocabulary Work Instruction

## 1. Background

### 1.1 Purpose

This work instruction defines the procedures for refining the IMO Instrument, IACS UR, KR regulations and industry standardsd controlled vocabulary . The goals are:
- SKOS 작업 이전에 통제 단어 분류
- Separate source definitions from editorial commentary
- Classify compound terms by domain specificity
- Normalize abbreviations
- Prepare the vocabulary for JSON conversion and eventual SKOS/OWL ontology generation

### 1.2 External Review Comments

처음부터 하나의 공통 개념으로 합치지 않는 것이 좋습니다. IMO/IACS/KR가 같은 headword를 써도 정의·적용범위가 조금씩 다를 수 있는데, SKOS는 “어떤 특정 관계나 정의가 어느 scheme에 속하는지”를 세밀하게 기록하는 데 한계가 있습니다. 그래서 1차는 source-specific concept로 분리하고, 나중에 mapping으로 잇는 방식이 안전합니다

### 1.3 Strategic Direction (Medium-term)

- JSON as single source of truth; markdown as derived view

### 1.4 Document Source Structure Patterns Before Extraction

Before starting Tasks 1-3, document the structural patterns of each source document type (IMO, IACS UR, KR) to identify where and how terms appear.

**Document for each source type:**

1. **Definitions section pattern**: heading level, numbering scheme, position within document (e.g., "1.2 Definitions", "Section 2 — Definitions")
2. **Definition format**: how individual terms are presented (e.g., `"Term" means ...`, `**Term**: ...`, numbered list)
3. **Non-definition locations**: where terms are defined outside the Definitions section (body text inline definitions, footnotes, tables, annexes, notes)
4. **Section numbering scheme**: overall document structure and hierarchy (e.g., `1.2.3.4` or `Chapter/Regulation` for SOLAS)
5. **Cross-reference patterns**: how documents refer to terms defined elsewhere (e.g., `as defined in UR S2`, `see 1.2.1 above`)
6. **Annex/Appendix structure**: whether annexes are normative or informative, and how they relate to the main body

**Output**: A pattern catalogue per document family (IMO, UR series, KR) recorded before any extraction begins. This catalogue informs the 11-pattern scan in Task 1 and the scope classification in Task 2.

---

## 2. Working Principles

### 2.0 Language Rule

> The controlled vocabulary data files (term, definition, editor note, scope note) are written in **English only**. This work instruction and internal notes may use Korean.

### 2.1 Document-Based Principle

> **All classification, tagging, and modification must be based on directly reading the regulatory source text. No guessing.**

- **Source Data**: IMO conventions/resolutions, IACS UR, KR rules/guidance, and other maritime regulatory texts (markdown conversions or PDFs). All entries must be verified against source text.
- **Source Types**:

| Source Type | Abbreviation | Examples |
|:---|:---|:---|
| IMO Convention/Code/Resolution | IMO | SOLAS Ch.II-1, MARPOL Annex VI, ISM Code |
| IACS Unified Requirement | UR | UR S11A, UR Z17, UR W11 |
| KR Classification Rules/Guidance | KR | KR Rules Pt.3, KR Guidance for FPSOs |
| International Standard | (use org directly) | ISO 148-1, IEC 60092, ASTM G77-17 |

- **Definition Status Criteria** (Axis 1: Authority):

| Status | Criterion | Source Pattern |
|:---|:---|:---|
| TRUE_DEF | Explicit "Definitions" section exists and the term is defined therein | `"Bulk carrier" means a ship...` / `**1.2.1 Ballast Tank**: ...` |
| DESCRIPTION | Extracted from body text, footnotes, annexes, or non-definitions sections | `"The alarm system is intended to..."`, footnote definitions |
| PARAPHRASE | Delegated to another regulation or heavily abbreviated | `"L = Rule length, as defined in UR S2"` |

- **Definition Style** (Axis 2: Form -- independent of status):

| Style | Description |
|:---|:---|
| `semantic` | Standard "X means Y" natural-language definition |
| `parametric` | Defined primarily by a formula, symbol mapping, or numeric threshold |
| `enumerated` | Defined by listing graded sub-categories (e.g., GOOD/FAIR/POOR) |
| `operational` | Specifies a procedure, test condition, or regulatory process |

> **Mixed-style rule:** When a definition combines two styles (e.g., enumerated + operational), assign the primary style based on the dominant structural pattern and record the secondary style in the Editor Note as `[Style: primary + secondary]`.

- **Authority Hierarchy** (for resolving conflicts when same term appears at multiple locations):

| Rank | Location | Treatment |
|:---:|:---|:---|
| 1 | Formal "Definitions" section in document | TRUE_DEF |
| 2 | Explicit definitional sentence in normative body text | DESCRIPTION |
| 3 | Normative Appendix/Annex expressly incorporated by the UR | TRUE_DEF with `location: appendix`. If the Annex definition is more detailed than body text, prefer the Annex definition and note the body-text version in Editor Note |
| 4 | Implementation Notes with definitional content | DESCRIPTION with `location: note` |
| 5 | Footnotes and informative annexes | Editor Note only |

### 2.2 Editorial Rules

| Rule | Content |
|:---|:---|
| Language | English only for data cells. Korean permitted in work instruction and section headers |
| Spelling | British English per IMO/IACS convention (moulded, vapour, draught, centre, programme) |
| Definition cell | Source definition text only (verbatim from source) |
| Editor notes | Separated from definition. Use `Editor Note` column or `[Editor Note: ...]` |
| Scope notes | Applicability/domain constraints from source text. Separate from editor notes |
| Headword casing | Section 2: Sentence case. Section 3: lowercase. Abbreviations: preserve source case |
| Headword number | Singular by default. Exception: conventionally plural terms (scantlings, bilges) |
| Abbreviation periods | Initialisms: period-free (BM not B.M.). Truncations: keep period (Rev., Corr., Cat.) |
| Subscripts | ASCII underscore in markdown/JSON: `R_eH`, `t_net`, `T_sc`. Plain inline as altLabel: `ReH` |
| Chemical formulas | Plain ASCII text: CO2, H2S, NOx |
| Hyphenation | Follow source text (watertight, non-destructive, double bottom) |
| Source citation | Preserve source-native locator syntax. Never use `§` symbol |
| Two-layer standard | Source-faithful fields preserve exact text; normalized fields follow house style |

### 2.3 Scope Definition

| Include | Exclude |
|:---|:---|
| Terms defined in IMO, IACS UR, KR rule body Definitions sections | General engineering terms -> tag as `search` scope |
| Maritime regulatory domain abbreviations | Chemical formulae, SI units -> tag as `notation`/`unit` |
| Explicit definitions from Definitions sections | UR revision/status/effective date -> separate register |
| Body-text descriptions (DESCRIPTION tag) | ISO/IEC pure delegation ("as defined in ISO X") -> external reference |
| Cross-UR definitions with different scopes -> separate entries per source | Informative annex/footnote commentary -> Editor Note |
| Terms from active documents | Terms from withdrawn-before-effective documents (e.g., H1) -> exclude entirely |

| Rule | Description 
|:---|:---|
| **Document Lifecycle** | Active documents only as primary entries. Deleted UR terms absorbed by successor: include under successor with Editor Note provenance. No-successor deleted terms: exclude |
| **ISO Incorporation Test** | Tier A (pure delegation): external ref only. Tier B (restated): include as PARAPHRASE. Tier C (modified): include as TRUE_DEF/DESCRIPTION |
| **Ship Type Names** | Include when explicitly defined in UR/IMO Definitions section. Exclude when used only descriptively |
| **Procedural Terms** | Include when IMO, IACS definition adds Maritime specific meaning beyond ISO 9001/general usage. Exclude otherwise as `search` |
| **Notes/Footnotes** | Excluded from definition cell by default. Include as DESCRIPTION only if IMO, IACS give operative definitional force |

### 2.4 Source Citation Format

Use a compact 3-dimension citation model: **Source Family + Locator Type + Optional Qualifier**

| Category | Format | Example |
|:---|:---|:---|
| UR + section | `UR {series}{number}.{section}` | `UR P2.7.4`, `UR S11.2.1.3` |
| UR + table | `UR {series}{number} Table {N}` | `UR P2 Table 7` |
| UR + annex | `UR {series}{number} Annex {X}` | `UR Z10.4 Annex III` |
| UR + revision | `UR {series}{number} (Rev.{N})` | `UR S19 (Rev.5)` |
| SOLAS | `SOLAS {Chapter}/{Regulation}` | `SOLAS II-1/3.30` |
| IMO Resolution | `IMO Res. {Body}.{N}({Session})` | `IMO Res. MSC.370(93)` |
| IMO Circular | `IMO {Body}/Circ.{N}` | `IMO MSC.1/Circ.1328` |
| ISO/IEC | `{Org} {Number}:{Year}` | `ISO 148-1:2016`, `IEC 60079-10-1:2015` |

**Rules:**
- Always use `UR` prefix for IACS references
- Use specific organization abbreviation (ISO, IEC, ASTM) directly -- no `STD` prefix
- Include edition year when citing specific requirements; omit for generic references
- Source column carries UR identifier only; table/figure/annex details go to Editor Note

---

## 3. Tasks

> **Section 4 (synonyms/variants) is excluded from current scope.** Relationship type separation will be handled via relations.json during JSON conversion.

### Task 1: Definition and Note Separation

**Goal:** Separate source definitions from editorial commentary in Section 2 Definition cells

**Problem Typology (11 patterns):**

| # | Pattern | Trigger | Target Field |
|:---:|:---|:---|:---|
| 1 | Legal/technical commentary mixed in definition | "but the two roles are legally distinct" | Editor Note |
| 2 | Alternative name mixed in definition | "Also called...", "Also known as..." | Alt Label (skos:altLabel) |
| 3 | Korean text mixed in | Any Korean characters | Replace with English |
| 4 | Reference annotation | `[-> see UR XX]`, `as defined in` | Source Ref |
| 5 | Applicability scope annotation | `[Note: applies primarily to...]` | Scope Note (skos:scopeNote) |
| 6 | Formula + applicability tail | "Applicable to TM and QT steels..." | Scope Note |
| 7 | Exclusion/negative scope statement | "does not cover...", "does not apply to..." | Scope Note |
| 8 | Pure cross-reference redirect | "See UR Z18" (no definition text) | Source Ref (status: PARAPHRASE, definition: null) |
| 9 | Embedded sub-definition of another term | "As per MSC.266(84), 'Special purpose ship' means..." | Flag for extraction (deferred to Task 1b) |
| 10 | Scope-limiting tail sentence | "This is for all synthetic cordage materials." | Scope Note |
| 11 | Example/enumeration tail | "e.g., Type A, B, and C" | Examples or broader/narrower relations |

**Note Field Mapping:**
- `skos:definition` -- source definition text only
- `skos:scopeNote` -- applicability, domain limits, scope constraints from source
- `skos:editorialNote` -- extraction rationale, QA comments, curator notes
- `skos:historyNote` -- concept history (withdrawn, superseded, renamed)
- `dcterms:source` -- UR/IMO/ISO references and redirect targets

**Procedure:**

1. Scan all Section 2 entries for the 11 pattern types (Pattern #9 items: flag with `[Task 1b]` tag only — separate entry extraction is deferred to Task 1b after Task 1 verification)
2. Add columns to Section 2 table:
   ```
   | Term | Definition | Source UR(s) | Status | Style | Scope Note | Editor Note |
   ```
3. Definition cell: retain only source definition text (verbatim)
4. Separate content into appropriate columns per typology
5. Replace all Korean text with English equivalents

---

### Task 2: Scope Classification -- Technical Terms

**Goal:** Classify Section 3 terms by domain specificity

**Classification (Markdown: 2-tier with flag):**

| Scope | Criterion | Examples |
|:---|:---|:---|
| **descriptor** | Term has special or restricted meaning in IACS/maritime context | hatch coaming, cargo containment system, secondary barrier, corrosion addition |
| **search** | General engineering/physics term with identical meaning everywhere | axial stress, beam elements, Von Mises stress, fillet weld |
| + `rule_bound` flag | General term BUT IACS UR attaches specific formula/threshold/acceptance criteria | critical buckling stress, section modulus, yield strength, design pressure |

**Decision Tree:**
1. Does this term exist in general engineering/physics textbooks? -- If NO -> `descriptor`
2. If YES: Does IACS, KR define a specific calculation method, acceptance criterion, or regulatory procedure for this term? -- If YES -> `search` + `rule_bound: true`. If NO -> `search`

**`rule_bound` qualification criteria** (at least one must be met):
- UR provides an explicit formula for calculating the value (e.g., `sigma_c = ...`)
- UR defines a numeric acceptance threshold or limit (e.g., "shall not exceed ...")
- UR specifies a test method or condition that differs from the general ISO/textbook procedure
- UR restricts the parameter's applicability to specific ship types, materials, or structural members

> Note: A term is NOT `rule_bound` merely because it appears in a UR equation as an input variable with no UR-specific definition of how to determine it.

**JSON extended classification** (for concept_class + functional_role):

| concept_class | functional_role | Example |
|:---|:---|:---|
| descriptor | entity | hatch coaming, cofferdam |
| descriptor | parameter | corrosion addition, freeboard |
| search | entity | beam element, shell element |
| search | parameter (rule_bound) | critical buckling stress, section modulus |

**Procedure:**

1. Scan all Section 3 entries and classify as descriptor/search
2. Flag `rule_bound` for borderline general terms with IACS-specific rules
3. Add columns:
   ```
   | Term | Category | Source UR(s) | Scope | Rule_Bound | Scope_Note |
   ```
4. Rename Section 3 title: "Technical Terms" (not "Compound Technical Terms" -- includes single-word entries like cofferdam, breakwater, girder)

---

### Task 3: Abbreviation Normalization

**Goal:** Normalize Section 1 abbreviations with proper type classification

**Semantic Class (primary type -- 6 values):**

| Semantic Class | Description | Examples |
|:---|:---|:---|
| `technical_term` | Domain-specific acronyms/abbreviations | BWMS, PSM, NDT, CSR, ESP |
| `organization` | Organizations and bodies | IACS, IMO, ISO, ASNT, CIE |
| `document_or_regulatory` | Codes, conventions, standards | FSS Code, IGC Code, SOLAS |
| `notation` | Chemical formulae and engineering symbols | CO2, H2S, Ceq, ReH, Rp0.2 |
| `unit` | Measurement units | kPa, kW, N/mm2, dB(A) |
| `doc_control_marker` | Document lifecycle markers | Rev., Corr., Del., Cat. |

**Form Type (secondary -- for normalization rules):**

| Form Type | Description | Period Rule | Examples |
|:---|:---|:---|:---|
| `simple` | No internal punctuation | Strip periods | BWMS, NDT |
| `dotted_initialism` | Period-separated initials | Strip periods (prefLabel=no dot, altLabel=dotted) | B.M. -> BM |
| `dotted_truncation` | Period marks abbreviation by truncation | Keep period | Rev., Corr., Cat. |
| `slash_pair` | Slash-separated | Split into individual entries | DMA/DMB/DMC/DMX |
| `subscript_variant` | Contains subscripts | ASCII underscore canonical; plain inline as alt | R_eH / ReH |

**Optional Source Category** (attribute, not primary type):
- `org`, `regulatory`, `standard`, `process`

**Normalization Rules:**
- Case: preserve as-is from source (RA vs Ra are distinct)
- Periods: initialisms strip periods; truncations keep periods
- Collision check: verify no polysemy collision before normalizing (e.g., O.T./OT)
- Merge duplicates: ReH and R_eH -> single entry, ReH as altLabel
- Polysemy context tags: use controlled vocabulary (structural, test, nav, coating, cert, survey, material, network)

**Procedure:**

1. Add columns to Section 1 table:
   ```
   | Abbreviation | Full Form | Source UR(s) | Semantic Class | Form Type |
   ```
2. Apply period normalization with collision check
3. Merge duplicate entries (same meaning, different notation)
4. Link abbreviation entries to corresponding Section 2 concepts where applicable

---

## 4. JSON Conversion

> Medium-term goal. JSON as single source of truth; markdown as derived view.

### 4.1 Target File Structure

```
output/
  terms.json                 -- Master concept data
  abbreviation_registry.json -- Abbreviation label registry
```

### 4.2 terms.json Schema
 ** SKOS 범위를 넘어서는 확장 필드는 이 단계에서는 포함하지 않는다 ** (e.g., `confidence` — requires custom extension vocabulary, deferred to OWL phase)
```json
{
  "record_id": "IACS_CV_0001",
  "term": "Ballast Water Management System",
  "aliases": [],
  "abbreviations": ["BWMS"],
  "concept_class": "descriptor",
  "functional_role": "entity",
  "definitions": [
    {
      "text": "System which processes ballast water such that it meets or exceeds the BWM Convention D-2 standard.",
      "status": "TRUE_DEF",
      "style": "semantic",
      "source_refs": [
        {"corpus": "IACS_UR", "document_id": "F45", "section": "1.2.2"},
        {"corpus": "IACS_UR", "document_id": "M74", "section": "2.1"}
      ],
      "scope_note": null,
      "editor_note": null
    }
  ],
  "term_status": "active"
}
```

### 4.3 record_id Convention

| Source Scope | Prefix | Example |
|:---|:---|:---|
| IACS UR terms | `IACS_CV_` | `IACS_CV_0001` |

> `CV` = Controlled Vocabulary. Covers all source types (IMO, IACS UR, KR) within the unified vocabulary.

### 4.4 concept_class Values

| concept_class | Description | Markdown Mapping |
|:---|:---|:---|
| `descriptor` | IACS/maritime domain-specific term with definition | Section 2 + descriptor scope |
| `search_phrase` | General engineering term for retrieval | Section 3 + search scope |
| `abbreviation_only` | Abbreviation without independent definition | Section 1 (no Section 2 entry) |
| `notation` | Chemical formula, engineering symbol | Section 1 (notation semantic_class) |
| `unit` | Measurement unit | Section 1 (unit semantic_class) |

### 4.5 abbreviation_registry.json Schema

```json
{
  "abbreviation": "BWMS",
  "full_form": "Ballast Water Management System",
  "context": null,
  "source_urs": ["F45", "M74", "Z17"],
  "semantic_class": "technical_term",
  "form_type": "simple",
  "linked_concept_id": "BallastWaterManagementSystem"
}
```

### 4.6 Domain Controlled Vocabulary

| Domain ID | UR Series | Description |
|:---|:---|:---|
| HullStructure | S | Hull structures, strength |
| Materials | W | Materials, welding, testing |
| Machinery | M | Machinery, propulsion |
| Electrical | E | Electrical, control systems |
| FireSafety | F, L | Fire protection, lifesaving, stability |
| Survey | Z | Survey, certification, classification |
| Environmental | P | Environmental protection, piping |
| General | A, C, D, G, I, K, N | General requirements |

---

## 5. Work Sequence and Priority

| Order | Task | Priority | Est. Volume | Parallelizable |
|:---:|:---|:---:|:---|:---:|
| 1 | **Task 1: Definition/Note Separation** | High | ~50 items | Yes (independent of Task 2, 3) |
| 1b | **Task 1b: Embedded Sub-definition Extraction** | Medium | Flagged items from Task 1 (Pattern #9) | Requires Task 1 complete |
| 2 | **Task 2: Scope Classification** | Medium | ~365 items | Yes (independent of Task 1, 3) |
| 3 | **Task 3: Abbreviation Normalization** | Low | ~30 items | Yes (independent of Task 1, 2) |
| 4 | **JSON Conversion** | Medium-term | Full corpus | Requires Tasks 1-3 complete |

> Tasks 1, 2, and 3 operate on different sections and can be executed in parallel.
> Task 1b is gated on Task 1 completion — it creates new entries from Pattern #9 flags.
> JSON conversion is gated on completion and verification of all tasks.

---

## 6. Verification

### 6.1 Three-Pass Quality Review

| Pass | Focus | Checks |
|:---|:---|:---|
| 1: Structural | Table integrity | Column counts, pipe delimiters, new columns populated, no orphaned rows |
| 2: Semantic | Content correctness | Definition purity, scope tags correct, status/style match, cross-references valid |
| 3: Quality | Cross-cutting | Summary statistics accurate, external review comments addressed, version metadata updated |

### 6.2 AI-Assisted Adversarial Review

After human verification, use an LLM to:
1. Extract definitions from cited UR source text
2. Compare against Definition cell content
3. Flag significant discrepancies for human review

### 6.3 Rollback and Version Control

- Baseline: save v1.3 snapshot before any task begins
- Per-task checkpoints: v1.3.T1 (after Task 1), v1.3.T2, v1.3.T3
- Final: v2.0 after all tasks verified
- Rollback trigger: any verification pass FAIL -> revert to last checkpoint, fix, re-verify
- Version naming: filename suffix or metadata header date field

---

## 7. Deliverables

| File | Description | Timing |
|:---|:---|:---|
| `controlled_vocabulary.md` (v2.0) | Controlled vocabulary with Tasks 1-3 applied | After all tasks complete + verified |
| `terms.json` | JSON master concept data | JSON conversion phase |
| `abbreviation_registry.json` | Abbreviation label registry | JSON conversion phase |

---

## 8. Glossary

| Term | Definition |
|:---|:---|
| TRUE_DEF | Definition from a formal "Definitions" section in the UR body |
| DESCRIPTION | Definition extracted from body text, footnotes, or non-definitions sections |
| PARAPHRASE | Definition delegated to another UR or heavily abbreviated/paraphrased |
| descriptor | Term with special/restricted meaning in IACS/maritime context |
| search | General engineering term with identical meaning outside IACS |
| rule_bound | Flag for search terms that have IACS-specific calculation/acceptance criteria |
| semantic_class | Primary type classification for abbreviations (6 values) |
| form_type | Notation form classification for abbreviation normalization |

---

*End of work instruction.*
