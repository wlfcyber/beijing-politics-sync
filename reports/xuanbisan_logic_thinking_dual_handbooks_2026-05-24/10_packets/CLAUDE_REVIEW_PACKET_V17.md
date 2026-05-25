# Claude External Review Packet V17

Status: `prepared_not_submitted_gptpro_first`

This packet supersedes V16. The intended order is GPT Pro V19 first, then Claude V17, unless the user explicitly waives that order.

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
19. `02_codex_lane/GAP005_2025_FANGSHAN_YIMO_Q16_2_Q16_3_SOURCE_LOCK.md`
20. `02_codex_lane/GAP005_2025_DONGCHENG_QIMO_Q18_2_SOURCE_LOCK.md`
21. `02_codex_lane/GAP005_2025_CHANGPING_ERMO_Q19_SOURCE_LOCK.md`
22. `02_codex_lane/GAP005_2025_XICHENG_YIMO_Q17_SOURCE_LOCK.md`
23. `02_codex_lane/GAP005_2025_SHIJINGSHAN_YIMO_Q19_SOURCE_LOCK.md`
24. `02_codex_lane/GAP005_2025_FENGTAI_YIMO_Q18_1_SOURCE_LOCK.md`
25. `02_codex_lane/GAP005_2025_CHAOYANG_QIMO_Q19_SOURCE_LOCK.md`

## Review Focus

Check only the delta after Claude V3, with special attention to Q0049:

- Q0049 2025朝阳期末 Q19 as a formal reasoning row.
- Whether the rendered formal rubric evidence is adequate for `A-formal`, with the PPT used only as support.
- Whether RF0033-RF0035 correctly separate排中律、矛盾律、三段论有效结构.
- Whether the reasoning V2 body entry teaches the checking order rather than reducing the题 to generic逻辑错误.
- Whether the gate files still prevent release claims.

## Output Format

Write result as `06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V17.md` with:

- Verdict.
- Delta fixed.
- Remaining P0/P1 findings.
- Gate audit.
- Required next patches.
- Forbidden claims.

Do not mark final pass.
