# Step 1 — Document Identification, Splitting, and Normalisation

> **Conformance.** When modifying this document, it must conform to [pre_specification.md](pre_specification.md). Verify that step numbers, artefact numbers, and workflow order are consistent with the parent specification.

> **Purpose.** Read target files, identify independent Document units, split multi-document files where necessary, and convert all inputs to a consistent normalised format. This prepares input for heading extraction (Step 2.1).

---

## 1.0 Work Specification

### Purpose

Read target files, identify independent Document units, split multi-document files where necessary, and convert all inputs to a consistent normalised format. This prepares input for heading extraction (Step 2).

### Inputs

- Target documents (user-provided: single file, multiple files, or folder)
- Shared definitions (`shared/` directory)
- (Optional) Special instructions

### Workflow

| # | Step | Task | Input | Output |
|:---:|:---|:---|:---|:---|
| 1 | Step 1.0 | Confirm user request | User input (files/folder/special instructions) | Confirmed target file list |
| 2 | Step 1.1 | Input normalisation | Target file list | Normalised `.md` + `meta.json` |
| 3 | Step 1.2.0 | Source family detection | Filename, path, internal metadata | Source Family classification |
| 4 | Step 1.2 | Document identification and splitting | Canonical input + Source Family | Document list + split files |
| 5 | Step 1.2.2 | Small document merge | Document list + token estimates | Merged processing units (≤ {{merge_threshold:32K}}) |
| 6 | — | Write manifest | Confirmed Document list | `corpus__pre__document_manifest.jsonl` |

### Final Outputs

> For file naming rules and the full artefact catalogue, see [pre_specification.md](pre_specification.md) §File Naming Convention and §Artefact Catalogue.

- `file-{source_file_key}__pre__meta.json` — file metadata (per source file) ← #3
- `file-{source_file_key}__pre__normalised.md` — normalised text (non-`.md` formats, per source file) ← #4
- `corpus__pre__document_manifest.jsonl` — persistent per-document registry ← #7a
- `doc-{doc_instance_key}__pre__split.md` — per-Document split (multi-doc files only) ← #4a

### Completion Criteria

- `meta.json` generated for all target files
- All Documents identified and split from multi-document files
- `unassigned_lines = 0` or escalated to user
- `corpus__pre__document_manifest.jsonl` generated and consumable by Stage 2
- Small document merge (§1.2.2) applied

### Next Step

→ Step 2: Heading Structure Extraction (`step2_heading_extraction.md`)

---

## Step 1.0 — Confirm User Request

Verify the user has provided a target document path (file or folder). Ask if missing. For folders, scan supported formats only (`.md`, `.pdf`, `.html`, `.xml`, `.json`); exclude `results/`, hidden directories, and symlinks.

---

## Step 1.1 — Input Normalisation

All input files are validated and converted to a canonical normalised markdown format before heading analysis. This ensures stable line numbering and consistent heading detection regardless of the original file format.

> **Execution timing**: Step 1.1 runs **inside each Step 1.2 agent** as internal pre-processing. For `.md` originals, markdown lint validation and auto-fix are applied before metadata generation. For non-`.md` formats, the agent normalises the file before identification and splitting. For multi-document non-`.md` files, the order is: **normalise → lint → identify boundaries on canonical text → split**. This ensures line ranges are determined on the stable canonical text, not the raw source format.

### Downstream Input Priority

All subsequent steps use the **canonical input file** as their source of truth. Resolution order:

1. `doc-{doc_instance_key}__pre__split.md` (if the document was split from a multi-doc file)
2. `file-{source_file_key}__pre__normalised.md` (if the document was converted from a non-`.md` format)
3. Original `.md` file (if the source was already markdown)

This is recorded as `canonical_input_path` in the document manifest.

### Normalisation by Format

