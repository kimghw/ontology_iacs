# IACS UR Applicability Taxonomy

## Architecture: 6-Element Model (5 Search Axes + 1 Meta Layer)

| Element | Name | Role | Default Priority |
|---|---|---|---|
| 1 | Target & Technical Domain | What/whom does this regulate? | #1 (strongest filter) |
| 2 | Vessel/Unit Profile | What kind of vessel/unit? | #2 |
| 3 | Applicability Predicates | Numeric + qualitative criteria | #5 |
| 4 | Normative & Lifecycle Context | Legal basis + enforcement + stage | #4/#7 (early promotion possible) |
| 5 | Temporal Applicability | When does it apply? | #6 |
| 6 | Exceptions & Precedence | Final judgment logic (meta layer) | #8 |

> **Adaptive priority:** Default order above, but if the query mentions SOLAS/IGC/IGF/MODU Code or specific dates, promote that axis early.

---

## Element 1: Target & Technical Domain

### Internal Slot Structure

| Slot | Description | Examples | Role | Unknown Handling |
|---|---|---|---|---|
| `target_entity` | Type of entity being regulated | Ship, Equipment, Engine, Material, Personnel, Service Supplier, Software, Certification Scheme | hard_gate | must_ask |
| `technical_domain` | Technical category (L1) | Hull Structure, Machinery & Propulsion, etc. | soft_signal | infer from target_object |
| `target_object` | Specific regulated object (L2/L3) | Steering Gear, IC Engine, Hatch Cover, Steel Plate, Welding Procedure, NDT Service, etc. | hard_gate | must_ask |

### target_entity Values

| Value | Description | Example URs |
|---|---|---|
| Ship/Vessel/Unit | Ship/unit design/construction/survey | A2, D1~D8, D11, M42, S11A, Z7, most URs |
| System | Integrated onboard systems (power, control, cargo, ballast, etc.) | C7, E24, E25, E26, E27, G3, M74, M86 |
| Equipment | Equipment type approval/testing/certification | A3, E7, E10, E18, E21, G5, M51, M67, M71, M82, M85, P2.11, P2.12, P6 |
| Engine | Engine type approval/certification/testing | M44, M78, M87, M88 |
| Material | Material manufacture/testing/certification | W7, W8, W9, W10, W11, W16, W24, W27, W31 |
| Personnel | Welder and other personnel qualification | W32 |
| Service Supplier | NDT firms, service supplier approval | W35, Z17 |
| Software | Onboard software approval | L5, C6 |
| Certification Scheme | Manufacturer certification scheme | Z26 |

### technical_domain (7 Level-1 Categories)

#### 1.1 Hull Structure (~37 URs)

| L2 Subcategory | URs |
|---|---|
| Global Strength, Loading & Stability | S1, S1A, S2, S4, S5, S6, S7, S11, S11A, S17, S20, S22, S34, L2, L5 |
| Local Structure & Structural Details | S3, S10, S12, S13, S18, S19, S23, S31, S33 |
| Hatch Covers, Doors & Access Openings | S8, S9, S15, S16, S21, S26, S30, S35 |
| Deck Fittings, Chain Lockers & Forecastle | A2, S27, S28, L4 |
| Corrosion Protection | Z8, Z9 |
| MODU Structure (regime_tag) | D4, D5, D6, D7 |
| Polar Structure | I2 |

#### 1.2 Machinery & Propulsion (~33 URs)

| L2 Subcategory | URs |
|---|---|
| IC Engines & Engine Safety | M2, M3, M9, M10, M11, M12, M28, M44, M51, M61, M67, M71, M78, M82, M87, M88 |
| Propulsion, Shafting & Propellers | M25, M34, M52, M85, K3 |
| Steering Gear | M42 |
| Turbines & Gears | M26, M56 |
| Auxiliary & Essential Services | A3, M40, M43, M46, M57, M84, M80 |
| Environmental Systems | M74, M77, M86 |
| MODU General/Design (regime_tag) | D1, D2, D3, D8, D11 |
| Polar Machinery | I3 |

#### 1.3 Electrical & Control (~14 URs)

