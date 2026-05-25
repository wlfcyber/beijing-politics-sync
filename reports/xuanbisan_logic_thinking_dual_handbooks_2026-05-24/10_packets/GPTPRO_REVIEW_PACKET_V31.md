# GPT Pro Review Packet V31

Status: `prepared_not_submitted`

This packet supersedes V30. Chrome submission is still blocked, so no real GPT Pro review has been captured. V31 adds the GAP006 source-lock decision for 2024西城二模 Q18(1), creating Q0063 as a formal scientific-induction reasoning row.

## Read

1. `PROGRESS.md`
2. `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V3.md`
3. `06_claude_review/EXTERNAL_REVIEW_STATUS.md`
4. `05_gptpro_review/EXTERNAL_REVIEW_STATUS.md`
5. `04_fusion/PROMOTION_QUALITY_CHECK.md`
6. `04_fusion/PROMOTION_LOG.md`
7. `01_source_inventory/COVERAGE_GAP.csv`
8. `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md`
9. `02_codex_lane/REASONING_FORM_LEDGER.csv`
10. `02_codex_lane/GAP006_2024_XICHENG_ERMO_Q18_1_SOURCE_LOCK.md`
11. `04_fusion/BLOCKER_RECONCILIATION.md`

## New Delta

- GAP006 now also has Q0063 from 2024西城二模 Q18(1). Q0063 is an A-formal scientific-induction / incomplete-induction reasoning row.
- Formal docx rubric requires both the reasoning type and the cause-finding method, including共变法、求异法、求同法, or valid combined methods.
- Q0063 is entered in `REASONING_FORM_LEDGER.csv` as RF0041 and in the reasoning V2 body draft.
- `PROMOTION_QUALITY_CHECK.md` still holds all rows because Claude V3 is NOT_PASS and GPT Pro is pending.

## Required Review

Check whether the current state is ready for a next Claude review, not final release.

Return:

- Verdict: `not_final / conditionally_ready_for_claude_review / reject`.
- P0 findings.
- P1 findings.
- Gate audit.
- Coverage priorities.
- Whether Q0063 correctly teaches the difference between the induction type and the cause-finding method.
- Forbidden claims.

Do not mark PASS.
