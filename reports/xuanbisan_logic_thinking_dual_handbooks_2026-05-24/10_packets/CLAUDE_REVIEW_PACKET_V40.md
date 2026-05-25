# Claude External Review Packet V40

Status: `prepared_not_submitted_gptpro_first`

This packet supersedes V39. The intended order is GPT Pro V42 first, then Claude V40, unless the user explicitly waives that order.

## Read

1. `PROGRESS.md`
2. `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V3.md`
3. `06_claude_review/EXTERNAL_REVIEW_STATUS.md`
4. `04_fusion/PROMOTION_QUALITY_CHECK.md`
5. `04_fusion/PROMOTION_LOG.md`
6. `01_source_inventory/COVERAGE_GAP.csv`
7. `04_fusion/THINKING_BAODIAN_V2_BODY_DRAFT.md`
8. `02_codex_lane/MAIN_THINKING_LEDGER.csv`
9. `02_codex_lane/GAP006_2024_HAIDIAN_YIMO_Q17_2_SOURCE_LOCK.md`
10. `01_source_inventory/GAP006_2024_UNRESOLVED_CANDIDATES.md`

## Review Focus

Check only the delta after Claude V3, with special attention to Q0083:

- Q0083 2024海淀一模 Q17(2) as an A-formal thinking main-question row on analysis and synthesis.
- Whether the material-action -> total hat -> small method -> trigger logic -> answer sentence chain is aligned with the formal rubric.
- Whether 2024门头沟/房山 choice candidates are correctly withheld as unresolved rather than promoted from classification cache alone.
- Whether the gate files still prevent release claims.

## Output Format

Write result as `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V40.md` with:

- Verdict.
- Delta fixed.
- Remaining P0/P1 findings.
- Gate audit.
- Required next patches.
- Forbidden claims.

Do not mark final pass.