| L2 Subcategory | URs |
|---|---|
| Power Generation & Distribution | E24, M80 |
| Control, Monitoring & Alarm | E10, E25, M29, M30, M35, M36 |
| Cables, Batteries & UPS | E7, E18, E21 |
| Cyber Resilience | E26, E27 |

#### 1.4 Cargo & Process Systems (~10 URs)

| L2 Subcategory | URs |
|---|---|
| Container Securing & Lashing | C6, C7 |
| Gas Cargo Containment & Process | G1, G3, G5 |
| Cargo, Ballast & Bilge Systems | F44, F45, M64, M65 |
| Fuel Installations & Alternative Fuels | M76, M24 |
| Tanker Fire & Gas Safety | F5, F6, F7, F8 |

#### 1.5 Piping & Pressure Equipment (~6 URs)

| L2 Subcategory | URs |
|---|---|
| Piping Design & Components | P2, P2.11, P2.12, P3 |
| Pressure / Heat-Recovery Equipment | P6 |
| Inert Gas / Tank Atmosphere | F20.4 |

#### 1.6 Materials, Welding & NDT (~17 URs)

| L2 Subcategory | URs |
|---|---|
| Steels | W11, W16, W31 |
| Castings & Forgings | W7, W8, W9, W10 |
| Welding & Welder Qualification | W23, W28, W32 |
| NDT / ANDT / Service Suppliers | W33, W34, W35 |
| Propeller Materials | W24, W27 |
| Anchors & Chains | W22, W29 |

#### 1.7 Survey, Certification & Maintenance (~26 URs)

| L2 Subcategory | URs |
|---|---|
| Hull Surveys (ESP) | Z1, Z3, Z6, Z7, Z7.1, Z7.2, Z10.1, Z10.2, Z10.3, Z10.4, Z10.5, Z11, Z15, Z24, Z28 |
| Cargo Installation Surveys | Z16 |
| Machinery Surveys | Z18, Z21, Z25 |
| New Construction Survey | Z23 |
| Service Suppliers & Calibration | Z17, Z19 |
| Certification Schemes | Z26, M87 |
| Maintenance, PMS & Remote Survey | Z13, Z20, Z27, Z29 |

### Cross-Domain Tags

| Tag Type | Values | Example URs | Role |
|---|---|---|---|
| `nature_tag` | Safety, Protection, Fire, Explosion | F5, F6, F7, F8, F45, M12, M75, M79, D8, D11 | soft_signal |
| `regime_tag` | MODU_Regime, Polar_Regime | D1~D8, D11, I1~I3 | hard_gate (canonical for MODU/Polar) |

---

## Element 2: Vessel/Unit Profile

### Internal Slot Structure (6 slots)

| Slot | Name | Description | Role | Unknown Handling |
|---|---|---|---|---|
| 1 | `ship_or_unit_type` | Basic vessel/unit classification | hard_gate | must_ask |
| 2 | `cargo_service` | Cargo type or service characteristic | derived | infer from ship_or_unit_type |
| 3 | `operational_condition` | Operating condition/mode | soft_signal | default: "not specified" |
| 4 | `design_notation_or_feature` | Design attributes/class notation | hard_gate | must_ask if candidate UR references CSR/Polar/hull type/ESP |
| 5 | `fuel_or_energy_mode` | Fuel/energy type | hard_gate | must_ask if gas/LFL/ammonia UR is candidate; else assume Conventional |
| 6 | `equipment_trigger` | Equipment/system presence condition | hard_gate | must_ask if relevant UR candidate exists |

### Slot 1: ship_or_unit_type

