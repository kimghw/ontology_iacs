# Phase 1 — Prerequisite Procedure (PRE)

> **Purpose.** Normalise heterogeneous source documents into Document units, produce a validated heading structure and chunk plan, and assign Work Units for downstream extraction. PRE does not perform Instruction-level extraction (TD, APP, CT) — that is handled separately.

> **Audience.** This document is an LLM execution directive (System Prompt). Agent runtimes such as Claude Code read this file and carry out the procedure automatically. It is NOT a manual for human operators.

---

## Inputs

| # | Input Item | Required | Description |
|:---:|:---|:---:|:---|
| 1 | Target documents | Required | Source documents to be processed — conventions, regulations, guidelines, etc. from IMO, IACS, KR, or other classification societies (`.md`, `.pdf`, `.html`, `.xml`, `.json`). Provided as a single file, multiple files, or a folder path |
| 2 | Shared definitions | Required | Terminology, identifiers, naming conventions, and classification taxonomy in the `shared/` directory (`project_definitions.md`, `naming_convention.md`, `document_classification.md`, `thresholds.yaml`) |
| 3 | Step-by-step guides | Required | Execution rules for each Stage (`step1_document_split.md`, `step2_heading_extraction.md`, `step3_workunit_packing.md`) |

> **Entry condition:** PRE begins as soon as the target documents are provided; Step 1.0 confirms the processing scope.

---

## Artefact Catalogue

### Promoted Artefacts (persistent — moved to `results/` after approval)

| # | Artefact | File Name | Produced by | Description |
|:---:|:---|:---|:---|:---|
| 1 | Heading structure TSV | `doc-{doc_instance_key}__heading__structure.tsv` | Step 2 | Final validated heading list with token measurements (inclusive + exclusive) |
| 2 | Heading regex spec | `doc-{doc_instance_key}__heading__regex_spec.json` | Step 2 | Finalised regex specification; reusable for same-DocType documents |
| 3 | File metadata | `file-{source_file_key}__pre__meta.json` | Step 1.1 | Original path, format, conversion date, character count, token count, parser version, line ending policy, grammar_version (set after heading extraction) |
| 4 | Normalised text | `file-{source_file_key}__pre__normalised.md` | Step 1.1 | Normalised document text (not generated for `.md` originals) |
| 4a | Document split | `doc-{doc_instance_key}__pre__split.md` | Step 1.2 | Per-document split file extracted from multi-document source files |
| 5 | Heading grammar | `doctype-{DocType}__heading__grammar_v{NN}.md` | Step 2 | Reusable heading grammar per DocType (managed by Coordinator) |
| 6 | WU metadata | `wu-{wu_key}__pre__meta.json` | Step 3.2 | WU composition, constituent docs, token counts |
| 7 | **PRE manifest** | `corpus__pre__manifest.json` | Step 3.3 | Master index of all PRE outputs — single entry point for downstream |
| 7a | Document manifest | `corpus__pre__document_manifest.jsonl` | Step 1.2 | Per-document registry: source path, split path, normalised path, hash, status |
| 7b | Chunk plan | `doc-{doc_instance_key}__heading__chunk_plan.json` | Step 3.1 | Chunk boundaries, token sizes; separate from heading structure TSV. Always promoted. |
| 7c | Final discrepancy log | `doc-{doc_instance_key}__heading__discrepancy_final.tsv` | Step 2 | Retained Warning/Info entries for post-approval audit trail |
| 8 | Coverage report | `doc-{doc_instance_key}__heading__coverage.json` | Step 2 Pass 4 | Line-level classification audit (heading vs non-heading). Conditionally promoted (on user request). |
| 9 | Regex runner script | `scripts/step2_regex_runner.py` | Step 2 | Fixed runner that executes regex spec against canonical input; produces full match set for Pass 2–4. Reusable across all documents. |

---

## Workflow

