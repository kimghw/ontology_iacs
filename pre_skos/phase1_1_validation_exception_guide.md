# Phase 1.1: Validation Exception Management Guide

> **Purpose**: Phase 1.1 is not an additional extraction phase. It is a **QA exception layer** for managing comments that recur across iterative validation of Phase 1 outputs (TRUE_DEF, APPLICABILITY, CONTROLLED_TERM).
> **Scope**: Normalise recurring comments → classify root cause → patch guide or fix data → re-verify affected scope.
> **Ownership**: This guide is shared across all three Phase 1 instructions. Each instruction references this document rather than duplicating the rules.

---

## 1. When to Escalate to Phase 1.1

A comment qualifies for the Phase 1.1 issue register **only** when it meets at least one of the following criteria:

| # | Criterion | Description |
|:---:|:---|:---|
| E1 | **Recurrence** | The same or equivalent comment has appeared 2+ times, or across 2+ documents/records |
| E2 | **Blocking** | The issue prevents validator pass (structural or semantic error) |
| E3 | **Ambiguous guide** | Current guide text alone cannot resolve the issue — reviewers disagree on the correct action |
| E4 | **Boundary dispute** | Whether the item belongs to Phase 1 or Phase 2 is unclear |

### Items that do NOT belong in Phase 1.1

- Typos and one-off data errors → fix directly in the result file
- Already-resolved issues → close in the original log
- Items clearly tagged `[Phase 2: ...]` with no boundary ambiguity → leave in Phase 2 backlog
- One-time reviewer questions answered by re-reading the guide → no register entry needed

---

## 2. Issue Register Schema

The issue register is a single TSV file shared across all three record types.

```
Issue_ID | Affected_Instruction | Issue_Scope | Concept_ID | Source_Doc | Source_Locator | Issue_Type | Severity | Comment_Text | Root_Cause | Disposition | Status | First_Seen_Iteration | Last_Seen_Iteration | Recurrence_Count
```

### 2.1 Column Definitions

| # | Column | Obligation | Data Type | Rule |
|:---:|:---|:---:|:---|:---|
| 1 | **Issue_ID** | **Required** | ID | Format: `P11_{SeqNo}`. Auto-increment. E.g., `P11_001` |
| 2 | **Affected_Instruction** | **Required** | enum-multi | Which instruction(s) the issue pertains to. Values: `TRUE_DEF`, `APPLICABILITY`, `CONTROLLED_TERM`, `COMMON`. Semicolon-delimited for multi-instruction issues. **Usage guide**: Use a specific instruction name (or semicolon-delimited pair, e.g., `TRUE_DEF; CONTROLLED_TERM`) when the issue affects concrete records or rules in those instructions. Use `COMMON` only for schema-wide structural issues that affect all three instructions equally (e.g., shared Concept_ID normalization rules, shared Source_Doc_Type enum, shared Normative_Status values, base URI pattern). |
| 3 | **Issue_Scope** | **Required** | enum | Granularity of the affected area. Values: `record` (specific Concept_ID), `source_doc` (all records from one source document), `instruction` (all records under one instruction), `cross_instruction` (shared rule / enum / schema across multiple instructions) |
| 4 | **Concept_ID** | Conditional | ID | The affected record's Concept_ID. **Required** when Issue_Scope = `record`. Leave blank for broader scopes |
| 5 | **Source_Doc** | Conditional | text | Source document where the issue was observed. **Required** when Issue_Scope = `record` or `source_doc` |
| 6 | **Source_Locator** | Conditional | text | Section/paragraph within the source document |
| 7 | **Issue_Type** | **Required** | enum | See Section 2.2 |
| 8 | **Severity** | **Required** | enum | `blocking` (prevents validator pass), `major` (data quality impact), `minor` (cosmetic or edge-case) |
| 9 | **Comment_Text** | **Required** | text | Verbatim or normalised comment describing the issue |
| 10 | **Root_Cause** | **Required** | enum | See Section 2.3 |
| 11 | **Disposition** | **Required** | enum | See Section 2.4 |
| 12 | **Status** | **Required** | enum | `open`, `in_progress`, `resolved`, `deferred` |
| 13 | **First_Seen_Iteration** | **Required** | integer | The validation iteration in which the issue was first identified (1, 2, 3, ...) |
| 14 | **Last_Seen_Iteration** | **Required** | integer | The most recent validation iteration in which the issue was observed. Equals First_Seen_Iteration when first logged; updated on each recurrence |
| 15 | **Recurrence_Count** | **Required** | integer | Total number of iterations in which this issue was observed. Starts at 1; incremented each time the issue recurs |

### 2.2 Issue_Type Values

