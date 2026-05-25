# GPT Pro Review Packet V7

Status: `prepared_not_submitted`

This packet supersedes V6. Chrome submission is still blocked, so no real GPT Pro review has been captured. V7 adds the GAP002 source-lock patch for 2026海淀一模 Q17(1) full questionnaire detail.

## Read

1. `PROGRESS.md`
2. `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V3.md`
3. `06_claude_review/EXTERNAL_REVIEW_STATUS.md`
4. `05_gptpro_review/EXTERNAL_REVIEW_STATUS.md`
5. `04_fusion/PROMOTION_QUALITY_CHECK.md`
6. `04_fusion/PROMOTION_LOG.md`
7. `01_source_inventory/COVERAGE_GAP.csv`
8. `04_fusion/THINKING_BAODIAN_V2_BODY_DRAFT.md`
9. `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md`
10. `02_codex_lane/MAIN_THINKING_LEDGER.csv`
11. `02_codex_lane/REASONING_FORM_LEDGER.csv`
12. `02_codex_lane/B_ADDITIONS_BACKCHECK_Q0018_Q0026.md`
13. `02_codex_lane/GAP008_DISJUNCTIVE_REASONING_SOURCE_LOCK.md`
14. `02_codex_lane/GAP002_2026_HAIDIAN_Q17_QUESTIONNAIRE_SOURCE_LOCK.md`
15. `03_claudecode_lane/suite_reports/2026海淀一模.md`
16. `03_claudecode_lane/suite_reports/2026西城一模.md`

## Post-Claude-V3 Patches To Check

- Q0026 甲 “材料分析” third reason was verified directly against 2026西城一模细则 line 75 and synced to the backcheck and suite report.
- MAIN/REASONING ledgers now have `rubric_source`.
- Q0004/Q0017 have main-thinking ledger entries.
- Q0019 wording is unified as “迁移或想象”.
- Q0020 has a question-specific answer sentence.
- GAP008 now has Q0027/Q0028 source-lock coverage: Q0027 is an A-formal valid 不相容选言推理 sample; Q0028 is a B-choice-signal invalid-trap sample.
- GAP002 now has full questionnaire detail source-locked from rendered paper page 5: Q17 problem 1 identity options and problem 2 facility-problem options are written into the source-lock file and reasoning body.
- `PROMOTION_QUALITY_CHECK.md` still holds all rows because Claude V3 is NOT_PASS and GPT Pro is pending.

## Required Review

Check whether the current state is ready for a next Claude V4 review, not final release.

Return:

- Verdict: `not_final / conditionally_ready_for_claude_v4 / reject`.
- P0 findings.
- P1 findings.
- Gate audit.
- Coverage priorities.
- Whether GAP002 and GAP008 can be treated as `source_locked_pending_external_review` or must remain `open`.
- Forbidden claims.

Do not mark PASS.