| Stage | Step | Task | Detail | Input | Output |
|:---:|:---|:---|:---|:---|:---|
| **1** | Step 1.0 | Confirm user request | [step1_document_split.md](step1_document_split.md) §Step 1.0 | User input (files/folder/special instructions) | Confirmed target file list |
| **1** | Step 1.1 | Input normalisation | [step1_document_split.md](step1_document_split.md) §1.1 | Target file list | Normalised `.md` + `meta.json` |
| **1** | Step 1.2 | Source family detection, identify and split Documents | [step1_document_split.md](step1_document_split.md) §1.2 | Normalised Document files | Document list + split files |
| **1** | Step 1.2.2 | Small document merge | [step1_document_split.md](step1_document_split.md) §1.2.2 | Document list + token estimates | Merged processing units (≤ {{merge_threshold:32K}}) + `corpus__pre__document_manifest.jsonl` |
| **2** | Step 2.1 | Heading extraction (Pass 1–3 per agent; Pass 4 at document level after merge) | [step2_heading_extraction.md](step2_heading_extraction.md) §2.2–2.4 | Canonical input documents | `doc-{doc_instance_key}__heading__structure.tsv`, `doc-{doc_instance_key}__heading__regex_spec.json`, `doctype-{DocType}__heading__grammar_v{NN}.md` |
| **2** | Step 2.2 | Token measurement | [step2_heading_extraction.md](step2_heading_extraction.md) §2.5 | Heading structure TSV | Per-heading Est_Tokens (inclusive/exclusive) |
| **3** | Step 3.1 | Context-window chunking | [step3_workunit_packing.md](step3_workunit_packing.md) §3.1 | Heading structure TSV + token measurements | Chunk plan |
| **3** | Step 3.2 | Work Unit packing | [step3_workunit_packing.md](step3_workunit_packing.md) §3.2 | Chunk plan + Document metadata | WU list + `wu-{wu_key}__pre__meta.json` |
| **3** | Step 3.3 | Approval and artefact promotion | [step3_workunit_packing.md](step3_workunit_packing.md) §3.3 | Chunking plan + WU packing plan + Document list | Approval → artefact promotion → `corpus__pre__manifest.json` |

---

## Completion Criteria

PRE is complete when **all** of the following conditions are met.

| # | Condition | Reference |
|:---:|:---|:---|
| 1 | `doc-{doc_instance_key}__heading__structure.tsv` generated for all target documents | Step 2 |
| 2 | Heading extraction convergence criteria met: Error = 0, Warning ≤ max({{warn_min:3}}, ⌈total headings × {{warn_ratio:0.02}}⌉) | Step 2 §Convergence Criteria |
| 3 | Token measurement (Inclusive/Exclusive) completed for all documents | Step 2 §2.5 |
| 4 | Chunk plan and WU packing plan generated | Step 3.1–3.2 |
| 5 | User approved via `approve_all` or `approve_partial` | Step 3.3 |
| 6 | Approved artefacts promoted to `results/` | Step 3.3 §Artefact Promotion |
| 7 | `corpus__pre__manifest.json` generated and consumable by downstream | Step 3.3 |

> When `approve_partial` is used, only approved WUs are promoted and the rest remain `held`. Downstream processing may proceed for approved WUs even if `held` WUs remain.

---

# Common Rules

| Shared file | Contents |
|:---|:---|
| [`project_definitions.md`](../shared/project_definitions.md) | Terminology (HD/TD/APP/CT), identifier chain (DocumentKey → Heading_ID), token measurement standards (Inclusive/Exclusive, thresholds), approval states |
| [`naming_convention.md`](../shared/naming_convention.md) | Filename 3-part pattern, scope/phase/artifact classification, storage paths, DocumentKey slug rules |
| [`document_classification.md`](../shared/document_classification.md) | Domain classification hierarchy — Authority, DocType, Source Family, Heading Level |
| [`thresholds.yaml`](../shared/thresholds.yaml) | All numeric thresholds and limits in one file. Md files reference values via `{{key:value}}` placeholders; run `scripts/update_thresholds.py` to propagate changes. |

## Agent Lifecycle

| # | Stage | Step | Agents Assigned | Created | Terminated |
|:---|:---|:---|:---|:---|:---|
| 1 | **Stage 1** | Step 1.2 | 1 per file | When file list is confirmed | Immediately after Document list is aggregated |
| 2 | **Stage 2** | Step 2 | 1 per Document or documentSplit | After Document list is confirmed | Small: after heading structure TSV complete. Large (documentSplit): after Pass 3 complete |
| 3 | **Stage 2** | Step 2 (Pass 4, large docs only) | 1 per Document | After Coordinator merges documentSplit results and grammar | After document-level Pass 4 complete |
| — | **Stage 3** | Step 3 | Coordinator-only (no worker agents) | N/A | N/A |

> Each stage spawns **new agents** independent of any previous stage. Agents are assigned in parallel up to the available agent count; excess items are executed in batches.

> **Note:** Step 1.1 (normalisation) runs as internal pre-processing within each Step 1.2 agent for non-.md documents, prior to splitting. No separate agent is spawned for Step 1.1.

## Coordinator Role

The Coordinator is the **single orchestration process** that manages agent lifecycle across all stages. It is **not** a worker agent — it does not perform heading extraction or content analysis.