| Value | Description | Dedicated URs |
|---|---|---|
| All Vessels/Units | No type restriction | ~72 URs |
| Oil Tanker | Crude oil / petroleum tankers | F6, F7, F8, M24, S13, Z10.1, Z10.4 |
| Bulk Carrier | Dry bulk cargo carriers | M65, S1A, S12, S17~S23, S28, S30, S31, Z9, Z10.2, Z10.5 |
| Container Ship | Dedicated container carriers | C6, C7, S11A, S33, S34, W31 |
| Gas Carrier | LNG/LPG carriers | F20.4, G1, G3, G5, Z7.2, Z16 |
| Chemical Tanker | IBC Code vessels | Z10.3 |
| Ro-Ro | Ro-Ro passenger and cargo ships | S8, S9, S15, S16, Z24 |
| MODU | Mobile offshore drilling units *(→ derived from: regime_tag.MODU_Regime)* | D1~D8, D11, E26, E27, W22, Z15 |
| Passenger Ship | International voyage passenger vessels | (E26, E27 shared) |
| General Cargo Ship | General dry cargo | Z7.1 |
| Fishing Vessel | Fishing vessels | M57 |
| Offshore Unit | Non-drilling offshore units | W16, W22 |
| Tanker (Oil+Chemical) | Shared oil and chemical tankers | F5, F20.4, F44, M64, M76, Z11 |
| Tanker (Oil+Chemical+Gas) | Shared oil, chemical and gas tankers | F20.4 |

### Slot 2: cargo_service

| Value | Description | Related URs |
|---|---|---|
| Crude Oil / Petroleum Products | Oil tanker cargoes | F6, F7, F8, F20.4, F44, M24, M76, S13, Z10.1, Z10.4 |
| Liquefied Gas / LNG / LPG | Gas carrier cargoes | G1, G3, G5, F20.4, Z7.2, Z16 |
| Chemicals / IBC Code | Chemical tanker cargoes | F20.4, F44, M64, M76, Z10.3 |
| Solid Bulk Cargo | Bulk carrier cargoes | M65, S1A, S12, S17~S23, S28, S30, S31, Z9, Z10.2, Z10.5 |
| Containers | Container ship cargoes | C6, C7, S11A, S33, S34, W31 |
| Towing & Mooring | Towing/mooring operations | A2, M79 |
| Offshore Drilling | MODU drilling operations | D1~D8, D11, Z15 |
| (not specified) | General/all | Most URs |

### Slot 3: operational_condition

| Value | Description | Related URs |
|---|---|---|
| Unrestricted Service | No area restriction | M28, S11, S11A |
| International Voyage | SOLAS international voyage *(→ derived from: normative_basis.SOLAS)* | E26, E27, M43, S8, S9, Z23 |
| Domestic Voyage | Non-international voyage | S8, S9, S15, S16 |
| Polar Waters | Ice-infested polar regions *(→ derived from: regime_tag.Polar_Regime)* | I1, I2, I3 |
| Offshore Operations | Offshore drilling/construction *(→ derived from: regime_tag.MODU_Regime)* | D1~D8, D11, W16, W22, Z15 |
| Port / Terminal Operations | Close quarters, harbors | M79 |
| Fresh Water / Harbour | Freshwater or harbour operations | Z3 |
| (not specified) | General operations | Most URs |

### Slot 4: design_notation_or_feature

| Value | Description | Related URs |
|---|---|---|
| CSR Ship | Common Structural Rules applied *(← canonical for CSR)* | S series exclusions |
| Double Hull | Double hull construction | Z10.4 |
| Double Skin | Double skin construction (bulk carriers) | Z10.5 |
| Single Side Skin | Single side skin construction | S12, S23, S31, Z10.1, Z10.2 |
| Ice Class / Polar PC1-PC7 | Polar Class notation *(→ derived from: regime_tag.Polar_Regime)* | I1, I2, I3 |
| ESP | Enhanced Survey Programme | Z10.1~Z10.5, Z11, Z17 |
| Self-Elevating | MODU subtype | D4 |
| Column-Stabilized | MODU subtype | D5 |
| Surface-Type | MODU subtype | D6 |

### Slot 5: fuel_or_energy_mode

| Value | Description | Related URs |
|---|---|---|
| Conventional Fuel | Standard fuel oil | Most URs |
| Gas Fuelled / IGF Code | Natural gas fuel | M78, M82, Z25 |
| Low Flashpoint Fuel | IGF Code fuels broadly | Z25 |
| Crude Oil as Fuel | Crude oil/slops as boiler fuel | M24 |
| Ammonia | Ammonia refrigerant/fuel | M57 |
| (not specified) | Fuel-agnostic | |

### Slot 6: equipment_trigger

