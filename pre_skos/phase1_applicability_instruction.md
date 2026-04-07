# Phase 1: APPLICABILITY Controlled Vocabulary Work Instruction

> **Pre-SKOS Phase**: This is a preparatory step for building SKOS `skos:broader` / `skos:related` hierarchical and associative relationships in Phase 2. Phase 1 focuses on source-faithful applicability extraction and flat-table cataloguing; formal SKOS semantic relations are constructed in the subsequent phase.

> **Scope**: Extract and structure the applicability/scope statements from **IMO conventions/codes, IACS UR documents, KR Rules/Guidance, and EU Directives/Regulations**.
> The goal is to capture **what, to whom, under what conditions, and when** each regulatory instrument applies, using a flat-table format with applicability-specific columns.
> Full cross-source reasoning (superseded_by, overrides_if, hybrid_split, etc.) is deferred to Phase 2.
> **Work Procedure**: Agents process source texts per Work Unit as defined by `commands/prerequisite.md` and allocated by `commands/agents.md`.
> **Segmentation**: Document segmentation (Chunks, Work Units) is determined by `commands/prerequisite.md`. This instruction does not define independent chunking logic. In standalone execution (without PRE), use a fallback heuristic: review window ≤ 100K tokens, working chunks ≤ 80K tokens, split at heading boundaries.
---

## 0. Prerequisites

A preparatory step where the LLM and user jointly review the target document and extract baseline data. Each instruction (TRUE_DEF, APPLICABILITY, CONTROLLED_TERM) is executed independently.

> **When PRE artefacts exist** (heading structure, Work Unit register, Task Brief): skip Steps 0.1–0.2 and use the PRE-defined Work Unit boundaries and extraction scope from the Task Brief. Proceed directly to Step 0.3 with the WU-scoped source text.
>
> **When running standalone** (no PRE): execute Steps 0.1–0.5 below.

1. **Document review** — Read the target document and identify how applicability statements are structured (e.g., Application section, regulation preambles, Part/Chapter scope clauses).
2. **Extraction scoping** — Extract only applicability/scope sentences from the relevant sections. Save extracted sentences to the intermediate directory (`results/temp/`).
3. **Pattern cataloguing** — Analyse the extracted sentences from Step 2 (or from the WU-scoped source text when using PRE artefacts) and compile a pattern catalogue (`results/temp/doc-{doc_key}__applicability__patterns.tsv`). Record recurring sentence structures (e.g., `"This UR applies to..."`, `"of [N] GT and above"`, `"not applicable to..."`, `"ships contracted for construction on or after..."`). This catalogue serves two purposes: (a) the separation script can use the patterns to **auto-flag potential omissions** in the remainder, and (b) patterns can be reused for **cross-instruction classification checks** (e.g., detecting a TRUE_DEF-type sentence mistakenly included in APPLICABILITY extraction).
4. **Extraction separation** — Run a separation script against the source document and the extracted sentences in `results/temp/` to produce two outputs: (a) **extracted sentences** (matched) and (b) **non-extracted sentences** (unmatched remainder). The script also applies the pattern catalogue from Step 3 to flag remainder sentences that match known applicability patterns as **omission candidates**. The LLM performs the initial extraction (Step 2); the separation and pattern matching are performed by script to ensure mechanical completeness.
5. **Extraction verification** — The LLM reviews the non-extracted sentences (unmatched remainder from Step 4), with priority on script-flagged omission candidates, to verify that no required applicability sentences were missed. If omissions are found, add them to the extracted set, update the pattern catalogue if a new pattern is identified, and re-run the separation script.

---

## 1. Admission Rule

| Condition | Include | Exclude (Phase 2 backlog) |
|:---|:---|:---|
| Source location | "Application", "Scope", "General" sections; opening paragraphs that state applicability; regulation preambles (IMO); Part/Chapter scope clauses (KR) | Detailed technical requirements (formulas, scantlings, test procedures) |
| Record type | **APPLICABILITY** only | TRUE_DEF records (handled by separate instruction) |
| Source | **IMO**: Conventions, mandatory/recommendatory codes, resolutions, circulars (active instruments only — see Source_Doc_Type enum in Section 3.6 for full list); **IACS**: UR, UI, Rec, PR (active documents only); **KR**: Rules, Technical Rules, Guidance, Interpretations (current editions only); **EU**: Directives, Regulations, Decisions (in force) | Withdrawn/superseded-before-effective documents |
| Language | English only (data cells) | Replace Korean text with English |
| Granularity | **One record per regulatory unit** (or per distinct applicability clause if a source has multiple independent scope blocks). For IMO, the regulatory unit is typically a regulation or rule within a chapter. For IACS, typically one document (UR, UI, Rec, or PR). For KR, the lowest autonomous applicability clause — often a Section-level scope clause (e.g., `Sec.1 101 Application`) rather than an entire Part or Chapter, since KR's Part–Chapter–Section–Article–Paragraph hierarchy places actual applicability statements at varying levels. For EU, the regulatory unit is typically an article-level scope clause within a Directive or Regulation. | Sub-clause level requirements |

**One-line decision**: Does the text state what entity / ship type / condition the instrument applies to? — **Yes -> adopt**, No -> skip.

---

## 2. Core Principle: Source-Faithful Extraction

- **Extract verbatim first, then decompose.** The `Applicability_Text@en` column preserves the original prose. Structured columns are derived from this anchor text.
- **One source unit may produce multiple applicability records** if it contains distinct scope blocks (e.g., UR A2 has "normal towing" and "other towing" as separate scopes; SOLAS II-1/Reg.3 and II-1/Reg.3-8 have distinct scopes).
- **Do not infer conditions not stated in the text.** If a source does not mention a ship type restriction, leave `Ship_Type` blank — do not default to "all ships".
- **Anchor traceability rule**: Every value in a structured column must be traceable to a phrase in `Applicability_Text@en`. If a value comes from a different section of the source document (not the main applicability statement), the anchor text must be extended to include that passage, or the source must be recorded in `Editor_Note` with a `[source: Section X.X]` tag.

---

## 3. Target Schema

```
Concept_ID | Record_Type | Scheme | Source_Doc_Type | Applicability_Text@en | Target_Entity | Target_Role | Target_Object@en | Ship_Type | Size_Threshold | Qual_Predicate@en | Geographic_Scope@en | Cargo_Substance@en | Normative_Basis | Implements_Requirement | Exclusion@en | Trigger_Event | Trigger_Date | Normative_Status | Applicability_Status | Source_Doc | Source_Locator | Editor_Note
```

### 3.1 Column Definitions with Obligation

