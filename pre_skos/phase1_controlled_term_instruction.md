# Phase 1: CONTROLLED_TERM Controlled Vocabulary Work Instruction (Unified)

> **Pre-SKOS Phase**: This is a preparatory step for building SKOS `skos:broader` / `skos:related` hierarchical and associative relationships in Phase 2. Phase 1 focuses on source-faithful term extraction and flat-table cataloguing; formal SKOS semantic relations are constructed in the subsequent phase.

> **Scope**: Extract and catalogue normative action terms, process terms, role terms, equipment terms, and operational terms that function as controlled vocabulary candidates across maritime regulatory documents — excluding terms already covered by TRUE_DEF (formal definitions) and APPLICABILITY (scope/application statements).
> The goal is to capture **what actions are prescribed, by what methods, through what processes, by which actors, and with what equipment** across the regulatory corpus, using a flat-table format compatible with TRUE_DEF and APPLICABILITY records.
> Full ontology modelling (OWL classes, SKOS-XL, cross-source mapping) is deferred to Phase 2.
> **Work Procedure**: Read and process all source texts sequentially.
> **Work Preparation**: When the user requests a review, divide the target material into segments of approximately 100K tokens and process them sequentially.
> **Architecture**: This instruction consists of a **Common Core** (Sections 1-9) applicable to all source families, plus **Source-Family Annexes** (A-E) providing document-specific extraction guidance.
---

## 0. Prerequisites

A preparatory step where the LLM and user jointly review the target document and extract baseline data. Each instruction (TRUE_DEF, APPLICABILITY, CONTROLLED_TERM) is executed independently.

1. **Document review** — Read the target document and analyse anchor terms, classification structure, and definition boundaries.
2. **Extraction scoping** — Extract normative terms from the body text (excluding Definitions and Scope/Application sections). Save extracted sentences to the intermediate directory (`results/temp/`).
3. **Pattern cataloguing** — Analyse the extracted sentences from Step 2 and compile a pattern catalogue (`results/temp/extraction_patterns_controlled_term.tsv`). Record recurring sentence structures (e.g., `"shall be carried out"`, `"is to be submitted for approval"`, `"shall be fitted with"`, equipment/test/survey names in prescriptive context). This catalogue serves two purposes: (a) the separation script can use the patterns to **auto-flag potential omissions** in the remainder, and (b) patterns can be reused for **cross-instruction classification checks** (e.g., detecting a TRUE_DEF-type or APPLICABILITY-type sentence mistakenly included in CONTROLLED_TERM extraction).
4. **Extraction separation** — Run a separation script against the source document and the extracted sentences in `results/temp/` to produce two outputs: (a) **extracted sentences** (matched) and (b) **non-extracted sentences** (unmatched remainder). The script also applies the pattern catalogue from Step 3 to flag remainder sentences that match known controlled-term patterns as **omission candidates**. The LLM performs the initial extraction (Step 2); the separation and pattern matching are performed by script to ensure mechanical completeness.
5. **Extraction verification** — The LLM reviews the non-extracted sentences (unmatched remainder from Step 4), with priority on script-flagged omission candidates, to verify that no required normative term sentences were missed. If omissions are found, add them to the extracted set, update the pattern catalogue if a new pattern is identified, and re-run the separation script.

> Findings during analysis may require updates to the TRUE_DEF or APPLICABILITY instructions.

---

## 1. Admission Rule

| Condition | Include | Exclude (Phase 2 backlog) |
|:---|:---|:---|
| Source location | Body text, normative annexes, tables — any section **outside** the formal "Definitions" and "Application/Scope" sections (see Annex mapping for source-specific section names) | Formal "Definitions" section (-> TRUE_DEF); "Application/Scope" section (-> APPLICABILITY) |
| Record type | **CONTROLLED_TERM** only | TRUE_DEF, APPLICABILITY, DESCRIPTION, PARAPHRASE |
| Term category | Action/procedure terms, test/survey types, approval/certification acts, manufacturing/quality processes, normative expression patterns, actor/role terms, **safety equipment/systems, environmental controls, training/competency terms, security measures, operational procedures** | Pure technical parameters (formulas, coefficients), material grade designations (Grade A, D36, etc.), ship type names (already in APPLICABILITY Ship_Type enum), **statutory tonnage formulas, PSC administrative codes, equipment class designations (Class A/B/C)** |
| Source | **IMO** Conventions/Codes/Resolutions/Circulars (active instruments); **IACS** UR/UI/Rec (active documents); **KR** Rules/Guidance (current editions); **EU** Directives/Regulations/Decisions (in force) | Withdrawn-before-effective documents; superseded amendments where consolidated version exists |
| Language | English only (data cells) | Replace Korean text with English |

### 1.1 Source-Specific Exclusion Mapping

| Source Family | "Definitions" Section Equivalent | "Scope" Section Equivalent |
|:---|:---|:---|
| **IACS UR/UI** | "Definitions" section | "Application" / "Scope" section |
| **IMO Conventions** | "Definitions" regulation (e.g., SOLAS Reg. 2, MARPOL Reg. 1) | "Application" regulation (e.g., SOLAS Reg. 1) |
| **IMO Codes** | "Definitions" chapter/section | "General" / "Application" chapter |
| **EU Legislation** | "Definitions" article (typically Art. 2) | "Subject matter and scope" article (typically Art. 1) |
| **KR Rules** | "Definitions" article within each Section | "Application" article (e.g., Sec.1 101) |

### 1.2 Document Status Filtering

| Source Family | Active Document Rule |
|:---|:---|
| **IMO Conventions** | Use latest consolidated text; individual amendments only if not yet consolidated |
| **IMO Codes** | Use current edition; include adopted-but-not-yet-effective amendments with Editor_Note tag |
| **IMO Resolutions** | Exclude revoked resolutions; include superseding resolution only |
| **IMO Circulars** | Exclude superseded circulars; use latest revision |
| **IACS** | Active documents only; exclude withdrawn-before-effective |
| **KR** | Current edition only |
| **EU** | In-force instruments; exclude repealed directives/regulations |

### 1.3 One-Line Decision

Is the term a normative action, process, method, equipment, role, or operational term used in prescriptive or recommendatory context (with shall/is to be/should/must/recommends) and **not** already captured by TRUE_DEF or APPLICABILITY? — **Yes -> adopt**, No -> skip.

> **Note**: For recommendatory sources (Resolutions, Circulars), terms using "should"/"recommends" are also admitted, tagged with `Normative_Status = recommendatory`.

---

## 2. Core Principles

### 2.1 Source-Specific Extraction

- **Register each term as encountered in the source document.** If the same term appears with distinct usage in different source documents, register separately.
- Cross-source harmonisation (prefLabel unification, exactMatch/closeMatch) is performed in Phase 2.

### 2.2 Method vs Stage Separation

- **Do not conflate test/inspection methods with certification stages.** A term like "hydrostatic test" is a method; "factory acceptance test" is a stage. Record them in separate `Term_Subclass` values.
- This principle applies equally to survey types: "close-up survey" is a scope/extent; "special survey" is a periodic interval.

### 2.3 Actor vs Role Separation

- **Separate organisational entities from the roles they play.** "Classification Society" is an actor; "Approving Authority" is a role.
- Record actors in `Term_Category = Actor` and roles in `Term_Category = Role`.

### 2.4 Verbatim-First, Then Normalise

