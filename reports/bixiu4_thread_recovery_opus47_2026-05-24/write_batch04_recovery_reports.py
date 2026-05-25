from __future__ import annotations

from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RECOVERY = ROOT / "reports" / "bixiu4_thread_recovery_opus47_2026-05-24"


def now_stamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M +08")


def write_report(name: str, body: str) -> None:
    path = RECOVERY / name
    path.write_text(body.strip() + "\n", encoding="utf-8")
    print(path)


STAMP = now_stamp()

batch04_result = f"""
# OPUS47_CLAUDECODE_BATCH04_2026_SHIJINGSHAN_ERMO_RECHECK_RESULT

Status: `OPUS47_BATCH04_SHIJINGSHAN_RECHECK_DONE__CORRECTION_APPLIED__MODEL_GATE_BLOCKED`

Timestamp: {STAMP}

## Real Call Evidence

This was a real ClaudeCode lane call, not a Codex simulation.

- Command: `claude -p --model claude-opus-4-7 --effort max --permission-mode auto --output-format json --debug-file OPUS47_CLAUDECODE_BATCH04_2026_SHIJINGSHAN_ERMO_RECHECK_DEBUG.log --no-session-persistence < OPUS47_CLAUDECODE_BATCH04_2026_SHIJINGSHAN_ERMO_RECHECK_PROMPT.md`
- Prompt: `OPUS47_CLAUDECODE_BATCH04_2026_SHIJINGSHAN_ERMO_RECHECK_PROMPT.md`
- RAW JSON: `OPUS47_CLAUDECODE_BATCH04_2026_SHIJINGSHAN_ERMO_RECHECK_RAW.json`
- Debug log: `OPUS47_CLAUDECODE_BATCH04_2026_SHIJINGSHAN_ERMO_RECHECK_DEBUG.log`
- Runtime: `duration_ms=519241`, `num_turns=46`, `terminal_reason=completed`, `fast_mode_state=off`
- Model proof: RAW JSON `modelUsage` includes large `claude-opus-4-7`; debug log records `model=claude-opus-4-7 modelSupported=true`.
- Model caution: RAW JSON also includes small auxiliary `claude-haiku-4-5-20251001` usage, and the runtime does not expose enough internal proof that `--effort max` / adaptive thinking was actually active.

Model gate decision: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`

## ClaudeCode Content Finding

ClaudeCode returned: `pass_with_corrections` under the blocked model gate.

Accepted content findings:

- Q1 official key A was checked; only correct option ② supports `系统观念 / 系统优化`; option ① is politics-and-law and is not inserted into the philosophy body.
- Q2 official key D was checked; only correct option ④ supports `矛盾就是对立统一`; option ② is the culture/national-spirit line and is excluded from this body.
- Q3 official key B was checked; correct options ①③ support `整体与部分` and `矛盾的特殊性 / 具体问题具体分析`; wrong option ④ was not used.
- Q9 official key D was checked; correct options ③④ support `实践是认识的基础` and `人民群众`.
- Q17(3) is source-supported only as optional scoring-reference angles: `联系、矛盾、实践与认识关系`. It must not be treated as three cumulative strong scoring points.
- Q20 remains excluded because `系统观` appears only as a broad optional angle inside a multi-module comprehensive question, without a specific philosophy material-to-answer chain.
- No ordinary reference answer is promoted to a scoring rubric; selection-question entries are labeled as official answer-key plus correct-option chains.

## Correction Applied

ClaudeCode found a matrix mirror lag:

- `M0034`, `M0035`, `M0036` still had structured `证据等级=强细则`.
- The authoritative accepted JSONL and candidate mirror rows already used `正式评分参考角度`.

Codex applied the correction with backup:

- Backup: `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_batch04_claudecode_mirror_correction_20260525_005508.csv`
- Updated rows: `M0034`, `M0035`, `M0036`
- New structured evidence label: `正式评分参考角度`
- `是否误放`: `否`
- `是否需补厚`: `否`

## Post-Correction Verification

- Matrix total rows: `860`
- `2026石景山二模` matrix rows: `36`
- `2026石景山二模` active suite-pending rows: `0`
- Exact global rows still marked production-line candidate: `485`
- Rows still marked as needing source/fusion adjudication: `485`
- Insert ledger rows: `47`
- DOCX/PDF rerendered after Batch04: `238` PDF pages
- Inserted-label style check: `188 / 188` pass
- Student-facing residue scan: `0` hits for the current banlist

## Boundary

This result is useful batch-level content evidence, but it is not a final acceptance gate. The model/effort proof remains blocked, GPTPro full-artifact review remains `real_call_pending`, and Claude Opus external full-artifact review remains pending.

Decision: `batch04-preliminary-pass-with-correction-applied-model-gate-blocked`
"""

