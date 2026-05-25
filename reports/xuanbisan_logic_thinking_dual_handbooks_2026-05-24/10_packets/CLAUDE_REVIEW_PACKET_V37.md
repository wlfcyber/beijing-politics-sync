# Claude External Review Packet V37

Status: `prepared_not_submitted_gptpro_first`

This packet supersedes V36. The intended order is GPT Pro V39 first, then Claude V37, unless the user explicitly waives that order.

## Read

1. `PROGRESS.md`
2. `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V3.md`
3. `06_claude_review/EXTERNAL_REVIEW_STATUS.md`
4. `04_fusion/PROMOTION_QUALITY_CHECK.md`
5. `04_fusion/PROMOTION_LOG.md`
6. `01_source_inventory/COVERAGE_GAP.csv`
7. `04_fusion/THINKING_BAODIAN_V2_BODY_DRAFT.md`
8. `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md`
9. `02_codex_lane/REASONING_FORM_LEDGER.csv`
10. `02_codex_lane/CHOICE_TRAP_LEDGER.csv`
11. `02_codex_lane/GAP006_2024_XICHENG_YIMO_Q11_Q12_Q13_SOURCE_LOCK.md`
12. `02_codex_lane/GAP006_2024_CHAOYANG_YIMO_Q7_SOURCE_LOCK.md`

## Review Focus

Check only the delta after Claude V3, with special attention to Q0076-Q0079:

- Q0076 2024西城一模 Q11 as a reasoning choice row on bounded enumeration and same-object substitution.
- Q0077 2024西城一模 Q12 as a thinking choice row on肯定/否定关系.
- Q0078 2024西城一模 Q13 as a thinking choice row on联想思维非逻辑制约的畅想性.
- Q0079 2024朝阳一模 Q7 as a thinking choice row on创新思维跨越性、逻辑推导 and继承借鉴.
- Whether Q0076-Q0079 are supported by the cited original papers and official answer keys.
- Whether the gate files still prevent release claims.
- Whether 门头沟/房山 choice candidates are correctly left as unresolved because raw paper/answer evidence was not recovered.

## Output Format

Write result as `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V37.md` with:

- Verdict.
- Delta fixed.
- Remaining P0/P1 findings.
- Gate audit.
- Required next patches.
- Forbidden claims.

Do not mark final pass.
