# Claude External Review Packet V38

Status: `prepared_not_submitted_gptpro_first`

This packet supersedes V37. The intended order is GPT Pro V40 first, then Claude V38, unless the user explicitly waives that order.

## Read

1. `PROGRESS.md`
2. `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V3.md`
3. `06_claude_review/EXTERNAL_REVIEW_STATUS.md`
4. `04_fusion/PROMOTION_QUALITY_CHECK.md`
5. `04_fusion/PROMOTION_LOG.md`
6. `01_source_inventory/COVERAGE_GAP.csv`
7. `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md`
8. `02_codex_lane/REASONING_FORM_LEDGER.csv`
9. `02_codex_lane/CHOICE_TRAP_LEDGER.csv`
10. `02_codex_lane/GAP006_2024_FENGTAI_YIMO_Q7_SOURCE_LOCK.md`

## Review Focus

Check only the delta after Claude V3, with special attention to Q0080:

- Q0080 2024丰台一模 Q7 as an A-support reasoning choice row on affirmative-judgment predicate non-distribution.
- Whether the prompt/answer evidence supports answer C.
- Whether the explanation handles the B-option boundary carefully enough.
- Whether the source lock clearly distinguishes paper-with-answer-key support from independent objective-question rubric explanation.
- Whether the gate files still prevent release claims.

## Output Format

Write result as `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V38.md` with:

- Verdict.
- Delta fixed.
- Remaining P0/P1 findings.
- Gate audit.
- Required next patches.
- Forbidden claims.

Do not mark final pass.