batch04_report = f"""
# COVERAGE_FUSION_BATCH04_2026_SHIJINGSHAN_ERMO_CODEX_20260525

Status: `CODEX_BATCH04_DONE__CLAUDECODE_PRELIMINARY_PASS_WITH_CORRECTION_APPLIED__MODEL_GATE_BLOCKED`

Timestamp: {STAMP}

## Scope

Batch04 covers `2026石景山二模` inside `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`.

Rows closed this round:

- existing candidate rows: `M0155`, `M0156`, `M0244`
- suite-source rows: `M0736` through `M0755`
- ClaudeCode mirror correction rows: `M0034`, `M0035`, `M0036`

Result: all active `2026石景山二模` rows now have explicit covered / inserted / excluded / residue dispositions. Suite-local active pending rows: `0`.

Global recovery matrix after Batch04:

- exact production-line candidate rows still open: `485`
- rows still marked as needing source/fusion adjudication: `485`

## Source Authority Used

Primary source bundle:

`01_source_inventory/suite_source_bundles/2026石景山二模.md`

Key source positions:

- lines 17-19: official choice answer key, Q1-Q15 = `A D B C C D B D D B B A A A D`.
- lines 21-22: Q16 is `经济与社会`.
- lines 23-50: Q17 scoring reference; Q17(1) is `政治与法治`, Q17(2) is `逻辑与思维`, Q17(3) is philosophy optional-angle scoring.
- lines 49-71: Q17(3) says one philosophy viewpoint may be used and lists `联系、矛盾、实践与认识关系` as allowed angles. This supports inclusion but not cumulative three-point scoring.
- lines 72-78: Q18 is international politics/economy, Q19 is law, and Q20 lists `系统观` only as one broad optional angle in a multi-module comprehensive question.
- lines 116-121: Q1 stem/options; correct option ② supports the system node.
- lines 122-127: Q2 stem/options; correct option ④ supports contradiction; option ② is culture/national spirit and is excluded from this philosophy body.
- lines 128-133: Q3 stem/options; correct options ①③ support whole/part and concrete analysis; wrong option ④ is not used.
- lines 158-163: Q9 stem/options; correct options ③④ support practice and people.

## DOCX Changes

New final-body entries inserted:

| node | heading | basis |
|---|---|---|
| 系统观念 / 系统优化 | `25. 2026石景山二模 第1题（选择题）` | official key Q1=A; only correct option ② is used for the system chain |
| 矛盾就是对立统一 | `36. 2026石景山二模 第2题（选择题）` | official key Q2=D; only correct option ④ is used for the opposition-unity chain |
| 整体与部分 | `16. 2026石景山二模 第3题（选择题）` | official key Q3=B; correct options ①③ link big-picture planning and detailed implementation |
| 矛盾的特殊性 / 具体问题具体分析 | `27. 2026石景山二模 第3题（选择题）` | official key Q3=B; correct option ① says 因地制宜、精准发力 |
| 实践是认识的基础 | `27. 2026石景山二模 第9题（选择题）` | official key Q9=D; correct options ③④ emphasize actual work and practice testing |
| 人民群众 | `26. 2026石景山二模 第9题（选择题）` | official key Q9=D; correct option ④ says performance must withstand people's test |

Existing Q17(3) final-body entries retained, but evidence labels are downgraded to `正式评分参考角度`:

- `联系的普遍性 / 联系的观点（总）`
- `矛盾就是对立统一`
- `实践与认识（总）`

No DOCX insertion was made for Q20. Its scoring reference lists `系统观` only as one broad optional angle in a multi-module comprehensive question, without a specific philosophy material-to-answer chain.

## ClaudeCode Correction

Real ClaudeCode Opus 4.7 Batch04 recheck completed under a blocked model gate.

Required correction found and applied:

- `M0034`, `M0035`, `M0036` were still labeled `强细则` in the structured matrix column.
- They now match accepted JSONL and candidate rows as `正式评分参考角度`.
- Backup: `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_batch04_claudecode_mirror_correction_20260525_005508.csv`

## Matrix And Ledger Verification

Updated files:

- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `05_delivery/docx_insert_ledger.csv`
- `04_fusion_audit/student_patch_entries.accepted.jsonl`
- current DOCX/PDF in `05_delivery/`

Post-update verification:

- `2026石景山二模` matrix rows: `36`
- `2026石景山二模` active suite-pending rows: `0`
- global active candidate rows: `485`
- insert ledger rows: `47`
- inserted ledger headings found in DOCX: `47 / 47`
- inserted label paragraphs: `188 / 188` pass style check

DOCX exact text hits after insertion:

- `2026石景山二模 第1题`: `1`
- `2026石景山二模 第2题`: `1`
- `2026石景山二模 第3题`: `2`
- `2026石景山二模 第9题`: `2`
- `2026石景山二模 第17(3)题`: `3`

## Render QA

Render results after Batch04:

- DOCX size: `353,607` bytes
- PDF size: `3,548,768` bytes
- PDF page count: `238`
- rendered page PNGs: `238`
- contact sheet exists: `07_render_check/word_pdf_pages/contact_every_12_pages.png`
- automated page-image scan: `238` pages checked; only `page_002.png` is near-blank and is the intended foreword title page

PDF normalized search pages:

- Q1 inserted entry: page `77`
- Q2 inserted entry: page `123`
- Q3 inserted entries: pages `67`, `135`
- Q9 inserted entries: pages `175`, `207`
- existing Q17(3) entries: pages `54`, `122`, `164`
- Q20: no final-body hit, as intended

Student-facing residue scan returned `0` hits in DOCX/PDF for the current banlist, including audit residues, source-lane terms, reference-answer residues, local paths, and the removed 2024海淀一模 Q17(2) misplacement.

## Boundary

This is not final acceptance. It is a Codex production-line batch closure for one suite, with a real but model-gate-blocked ClaudeCode Opus 4.7 recheck. GPTPro web / Claude Opus external full-artifact review remains `real_call_pending`.
"""