- **Extract the term as it appears in the source** (verbatim form -> `Source_Form@en`).
- **Assign a normalised preferred label** (`prefLabel@en`) following the Label Policy (Section 5).
- Both forms are preserved; the normalised form is for controlled vocabulary use.

### 2.5 Equipment vs System Separation (New)

- **Distinguish individual equipment items from integrated systems.** "Smoke detector" is equipment; "fire detection system" is a system comprising multiple equipment items.
- Record in `Term_Category = Safety_Equipment` with appropriate `Term_Subclass`.

### 2.6 Normative Status Preservation (New)

- **Preserve the normative force of the source.** Mandatory instruments ("shall") and recommendatory instruments ("should"/"recommends") are both admitted but must be distinguished via the `Normative_Status` field.
- Do not normalise "should" to "shall" or vice versa.

---

## 3. Target Schema

```
Concept_ID | Record_Type | Scheme | Source_Doc_Type | Term_Category | Term_Subclass | Domain_Facet | prefLabel@en | altLabel@en | Source_Form@en | Definition_Context@en | Deontic_Pattern@en | Normative_Status | Source_Doc | Source_Locator | Editor_Note
```

### 3.1 Column Definitions with Obligation

| # | Column | Obligation | SKOS/DC Mapping | Data Type | Cardinality | Rule |
|:---:|:---|:---:|:---|:---|:---|:---|
| 1 | **Concept_ID** | **Required** | URI fragment | ID | single | Format: `{Scheme}_{SourceKey}_CT_{SeqNo}`. See Section 3.5 for source-family patterns. **Once assigned, never renumbered; gaps permitted.** Normalization: remove dots/parentheses, replace `/` with `_`. |
| 2 | **Record_Type** | **Required** | `dct:type` | enum | single | Fixed to `CONTROLLED_TERM`. Discriminator for coexistence with TRUE_DEF and APPLICABILITY records. |
| 3 | **Scheme** | **Required** | `skos:inScheme` | enum | single | One of: `IMO`, `IACS`, `KR`, `EU`. Identifies the source authority. |
| 4 | **Source_Doc_Type** | **Required** | `dct:type` (secondary) | enum | single | Classifies the document genre. Values from closed list (Section 3.2a). Shared with TRUE_DEF and APPLICABILITY instructions. |
| 5 | **Term_Category** | **Required** | `mreg:termCategory` | enum | single | Primary functional classification. Values from Section 3.3. |
| 6 | **Term_Subclass** | **Required** | `mreg:termSubclass` | enum | single | Secondary classification within the category. Values from Section 3.4. |
| 7 | **Domain_Facet** | **Required** | `mreg:domainFacet` | enum | single | Domain/subject-area tag. Values from Section 3.3a. Enables cross-category domain filtering (e.g., all Environment-related terms regardless of Term_Category). |
| 8 | **prefLabel@en** | **Required** | `skos:prefLabel` | text | single | Normalised preferred label. Sentence case, singular, English. See Label Policy (Section 5). |
| 9 | **altLabel@en** | Optional | `skos:altLabel` | text-multi | multi | Abbreviations, acronyms, legitimate variants. Semicolon-separated. |
| 10 | **Source_Form@en** | **Required** | `mreg:sourceForm` | text | single | Term as it appears verbatim in the source document. Preserves original casing and phrasing. **This is a provenance field, not a search label.** Mapped to a custom property `mreg:sourceForm` (not `skos:hiddenLabel`) to avoid SKOS label disjointness violations when Source_Form matches prefLabel or altLabel. |
| 11 | **Definition_Context@en** | **Required** | `skos:scopeNote` | text | single | 1-2 sentence contextual description extracted from the source, showing how the term is used in prescriptive context. **Not a formal definition** (that belongs to TRUE_DEF). This is a usage-context note. Verbatim or near-verbatim from source. |
| 12 | **Deontic_Pattern@en** | Conditional | `mreg:deonticPattern` | text | single | The normative expression pattern in which the term typically appears. E.g., `"is to be carried out"`, `"shall be submitted for approval"`, `"should be provided"`. **Fill if the term consistently appears with a specific obligation pattern.** |
| 13 | **Normative_Status** | **Required** | `mreg:normativeStatus` | enum | single | Normative force of the source instrument. Values: `mandatory` (shall/must/is to be), `recommendatory` (should/recommends), `guidance` (advisory best-practice), `interpretive` (official interpretation of a mandatory requirement), `discretionary` (left to Administration/society discretion; may). Shared value set with APPLICABILITY (Section 3.7 of APPLICABILITY instruction). |
| 14 | **Source_Doc** | **Required** | `dcterms:source` | text | single | Source document identifier. See Annexes for format per source family. |
| 15 | **Source_Locator** | **Required** | (locator) | text | single | Section/Table/Annex/Regulation location. E.g., `Reg. 13.2.1`, `Table 6`, `Art. 5(3)`. |
| 16 | **Editor_Note** | Optional | `skos:editorialNote` | text | single | Extraction rationale, synonym/homonym flags, Phase 2 action tags, QA comments. For cross-scheme equivalents: `[equivalent: {Scheme}_{Concept_ID}]`. For Resolutions/Circulars: `[normative_basis: {parent instrument}]`. |

#### Obligation Legend

| Obligation | Meaning |
|:---|:---|
| **Required** | Must always be filled. Record is invalid without it. |
| **Conditional** | Must be filled if the source text contains the relevant information. Leave blank if not stated. |
| **Optional** | Fill if available and useful. Record remains valid without it. |

### 3.2 Interoperability with TRUE_DEF and APPLICABILITY Records

| Aspect | TRUE_DEF | APPLICABILITY | CONTROLLED_TERM | Resolution |
|:---|:---|:---|:---|:---|
| **Discriminator** | `Record_Type` = `TRUE_DEF` | `Record_Type` = `APPLICABILITY` | `Record_Type` = `CONTROLLED_TERM` | `Record_Type` is the single discriminator |
| **Term source** | Formal Definitions section | Application/Scope section | Body text (normative requirements) | Non-overlapping source locations |
| **Definition** | `Definition@en` (verbatim formal def) | -- | `Definition_Context@en` (usage context, not formal def) | TRUE_DEF definitions take precedence if a term has both |
| **Scheme** | `IMO`, `IACS`, `KR`, `EU` | `IMO`, `IACS`, `KR`, `EU` | `IMO`, `IACS`, `KR`, `EU` | All four Scheme values are shared across all three instructions |
| **Source_Doc_Type** | Present (Section 3.6 of TRUE_DEF) | Present (Section 3.6 of APPLICABILITY) | Present (Section 3.2a) | All three instructions share the same closed list including EU-specific values (`Directive`, `Regulation_EU`, `Decision`) |

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

> **Full list** (shared by TRUE_DEF, APPLICABILITY, and CONTROLLED_TERM): `Convention` through `Technical_Rule` (13 values) plus `Directive`, `Regulation_EU`, `Decision` (3 EU-specific values, used when Scheme = `EU`). All 16 values are now available across all three instructions. The former single value `Code` is split into `Mandatory_Code` and `Recommendatory_Code` to separate document genre from normative force, aligning with the APPLICABILITY instruction.

### 3.3 Term_Category Controlled Values

#### Existing Categories (from IACS foundation)