| Value | Description | Related URs |
|---|---|---|
| Gas Fuel Engine | Natural gas fuelled IC engine | M78, M82, Z25 |
| BWMS Installed | Ballast Water Management System | M74, F45 |
| Harmonic Filter Installed | Harmonic filters on main busbars | E24 |
| EGCS Installed | Exhaust Gas Cleaning System | M86 |
| SCR System Installed | SCR reductant storage system | M77 |
| Unattended Machinery Space | Periodically unattended machinery | M29, M30, M35, M36, Z20 |
| Crosshead Engine | Crosshead type IC engine | M12 |
| Steam Turbine | Main/auxiliary steam turbine | M26 |
| Towing Winch | Port/terminal towing winch | M79 |
| Stability Software | Onboard stability calculation SW | L5 |
| UPS Unit | Uninterruptible Power Supply | E21 |
| Battery System | Essential/emergency batteries | E18 |
| Economizer (Isolated) | Shell type economizer, isolated | P6 |
| OT/CBS Systems | Operational Technology / CBS | E26, E27 |
| Inert Gas System | Inert gas system on tanker | F7 |

---

## Element 3: Applicability Predicates

> **Role classification:** All `quantitative_thresholds` are **hard_gate** (Unknown Handling: must_ask if candidate UR has a threshold). All `qualitative_predicates` are **hard_gate** except engine type and construction type which may be **derived** from target_object or equipment_trigger.

### quantitative_thresholds

| Type | Values | Related URs |
|---|---|---|
| Length (L) | >= 24m | L2, L4, S10 |
| Length (L) | >= 65m | S1 |
| Length (L) | >= 80m | S26, S27 |
| Length (L) | >= 90m | S6, S7, S11, S11A |
| Length (L) | >= 150m | S1A, S17, S18, S19, S20, S22, S34, Z10.5 |
| Length (L) | >= 290m | S34 (global analysis) |
| Length (L) | 90-500m | S7, S11A |
| Gross Tonnage (GT) | >= 500 | A2, M42, E26, E27, Z7.1 |
| Power (kW) | > 37 kW | M2 |
| Power (kW) | >= 110 kW | M56 (aux), M87 (simplified below) |
| Power (kW) | >= 220 kW | M56 (main propulsion) |
| Cylinder bore | >= 200 mm | M9 |
| Cylinder bore | <= 230 mm | M11 (exemption) |
| Crankcase volume | >= 0.6 m3 | M9 |
| Steel thickness | > 50 mm, <= 100 mm | S33, W31 |
| Steel plate thickness | <= 100 mm (plates), <= 50 mm (sections) | W11 |
| Cargo density | >= 1.0 t/m3 | S17, S18, S20 |
| Cargo density | >= 1.78 t/m3 | S19, S22 |
| SCR tank volume | >= 500 L | M77 |
| Anchor mass | <= 1500 kg | W29 (SHHP) |
| Ship proportions | L/B, B/T, Cb ranges | S11A |

### qualitative_predicates

| Condition Type | Example Values | Related URs |
|---|---|---|
| Engine type | Crosshead type engine | M12 |
| Engine type | Crosshead and trunk-piston engine | M35 |
| Engine type | Trunk-piston engine | M36 |
| Construction type | Single deck, topside/hopper tanks | S12, M65 |
| Construction type | Vertically corrugated transverse watertight bulkheads | S18, S19 |
| Steel grade | YP36, YP40, YP47 | S33, W31 |
| Equipment presence | Harmonic filters on main busbars | E24 |
| Equipment presence | BWMS fitted | M74, F45 |
| Equipment presence | Towing winch in close quarters | M79 |
| Ship status | Built before 30 June 1996 | S15, S16 |
| Ship status | Not built per UR S21(Rev.3) | S30 |
| Ship status | Not built per UR S12 Rev.1 | S31 |
| Tank type | Integral tanks (not independent) | Z10.3 |
| Service condition | Ships of unrestricted service | M28, S11 |
| Statutory condition | Subject to MARPOL Annex I Reg.18 | S13 |
| Statutory condition | SOLAS II-2/4.5.5.1 and 4.5.5.2 do not apply | F20.4 |
| Manufacturing condition | New engine type for classification | M71 |
| Qualification condition | Welders engaged in fusion welding | W32 |
| Service condition | NDT firms for new construction | W35 |
| Material condition | Steel construction only | I1, I2, I3 |