| # | Column | Obligation | SKOS/DC Mapping | Data Type | Cardinality | Rule |
|:---:|:---|:---:|:---|:---|:---|:---|
| 1 | **Concept_ID** | **Required** | URI fragment | ID | single | Format: `{Scheme}_{SourceKey}_APP_{SeqNo}`. See Section 3.5 for Concept_ID design rules per source family. **Once assigned, never renumbered; gaps permitted.** |
| 2 | **Record_Type** | **Required** | `dct:type` | enum | single | Fixed to `APPLICABILITY`. Discriminator so both record types coexist in one sheet. |
| 3 | **Scheme** | **Required** | `skos:inScheme` | enum | single | One of `IMO`, `IACS`, `KR`, `EU`. Identifies the source family of the regulatory instrument. |
| 4 | **Source_Doc_Type** | **Required** | `dct:type` (secondary) | enum | single | Classifies the document genre. Values from closed list (Section 3.6). |
| 5 | **Applicability_Text@en** | **Required** | `skos:scopeNote` | text | single | Verbatim or lightly normalized applicability statement from the source section. This is the **anchor field** — all structured columns are derived from this text. Must include all passages from which structured column values are extracted. See Section 2 anchor traceability rule. |
| 6 | **Target_Entity** | **Required** | `mreg:targetEntity` | enum-multi | multi | Top-level regulated entity. Values from closed list (Section 3.3). Semicolon-delimited. |
| 7 | **Target_Role** | Optional | `mreg:targetRole` | enum-multi | multi | Specific regulatory role of the target entity. Values from closed list (Section 3.3a). Semicolon-delimited. Particularly relevant for IMO instruments where applicability often addresses roles (Flag State, Port State, Company, Master). |
| 8 | **Target_Object@en** | Optional | `dcterms:subject` | text-multi | multi | Specific regulated object. Free text, verbatim from source. E.g., `"shipboard fittings and supporting hull structures"`. Semicolon-delimited. |
| 9 | **Ship_Type** | Conditional | `mreg:shipType` | enum-multi | multi | Ship/unit types from closed list (Section 3.4). Semicolon-delimited. **Fill if the source explicitly restricts ship type; leave blank otherwise.** |
| 10 | **Size_Threshold** | Conditional | `mreg:threshold` | structured-text-multi | multi | Quantitative applicability bounds. Format: `param op value unit`. E.g., `GT >= 500`; `L >= 90 m`. Semicolon-delimited. **Fill if the source states a quantitative threshold.** |
| 11 | **Qual_Predicate@en** | Optional | `mreg:qualPredicate` | text-multi | multi | Qualitative conditions not captured by Size_Threshold, Geographic_Scope, or Cargo_Substance. Free text. E.g., `"crosshead type engines"`. Semicolon-delimited. |
| 12 | **Geographic_Scope@en** | Conditional | `mreg:geographicScope` | text-multi | multi | Voyage type, navigational area, or jurisdictional scope. Near-verbatim from source. E.g., `"international voyage"`; `"polar waters"`; `"ships in ports of a Party"`. Semicolon-delimited. **Fill if the source explicitly restricts by voyage type, geographic area, or jurisdictional reach; leave blank otherwise.** |
| 13 | **Cargo_Substance@en** | Conditional | `mreg:cargoSubstance` | text-multi | multi | Cargo type or substance that defines or restricts applicability. Near-verbatim from source. E.g., `"dangerous goods in packaged form"`; `"noxious liquid substances in bulk"`; `"liquefied gases"`. Semicolon-delimited. **Fill if the source defines applicability by cargo or substance carried; leave blank otherwise.** |
| 14 | **Normative_Basis** | Optional | `dct:conformsTo` | text-multi | multi | External regulatory instruments that mandate or scope the requirement. E.g., `SOLAS II-1/3-8`; `IGC Code`; `MARPOL Annex VI`. Semicolon-delimited. For IMO instruments, this may reference parent conventions or enabling resolutions. |
| 15 | **Implements_Requirement** | Optional | `mreg:implementsRequirement` | text-multi | multi | Directed cross-source implementation link. Records which higher-level requirement this applicability record operationalizes. E.g., an IACS UR record may list `SOLAS II-1/3-8`; a KR Rule record may list `IACS UR A2` or `SOLAS II-1/3-8`. Semicolon-delimited. Captures the IMO → IACS → KR normative hierarchy. **Fill only when the source document contains an explicit, individual-article-level cross-reference (e.g., "in compliance with SOLAS II-1/3-8"). Do not infer implementation links from general statements that a rule set "reflects" or "is based on" international conventions. If no explicit cross-reference exists, leave blank and tag `[Phase 2: implements_mapping]` in Editor_Note.** |
| 16 | **Exclusion@en** | Conditional | `xkos:exclusionNote` | text-multi | multi | Explicit exclusion clauses, near-verbatim. E.g., `"high speed craft"`. Semicolon-delimited. **Fill if the source contains explicit exclusion language.** |
| 17 | **Trigger_Event** | Conditional | `mreg:triggerEvent` | text | single | Implementation milestone. E.g., `"ships contracted for construction on or after [date]"`. **Fill if stated in source.** |
| 18 | **Trigger_Date** | Conditional | `dct:temporal` | date (ISO 8601) | single | Date extracted from Trigger_Event. E.g., `2024-07-01`. **Fill if a date is extractable from Trigger_Event.** |
| 19 | **Normative_Status** | Optional | `mreg:normativeStatus` | enum | single | `mandatory`, `recommendatory`, `guidance`, `interpretive`, `discretionary`. See Section 3.7 for definitions and Section 3.7a for Source_Doc_Type-based default mapping. If the source text contains an explicit enforcement cue (e.g., "shall", "should", "may", "for guidance only"), that cue overrides the default. Shared value set with CONTROLLED_TERM instruction. |
| 20 | **Applicability_Status** | **Required** | (custom QA) | enum | single | Extraction confidence: `explicit` (clear, self-contained applicability statement in source), `partial` (source contains some but not all applicability information; missing elements left blank), `unclear` (source language is ambiguous or contradictory), `composite` (anchor text assembled from multiple source sections — each section recorded via `[source: Section X.X]` in Editor_Note). **`inferred` is not permitted in Phase 1** — inferred applicability belongs to Phase 2 reasoning. |
| 21 | **Source_Doc** | **Required** | `dcterms:source` | text | single | Document identifier per source family. See Section 3.8 for naming conventions. |
| 22 | **Source_Locator** | **Required** | (locator) | text | single | Section/paragraph/regulation location. E.g., `A2.0`, `Reg.3-4`, `Pt.3 Ch.1 Sec.1`. |
| 23 | **Editor_Note** | Optional | `skos:editorialNote` | text | single | Extraction rationale, QA comments, ambiguity flags, cross-source references for Phase 2. When a structured column value is sourced from a section outside Applicability_Text, record `[source: Section X.X]` here. |

> **Obligation**: **Required** = must always be filled; **Conditional** = fill if source contains the information; **Optional** = fill if available.

### 3.2 Interoperability with TRUE_DEF and CONTROLLED_TERM Records

When APPLICABILITY and TRUE_DEF records coexist in one sheet:

