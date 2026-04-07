# Project Definitions

Defines the identifier chain, token measurement standards, processing units, and approval states shared across the entire pipeline.

> **Maintenance policy** — Update this document whenever identifiers, measurement standards, or terminology change during project development. When pipeline stages are added or modified, update the Terminology section accordingly.

> For the domain classification hierarchy (Authority, DocType, Source Family, Heading Level), refer to `document_classification.md`.

## Identifier Chain

> Authority → DocType → Document classification is defined in `document_classification.md`. The chain below covers **key generation rules** only.

| Level | Identifier | Format | Uniqueness | Example |
|:---|:---|:---|:---|:---|
| Source File | `SourceFileKey` | Slug of original filename (extension excluded). See `naming_convention.md` §DocumentKey Slug Rule | Per-run | `iacs_ur_2024` |
| Document | `DocumentKey` | Slug rule applied (revision-independent). See `naming_convention.md` §DocumentKey Slug Rule | Per-DocType | `ur_a2` |
| Document Instance | `DocumentInstanceKey` | `{DocumentKey}_{revision}_{language}` | Global (deterministic) | `ur_a2_rev5_en` |
| documentSplit (temporary) | `documentSplitKey` | `{doc_instance_key}_s{NNN}` | Per-Document | `ur_a2_rev5_en_s001` |
| Chunk | `ChunkKey` | `{doc_instance_key}_ch{NNN}` (zero-padded) | Per-Document | `ur_a2_rev5_en_ch001` |
| Work Unit | `WU_Key` | standalone: `{doc_instance_key}`, split: `{doc_instance_key}_wu{NNN}`, merged: `merge_{short_hash}` | Global | `ur_e26_rev1_en` |
| Heading | `Heading_ID` | `{DocumentKey}_HD_{NNN}` (min-width 3) | Per-Document | `ur_a2_HD_042` |

> `DocumentInstanceKey` is **not** execution-unique. The same instance produces the same key across re-runs. Use a separate `RunID` when per-execution unique identification is required.

## Token Measurement Standard

| Item | Definition |
|:---|:---|
| **Tokenizer** | `cl100k_base` (OpenAI tiktoken). Approximation: English 1 token ≈ 4 chars, Korean 1 token ≈ 1.5 chars |
| **Est_Tokens_Inclusive** | Token count for the entire `[Start_Line, End_Line]` span (children included). **Non-additive** |
| **Est_Tokens_Exclusive** | Token count for the heading's own content only (children excluded). **Additive** |
| **Additivity formula** | `parent.Exclusive + Σ(children.Inclusive) = parent.Inclusive` |
| **Hard limit** | Absolute upper bound of the context window (64K, 128K, etc.) |
| **Content budget** | Hard limit − reserved space (system ~2K + output ~2K + safety). For 64K ≈ 60K |
| **char_approx** | Fallback when tiktoken is unavailable: `ceil(char_count / 4 × 1.1)` — **10% upward** buffer |
| **Line reference** | All `Start_Line`/`End_Line` values are relative to the **canonical input file** |

## Token Thresholds

| Unit | Role |
|:---|:---|
| **documentSplit** | Temporary split before heading extraction. For thresholds, see `prerequisite/step2_heading_extraction.md` |
| **Chunk** | Heading-aligned final split. For Upper Bound, see `prerequisite/step3_workunit_packing.md` |
| **Work Unit** | Execution unit packing. For Lower/Upper Bound, see `prerequisite/step3_workunit_packing.md` |

> Specific numeric values (64K, 32K, 16K, etc.) are tuneable parameters and are therefore not listed here. Always refer to the latest values in the corresponding specification.

## Terminology

### Global (entire pipeline)

| Abbreviation | Full Name | Description | PRE Scope |
|:---|:---|:---|:---:|
| **HD** | `HEADING` | Document heading extraction | Yes |
| **TD** | `TRUE_DEF` | Definition extraction | No |
| **APP** | `APPLICABILITY` | Applicability scope extraction | No |
| **CT** | `CONTROLLED_TERM` | Controlled term extraction | No |

### Processing Units

| Unit | Nature | Lifespan |
|:---|:---|:---|
| **Source File** | Physical input file; may contain one or more Documents | Step 1.0–1.1 (normalisation). Superseded by Document units after splitting |
| **Document** | Independent document unit; the smallest unit of management | Entire pipeline |
| **documentSplit** | Temporary line-based split of large documents | Created during heading extraction stage, discarded after merge |
| **Chunk** | Heading-aligned final split | Exists for all documents (small documents → single Chunk) |
| **Work Unit (WU)** | Execution unit (standalone / split / merged) | Entire pipeline after WU packing |

### Approval States

| State | Description |
|:---|:---|
| `approve_all` | All WUs approved → promote |
| `approve_partial` | Some WUs approved, remainder `held` |
| `revise_and_rerun` | Re-run after threshold adjustment |
| `reject` | Abort PRE |
