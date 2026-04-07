# File Naming Convention

Defines the output file naming pattern, scope/phase/artifact classification, storage paths, and DocumentKey slug rules.

> **Maintenance policy** — Update this document whenever a new scope, phase, or artifact is added during project development. In the future, a filename validation script will be generated based on these rules for automated verification.

All output filenames follow a 3-part pattern separated by double underscores (`__`).

```
{scope}__{phase}__{artifact}.{ext}
```

## Scope

| Prefix | Purpose | Example |
|:---|:---|:---|
| `file-{source_file_key}` | Per-source-file output (normalisation) | `file-iacs_ur_2024__pre__normalised.md` |
| `doc-{doc_instance_key}` | Per-document PRE output (split, meta, heading extraction) | `doc-ur_a2_rev5_en__heading__structure.tsv` |
| `documentSplit-{doc_instance_key}_s{NNN}` | Temporary documentSplit (discarded after merge) | `documentSplit-ur_a2_rev5_en_s001__heading__extraction_llm.tsv` |
| `doctype-{DocType}` | Per-DocType shared asset | `doctype-UR__heading__grammar_v01.md` |
| `wu-{wu_key}` | Per-WU execution output | `wu-ur_e26_rev1_en__true_def__extracted_segments.tsv` |
| `corpus` | Entire corpus | `corpus__pre__manifest.json` |

## Phase

| Phase | Description |
|:---|:---|
| `pre` | Prerequisite — document splitting, normalisation, WU packing |
| `heading` | Heading structure extraction |
| `true_def` | Definition extraction |
| `applicability` | Applicability scope extraction |
| `controlled_term` | Controlled term extraction |

## Artifact (Primary)

| Artifact | Description |
|:---|:---|
| `meta` | Metadata JSON |
| `normalised` | Normalised text |
| `split` | Split document |
| `structure` | Heading structure TSV |
| `regex_spec` | Regex specification JSON |
| `grammar_candidate` | Grammar update proposal |
| `grammar_v{NN}` | Finalised heading grammar (version-controlled) |
| `chunk_plan` | Chunk boundary definition JSON |
| `extraction_llm` | LLM extraction result TSV |
| `extraction_script` | Script extraction result TSV |
| `discrepancy` | Discrepancy log TSV (intermediate) |
| `discrepancy_final` | Final discrepancy log TSV (promoted) |
| `validated` | Validated TSV |
| `coverage` | Line-level classification audit JSON |
| `manifest` | PRE master index |
| `document_manifest` | Document registry |
| `task_brief` | Task brief |
| `extracted_segments` | Extracted segments |
| `patterns` | Pattern catalogue |

## Storage Paths

| Path | Purpose |
|:---|:---|
| `results/temp/pre/` | Temporary output (before approval) |
| `results/temp/pre/documentSplits/` | documentSplit temporary output (discarded after merge) |
| `results/` | Permanent output (promoted after approval) |
| `results/grammars/` | Finalised heading grammar |
| `results/grammars/staging/` | Grammar candidate (unfinalised, not reusable) |

## DocumentKey Slug Rule

Deterministically generate a DocumentKey from a document name:

1. Convert to lowercase
2. Replace spaces, hyphens, slashes, and dots with `_`
3. Remove characters outside `[a-z0-9_]`
4. Collapse consecutive `_` into a single `_`
5. Strip leading and trailing `_`

| Input | Result |
|:---|:---|
| `UR A2` | `ur_a2` |
| `SOLAS II-1` | `solas_ii_1` |
| `KR Rules Pt.3 Ch.1` | `kr_rules_pt_3_ch_1` |
| `MARPOL Annex I` | `marpol_annex_i` |