| Value | Description | Primary Domain | Examples |
|:---|:---|:---|:---|
| `Test` | Testing and examination methods, test stages | Structural, Manufacturing | tensile test, factory acceptance test |
| `Survey` | Survey types, inspection activities, examination acts | Survey | special survey, close-up survey |
| `NDT_Method` | Non-destructive testing/examination methods | Structural | ultrasonic testing, radiographic testing |
| `Approval` | Approval and certification actions/decisions/documents | Regulatory | type approval, manufacturer approval |
| `Manufacturing` | Manufacturing processes and treatments | Manufacturing | rolling, forging, casting, heat treatment |
| `Welding` | Welding processes, procedures, qualifications, consumables | Welding | welding procedure, welder qualification |
| `Quality` | Quality management and assurance activities | Quality | quality assurance, conformity of production |
| `Normative` | Normative/deontic expression patterns | Cross-domain | shall, is to be, not less than |
| `Actor` | Organisational entities participating in regulatory processes | Cross-domain | Classification Society, manufacturer, Flag State |
| `Role` | Functional roles played by actors | Cross-domain | approving authority, surveyor, Ship Security Officer |
| `Document` | Certificates, reports, plans, records | Cross-domain | type approval certificate, Oil Record Book |
| `Condition` | State assessments, status indicators | Survey, Structural | substantial corrosion, coating condition |

#### New Categories (for IMO/KR/EU extension)

| Value | Description | Primary Domain | Examples |
|:---|:---|:---|:---|
| `Safety_Equipment` | Safety systems, life-saving appliances, fire protection equipment, navigation equipment | Safety | lifeboat, fire detection system, ECDIS, EPIRB |
| `Environment` | Pollution prevention actions, emission controls, discharge procedures, treatment systems | Environment | oily water separator, ballast water exchange, scrubber |
| `Competency` | Training programmes, seafarer qualifications, certification of competence, watchkeeping | Training | basic safety training, certificate of competency, sea service |
| `Security` | Ship/port security measures, cybersecurity, access control | Security | Ship Security Plan, security level, SSO |
| `Operation` | Cargo handling, emergency procedures, operational controls, drills, maintenance | Operations | abandon ship drill, bunkering procedure, cargo stowage |
| `Enforcement` | Port State Control actions, detention, deficiency, flag state oversight | Regulatory | detention, deficiency, clear grounds inspection |
| `Labour` | Seafarer welfare, employment conditions, hours of work/rest, accommodation | Labour | hours of rest, employment agreement, repatriation |
| `Measurement` | Load line, freeboard, tonnage, stability parameters | Measurement | summer freeboard, gross tonnage, damage stability |

### 3.3a Domain_Facet Controlled Values

> **Purpose**: The Domain_Facet is an orthogonal axis to Term_Category. Term_Category classifies **what the term is** (functional type); Domain_Facet classifies **what domain the term belongs to** (subject area). This 2-level model (recommended by Codex) prevents category explosion while enabling domain-specific filtering.

| Value | Description | Typical Sources |
|:---|:---|:---|
| `Structural` | Hull construction, structural integrity, materials | IACS UR S/W series, SOLAS II-1 |
| `Machinery` | Machinery, propulsion, electrical systems | IACS UR M series, SOLAS II-1 Part C |
| `Welding` | Welding processes and qualification | IACS UR W series |
| `Manufacturing` | Material production, heat treatment, delivery conditions | IACS UR W/M series |
| `Survey` | Classification and statutory surveys, inspections | IACS UR Z series, ESP Code, RO Code |
| `Safety` | Life safety, fire protection, LSA, structural fire protection | SOLAS II-2, III, FSS Code, LSA Code |
| `Navigation` | Navigation equipment, COLREG, routing, pilotage, bridge procedures | SOLAS V, COLREG |
| `Communication` | GMDSS, radio, distress signalling | SOLAS IV |
| `Environment` | Pollution prevention, emissions, ballast water, garbage, sewage | MARPOL I-VI, BWM Convention |
| `Security` | Ship/port security, cybersecurity, ISPS | SOLAS XI-2, ISPS Code |
| `Training` | Crew competency, certification, watchkeeping | STCW, STCW-F |
| `Operations` | Cargo handling, emergency procedures, ISM, operational safety | ISM Code, IMDG, CSS, BLU Codes |
| `Labour` | Seafarer welfare, working conditions, health | MLC 2006 |
| `Regulatory` | Approval, certification, flag/port state control, enforcement | SOLAS I/XI-1, PSC Procedures, RO Code |
| `Stability` | Intact/damage stability, subdivision, load lines, freeboard | SOLAS II-1 Part B, ICLL, Grain Code |
| `Chemical_Hazard` | Dangerous goods, chemicals, gases | IMDG, IBC, IGC Codes |

### 3.4 Term_Subclass Controlled Values

#### Test
| Value | Description |
|:---|:---|
| `Destructive` | Mechanical/material tests that consume or alter the specimen |
| `Pressure_Tightness` | Hydrostatic, pneumatic, tightness, burst tests |
| `Functional_Performance` | Operational, functional, performance, endurance tests |
| `Test_Stage` | Certification/production stages (type test, FAT, shipboard trials) |
| `Fire_Test` | Fire resistance, fire endurance, flame spread tests (FSS/FTP Code) |

#### Survey
| Value | Description |
|:---|:---|
| `Periodic` | Interval-based surveys (annual, intermediate, special) |
| `Continuous` | Continuous survey programmes |
| `Occasional` | Event-triggered surveys (damage, reactivation, repair) |
| `Extent` | Survey scope/extent descriptors (close-up, overall) |
| `Execution_Condition` | Survey execution conditions (dry dock, in-water, remote) |
| `Statutory` | Flag state / IMO statutory surveys (initial, renewal, periodical) |
| `Port_State` | Port State Control inspections and follow-up surveys |

#### NDT_Method
| Value | Description |
|:---|:---|
| `Surface` | Surface methods (VT, MT, PT, ET) |
| `Volumetric` | Volumetric methods (UT, RT, PAUT, TOFD) |
| `Measurement` | Dimensional measurement (thickness measurement) |

#### Approval
| Value | Description |
|:---|:---|
| `Decision` | Approval/acceptance decisions |
| `Credential` | Certificates and formal credentials |
| `Status` | Approval/certification status (valid, expired, suspended) |
| `Delegation` | Authorization/delegation of approval authority (RO Code) |

#### Manufacturing
| Value | Description |
|:---|:---|
| `Forming` | Rolling, forging, casting, forming |
| `Joining` | Welding, brazing (-> use Welding category for detailed welding terms) |
| `Heat_Treatment` | Normalising, quenching, tempering, stress relieving |
| `Delivery_Condition` | Material supply condition (AR, N, QT, TM/TMCP) |
| `Surface_Treatment` | Coating, painting, surface finishing |

#### Welding
| Value | Description |
|:---|:---|
| `Process_Type` | SMAW, GTAW, GMAW, SAW, etc. |
| `Procedure` | WPS, PQR, WPQT |
| `Consumable` | Electrode, wire, flux, filler metal |
| `Personnel` | Welder/operator qualification |
| `Joint_Type` | Butt weld, fillet weld, tee joint |
| `Thermal_Process` | Preheating, PWHT |

#### Quality
| Value | Description |
|:---|:---|
| `System` | QMS, QA system, SMS (ISM Code Safety Management System) |
| `Activity` | QC, inspection, audit, management review |
| `Requirement` | Conformity, traceability, non-conformity, corrective action |
| `Scheme` | ACS, ESP, PMS, CBM |