---

## Element 4: Normative & Lifecycle Context

### normative_basis

> **Role:** hard_gate (when explicitly mentioned in query) / soft_signal (when inferred). **Unknown Handling:** promote to hard_gate if query mentions SOLAS/IGC/IGF/MODU Code.
> When query mentions SOLAS/IGC/IGF/MODU Code, promote this axis early as primary filter.

| Value | Gate Role Example | Related URs |
|---|---|---|
| SOLAS | Z23 excludes SOLAS I/3 ships *(← canonical for SOLAS/International Voyage)* | E21, E26, M42, M43, S8, S9, Z23 |
| MARPOL | S13 requires MARPOL Annex I Reg.18 | S13 |
| Load Line Convention (1966/1988) | P3 applies only when required by LLC | L2, L4, L5, P3, S3 |
| BWM Convention | M74 applies in addition to BWM Conv. | M74, F45 |
| IGC Code | G1 excludes MSC.370(93) vessels; P2 excludes IGC piping | G1, G3, G5, P2(excl.) |
| IGF Code | M78 references IGF Code requirements; P2 excludes IGF piping | M78, Z25, P2(excl.) |
| MODU Code | Base regime for D1~D11, Z15 *(→ derived from: regime_tag.MODU_Regime)* | D1~D11, L5, Z15 |
| IS Code 2008 | One of L5's applicability bases | L5 |
| FSS Code | One of E21's applicability conditions | E21 |
| IBC Code | Z10.3 prerequisite; P2 exclusion | Z10.3, P2(excl.) |
| CSR | Exclusion condition for 17 S-series URs *(→ derived from: design_notation_or_feature.CSR Ship)* | S series |

### enforcement_mode

> **Role:** output_only — determined after UR identification, not used for filtering.

| Value | Description | Example |
|---|---|---|
| Mandatory | Compulsory application | Most URs |
| Guidance | Non-mandatory guidance | E26 non-mandatory vessels |
| Society Discretion | At individual society's judgment | M56 below 110kW, M57 below 25kg |

### lifecycle_stage

> **Role:** soft_signal (helps narrow candidates) / output_only (included in result). **Unknown Handling:** default "not specified", infer from query_intent.

| Value | Description | Example URs |
|---|---|---|
| Design Approval | Initial design review | S11A, S34, M44, P2 |
| Construction | Building phase | W28, W32, W33, Z23 |
| Type Approval / Testing | Equipment type approval | E10, M51, M67, M71, M82, M85, M87 |
| Shop Test (FAT) | Factory acceptance test | M51, M88 |
| Onboard Test / Trials | Shipboard trials | M88, M25 |
| Certification | Product/system certification | M87, W24, W27, Z26 |
| In-Service Survey | Periodic classification survey | Z1, Z3, Z7, Z10.x, Z18, Z21 |
| Maintenance / PMS | Planned maintenance | Z13, Z20, Z27 |
| Retrofit / Conversion | Existing ship modification | S15, S16, S19, S22, S23 |

---

## Element 5: Temporal Applicability

### Internal Slot Structure

| Slot | Description | Role | Unknown Handling |
|---|---|---|---|
| `trigger_event` | Event type that triggers application | hard_gate | infer from lifecycle_stage; must_ask if ambiguous |
| `trigger_date` | Reference date | hard_gate | must_ask |
| `revision_or_version` | Applicable revision/version | derived | resolve from trigger_date + UR revision history |

### trigger_event Values

| Value | Description | Example URs |
|---|---|---|
| Contracted for Construction | Construction contract date | A2, S11A, E7, E24, E26, E27, M42, most URs |
| Keel Laid | Keel laying or similar stage | L4 |
| Ship Delivered | Ship delivery date | Z21 |
| Application for Type Approval | Type approval application date | E10, M71, M78, M87 |
| Application for Certification | Equipment/engine certification date | A3, M9, M35, M67, M80 |
| Application for System Approval | System/plan approval application | M76, F45 |
| Survey Commenced | Survey commencement date | Z13, Z20, Z24, Z29 |
| Application for Welder Qualification | Welder qualification application | W32 |
| Application for Manufacturer Approval | Manufacturer approval application | W31, W11 |
| Request for Class | Class application date | Z9 |