| Value | Description |
|:---|:---|
| `schema_conflict` | Column definition or schema mismatch across instructions |
| `enum_mismatch` | Controlled value not in closed list, or list inconsistency between instructions |
| `record_boundary` | Unclear whether text produces one record or multiple, or which Record_Type applies |
| `traceability` | Structured column value not traceable to anchor/source text |
| `split_merge` | Ambiguity on whether to split or merge concepts/records |
| `cross_reference` | Unresolved or incorrect cross-source reference (Implements_Requirement, Normative_Basis, etc.) |
| `normative_force` | Disagreement on Normative_Status assignment |
| `language_tag` | Language tag inconsistency (@en vs @en-GB, British vs American spelling) |
| `deduplication` | Unclear whether a term/record is a duplicate or a distinct entry |

### 2.3 Root_Cause Values

| Value | Description |
|:---|:---|
| `guide_gap` | Current instruction does not address this situation |
| `guide_ambiguity` | Instruction text is ambiguous — multiple valid interpretations |
| `guide_conflict` | Two rules within the same instruction (or across instructions) conflict |
| `source_ambiguity` | Source document itself is ambiguous or contradictory |
| `extraction_error` | Extractor misapplied a clear rule |
| `validator_limitation` | Validator cannot express the required constraint |

### 2.4 Disposition Values

| Value | Description |
|:---|:---|
| `fix_data` | Correct the affected record(s) in the result file |
| `fix_guide` | Patch the instruction document to resolve ambiguity |
| `fix_both` | Both data and guide require changes |
| `defer_phase2` | Confirmed as Phase 2 scope — remove from Phase 1.1 tracking |
| `false_positive` | On review, the comment was incorrect or already resolved |
| `needs_human_decision` | Cannot be resolved by rule alone — requires domain expert input |

---

## 3. Workflow

```
Step 1   During validation, identify a comment that meets escalation criteria (Section 1)
Step 2   Check existing issue register — if a matching Issue_ID exists:
           - Update Last_Seen_Iteration to the current iteration number
           - Increment Recurrence_Count by 1
           - Update Status as appropriate
           - Do not create a duplicate entry
Step 3   If new, create a register entry:
           - Set Affected_Instruction and Issue_Scope
           - Set Issue_Type, Severity, Root_Cause
           - Set First_Seen_Iteration = Last_Seen_Iteration = current iteration
           - Set Recurrence_Count = 1
Step 4   Assign Disposition:
           - fix_data → apply correction to result TSV, mark Status = resolved
           - fix_guide → draft guide patch, apply, mark Status = resolved
           - fix_both → apply both, mark Status = resolved
           - defer_phase2 → move to Phase 2 backlog, mark Status = deferred
           - needs_human_decision → flag for review, mark Status = open
Step 5   Re-verify at the scope indicated by Issue_Scope:
           - record     → re-verify only the specific Concept_ID(s)
           - source_doc → re-verify all records from that Source_Doc
           - instruction → re-verify all records under that instruction
           - cross_instruction → re-verify affected records across all
             instructions that share the changed rule/enum/schema
Step 6   Update register Status
```

---

## 4. File Naming and Versioning

**Critical rule**: Unlike Phase 1 result files which overwrite on each run, the Phase 1.1 issue register is **versioned and never overwritten**. This is essential for tracking whether the same comment recurs across iterations.

| File | Name Pattern | Location |
|:---|:---|:---|
| Issue register | `phase1_1_issue_register_{YYYYMMDD}_v{NN}.tsv` | `results/phase1_1/` |
| Guide patches | `phase1_1_guide_patch_{YYYYMMDD}_v{NN}.md` | `results/phase1_1/` |

- `{YYYYMMDD}`: Date of creation
- `v{NN}`: Version within the same date (v01, v02, ...)
- The `results/phase1_1/` directory shall be created automatically if it does not exist
- Previous versions are retained — **do not delete or overwrite**

---

## 5. Convergence Criteria

Phase 1.1 is considered converged when **all** of the following are true:

1. No `blocking` issues remain with Status = `open` **or** `in_progress` (both must be resolved or deferred)
2. No `major` issues remain with Status = `open` (must be resolved, deferred, or downgraded to `minor`)
3. No issue has recurred for 2 consecutive iterations (i.e., `Last_Seen_Iteration` has not increased for at least 2 full iterations)
4. All `fix_guide` dispositions have been applied to the relevant instruction documents
5. All `needs_human_decision` items have been resolved or explicitly deferred to Phase 2

At convergence, the latest issue register version becomes the Phase 1 QA signoff artifact.

---

*Phase 1.1 scope: QA exception management across TRUE_DEF / APPLICABILITY / CONTROLLED_TERM. Not an extraction phase — a validation convergence layer. 15-column versioned issue register, 4-level Issue_Scope (record / source_doc / instruction / cross_instruction), 9 issue types, 6 root causes, 6 dispositions. Iteration tracking via First_Seen / Last_Seen / Recurrence_Count. Escalation by recurrence, blocking severity, guide ambiguity, or Phase 1/2 boundary dispute.*
