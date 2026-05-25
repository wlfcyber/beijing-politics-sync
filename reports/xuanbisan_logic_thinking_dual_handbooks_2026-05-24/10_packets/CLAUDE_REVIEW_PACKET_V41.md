# Claude External Review Packet V41

Status: `prepared_not_submitted_gptpro_first`

This packet supersedes V40. The intended order is GPT Pro V43 first, then Claude V41, unless the user explicitly waives that order.

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
12. `02_codex_lane/GAP006_2024_CHAOYANG_ERMO_Q19_SOURCE_LOCK.md`
13. `01_source_inventory/GAP006_2024_UNRESOLVED_CANDIDATES.md`
14. `04_fusion/BLOCKER_RECONCILIATION.md`

## Review Focus

Check only the delta after Claude V3, with special attention to Q0084-Q0085:

- Q0084 2024朝阳二模 Q19(1) as an A-formal dual-registration row:辩证思维动态性 plus类比推理.
- Whether the material-action -> total hat -> small method -> trigger logic -> answer sentence chain is aligned with the formal rubric for Q0084.
- Whether Q0084 should appear in both the thinking body and reasoning body, or whether either placement creates overclaim risk.
- Q0085 2024朝阳二模 Q19(2) as an A-formal reasoning row on联言判断 and真值条件.
- Whether Q0085 is correctly excluded from the thinking-method main chain.
- Whether 2024门头沟/房山 choice candidates are correctly withheld as unresolved rather than promoted from classification cache alone.
- Whether the gate files still prevent release claims.

## Output Format

Write result as `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V41.md` with:

- Verdict.
- Delta fixed.
- Remaining P0/P1 findings.
- Gate audit.
- Required next patches.
- Forbidden claims.

Do not mark final pass.