model_ledger = f"""
# MODEL_EVIDENCE_LEDGER

Status: `OPUS47_BATCH04_ADDED__BLOCKED_MODEL_CONFIRMATION_REQUIRED_FOR_EFFORT_PROOF`

Timestamp: {STAMP}

## Required Standard

Qualified new ClaudeCode evidence must prove all of the following:

- Model lane: ClaudeCode, not Codex simulation.
- Model identity: Opus 4.7 or a CLI-resolved Opus alias that emits auditable evidence showing the actual Opus 4.7 model.
- Reasoning setting: max effort / adaptive thinking, not default unknown effort.
- Command evidence: timestamp, command, input prompt, output path, and debug/JSON/model metadata where available.
- Output boundary: the output may support audit decisions but cannot replace row-level source evidence.

## Known Invalid Evidence

| time +08 | command/model | output | qualification |
|---|---|---|---|
| 2026-05-24 22:01 | `claude.exe -p --model sonnet` | `03_claudecode_lane/claudecode_verify_gptpro_web_fixes_20260524.md` | invalid; not counted |
| 2026-05-24 22:09 | `claude.exe -p --model sonnet` | `03_claudecode_lane/claudecode_verify_batch03_cleanup_20260524.md` | invalid; not counted |

## New Evidence Slots

| evidence id | time +08 | command | model proof | effort proof | input | output | status |
|---|---|---|---|---|---|---|---|
| OPUS47_RECHECK_001 | 2026-05-24 22:59-23:06 | `claude -p --model claude-opus-4-7 --effort max ... < OPUS47_CLAUDECODE_RECHECK_PROMPT.md` | JSON/debug show `claude-opus-4-7` | command includes `--effort max`, but runtime proof is insufficient | `OPUS47_CLAUDECODE_RECHECK_PROMPT.md` | `OPUS47_CLAUDECODE_RECHECK_RESULT.md`, RAW/debug artifacts | `blocked` |
| OPUS47_ROW_RECHECK_001 | 2026-05-24 23:37-23:41 | `claude -p --model claude-opus-4-7 --effort max ... < OPUS47_CLAUDECODE_ROW_SOURCE_RECHECK_PROMPT.md` | JSON/debug show `claude-opus-4-7` | command includes `--effort max`, but runtime proof is insufficient; minor Haiku auxiliary exists | `OPUS47_CLAUDECODE_ROW_SOURCE_RECHECK_PROMPT.md` | `OPUS47_CLAUDECODE_ROW_SOURCE_RECHECK_RESULT.md`, RAW/debug artifacts | `pass_with_model_gate_blocked` |
| OPUS47_BATCH02_HAIDIAN_RECHECK_001 | 2026-05-24 23:57-2026-05-25 00:04 | `claude -p --model claude-opus-4-7 --effort max ... < OPUS47_CLAUDECODE_BATCH02_2024_HAIDIAN_RECHECK_PROMPT.md` | JSON/debug show `claude-opus-4-7` | command includes `--effort max`, but runtime proof is insufficient; minor Haiku auxiliary exists | `OPUS47_CLAUDECODE_BATCH02_2024_HAIDIAN_RECHECK_PROMPT.md` | `OPUS47_CLAUDECODE_BATCH02_2024_HAIDIAN_RECHECK_RESULT.md`, RAW/debug artifacts | `pass_with_corrections_model_gate_blocked` |
| OPUS47_BATCH03_CHAOYANG_RECHECK_001 | 2026-05-25 00:23-00:28 | `claude -p --model claude-opus-4-7 --effort max ... < OPUS47_CLAUDECODE_BATCH03_2026_CHAOYANG_ERMO_RECHECK_PROMPT.md` | JSON/debug show `claude-opus-4-7` | command includes `--effort max`, but runtime proof is insufficient; minor Haiku auxiliary exists | `OPUS47_CLAUDECODE_BATCH03_2026_CHAOYANG_ERMO_RECHECK_PROMPT.md` | `OPUS47_CLAUDECODE_BATCH03_2026_CHAOYANG_ERMO_RECHECK_RESULT.md`, RAW/debug artifacts | `pass_with_corrections_model_gate_blocked` |
| OPUS47_BATCH04_SHIJINGSHAN_RECHECK_001 | 2026-05-25 00:43-00:51 | `claude -p --model claude-opus-4-7 --effort max --permission-mode auto --output-format json --debug-file OPUS47_CLAUDECODE_BATCH04_2026_SHIJINGSHAN_ERMO_RECHECK_DEBUG.log --no-session-persistence < OPUS47_CLAUDECODE_BATCH04_2026_SHIJINGSHAN_ERMO_RECHECK_PROMPT.md` | RAW JSON `modelUsage` includes large `claude-opus-4-7`; debug records `model=claude-opus-4-7 modelSupported=true` | command includes `--effort max`, but runtime proof is insufficient; RAW JSON includes minor `claude-haiku-4-5-20251001` auxiliary usage | `OPUS47_CLAUDECODE_BATCH04_2026_SHIJINGSHAN_ERMO_RECHECK_PROMPT.md` | `OPUS47_CLAUDECODE_BATCH04_2026_SHIJINGSHAN_ERMO_RECHECK_RESULT.md`, RAW/debug artifacts | `pass_with_corrections_model_gate_blocked`; M0034-M0036 correction applied |

## Batch04 Result Summary

- Exit status: shell command completed successfully.
- ClaudeCode content result: `pass_with_corrections`.
- Model identity: runtime/RAW JSON and debug log show `claude-opus-4-7`.
- Effort/adaptive-thinking evidence: still unverified by the lane; therefore no qualified final PASS.
- Additional caution: RAW JSON includes small auxiliary `claude-haiku-4-5-20251001` usage.
- Content correction accepted and applied: `2026石景山二模 Q17(3)` rows `M0034`, `M0035`, `M0036` were downgraded in the structured matrix column from `强细则` to `正式评分参考角度`.
- Content observation: Batch04 source placement is defensible after correction; Q1/Q2/Q3/Q9 insertions use official answer-key plus correct-option chains, Q17(3) is optional scoring-reference angle support only, and Q20 remains excluded as broad optional-angle wording.

## Boundary

No Sonnet, Haiku-only, or model-unknown output is counted as qualified ClaudeCode evidence. Current decision remains:

Decision: `blocked-model-confirmation-required`
"""