#### Normative
| Value | Description |
|:---|:---|
| `Obligation` | shall, is to be, must |
| `Prohibition` | shall not, is not to |
| `Permission` | may |
| `Recommendation` | should, recommends |
| `Exemption` | need not, may exempt |
| `Quantitative_Constraint` | minimum, not less than, not to exceed |
| `Discretionary` | to the satisfaction of, as deemed necessary |
| `Reference` | in accordance with, as specified in, in compliance with |

#### Actor
| Value | Description |
|:---|:---|
| `Regulatory` | Classification Society, Flag State, Port State, Administration, Contracting Government |
| `Industry` | Manufacturer, shipbuilder, owner, Company (ISM), operator |
| `Service` | Service supplier, testing laboratory, Recognized Organization |
| `International` | IMO, ILO, EU Commission |

#### Role
| Value | Description |
|:---|:---|
| `Authority` | Approving authority, certifying authority, competent authority |
| `Inspector` | Surveyor, NDT operator, PSC inspector, auditor |
| `Applicant` | Applicant for approval/certification |
| `Producer` | Manufacturer in production role |
| `Shipboard` | Master, chief officer, Ship Security Officer, Designated Person Ashore |

#### Document
| Value | Description |
|:---|:---|
| `Certificate` | TAC, DEC, IOPP, SMC, DOC, ISSC, classification certificate |
| `Report` | Test report, survey report, thickness measurement report |
| `Plan` | Survey programme, inspection plan, Ship Security Plan, SMS manual |
| `Record` | Maintenance record, quality record, Oil Record Book, Ballast Water Record Book |

#### Condition
| Value | Description |
|:---|:---|
| `Corrosion` | Substantial corrosion, pitting, grooving |
| `Coating` | GOOD, FAIR, POOR |
| `Structural` | Buckling, fracture, deformation |
| `Operational` | Operational condition, deficient condition |

#### Safety_Equipment (New)
| Value | Description |
|:---|:---|
| `Life_Saving` | Lifeboat, life raft, lifejacket, immersion suit, rescue boat |
| `Fire_Protection` | Fixed suppression (CO2, foam, water mist, inert gas), portable extinguisher |
| `Fire_Detection` | Smoke detector, flame detector, fire alarm system |
| `Navigation_Equipment` | Radar, ECDIS, AIS, compass, echo sounder |
| `Communication_Equipment` | EPIRB, VDR, SART, GMDSS equipment, VHF |
| `Personal_Protective` | SCBA, immersion suit, lifeline |
| `Structural_Safety` | Watertight door, fire door, collision bulkhead, freeing port |

#### Environment (New)
| Value | Description |
|:---|:---|
| `Pollution_Prevention` | Oil-water separator, ballast water treatment system, incinerator |
| `Emission_Control` | Scrubber, SCR, EGR, EEDI, EEXI, CII |
| `Discharge` | Discharge criteria, special area restrictions, port reception facility |
| `Waste_Management` | Garbage management plan, sewage treatment, food waste |
| `Substance` | Oil, noxious liquid substance, ozone-depleting substance, SOx, NOx |
| `Monitoring` | Oil discharge monitor, emission monitoring, continuous monitoring |

#### Competency (New)
| Value | Description |
|:---|:---|
| `Certificate_Type` | Certificate of competency, endorsement, GMDSS certificate |
| `Training_Programme` | Basic safety training, advanced firefighting, survival craft |
| `Watchkeeping` | Watch pattern, bridge resource management, fatigue management |
| `Sea_Service` | Minimum sea service, qualifying sea service |
| `Medical_Fitness` | Eyesight standard, medical examination, medical certificate |

#### Security (New)
| Value | Description |
|:---|:---|
| `Security_Level` | Level 1 (normal), Level 2 (heightened), Level 3 (exceptional) |
| `Security_Plan` | Ship Security Plan, Port Facility Security Plan |
| `Security_Personnel` | Ship Security Officer, Company Security Officer, PFSO |
| `Access_Control` | Restricted area, identification, security barrier |
| `Assessment` | Ship security assessment, vulnerability assessment |

#### Operation (New)
| Value | Description |
|:---|:---|
| `Cargo_Handling` | Loading, discharge, stowage, securing, fumigation |
| `Emergency` | Abandon ship drill, fire drill, muster, emergency towing |
| `Maintenance` | Planned maintenance system, condition monitoring |
| `Bunkering` | Bunkering procedure, fuel oil changeover |
| `Navigation_Procedure` | Passage planning, voyage monitoring, pilotage |

#### Enforcement (New)
| Value | Description |
|:---|:---|
| `Detention` | Detention, release from detention |
| `Deficiency` | Deficiency, grounds for detention, clear grounds |
| `Rectification` | Rectification, corrective action, follow-up inspection |
| `Banning` | Banning order, refusal of access |

#### Labour (New)
| Value | Description |
|:---|:---|
| `Employment` | Employment agreement, wages, leave entitlement |
| `Working_Conditions` | Hours of work, hours of rest, manning levels |
| `Welfare` | Accommodation, recreation, food and catering |
| `Health` | Medical care, occupational safety, health protection |
| `Repatriation` | Repatriation, financial security |

#### Measurement (New)
| Value | Description |
|:---|:---|
| `Freeboard` | Summer freeboard, winter freeboard, tropical freeboard, timber freeboard |
| `Tonnage` | Gross tonnage, net tonnage, deadweight |
| `Stability_Parameter` | Intact stability, damage stability, GZ curve, GM |
| `Zone` | Seasonal zone (tropical, summer, winter North Atlantic) |

### 3.5 Concept_ID / URI Design

- **General Pattern**: `{Scheme}_{SourceKey}_CT_{SeqNo}`
- `Scheme`: Must match column 3 value
- `SourceKey`: Normalised source identifier (source-family-specific rules below)
- `_CT_`: Fixed infix distinguishing CONTROLLED_TERM records
- `SeqNo`: Three-digit sequence number, local within that source unit

#### Source-Family Concept_ID Patterns

| Source Family | Scheme | Pattern | Examples |
|:---|:---|:---|:---|
| IACS UR | `IACS` | `IACS_{URKey}_CT_{SeqNo}` | `IACS_W11_CT_001`, `IACS_Z10_1_CT_001` |
| IACS UI | `IACS` | `IACS_UI_SC123_CT_{SeqNo}` | `IACS_UI_SC123_CT_001` |
| IACS Rec | `IACS` | `IACS_REC_{RecNo}_CT_{SeqNo}` | `IACS_REC_41_CT_001` |
| IMO Convention | `IMO` | `IMO_{ConvChapter}_CT_{SeqNo}` | `IMO_SOLAS_II_2_CT_001`, `IMO_MARPOL_I_CT_001` |
| IMO Code | `IMO` | `IMO_{CodeAbbr}_CT_{SeqNo}` | `IMO_ISM_CT_001`, `IMO_FSS_CT_001` |
| IMO Resolution | `IMO` | `IMO_RES_{CommitteeNo}_CT_{SeqNo}` | `IMO_RES_MSC396_CT_001` |
| IMO Circular | `IMO` | `IMO_CIRC_{CommitteeNo}_CT_{SeqNo}` | `IMO_CIRC_MSC1040_CT_001` |
| KR Rule | `KR` | `KR_{PartChapter}_CT_{SeqNo}` | `KR_PT3_CH2_CT_001` |
| EU Directive | `EU` | `EU_DIR_{Year}_{No}_CT_{SeqNo}` | `EU_DIR_2009_45_CT_001` |
| EU Regulation | `EU` | `EU_REG_{Year}_{No}_CT_{SeqNo}` | `EU_REG_2015_757_CT_001` |