| Aspect | TRUE_DEF | APPLICABILITY | Resolution |
|:---|:---|:---|:---|
| **Discriminator** | `Record_Type` = `TRUE_DEF` | `Record_Type` = `APPLICABILITY` | `Record_Type` is the single discriminator field for both types |
| **Scope text** | `Scope_Note@en` (scope extracted from definition) | `Applicability_Text@en` (verbatim applicability statement, anchor field) | Both map to `skos:scopeNote` but serve different roles: Scope_Note captures scope embedded within a definition; Applicability_Text is the standalone anchor for structured decomposition |
| **Scheme** | `IMO`, `IACS`, `KR`, or `EU` | `IMO`, `IACS`, `KR`, or `EU` | Both record types now share the same Scheme value set |
| **TRUE_DEF-only columns** | prefLabel, altLabel, Definition, Scope_Note, Example filled | Left blank | Validation must be conditional on Record_Type |
| **APPLICABILITY-only columns** | Left blank | Target_Entity, Target_Role, Ship_Type, Size_Threshold, Geographic_Scope, Cargo_Substance, etc. filled | Validation must be conditional on Record_Type |

When APPLICABILITY and CONTROLLED_TERM records coexist:

| Aspect | APPLICABILITY | CONTROLLED_TERM | Resolution |
|:---|:---|:---|:---|
| **Discriminator** | `Record_Type` = `APPLICABILITY` | `Record_Type` = `CONTROLLED_TERM` | `Record_Type` is the single discriminator |
| **Source location** | Application/Scope section | Body text (normative requirements) | Non-overlapping source locations |
| **Scheme** | `IMO`, `IACS`, `KR`, `EU` | `IMO`, `IACS`, `KR`, `EU` | All four Scheme values shared |
| **CONTROLLED_TERM-only columns** | Left blank (Term_Category, Term_Subclass, etc.) | Filled per CONTROLLED_TERM instruction | Validation must be conditional on Record_Type |

### 3.3 Target_Entity Controlled Values

| Value | Description | Example Source |
|:---|:---|:---|
| `Ship` | Ship/vessel/unit design, construction, survey | IACS UR A2, SOLAS II-1, KR Pt.3 |
| `Equipment` | Equipment type approval, testing, certification | IACS UR A3, SOLAS II-2, KR Pt.6 |
| `Material` | Material manufacture, testing, certification | IACS UR W7, KR Pt.2 |
| `Engine` | Engine type approval, certification, testing | IACS UR M44, MARPOL Annex VI |
| `System` | Integrated shipboard systems | IACS UR E26, SOLAS V |
| `Personnel` | Welder and personnel qualification | IACS UR W32, STCW |
| `Software` | Onboard software approval | IACS UR L5 |
| `Service_Supplier` | NDT firms, service supplier approval | IACS UR W35 |
| `Certification_Scheme` | Manufacturer certification schemes | IACS UR Z26 |
| `Administration` | Government maritime authority (Flag State, Port State, or Coastal State in their regulatory capacity) | SOLAS I, MARPOL I |
| `Organization` | Companies, recognized organizations, port facilities | ISM Code, ISPS Code |
| `Cargo` | Cargo-related requirements (dangerous goods, grain, bulk cargoes) | IMDG Code, IMSBC Code |
| `Document_Record` | Certificates, plans, records, manuals | SOLAS I/Reg.12, ISM Code |

### 3.3a Target_Role Controlled Values

Use `Target_Role` when the regulated entity acts in a specific regulatory capacity. This is particularly common in IMO instruments.

| Value | Parent Entity | Description | Example Source |
|:---|:---|:---|:---|
| `Flag_State` | Administration | State whose flag the ship flies | SOLAS I, MARPOL I |
| `Port_State` | Administration | State exercising port state control | SOLAS XI-1, MOU instruments |
| `Coastal_State` | Administration | State with coastal jurisdiction | MARPOL I/Reg.6 |
| `Shipowner` | Organization | Registered owner of a ship | MLC 2006 |
| `Company_ISM` | Organization | Company as defined by ISM Code | ISM Code |
| `Master` | Personnel | Ship's master | SOLAS V, STCW |
| `Seafarer` | Personnel | Seafarers as defined by STCW/MLC | STCW, MLC 2006 |
| `Officer` | Personnel | Certified officers (deck/engine) | STCW Ch.II/III |
| `RO` | Organization | Recognized Organization (classification society acting on behalf of flag state) | SOLAS XI-1, RO Code |
| `Port_Facility` | Organization | Port facility (ISPS context) | ISPS Code |
| `Training_Provider` | Organization | Maritime training institution | STCW |
| `Manufacturer` | Organization | Equipment/material manufacturer | IACS UR Z26, KR Pt.2 |

### 3.4 Ship_Type Controlled Values

IMO does not provide universally applicable ship type definitions; each instrument uses its own specific descriptions. To avoid conflicting classifications, the common core list is limited to **regulatory-category types** that appear consistently across IMO conventions, IACS URs, and classification rules. Design/operational sub-types are placed in the extension taxonomy (Section 3.4a).

#### 3.4 Core List (Regulatory Categories)

| Value | Description |
|:---|:---|
| `All_Ships` | No ship type restriction (use only when explicitly stated) |
| `Passenger_Ship` | Ships carrying more than 12 passengers (SOLAS I/Reg.2(f)) |
| `Cargo_Ship` | Ships which are not passenger ships (SOLAS I/Reg.2(g)); note: each convention may further qualify by GT threshold and voyage type |
| `Oil_Tanker` | Tankers as defined by MARPOL Annex I |
| `Bulk_Carrier` | Bulk carriers as defined by SOLAS XII and IACS UR S |
| `Gas_Carrier` | Ships subject to the IGC Code |
| `Chemical_Tanker` | Ships subject to the IBC Code |
| `HSC` | High Speed Craft subject to the HSC Code |
| `MODU` | Mobile Offshore Drilling Units subject to the MODU Code |
| `Offshore_Unit` | Non-drilling offshore units (general regulatory category) |
| `Fishing_Vessel` | Fishing vessels subject to the Torremolinos Protocol / Cape Town Agreement |
| `Special_Purpose_Ship` | Ships engaged in special purposes (SPS Code) |
| `Conventional_Ship` | Displacement-type ships (as defined in specific IACS URs, e.g., UR A2) |
| `Nuclear_Ship` | Nuclear powered ships (SOLAS VIII) |

#### 3.4a Extension Taxonomy (Design/Operational Sub-Types)

The following values are **not part of the common core**. Use them only when a source document explicitly uses these specific terms, and record them in `Qual_Predicate@en` (there is no separate `Ship_Type_Ext` column in Phase 1). In Phase 2, these will be formalized as `skos:narrower` under the appropriate core type.

