# ClaudeCode Opus 4.7 Batch07 Recheck Prompt

You are the ClaudeCode production-line reviewer for the 必修四政治庄园 recovery thread.

Required model gate:
- This run must use `claude-opus-4-7` with max effort / adaptive thinking.
- Do not treat Sonnet, Haiku, or model-unknown output as qualified evidence.
- If runtime evidence cannot prove max effort / adaptive thinking, write `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

Workspace root:
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible`

Recovery directory:
`reports\bixiu4_thread_recovery_opus47_2026-05-24`

Primary files to inspect:
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\COVERAGE_FUSION_BATCH07_2024_FENGTAI_YIMO_CODEX_20260525.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\batch07_2024_fengtai_yimo_apply_20260525.py`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\01_source_inventory\suite_source_bundles\2024丰台一模.md`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\04_fusion_audit\student_patch_entries.accepted.jsonl`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\docx_insert_ledger.csv`
- Current DOCX/PDF under `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery`
- Rendered pages under `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\07_render_check\word_pdf_pages`

Review tasks:
1. Verify Q1-Q21 for `2024丰台一模` against the source bundle and official answer/scoring reference, not against Codex summaries alone.
2. Confirm Q8 is validly inserted into exactly two philosophy nodes:
   - `一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一`
   - `系统观念 / 系统优化`
   Check the official answer key and correct-option chain at source lines around `221-235` and `422-458`.
3. Confirm Q9 is already covered by current DOCX and does not need a duplicate text entry. Note any residual image/cartoon limitation separately if relevant.
4. Confirm Q18(1) and Q21 are not overclaimed:
   - Q18(1) source gives broad angles (`联系、发展、矛盾、唯物史观`) and level scoring, not point-by-point detailed rubric.
   - Q21 source gives broad angles (`唯物辩证法、构建人类命运共同体`) and level scoring, not point-by-point detailed rubric.
   Do not approve any claim that ordinary reference-answer angle prompts are strong detailed scoring rules.
5. Confirm Q1-Q7, Q10-Q17, Q18(2), Q19, Q20, and extraction residue Qunknown were reasonably excluded or closed by module boundary, including added missing rows Q5/Q7.
6. Confirm `2024丰台一模` has zero rows still needing source/fusion adjudication in the matrix.
7. Confirm current render gate:
   - PDF page count is 235.
   - `page_*.png` count is 235.
   - No blank rendered pages.
   - The two Batch07 Q8 entries have all four student-facing labels bold and color `21574C`.

Write your result to:
`reports\bixiu4_thread_recovery_opus47_2026-05-24\OPUS47_CLAUDECODE_BATCH07_2024_FENGTAI_YIMO_RECHECK_RESULT.md`

Required result format:
- `Decision: pass_with_model_gate_blocked`, `pass`, or `fail`.
- `Model evidence:` include runtime evidence you can inspect. If max effort / adaptive thinking is not machine-confirmable, state `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- `Source findings:` row-level findings, especially Q8/Q9/Q18/Q21 and added Q5/Q7 boundary rows.
- `Required corrections:` list exact files/rows if any correction is needed.
- `Residual blockers:` include GPTPro/Claude external full-artifact review as `real_call_pending` if not completed.
