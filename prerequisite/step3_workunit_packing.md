# Step 3 — Chunking, Work Unit Packing, and Approval

> **Purpose.** Determine context-window Chunks based on the heading structure TSV and token measurements, pack them into Work Units, and obtain user approval to finalise (promote) all artefacts. This is the final stage of PRE.

---

## Outputs

> For file naming rules and the full artefact catalogue, see [pre_specification.md](pre_specification.md) §File Naming Convention and §Artefact Catalogue.

This step produces artefacts #6, #7, #7b from the catalogue:
- #6 `wu-{wu_key}__pre__meta.json` — WU metadata (composition, constituent docs, token counts)
- #7 `corpus__pre__manifest.json` — PRE master index (generated after approval)
- #7b `doc-{doc_instance_key}__heading__chunk_plan.json` — Chunk boundaries and token sizes (always generated and promoted)

This step also performs **artefact promotion** — moving all promoted artefacts (#1–#7c) from `results/temp/pre/` to `results/`.

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
| **Upper Bound changed** | Rerun Step 3.1 (chunking) **and** Step 3.2 (packing) — because chunk boundaries depend on the Upper Bound |
| **Sliding window parameters (window_size, overlap) changed** | Rerun Step 3.1 and 3.2 |

> Sliding window parameters are derived from the Upper Bound. Changing the Upper Bound automatically changes these parameters.

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
| `wu_key` | string | Unique WU identifier | `merge_a3f7c2b1` |
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
| **≤ Upper Bound (≤ {{chunk_max:32K}} tokens)** | No chunking needed — single Chunk (= 1 Document). **WU determination deferred to Step 3.2** (may become standalone or merge candidate). |
| **> Upper Bound (> {{chunk_max:32K}} tokens)** | Mandatory recursive split at heading boundaries; each Chunk targets ≤ Upper Bound tokens |

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

> Oversize leaf splits are recorded in the chunk plan with `split_method = "oversize_paragraph"` or `"oversize_window"` for user review during approval.

> **Chunk plan artefact**: `doc-{doc_instance_key}__heading__chunk_plan.json` is **always promoted**. While the heading structure TSV provides the structural hierarchy, the chunk plan definitively records all chunk boundaries, which is especially critical for reconstructing oversize leaf splits.

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
- The heading structure TSV serves as the primary **chunk map** for all subsequent processing. The always-promoted `chunk_plan.json` records all chunk boundaries and supplements the heading structure TSV.

### Chunk Plan Schema

`doc-{doc_instance_key}__heading__chunk_plan.json`:

**Example A — heading-based document:**

```json
{
  "doc_instance_key": "ur_a2_rev5_en",
  "chunks": [
    {
      "chunk_key": "ur_a2_rev5_en_ch001",
      "heading_range": {"first": "ur_a2_HD_001", "last": "ur_a2_HD_045"},
      "heading_level": "Part",
      "start_line": 1,
      "end_line": 890,
      "est_tokens": 28000,
      "split_method": "recursive",
      "measure_method": "tiktoken",
      "sub_chunks": null
    },
    {
      "chunk_key": "ur_a2_rev5_en_ch002",
      "heading_range": {"first": "ur_a2_HD_046", "last": "ur_a2_HD_046"},
      "heading_level": "Regulation",
      "start_line": 891,
      "end_line": 1720,
      "est_tokens": 35000,
      "split_method": "oversize_paragraph",
      "measure_method": "tiktoken",
      "sub_chunks": [
        {"sub_chunk_key": "ur_a2_rev5_en_ch002_p001", "start_line": 891, "end_line": 1300, "est_tokens": 17000},
        {"sub_chunk_key": "ur_a2_rev5_en_ch002_p002", "start_line": 1301, "end_line": 1720, "est_tokens": 18000}
      ]
    }
  ]
}
```

**Example B — headingless document:**

```json
{
  "doc_instance_key": "ur_x1_rev1_en",
  "chunks": [
    {
      "chunk_key": "ur_x1_rev1_en_ch001",
      "heading_range": null,
      "heading_level": null,
      "start_line": 1,
      "end_line": 1200,
      "est_tokens": 42000,
      "split_method": "headingless",
      "measure_method": "tiktoken",
      "sub_chunks": [
        {"sub_chunk_key": "ur_x1_rev1_en_ch001_p001", "start_line": 1, "end_line": 600, "est_tokens": 21000},
        {"sub_chunk_key": "ur_x1_rev1_en_ch001_p002", "start_line": 601, "end_line": 1200, "est_tokens": 21000}
      ]
    }
  ]
}
```

---

## Step 3.2 — Work Unit Packing

After context-window Chunks are determined, pack Chunks (or whole Documents where Chunk = Document) into **Work Units (WUs)** according to the thresholds defined in §Work Unit Token Range.

### Packing Logic

| Document Chunking Result | WU Packing Action |
|:---|:---|
| **Single chunk, > Upper Bound (impossible after A)** | Error — should not occur. Escalate. |
| **Multiple chunks from same document** | Each chunk (or coalesced group of adjacent chunks) becomes a **split WU**, targeting {{wu_range:16K–32K}} each. Adjacent chunks from the same document may be coalesced into one WU if combined ≤ Upper Bound. |
| **Single chunk, within {{wu_range:16K–32K}}** | **Standalone** — 1 Document = 1 WU. |
| **Single chunk, < Lower Bound** | **Merge candidate** — eligible for cross-document merge per §Merge constraints. |

> **Split WU remainder**: If a split document's last WU falls below the Lower Bound, it is accepted as-is. Do not merge split document pieces with other documents.

### Coordinator Execution

The Coordinator performs WU packing immediately after all heading structure TSVs, token measurements, and chunk plans are complete (after Step 2 agents are terminated):

1. Read all document metadata, heading structure TSVs, and chunk plans
2. Apply WU Token Range rules (split/standalone/merge) with merge eligibility checks
3. Assign WU_Keys per the naming convention
4. Generate `wu-{wu_key}__pre__meta.json` for each WU
5. Prepare the WU Packing Plan for user approval (Step 3.3)

---

## Step 3.3 — Chunking Plan and Document List Approval

Present the consolidated chunking plan and target document list together for a single user approval.

### Chunking Plan (example)

| Chunk Key | Document | Heading Range | Heading_Level | Split_Method | Est. Tokens | Measure_Method |
|:---|:---|:---|:---|:---|:---|:---|
| `ur_a2_rev5_en_ch001` | UR A2 | Part A–C | Part | `recursive` | 30K | tiktoken |
| `solas_ii_1_rev2024_en_ch001` (no split) | SOLAS II-1 | Full document | — | `no_split` | 28K | tiktoken |
| `marpol_annex_i_rev2024_en_ch001` | MARPOL Annex I | Regulations 1–8 | Part | `recursive` | 30K | tiktoken |
| `marpol_annex_i_rev2024_en_ch002` | MARPOL Annex I | Regulations 9–16 | Part | `recursive` | 27K | tiktoken |
| `marpol_annex_i_rev2024_en_ch003` | MARPOL Annex I | Regulations 17–28 | Part | `recursive` | 31K | tiktoken |

### WU Packing Plan (example)

| WU_Key | WU_Type | Constituent Docs | Est. Tokens | Heading Count |
|:---|:---|:---|:---|:---|
| `ur_e26_rev1_en` | standalone | UR E26 | 30K | 205 |
| `ur_z10_2_rev3_en_wu001` | split | UR Z10.2 (ch001–ch002) | 24K | 147 |
| `ur_z10_2_rev3_en_wu002` | split | UR Z10.2 (ch003–ch004) | 24K | 147 |
| `merge_a3f7c2b1` | merged | UR F1 (5K) + UR F2 (7K) + UR F3 (4K) | 16K | 12 |

### Target Document List (example)

| # | File Path | Document | Authority | DocType | DocumentKey | InstanceKey | Total Tokens | Chunks | WU Count | Heading Count |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | `{path}` | `{doc name}` | `{IACS/IMO/KR/EU}` | `{UR/SOLAS/...}` | `{doc_key}` | `{doc_instance_key}` | `{n}K` | `{n or 1}` | `{n}` | `{n}` |

### Execution Summary (example)

| Metric | Value |
|:---|:---|
| Total Documents | `{n}` |
| Total Chunks | `{n}` |
| Total Work Units | `{n}` |
| Open Warnings | `{n}` (from final discrepancy TSVs) |
| Grammar Versions | `{list of doctype grammar versions}` |
| Oversize Exceptions | `{n or "none"}` |
| Merge Eligibility Violations | `{n or "none"}` |

### Approval States

| User Response | Action |
|:---|:---|
| **`approve_all`** | Promote all artefacts. PRE complete. |
| **`approve_partial`** | Promote specified WUs only. Remaining WUs are held with status `held` for later revision. |
| **`revise_and_rerun`** | User specifies threshold changes or reprocessing scope. Coordinator re-runs affected steps per §Threshold Change Rerun Rules. |
| **`reject`** | Abort PRE. No promotion. All temp artefacts retained for debugging. |

### Post-Partial-Approval Workflow

When `approve_partial` is selected:
1. Approved WUs are promoted immediately. A **partial** `corpus__pre__manifest.json` is generated containing only the approved WUs.
2. Held WUs remain in `results/temp/pre/` with status `held`.
3. To resume: the user invokes Step 3.3 again. The Coordinator presents only held WUs for re-approval.
4. On re-approval, the Coordinator **updates** (upserts) the existing `corpus__pre__manifest.json` with the newly approved WUs.
5. Held WU artefacts are immutable between approval rounds — they are not re-processed unless the user selects `revise_and_rerun`.

→ **Obtain user approval.** Once approved, the Coordinator promotes artefacts.

---

## Artefact Promotion

After approval, the Coordinator promotes artefacts from `results/temp/pre/` → `results/`:

**Always promoted:**
- #1 `doc-{doc_instance_key}__heading__structure.tsv`
- #2 `doc-{doc_instance_key}__heading__regex_spec.json`
- #3 `file-{source_file_key}__pre__meta.json`
- #4 `file-{source_file_key}__pre__normalised.md` (if applicable)
- #4a `doc-{doc_instance_key}__pre__split.md` (multi-document source files only)
- #5 `doctype-{DocType}__heading__grammar_v{NN}.md`
- #6 `wu-{wu_key}__pre__meta.json`
- #7 `corpus__pre__manifest.json`
- #7a `corpus__pre__document_manifest.jsonl`
- #7b `doc-{doc_instance_key}__heading__chunk_plan.json`
- #7c `doc-{doc_instance_key}__heading__discrepancy_final.tsv` (retained for audit)

**Discarded after promotion:**
- Step 2 intermediate artefacts (extraction_llm.tsv, extraction_script.tsv, discrepancy working copies, validated.tsv, grammar_candidate.md — not numbered in the catalogue)
- #8 `doc-{doc_instance_key}__heading__coverage.json` — conditionally promoted (on user request)

See [pre_specification.md](pre_specification.md) §Artefact Catalogue for the complete list.

The **PRE manifest** (`results/corpus__pre__manifest.json`) is generated as the final step — it records all document entries, WU_Keys, promoted file paths, grammar versions, open warning count, and oversize exception count. It serves as the single entry point for downstream consumers (`commands/agents.md`, `task_brief_generator.md`).

> **Interface contract**: The PRE manifest must populate the required fields defined in [pre_specification.md](pre_specification.md) §PRE Manifest — Downstream Interface Contract. Downstream phases (TD/APP/CT) assume these fields exist.

> For file naming rules and storage paths, see [pre_specification.md](pre_specification.md) §File Naming Convention.