#### SourceKey Normalization Rules

> **Steps 1–5** are the shared core rules, identical across all three instructions (TRUE_DEF / APPLICABILITY / CONTROLLED_TERM). Apply them uniformly to ensure Concept_IDs are predictable and cross-linkable. **Steps 6–7** are CONTROLLED_TERM-specific extensions for IMO Code abbreviations and EU legislation patterns.

| Step | Rule | Scope | Example |
|:---:|:---|:---|:---|
| 1 | Replace dots, parentheses, and commas with underscores (or remove if at word boundary) | Shared | `Z10.1` → `Z10_1`; `W(rev)11` → `Wrev11` |
| 2 | Replace `/` and `-` with `_` | Shared | `II-1/3-8` → `II_1_3_8` |
| 3 | Collapse consecutive underscores | Shared | `II__1` → `II_1` |
| 4 | Use UPPERCASE | Shared | `Pt3_Ch2` → `PT3_CH2` |
| 5 | Remove document-type prefix (already in pattern) | Shared | `UR W11` → `W11` |
| 6 | IMO Codes: standard abbreviation | CT only | `FSS Code` → `FSS`, `ISM Code` → `ISM` |
| 7 | EU: year + number | CT only | `Directive 2009/45/EC` → `DIR_2009_45` |

- Base URI pattern: `https://{domain}/maritime-cv/{Concept_ID}` — `{Concept_ID}` is the full value including the Scheme prefix
- In Phase 1, only the local ID (`Concept_ID`) is finalised.

---

## 4. Extraction Patterns

### 4.1 Universal Extraction Patterns (all source families)

| # | Pattern | Trigger | Target Columns |
|:---:|:---|:---|:---|
| CT1 | Action verb in obligation context | "X **is to be carried out**", "Y **shall be submitted**" | prefLabel (action/object), Deontic_Pattern |
| CT2 | Named test/examination method | "tensile test", "Charpy V-notch impact test", "fire resistance test" | prefLabel, Term_Category = Test |
| CT3 | Named survey type | "special survey", "annual survey", "initial survey" | prefLabel, Term_Category = Survey |
| CT4 | NDT method reference | "ultrasonic testing", "PAUT", "radiographic examination" | prefLabel, Term_Category = NDT_Method |
| CT5 | Approval/certification action | "type approval", "manufacturer approval", "shall be certified" | prefLabel, Term_Category = Approval |
| CT6 | Manufacturing process | "normalising", "quenching and tempering", "flash butt welding" | prefLabel, Term_Category = Manufacturing or Welding |
| CT7 | Quality/conformity term | "quality management system", "conformity of production" | prefLabel, Term_Category = Quality |
| CT8 | Actor/role identification | "the Classification Society shall", "the Surveyor is to", "the Administration shall" | prefLabel, Term_Category = Actor or Role |
| CT9 | Document/credential name | "type approval certificate", "inspection certificate", "Oil Record Book" | prefLabel, Term_Category = Document |
| CT10 | Condition/state assessment | "substantial corrosion", "coating condition GOOD" | prefLabel, Term_Category = Condition |

### 4.2 Extended Extraction Patterns (IMO/KR/EU sources)

| # | Pattern | Trigger | Target Columns |
|:---:|:---|:---|:---|
| CT11 | Safety equipment specification | "shall be fitted with", "shall be equipped with", equipment names in prescriptive context | prefLabel, Term_Category = Safety_Equipment |
| CT12 | Environmental control | "shall not discharge", "emission control", "treatment system", "ballast water exchange" | prefLabel, Term_Category = Environment |
| CT13 | Training/competency requirement | "certificate of competency", "minimum sea service", "shall hold", "shall be trained" | prefLabel, Term_Category = Competency |
| CT14 | Security measure | "security level", "security plan", "security officer", "restricted area" | prefLabel, Term_Category = Security |
| CT15 | Operational procedure | "drill", "muster", "cargo operation", "bunkering", "emergency procedure" | prefLabel, Term_Category = Operation |
| CT16 | Manning/crew requirement | "master", "chief officer", "minimum safe manning", role titles + "shall" | prefLabel, Term_Category = Actor or Competency |
| CT17 | Measurement/threshold parameter | "freeboard", "gross tonnage", "damage stability", "GZ curve" | prefLabel, Term_Category = Measurement |
| CT18 | Enforcement/PSC action | "detention", "deficiency", "clear grounds", "rectification" | prefLabel, Term_Category = Enforcement |

### 4.3 Synonym/Variant Detection Patterns

| # | Pattern | Action |
|:---:|:---|:---|
| SYN1 | Same concept, different surface forms | "tightness test" / "leak test" / "leakage test" -> Select one prefLabel, others as altLabel |
| SYN2 | Abbreviation | "factory acceptance test" / "FAT" -> Full form as prefLabel, abbreviation as altLabel |
| SYN3 | British/American spelling | "normalising" / "normalizing" -> British as prefLabel (per house style), American as altLabel |
| SYN4 | IMO-specific acronyms | "Life-Saving Appliance" / "LSA"; "International Safety Management" / "ISM" -> Full form as prefLabel |
| SYN5 | Cross-source equivalent naming | "the Administration" (IMO) / "the Society" (IACS) / "the competent authority" (EU) -> Record separately; tag `[equivalent:]` in Editor_Note |
| SYN6 | Convention reference naming | "SOLAS fire safety" / "Chapter II-2 fire safety" -> Descriptive form as prefLabel |

### 4.4 Hierarchy Detection Patterns (Phase 2)

> **Note**: Hierarchy detection is deferred to Phase 2. The patterns below are retained as reference for Phase 2 execution; hierarchy candidates should be tagged in Editor_Note.

| # | Pattern | Example |
|:---:|:---|:---|
| HIE1 | Generic-specific | "pressure test" -> "hydrostatic test" / "pneumatic test" |
| HIE2 | Method-variant | "ultrasonic testing" -> "PAUT" / "TOFD" |
| HIE3 | Type-instance | "survey" -> "special survey" / "annual survey" |
| HIE4 | Equipment hierarchy | "life-saving appliance" -> "lifeboat" / "life raft" / "rescue boat" |
| HIE5 | Competency hierarchy | "STCW competency" -> "basic safety training" / "advanced firefighting" |
| HIE6 | Operational hierarchy | "cargo operation" -> "loading procedure" / "discharge procedure" |

---

## 5. Label Policy

| Label type | Purpose | Example |
|:---|:---|:---|
| `skos:prefLabel` | Primary normalised label. **One per language.** | "hydrostatic test"@en |
| `skos:altLabel` | Abbreviations, acronyms, legitimate variants | "FAT"@en; "leak test"@en |
| `skos:hiddenLabel` | OCR variants, typos, dotted forms (search-only) | "B.W.M.S."@en |
| `mreg:sourceForm` | Verbatim source form (provenance, not a search label) | "Hydrostatic Test"@en (original casing) |

### Naming conventions

| Rule | Content |
|:---|:---|
| Case | Sentence case (lowercase unless proper noun) |
| Number | Singular by default |
| Form | Noun phrase preferred. For test types: `[qualifier] + test`. For processes: gerund or noun form |
| Abbreviation | Full form as prefLabel; abbreviation as altLabel. Never abbreviation-only as prefLabel |
| Compound terms | Use natural word order: "welding procedure qualification test", not "test, welding procedure qualification" |
| IMO-specific | Preserve official IMO names (e.g., "GMDSS", "EPIRB" as altLabel only) |

