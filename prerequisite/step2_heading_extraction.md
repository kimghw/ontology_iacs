# Step 2 — Heading Structure Extraction

> **Purpose.** Extract a complete heading structure from canonical input documents using the LLM-Script cooperative process (Pass 1–4) and measure per-heading token counts. These results serve as the foundation for chunking and Work Unit assignment (Step 3).

---

## 2.0 Work Specification

### Purpose

Extract a complete heading structure from canonical input documents and measure per-heading token counts.
These results serve as the input for Step 3 chunking and Work Unit assignment.

### Inputs

- Canonical input documents (from Step 1)
- (Optional) Existing DocType grammar

### Key Branching

| Condition | Processing Mode |
|:---|:---|
| Document ≤ {{split_threshold:64K}} tokens | 1 Document = 1 agent, Pass 1–4 → token measurement |
| Document > {{split_threshold:64K}} tokens | documentSplit pre-split → per-documentSplit Pass 1–3 → Coordinator merge → document-level Pass 4 → token measurement |

### Final Outputs

> For file naming rules and the full artefact catalogue, see [pre_specification.md](pre_specification.md) §File Naming Convention and §Artefact Catalogue.

- #1 `doc-{doc_instance_key}__heading__structure.tsv` — Final heading tree (Heading_ID, hierarchy, line ranges, token counts). Direct input for Step 3 chunking.
- #2 `doc-{doc_instance_key}__heading__regex_spec.json` — Regex pattern array used in Pass 2–4. Reused for subsequent documents of the same DocType.
- #5 `doctype-{DocType}__heading__grammar_v{NN}.md` — Per-DocType heading grammar definition (hierarchy, numbering schemes, patterns). Version-controlled.
- #8 `doc-{doc_instance_key}__heading__coverage.json` — Heading/non-heading classification for every line. For omission verification.
- #7c `doc-{doc_instance_key}__heading__discrepancy_final.tsv` — Remaining Warning/Info entries after Pass 4. Retained for approval audit trail.
- #9 `scripts/step2_regex_runner.py` — Fixed regex runner script (reusable across all documents). See §regex runner.

### Completion Criteria

- Error = 0
- Warning ≤ max({{warn_min:3}}, ⌈total_headings × {{warn_ratio:0.02}}⌉)
- **Evaluation point:** Assessed against the final `structure.tsv` after Pass 4 completion. Errors during Pass 3 iterations are managed by the convergence criteria (§2.4).

### Next Step

→ Step 3: Work Unit Packing (`step3_workunit_packing.md`)

---

## 2.1 Terms and Processing Units

| Unit | Nature | Condition | Key Format | Example |
|:---|:---|:---|:---|:---|
| **documentSplit** | Temporary line-based pre-split of a large Document. Used only for heading extraction; discarded after merge. {{split_overlap:100}}-line overlap between adjacent documentSplits. | Document > {{split_threshold:64K}} tokens | `{doc_instance_key}_s{NNN}` | `ur_a2_rev5_en_s001` |
| **Chunk** | Final heading-aligned segment (target ≤ {{chunk_max:32K}} tokens). Created only after validated heading structure is available. | All Documents (≤ {{chunk_max:32K}} → single Chunk = 1 Document; > {{chunk_max:32K}} → recursive split) | `{doc_instance_key}_ch{NNN}` | `ur_a2_rev5_en_ch001` |

> **documentSplit vs Chunk:** documentSplits are temporary pre-extraction splits; Chunks are final post-extraction splits.
>
> **Default behaviour:** Document ≤ {{chunk_max:32K}} tokens → single Chunk = 1 Document. Document > {{chunk_max:32K}} tokens → recursive split at heading boundaries. Document > {{split_threshold:64K}} tokens → documentSplit pre-split before heading extraction.

### Intermediate Artefacts (discarded after processing)

> For final outputs, see §2.0 Work Specification.