| Value | Parent Core Type | Description |
|:---|:---|:---|
| `Container_Ship` | Cargo_Ship | Dedicated container carriers |
| `General_Cargo` | Cargo_Ship | General dry cargo ships without specialized cargo systems |
| `RoRo` | Cargo_Ship (or Passenger_Ship for RoPax) | Ro-Ro cargo ships and Ro-Ro passenger ships |
| `Offshore_Support_Vessel` | Cargo_Ship | Platform supply vessels, anchor handling vessels, etc. |
| `FPSO` | Offshore_Unit | Floating Production Storage and Offloading units |
| `FSU` | Offshore_Unit | Floating Storage Units |
| `Pleasure_Yacht` | — | Yachts and pleasure craft |
| `Barge` | — | Non-self-propelled barges |

### 3.5 Concept_ID / URI Design

**General pattern**: `{Scheme}_{SourceKey}_APP_{SeqNo}`

- `Scheme`: `IMO`, `IACS`, `KR`, or `EU`
- `SourceKey`: Normalized source unit key (document-level or major-unit-level)
- `_APP_`: Fixed infix distinguishing applicability records from definition records
- `SeqNo`: Three-digit sequence number, local within that source unit

**Normalization rules** (shared across all three instructions — TRUE_DEF / APPLICABILITY / CONTROLLED_TERM). **Steps 1–5** are the shared core rules. **Steps 6–7** handle source-family-specific abbreviation patterns for IMO Codes and EU legislation:

| Step | Rule | Example |
|:---:|:---|:---|
| 1 | Replace dots, parentheses, and commas with underscores (or remove if at word boundary) | `Z10.1` → `Z10_1`; `Pt.3 Ch.1` → `Pt3_Ch1` |
| 2 | Replace `/` and `-` with `_` | `II-1/3-8` → `II_1_3_8` |
| 3 | Collapse consecutive underscores | `II__1` → `II_1` |
| 4 | Use UPPERCASE | `Pt3_Ch1` → `PT3_CH1` |
| 5 | Remove document-type prefix (already in pattern) | `UR S11A` → `S11A` |
| 6 | IMO Codes: use standard abbreviation | `FSS Code` → `FSS`, `ISM Code` → `ISM` |
| 7 | EU: year + number pattern | `Directive 2009/45/EC` → `DIR_2009_45` |

#### Examples by Source Family

| Source Family | Source Document | Concept_ID Example |
|:---|:---|:---|
| **IACS** | UR A2 | `IACS_A2_APP_001` |
| **IACS** | UR S11A | `IACS_S11A_APP_001` |
| **IACS** | UI SC123 | `IACS_UI_SC123_APP_001` |
| **IACS** | Rec 87 | `IACS_REC_87_APP_001` |
| **IACS** | PR 38 | `IACS_PR_38_APP_001` |
| **IMO** | SOLAS Ch.II-1, Reg.3-8 | `IMO_SOLAS_II_1_R3_8_APP_001` |
| **IMO** | MARPOL Annex VI | `IMO_MARPOL_AVI_APP_001` |
| **IMO** | IGC Code | `IMO_IGC_APP_001` |
| **IMO** | IBC Code Ch.1 | `IMO_IBC_CH1_APP_001` |
| **IMO** | STCW Ch.II | `IMO_STCW_II_APP_001` |
| **IMO** | ISM Code | `IMO_ISM_APP_001` |
| **IMO** | Load Line Convention | `IMO_LL_APP_001` |
| **KR** | Rules for Steel Ships, Pt.3 Ch.1 | `KR_STEEL_PT3_CH1_APP_001` |
| **KR** | Rules for FRP Ships, Pt.2 | `KR_FRP_PT2_APP_001` |
| **KR** | Guidance for Classification of Steel Ships | `KR_GSTEEL_APP_001` |
| **KR** | Rules for Mobile Offshore Units | `KR_MOU_APP_001` |
| **EU** | Directive 2009/45/EC | `EU_DIR_2009_45_APP_001` |
| **EU** | Regulation (EU) 2015/757 | `EU_REG_2015_757_APP_001` |

- In Phase 1, only the local ID (`Concept_ID`) is finalized. See **Appendix B** for the base URI pattern and namespace configuration.

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

### 3.7 Normative_Status Definitions (Shared with CONTROLLED_TERM)

| Value | Definition | Typical Source Context |
|:---|:---|:---|
| `mandatory` | Legally binding requirement; compliance is compulsory | IMO conventions, IACS UR, KR Rules |
| `recommendatory` | Formally recommended by the regulatory body; not legally binding | IMO resolutions, IACS Rec |
| `guidance` | Advisory or best-practice guidance | KR Guidance, IACS guidance notes |
| `interpretive` | Official interpretation of a mandatory requirement; clarifies application | IACS UI, KR Interpretations, IMO unified interpretations |
| `discretionary` | Left to the discretion of the Administration, classification society, or surveyor | Provisions with "may", "at society's discretion" |

### 3.7a Normative_Status Default by Source_Doc_Type

The global default `mandatory` is removed. Instead, the default is derived from `Source_Doc_Type`. If the source text contains an explicit enforcement cue, it overrides the default below.

| Source_Doc_Type | Default Normative_Status | Rationale |
|:---|:---|:---|
| `Convention` | `mandatory` | Binding upon ratification and entry into force |
| `Mandatory_Code` | `mandatory` | Made mandatory under parent convention |
| `Recommendatory_Code` | `recommendatory` | Advisory codes adopted by IMO |
| `Resolution` | *(leave blank)* | Case-by-case: may adopt mandatory code amendments or be purely recommendatory. Record rationale in Editor_Note |
| `Circular` | `recommendatory` | MSC/MEPC circulars are generally non-binding guidance |
| `UR` | `mandatory` | Minimum requirements to be incorporated into member society rules |
| `UI` | `interpretive` | Harmonised interpretation of existing requirements |
| `Rec` | `recommendatory` | Industry advice; not binding on member societies |
| `PR` | `mandatory` | Procedural requirements binding on member societies |
| `Rule` | `mandatory` | Classification rules with binding effect |
| `Technical_Rule` | `mandatory` | Binding technical rules for specific ship types/systems |
| `Guidance` | `guidance` | Recommended practice; non-mandatory |
| `Interpretation` | `interpretive` | Clarification of rules; KR explicitly marks these as non-mandatory |

> **Override rule**: When the source text contains explicit modal language ("shall" → `mandatory`, "should" / "is recommended" → `recommendatory`, "may" / "at society's discretion" → `discretionary`, "for guidance only" → `guidance`), that cue takes precedence over the Source_Doc_Type default. Record the override rationale in Editor_Note.

### 3.8 Source_Doc Naming Conventions