---

## 6. Editorial Rules (Phase 1 Summary)

| Rule | Content |
|:---|:---|
| Language | English only (data cells). Korean permitted only in internal notes |
| Spelling | British English (normalising, vapour, centre, programme). **TSV column headers use `@en` for simplicity. When converting to RDF, all English-language literals shall carry the `@en-GB` tag (BCP 47 compliant).** This two-layer approach avoids header verbosity while preserving dialect precision in the final RDF output |
| Definition_Context | Near-verbatim from source. Not a formal definition -- a usage-context excerpt showing how the term is used prescriptively |
| Deontic_Pattern | Record the most representative obligation pattern. Use the exact modal verb form from the source |
| Normative_Status | Derive from the source instrument's normative force, not from the individual sentence. Conventions/Mandatory_Codes = `mandatory`; Recommendatory_Codes/Circulars = `recommendatory`; Guidance = `guidance`; UI/Interpretations = `interpretive`; "may"/"at society's discretion" = `discretionary`. Shared 5-value set with APPLICABILITY instruction |
| Source citation | Separate Source_Doc and Source_Locator. Do not use special character symbols. See Annexes for source-specific citation formats |
| Enum values | Use exact values from Sections 3.3, 3.3a, and 3.4. If no match, use closest value + flag in Editor_Note |
| Empty cells | Leave blank if information not present. Do not default or infer |
| Deduplication | **Phase 1 rule: register every source-document occurrence as a separate record**, consistent with Section 2.1 source-specific extraction. If the same term (identical prefLabel) appears in multiple documents of the same Scheme, each document gets its own record with its own Concept_ID, Source_Doc, and Source_Locator. Tag `[same_scheme_dup: {other Concept_ID}]` in Editor_Note for Phase 2 consolidation. **Cross-Scheme**: Always register separately; tag `[equivalent: {Scheme}_{Concept_ID}]` in Editor_Note for Phase 2 consolidation. **Phase 2 will merge same-Scheme duplicates into canonical terms.** |

---

## 7. Procedure

```
Step 1   Identify the source family and select the corresponding Annex (A-E)
Step 2   Open the target document (from source directory)
Step 3   Skip the "Definitions" section (-> TRUE_DEF) and "Scope/Application"
         section (-> APPLICABILITY) per Section 1.1 mapping
Step 4   Scan the body text for terms matching Extraction Patterns CT1-CT18
Step 5   Apply Admission Rule -- confirm the term qualifies and is not already
         in TRUE_DEF or APPLICABILITY
Step 6   Assign Concept_ID per Section 3.5 rules
         Set Record_Type = CONTROLLED_TERM
         Set Scheme per source family
         Set Source_Doc_Type per document genre
Step 7   Assign Term_Category and Term_Subclass per Sections 3.3-3.4
         Assign Domain_Facet per Section 3.3a
Step 8   Normalise prefLabel per Label Policy (Section 5)
         Record Source_Form@en (verbatim)
         Record altLabel@en (abbreviations, variants)
Step 9   Extract Definition_Context@en -- 1-2 sentence usage context
Step 10  Record Deontic_Pattern@en if a consistent obligation pattern exists
         Record Normative_Status per source instrument
Step 11  Check Synonym/Variant patterns (SYN1-SYN6)
         Check Hierarchy patterns (HIE1-HIE6) — tag candidates in Editor_Note for Phase 2
Step 12  Record Source_Doc / Source_Locator per Annex format
Step 13  Verify (Section 8)
```

---

## 8. Verification

### 8.1 2-Pass Review

| Pass | Focus | Check items |
|:---|:---|:---|
| **Structural** | Table integrity | Column count consistency (16 columns), no duplicate Concept_ID, valid enum values (Scheme, Source_Doc_Type, Term_Category, Term_Subclass, Domain_Facet, Normative_Status), `_CT_` infix present, Record_Type = `CONTROLLED_TERM` |
| **Semantic** | Content correctness | Definition_Context = source-faithful usage excerpt (not formal definition), prefLabel normalised per Label Policy, no overlap with TRUE_DEF terms, Deontic_Pattern uses exact modal form, Normative_Status consistent with source instrument type |

### 8.2 Cross-Check Rules

| Rule | Check | Severity |
|:---|:---|:---|
| Required fields | Concept_ID, Record_Type, Scheme, Source_Doc_Type, Term_Category, Term_Subclass, Domain_Facet, prefLabel, Source_Form, Definition_Context, Normative_Status, Source_Doc, Source_Locator must be filled | **Error** |
| Record_Type value | Must be `CONTROLLED_TERM` | **Error** |
| Scheme value | Must be one of `IMO`, `IACS`, `KR`, `EU` | **Error** |
| Source_Doc_Type value | Must be from closed list (Section 3.2a) | **Error** |
| Concept_ID format | Must match `{Scheme}_{SourceKey}_CT_{SeqNo}` pattern | **Error** |
| Concept_ID-Scheme coherence | Concept_ID prefix must match Scheme value (`IMO_*` for IMO, `IACS_*` for IACS, `KR_*` for KR, `EU_*` for EU) | **Error** |
| Term_Category validation | Must be from Section 3.3 list | **Error** |
| Term_Subclass validation | Must be valid for the parent Term_Category (Section 3.4) | **Error** |
| Domain_Facet validation | Must be from Section 3.3a list | **Error** |
| Normative_Status validation | Must be one of `mandatory`, `recommendatory`, `guidance`, `interpretive`, `discretionary` | **Error** |
| No TRUE_DEF overlap | prefLabel must not duplicate a prefLabel already registered in TRUE_DEF for the same Source_Doc | **Warning** |
| Synonym consistency | If term A lists term B as altLabel, term B must not have its own primary record with the same prefLabel | **Warning** |
| Deontic_Pattern format | Must contain a modal verb (shall, is to be, may, must, need not, should, recommends) | **Warning** |
| Record_Type-conditional validation | CONTROLLED_TERM records must not contain TRUE_DEF-only columns (Definition@en, Example@en) or APPLICABILITY-only columns (Target_Entity, Ship_Type, etc.) | **Error** |
| Cross-scheme semantic duplicate | If identical prefLabel exists in different Scheme, flag as `[equivalent: {Scheme}_{ID}]` in Editor_Note | **Warning** |
| Normative_Status-Deontic coherence | If Normative_Status = `guidance` or `discretionary`, Deontic_Pattern should not contain "shall"/"must" | **Warning** |
| Domain_Facet-Term_Category coherence | Verify logical alignment (e.g., Term_Category = `Welding` + Domain_Facet = `Environment` is suspicious) | **Warning** |
| Concept_ID global uniqueness | No duplicate Concept_ID across all Scheme values | **Error** |

---

## 9. Output Specification

All final output files are saved to the **`results/`** subdirectory under the working directory from which the instruction is executed. Per-chunk intermediate files (partial TSV and log files produced during segmented processing) are saved to **`results/temp/`**. Both directories shall be created automatically if they do not exist. Each extraction run produces exactly **3 final files** in `results/`: one result file, one summary file, and one log file. Intermediate files in `results/temp/` are retained for traceability but are not considered deliverables.

### 9.1 File Naming Convention