### Example Records

| trigger_event | trigger_date | revision_or_version | UR |
|---|---|---|---|
| Contracted for Construction | on or after 1 July 2024 | Rev.1 | E26 |
| Contracted for Construction | on or after 1 January 2027 | Rev.8 | S10 |
| Application for Type Approval | on or after 1 January 2027 | - | M87 |
| Survey Commenced | on or after 1 January 2023 | - | Z29 |
| Keel Laid | on or after 1 July 2003 | - | L4 |
| Ship Delivered | on or after 1 January 2016 | Rev.3 | Z21 |

---

## Element 6: Exceptions & Precedence (Meta Layer)

| Rule Field | Description | Example |
|---|---|---|
| `excludes_if` | UR does NOT apply when condition is true | "CSR Bulk Carriers", "CSR Oil Tankers", "High Speed Craft", "Special Purpose Ships", "Offshore Units" (A2); "Escort/Canal/Emergency towing" (A2); "Boiler integral pipes" (P2); "Low flashpoint fuel piping" (P2); "Fixed fire extinguishing hoses" (P2.12); "Welding procedure per UR W1" (W28); "Oxy-acetylene welding; pipes and pressure vessels" (W32); "SOLAS I/3 ships; HSC; MODUs" (Z23) |
| `unless` | Conditional exception | "unless flag Administration decides otherwise" |
| `alternative_rule` | Rule to apply instead when excluded | "P2 excluded → IGC/IGF Code piping requirements apply" |
| `superseded_by` | Replaced by another UR | "K2 → W24", "S21A → S21 Rev.6" |
| `overrides_if` | This UR takes precedence | "SOLAS II-1/55 statutory reqs override UR M24" |
| `hybrid_split` | Zone-based split within same vessel | "Z10.2 (single skin holds) + Z10.5 (double skin holds)" |
| `discretionary_if` | Application at society's discretion | "M56: below 110kW may be applied at society's request" |
| `guidance_only` | Non-mandatory guidance | "E26: cargo ships < 500GT, fishing vessels are guidance only" |
| `retrospective_only` | Retroactive to existing ships only | "S15, S16: Ro-Ro pax built before 30 June 1996" |
| `mutually_exclusive` | Cannot apply simultaneously | "Z10.1 (single hull) vs Z10.4 (double hull)"; "Z10.2 (single skin BC) vs Z10.5 (double skin BC)" |
| `also_applies_to` | Additional applicability | "CSR ships: S1 applies in addition to CSR" |

### Evaluation Order (runtime)

The following order MUST be applied sequentially for each candidate UR:

| Step | Check Fields | Output Status | Action | Description |
|---|---|---|---|---|
| 1 | `superseded_by` | `not_applicable` | Exclude | UR replaced or withdrawn → exclude, do NOT proceed |
| 2 | `excludes_if`, `retrospective_only`, `mutually_exclusive` | `not_applicable` | Exclude or Branch | Exclusion condition met → exclude; if `alternative_rule` exists for this UR → add alternative to candidate list |
| 3 | `hybrid_split` | (split) | Split | Mixed-zone vessel → split into zone-specific UR pairs, re-enter Step 4 for each |
| 4 | `unless`, `overrides_if`, `also_applies_to` | (modify) | Adjust | `unless` may reinstate an excluded UR; `overrides_if` adjusts precedence; `also_applies_to` adds companion UR |
| 5 | `discretionary_if`, `guidance_only` | `guidance_only` | Flag | Not mandatory → set enforcement_mode in output |