- `doc-{doc_instance_key}__heading__extraction_llm.tsv` — Heading list extracted by LLM in Pass 1. Contains provisional Heading_ID, Heading_Level, Heading_Number, and line numbers. Serves as the baseline for Pass 2 cross-check.
- `doc-{doc_instance_key}__heading__extraction_script.tsv` — Full match results from the regex runner against canonical input in Pass 2. Adds Matched_Pattern_Index and Matched_Text columns. Aligned with LLM results to compute discrepancies.
- `doc-{doc_instance_key}__heading__discrepancy.tsv` — Discrepancy working copy generated per Pass 2–3 iteration. Records Agreed/LLM_only/Script_only/Level_mismatch/Number_mismatch classification with Severity (Error/Warning/Info). Suffixed `_iter{N}` to preserve judgement history across iterations.
- `doc-{doc_instance_key}__heading__validated.tsv` — Confirmed heading list after Pass 3 discrepancy resolution. Reflects LLM_only withdrawals, Script_only confirmations, and level/number corrections. Input for Pass 4 and merge.
- `doc-{doc_instance_key}__heading__grammar_candidate.md` — Grammar update proposal submitted by the agent. Describes newly discovered structural patterns (numbering schemes, keyword prefixes) in diff format. Stored in `results/grammars/staging/`; not reusable by other agents until Coordinator merges.

---

## 2.2 Overall Processing Flow

> Agents from Step 1.2 have been terminated after the Document list was finalised. This step assigns **new agents** at the Document or documentSplit level.

| Document Size | Processing Mode |
|:---|:---|
| **≤ {{split_threshold:64K}} tokens** | 1 Document = 1 agent. A single agent runs Pass 1–4 and token measurement. |
| **> {{split_threshold:64K}} tokens** | Pre-split into temporary documentSplits. documentSplit agents run **Pass 1–3 only**. Coordinator merges results and grammar candidates, then spawns a **document-level Pass 4 agent**. |

Assign as many agents as available in parallel. If items exceed agent count, execute in batches.

### Regular Documents (≤ {{split_threshold:64K}} tokens)

1. **Assignment** — One agent per Document. Each agent runs Pass 1–3 → submits grammar candidate to `results/grammars/staging/`. The Coordinator collects all candidates for the DocType, merges them into the confirmed grammar, and increments the version. Then the same agent (or a new one) runs Pass 4 with the confirmed grammar → token measurement.
2. **Result reporting** — Output heading structure TSV.

### Large Documents (> {{split_threshold:64K}} tokens)

1. **Pre-split into documentSplits** — Divide into temporary documentSplits considering the context window and document size.
2. **Per-documentSplit Pass 1–3** — Assign agents in parallel; each agent independently runs Pass 1–3 on its assigned documentSplit.
3. **Merge** — The Coordinator merges documentSplit results in line-number order, deduplicates overlap, and reassigns document-level Heading_IDs.
4. **Document-level Pass 4** — Run Pass 4 on the merged result.
5. **Discard documentSplits** — Discard all documentSplit-scoped intermediate artefacts.

```text
Example: 7 Documents (5 regular + 2 large), 4 agents

  Batch 1 — Regular Documents:
    Batch 1a: Doc1 (agent 1), Doc2 (agent 2), Doc3 (agent 3), Doc4 (agent 4) → parallel
    Batch 1b: Doc5 (agent 1) → run
    → Heading structure TSV complete for each

  Batch 2 — Large Documents:
    Doc6 (180K tokens) → 3 documentSplits:
      Batch 2a: documentSplit1 (agent 1), documentSplit2 (agent 2), documentSplit3 (agent 3) → Pass 1–3 parallel
      → Coordinator merge + grammar merge
      → Pass 4 agent (agent 1) on merged Doc6 → final structure TSV
    Doc7 (250K tokens) → 4 documentSplits:
      Batch 2b: documentSplit1–4 → Pass 1–3 parallel
      → Coordinator merge + grammar merge
      → Pass 4 agent on merged Doc7 → final structure TSV

  → Aggregate all results → Step 3 (step3_workunit_packing.md)
```

---

## 2.3 Pass Details

Each agent executes heading extraction for its assigned Document (or documentSplit, Pass 1–3 only for large documents) using the LLM-Script cooperative process.

### Pass 1 — LLM Initial Extraction

1. **Document review** — The LLM reads the canonical input document (or documentSplit text + ancestor stack) and identifies the source family, structural hierarchy pattern (e.g., Part > Chapter > Regulation > Paragraph), and non-standard structural features.
2. **LLM heading extraction** — Extract all headings at every structural level, assigning a tentative `Heading_Level` and `Heading_Number` to each. Draft an initial heading grammar.
   > **Heading identification rule:** A heading does NOT contain a sentence.

3. **Assign Heading_ID** — Each heading receives a provisional ID:
   - Regular document: `{DocumentKey}_HD_{SeqNo}`
   - documentSplit: `{DocumentKey}_HD_s{NNN}_{SeqNo}` (documentSplit-local; replaced after merge)

