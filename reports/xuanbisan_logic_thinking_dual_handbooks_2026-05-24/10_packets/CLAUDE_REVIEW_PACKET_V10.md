# Claude External Review Packet V10

Status: `prepared_not_submitted_gptpro_first`

This packet supersedes V9. The intended order is GPT Pro V12 first, then Claude V10, unless the user explicitly waives that order.

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
13. `02_codex_lane/GAP002_2026_HAIDIAN_Q17_QUESTIONNAIRE_SOURCE_LOCK.md`
14. `02_codex_lane/GAP001_2024_CHAOYANG_ERMO_Q7_SOURCE_LOCK.md`
15. `02_codex_lane/GAP007_2024_BEIJING_GAOKAO_Q19_2_SOURCE_AUDIT.md`
16. `02_codex_lane/GAP003_2026_SHUNYI_YIMO_CHOICE_CORPUS_SOURCE_LOCK.md`
17. `02_codex_lane/GAP004_2026_CHAOYANG_YIMO_CHOICE_CORPUS_SOURCE_LOCK.md`
18. `02_codex_lane/GAP005_2025_MENTOUGOU_YIMO_Q21_1_SOURCE_LOCK.md`

## Review Focus

Check only the delta after Claude V3:

1. Q0026 provenance/rubric-source patches.
2. Ledger `rubric_source` additions and Q0004/Q0017 main-thinking additions.
3. Q0019 “迁移或想象” consistency.
4. Q0020 question-specific answer sentence.
5. GAP008 source-lock quality: Q0027 valid 不相容选言推理 and Q0028 invalid-trap sample.
6. GAP002 source-lock quality: Q0022 full questionnaire detail from 2026海淀一模 page 5 and its fit with “划分标准不一 / 选言判断遗漏”.
7. GAP001 source-lock quality: Q0029 2024朝阳二模 Q7 answer D and A-option 小项不当扩大 classification.
8. GAP007 audit quality: Q0030 must remain blocked because only a scoring-reference signal exists; the original 2024北京高考 青海防沙治沙 question is not locked and a checked public PDF mismatches.
9. GAP003 source-lock quality: Q1-Q15 full classification, Q0031-Q0034/Q0036 choice-trap rows, and Q0035 answer-key conflict handling.
10. GAP004 source-lock quality: Q1-Q15 full classification, Q0037-Q0040 choice-trap rows, and Q0039 teacher-key versus old-index conflict handling.
11. GAP005/GAP009 source-lock quality: Q0041 2025门头沟一模 Q21(1) as a formal composite thinking row under a scientific-thinking prompt; check whether the辩证、创新、科学 split is source-grounded and whether the V2 body entry avoids release claims.
12. Whether the gate files still prevent release claims.

## Output Format

Write result as `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V10.md` with:

- Verdict.
- Delta fixed.
- Remaining P0/P1 findings.
- Gate audit.
- Required next patches.
- Forbidden claims.

Do not mark final pass.
