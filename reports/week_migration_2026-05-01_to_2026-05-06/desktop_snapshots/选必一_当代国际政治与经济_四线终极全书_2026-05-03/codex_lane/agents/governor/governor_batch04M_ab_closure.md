# Governor Gate: Batch04M A/B Closure

time: 2026-05-04
role: Codex A Governor
scope: Batch04M remaining prelim after ClaudeCode B conflict pass
final_gate: PASS_WITH_GUARD
review_gate: ALLOW_REAL_CLAUDE_OPUS_GPT_CONTENT_REVIEW_ONLY
final_pass: NOT_ALLOWED

## Files Reviewed

- `06_conflicts/batch04M_claudecode_conflict_resolution.md`
- `claudecode_lane/batch04M_conflicts_for_codex.md`
- `fusion/scoring_atom_table_batch04M_remaining_prelim.csv`
- `SOURCE_LEDGER.csv`
- `COVERAGE_MATRIX.csv`
- `07_student_doc/选必一_完整学生讲义_融合稿_20260504.md`

## Gate Ruling

Batch04M A/B closure is sufficient to enter real Claude Opus / GPT content review as an advisory content-review stage. This is not a final acceptance gate and must not be treated as final PASS, Word/DOCX/PDF release, FINAL_ACCEPTANCE, or coverage close.

## Hard Checks

1. reference answer not rubric: PASS
   - `2024石景山一模 Q19(2)` and `2024顺义二模 Q19(2)` are downgraded to `P1_reference_answer_only` / `reference_only`.
   - Fusion rows keep them outside main student core and only as expression-awareness boundary material.
   - No ordinary reference answer is promoted to P0 scoring rubric or stable scoring atom.

2. `2026丰台期末 Q20`: PASS AS BLOCKED
   - A/B ruling is `BLOCKED_PROMPT_ONLY`.
   - `SOURCE_LEDGER.csv` marks current scoring missing / prompt-only support.
   - `COVERAGE_MATRIX.csv` marks `blocked_prompt_only`.
   - No atom from this question is promoted in `fusion/scoring_atom_table_batch04M_remaining_prelim.csv`.
   - Student draft only says this question has prompt support and does not enter the main framework.

3. `2026石景山期末`: PASS AS EXCLUDED
   - `COVERAGE_MATRIX.csv` keeps it as `excluded,user_confirmed_excluded_no_scoring`.
   - No fusion atom is promoted.
   - Student draft keeps only a short exclusion reminder.

4. `2025丰台一模 Q20` hard negative: PASS WITH GUARD
   - Four practical-measure rows are `boundary_only` because they are primarily 《经济与社会》 practical-measure scoring.
   - Only the double-circulation / two-markets-two-resources fallback remains as `candidate_with_guard`.
   - The hard negative rule is preserved as `boundary_only`: piling 新型国际关系、人类命运共同体 or generic 推动经济全球化发展 does not score in this question.
   - Student draft includes the warning that this question cannot be answered by套人类命运共同体 or 新型国际关系.

5. student doc clean: PASS FOR REVIEW DRAFT
   - Scan found no source IDs, filesystem paths, P0/P1/P2/P3 labels, Codex/GPT/Claude labels, candidate/guard technical labels, FINAL_ACCEPTANCE, DOCX/PDF release language, or backend audit fields.
   - The occurrences of “AI/大模型” are material-context language, not model/backend pollution.
   - The final “慎用与排除” section is student-facing caution language, not evidence metadata leakage.

## Allowed Next Step

- May enter real Claude Opus teaching-text review and real GPT content review.
- Those reviews are advisory only; local source evidence and Governor/Patcher rulings remain controlling.

## Still Blocked

- Do not release final Markdown as final accepted.
- Do not generate or release Word/DOCX/PDF.
- Do not mark FINAL_ACCEPTANCE.
- Do not close coverage or source ledger.
- Do not promote prompt-only, reference-only, or guarded rows into stable main-frequency atoms without new local P0 scoring evidence.
- Do not treat `2026丰台期末 Q20` placeholder terms as scoring atoms.
- Do not re-open `2026石景山期末`.
- Do not let the `2025丰台一模 Q20` hard negative spill over to other questions where HMC / 新型国际关系 / 经济全球化 genuinely score.

## Downstream Required Before Any Final Gate

- Run real Claude Opus / GPT content review against the current student draft.
- Re-run student clean scan after any content-review patch.
- Re-run bridge consistency check between fusion atoms, student draft, coverage, and source ledger.
- Re-run Governor and Confucius review after content patches.
- Only after full source/coverage tasks are complete may a separate final-acceptance gate be considered.
