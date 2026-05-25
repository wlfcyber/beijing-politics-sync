# Claude External Review Packet V4

Status: `prepared_not_submitted_gptpro_first`

This packet is for the next real Claude review after Claude V3 NOT_PASS and post-V3 local patches, including GAP008 source-lock. The intended order is GPT Pro V6 first, then Claude V4, unless the user explicitly waives that order.

## Read

1. `PROGRESS.md`
2. `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V3.md`
3. `06_claude_review/EXTERNAL_REVIEW_STATUS.md`
4. `04_fusion/PROMOTION_QUALITY_CHECK.md`
5. `04_fusion/PROMOTION_LOG.md`
6. `01_source_inventory/COVERAGE_GAP.csv`
7. `04_fusion/THINKING_BAODIAN_V2_BODY_DRAFT.md`
8. `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md`
9. `02_codex_lane/MAIN_THINKING_LEDGER.csv`
10. `02_codex_lane/REASONING_FORM_LEDGER.csv`
11. `02_codex_lane/CHOICE_TRAP_LEDGER.csv`
12. `02_codex_lane/GAP008_DISJUNCTIVE_REASONING_SOURCE_LOCK.md`

## Review Focus

Check only the delta after Claude V3:

1. Q0026 provenance/rubric-source patches.
2. Ledger `rubric_source` additions and Q0004/Q0017 main-thinking additions.
3. Q0019 “迁移或想象” consistency.
4. Q0020 question-specific answer sentence.
5. GAP008 source-lock quality: Q0027 valid 不相容选言推理 and Q0028 invalid-trap sample.
6. Whether the gate files still prevent release claims.

## Output Format

Write result as `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V4.md` with:

- Verdict.
- Delta fixed.
- Remaining P0/P1 findings.
- Gate audit.
- Required next patches.
- Forbidden claims.

Do not mark final pass.
