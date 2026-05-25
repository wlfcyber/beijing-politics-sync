# Claude External Review Packet V47

Status: `prepared_not_submitted_gptpro_first`

This packet supersedes V46. The intended order is GPT Pro V49 first, then Claude V47, unless the user explicitly waives that order.

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
13. `02_codex_lane/GAP006_2024_HAIDIAN_ERMO_Q5_Q6_SOURCE_LOCK.md`
14. `02_codex_lane/GAP011_2026_MENTOUGOU_YIMO_Q5_Q6_Q18_2_SOURCE_LOCK.md`
15. `02_codex_lane/GAP006_2024_HAIDIAN_ERMO_Q17_2_SOURCE_LOCK.md`
16. `02_codex_lane/GAP011_2026_MENTOUGOU_YIMO_Q7_SOURCE_LOCK.md`
17. `04_fusion/BLOCKER_RECONCILIATION.md`

## Review Focus

Check only the delta after Claude V3, with special attention to Q0093-Q0099:

- Q0093 2024海淀二模 Q5 as求异法 reasoning choice row.
- Q0094 2024海淀二模 Q6 as概念属性 and换位推理边界 reasoning row.
- Q0095 2026门头沟一模 Q5 as `B-choice-signal`, not a full main-question chain.
- Q0096 2026门头沟一模 Q6 as类比推理 plus换位/换质 reasoning row.
- Q0097 2026门头沟一模 Q18(2) as a formal thinking main row with辩证思维 and创新思维 trigger chains.
- Q0098 2024海淀二模 Q17(2) as a separate formal main row on感性具体, 思维抽象, and思维具体.
- Q0099 2026门头沟一模 Q7 as a `B-choice-signal` mixed-boundary row: ① is必修四实践第一观点, ④ is辩证思维整体性, ②/③ are terminology traps.
- Whether all gate files still prevent final/pass/release claims.

## Output Format

Write result as `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V47.md` with:

- Verdict.
- Delta fixed.
- Remaining P0/P1 findings.
- Gate audit.
- Required next patches.
- Forbidden claims.

Do not mark final pass.
