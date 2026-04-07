# Step 3 — Chunking, Work Unit Packing, and Issue Gate

> **Purpose.** Determine context-window Chunks based on the heading structure TSV and token measurements, pack them into Work Units, and write all artefacts directly to `results/`. The user is engaged only when an issue trigger fires (§Step 3.3). This is the final stage of PRE.

---

## Outputs

Step 3 newly produces:

- #6 `wu-{wu_key}__pre__meta.json` — WU metadata (composition, constituent documents, token counts)
- #7 `corpus__pre__manifest.json` — PRE master index (generated as the final step)
- #7b `doc-{doc_instance_key}__heading__chunk_plan.json` — Chunk boundaries and token sizes

> File naming rules and the full artefact catalogue are defined in [pre_specification.md](pre_specification.md) §File Naming Convention and §Artefact Catalogue.

---

## Work Unit Token Range

| Parameter | Value |
|:---|:---|
| **WU Target Range** | **{{wu_range:16K–32K}}** tokens |

| Document Size | Action |
|:---|:---|
| **> Upper Bound (> {{chunk_max:32K}} tokens)** | **Split** — split into multiple WUs at heading boundaries, each within {{wu_range:16K–32K}} range |
| **Lower Bound ≤ size ≤ Upper Bound** | **Standalone** — 1 Document = 1 WU |
| **< Lower Bound** | **Merge candidate** — eligible for merging with other whole documents until {{wu_range:16K–32K}} is reached |

### Merge Constraints

- **Whole documents only** — a document is either fully included or not included at all
- **Merge eligibility**: Only documents satisfying **all** of the following may be merged into the same WU:
  - Same `Authority`
  - Same `DocType`
  - Same language
  - Same `grammar_version` (heading grammar version used during extraction)
  - Same `Measure_Method` (tiktoken or char_approx) — do not mix measurement methods within a merged WU
- Documents exceeding the Upper Bound are split; each piece is a standalone WU and must **not** be merged with other documents
- When merging, add eligible documents in DocumentKey order (ASCII lexicographic order — guaranteed by the slug rule which produces only `[a-z0-9_]` characters) until the next addition would exceed the Upper Bound; then close the current WU and start a new one
- If the last WU falls below the Lower Bound, it is accepted as-is (do not force-merge across split boundaries)

### Threshold Change Rerun Rules

| Change | Rerun Scope |
|:---|:---|
| **Lower Bound only changed** | Rerun Step 3.2 only (WU packing) |
| **Upper Bound changed** | Rerun Step 3.1 (chunking) **and** Step 3.2 (packing) — chunk boundaries and the derived sliding-window parameters (`window_size`, `overlap`) both depend on the Upper Bound |

> These thresholds are tuneable. Adjust the values and re-run the appropriate steps per the table above.

---

## WU_Key Naming Convention

| WU Type | WU_Key Format | Example |
|:---|:---|:---|
| **Standalone** (1 Doc = 1 WU) | `{doc_instance_key}` | `ur_e26_rev1_en` |
| **Split** (1 Doc → N WUs) | `{doc_instance_key}_wu{NNN}` | `ur_z10_2_rev3_en_wu001` |
| **Merged** (N Docs → 1 WU) | `merge_{short_hash}` (first 8 chars of SHA-256 of sorted constituent keys) | `merge_a3f7c2b1` |

> For merged WUs, the short hash avoids excessively long filenames. The full constituent list is recorded in the WU metadata JSON.

### WU Header Metadata

Recorded in `wu-{wu_key}__pre__meta.json`:

| Field | Type | Description | Example |
|:---|:---|:---|:---|
| `wu_key` | string | See §WU_Key Naming Convention | `merge_a3f7c2b1` |
| `wu_type` | string | `standalone`, `split`, `merged` | `merged` |
| `authority` | string | Issuing body (same for all constituents) | `IACS` |
| `doc_type` | string | Document category (same for all constituents) | `UR` |
| `language` | string | Language code | `en` |
| `grammar_version` | string | Heading grammar version used | `v02` |
| `constituent_docs` | array | List of constituent document entries | See below |
| `constituent_docs[].doc_instance_key` | string | DocumentInstanceKey | `ur_f1_rev2_en` |
| `constituent_docs[].document_key` | string | DocumentKey | `ur_f1` |
| `constituent_docs[].start_line` | int | First line in canonical input (inclusive) | `1` |
| `constituent_docs[].end_line` | int | Last line in canonical input (inclusive) | `27` |
| `constituent_docs[].est_tokens` | int | Token count for this document | `5200` |
| `constituent_docs[].heading_range` | object | First/last Heading_IDs in this constituent document | {"first": "..._HD_NNN", "last": "..._HD_NNN"} |
| `est_tokens_total` | int | Total WU token count | `18450` |
| `split_part` | int\|null | For split WUs: 1-based index | `1` |
| `split_total` | int\|null | For split WUs: total number of parts | `2` |
| `chunk_keys` | array | List of ChunkKeys included in this WU | `["ur_f1_rev2_en_ch001"]` |
| `created_at` | string | ISO 8601 timestamp | `2026-04-05T10:30:00Z` |