> **Control flow:**
> - Step 1 exclude → skip Steps 2~5 entirely.
> - Step 2 exclude → check if `alternative_rule` exists; if yes, add the alternative UR to the candidate list (the alternative re-enters at Step 1). If no, mark `not_applicable` and stop.
> - Step 3 split → each zone-UR pair proceeds independently through Steps 4~5.
> - Step 4 adjust → `unless` can override a Step 2 exclusion (e.g., "unless flag Administration decides otherwise"); `overrides_if` resolves conflicts between two applicable URs.
> - After Step 5, remaining candidates that passed all checks → `applicable` (or `guidance_only` if flagged).
>
> **Mapping of Element 6 fields not in table:**
> - `alternative_rule`: triggered as a sub-action of Step 2 (see control flow above)
> - `retrospective_only`: evaluated as a specialized `excludes_if` in Step 2 — excludes ships NOT matching the retroactive condition (canonical source: Element 5 `trigger_date` / Element 3 `qualitative_predicates`)

---

## Agent Query Processing Workflow

### Step 0: Extract target_entity + target_object + query_intent

#### query_intent Values

> `query_intent` determines the system's processing mode. A single query maps to exactly one intent. Multi-intent queries (e.g., "documents and tests needed") should be decomposed into separate processing passes.

| Value | Description | System Action | Example Query |
|---|---|---|---|
| `applicability_check` | Determine which URs apply | Run Element 1~6 filtering pipeline | "What URs apply to a 100m container ship?" |
| `requirement_lookup` | Retrieve specific requirements from applicable URs | Find applicable URs first, then extract requirement_aspect | "What documents are needed for engine type approval?" |
| `revision_check` | Determine applicable revision/date | Resolve temporal applicability (Element 5) | "Which revision of S11A applies for 2024 contract?" |
| `exception_check` | Check exclusions or exemptions | Focus on Element 6 evaluation | "Is there an exemption for ships under 500GT?" |

#### requirement_aspect Values (output filter, used when query_intent = requirement_lookup)

| Value | Description | Example |
|---|---|---|
| `documents` | Required submissions (docs, drawings, plans, manuals) | Approval drawings, operating manuals |
| `calculations` | Required calculations and analyses | Structural analysis, stability calculation |
| `test_inspection` | Required tests, inspections, trials (FAT, onboard, survey) | FAT, sea trial, ESP inspection items |
| `certificate` | Required certificates and approvals | Type approval certificate, manufacturer approval |
| `procedure` | Required procedures and specifications | Welding procedure, NDT specification |

> **Note:** `query_intent` and `requirement_aspect` are agent runtime fields, not UR taxonomy attributes. They determine *what the user wants to know*, not *what the UR regulates*. `requirement_aspect` values are mutually exclusive output filters applied after UR identification.

#### Examples

```
Query: "What documents are needed for engine type approval?"
→ target_entity: Engine
→ target_object: IC Engine (regulated object)
→ query_intent: required_documents
→ requirement_aspect: documents
→ Immediate candidate: M44
```

```
Query: "NDT supplier approval requirements"
→ target_entity: Service Supplier
→ target_object: NDT Service (regulated object)
→ query_intent: certification_path
→ Immediate candidates: W35, Z17
```

```
Query: "Does UR S11A apply to my 120m container ship contracted in 2024?"
→ target_entity: Ship
→ target_object: Hull Structure (regulated object)
→ query_intent: applicability_check
→ Immediate candidate: S11A
  (ship_or_unit_type: Container Ship → resolved in Step 1)
```

### Step 1: Extract technical_domain + vessel/unit profile (~80% reduction)

```
Query: "Longitudinal strength rules for 100m container ship contracted in 2024"
→ technical_domain: Hull Structure > Global Strength
→ ship_or_unit_type: Container Ship
→ Candidates: S11A, S34
```

### Step 2: Re-interrogation (adaptive priority)

**Default order:**
1. target_entity / target_object (if unclear)
2. technical_domain (if unclear)
3. ship_or_unit_type (if unclear)
4. equipment_trigger (if "All Vessels" and equipment-specific UR suspected)
5. design_notation_or_feature (CSR? Polar Class?)
6. fuel_or_energy_mode (Gas fuelled? Low flashpoint?)
7. lifecycle_stage (Design? Survey? Type Approval?)
8. quantitative_thresholds (Length? GT? Power?)
9. trigger_event + trigger_date (Contract date? Certification date?)

**Early promotion conditions:**
- Query mentions SOLAS/IGC/IGF/MODU Code → promote normative_basis to step 1-2
- Query mentions specific dates → promote temporal_applicability to step 3-4
- Query mentions "CSR" → promote design_notation_or_feature to step 2-3