| Input Format | Normalisation Method | Conversion Actor | Output |
|:---|:---|:---|:---|
| `.md` | No text conversion needed. Run markdown lint validation (§Markdown Lint) and auto-fix heading level violations. Generate metadata file. | **Lint** | Original file (or lint-fixed copy) used as canonical input; `file-{source_file_key}__pre__meta.json` |
| `.pdf` | Split into {{pdf_pages:50}}-page chunks and assign each chunk to an agent. Each agent converts its page range to markdown with page markers (`<!-- PAGE NNN -->`). Coordinator merges agent outputs in page order to produce the final `.md`. | **Agent** ({{pdf_pages:50}} pages/agent) | `file-{source_file_key}__pre__normalised.md` + `meta.json` |
| `.html` | Convert via script: strip tags, preserve structural elements (`<h1>`–`<h6>`, `<section>`) as markdown headings | **Script** | `file-{source_file_key}__pre__normalised.md` + `meta.json` |
| `.xml` | Convert via script: parse structure, map element hierarchy to heading levels | **Script** | `file-{source_file_key}__pre__normalised.md` + `meta.json` |
| `.json` | Convert via script: parse key hierarchy, map to heading levels, extract text values | **Script** | `file-{source_file_key}__pre__normalised.md` + `meta.json` |

### PDF Normalisation Detail

1. **Split unit**: Split the source PDF into {{pdf_pages:50}}-page chunks and assign each range to one sub-agent. **Maximum {{pdf_agents:20}} sub-agents per PDF**.
2. **Agent task**: Each agent converts the assigned page range to markdown, preserving original text and structure.
   - Insert `<!-- PAGE NNN -->` markers at page boundaries
3. **Merge**: Coordinator merges all agent outputs in page order into a single `normalised.md`.
   - Restore sentences/headings that were split at chunk boundaries during merge
4. **meta.json**: Record `agent` in the `parser` field, `{{pdf_pages:50}}` in the `pages_per_agent` field

### Script-based Normalisation (HTML/XML/JSON)

HTML, XML, and JSON formats have programmatically parseable structure, so **conversion scripts** are used instead of agents.
- Scripts are located in the `scripts/` directory, with per-format converters (`html_to_md.py`, `xml_to_md.py`, `json_to_md.py`).
- Script output follows the same format as agent conversion (`normalised.md` + `meta.json`).
- Record the script name and version in the `parser` field of `meta.json`.

### Normalisation Requirements (non-`.md` formats)

- **Stable line map**: Every line in the normalised file has a fixed line number that does not change across runs (given the same parser version and configuration)
- **Heading markers preserved**: Structural elements from the original format are converted to markdown headings (`#`, `##`, etc.) so that regex-based heading detection works uniformly
- **All subsequent steps operate on the canonical input file**, not the raw source format
- **Line ending policy**: Normalise to `\n` (LF). Record in metadata.
- **Page markers**: For PDF, insert `<!-- PAGE NNN -->` comments at page boundaries. These are non-content lines excluded from heading extraction but preserved for traceability.

### Markdown Lint (all formats including `.md`)

Validate heading structure for all formats. `HL001` (level skip → auto-demote), `HL002` (Setext → ATX auto-convert), `HL003` (empty heading → escalate). If auto-fix is applied, output as `normalised.md` and update `canonical_input_path`. Record lint results in `meta.json`.

### Normalisation Reproducibility

Record the following in `file-{source_file_key}__pre__meta.json` to ensure reproducibility:

| Field | Description | Example |
|:---|:---|:---|
| `source_path` | Original file path | `UR_MD/ur-a2rev5.pdf` |
| `source_hash` | SHA-256 of original file | `a1b2c3...` |
| `source_format` | Original format | `pdf` |
| `parser` | Parser/library or conversion actor used | `agent` (PDF) / `html_to_md.py` (HTML) |
| `parser_version` | Parser/script version | `1.0.0` |
| `pages_per_agent` | Pages per agent (PDF only) | `{{pdf_pages:50}}` |
| `agent_count` | Number of agents assigned (PDF only) | `5` |
| `line_ending` | Normalised line ending | `LF` |
| `page_marker_format` | Page marker format (PDF only) | `<!-- PAGE NNN -->` |
| `ligature_handling` | How ligatures were processed | `expanded` |
| `char_count` | Total character count | `45230` |
| `est_tokens` | Estimated token count | `11307` |
| `token_method` | Tokenizer used | `tiktoken` |
| `grammar_version` | Heading grammar version used (set after heading extraction, null initially) | `v02` |
| `created_at` | Conversion timestamp | `2026-04-05T10:30:00Z` |

### Manifest Finalisation

After all normalisation is complete, the Coordinator updates `corpus__pre__document_manifest.jsonl`:
- Set `normalised_path` for each non-`.md` document
- Compute `canonical_input_path` using the priority chain: `document_split_path → normalised_path → source_path` (first non-null)
- The manifest is now finalised and ready for Stage 2 consumption.

> **`grammar_version` update:** After heading extraction (Stage 2) completes, the Coordinator updates each document's `file-{source_file_key}__pre__meta.json` and the manifest's `grammar_version` field with the final promoted grammar version used during Pass 4. This is the version recorded in WU metadata for merge eligibility.

> For file naming rules and storage paths, see [pre_specification.md](pre_specification.md) §File Naming Convention.

---

## Step 1.2 — Source Family Detection, Identify and Split Documents

A single file may contain one or more independent documents. Determine Document boundaries using source-family criteria.

### 1.2.0 Source Family Detection

Before identification and splitting, determine the **source family** for each file. The source family governs splitting criteria, heading grammar selection, and normalisation rules.

| Detection Priority | Signal | Example |
|:---|:---|:---|
| 1 (highest) | User-provided explicit mapping | "This folder is all IACS UR" |
| 2 | Document internal title / metadata | Title contains "SOLAS" → IMO Convention |
| 3 | Filename pattern | `ur-a2rev5.md` → IACS UR |
| 4 | Parent directory path pattern | `UR_MD/` → IACS UR |

All available signals are collected. If signals at different priority levels conflict, the highest-priority non-ambiguous signal is used. If signals at the SAME priority level conflict, assign `unknown` and escalate to user.

- If detection is ambiguous or contradictory → assign `unknown` and **escalate to user**.
- If a file contains mixed families → assign `mixed` and **escalate to user** (do not auto-split across families).

### Document Identification

> Authority, DocType, Source Family 분류는 [`shared/document_classification.md`](../shared/document_classification.md)를 참조한다.
> 식별자 체인(DocumentKey, DocumentInstanceKey 등)과 slug 규칙은 [`shared/project_definitions.md`](../shared/project_definitions.md) §Identifier Chain 및 [`shared/naming_convention.md`](../shared/naming_convention.md) §DocumentKey Slug Rule을 참조한다.

**Step 1.2에서의 식별 흐름:** file → Source Family 판별 → Document 경계 식별 → Authority + DocType + DocumentKey + DocumentInstanceKey 도출.

> **키 사용 원칙:**
> - **DocumentKey** (`ur_a2`): cross-revision 참조, concept grouping, Heading_ID prefix
> - **DocumentInstanceKey** (`ur_a2_rev5_en`): 파일 경로, 산출물 명명, Concept_ID prefix, WU ID

### DocumentRoot vs. Heading Hierarchy

Document는 heading level이 **아니다** — heading tree의 관리 컨테이너이다. Heading 계층은 DocumentRoot 아래 Level 1부터 시작한다. Source family별 heading level 명칭은 [`shared/document_classification.md`](../shared/document_classification.md) §Heading Level을 참조한다.

```
DocumentRoot (UR A2, SOLAS II-1)    ← 관리 단위; TSV row at Depth=0
  └─ Heading L1 (Part A, ...)        ← heading 계층 시작 (Depth=1)
       └─ Heading L2 (Reg. 1, ...)   ← Depth=2
            └─ Heading L3 (1.1, ...) ← Depth=3
```