Output: `doc-{doc_instance_key}__heading__extraction_llm.tsv` (or `documentSplit-{...}__heading__extraction_llm.tsv`)

### Pass 2 — Script Full Match and Omission Detection

> The "script" here is not a pre-existing external program. The LLM analyses the Pass 1 results and draft grammar to produce a **regex specification** (JSON format). A **fixed runner script** (`scripts/step2_regex_runner.py`) executes the regex patterns against the canonical input document. The script produces a **full match set**, not just omission candidates. Discrepancies are computed by alignment.

4. **Regex spec generation and full match scan** — The LLM derives regex patterns (numbering schemes, keyword prefixes like `Part`, `Chapter`, `Reg.`, `Art.`) from the Pass 1 results and draft grammar, outputting them as a **JSON array**. The Coordinator (or runner script) compiles each pattern (log `Warning` on `re.error`, do not silently skip), executes them against the canonical input, and produces the **full script match set**.

   **Regex spec JSON schema:**

   ```json
   [
     {
       "pattern": "<regex with named groups>",
       "expected_level": "<HeadingLevel>",
       "number_group": "<named group for heading number, or null>",
       "text_group": "<named group for heading text, or null>",
       "flags": ["IGNORECASE"],
       "priority": 1,
       "notes": "optional description"
     }
   ]
   ```

   > `number_group` and `text_group` refer to named capture groups in the regex pattern. These enable `Number_mismatch` detection. If `number_group` is null, `Number_mismatch` cannot be determined and is not flagged.
   >
   > Allowed `flags` values: `IGNORECASE`, `MULTILINE`. Other Python `re` flags are not permitted to ensure runner portability.

   **Multi-match resolution:** When multiple patterns match the same line, the runner selects the match with the highest `priority` value (1 = highest priority). On tie, the longest match wins. On further tie, the pattern appearing first in the spec array wins. Only the selected match is included in the full match set for that line.