thread_status = f"""
# THREAD_RECOVERY_STATUS_20260524

Status: `RECOVERED_EXECUTION_IN_PROGRESS`

Timestamp: {STAMP}

## Recovery Position

This thread has taken over execution from the failed old thread. It does not fork from the old active goal and does not treat the old Sonnet evidence as valid ClaudeCode evidence.

Recovery directory:

`reports/bixiu4_thread_recovery_opus47_2026-05-24/`

## Completed In Recovery

1. Created/updated recovery control files:
   - `THREAD_RECOVERY_STATUS_20260524.md`
   - `SONNET_INVALIDATION_LEDGER.md`
   - `MODEL_EVIDENCE_LEDGER.md`
   - `OPUS47_CLAUDECODE_RECHECK_PROMPT.md`
   - `OPUS47_CLAUDECODE_RECHECK_RESULT.md`
2. Invalidated the 22:01 and 22:09 `sonnet` ClaudeCode calls as qualified evidence.
3. Built `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv` with 860 rows.
4. Cleaned student-facing audit residues and rerendered DOCX/PDF.
5. Fixed inserted-label style mismatch and verified inserted labels.
6. Corrected the `2026石景山二模 Q17(3)` material-trigger/evidence-label issue.
7. Completed Batch01 source recitation for the 9 accepted rows flagged by Opus observation.
8. Completed Batch02 for `2024海淀一模`; removed misplaced Q17(2), synchronized ledger, rerendered, and applied ClaudeCode Q16 evidence downgrade.
9. Completed Batch03 for `2026朝阳二模`; inserted Q1/Q3/Q4, retained supported Q16/Q21, excluded Q5/Q20, rerendered, and applied ClaudeCode non-blocking corrections.
10. Completed Batch04 for `2026石景山二模`; inserted Q1/Q2/Q3/Q9, retained Q17(3) only as optional scoring-reference angles, excluded Q20, rerendered, and applied ClaudeCode matrix mirror correction for `M0034`, `M0035`, `M0036`.

## Current Artifact Snapshot

- Current DOCX: `353,607` bytes.
- Current PDF: `3,548,768` bytes.
- PDF page count: `238`.
- Rendered page PNGs: `238` plus contact sheet.
- `docx_insert_ledger.csv`: `47` rows, `47 / 47` exact heading matches in DOCX.
- Inserted label style check: `188 / 188` label paragraphs pass.
- Automated DOCX/PDF scans: `0` hits for audit/source-lane residue terms, reference-answer residue terms, local paths, and the removed 2024海淀一模 Q17(2) misplacement.

## Matrix Snapshot

- Total rows: `860`.
- Batch02 `2024海淀一模` active pending rows: `0`.
- Batch03 `2026朝阳二模` active pending rows: `0`.
- Batch04 `2026石景山二模` active pending rows: `0`.
- Exact rows still marked production-line candidate: `485`.
- Rows still marked as needing source/fusion adjudication: `485`.

## ClaudeCode / Model State

Real calls completed:

- `OPUS47_RECHECK_001`
- `OPUS47_ROW_RECHECK_001`
- `OPUS47_BATCH02_HAIDIAN_RECHECK_001`
- `OPUS47_BATCH03_CHAOYANG_RECHECK_001`
- `OPUS47_BATCH04_SHIJINGSHAN_RECHECK_001`

All used `claude-opus-4-7 --effort max` and produced Opus runtime evidence, but none can expose enough max-effort/adaptive-thinking proof to satisfy the user's hard gate. Some RAW JSON also includes minor Haiku auxiliary usage. Therefore the model state remains:

`BLOCKED_MODEL_CONFIRMATION_REQUIRED`

No Sonnet/Haiku-only/model-unknown output is being counted as qualified ClaudeCode evidence.

## Open Blockers

1. Opus 4.7 max-effort/adaptive-thinking proof is still blocked.
2. GPTPro full-artifact web review remains `real_call_pending`.
3. Claude Opus external full-artifact teaching/content review remains pending/not final.
4. `485` production-line candidate rows still need source/fusion disposition if the target is true full-question exhaustion.
5. Full every-page manual typography comparison is not claimed.

## Decision

Decision: `recovered-execution-in-progress`
"""

