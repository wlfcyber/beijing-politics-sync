# Claude External Review Packet V33

Status: `prepared_not_submitted_gptpro_first`

This packet supersedes V32. The intended order is GPT Pro V35 first, then Claude V33, unless the user explicitly waives that order.

## Read

1. `PROGRESS.md`
2. `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V3.md`
3. `06_claude_review/EXTERNAL_REVIEW_STATUS.md`
4. `04_fusion/PROMOTION_QUALITY_CHECK.md`
5. `04_fusion/PROMOTION_LOG.md`
6. `01_source_inventory/COVERAGE_GAP.csv`
7. `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md`
8. `02_codex_lane/REASONING_FORM_LEDGER.csv`
9. `02_codex_lane/GAP006_2024_XICHENG_YIMO_Q19_2_Q19_3_SOURCE_LOCK.md`

## Review Focus

Check only the delta after Claude V3, with special attention to Q0067-Q0068:

- Q0067 2024西城一模 Q19(2) as a definition-components row.
- Q0068 2024西城一模 Q19(3) as a concept-extension relation row.
- Whether the student-facing explanation distinguishes definition structure from extension relation.
- Whether the gate files still prevent release claims.

## Output Format

Write result as `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V33.md` with:

- Verdict.
- Delta fixed.
- Remaining P0/P1 findings.
- Gate audit.
- Required next patches.
- Forbidden claims.

Do not mark final pass.
