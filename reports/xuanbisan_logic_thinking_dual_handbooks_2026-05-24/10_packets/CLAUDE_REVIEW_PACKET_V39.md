# Claude External Review Packet V39

Status: `prepared_not_submitted_gptpro_first`

This packet supersedes V38. The intended order is GPT Pro V41 first, then Claude V39, unless the user explicitly waives that order.

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
11. `02_codex_lane/GAP006_2024_HAIDIAN_YIMO_Q6_Q7_SOURCE_LOCK.md`

## Review Focus

Check only the delta after Claude V3, with special attention to Q0081-Q0082:

- Q0081 2024海淀一模 Q6 as a reasoning choice row with thinking cross-registration:选言推理 and逆向思维.
- Q0082 2024海淀一模 Q7 as a联言判断 type-recognition row.
- Whether the prompt/answer evidence supports answer B for Q0081 and answer C for Q0082.
- Whether the gate files still prevent release claims.

## Output Format

Write result as `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V39.md` with:

- Verdict.
- Delta fixed.
- Remaining P0/P1 findings.
- Gate audit.
- Required next patches.
- Forbidden claims.

Do not mark final pass.
