# ClaudeCode Opus 4.7 Batch08 Recheck Prompt

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
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\COVERAGE_FUSION_BATCH08_2025_DONGCHENG_YIMO_CODEX_20260525.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\batch08_2025_dongcheng_yimo_apply_20260525.py`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\01_source_inventory\suite_source_bundles\2025东城一模.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\_source_image_extracts\2025_dongcheng_yimo_q5_cartoon.png`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\04_fusion_audit\student_patch_entries.accepted.jsonl`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\docx_insert_ledger.csv`
- Current DOCX/PDF under `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery`
- Rendered pages under `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\07_render_check\word_pdf_pages`

Review tasks:
1. Verify Q1-Q21 for `2025东城一模` against the source bundle and official answer/scoring reference, not against Codex summaries alone.
2. Confirm new insertions:
   - Q1 -> `人民群众`
   - Q4 -> `根据固有联系建立新的具体联系`
   - Q5 -> `矛盾就是对立统一` and the actual cartoon image is embedded near the Q5 entry
   - Q16 -> `发展的观点 / 发展的普遍性`
3. Confirm existing coverage:
   - Q6 is already covered under `认识发展原理`
   - Q16 existing nodes remain valid: value guidance/judgment, social existence/social consciousness, dialectical negation, contradiction universality/speciality
   - Q18(1) existing nodes remain valid because the formal marking report explicitly allows philosophy substitutions such as 联系、系统优化、发展、量变质变、主要矛盾、两点论重点论
   - Q21 existing coverage is valid only as education / upper-structure reaction on economic base, with angle/level evidence; do not upgrade it to a detailed point-by-point rubric
4. Confirm excluded or boundary rows are source-defensible:
   - Q2-Q3, Q7-Q15, Q17, Q18(2), Q19, Q20, Qunknown
   - Added missing rows Q9 and Q14 are reasonable; Q14 is culture-line boundary for the current philosophy handbook
5. Confirm `2025东城一模` has zero rows still needing source/fusion adjudication in the matrix.
6. Confirm current render gate:
   - PDF page count is 237.
   - `page_*.png` count is 237.
   - No blank rendered pages.
   - Full-document label style is consistent.
   - Q5 rendered page shows the cartoon image and no overlap.

Write your result to:
`reports\bixiu4_thread_recovery_opus47_2026-05-24\OPUS47_CLAUDECODE_BATCH08_2025_DONGCHENG_YIMO_RECHECK_RESULT.md`

Required result format:
- `Decision: pass_with_model_gate_blocked`, `pass`, or `fail`.
- `Model evidence:` include runtime evidence you can inspect. If max effort / adaptive thinking is not machine-confirmable, state `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- `Source findings:` row-level findings, especially Q1/Q4/Q5/Q16/Q18/Q21 and added Q9/Q14 boundary rows.
- `Required corrections:` list exact files/rows if any correction is needed.
- `Residual blockers:` include GPTPro/Claude external full-artifact review as `real_call_pending` if not completed.
