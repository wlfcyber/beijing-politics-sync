# Claude External Review Packet V3

Status: `prepared_not_submitted`

This packet is for the next real Claude review after Claude V2 NOT_PASS and the post-V2 local patches.

## Read

1. `PROGRESS.md`
2. `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V2.md`
3. `06_claude_review/EXTERNAL_REVIEW_STATUS.md`
4. `04_fusion/PROMOTION_QUALITY_CHECK.md`
5. `04_fusion/PROMOTION_LOG.md`
6. `01_source_inventory/COVERAGE_GAP.csv`
7. `04_fusion/THINKING_BAODIAN_V2_BODY_DRAFT.md`
8. `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md`
9. `02_codex_lane/MAIN_THINKING_LEDGER.csv`
10. `02_codex_lane/REASONING_FORM_LEDGER.csv`
11. `02_codex_lane/CHOICE_TRAP_LEDGER.csv`

## Review Focus

Check only the delta after Claude V2:

1. Q0026 甲: Does the new wording correctly respect the source fact that the rubric lists parallel usable reasons rather than a main/sub chain?
2. Q0020: Is the independent material-action paragraph enough?
3. Promotion quality: Did removing undefined `partial-plus` fix the gate ambiguity?
4. V2 body usage entries/cross-refs: are they useful or still noisy?
5. Coverage gap priority columns: do they make the next work executable?

## Output Format

Write result as `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V3.md` with:

- Verdict.
- Delta fixed.
- Remaining P0/P1 findings.
- Gate audit.
- Required next patches.
- Forbidden claims.

Do not mark final pass.