> For standalone and split WUs, `constituent_docs` has a single entry. For merged WUs, each constituent carries its own heading range.

> All downstream artefacts use `wu-{wu_key}` as the file scope prefix. Document-level aggregation is performed after WU-level processing by reading the `constituent_docs` field.

---

## Step 3.1 — Context-Window Chunking

Use heading-level token measurements to determine chunking strategy via **recursive top-down splitting**. This step produces **heading-aligned Chunks** — each Chunk ≤ Upper Bound tokens. WU assignment is deferred to Step 3.2.

| Total Document Size | Chunking Strategy |
|:---|:---|
| **≤ Upper Bound** | No chunking needed — single Chunk = 1 Document; WU decision deferred to §3.2 |
| **> Upper Bound** | Mandatory recursive split at heading boundaries; each Chunk targets ≤ Upper Bound tokens |

### Recursive Splitting Algorithm

1. Start at the highest heading level (top-down)
2. Examine sibling spans at the current level using **`Est_Tokens_Inclusive`** for span sizing
3. If a sibling span's `Est_Tokens_Inclusive` is ≤ Upper Bound → adopt as a Chunk
4. If a sibling span exceeds the Upper Bound → recurse into its child headings, repeat from step 2
5. If a **leaf heading** (no children) exceeds the Upper Bound → apply the **oversize leaf exception** (see below)
6. When computing the total tokens of a Chunk composed of multiple sibling spans, sum their `Est_Tokens_Inclusive` values (siblings do not overlap, so no double-counting occurs).

> **Heading line inclusion rule**: The heading line itself is included in the span's token count. When computing sibling sums, use `Est_Tokens_Inclusive` of each sibling span (non-overlapping siblings can be safely summed).

> **Optional coalesce**: After the recursive pass, consecutive sibling spans whose combined `Est_Tokens_Inclusive` remains ≤ Upper Bound may be merged into a single Chunk to reduce fragmentation.

### Oversize Leaf Exception

When a leaf heading exceeds the Upper Bound tokens and cannot be split at heading boundaries:

| Option | When to use | Merge rule |
|:---|:---|:---|
| **Paragraph/list-item split** | Content contains ≥ 3 structural split boundaries (blank-line separators `\n\n`, or line-start item markers matching `^\s*(?:\.\d+\|\d+[.)]\|\(\d+\)\|[A-Za-z][.)]\|[-*+])\s`) and splitting at those boundaries produces all segments ≤ Upper Bound | Split at paragraph boundaries; assign synthetic sub-chunk IDs (`{ChunkKey}_p{NNN}`). Merge results by paragraph order; deduplicate at overlap. |
| **Sliding extraction window** | Paragraph/list-item split fails (< 3 structural boundaries, or any segment > Upper Bound after split) | `window_size = floor(Upper_Bound × 0.875)`, `overlap = floor(window_size × 0.21)`, `unique = window_size - overlap`. Adjusts automatically when Upper Bound changes. Coordinator merges and deduplicates. Assign synthetic sub-chunk IDs (`{ChunkKey}_w{NNN}`). |
| **User escalation** | Sliding window produces segments with > 20% token variance from target, or content structure is ambiguous | Present the oversize leaf to user with a recommendation |

> Oversize leaf splits are recorded in the chunk plan with `split_method = "oversize_paragraph"` or `"oversize_window"`. They are surfaced in the §3.3 Issue Gate report when user escalation is triggered.

> **Chunk plan artefact**: `doc-{doc_instance_key}__heading__chunk_plan.json`. While the heading structure TSV provides the structural hierarchy, the chunk plan definitively records all chunk boundaries, which is especially critical for reconstructing oversize leaf splits.

### Oversize Exclusive Segment

When a **non-leaf heading's own exclusive content** (preamble before the first child heading) exceeds the Upper Bound, treat it as a synthetic leaf and apply the oversize leaf exception rules above. Record with `split_method = "oversize_preamble"` in the chunk plan.

### Headingless Document Fallback

If a document has no headings at all (or only a DocumentRoot with no child headings):

1. If ≤ Upper Bound → single Chunk = 1 Document (proceed to WU packing)
2. If > Upper Bound → apply paragraph/list-item split or sliding window (same as oversize leaf exception) with the entire document treated as a single leaf
3. Record as `split_method = "headingless"` in the chunk plan

### Chunking Rules

- **Split boundaries must align with heading boundaries** (except for the oversize leaf exception and headingless fallback)
- Chunk key convention: `{doc_instance_key}_ch{NNN}` — zero-padded, sequential per document
- Task Brief is generated **per Work Unit**; Chunk boundaries and token sizes are recorded inside
- The heading structure TSV serves as the primary **chunk map** for all subsequent processing. The `chunk_plan.json` records all chunk boundaries and supplements the heading structure TSV.

### Chunk Plan Schema

`doc-{doc_instance_key}__heading__chunk_plan.json` contains `doc_instance_key` and a `chunks[]` array per document. Each chunk entry has the following fields:

