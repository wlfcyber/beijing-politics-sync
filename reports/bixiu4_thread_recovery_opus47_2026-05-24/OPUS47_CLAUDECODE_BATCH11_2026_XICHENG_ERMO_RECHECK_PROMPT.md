# ClaudeCode Opus 4.7 Batch11 Recheck Prompt

You are the ClaudeCode production-line reviewer for the 必修四政治庄园 recovery thread.

Required model gate:
- This run must use `claude-opus-4-7` with max effort / adaptive thinking.
- Do not treat Sonnet, Haiku, or model-unknown output as qualified evidence.
- If runtime evidence cannot prove max effort / adaptive thinking, write `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Ordinary reference answers cannot be promoted into scoring rules. Use official answer keys, scoring standards, marking rules, rendered rubric evidence, and explicit source text.

Workspace root:
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible`

Recovery directory:
`reports\bixiu4_thread_recovery_opus47_2026-05-24`

Primary files to inspect:
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\COVERAGE_FUSION_BATCH11_2026_XICHENG_ERMO_CODEX_20260525.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH11_2026_XICHENG_ERMO_RUBRIC_TRANSCRIPTION_20260525.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\batch11_2026_xicheng_ermo_apply_20260525.py`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\01_source_inventory\suite_source_bundles\2026西城二模.md`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\04_fusion_audit\student_patch_entries.accepted.jsonl`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\docx_insert_ledger.csv`
- Current DOCX/PDF under `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery`
- Rendered pages under `reports\bixiu4_thread_recovery_opus47_2026-05-24\word_render_qa_20260525_batch11_word`

Review tasks:
1. Verify Q1-Q20 for `2026西城二模` against the source bundle, answer key, and Q16 rendered rubric evidence. Do not rely on Codex summaries alone.
2. Confirm new insertions:
   - Q3 -> `联系的普遍性 / 联系的观点（总）`, using official answer D and correct item ④ `世界并不缺乏联系`.
   - Q4 -> `系统观念 / 系统优化`, using official answer A and its direct wording `系统优化方法` / `整体最优`.
   - Q16 -> `价值观的导向作用`, using rendered rubric evidence and the transcription that explicitly lists `价值观的导向作用`. Existing Q16 contradiction/practice entries should also be repaired to rendered-rubric evidence.
   - Q20 -> `一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一`, `人民群众`, and `发展的观点 / 发展的普遍性`. These must remain weaker broad teacher-answer/material-evidence support, not detailed scoring-rule support.
3. Confirm excluded or boundary rows are source-defensible:
   - Q1, Q2, Q5-Q15, Q17-Q19, and Qunknown.
   - Confirm added missing rows Q10, Q12, Q13, and Q14 are present and closed as boundary exclusions.
4. Confirm `2026西城二模` has zero source rows still needing placement/fusion adjudication in the matrix.
5. Confirm current render gate:
   - PDF page count is 241.
   - `page-*.png` count is 241.
   - Full-document label count is DOCX/PDF `2231 / 2231`.
   - New entries are visible in rendered pages: Q20 reality page 16-17, Q3 page 54, Q4 page 79, Q20 development page 91, Q20 people page 209, Q16 value-guidance page 222.

Write your result to:
`reports\bixiu4_thread_recovery_opus47_2026-05-24\OPUS47_CLAUDECODE_BATCH11_2026_XICHENG_ERMO_RECHECK_RESULT.md`

Required result format:
- `Decision: pass_with_model_gate_blocked`, `pass`, or `fail`.
- `Model evidence:` include runtime evidence you can inspect. If max effort / adaptive thinking is not machine-confirmable, state `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- `Source findings:` row-level findings, especially Q3, Q4, Q16 rendered-rubric repair, Q20 weaker evidence boundary, and excluded Q10/Q12/Q13/Q14.
- `Required corrections:` list exact files/rows if any correction is needed.
- `Residual blockers:` include GPTPro/Claude external full-artifact review as `real_call_pending` if not completed.
