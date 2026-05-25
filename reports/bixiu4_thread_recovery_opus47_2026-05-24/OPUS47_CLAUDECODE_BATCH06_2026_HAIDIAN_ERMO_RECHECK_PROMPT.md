# ClaudeCode Opus 4.7 Batch06 Recheck Prompt

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
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\COVERAGE_FUSION_BATCH06_2026_HAIDIAN_ERMO_CODEX_20260525.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\01_source_inventory\suite_source_bundles\2026海淀二模.md`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\01_source_inventory\suite_source_bundles\2026海淀二模_Q16_readable_evidence.md`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\04_fusion_audit\student_patch_entries.accepted.jsonl`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\04_fusion_audit\student_patch_entries.blocked.jsonl`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\docx_insert_ledger.csv`
- Current DOCX/PDF under `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery`
- Rendered pages under `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\07_render_check\word_pdf_pages`

Review tasks:
1. Verify Q1-Q21 for `2026海淀二模` against the source bundle and official answer/scoring reference, not against Codex summaries alone.
2. Confirm Q2/Q3/Q4 are valid current DOCX insertions:
   - Q2 -> `社会存在与社会意识`
   - Q3 -> `主观能动性 / 意识的能动作用`
   - Q4 -> `联系的客观性`
3. Confirm Q16 is not overclaimed:
   - Keep only broad nodes `联系的普遍性 / 联系的观点（总）` and `实践与认识（总）`.
   - Evidence level must remain `答案和评分参考角度（非逐点细则）`.
   - Do not approve separate `矛盾就是对立统一`, `实践是认识的基础`, or `认识对实践的反作用` entries unless you find a formal detailed scoring source.
4. Confirm Q21 remains HOLD/no insert because the source only gives broad angle prompts and includes a `辩证思维` boundary risk.
5. Confirm missing boundary rows added for Q5/Q9/Q10/Q14 are reasonable and that `2026海淀二模` has zero exact `是：需逐题回源/融合裁决` rows.
6. Confirm current render gate:
   - PDF page count is 234.
   - `page_*.png` count is 234.
   - No blank rendered pages.
   - DOCX label style checks passed for the four student-facing labels.

Write your result to:
`reports\bixiu4_thread_recovery_opus47_2026-05-24\OPUS47_CLAUDECODE_BATCH06_2026_HAIDIAN_ERMO_RECHECK_RESULT.md`

Required result format:
- `Decision: pass_with_model_gate_blocked`, `pass`, or `fail`.
- `Model evidence:` include what runtime evidence you can inspect. If max effort / adaptive thinking is not machine-confirmable, state `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- `Source findings:` row-level findings, especially Q2/Q3/Q4/Q16/Q21.
- `Required corrections:` list exact files/rows if any correction is needed.
- `Residual blockers:` include GPTPro/Claude external full-artifact review as `real_call_pending` if not completed.