- `chunk_key`: ChunkKey (`{doc_instance_key}_ch{NNN}`)
- `heading_range`: `{"first": "<Heading_ID>", "last": "<Heading_ID>"}` or `null` (headingless documents)
- `heading_level`: name of the heading level at which the chunk boundary was cut, or `null`
- `start_line`, `end_line`: line range in the canonical input file (inclusive)
- `est_tokens`: chunk token count
- `split_method`: `recursive` / `oversize_paragraph` / `oversize_window` / `oversize_preamble` / `headingless`
- `measure_method`: `tiktoken` or `char_approx`
- `sub_chunks`: array of sub-chunks when further split via the oversize-leaf exception or the headingless fallback; otherwise `null`. Each sub-chunk contains `sub_chunk_key` (`{ChunkKey}_p{NNN}` or `{ChunkKey}_w{NNN}`), `start_line`, `end_line`, and `est_tokens`.

Token thresholds (Upper/Lower Bounds) and split rules follow §Work Unit Token Range and §Step 3.1. The Coordinator generates the actual JSON structure based on the field definitions above.

---

## Step 3.2 — Work Unit Packing

After context-window Chunks are determined, pack Chunks (or whole Documents where Chunk = Document) into **Work Units (WUs)** according to the thresholds defined in §Work Unit Token Range.

### Packing Logic

> Branching criteria: see §Work Unit Token Range. The table below maps chunking outcomes to WU packing actions only.

| Chunking Outcome | WU Packing Action |
|:---|:---|
| **Single chunk, > Upper Bound** | Error — should not occur after Step 3.1. Escalate. |
| **Multiple chunks from same document** | Each chunk (or coalesced group of adjacent chunks) becomes a **split WU**. Adjacent chunks from the same document may be coalesced into one WU if combined ≤ Upper Bound. |
| **Single chunk, within WU target range** | **Standalone** — 1 Document = 1 WU. |
| **Single chunk, below WU target range** | **Merge candidate** — eligible for cross-document merge per §Merge Constraints. |

> **Split WU remainder**: If a split document's last WU falls below the Lower Bound, it is accepted as-is. Do not merge split document pieces with other documents.

### Coordinator Execution

The Coordinator performs WU packing immediately after all heading structure TSVs, token measurements, and chunk plans are complete (after Step 2 agents are terminated):

1. Read all document metadata, heading structure TSVs, and chunk plans
2. Apply WU Token Range rules (split/standalone/merge) with merge eligibility checks, and assign WU_Keys per the naming convention
3. Emit WU metadata and present the WU Packing Plan (see §Outputs and §3.3)

---

## Step 3.3 — Issue Gate and Auto-Completion

Default behaviour is auto-completion. The Coordinator automatically detects issues based on triggers defined in their respective sections (§2.4, §Oversize-Leaf Exception, §Merge Constraints, §Work Unit Token Range, etc.). When no trigger fires, the Coordinator writes artefacts directly to `results/` (see §Artefact Storage) without presenting the tables below. When a trigger fires, the Coordinator surfaces the following report and requests a decision.

### Issue Report

When a trigger fires, the Coordinator provides the chunking plan, WU packing plan, target Document list, and execution summary (total Document/Chunk/WU counts, open Warning count, grammar versions, oversize exceptions, merge eligibility violations, etc.) so the user can diagnose the cause. The exact report format and included items are determined by the Coordinator based on the issue type and context.

### User Response

| User Response | Action |
|:---|:---|
| **`proceed`** | Acknowledge the issue and continue (e.g., accept Warning overflow). Coordinator resumes auto-completion. |
| **`revise`** | Adjust thresholds or rerun scope. Coordinator re-runs affected steps per §Threshold Change Rerun Rules. |
| **`abort`** | Halt processing for affected Document(s). Quarantine temp copies to `results/aborted/{doc_instance_key}/`. |

---

## Artefact Storage

All artefacts produced in Steps 1–3 are written directly to `results/`. There is no temp/promotion staging.

At step completion, the following intermediate artefacts are auto-deleted: Step 2's `extraction_llm.tsv`, `extraction_script.tsv`, discrepancy working copies, `validated.tsv`, and `grammar_candidate.md`.

When a Document is aborted due to an issue, a debug copy is quarantined to `results/aborted/{doc_instance_key}/`.

`coverage.json` (#8) is always generated.

The authoritative artefact catalogue and file naming rules live in [pre_specification.md](pre_specification.md) §Artefact Catalogue.

The **PRE manifest** (`results/corpus__pre__manifest.json`) is generated as the final step — it records all document entries, WU_Keys, written file paths, grammar versions, open warning count, and oversize exception count. It serves as the single entry point for downstream consumers (`commands/agents.md`, `task_brief_generator.md`).

> **Interface contract**: The PRE manifest must populate the required fields defined in [pre_specification.md](pre_specification.md) §PRE Manifest — Downstream Interface Contract. Downstream phases (TD/APP/CT) assume these fields exist.

> For file naming rules and storage paths, see [pre_specification.md](pre_specification.md) §File Naming Convention.
