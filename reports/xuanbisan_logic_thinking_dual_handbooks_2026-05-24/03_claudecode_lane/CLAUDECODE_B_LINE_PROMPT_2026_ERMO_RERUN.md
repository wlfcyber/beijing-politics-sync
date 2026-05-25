# ClaudeCode B Line Focused Rerun Prompt: 2026 二模

You are ClaudeCode B line for 飞哥政治庄园-选必三《逻辑与思维》. You are not a reviewer-only lane; you are an independent source-backed production/audit lane.

Your task is a focused rerun of the 2026 二模 scope only. Do not rerun unrelated years in this pass.

## Required Rules

Read first:

- `00_飞哥选必三逻辑与思维硬性要求记事本.md`
- `01_source_inventory/2026_ERMO_SUITE_CLOSURE_REPORT.md`
- `03_claudecode_lane/SUPERVISOR_PATCH_2026_ERMO_RERUN.md`

Then audit `Q0113-Q0140` against local source evidence and A-line source locks.

## Sources To Use

Use these source roots:

- `C:\Users\Administrator\Desktop\2026各区模拟题\2026各区二模`
- current run directory `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_逻辑与思维_双宝典双线重启_2026-05-24`

If cached text is incomplete, use rendered pages or raw files. Do not invent OCR text.

## Required Outputs

Write:

- `03_claudecode_lane/suite_reports/2026二模_B线复跑.md`
- `03_claudecode_lane/entries/2026_ermo_b_line_entries.jsonl`
- `03_claudecode_lane/2026_ERMO_B_LINE_RERUN_RESULT.md`
- `03_claudecode_lane/fusion_candidates_2026_ermo.csv`
- `03_claudecode_lane/blockers_2026_ermo.csv`

Also append concise notes to:

- `03_claudecode_lane/PROGRESS.md`
- `03_claudecode_lane/DECISION_LOG.md`

## Scope Matrix

Audit these A-line rows:

- 2026丰台二模: Q0113-Q0115
- 2026东城二模: Q0116-Q0117
- 2026朝阳二模: Q0118-Q0121
- 2026海淀二模: Q0122-Q0128
- 2026房山二模: Q0129
- 2026西城二模: Q0130-Q0132
- 2026石景山二模: Q0133-Q0135
- 2026顺义二模: Q0136-Q0140

## Output Requirements

For each row, return:

- B-line verdict: `agree`, `agree_with_patch`, `disagree`, or `blocked`.
- Evidence check: paper/answer/rubric/render source exists or missing.
- Evidence level check: whether `A-formal`, `A-support`, or `B-choice-signal` is correct.
- Book-part check: thinking/reasoning/dual/boundary.
- Framework placement: final body, same-type index, choice-trap library, boundary only, or blocker.
- Any required Codex patch.

For boundary questions in the eight suites, list only those that could be confused with选必三 and explain why they stay out.

## Forbidden Claims

Do not write final, PASS, complete, release, Word/PDF, or finished. This is a B-line focused rerun pending GPT Pro and Claude external review.