| Source Family | Pattern | Examples |
|:---|:---|:---|
| **IMO** | `{Convention/Code} {Chapter/Annex/Part}` | `SOLAS II-1`, `MARPOL Annex VI`, `IGC Code`, `STCW Ch.II`, `ISM Code`, `LL Convention` |
| **IACS** | `{DocType} {Series}{Number}` or `{DocType} {Number}` | `UR A2`, `UR S11A`, `UI SC123`, `Rec 87`, `PR 38` |
| **KR** | `KR {RuleSet} {Part/Chapter}` | `KR Rules Pt.3 Ch.1`, `KR Guidance Pt.7`, `KR FRP Rules Pt.2` |
| **EU** | `{InstrumentType} {Year}/{Number}/{Suffix}` | `Directive 2009/45/EC`, `Regulation (EU) 2015/757`, `Decision 2009/17/EC` |

---

## 4. Extraction Patterns — Applicability Decomposition

The `Applicability_Text@en` field is the anchor. The following patterns guide decomposition into structured columns.

### 4.1 Primary Extraction Patterns

| # | Pattern | Trigger phrase | Target Column |
|:---:|:---|:---|:---|
| A1 | Entity identification | "This UR applies to...", "Requirements for...", "These regulations apply to...", "This Part applies to..." | Target_Entity, Target_Object |
| A1a | Role identification | "The Administration shall...", "Each Contracting Government...", "The Company shall ensure..." | Target_Role |
| A2 | Ship type restriction | "all [ship type]", "ships of type...", "every oil tanker..." | Ship_Type |
| A3 | Quantitative threshold | "of [N] [unit] and above", ">= [N]", "[N] or more" | Size_Threshold |
| A4 | Qualitative condition | "where [condition]", "fitted with...", "intended for..." | Qual_Predicate |
| A4a | Geographic/voyage scope | "engaged in international voyages", "operating in polar waters", "in ports of a Party", "within special areas" | Geographic_Scope |
| A4b | Cargo/substance scope | "carrying dangerous goods", "noxious liquid substances in bulk", "liquefied gases", "INF cargo" | Cargo_Substance |
| A5 | Normative reference | "per SOLAS...", "subject to [Convention]", "as required by..." | Normative_Basis |
| A5a | Implementation link | "implements [Regulation]", "in compliance with [UR]", "as required by [Convention]" | Implements_Requirement |
| A6 | Exclusion clause | "not applicable to...", "excluding...", "does not apply to...", "other than..." | Exclusion |
| A7 | Implementation clause | "ships contracted for construction on or after...", "keel laid on or after...", "entry into force [date]" | Trigger_Event + Trigger_Date |
| A8 | Enforcement qualifier | "guidance only", "at society's discretion", "may be considered", "should", "is recommended" | Normative_Status |

### 4.2 Capture-in-Phase-1 / Reason-in-Phase-2 Patterns

The following patterns involve source-internal applicability semantics that must be **captured** (recorded in structured columns or Editor_Note) in Phase 1, even though full cross-source **reasoning** is deferred to Phase 2.

| # | Pattern | Phase 1 Action |
|:---:|:---|:---|
| A11 | Conditional override | "unless the flag Administration determines otherwise" → Record the override condition in `Qual_Predicate@en` and tag `[Phase 2: unless]` in Editor_Note |
| A12 | Retrospective applicability | "existing ships built before [date]" → Record in `Trigger_Event` / `Trigger_Date` with qualifier "existing ships" and tag `[Phase 2: retrospective]` in Editor_Note |
| A15 | Transitional provision | "ships complying with [old regulation] need not comply until [date]" → Record the transitional date in `Trigger_Event` / `Trigger_Date` and tag `[Phase 2: transitional]` in Editor_Note |

### 4.3 Fully Deferred Patterns (Phase 2)

When patterns belonging to Phase 2 (A9, A10, A13, A14: supersession, hybrid split, alternative rule, equivalence) are encountered, tag them as `[Phase 2: {tag}]` in Editor_Note and move on. See **Appendix D** for the detailed pattern table.

---

## 5. Multi-Value Encoding

All multi-valued columns use **semicolon (`;`)** as delimiter.

```
Size_Threshold:        GT >= 500; L >= 90 m; Cb 0.55-0.90
Geographic_Scope@en:   international voyage; polar waters
Cargo_Substance@en:    dangerous goods in packaged form; noxious liquid substances in bulk
Exclusion@en:          CSR bulk carriers; high speed craft; special purpose ships
Ship_Type:             Oil_Tanker; Chemical_Tanker
Implements_Requirement:  SOLAS II-1/3-8; IMO Res.MSC.474(102)
```

For `Size_Threshold`, two formats are permitted:
- **Comparator form**: `{parameter} {operator} {value} {unit}` — for single-bound thresholds
- **Range form**: `{parameter} {low}-{high} {unit}` — for bounded ranges

Both forms are valid and may coexist within the same record (semicolon-delimited).

| Parameter | Abbreviation | Example |
|:---|:---|:---|
| Gross tonnage | `GT` | `GT >= 500` |
| Length | `L` | `L >= 90 m` |
| Cylinder bore | `bore` | `bore >= 200 mm` |
| Power output | `kW` | `kW > 37` |
| Crankcase volume | `V_cc` | `V_cc >= 0.6 m3` |
| Plate thickness | `t` | `t > 50 mm` |
| Cargo density | `rho_c` | `rho_c >= 1.0 t/m3` |
| Range | — | `L 90-500 m` |
| Deadweight tonnage | `DWT` | `DWT >= 20000` |
| Number of persons | `N_persons` | `N_persons > 12` |

---

## 6. Editorial Rules (Phase 1 Summary)

| Rule | Content |
|:---|:---|
| Language | English only (data cells). Korean permitted only in internal notes |
| Spelling | British English (moulded, vapour, draught, centre, programme). **TSV column headers use `@en` for simplicity. When converting to RDF, all English-language literals shall carry the `@en-GB` tag (BCP 47 compliant).** This two-layer approach avoids header verbosity while preserving dialect precision in the final RDF output |
| Applicability_Text | Preserve original wording. Minor normalization allowed (remove line breaks, fix OCR artefacts). Must include all passages from which structured column values are extracted |
| Structured columns | Derived from Applicability_Text. Must be traceable back to anchor text |
| Source citation | Separate Source_Doc and Source_Locator. Do not use `§` symbol. Follow naming conventions in Section 3.8 |
| Enum values | Use exact values from Section 3.3, 3.3a, 3.4, 3.6, 3.7. If no match, use closest value + flag in Editor_Note |
| Empty cells | Leave blank if information not present. Do not default or infer |
| Cross-source linking | Use `Implements_Requirement` for directed hierarchy links. Do not duplicate the same information in `Normative_Basis` and `Implements_Requirement` — use `Normative_Basis` for cited external references, `Implements_Requirement` for directed implementation relationships. **Implements_Requirement must be backed by an explicit, article-level cross-reference in the source text. General statements that a rule set "reflects" or "incorporates" international conventions do not qualify — leave blank and defer to Phase 2 mapping** |

---

## 7. Procedure