| File | Name Pattern | Description |
|:---|:---|:---|
| **Result** | `phase1_controlled_term_result.tsv` | Final extraction table in TSV format (Tab-Separated Values). Contains all extracted records conforming to the Target Schema (Section 3). One header row + data rows. UTF-8 with BOM. |
| **Summary** | `phase1_controlled_term_summary.md` | Extraction summary report in Markdown format. |
| **Log** | `phase1_controlled_term_log.md` | Processing log in Markdown format. |

### 9.2 Result File (`phase1_controlled_term_result.tsv`)

- **Format**: TSV (Tab-Separated Values), UTF-8 with BOM
- **Header row**: Column names exactly as defined in Section 3.1, tab-delimited
- **Column order**: `Concept_ID	Record_Type	Scheme	Source_Doc_Type	Term_Category	Term_Subclass	Domain_Facet	prefLabel@en	altLabel@en	Source_Form@en	Definition_Context@en	Deontic_Pattern@en	Normative_Status	Source_Doc	Source_Locator	Editor_Note`
- **Empty cells**: Leave blank (no placeholder text such as "N/A" or "-")
- **Multi-value delimiter**: Semicolon (`;`) within a cell, as per Section 3.1
- **Quoting**: Fields containing tabs, newlines, or double quotes must be enclosed in double quotes. Embedded double quotes are escaped as `""`
- **Sort order**: By `Source_Doc` (ascending), then by `Source_Locator` (document order)

### 9.3 Summary File (`phase1_controlled_term_summary.md`)

The summary file shall contain the following sections:

```markdown
# Phase 1 CONTROLLED_TERM Extraction Summary

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

## Records by Term_Category
| Term_Category | Count |
|:---|---:|
| {category} | {n} |
| ... | ... |

## Quality Flags
- Phase 2 backlog items: {count}
- Editor_Note flags: {count}
- TRUE_DEF overlap warnings: {count}
- Cross-scheme semantic duplicates: {count}

## Issues / Observations
- {free text: notable decisions, ambiguities, deferred items}
```

### 9.4 Log File (`phase1_controlled_term_log.md`)

The log file records the sequential processing trace:

