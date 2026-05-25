# ClaudeCode Opus 4.7 Batch11 Read-Only Recheck Prompt

You are the ClaudeCode production-line reviewer for the 必修四政治庄园 recovery thread.

Runtime gate:
- This run must use `claude-opus-4-7` with max effort / adaptive thinking.
- Do not treat Sonnet, Haiku, or model-unknown output as qualified evidence.
- If runtime evidence cannot prove max effort / adaptive thinking, write `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Do not use Bash or edit files. Use only read-only file inspection tools if needed.

Review scope:
- Suite: `2026西城二模`.
- Codex batch report: `reports\bixiu4_thread_recovery_opus47_2026-05-24\COVERAGE_FUSION_BATCH11_2026_XICHENG_ERMO_CODEX_20260525.md`.
- Rubric transcription: `reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH11_2026_XICHENG_ERMO_RUBRIC_TRANSCRIPTION_20260525.md`.
- Matrix: `reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`.
- Source bundle: `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\01_source_inventory\suite_source_bundles\2026西城二模.md`.
- Accepted JSONL: `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\04_fusion_audit\student_patch_entries.accepted.jsonl`.
- Ledger: `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\docx_insert_ledger.csv`.
- Render manifest: `reports\bixiu4_thread_recovery_opus47_2026-05-24\word_render_qa_20260525_batch11_word\render_manifest.json`.

Facts already verified by Codex that you must independently check where possible:
- Matrix rows after Batch11: `879`; `2026西城二模` rows: `33`; `2026西城二模` open rows: `0`; global broader open rows: `412`.
- Ledger rows: `70`; `2026西城二模` ledger rows: `8`.
- Accepted JSONL rows: `70`; `2026西城二模` accepted rows: `8`.
- DOCX/PDF label count: `2231 / 2231`.
- PDF page count and PNG page count: `241 / 241`.
- Insertions:
  - Q3 -> `联系的普遍性 / 联系的观点（总）`, official answer D, correct item ④.
  - Q4 -> `系统观念 / 系统优化`, official answer A.
  - Q16 -> `价值观的导向作用`, supported by rendered rubric transcription; existing Q16 contradiction/practice evidence repaired to rendered-rubric evidence.
  - Q20 -> `一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一`, `人民群众`, `发展的观点 / 发展的普遍性`, with weak/broad teacher-answer plus material evidence only.
- Exclusions/boundaries:
  - Q1, Q2, Q5-Q15, Q17-Q19, Qunknown.
  - Missing rows Q10/Q12/Q13/Q14 were added and closed as boundary exclusions.

Return only the review result in stdout. Required format:

Decision: pass_with_model_gate_blocked, pass, or fail

Model evidence:
- State whether you can inspect `claude-opus-4-7`.
- State `BLOCKED_MODEL_CONFIRMATION_REQUIRED` if max effort / adaptive thinking is not machine-confirmable from inside the run.

Source findings:
- Q3, Q4, Q16, Q20, excluded rows, missing rows, and render gate.

Required corrections:
- Exact rows/files if any correction is required, otherwise `none`.

Residual blockers:
- GPTPro full-artifact external review: real_call_pending.
- Claude Opus external full-artifact review: real_call_pending.
