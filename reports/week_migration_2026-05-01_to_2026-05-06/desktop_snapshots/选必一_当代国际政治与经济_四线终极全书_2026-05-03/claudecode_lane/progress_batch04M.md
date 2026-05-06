# Batch04M Remaining — ClaudeCode Lane B Progress

Run: `选必一_当代国际政治与经济_四线终极全书_2026-05-03`
Lane: ClaudeCode B (independent verification)
Coverage: 15 remaining suites in Batch04M
Status: complete

## Suite-by-suite outcome

| # | Suite | In-scope Q | Tier | Atoms | Disposition |
|---|---|---|---|---|---|
| 1 | 2026海淀期末 | none | excluded | 0 | boundary_only — verified no Xuanbiyi (Q16-21 全部 必修一/二/三/四 + 选必二/三) |
| 2 | 2024丰台一模 | Q20 (7) | P0_scoring_pdf_guarded | 5 (aspect-bundles) | candidate_for_fusion_guarded — cap-tier rubric, no per-pt切分 |
| 3 | 2024丰台二模 | Q19 (6) | P0_scoring_docx | 4 (3×2pt + 1 ext) | candidate_for_fusion_clean |
| 4 | 2024石景山一模 | Q19(2) (8) | P1_reference_only_pptx | 0 promotable / 3 boundary | NOT_PROMOTED — pptx slides only, no rubric |
| 5 | 2024顺义二模 | Q19(2) (8) | P1_reference_answer_only | 0 promotable / 4 boundary | NOT_PROMOTED — no rubric anywhere; Q18 mixed-module boundary |
| 6 | 2025丰台一模 | Q20 (8) | P0_scoring_docx_guarded | 1 (选必一 fallback) + 1 negative | guarded — primary atoms 经济与社会-coded; 选必一 only via 两个市场两种资源 fallback |
| 7 | 2025丰台期末 | Q20 (8) | P0_scoring_pptx | 8 atoms | candidate_for_fusion_clean |
| 8 | 2025延庆一模 | Q20(2) (8) | P0_scoring_pdf | 5 atoms | candidate_for_fusion_clean |
| 9 | 2025房山一模 | Q18(2) (8) | P0_scoring_pdf | 10 atoms (4+3+1 chain + replacements) | candidate_for_fusion_clean (chain logic) |
| 10 | 2025昌平二模 | Q21 (8) | P0_scoring_pptx_guarded | 4 (选必一-exclusive) + 4 (boundary 经济与社会双码) | guarded — no module tag; admit only 选必一-exclusive atoms |
| 11 | 2025石景山一模 | Q17(2) (8) | P0_scoring_docx | 4×2pt atoms | candidate_for_fusion_clean |
| 12 | 2025顺义一模 | Q20 (8) | P0_scoring_docx | 4×2pt atoms (rich substitution) | candidate_for_fusion_clean |
| 13 | 2026丰台期末 | Q20 (8) prompt-only | prompt_only_blocker | 0 | BLOCKER — LAC 五大工程 prompt found in deck (p.64) but rubric absent; deck pivots to 综合 五年规划 题 |
| 14 | 2024模块分类汇编 | n/a | source-bundle boundary | 0 | bundled paper aggregator under `已放弃` adjacent — defer to per-district P0 sources |
| 15 | 2026石景山期末 | n/a | excluded | 0 | confirmed exclusion — only `P1_candidate_reference_answer` under `已放弃/` folder; no P0 |

## Critical findings

1. **Source mis-tag**: SRC_066dbcf5b765 and SRC_ef312c0ead76 are tagged under both `2024丰台一模` and `2025丰台一模` paths in extraction logs. Content (header "2025.3" + 《北京市外商投资条例》 etc.) is 2025-only. The genuine 2024丰台一模 P0 scoring is `SRC_04f136a5f8d1` (供应链共赢链 Q20). Codex A ledger should re-tag the duplicates.
2. **2026丰台期末 LAC Q20 rubric gap**: deck `SRC_45c50fff4444` (page 64) carries the LAC "五大工程" Q20 prompt verbatim, but the immediately-following pages contain a different 9-pt question (五年规划/综合) rubric, not the LAC 8-pt rubric. Companion paper file `SRC_371641aaa3a7` is empty (107 B). DO NOT promote.
3. **Reference-answer-only suites**: 2024石景山一模 Q19(2) and 2024顺义二模 Q19(2) yield NO promotable atoms (per rule "reference answers cannot become rubrics"). Recorded as boundary documentation only.
4. **2025昌平二模 Q21 admission**: prompt has no explicit 《当代国际政治与经济》 tag, but rubric note (2) treats 推动经济全球化发展/两个市场两种资源/全球经济治理话语权 as cross-material scoring knowledge — admit guarded on 选必一-exclusive atoms only.
5. **2024丰台一模 Q20 cap-tier**: rubric scores by aspect-count (3 of 4 → 6-7; 2 → 4-5; 1 → 2-3) without per-aspect 1-pt切分 → `_guarded` aspect-bundles, parallel to 2026石景山一模 04L pattern.
6. **2025丰台一模 Q20 anti-hit guard**: rubric line 124 explicitly forbids piling on 新型国际关系/HMC/经济全球化 — primary atoms 便利投资/贸易/人才/政策 are 经济与社会-coded; only the macro fallback (两个市场两种资源/双循环) carries 选必一 anchor.

## Output files written

- `claudecode_lane/progress_batch04M.md` (this file)
- `claudecode_lane/batch04M_remaining_matrix.csv`
- `claudecode_lane/batch04M_remaining_entries.md`
- `claudecode_lane/batch04M_missing_blockers.md`
- `claudecode_lane/batch04M_conflicts_for_codex.md`
- `04_suite_reports/claudecode_suite_reports/batch04M_remaining_suite_report.md`

No files written outside lane B's writable scope.