> TSV의 첫 번째 행(Depth=0)은 문서 자체를 나타내는 **synthetic DocumentRoot row**이다. 텍스트에서 추출한 heading이 아니며, 실제 heading은 모두 Depth ≥ 1이다.

### Source Family Splitting Criteria

> Source Family별 문서 경계 기준은 [`shared/document_classification.md`](../shared/document_classification.md) §Source Family를 참조한다.

분할 예시:
- **IACS UR/UI/Rec/PR**: `ur-a2rev5.md` → `UR A2` (1 파일 = 1 Document)
- **IMO Conventions**: `solas_consolidated.md` → `SOLAS II-1`, `SOLAS II-2` (Chapter/Annex 단위)
- **KR Rules**: `kr_rules_pt3.md` → `KR Rules Pt.3 Ch.1`, `Pt.3 Ch.2` (Part+Chapter 단위)
- **EU Legislation**: `directive_2009_45_ec.md` → `Directive 2009/45/EC` (Directive/Regulation 단위)
### 1.2.1 Per-File Agent Parallelisation

> **Coordinator role:** Batch construction, agent assignment/monitoring, agent termination at end of Step 1.2.

1. **Batch construction** — Divide file list into batches of size N (available agent count). 1 agent = 1 file.
2. **Source family detection** — Determine source family per §1.2.0 priority rules.
3. **Identification** — Identify Document boundaries using source-family criteria.
4. **Splitting** — For multi-document files: determine per-Document start/end line ranges, generate split files (`doc-{doc_instance_key}__pre__split.md`), verify full content allocation.
5. **Aggregation** — Consolidate confirmed Document list → write `corpus__pre__document_manifest.jsonl`.
6. **Terminate agents** — Step 1.2 agents terminated here. Subsequent steps assign new agents.

### 1.2.2 Small Document Merge

After splitting and token estimation, adjacent documents under {{merge_threshold:32K}} tokens within the same source file and source family are merged into a single processing unit (≤ {{merge_threshold:32K}} total) to reduce agent count in Step 2.

### Document Manifest Schema

`corpus__pre__document_manifest.jsonl` — one JSON object per line, one line per Document:

| Field | Type | Description |
|:---|:---|:---|
| `doc_instance_key` | string | DocumentInstanceKey |
| `document_key` | string | DocumentKey |
| `authority` | string | Issuing body |
| `doc_type` | string | DocType |
| `revision` | string | Revision label (e.g., rev5, 2024) |
| `language` | string | Language code (ISO 639-1, e.g., en, ko) |
| `document_title` | string | Full document title for DocumentRoot row generation |
| `source_family` | string | Detected source family |
| `source_path` | string | Original file path |
| `source_hash` | string | SHA-256 of original file |
| `document_split_path` | string\|null | Path to split file (null if 1 file = 1 doc) |
| `normalised_path` | string\|null | Path to normalised file (null if `.md` original) |
| `canonical_input_path` | string | **Downstream source of truth**: document_split_path → normalised_path → source_path (first non-null) |
| `start_line_in_source` | int\|null | Start line in original file (for multi-doc files) |
| `end_line_in_source` | int\|null | End line in original file (for multi-doc files) |
| `shared_front_matter_lines` | int | Lines classified as shared front matter |
| `discarded_boilerplate_lines` | int | Lines classified as boilerplate |
| `unassigned_lines` | int | Lines not assigned to any Document (should be 0 or escalated) |
| `shared_back_matter_lines` | int | Lines classified as shared back matter |
| `est_tokens` | int\|null | Document total token count (null until Step 1.1 meta.json is generated) |
| `token_method` | string\|null | tiktoken or char_approx (null until measured) |
| `status` | string | `confirmed`, `escalated`, `skipped` |
| `created_at` | string | ISO 8601 timestamp |
