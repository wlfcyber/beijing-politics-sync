# Claude External Review Packet V42

Status: `prepared_not_submitted_gptpro_first`

This packet supersedes V41. The intended order is GPT Pro V44 first, then Claude V42, unless the user explicitly waives that order.

## Read

1. `PROGRESS.md`
2. `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V3.md`
3. `06_claude_review/EXTERNAL_REVIEW_STATUS.md`
4. `04_fusion/PROMOTION_QUALITY_CHECK.md`
5. `04_fusion/PROMOTION_LOG.md`
6. `04_fusion/PROMOTION_HOLD.md`
7. `01_source_inventory/COVERAGE_GAP.csv`
8. `04_fusion/THINKING_BAODIAN_V2_BODY_DRAFT.md`
9. `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md`
10. `02_codex_lane/MAIN_THINKING_LEDGER.csv`
11. `02_codex_lane/REASONING_FORM_LEDGER.csv`
12. `02_codex_lane/CHOICE_TRAP_LEDGER.csv`
13. `02_codex_lane/GAP006_2024_SHUNYI_ERMO_Q3_Q5_Q6_Q7_SOURCE_LOCK.md`
14. `01_source_inventory/GAP006_2024_UNRESOLVED_CANDIDATES.md`
15. `04_fusion/BLOCKER_RECONCILIATION.md`

## Review Focus

Check only the delta after Claude V3, with special attention to Q0086-Q0089:

- Q0086 2024顺义二模 Q3 as a B-choice-signal thinking row, not a full主观题 trigger chain.
- Q0087 2024顺义二模 Q5 as a thinking trap row only, because the correct answer is not a logic-and-thinking option.
- Q0088 2024顺义二模 Q6 as an A-formal reasoning choice row on复合判断.
- Q0089 2024顺义二模 Q7 as an A-formal reasoning choice row on必要条件假言判断.
- Whether Q0086/Q0087 placement is too strong, too weak, or right for a choice-signal/trap layer.
- Whether the gate files still prevent release claims.

## Output Format

Write result as `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V42.md` with:

- Verdict.
- Delta fixed.
- Remaining P0/P1 findings.
- Gate audit.
- Required next patches.
- Forbidden claims.

Do not mark final pass.
