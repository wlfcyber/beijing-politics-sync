# Automation Checker - Batch04M Remaining Status

check_time: 2026-05-04 00:45
role: Codex A automation checker
write_scope: only this file
student_doc_touched: no
word_pdf_final_touched: no

## Verdict

status: WARN_WITH_BLOCKERS

Batch04M remaining is internally visible as Codex A prelim, but it is not final-fusion-ready. The A-side CSV structure is readable, 2026丰台期末 Q20 remains prompt-only blocked, and guarded rows are labeled in candidate/fusion files. However, ClaudeCode B is still active and its `batch04M_remaining_matrix.csv` is structurally incomplete, while `COVERAGE_MATRIX.csv` still marks all Batch04M rows as `claudecode_batch04M_running` with Patcher/Governor pending. Final student draft, Word/PDF, FINAL_ACCEPTANCE, and coverage close remain blocked.

## Read Scope

- `COVERAGE_MATRIX.csv`
- `SOURCE_LEDGER.csv`
- `fusion/scoring_atom_table_batch04M_remaining_prelim.csv`
- `05_coverage/batch04M_remaining_candidates.csv`
- `progress.md`
- `task_plan.md`
- `claudecode_lane/batch04M_remaining_matrix.csv`

## CSV Structure Check

PASS:

- `COVERAGE_MATRIX.csv`: 76 rows, 11 columns, no row-width errors.
- `SOURCE_LEDGER.csv`: 206 rows, 9 columns, no row-width errors.
- `fusion/scoring_atom_table_batch04M_remaining_prelim.csv`: 43 rows, 14 columns, no row-width errors.
- `05_coverage/batch04M_remaining_candidates.csv`: 16 rows, 7 columns, no row-width errors.

WARN/BLOCK:

- `claudecode_lane/batch04M_remaining_matrix.csv`: 70 rows, header has 11 columns, 65 data rows have row-width mismatch. Treat as incomplete B-line output and do not use as machine-merge input.

## Coverage / Progress Consistency

PASS:

- `progress.md` and `task_plan.md` agree that Batch04M is Codex A prelim only and that final delivery remains blocked.
- `05_coverage/batch04M_remaining_candidates.csv` has 15 Batch04M suite/question outcomes matching the coverage rows.
- `fusion/scoring_atom_table_batch04M_remaining_prelim.csv` has 42 prelim atoms: 28 `candidate_with_fixes`, 14 `candidate_with_guard`.

WARN:

- `COVERAGE_MATRIX.csv` rows 62-76 still show `claudecode_batch04M_running`, `patcher_status=pending`, and `governor_status=pending`. This is consistent with waiting for B-line closure, but not consistent with any attempt to declare Batch04M closed.
- ClaudeCode B screen `xuanbiyi_claudecode_batch04M_20260504` is still active. Therefore Batch04M A/B closure must wait.

## 2026丰台期末 Q20

status: BLOCK

The block is preserved across the checked control files:

- `05_coverage/batch04M_remaining_candidates.csv`: `blocked_prompt_only`, evidence `prompt_found_current_scoring_missing`.
- `COVERAGE_MATRIX.csv` row 74: `batch04M_prompt_only_blocker`, `blocked_prompt_only`, `prompt_found_current_scoring_missing`.
- `fusion/scoring_atom_table_batch04M_remaining_prelim.csv`: no promoted 2026丰台期末 Q20 atom.
- `SOURCE_LEDGER.csv` rows 205-206: both notes say prompt found but no current formal scoring rubric found.

Critical warning: `SOURCE_LEDGER.csv` row 205 still has broad `P0_candidate_scoring` / `P0_candidate_scoring` labels for the scoring PDF. Downstream must hard-override that broad label with the finer status `batch04M_rechecked_prompt_only_or_support_source`. It is not permission to promote.

## Guarded Row Risk

status: WARN

Guarded rows are visible in the fusion file, but several can be misread if downstream only reads broad source labels:

- `2024丰台一模 Q20`: `M-FT24YM-01..04`, `P0_scoring_docx_level_aspects_guarded`; four level/aspect bundles, not fixed point-by-point rubric frequency.
- `2024石景山一模 Q19(2)`: `M-SJS24YM-01..03`, `P1_pptx_reference_answer_guarded`; reference/answer-chain only, not P0 scoring frequency.
- `2024顺义二模 Q19(2)`: `M-SY24EM-01..03`, `P0_answer_only_mixed_module_guarded`; mixed-module answer-only, only optional 选必一 subchain expression accumulation.
- `2025昌平二模 Q21`: `M-CP25EM-01..04`, `P0_formal_scoring_pptx_no_explicit_book_guard`; no explicit book tag, guarded economic-globalization expression only.

Additional A/B warning from the visible B matrix content: B appears to downgrade `2025丰台一模 Q20` main four practical-measure atoms as mostly `经济与社会` coded, with only `两个市场两种资源/双循环` as guarded fallback. Because the B matrix CSV is malformed and B is still running, this should become an A/B closure item rather than an automatic promotion or automatic deletion.

## ClaudeCode B Waiting State

status: BLOCK_FOR_AB_CLOSURE

- Active screen exists: `43807.xuanbiyi_claudecode_batch04M_20260504`.
- Active Claude process exists under `START_CLAUDECODE_BATCH04M.sh`.
- `claudecode_lane/batch04M_remaining_matrix.csv` exists but is row-width invalid.

Conclusion: wait for ClaudeCode B to finish cleanly or for B-line outputs to be structurally repaired before A/B conflict closure and total fusion.

## Final-Fusion Preconditions Still Open

BLOCK:

- Resolve B-line incomplete/malformed matrix and active screen state.
- Close A/B conflicts, especially `2025丰台一模 Q20`, `2024石景山一模 Q19(2)`, `2024顺义二模 Q19(2)`, and the already blocked `2026丰台期末 Q20`.
- Preserve all guarded labels through total fusion; do not convert guarded rows into stable main-frequency rows.
- Keep `2026丰台期末 Q20` out of fusion atoms unless a current formal scoring rubric is found and rechecked.
- Keep `2026石景山期末` excluded and `2024模块分类汇编` source-bundle boundary only.
- Do not start final student Markdown, Word/PDF, FINAL_ACCEPTANCE, or coverage close until Batch04M A/B closure plus total fusion review are complete.

## Files Blocking Final Delivery

- `COVERAGE_MATRIX.csv`: Batch04M rows still `claudecode_batch04M_running`, Patcher/Governor pending, row 74 blocked.
- `SOURCE_LEDGER.csv`: row 205 broad P0 candidate label conflicts with prompt-only note and must not be read as promotion.
- `claudecode_lane/batch04M_remaining_matrix.csv`: malformed/incomplete B-line CSV.
- `fusion/scoring_atom_table_batch04M_remaining_prelim.csv`: prelim only, not final merged student-ready table.
- `progress.md` / `task_plan.md`: both continue to block student final, Word/PDF, FINAL_ACCEPTANCE, and coverage close.