```
Step 1   Open the target source document
         - IACS: UR/UI/Rec/PR document (from respective chunk directories)
         - IMO: Convention/Code chapter or regulation text
         - KR: Rules/Guidance Part or Chapter
Step 2   Locate the "Application", "Scope", or "General" section
         - IMO: Regulation preamble or "Application" article
         - KR: Part/Chapter scope clause (typically Section 1)
Step 3   Copy the full applicability statement -> Applicability_Text@en
         (include all paragraphs containing scope, threshold, exclusion,
          and implementation date information)
Step 4   Apply Admission Rule — confirm this is an applicability statement
Step 5   Assign Concept_ID per Section 3.5 rules
         Set Record_Type = APPLICABILITY
         Set Scheme = IMO | IACS | KR | EU (as appropriate)
         Set Source_Doc_Type per Section 3.6
Step 6   Decompose Applicability_Text using Patterns A1-A8 (Section 4.1)
         -> Fill Target_Entity, Target_Role, Target_Object, Ship_Type,
            Size_Threshold, Qual_Predicate, Geographic_Scope,
            Cargo_Substance, Normative_Basis, Implements_Requirement,
            Exclusion, Trigger_Event, Trigger_Date, Normative_Status
Step 7   Verify anchor traceability — every structured value must trace
         back to a phrase in Applicability_Text@en. If not, extend the
         anchor text or record [source: Section X.X] in Editor_Note
Step 8   Capture A11/A12/A15 patterns in structured columns + Editor_Note
         (Section 4.2); tag fully deferred A9/A10/A13/A14 in Editor_Note
         only (Section 4.3)
Step 9   Assign Applicability_Status (explicit/partial/unclear/composite)
Step 10  Record Source_Doc / Source_Locator per Section 3.8
Step 11  Verify (Section 8)
```

---

## 8. Verification

### 8.1 2-Pass Review

| Pass | Focus | Check items |
|:---|:---|:---|
| **Structural** | Table integrity | Column count consistency (23 columns), Required-field empty cell check (Optional/Conditional fields may be blank per obligation rules), no duplicate Concept_ID, valid enum values, `_APP_` infix present, Record_Type = `APPLICABILITY`, Scheme matches source family |
| **Semantic** | Content correctness | Applicability_Text = source-faithful, structured columns traceable to anchor text, no information fabricated, Size_Threshold format valid, Trigger_Date is ISO 8601, Implements_Requirement captures correct hierarchy direction |

### 8.2 Cross-Check Rules

| Rule | Check | Severity |
|:---|:---|:---|
| Anchor traceability | Every non-empty structured column value must be traceable to a phrase in Applicability_Text@en. If sourced from elsewhere, Editor_Note must contain `[source: Section X.X]` | **Error** |
| Enum validation | Target_Entity values must be from Section 3.3 list | **Error** |
| Target_Role validation | Target_Role values must be from Section 3.3a list | **Error** |
| Ship_Type validation | Ship_Type values must be from Section 3.4 core list. Extension types (Section 3.4a) must not appear in Ship_Type column — record in Qual_Predicate@en instead | **Error** |
| Source_Doc_Type validation | Source_Doc_Type values must be from Section 3.6 list | **Error** |
| Normative_Status validation | Normative_Status values must be from Section 3.7 list | **Error** |
| Threshold format | Size_Threshold must match either comparator form (`param op value unit`) or range form (`param low-high unit`) per Section 5 | **Warning** |
| Date format | Trigger_Date must be ISO 8601 (YYYY-MM-DD) | **Error** |
| Geographic_Scope conditional fill | Geographic_Scope must be filled when source contains voyage type, geographic area, or jurisdictional scope phrases | **Warning** |
| Cargo_Substance conditional fill | Cargo_Substance must be filled when source defines applicability by cargo or substance carried | **Warning** |
| Completeness | At minimum, Concept_ID + Record_Type + Scheme + Source_Doc_Type + Applicability_Text + Target_Entity + Source_Doc + Source_Locator + Applicability_Status must be filled | **Error** |
| Exclusion source check | Every Exclusion entry must correspond to an explicit "not applicable" / "excluding" phrase in source | **Error** |
| Duplicate detection | Same Source_Doc + Source_Locator should not produce duplicate records unless distinct scope blocks | **Warning** |
| Conditional fill check | Conditional columns must be filled when corresponding trigger phrases (Section 4.1) are present in Applicability_Text | **Warning** |
| Record_Type-conditional validation | APPLICABILITY-only columns must not appear in TRUE_DEF records; TRUE_DEF-only columns must not appear in APPLICABILITY records | **Error** |
| Concept_ID prefix check | Concept_ID prefix must match Scheme value (`IMO_`, `IACS_`, `KR_`, `EU_`) | **Error** |
| Source family consistency | Scheme value must be consistent with Source_Doc naming (e.g., Scheme=`IMO` must have IMO-style Source_Doc) | **Error** |
| Implements directionality | Implements_Requirement should reference a higher-level source (IMO/EU > IACS > KR), not lower | **Warning** |
| Implements explicit basis | Implements_Requirement must be backed by an explicit article-level cross-reference in the source text, not inferred from general "reflects/incorporates" statements | **Error** |

> **SHACL note**: Section 8.2 cross-check rules are the normative validation specification. SHACL shapes for automated validation will be generated from these rules in Phase 2 — no separate SHACL table is maintained in this document.

---

## 9. Namespace Prefixes

Column-to-property mappings are specified in the SKOS/DC Mapping column of Section 3.1. See **Appendix B** for Turtle prefix declarations and detailed descriptions.

---

## 10. Worked Example (Quick Reference)

Below is an abbreviated example showing only the key workflow. See **Appendix C** for detailed examples per source family (full 23-column records for IACS/IMO/KR).

### IACS UR A2 — Abbreviated

| Column | Value |
|:---|:---|
| Concept_ID | `IACS_A2_APP_001` |
| Scheme / Source_Doc_Type | `IACS` / `UR` |
| Applicability_Text@en | *(verbatim from A2.0–A2.2: includes entity, threshold, exclusion, trigger date)* |
| Target_Entity | `Ship` |
| Ship_Type | `Conventional_Ship` |
| Size_Threshold | `GT >= 500` |
| Exclusion@en | `high speed craft; special purpose ships; offshore units` |
| Trigger_Date | `2022-01-01` |
| Source_Doc / Source_Locator | `UR A2` / `A2.0, A2.1, A2.2` |

> **Key point**: Apply patterns to Applicability_Text in order: entity (A1) → ship type (A2) → threshold (A3) → exclusion (A6) → trigger (A7).

---

## 11. Source Family Quick Reference