| Responsibility | Description |
|:---|:---|
| Batch scheduling | Divide pending items into batches sized to available agent count |
| State management | Track each processing item through its lifecycle states |
| Grammar version lock | Serialise concurrent grammar candidate updates (single-writer). Grammar candidates go to `staging/`; only the Coordinator promotes to `results/grammars/`. |
| documentSplit merge | Merge documentSplit heading results, resolve boundary conflicts, reassign Heading_IDs |
| Ancestor context | For each documentSplit, provide the active ancestor stack (parent heading chain at documentSplit start) to maintain hierarchy continuity |
| Retry | Re-queue failed items with backoff; escalate after max {{retry_max:3}} retries |
| Approval | Present consolidated results for user approval; promote artefacts on approval |
| WU packing | Apply WU Token Range rules, assign WU_Keys, generate WU metadata |

## Failure Handling

| Error Type | Action |
|:---|:---|
| **Transient** (API timeout, 429/503) | Auto-retry up to {{retry_max:3}} times, exponential backoff ({{retry_backoff:30s, 60s, 120s}}) |
| **Recoverable** (context window exceeded) | Auto-reshard with smaller content budget; retry. Escalate after {{reshard_max:2}} failed reshard attempts. |
| **Fatal** (file not found, unsupported format, persistent parse failure) | Mark as `escalated` immediately; report to user |

## Work Unit Lifecycle States

```
planned → running → completed → validated → approved → promoted
                                           ↘ held (partial approval) → approved (re-approval)
                  ↘ failed → retryable → running (retry)
                             ↘ escalated (max retries exceeded)
```

> `merged` is not a WU lifecycle state — it is a WU_Type (`standalone`, `split`, `merged`). `promoted` means artefacts have been moved from `results/temp/pre/` to `results/`.

## PRE Manifest — Downstream Interface Contract

`corpus__pre__manifest.json` is the **interface contract** between PRE and downstream phases (TD/APP/CT). PRE must populate the fields below; downstream consumers assume these fields exist. Minimum required fields:

| Field | Description |
|:---|:---|
| `run_id` | Unique execution identifier |
| `created_at` | ISO 8601 timestamp |
| `documents[]` | Array of document entries |
| `documents[].doc_instance_key` | DocumentInstanceKey |
| `documents[].document_key` | DocumentKey |
| `documents[].authority` | Issuing body |
| `documents[].doc_type` | DocType |
| `documents[].language` | Language code (ISO 639-1) |
| `documents[].source_path` | Original file path |
| `documents[].source_hash` | SHA-256 of original file |
| `documents[].normalised_path` | Path to normalised file (null if `.md` original) |
| `documents[].canonical_input_path` | Downstream source of truth file path |
| `documents[].document_split_path` | Path to document split file (null if single-doc) |
| `documents[].heading_count` | Number of headings extracted |
| `documents[].est_tokens` | Total document token count |
| `documents[].grammar_version` | DocType grammar version used |
| `documents[].status` | `approved`, `held`, `escalated` |
| `work_units[]` | Array of WU entries |
| `work_units[].wu_key` | WU_Key |
| `work_units[].wu_type` | `standalone`, `split`, `merged` |
| `work_units[].constituent_doc_instance_keys[]` | List of DocumentInstanceKeys |
| `work_units[].est_tokens_total` | Total WU token count |
| `work_units[].status` | `approved`, `held`, `escalated` |
| `work_units[].promoted_files[]` | List of promoted file paths |
| `open_warnings` | Count of unresolved Warning-severity items |
| `oversize_exceptions` | Count of oversize leaf exceptions |
| `token_method` | `tiktoken` or `char_approx` |
| `tokenizer_version` | Tokenizer identifier |

> **Note:** `documents[].status` transitions from `confirmed` (in `corpus__pre__document_manifest.jsonl`) to `approved`/`held`/`escalated` (in `corpus__pre__manifest.json`) after the approval step.

---

*Related documents:*
- *[step1_document_split.md](step1_document_split.md) — Document identification, splitting, normalisation*
- *[step2_heading_extraction.md](step2_heading_extraction.md) — Heading extraction Pass 1–3 per agent, Pass 4 at document level, TSV schema*
- *[step3_workunit_packing.md](step3_workunit_packing.md) — Chunking, WU packing, approval*
- *Heading instruction: `pre_skos/phase1_heading_instruction.md`*
- *Task Brief Generator: `pre_skos/task_brief/task_brief_generator.md`*
- *Extraction agent operations: `commands/agents.md`*
