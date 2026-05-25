# FANGSHAN_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525

Status: `FANGSHAN_2025_YIMO_REPAIRED_DOCX_Q2_Q5_INSERTED_MODEL_GATES_OPEN`

Updated: 2026-05-25 14:54 +08

## Source Basis

- Source bundle: `preprocessed_corpus\gpt_suite_bundles\2025各区模拟题__2025各区一模__2025房山一模.md`.
- Formal answer key: source-bundle lines `21-27`.
- Q2 prompt and teacher detail: source-bundle lines `198-204`, `417-424`.
- Q5 prompt and teacher detail: source-bundle lines `222-228`, `447-454`.
- Q16 formal rubric: source-bundle lines `29-45`; Q16(2)(3) are logic/innovative-thinking boundaries.
- Q20 formal rubric: source-bundle lines `150-160`.

## Decisions

- Inserted into current DOCX:
  - `2025房山一模 第2题（选择题）` under `系统观念 / 系统优化`.
  - `2025房山一模 第5题（选择题）` under `辩证否定 / 守正创新`.
- Q2/Q5 are recorded as correct-option chains only: `选择题边界已明示；非主观题评分细则`.
- Q3 remains current-DOCX covered under the formal answer key. The teacher-version detailed explanation conflicts with the formal key, so the formal key controls.
- Q4 remains current-DOCX covered as a choice chain.
- Q16(1) and Q20 remain current-DOCX covered under formal rubric support.
- Q1, Q6-Q15, Q17-Q19 are excluded by module boundary; Q10/Q11 were added to the matrix because the prior matrix lacked explicit rows for them.
- No Sonnet/Haiku/model-unknown evidence was promoted.
- GPTPro web review and full Claude Opus 4.7 web/app DOCX/PDF artifact review remain `real_call_pending`.

## Backups And Outputs

- DOCX backup: `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24_backup_before_2025_fangshan_yimo_q2_q5_choice_insert_20260525_145438.docx`.
- Matrix backup: `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_2025_fangshan_yimo_candidate_repair_20260525_145438.csv`.
- Ledger backup: `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\docx_insert_ledger_backup_before_2025_fangshan_yimo_q2_q5_choice_insert_20260525_145438.csv`.
- Matrix rows added: `M1472, M1473`.
- Inserted headings: `37. 2025房山一模 第2题（选择题）; 26. 2025房山一模 第5题（选择题）`.

## Boundary

This is a local source/DOCX/matrix repair. It does not close external model review, full manual typography review, ClaudeCode model confirmation, or the deferred ORDER_063 final GitHub upload gate.

## Post-Render Verification

- Updated: 2026-05-25 14:55 +08.
- Matrix audit after repair: `1473` rows, `452` in-book/body rows, `268` total risk rows, `0` in-book/body risk rows.
- Render rerun after DOCX insertion: `279/279` PDF pages rendered to PNG.
- DOCX/PDF label counts: `2779/2779`.
- Blank-like body pages excluding cover/foreword: `0`.
- Target page inspection:
  - Q2 appears on rendered page `94`; visible layout is clean.
  - Q5 appears across rendered pages `129-130`; split is natural, answer landing continues cleanly, with no visible overlap or clipping.
- PDF text probe found Q2 material on page `94` and Q5 material on pages `129-130`.
- Boundary remains: GPTPro web review and full Claude Opus 4.7 web/app DOCX/PDF artifact review are still `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
