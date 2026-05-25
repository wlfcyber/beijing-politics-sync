# ClaudeCode Opus 4.7 Batch09 Recheck Prompt

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
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\COVERAGE_FUSION_BATCH09_2025_FENGTAI_YIMO_CODEX_20260525.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\batch09_2025_fengtai_yimo_apply_20260525.py`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\01_source_inventory\suite_source_bundles\2025丰台一模.md`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\04_fusion_audit\student_patch_entries.accepted.jsonl`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\docx_insert_ledger.csv`
- Current DOCX/PDF under `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery`
- Rendered pages under `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\07_render_check\word_pdf_pages`

Review tasks:
1. Verify Q1-Q21 for `2025丰台一模` against the source bundle and official answer/scoring reference, not against Codex summaries alone.
2. Confirm new insertions:
   - Q15 -> `辩证否定 / 守正创新`, using the official answer key plus correct-option chain "连续性与创新性的有机统一".
   - Q18(1) -> `一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一`, using the formal scoring point "我国从实际出发" in the scientific-thinking question. Do not treat the whole scientific-thinking question as 必修四 philosophy.
3. Confirm existing coverage:
   - Q2 is already covered under `矛盾就是对立统一`.
   - Q4 is already covered under `规律的客观性`.
   - Q16 is already covered under `价值判断与价值选择`; culture-line angles remain outside the current philosophy mainline.
   - Q18(3) existing coverage remains valid under 联系观、发展观、矛盾观、价值观. Its evidence is formal scoring-angle/level support, not point-by-point detailed rubric.
4. Confirm excluded or boundary rows are source-defensible:
   - Q1, Q3, Q5-Q14, Q17, Q18(2), Q19, Q20, Q21, and Qunknown.
   - Confirm added rows Q12 and Q13 are reasonable boundary closures; Q13 source extraction has incomplete option text, but the stem and official answer key support a logic/thinking boundary for this 必修四 philosophy task.
5. Confirm `2025丰台一模` has zero exact-source rows still needing placement/fusion adjudication in the matrix.
6. Confirm current render gate:
   - PDF page count is 239.
   - `page_*.png` count is 239.
   - No blank rendered pages.
   - Full-document label count is DOCX/PDF `2192 / 2192`.
   - New Q18(1) is visible in the PDF around page 16 and new Q15 is visible around page 108.

Write your result to:
`reports\bixiu4_thread_recovery_opus47_2026-05-24\OPUS47_CLAUDECODE_BATCH09_2025_FENGTAI_YIMO_RECHECK_RESULT.md`

Required result format:
- `Decision: pass_with_model_gate_blocked`, `pass`, or `fail`.
- `Model evidence:` include runtime evidence you can inspect. If max effort / adaptive thinking is not machine-confirmable, state `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- `Source findings:` row-level findings, especially Q15, Q18(1), Q2, Q4, Q16, Q18(3), Q12/Q13, and excluded Q17-Q21.
- `Required corrections:` list exact files/rows if any correction is needed.
- `Residual blockers:` include GPTPro/Claude external full-artifact review as `real_call_pending` if not completed.
