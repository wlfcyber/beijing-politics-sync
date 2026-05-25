# GPT Pro Review Packet V37

Status: `prepared_not_submitted`

This packet supersedes V36. Chrome submission is still blocked, so no real GPT Pro review has been captured. V37 adds the GAP006 source-lock decision for 2024东城一模 Q6-Q8, creating Q0071-Q0073 as reasoning choice rows.

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
10. `02_codex_lane/CHOICE_TRAP_LEDGER.csv`
11. `02_codex_lane/GAP006_2024_DONGCHENG_YIMO_Q6_Q7_Q8_SOURCE_LOCK.md`
12. `04_fusion/BLOCKER_RECONCILIATION.md`

## New Delta

- GAP006 now also has Q0071-Q0073 from 2024东城一模 Q6-Q8.
- Q0071 is an A-formal logic-rule comprehensive choice row; official answer D.
- Q0072 is an A-formal syllogism validity vs premise-truth row; official answer A.
- Q0073 is an A-formal compound hypothetical/disjunctive reasoning chain row; official answer D.
- Q0071-Q0073 are entered in `REASONING_FORM_LEDGER.csv` as RF0045-RF0047, in `CHOICE_TRAP_LEDGER.csv` as CT0017-CT0019, and in the reasoning V2 body draft.
- `PROMOTION_QUALITY_CHECK.md` still holds all rows because Claude V3 is NOT_PASS and GPT Pro is pending.

## Required Review

Check whether the current state is ready for a next Claude review, not final release.

Return:

- Verdict: `not_final / conditionally_ready_for_claude_review / reject`.
- P0 findings.
- P1 findings.
- Gate audit.
- Coverage priorities.
- Whether Q0071-Q0073 are correctly kept in the reasoning/choice handbook rather than the thinking-trigger handbook.
- Whether Q0072 correctly distinguishes valid form from true conclusion.
- Whether Q0073's inference chain is valid.
- Forbidden claims.

Do not mark PASS.
