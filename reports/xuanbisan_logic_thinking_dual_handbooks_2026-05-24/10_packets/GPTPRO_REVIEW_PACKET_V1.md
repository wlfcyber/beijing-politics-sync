# GPT Pro Review Packet V1

Status: `prepared_not_submitted`

This packet supersedes V0 because Codex A line has expanded from 17 to 26 source-locked rows and corrected Claude V0 F1.

## Review Target

Run directory:

`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_逻辑与思维_双宝典双线重启_2026-05-24`

Read in this order:

1. `TASK_BRIEF.md`
2. `PROGRESS.md`
3. `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V0.md`
4. `04_fusion/BLOCKER_RECONCILIATION.md`
5. `04_fusion/PROMOTION_GATE.md`
6. `04_fusion/PROMOTION_LOG.md`
7. `04_fusion/PROMOTION_HOLD.md`
8. `04_fusion/A_B_DIFF_SNAPSHOT.md`
9. `04_fusion/THINKING_BAODIAN_REVIEW_DRAFT.md`
10. `04_fusion/REASONING_BAODIAN_REVIEW_DRAFT.md`

Then spot-check evidence:

- `01_source_inventory/QUESTION_COVERAGE_MATRIX.csv`
- `02_codex_lane/HARD_SAMPLE_SOURCE_PACKETS.md`
- `02_codex_lane/FAMILY_SOURCE_PACKETS_Q0006_Q0012.md`
- `02_codex_lane/B_ADDITIONS_BACKCHECK_Q0013_Q0017.md`
- `02_codex_lane/B_ADDITIONS_BACKCHECK_Q0018_Q0026.md`
- `02_codex_lane/MAIN_THINKING_LEDGER.csv`
- `02_codex_lane/REASONING_FORM_LEDGER.csv`
- `02_codex_lane/CHOICE_TRAP_LEDGER.csv`

## What Changed Since V0

- Q0011 was corrected from 科学思维单角度 to 科学思维总帽下三模块复合：科学2分 + 创新3分 + 辩证2分.
- B-line high-confidence rows named by Claude V0 were A-line source-locked as Q0018-Q0026.
- Promotion gate, promotion hold, promotion log, and blocker reconciliation files were added.
- Claude V0 remains `NOT_PASS`; V1 must not treat it as a pass.

## Required Review

Act as strict GPT Pro chief reviewer. Do not praise. Find defects and coverage gaps.

Check:

1. Is Q0011 now correctly routed after the official rubric split?
2. Are Q0018-Q0026 source-locked and correctly assigned between 思维宝典 and 推理宝典?
3. Is the promotion gate strict enough to prevent provisional rows entering final materials?
4. Which rows in `PROMOTION_HOLD.md` are highest priority to clear before a usable V1?
5. Are there new routing errors, especially formal-logic rows accidentally entering 思维主链?
6. What 2024-2026 suites/questions remain most urgent for full exhaustion?

## Output Format

Return:

- Verdict: `not_final / conditionally_usable_after_fixes / reject`.
- P0 findings: must fix before any V1 external review claim.
- P1 findings: must fix before Word/PDF.
- Coverage gaps by suite/question.
- Gate audit: rows incorrectly promoted or incorrectly held.
- Final claim audit: forbidden claims.

Do not mark PASS.