5. **LLM cross-check** — The LLM aligns the Pass 1 heading list against the script's full match set and classifies each entry:
   - `Agreed`: both LLM and script identify a heading at the same line
   - `LLM_only`: extracted by LLM but not matched by any script pattern (potential false positive or non-standard format)
   - `Script_only`: matched by script but not extracted by LLM (potential omission)
   - `Level_mismatch`: both identify a heading but assign different levels (LLM level vs script's `expected_level`)
   - `Number_mismatch`: both identify a heading but the captured number differs (requires `number_group` in regex spec; not flagged if `number_group` is null)

Output: `doc-{doc_instance_key}__heading__extraction_script.tsv` (full match set), `doc-{doc_instance_key}__heading__discrepancy.tsv`

The `heading__extraction_script.tsv` follows the same column structure as `heading__extraction_llm.tsv`, with additional columns: `Matched_Pattern_Index` (int, index into regex spec array), `Matched_Text` (string, text captured by the pattern).

### Pass 3 — Cross-Verification and Correction

Cross-verify Pass 1 and Pass 2 results and correct discrepancies.

6. **Cross-verification**
   - **String matching** — Script-based matching of Pass 1 and Pass 2 results for classification
   - **LLM adjudication** — LLM reviews mismatches and corrects (false positive removal, non-standard heading addition, level/number correction)
   - **Logging** — Record mismatches and resolution results
7. **Regex spec update** — If new structural patterns are discovered, add regex patterns and save grammar update proposals to `results/grammars/staging/`.

> **Single-writer principle:** Only the Coordinator writes to the confirmed grammar file. Agents save grammar candidates to staging; other agents cannot reuse them until the Coordinator merges.

### Pass 4 — Final Omission Check

> For large documents (> {{split_threshold:64K}} tokens), Pass 4 runs at **document level** after Coordinator merge, not at documentSplit level. The agent receives the merged heading tree, the confirmed grammar (post-merge), and Pass 4 for large documents operates in **split mode**: the Coordinator's regex runner executes the final regex spec against the full canonical input document (script execution, not LLM). The runner produces a list of flagged omission candidates with their line numbers. The Pass 4 LLM agent then reviews ONLY the flagged candidates, receiving each candidate with ±{{p4_context:50}} lines of surrounding context. The agent does NOT receive the full document text. This ensures Pass 4 stays within the context window budget.

8. **Regex spec final scan** — The LLM updates the regex spec JSON based on the **confirmed grammar** (promoted by Coordinator after Pass 3), and the Coordinator (or runner) executes it one last time against the full document. Flags any **remaining omission candidates**.
9. **LLM final review** — Review flagged remaining candidates and make final judgements. If new headings are confirmed, add them and update the grammar candidate. Perform:
   - **Coverage check**: Classify every line as heading or non-heading. Produce `doc-{doc_instance_key}__heading__coverage.json` recording line ranges and their classification.
   - **Format consistency verification**: Verify all headings follow the confirmed grammar patterns.
10. **Final discrepancy log** — Extract all remaining Warning/Info entries from the working discrepancy TSV into `doc-{doc_instance_key}__heading__discrepancy_final.tsv`. This file is **promoted** (not discarded) for post-approval audit trail.

Output: `doc-{doc_instance_key}__heading__structure.tsv` (final), `doc-{doc_instance_key}__heading__regex_spec.json` (final; promoted for reuse on same-DocType documents), `doc-{doc_instance_key}__heading__coverage.json`, `doc-{doc_instance_key}__heading__discrepancy_final.tsv`

> **Post-Pass 4 grammar update:** If Pass 4 produces an updated grammar candidate, the agent saves it to `results/grammars/staging/`. The Coordinator performs a final merge, increments the grammar version, and promotes it as the definitive grammar for this DocType. This fully promoted grammar is reused for subsequent documents of the same DocType.

---

## 2.4 Convergence Criteria and Discrepancy Handling

### Iteration Trigger Conditions

- **Trigger:** An iteration is triggered when `Error > 0` at the end of Pass 3. Iterations are not triggered for `Warning`-only results.
- **Scope:** Re-execute from Pass 2 (including regex spec update) through Pass 3.
- **Maximum iterations:** 2. If `Error` remains after the 2nd iteration, escalate.

### Escalation Procedure

- **Target:** User (project operator).
- **Format:** Report with the final discrepancy TSV (`discrepancy_final.tsv`) and a list of remaining Errors attached.
- **Post-escalation:** Processing of the affected Document is **suspended**. Resume after the user provides manual correction or further instructions.

### Severity Classification

- Items where the LLM cannot confidently determine heading status from regex matches (`Warning`) are recorded in the **final discrepancy TSV** and flagged for user approval.

| Severity | Criteria |
|:---|:---|
| `Error` | Missing or demonstrably wrong → **0** tolerated |
| `Warning` | Ambiguous judgement → **≤ max({{warn_min:3}}, ⌈total_headings × {{warn_ratio:0.02}}⌉)** tolerated; excess requires user confirmation |
| `Info` | Formatting difference (no structural impact) → logged only |

### Coordinator Grammar Merge Conflict Resolution Rules

- **Same pattern, different level:** Adopt the level with higher occurrence frequency in the document. If frequency is equal, adopt the lower (higher-hierarchy) level.
- **Pattern duplication:** When two agents match the same heading with different regex patterns, adopt the more specific (narrower match scope) pattern and discard the other.
- **Unresolvable conflicts:** If automatic resolution is not possible, report the conflict details to the user and request manual decision.

---

## 2.5 Token Measurement per Heading

Measure the token count of the content under each heading. See §2.6 Output Schema for column definitions.

- **Method**: `tiktoken` (`cl100k_base` encoding). The same encoding must be used project-wide to ensure consistency with Step 3 chunking thresholds.
- **Fallback**: If `tiktoken` is unavailable, use `char_approx` (`ceil(char_count / {{approx_divisor:4}} × {{approx_multiplier:1.1}})`). Record `char_approx` in the `Measure_Method` column.
- **Timing**: Performed after Pass 4 completion, when generating the final `heading__structure.tsv`.

---

## 2.6 Output Schema

`doc-{doc_instance_key}__heading__structure.tsv`:

| Column | Type | Required | Description |
|:---|:---|:---:|:---|
| `Heading_ID` | string | Yes | `{DocumentKey}_HD_{NNN}` — min-width {{hdid_digits:3}} digits, zero-padded. If heading count exceeds {{hdid_expand:999}}, expand to 4+ digits. Starting from 000 (DocumentRoot row). Since DocumentKey itself contains underscores, use `_HD_` as the parsing delimiter. |
| `Parent_Heading_ID` | string\|null | Yes | `Heading_ID` of the parent node; empty string for the DocumentRoot row (Depth=0). **TSV null convention:** empty field (no characters between column delimiters). In TSV, this means two adjacent tabs for mid-row fields, or a tab followed by newline for the last column. |
| `Depth` | int | Yes | Tree depth: DocumentRoot = 0 (synthetic row), first heading level = 1, etc. Depth is determined by the heading's position in the document tree hierarchy, **not** by the raw markdown heading level. Step 1.1 Markdown Lint (HL001) guarantees that heading levels increment by exactly one, so Depth = markdown `#` count − 1 after lint. If lint was not applied and levels are skipped, compress depth to sequential values (e.g., `#` → `###` with no `##` maps to Depth 1 → 2, not 1 → 3). |
| `Heading_Level` | string | Yes | Hierarchy level name from the document (e.g., `DocumentRoot`, `Chapter`, `Part`, `Regulation`, `Paragraph`). The Depth=0 row uses `DocumentRoot`. |
| `Heading_Number` | string\|null | Yes | Original numbering as it appears in the document (e.g., `II-1`, `A`, `1.1.3`). Empty string for the DocumentRoot row and for unnumbered headings. |
| `Heading_Text` | string | Yes | Full heading title text |
| `Start_Line` | int | Yes | First line of this heading's span in the canonical input file (**inclusive**). For the DocumentRoot row: line 1. |
| `End_Line` | int | Yes | Last line of this heading's span (**inclusive**). Defined as: line immediately before the next heading at depth ≤ current depth. For DocumentRoot and last heading: document's final line number. |
| `Est_Tokens_Inclusive` | int | Yes | Token count for full span `[Start_Line, End_Line]` including descendants. **Non-additive.** |
| `Est_Tokens_Exclusive` | int | Yes | Token count for own content only (excluding descendants). **Additive** within subtrees. Invariant: `parent.exclusive + Σ(children.inclusive) = parent.inclusive`. |
| `Measure_Method` | string | Yes | `tiktoken` or `char_approx` |

> **TSV null convention:** Use an empty field (no characters between column delimiters). In TSV, this means two adjacent tabs for mid-row fields, or a tab followed by newline for the last column. Do not write the literal string `null` or `\N`.
>
> The **first row** (Depth=0) is a **synthetic DocumentRoot row** representing the document itself. It is not a heading extracted from the text. All actual headings have Depth ≥ 1. The DocumentRoot's `Est_Tokens_Inclusive` equals the total document token count; its `Est_Tokens_Exclusive` covers only content before the first Depth=1 heading (preamble text).

```tsv
Heading_ID	Parent_Heading_ID	Depth	Heading_Level	Heading_Number	Heading_Text	Start_Line	End_Line	Est_Tokens_Inclusive	Est_Tokens_Exclusive	Measure_Method
solas_ii_1_HD_000		0	DocumentRoot		SOLAS Chapter II-1	1	2830	38200	320	tiktoken
solas_ii_1_HD_001	solas_ii_1_HD_000	1	Part	A	General	47	312	4100	200	tiktoken
solas_ii_1_HD_002	solas_ii_1_HD_001	2	Regulation	1	Application	48	89	620	620	tiktoken
...
```

---

`doc-{doc_instance_key}__heading__regex_spec.json`:

```json
[
  {
    "pattern": "<regex with named groups>",
    "expected_level": "<HeadingLevel>",
    "number_group": "<named group name | null>",
    "text_group": "<named group name | null>",
    "flags": ["IGNORECASE"],
    "priority": 1,
    "notes": "optional"
  }
]
```

| Field | Type | Required | Description |
|:---|:---|:---:|:---|
| `pattern` | string | Yes | Regex with named capture groups. Python `re` compatible. |
| `expected_level` | string | Yes | Heading level assigned to matches (e.g., `Chapter`, `Regulation`). |
| `number_group` | string\|null | Yes | Named group that captures heading number. `null` if not applicable. |
| `text_group` | string\|null | Yes | Named group that captures heading text. `null` if not applicable. |
| `flags` | string[] | Yes | Allowed values: `IGNORECASE`, `MULTILINE` only. |
| `priority` | int | Yes | Multi-match tie-break: lowest value wins (1 = highest priority) → longest match → array order. |
| `notes` | string | No | Optional description. |

---

> For file naming rules and storage paths, see [pre_specification.md](pre_specification.md) §File Naming Convention.
