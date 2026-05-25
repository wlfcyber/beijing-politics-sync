# Claude External Review Packet V30

Status: `prepared_not_submitted_gptpro_first`

This packet supersedes V29. The intended order is GPT Pro V32 first, then Claude V30, unless the user explicitly waives that order.

## Read

1. `PROGRESS.md`
2. `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V3.md`
3. `06_claude_review/EXTERNAL_REVIEW_STATUS.md`
4. `04_fusion/PROMOTION_QUALITY_CHECK.md`
5. `04_fusion/PROMOTION_LOG.md`
6. `01_source_inventory/COVERAGE_GAP.csv`
7. `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md`
8. `02_codex_lane/REASONING_FORM_LEDGER.csv`
9. `02_codex_lane/GAP006_2024_HAIDIAN_YIMO_Q18_2_SOURCE_LOCK.md`

## Review Focus

Check only the delta after Claude V3, with special attention to Q0064:

- Q0064 2024海淀一模 Q18(2) as an incomplete-induction reliability row.
- Whether the student-facing explanation clearly teaches `部分案例 -> 一般结论 -> 不完全归纳`, and then `扩大样本 + 探求因果` as the reliability upgrade.
- Whether the gate files still prevent release claims.

## Output Format

Write result as `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V30.md` with:

- Verdict.
- Delta fixed.
- Remaining P0/P1 findings.
- Gate audit.
- Required next patches.
- Forbidden claims.

Do not mark final pass.