format_qa = f"""
# FORMAT_RENDER_QA_20260524

Status: `FORMAT_QA_BATCH04_RERENDERED_STILL_NOT_FINAL`

Timestamp: {STAMP}

## Files Checked

- DOCX: `05_delivery/哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.docx`
- PDF: `05_delivery/哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.pdf`
- Insert ledger: `05_delivery/docx_insert_ledger.csv`
- Render folder: `07_render_check/word_pdf_pages/`
- Batch notes: Batch01 source recitation, Batch02 海淀一模, Batch03 朝阳二模, Batch04 石景山二模.

## Fixes Covered

| fix | result |
|---|---|
| Student-facing audit/source residue cleanup | 0 residual hits in current DOCX/PDF |
| Inserted label style normalization | current ledger entries checked; `188 / 188` label paragraphs pass |
| 2024海淀一模 Q17(2) misplacement removal | old system-optimization entry removed; no residual DOCX/PDF hit |
| Batch02 Q16 evidence-label downgrade | matrix evidence label downgraded; no DOCX body change |
| Batch03 2026朝阳二模 insertions | Q1/Q3/Q4 inserted; Q16/Q21 confirmed already covered; Q5/Q20 exclusions retained |
| Batch04 2026石景山二模 insertions | Q1/Q2/Q3/Q9 inserted; Q17(3) downgraded to optional scoring-reference angles; Q20 excluded |
| Batch04 ClaudeCode correction | `M0034`, `M0035`, `M0036` matrix evidence labels synced to `正式评分参考角度` |

## Rerender And Page Checks

| check | result |
|---|---|
| Final DOCX exists | PASS: `353,607` bytes |
| Final PDF exists | PASS: `3,548,768` bytes |
| PDF page count | PASS: `238` pages |
| Rendered page PNGs | PASS: `page_001.png` through `page_238.png` exist |
| Contact sheet | PASS: `contact_every_12_pages.png` exists |
| Insert ledger rows | PASS: `47` |
| Insert ledger exact heading match | PASS: `47 / 47` headings found in current DOCX |
| Inserted label style after Batch04 | PASS: `188 / 188` label paragraphs match the old label pattern |
| Page-image dimensions | PASS: all rendered pages are `993 x 1404 px` |
| Blank-like pages | INFO/PASS: only `page_002.png`, the intended foreword title page |

## Batch04 PDF Search

PDF normalized text search after rerender:

- `2026石景山二模 第1题`: page `77`
- `2026石景山二模 第2题`: page `123`
- `2026石景山二模 第3题`: pages `67`, `135`
- `2026石景山二模 第9题`: pages `175`, `207`
- `2026石景山二模 第17(3)题`: pages `54`, `122`, `164`
- `2026石景山二模 第20题`: no final-body hit, as intended

## Student-Facing Residue Scan

After the Batch04 rerender, automated DOCX and PDF scans returned `0` hits for:

- audit residue terms
- `NEED_EVIDENCE`
- `source_lane`
- `correct_option_chain`
- reference-answer residue terms
- local path residues
- `source_repair_basis`
- removed `2024海淀一模 第17题第（2）问` misplacement text

## Visual Samples

Visual samples checked after Batch04: pages `67`, `77`, `123`, `135`, `175`, and `207`.

The automated page-image scan checked all 238 pages for near-blank output and edge clipping. It flagged only `page_002.png`; manual inspection confirms that page is a sparse foreword title page, not a render failure.

## Boundary

This remains short of final acceptance because full source/fusion closure, qualified Opus 4.7 max/adaptive proof, GPTPro full-artifact review, Claude Opus external full-artifact review, and a full every-page manual typography comparison remain open.

Decision: `format-improved-batch04-rerendered-still-not-final`
"""