```markdown
# Phase 1 CONTROLLED_TERM Processing Log

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

### 9.5 Overwrite Rule

Each new extraction run **overwrites** the previous final output files in `results/` and all intermediate files in `results/temp/`. If incremental preservation is needed, the user must rename or archive prior files before initiating a new run.

---

## 10. Phase 1.1 — Validation Exception Management

When recurring comments are identified during iterative validation of Phase 1 outputs, they are escalated to Phase 1.1 for systematic resolution. Phase 1.1 is **not** an additional extraction phase — it is a QA exception layer.

**Full specification**: See [`phase1_1_validation_exception_guide.md`](phase1_1_validation_exception_guide.md) (shared across all three Phase 1 instructions).

**Escalation criteria (summary)**:
- Comment recurs 2+ times or across 2+ documents/records
- Issue blocks validator pass
- Current guide text is ambiguous — reviewers disagree on correct action
- Phase 1 / Phase 2 boundary is unclear

**Key difference from Phase 1 overwrite rule**: The Phase 1.1 issue register is **versioned and never overwritten** (`results/phase1_1/phase1_1_issue_register_{date}_v{NN}.tsv`).

---

## 11. Phase 2 Preview (Reference Only)

| Item | Description |
|:---|:---|
| Cross-document consolidation | Merge same-concept records from different documents into canonical terms |
| Cross-source mapping | Map equivalent terms across IMO/IACS/KR/EU using skos:exactMatch / skos:closeMatch |
| Broader/Related assignment | Assign `skos:broader` and `skos:related` relationships |
| Formal hierarchy | Validate and formalise hierarchy candidates into skos:broader / skos:related |
| Frequency/Fitness assessment | Assess term frequency and controlled-vocabulary fitness |
| Synonym resolution | Finalise prefLabel selection among synonym groups |
| OWL class generation | Map Term_Category/Term_Subclass to OWL class hierarchy |
| SKOS-XL | Label-to-label relations (acronymOf, abbreviationOf) |
| Deontic ontology | Model normative expressions as formal deontic logic classes |
| TRUE_DEF linking | Link CONTROLLED_TERM records to corresponding TRUE_DEF records where formal definitions exist |
| APPLICABILITY linking | Link actor/role terms to APPLICABILITY Target_Entity/Target_Role values |
| Regulatory relation modelling | requiresCertificate, performedBy, verifiedBy, mandatedBy relations (beyond SKOS) |
| KR source-language preservation | Add `Source_Form_Local@ko` for Korean-origin terms (Gemini recommendation) |

---

## Annex A: IACS Source-Family Overlay

### A.1 Document Types Covered
- **UR** (Unified Requirements): Mandatory technical requirements
- **UI** (Unified Interpretations): Interpretations of convention requirements
- **Rec** (Recommendations): Non-mandatory guidance

### A.2 Document Structure
```
UR document -> Sections (numbered) -> Paragraphs -> Sub-paragraphs
```
- "Definitions" section: typically near the beginning -> exclude (TRUE_DEF)
- "Application" / "Scope" section: typically Section 1 -> exclude (APPLICABILITY)
- Body text: remaining sections -> extract CONTROLLED_TERM

### A.3 Source_Doc Format
| Type | Format | Example |
|:---|:---|:---|
| UR | `UR {Series}{Number}` | `UR W11`, `UR M44`, `UR Z10.1` |
| UI | `UI {Key}` | `UI SC123`, `UI CC1` |
| Rec | `Rec {Number}` | `Rec 41` |

### A.4 IACS-Specific Extraction Hints
- **Primary CT patterns**: CT1-CT10 (core IACS domain)
- **Heavy on**: Test, Survey, NDT_Method, Manufacturing, Welding, Quality, Approval
- **Deontic patterns**: predominantly "is to be", "are to be", "shall"
- **Domain_Facet**: typically Structural, Machinery, Welding, Manufacturing, Survey

---

## Annex B: IMO Conventions Source-Family Overlay

### B.1 Document Types Covered
- **SOLAS** (Safety of Life at Sea, 1974 as amended)
- **MARPOL** (Marine Pollution, 73/78 as amended)
- **STCW** (Standards of Training, Certification and Watchkeeping)
- **ICLL** (International Convention on Load Lines)
- **BWM** (Ballast Water Management)
- **COLREG** (Collision Regulations)
- **TONNAGE** (International Convention on Tonnage Measurement)
- **MLC** (Maritime Labour Convention)
- Other conventions (SAR, OPRC, Hong Kong Convention, etc.)

### B.2 Document Structure
```
Convention -> Parts/Chapters -> Regulations -> Paragraphs -> Sub-paragraphs
```
- SOLAS: Chapter I-XIV, each with Regulations (Reg. 1, 2, ...)
- MARPOL: Annex I-VI, each with Regulations
- STCW: Parts/Chapters with Regulations and Code sections (A/B)
- "Definitions" regulation (e.g., SOLAS Reg. 2): -> exclude (TRUE_DEF)
- "Application" regulation (e.g., SOLAS Reg. 1): -> exclude (APPLICABILITY)
- **Note**: Definitions are often regulation-local ("For the purpose of this Chapter..."). Only exclude if in a dedicated Definitions regulation/article.

### B.3 Source_Doc Format
| Convention | Format | Example |
|:---|:---|:---|
| SOLAS | `SOLAS {Chapter}` | `SOLAS II-2`, `SOLAS V` |
| MARPOL | `MARPOL Annex {Number}` | `MARPOL Annex I`, `MARPOL Annex VI` |
| STCW | `STCW {Part/Section}` | `STCW Code A-II/1` |
| ICLL | `ICLL {Year}` | `ICLL 1988 Protocol` |
| BWM | `BWM Convention` | `BWM Convention` |
| COLREG | `COLREG` | `COLREG` |
| MLC | `MLC 2006 {Standard}` | `MLC 2006 Standard A2.3` |

### B.4 IMO Convention-Specific Extraction Hints
- **Primary CT patterns**: CT1, CT3, CT5, CT8, CT9, CT11-CT17
- **Heavy on**: Safety_Equipment, Environment, Competency, Operation, Actor, Role, Document, Survey (Statutory)
- **Deontic patterns**: "shall", "shall not", "should", "may"
- **Amendment handling**: Use latest consolidated text; note amendment year in Editor_Note if relevant
- **Multi-edition concern**: Same regulation across SOLAS 1974/1981/1988/2000 editions -- extract from consolidated version, note version lineage in Editor_Note

---

## Annex C: IMO Codes Source-Family Overlay

### C.1 Document Types Covered
- **ISM Code** (International Safety Management)
- **ISPS Code** (Ship and Port Facility Security)
- **IGC Code** (Gas Carriers)
- **IBC Code** (Chemical Tankers)
- **IMDG Code** (Dangerous Goods)
- **FSS Code** (Fire Safety Systems)
- **FTP Code** (Fire Test Procedures)
- **LSA Code** (Life-Saving Appliances)
- **Polar Code**, **Grain Code**, **CSS Code**, **BLU Code**, etc.

### C.2 Document Structure
```
Code -> Parts/Chapters -> Sections -> Paragraphs
```
- Part A (mandatory) / Part B (recommendatory) where applicable (ISM, ISPS)
- Chapters with numbered paragraphs
- "Definitions" chapter/section -> exclude (TRUE_DEF)
- "General/Application" chapter -> exclude (APPLICABILITY)

### C.3 Source_Doc Format
| Code | Format | Example |
|:---|:---|:---|
| ISM Code | `ISM Code` | `ISM Code` |
| ISPS Code | `ISPS Code Part {A/B}` | `ISPS Code Part A` |
| IGC Code | `IGC Code` | `IGC Code` |
| IMDG Code | `IMDG Code {Part}` | `IMDG Code Part 7` |
| FSS Code | `FSS Code Ch.{N}` | `FSS Code Ch.5` |

### C.4 Code-Specific Extraction Hints
- **ISM Code**: Quality (System), Actor (Company, DPA), Document (SMS, DOC, SMC), Operation (Emergency)
- **ISPS Code**: Security (all subclasses), Actor (CSO, SSO, PFSO), Document (SSP, PFSP, DoS)
- **IGC/IBC/IMDG**: Safety_Equipment, Environment (Substance), Operation (Cargo_Handling), Condition
- **FSS/FTP/LSA Code**: Safety_Equipment (all subclasses), Test (Fire_Test)
- **Normative_Status**: Part A = `mandatory`, Part B = `recommendatory`

---

## Annex D: IMO Resolutions & Circulars Source-Family Overlay

### D.1 Document Types Covered
- **Resolutions**: Adopted by IMO Assembly, MSC, MEPC, other committees
- **Circulars**: MSC, MEPC, MSC-MEPC joint, LL.3, STCW, others

### D.2 Special Normative Status Handling
- Resolutions adopting amendments to mandatory instruments: `Normative_Status = mandatory`
- Resolutions with "recommends" / "invites" language: `Normative_Status = recommendatory`
- Circulars providing guidelines/interpretations: `Normative_Status = guidance`
- **Always record** `[normative_basis: {parent instrument}]` in Editor_Note to link back to the parent convention/code

### D.3 Source_Doc Format
| Type | Format | Example |
|:---|:---|:---|
| Assembly Resolution | `IMO Res. A.{Number}({Session})` | `IMO Res. A.1138(31)` |
| MSC Resolution | `IMO Res. MSC.{Number}({Session})` | `IMO Res. MSC.396(95)` |
| MEPC Resolution | `IMO Res. MEPC.{Number}({Session})` | `IMO Res. MEPC.328(76)` |
| MSC Circular | `MSC/Circ.{Number}` or `MSC.1/Circ.{Number}` | `MSC.1/Circ.1040` |
| MEPC Circular | `MEPC/Circ.{Number}` or `MEPC.1/Circ.{Number}` | `MEPC.1/Circ.834` |

### D.4 Extraction Hints
- **Primary CT patterns**: CT1, CT5, CT8, CT9, CT11-CT15
- Terms defined in resolutions/circulars often supplement or interpret terms from conventions/codes
- **Deduplication**: If a circular uses the same term as a convention, register separately (per Section 6 source-specific rule) and tag `[same_scheme_dup: {Convention Concept_ID}]` in Editor_Note
- **Careful with**: "invites", "urges", "encourages" -- these are NOT equivalent to "shall"; record as `Normative_Status = guidance`

---

## Annex E: EU Maritime Legislation Source-Family Overlay

### E.1 Document Types Covered
- **Directives**: Require national transposition (e.g., Directive 2009/45/EC on passenger ship safety)
- **Regulations**: Directly binding across EU (e.g., Regulation (EU) 2015/757 on MRV of CO2 emissions)
- **Decisions**: Binding on specific addressees

### E.2 Document Structure
```
EU Instrument -> Recitals -> Articles -> Paragraphs -> Annexes
```
- Art. 1 "Subject matter and scope" -> exclude (APPLICABILITY)
- Art. 2 "Definitions" -> exclude (TRUE_DEF)
- Recitals (preamble "Whereas..."): exclude (not normative)
- Remaining Articles + Annexes -> extract CONTROLLED_TERM

### E.3 Source_Doc Format
| Type | Format | Example |
|:---|:---|:---|
| Directive | `Directive {Year}/{Number}/{Suffix}` | `Directive 2009/45/EC` |
| Regulation | `Regulation (EU) {Year}/{Number}` | `Regulation (EU) 2015/757` |
| Decision | `Decision {Year}/{Number}/{Suffix}` | `Decision 2009/17/EC` |

### E.4 EU-Specific Extraction Hints
- **Primary CT patterns**: CT1, CT5, CT8, CT9, CT12, CT18
- **Heavy on**: Actor (EU Commission, Member State, Notified Body), Enforcement (penalties, compliance), Environment (MRV, EU ETS), Document (EU certificates)
- **Deontic patterns**: "shall", "shall ensure", "Member States shall" -- EU legislation uses strong obligation language
- **EU-specific actors**: "Commission", "Member State", "notified body", "recognised organisation" (EU-specific meaning)
- **Normative_Status**: Directives and Regulations = `mandatory`; Recommendations = `recommendatory`
- **Cross-reference**: EU instruments frequently reference IMO conventions -- tag `[implements: {IMO instrument}]` in Editor_Note

---

*Unified Phase 1 scope: CONTROLLED_TERM across IMO/IACS/KR/EU sources, 16-column flat table, 20 Term_Category values, 16 Domain_Facet values, CT1-CT18 extraction patterns, SYN1-SYN6 synonym patterns, HIE1-HIE6 hierarchy patterns, Common Core + 5 Source-Family Annexes (A: IACS, B: IMO Conventions, C: IMO Codes, D: Resolutions/Circulars, E: EU Legislation). Output: 3 final files (result TSV + summary MD + log MD) in `results/`, intermediate chunk files in `results/temp/`.*
