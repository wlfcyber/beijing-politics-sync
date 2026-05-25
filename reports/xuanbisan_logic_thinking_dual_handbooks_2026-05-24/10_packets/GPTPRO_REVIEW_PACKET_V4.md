# GPT Pro Review Packet V4

Status: `prepared_not_submitted`

This packet supersedes V3. Claude V2 returned NOT_PASS, then Codex applied post-review local patches. This packet is for the first real GPT Pro review of the current state; it must not be counted as submitted until a user-visible or explicitly accepted GPT Pro run returns a real result.

## Read First

Run directory:

`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_逻辑与思维_双宝典双线重启_2026-05-24`

Read:

1. `PROGRESS.md`
2. `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V2.md`
3. `06_claude_review/EXTERNAL_REVIEW_STATUS.md`
4. `04_fusion/PROMOTION_QUALITY_CHECK.md`
5. `04_fusion/PROMOTION_LOG.md`
6. `01_source_inventory/COVERAGE_GAP.csv`
7. `04_fusion/THINKING_BAODIAN_V2_BODY_DRAFT.md`
8. `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md`
9. `02_codex_lane/MAIN_THINKING_LEDGER.csv`
10. `02_codex_lane/REASONING_FORM_LEDGER.csv`
11. `02_codex_lane/CHOICE_TRAP_LEDGER.csv`

## Post-Claude-V2 Patches To Check

- Q0026 甲 was rechecked against 2026西城一模细则 lines 73-77. The source does not provide a主链/次链; it lists 四概念错误 / 前提不真 / 材料分析 as parallel usable reasons. The drafts now say not to invent a主次链 and recommend a combined answer.
- Q0020 now has an independent material-action paragraph based on the original paper page: 全民阅读设施管理单位 -> 应提供适老内容/便利服务; 某实体书店提供这些服务; therefore it is a facility-management unit. It remains a sufficient-condition肯后错误.
- `PROMOTION_QUALITY_CHECK.md` removed undefined `partial-plus` and keeps all rows at `partial` + `hold`.
- V2 body drafts now include use instructions and cross-refs.
- `COVERAGE_GAP.csv` now has priority/owner/milestone columns.

## Required Review

Act as strict GPT Pro chief reviewer. Do not praise. Find defects.

Check:

1. Did the Q0026 甲 patch correctly follow the actual source, or should the answer still be rewritten differently?
2. Does Q0020 now contain enough material detail to be student-usable?
3. Are the thinking and reasoning V2 body drafts safe enough for a next Claude V3 review, even though they are not final?
4. Does the quality gate now avoid false release signals?
5. Which coverage gaps must be handled before any final handbook claim?
6. What claims remain forbidden?

## Output Format

Return:

- Verdict: `not_final / conditionally_usable_after_fixes / reject`.
- P0 findings.
- P1 findings.
- Gate audit.
- Coverage priorities.
- Forbidden final claims.

Do not mark PASS.
