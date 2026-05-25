# GPT Pro Review Packet V10

Status: `prepared_not_submitted`

This packet supersedes V9. Chrome submission is still blocked, so no real GPT Pro review has been captured. V10 adds the GAP003 source-lock decision for 2026顺义一模 Q1-Q15 choice-question corpus.

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
12. `02_codex_lane/CHOICE_TRAP_LEDGER.csv`
13. `02_codex_lane/GAP008_DISJUNCTIVE_REASONING_SOURCE_LOCK.md`
14. `02_codex_lane/GAP002_2026_HAIDIAN_Q17_QUESTIONNAIRE_SOURCE_LOCK.md`
15. `02_codex_lane/GAP001_2024_CHAOYANG_ERMO_Q7_SOURCE_LOCK.md`
16. `02_codex_lane/GAP007_2024_BEIJING_GAOKAO_Q19_2_SOURCE_AUDIT.md`
17. `02_codex_lane/GAP003_2026_SHUNYI_YIMO_CHOICE_CORPUS_SOURCE_LOCK.md`
18. `03_claudecode_lane/suite_reports/2026顺义一模.md`
19. `04_fusion/BLOCKER_RECONCILIATION.md`

## Post-Claude-V3 Patches To Check

- Q0026 甲 “材料分析” third reason was verified directly against 2026西城一模细则 line 75 and synced to the backcheck and suite report.
- MAIN/REASONING ledgers now have `rubric_source`.
- Q0004/Q0017 have main-thinking ledger entries.
- Q0019 wording is unified as “迁移或想象”.
- Q0020 has a question-specific answer sentence.
- GAP008 now has Q0027/Q0028 source-lock coverage: Q0027 is an A-formal valid 不相容选言推理 sample; Q0028 is a B-choice-signal invalid-trap sample.
- GAP002 now has Q0022 full questionnaire detail source-locked from rendered paper page 5.
- GAP001 now has Q0029 source-locked from 2024朝阳二模 paper and reference answer key: Q7 answer D, with A as the 三段论小项不当扩大 trap.
- GAP007 now has Q0030 as a missing/audit row only: the scoring-reference signal exists in 2026丰台期末细则, but the original 2024北京高考 青海防沙治沙 question is not locked and a checked public 2024北京卷 PDF mismatches.
- GAP003 now has Q1-Q15 fully classified from 2026顺义一模 paper and formal answer key. Q0031-Q0034/Q0036 are local choice-trap/source-lock rows; Q0035 is held as an answer-conflict row because the official key says A but the old wrong-option library marked A wrong.
- `PROMOTION_QUALITY_CHECK.md` still holds all rows because Claude V3 is NOT_PASS and GPT Pro is pending.

## Required Review

Check whether the current state is ready for a next Claude review, not final release.

Return:

- Verdict: `not_final / conditionally_ready_for_claude_review / reject`.
- P0 findings.
- P1 findings.
- Gate audit.
- Coverage priorities.
- Whether GAP001, GAP002, GAP003, and GAP008 can be treated as `source_locked_pending_external_review` or must remain `open`.
- Whether Q0035 should remain conflict-held, be accepted under the official answer key, or be removed pending manual review.
- Whether GAP007 is correctly held as `source_identified_original_question_not_locked` and excluded from the student-facing body.
- Forbidden claims.

Do not mark PASS.