governor = f"""
# GOVERNOR_RECOVERY_REPORT_20260524

Status: `RECOVERED_EXECUTION_IN_PROGRESS`

Timestamp: {STAMP}

## Scope

This Governor report covers:

`reports/bixiu4_thread_recovery_opus47_2026-05-24/`

It does not claim final acceptance of the handbook.

## Evidence Hygiene

Governor decision: `PASS_FOR_INVALIDATION`

Invalidated as qualified ClaudeCode evidence:

- `03_claudecode_lane/claudecode_verify_gptpro_web_fixes_20260524.md`
- `03_claudecode_lane/claudecode_verify_batch03_cleanup_20260524.md`

Reason: both came from `claude.exe -p --model sonnet` at 22:01 and 22:09. They remain historical pointers only.

## Opus 4.7 Gate

Governor decision: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`

Real commands ran with `--model claude-opus-4-7 --effort max`, and RAW/debug/model usage artifacts show `claude-opus-4-7`. However, the available CLI/debug/JSON artifacts still do not expose enough evidence that max-effort/adaptive-thinking was actually active. Therefore none of these runs can be promoted to qualified final ClaudeCode PASS:

- `OPUS47_RECHECK_001`
- `OPUS47_ROW_RECHECK_001`
- `OPUS47_BATCH02_HAIDIAN_RECHECK_001`
- `OPUS47_BATCH03_CHAOYANG_RECHECK_001`
- `OPUS47_BATCH04_SHIJINGSHAN_RECHECK_001`

Additional caution: RAW JSON usage includes small auxiliary Haiku usage on Opus runs, so no unqualified Opus-only final evidence is claimed.

## Coverage Matrix

`FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv` contains `860` rows.

Current state after Batch04:

- Batch02 `2024海淀一模` active pending rows: `0`.
- Batch03 `2026朝阳二模` active pending rows: `0`.
- Batch04 `2026石景山二模` active pending rows: `0`.
- Exact rows still marked production-line candidate: `485`.
- Rows still carrying need-source/fusion adjudication: `485`.

Boundary:

- This is a recovery control matrix, not final closure.
- Remaining candidate rows still require source/fusion disposition if the target is full-question exhaustion.

## Batch01

Governor decision: `CODEX_AND_CLAUDECODE_CONTENT_RECHECK_DONE__MODEL_GATE_STILL_BLOCKED`

`ROW_SOURCE_RECITATION_BATCH01_20260524.md` covers the 9 accepted rows flagged by the Opus observation. ClaudeCode Opus 4.7 row-source recheck found no content corrections required, but the model gate remains blocked.

## Batch02: 2024海淀一模

Governor decision: `CODEX_BATCH_DONE__CLAUDECODE_PRELIMINARY_PASS_WITH_CORRECTIONS__MODEL_GATE_BLOCKED`

Codex completed row-level source/fusion decisions, removed the misplaced Q17(2) system-optimization entry, synchronized the insert ledger, rerendered DOCX/PDF, and applied ClaudeCode's Q16 evidence downgrade.

## Batch03: 2026朝阳二模

Governor decision: `CODEX_BATCH_DONE__CLAUDECODE_PRELIMINARY_PASS_WITH_CORRECTIONS__MODEL_GATE_BLOCKED`

Codex completed all suite rows, inserted Q1/Q3/Q4 from official choice-key / correct-option chains, retained supported Q16/Q21, excluded Q5/Q20, rerendered DOCX/PDF, and applied ClaudeCode's two non-blocking corrections.

## Batch04: 2026石景山二模

Governor decision: `CODEX_BATCH_DONE__CLAUDECODE_PRELIMINARY_PASS_WITH_CORRECTION_APPLIED__MODEL_GATE_BLOCKED`

Codex completed:

- all 36 `2026石景山二模` matrix rows closed to explicit dispositions;
- Q1/Q2/Q3/Q9 final-body insertions from official choice-key / correct-option chains;
- Q17(3) retained only as optional scoring-reference-angle support, not cumulative strong scoring points;
- Q20 excluded as broad multi-module optional-angle wording;
- DOCX/PDF rerender and format QA refresh;
- ClaudeCode correction for `M0034`, `M0035`, `M0036` structured evidence labels.

This remains model-gate-blocked and is not final evidence.

## Format / Render Gate

Governor decision: `STYLE_AND_BATCH04_RENDER_CHECKED_STILL_SCOPE_BOUND`

Confirmed after latest rerender:

- DOCX exists: `353,607` bytes.
- PDF exists: `3,548,768` bytes.
- PDF page count: `238`.
- Rendered page PNGs: `238`, plus contact sheet.
- Insert ledger rows: `47`.
- Insert ledger exact heading matches: `47 / 47`.
- Inserted label style check: `188 / 188`.
- Automated DOCX/PDF scan: `0` hits for current residue banlist.
- Page-image scan: all `238` pages rendered at `993 x 1404 px`; only `page_002.png` is near-blank and was manually verified as the intended foreword page.

Boundary:

- Full every-page manual typography comparison is not claimed.

## External Review Gates

Governor decision: `real_call_pending`

- GPTPro web full-artifact review: `real_call_pending`.
- Claude Opus external full-artifact teaching/content review: pending/not final.
- Existing GPTPro work is scoped/pasted-payload review, not a full DOCX/PDF artifact pass.

## Governor Verdict

Verdict: `RECOVERED_EXECUTION_IN_PROGRESS`

The new thread has taken over, invalidated Sonnet evidence, made concrete DOCX/PDF and matrix corrections, completed three suite batches after the initial source-recitation round, and ran real Opus 4.7 ClaudeCode rechecks with corrections applied. The recovery is progressing, but final acceptance is still blocked.

Remaining blockers:

1. Opus 4.7 max-effort/adaptive-thinking proof gap.
2. GPTPro full-artifact web review pending.
3. Claude Opus external full-artifact review pending/not final.
4. `485` production-line candidate rows still needing source/fusion disposition.
5. Full every-page manual typography comparison not claimed.

Decision: `recovered-execution-in-progress`
"""