| Aspect | IMO | IACS | KR | EU |
|:---|:---|:---|:---|:---|
| **Source_Doc_Type** | Convention, Mandatory_Code, Resolution, Circular | UR, UI, Rec, PR | Rule, Guidance, Interpretation | Directive, Regulation_EU, Decision |
| **Default Enforcement** | Per Source_Doc_Type (Section 3.7a): Convention/Mandatory_Code → `mandatory`; Recommendatory_Code/Circular → `recommendatory`; Resolution → blank | Per Source_Doc_Type (Section 3.7a): UR/PR → `mandatory`; UI → `interpretive`; Rec → `recommendatory` | Per Source_Doc_Type (Section 3.7a): Rule/Technical_Rule → `mandatory`; Guidance → `guidance`; Interpretation → `interpretive` | Directive/Regulation_EU → `mandatory`; Decision → context-dependent |
| **Target_Role usage** | High (Flag_State, Port_State, Company, Master) | Low | Low | Medium (Flag_State, Shipowner, Company) |
| **Implements_Requirement** | Usually blank (top-level) | References IMO (explicit article-level cross-ref only) | Fill only when explicit article-level cross-ref exists; otherwise defer to Phase 2 | References IMO conventions where applicable |
| **Granularity** | Regulation or article | One document (UR, UI, Rec, or PR) | Lowest autonomous applicability clause (often Section-level, e.g., `Sec.1 101 Application`) | Article-level scope clause |

---

## 12. Output Specification

All final output files are saved to the **`results/`** subdirectory under the working directory from which the instruction is executed. Per-chunk intermediate files (partial TSV and log files produced during segmented processing) are saved to **`results/temp/`**. Both directories shall be created automatically if they do not exist. Each extraction run produces exactly **3 final files** in `results/`: one result file, one summary file, and one log file. Intermediate files in `results/temp/` are retained for traceability but are not considered deliverables.

### 12.1 File Naming Convention

| File | Name Pattern | Description |
|:---|:---|:---|
| **Result** | `phase1_applicability_result.tsv` | Final extraction table in TSV format (Tab-Separated Values). Contains all extracted records conforming to the Target Schema (Section 3). One header row + data rows. UTF-8 with BOM. |
| **Summary** | `phase1_applicability_summary.md` | Extraction summary report in Markdown format. |
| **Log** | `phase1_applicability_log.md` | Processing log in Markdown format. |

### 12.2 Result File (`phase1_applicability_result.tsv`)

- **Format**: TSV (Tab-Separated Values), UTF-8 with BOM
- **Header row**: Column names exactly as defined in Section 3.1, tab-delimited
- **Column order**: `Concept_ID	Record_Type	Scheme	Source_Doc_Type	Applicability_Text@en	Target_Entity	Target_Role	Target_Object@en	Ship_Type	Size_Threshold	Qual_Predicate@en	Geographic_Scope@en	Cargo_Substance@en	Normative_Basis	Implements_Requirement	Exclusion@en	Trigger_Event	Trigger_Date	Normative_Status	Applicability_Status	Source_Doc	Source_Locator	Editor_Note`
- **Empty cells**: Leave blank (no placeholder text such as "N/A" or "-")
- **Multi-value delimiter**: Semicolon (`;`) within a cell, as per Section 3.1
- **Quoting**: Fields containing tabs, newlines, or double quotes must be enclosed in double quotes. Embedded double quotes are escaped as `""`
- **Sort order**: By `Source_Doc` (ascending), then by `Source_Locator` (document order)

### 12.3 Summary File (`phase1_applicability_summary.md`)

The summary file shall contain the following sections:

```markdown
# Phase 1 APPLICABILITY Extraction Summary

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

## Records by Applicability_Status
| Status | Count |
|:---|---:|
| explicit | {n} |
| partial | {n} |
| unclear | {n} |
| composite | {n} |

## Quality Flags
- Phase 2 backlog items: {count}
- Editor_Note flags: {count}
- Anchor traceability errors: {count}

## Issues / Observations
- {free text: notable decisions, ambiguities, deferred items}
```

### 12.4 Log File (`phase1_applicability_log.md`)

The log file records the sequential processing trace:

```markdown
# Phase 1 APPLICABILITY Processing Log

## {Source_Doc} — {Section/Chapter}
- **Segment**: {segment number} / {total segments}
- **Tokens (approx)**: {n}K
- **Records extracted**: {count}
- **Decisions**:
  - {source clause}: Admitted / Excluded — {reason}
  - ...
- **Flags**:
  - {Concept_ID}: {flag description}
  - ...
```

### 12.5 Overwrite Rule

Each new extraction run **overwrites** the previous final output files in `results/` and all intermediate files in `results/temp/`. If incremental preservation is needed, the user must rename or archive prior files before initiating a new run.

---

## 13. Phase 1.1 — Validation Exception Management

When recurring comments are identified during iterative validation of Phase 1 outputs, they are escalated to Phase 1.1 for systematic resolution. Phase 1.1 is **not** an additional extraction phase — it is a QA exception layer.

**Full specification**: See [`phase1_1_validation_exception_guide.md`](phase1_1_validation_exception_guide.md) (shared across all three Phase 1 instructions).

**Escalation criteria (summary)**:
- Comment recurs 2+ times or across 2+ documents/records
- Issue blocks validator pass
- Current guide text is ambiguous — reviewers disagree on correct action
- Phase 1 / Phase 2 boundary is unclear

**Key difference from Phase 1 overwrite rule**: The Phase 1.1 issue register is **versioned and never overwritten** (`results/phase1_1/phase1_1_issue_register_{date}_v{NN}.tsv`).

---

## 14. Phase 2 Preview

See **Appendix A** for the full list of Phase 2 deferred items. The deferred tags (`[Phase 2: ...]`) from Section 4.2 serve as Phase 2 entry points. Items with `defer_phase2` disposition from Phase 1.1 are also Phase 2 entry candidates.

| Item | Description |
|:---|:---|
| Broader/Related assignment | Assign `skos:broader` and `skos:related` relationships |
| Frequency/Fitness assessment | Assess term frequency and controlled-vocabulary fitness |

---

*Phase 1 scope: Source-faithful applicability extraction from **IMO, IACS, KR, and EU** instruments, structured decomposition into 23 columns (including Geographic_Scope and Cargo_Substance), stable ID with `{Scheme}_..._APP_` pattern, verbatim anchor text with full traceability, Record_Type discriminator, Source_Doc_Type classification, Target_Role identification, Implements_Requirement for cross-source hierarchy, Phase 1 capture of A11/A12/A15 patterns (override, retrospective, transitional). Output: 3 final files (result TSV + summary MD + log MD) in `results/`, intermediate chunk files in `results/temp/`.*

---
---

# Appendices

## Appendix A — Phase 2 Preview (Deferred Items)

Items deferred to Phase 2: cross-source reasoning (`superseded_by`, `overrides_if`, `hybrid_split`), cross-source mapping (`skos:closeMatch`/`exactMatch`), formal Boolean applicability logic, temporal chain resolution, full retrospective/transitional/override **reasoning** (Phase 1 captures raw data per Section 4.2; Phase 2 performs chain resolution), SKOS ConceptScheme URIs for enums, equivalence/exemption, SHACL automated validation, TRUE_DEF-APPLICABILITY linking, `Interprets_Requirement` column, Normative_Force/Decision_Modality split, **`Applicability_Status = inferred`** (context-derived applicability permitted only after Phase 2 reasoning).

