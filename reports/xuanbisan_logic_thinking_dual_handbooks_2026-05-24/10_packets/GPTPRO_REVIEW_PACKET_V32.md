# GPT Pro Review Packet V32

Status: `prepared_not_submitted`

This packet supersedes V31. Chrome submission is still blocked, so no real GPT Pro review has been captured. V32 adds the GAP006 source-lock decision for 2024海淀一模 Q18(2), creating Q0064 as a formal incomplete-induction reliability row.

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
10. `02_codex_lane/GAP006_2024_HAIDIAN_YIMO_Q18_2_SOURCE_LOCK.md`
11. `04_fusion/BLOCKER_RECONCILIATION.md`

## New Delta

- GAP006 now also has Q0064 from 2024海淀一模 Q18(2). Q0064 is an A-formal incomplete-induction reliability row.
- Formal docx rubric requires `不完全归纳推理` and the two reliability upgrades: broader investigated objects and causal analysis, with求同法、求异法、共变法 as acceptable concrete cause-finding methods.
- Q0064 is entered in `REASONING_FORM_LEDGER.csv` as RF0042 and in the reasoning V2 body draft.
- `PROMOTION_QUALITY_CHECK.md` still holds all rows because Claude V3 is NOT_PASS and GPT Pro is pending.

## Required Review

Check whether the current state is ready for a next Claude review, not final release.

Return:

- Verdict: `not_final / conditionally_ready_for_claude_review / reject`.
- P0 findings.
- P1 findings.
- Gate audit.
- Coverage priorities.
- Whether Q0064 is correctly grouped with Q0053/Q0063 while preserving its narrower `样本 + 因果` reliability teaching point.
- Forbidden claims.

Do not mark PASS.
