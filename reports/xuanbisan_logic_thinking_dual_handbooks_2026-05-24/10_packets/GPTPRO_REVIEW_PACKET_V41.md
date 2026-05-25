# GPT Pro Review Packet V41

Status: `prepared_not_submitted`

This packet supersedes V40. Chrome submission is still blocked, so no real GPT Pro review has been captured. V41 adds the GAP006 source-lock decision for 2024海淀一模 Q6-Q7, creating Q0081-Q0082 as official-answer-key choice rows.

## Read

1. `PROGRESS.md`
2. `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V3.md`
3. `06_claude_review/EXTERNAL_REVIEW_STATUS.md`
4. `05_gptpro_review/EXTERNAL_REVIEW_STATUS.md`
5. `04_fusion/PROMOTION_QUALITY_CHECK.md`
6. `04_fusion/PROMOTION_LOG.md`
7. `01_source_inventory/COVERAGE_GAP.csv`
8. `04_fusion/THINKING_BAODIAN_V2_BODY_DRAFT.md`
9. `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md`
10. `02_codex_lane/REASONING_FORM_LEDGER.csv`
11. `02_codex_lane/CHOICE_TRAP_LEDGER.csv`
12. `02_codex_lane/GAP006_2024_HAIDIAN_YIMO_Q6_Q7_SOURCE_LOCK.md`
13. `04_fusion/BLOCKER_RECONCILIATION.md`

## New Delta

- GAP006 now also has Q0081-Q0082 from 2024海淀一模 Q6-Q7.
- Q0081 is a reasoning choice row with thinking cross-registration:选言推理 plus逆向思维; official answer key says B.
- Q0082 is a reasoning choice row on联言判断 type recognition: “不是P而是Q” equals “非P并且Q”; official answer key says C.
- `PROMOTION_QUALITY_CHECK.md` still holds all rows because Claude V3 is NOT_PASS and GPT Pro is pending.

## Required Review

Check whether the current state is ready for a next Claude review, not final release.

Return:

- Verdict: `not_final / conditionally_ready_for_claude_review / reject`.
- P0 findings.
- P1 findings.
- Gate audit.
- Coverage priorities.
- Whether Q0081 is correctly cross-registered rather than forced into only reasoning or only thinking.
- Whether Q0082 correctly identifies “不是P而是Q” as a联言判断.
- Whether the unresolved raw-source gaps for 门头沟/房山 candidates are still accurately held.
- Forbidden claims.

Do not mark PASS.