---

## Appendix B — Base URI Pattern & Namespace Prefixes

### Base URI

- Pattern: `https://{domain}/maritime-cv/{Concept_ID}`
- `{Concept_ID}` is the **full** Concept_ID value including the Scheme prefix (e.g., `IACS_A2_APP_001`, not just `A2_APP_001`). The Scheme prefix is part of the URI to ensure global uniqueness.
- E.g., `https://example.org/maritime-cv/IACS_A2_APP_001`
- E.g., `https://example.org/maritime-cv/IMO_SOLAS_II_1_R3_8_APP_001`
- E.g., `https://example.org/maritime-cv/KR_STEEL_PT3_CH1_APP_001`

### Namespace Prefixes

```turtle
@prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
@prefix dct:   <http://purl.org/dc/terms/> .
@prefix xkos:  <http://rdf-vocabulary.ddialliance.org/xkos#> .
@prefix mreg:  <https://example.org/maritime-cv/> .
```

> Column-to-property mappings are specified in the SKOS/DC Mapping column of Section 3.1.
> `xkos:exclusionNote` is a sub-property of `skos:scopeNote`. The `mreg:` (maritime regulation) prefix is the project-wide custom namespace covering all source families (IMO, IACS, KR, EU).

---

## Appendix C — Worked Examples (Full Detail)

Below, only **key differentiating columns** are shown. Columns with default or blank values are omitted. Full 23-column records follow Section 3.1.

### C.1 IACS UR A2 (Source: A2.0–A2.2)

> "This UR is to apply to design and construction of shipboard fittings and supporting structures used for the normal towing and mooring operations of conventional ships. Conventional ships means new displacement-type ships of 500 GT and above, excluding high speed craft, special purpose ships, and offshore units of all types. This UR applies to ships subject to SOLAS regulation II-1/3-4. Ships contracted for construction on or after 1 January 2022..."

| Column | Value |
|:---|:---|
| Concept_ID | `IACS_A2_APP_001` |
| Scheme / Source_Doc_Type | `IACS` / `UR` |
| Target_Entity | `Ship` |
| Target_Object@en | `shipboard fittings and supporting hull structures` |
| Ship_Type | `Conventional_Ship` |
| Size_Threshold | `GT >= 500` |
| Normative_Basis | *(left blank — same reference recorded in Implements_Requirement; do not duplicate per Section 6 rule)* |
| Implements_Requirement | `SOLAS II-1/3-4` |
| Exclusion@en | `high speed craft; special purpose ships; offshore units; escort towing; canal transit towing; emergency towing for tankers` |
| Trigger_Date | `2022-01-01` |
| Source_Doc / Source_Locator | `UR A2` / `A2.0, A2.1, A2.2` |
| Editor_Note | `UR A2 Rev.5 (Sep 2020) original text cites "SOLAS regulation II-1/3-4" — retained verbatim per source-faithful principle. However, II-1/3-4 covers emergency towing arrangements for tankers; the safe mooring regulation for towing and mooring equipment (GT >= 3000, 2024-01-01) is II-1/3-8 added by MSC.474(102). [Phase 2: verify whether A2 subsequent revisions update the SOLAS cross-reference from II-1/3-4 to II-1/3-8; consider splitting emergency towing scope as separate APP record]` |

### C.2 IMO SOLAS II-1/Reg.3-8

> "Ships of 3,000 gross tonnage and above, constructed on or after 1 January 2024, shall be provided with arrangements for towing and mooring equipment..."

| Column | Value |
|:---|:---|
| Concept_ID | `IMO_SOLAS_II_1_R3_8_APP_001` |
| Scheme / Source_Doc_Type | `IMO` / `Convention` |
| Target_Entity | `Ship` |
| Target_Object@en | `towing and mooring equipment; shipboard fittings and supporting hull structures` |
| Size_Threshold | `GT >= 3000` |
| Trigger_Date | `2024-01-01` |
| Source_Doc / Source_Locator | `SOLAS II-1` / `Reg.3-8` |
| Editor_Note | `Added by MSC.474(102) — safe mooring provisions. II-1/3-4 is a separate regulation covering emergency towing arrangements for tankers. [Phase 2: cross-source link to IACS_A2_APP_001]` |

### C.3 KR Rules for Steel Ships (Pt.3 Ch.1 Sec.1)

> "The requirements in this Chapter apply to the hull structural design and construction of steel ships of 90 m in length and above, intended for unrestricted ocean service..."

| Column | Value |
|:---|:---|
| Concept_ID | `KR_STEEL_PT3_CH1_APP_001` |
| Scheme / Source_Doc_Type | `KR` / `Rule` |
| Target_Entity | `Ship` |
| Target_Object@en | `hull structural design and construction` |
| Size_Threshold | `L >= 90 m` |
| Qual_Predicate@en | `steel ships; unrestricted ocean service` |
| Source_Doc / Source_Locator | `KR Rules Pt.3 Ch.1` / `Sec.1` |
| Editor_Note | `Ships <90m redirected to Pt.11. [Phase 2: alternative_rule] [Phase 2: implements_mapping — KR states rules reflect SOLAS and IACS UR but no article-level cross-reference in this scope clause]` |

---

## Appendix D — Deferred Patterns Detail (A9–A15)

| # | Pattern | Action |
|:---:|:---|:---|
| A9 | Cross-source supersession | "supersedes UR X", "replaces UR Y", "amends Regulation Z" -> Tag `[Phase 2: superseded_by]` in Editor_Note |
| A10 | Hybrid split | "for single skin holds apply Z10.2, for double skin holds apply Z10.5" -> Tag `[Phase 2: hybrid_split]` |
| A11 | Conditional override | "unless the flag Administration determines otherwise" -> **Phase 1 capture**: record override condition in `Qual_Predicate@en` + tag `[Phase 2: unless]` in Editor_Note |
| A12 | Retrospective applicability | "existing ships built before [date]" -> **Phase 1 capture**: record in `Trigger_Event`/`Trigger_Date` with "existing ships" qualifier + tag `[Phase 2: retrospective]` in Editor_Note |
| A13 | Alternative rule | "if excluded, apply IGC Code requirements instead" -> Tag `[Phase 2: alternative_rule]` in Editor_Note |
| A14 | Equivalence / exemption | "equivalent arrangement as accepted by the Administration" -> Tag `[Phase 2: equivalence]` in Editor_Note |
| A15 | Transitional provision | "ships complying with [old regulation] need not comply until [date]" -> **Phase 1 capture**: record transitional date in `Trigger_Event`/`Trigger_Date` + tag `[Phase 2: transitional]` in Editor_Note |