confucius = f"""
# CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524

Status: `ARTIFACTS_PRESENT_BUT_NOT_FINAL`

Timestamp: {STAMP}

## Recovery Artifacts

Required recovery artifacts exist:

- `THREAD_RECOVERY_STATUS_20260524.md`
- `SONNET_INVALIDATION_LEDGER.md`
- `MODEL_EVIDENCE_LEDGER.md`
- `OPUS47_CLAUDECODE_RECHECK_PROMPT.md`
- `OPUS47_CLAUDECODE_RECHECK_RESULT.md`
- `FORMAT_RENDER_QA_20260524.md`
- `GOVERNOR_RECOVERY_REPORT_20260524.md`
- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`

Additional Batch artifacts now exist:

- `ROW_SOURCE_RECITATION_BATCH01_20260524.md`
- `OPUS47_CLAUDECODE_ROW_SOURCE_RECHECK_PROMPT.md`
- `OPUS47_CLAUDECODE_ROW_SOURCE_RECHECK_RESULT.md`
- `COVERAGE_FUSION_BATCH02_2024_HAIDIAN_YIMO_CODEX_20260524.md`
- `MISPLACED_ENTRY_REMOVAL_2024_HAIDIAN_YIMO_Q17_2_20260524.md`
- `OPUS47_CLAUDECODE_BATCH02_2024_HAIDIAN_RECHECK_RESULT.md`
- `COVERAGE_FUSION_BATCH03_2026_CHAOYANG_ERMO_CODEX_20260525.md`
- `OPUS47_CLAUDECODE_BATCH03_2026_CHAOYANG_ERMO_RECHECK_RESULT.md`
- `COVERAGE_FUSION_BATCH04_2026_SHIJINGSHAN_ERMO_CODEX_20260525.md`
- `OPUS47_CLAUDECODE_BATCH04_2026_SHIJINGSHAN_ERMO_RECHECK_PROMPT.md`
- `OPUS47_CLAUDECODE_BATCH04_2026_SHIJINGSHAN_ERMO_RECHECK_RESULT.md`
- `OPUS47_CLAUDECODE_BATCH04_2026_SHIJINGSHAN_ERMO_RECHECK_RAW.json`
- `OPUS47_CLAUDECODE_BATCH04_2026_SHIJINGSHAN_ERMO_RECHECK_DEBUG.log`

## Artifact Check

| check | result |
|---|---|
| Sonnet evidence invalidated | PASS |
| New Opus 4.7 calls are real commands | PASS |
| Opus 4.7 max-effort/adaptive proof | BLOCKED |
| Batch01 source recitation exists | PASS |
| Batch02 `2024海淀一模` row decisions exist | PASS |
| Batch02 DOCX misplacement removal exists | PASS |
| Batch02 Q16 evidence downgrade applied | PASS |
| Batch03 `2026朝阳二模` row decisions exist | PASS |
| Batch03 Q1/Q3/Q4 insertions exist | PASS |
| Batch03 ClaudeCode non-blocking corrections applied | PASS |
| Batch04 `2026石景山二模` row decisions exist | PASS |
| Batch04 Q1/Q2/Q3/Q9 insertions exist | PASS |
| Batch04 Q17(3) evidence downgrade applied | PASS |
| Batch04 Q20 boundary exclusion retained | PASS |
| Batch04 ClaudeCode correction applied | PASS |
| Current DOCX/PDF rerendered | PASS |
| Student-facing residue scan | PASS |
| GPTPro full-artifact review | `real_call_pending` |
| Claude Opus external full-artifact review | pending/not final |
| Full source/fusion closure | OPEN |

## Student-Facing Artifact Snapshot

- DOCX: present, `353,607` bytes.
- PDF: present, `3,548,768` bytes.
- PDF pages: `238`.
- Rendered pages: `238` plus contact sheet.
- Insert ledger: `47` rows, all exact headings found in current DOCX.
- Inserted label styles: `188 / 188` pass.
- Removed misplacement: `2024海淀一模 第17题第（2）问` no longer appears in DOCX or PDF text extraction.
- Batch04 inserted search pages: Q1 page `77`, Q2 page `123`, Q3 pages `67` and `135`, Q9 pages `175` and `207`.

## Confucius Verdict

Verdict: `not_final`

A zero-baseline student can use the current artifact better than the pre-recovery state because style mismatches, residue terms, one off-question material trigger, one module-misplaced entry, and multiple missing district choice-question placements have been corrected. However, the artifact cannot be called final because the row matrix still has `485` candidate rows requiring source/fusion disposition, the qualified Opus effort proof is blocked, and the external full-artifact review gates remain open.
"""


def main() -> None:
    write_report("OPUS47_CLAUDECODE_BATCH04_2026_SHIJINGSHAN_ERMO_RECHECK_RESULT.md", batch04_result)
    write_report("COVERAGE_FUSION_BATCH04_2026_SHIJINGSHAN_ERMO_CODEX_20260525.md", batch04_report)
    write_report("MODEL_EVIDENCE_LEDGER.md", model_ledger)
    write_report("THREAD_RECOVERY_STATUS_20260524.md", thread_status)
    write_report("FORMAT_RENDER_QA_20260524.md", format_qa)
    write_report("GOVERNOR_RECOVERY_REPORT_20260524.md", governor)
    write_report("CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md", confucius)


if __name__ == "__main__":
    main()