### Step 3: Apply predicates + temporal trigger

```
→ L >= 100m: S11A applies (L >= 90m met)
→ Contract date 2024: S11A applicable revision (contracted on or after 1 July 2016)
```

### Step 4: Exception & precedence validation

```
→ excludes_if: S11A has no CSR exclusion (it IS the container ship standard)
→ superseded_by: S11 does NOT apply to container ships (S11A supersedes)
→ Final: S11A confirmed
```

### Step 5: Output

#### Output Status Values

| Status | Meaning | Boundary | Next Action |
|---|---|---|---|
| `applicable` | All hard_gate conditions passed, no exclusion triggered | All gates resolved to true | Return applicable UR with evidence |
| `not_applicable` | Excluded by superseded_by, excludes_if, or hard_gate failure | At least one gate definitively failed | Return exclusion reason and rule field |
| `conditionally_applicable` | All known gates passed, but 1+ soft_signal or non-critical gate remains unresolved | No gate failed, but resolution incomplete | Generate follow-up questions (priority 2~3) |
| `insufficient_information` | 1+ hard_gate value is unknown and no default exists | Cannot evaluate core gates | Generate follow-up questions (priority 1) |
| `guidance_only` | UR matched but enforcement_mode is Guidance or Society Discretion | Applicable but not mandatory | Flag enforcement mode, return UR with caveat |

#### Follow-up Question Schema

```json
{
  "field": "fuel_or_energy_mode",
  "question": "가스연료 또는 저인화점 연료 엔진인가요?",
  "reason": "IGF 관련 UR 분기 판정",
  "answer_type": "enum",
  "options": ["Gas Fuelled / IGF Code", "Low Flashpoint Fuel", "Conventional Fuel"],
  "priority": 1
}
```

| Parameter | Description | Values |
|---|---|---|
| `field` | Taxonomy slot to be resolved | Any slot name from Element 1~5 |
| `question` | Natural language question for user | Free text |
| `reason` | Why this information is needed | Free text |
| `answer_type` | Expected answer format | `enum` / `boolean` / `date` / `number` / `text` |
| `options` | Choices (when answer_type = enum) | Array of valid values |
| `priority` | Urgency level | 1 (must ask now) / 2 (important) / 3 (supplementary) |

> **Rule:** Maximum 3 questions per turn. Priority 1 questions first.

#### Output Example

```
[Applicable URs]
- UR S11A (Longitudinal Strength Standard for Container Ships)
  status: applicable
  evidence: Container ship, L >= 90m, contracted after 2016-07-01
  target_entity: Ship
  lifecycle_stage: Design Approval

[Also Consider]
- UR S34 (FEA Load Cases)
  status: insufficient_information
  missing: [length value — hard_gate >= 150m not evaluable]

[Excluded URs with Reasons]
- UR S11 — status: not_applicable — rule: superseded_by → S11A covers container ships
- UR S7 — status: not_applicable — rule: excludes_if → CSR BC/OT exclusion

[Follow-up Questions]
- { "field": "length", "question": "선박 길이(m)를 알려주세요.", "reason": "S34 FEA 화물창 해석 적용 판정 (>= 150m hard_gate)", "answer_type": "number", "priority": 1 }

[Routing Information]
- If CSR-applicable vessel → refer to CSR BC&OT rules (alternative_rule)
```

---

## Summary Statistics

| Category | Count |
|---|---|
| Total valid URs | 102 |
| Technical Domain L1 categories | 7 |
| Technical Domain L2 subcategories | 35 |
| target_entity types | 9 |
| Vessel/Unit Profile slots | 6 |
| Unique ship_or_unit_type values | 13 |
| Unique equipment_trigger values | 15 |
| Unique fuel_or_energy_mode values | 5 |
| qualitative_predicates types | 18+ |
| trigger_event types | 10 |
| Exception/precedence rule types | 11 |
| URs with CSR exclusion | 17 |
| URs with nature_tag=Safety | ~10 |
| URs with regime_tag=MODU | 10 |
| URs with regime_tag=Polar | 3 |
