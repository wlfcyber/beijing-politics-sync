# Opus 4.7 ClaudeCode Recheck Prompt - Batch17 2025门头沟一模

You are the ClaudeCode production lane for the 必修四政治庄园 recovery thread.

Required runtime target: Claude Opus 4.7, max effort, adaptive thinking. If your runtime cannot prove that model/effort/thinking configuration, say so explicitly. Do not count Sonnet, Haiku, or model-unknown output as valid evidence.

## Hard Rules

- Do not write the forbidden strict-final acceptance status.
- Do not treat ordinary reference answers as detailed rubrics.
- For choice questions, distinguish objective answer-key evidence from subjective scoring-rubric evidence.
- Codex and ClaudeCode are both production lines. Verify the batch as a production lane, not as a passive reviewer.
- GPTPro web / external Claude Opus review remains `real_call_pending` unless actually completed elsewhere.
- Q21(1) must remain a selected-compulsory-3 scientific-thinking boundary unless you find stronger contrary source evidence.
- Q21(2) may only keep the philosophy points that the marking summary explicitly names as secondary-module support. Do not upgrade it into point-by-point main-chain scoring-rule evidence.

## Base Folder

`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible`

## Files To Inspect

Batch17 artifacts:

- `reports\bixiu4_thread_recovery_opus47_2026-05-24\batch17_2025_mentougou_yimo_closure_20260525.py`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH17_2025_MENTOUGOU_YIMO_SOURCE_TRANSCRIPTION_20260525.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\COVERAGE_FUSION_BATCH17_2025_MENTOUGOU_YIMO_CODEX_20260525.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\FORMAT_RENDER_QA_20260524.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\GOVERNOR_RECOVERY_REPORT_20260524.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md`
- current DOCX/PDF under `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\`

Primary source packet:

- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\texts\1d8a23fe11f59810_2025北京门头沟高三一模政治_教师版.txt`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\texts\26d9b228064053c1_2025门头沟一模细则.txt`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_suite_bundles\2025各区模拟题__2025各区一模__2025门头沟一模.md`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\01_source_inventory\suite_source_bundles\2025门头沟一模.md`

## Expected Batch17 Decisions To Verify

1. The objective answer key is `1C 2A 3B 4A 5D 6C 7C 8B 9A 10A 11B 12B 13B 14D 15D`.
2. Current DOCX contains `2025门头沟一模` 10 times: Q6 once, Q7 once, Q16 four times, Q21 four times.
3. Q6 is covered as a choice-question answer-key chain under `认识受主客观因素影响 / 认识具有主体差异性`; it is not a subjective scoring-rule claim.
4. Q7 is covered as a choice-question answer-key chain under `人生价值的创造和实现 / 个人与社会的统一 / 主观能动性`; it is not a subjective scoring-rule claim.
5. Q16 has formal scoring-rule support for `联系的观点看问题`, `发展的观点看问题`, `对立统一`, and `价值判断与价值选择`; current DOCX already covers these, so no duplicate insertion was made.
6. Q21(1) is excluded because the prompt and scoring rule are explicitly `科学思维` / selected compulsory 3.
7. Q21(2) remains existing DOCX coverage only under secondary-module support. The marking summary prioritizes `经济与社会` and only names philosophy items as other-module options.
8. Q1-Q5 except Q6/Q7, Q8-Q15, and Q17-Q20 are source-reviewed module boundaries or old term-hit false positives.
9. Matrix has 30 `2025门头沟一模` rows and 0 open-ish rows for this suite.
10. No DOCX/PDF content changed in Batch17, so Batch16 render evidence remains controlling until the next actual DOCX edit.

## Required Output

Write a concise Markdown result with:

- `model_gate`: pass only if you can prove Opus 4.7 max effort/adaptive thinking from runtime evidence; otherwise `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- `content_result`: pass / pass_with_notes / fail.
- `sonnet_haiku_used`: must be `no` for qualified evidence.
- `answer_key_check`: whether the key and source are real and sufficient for objective-choice placement only.
- `matrix_check`: whether Q6/Q7 existing coverage, Q16 existing coverage, Q21 split boundary, and module exclusions are coherent.
- `docx_check`: whether current DOCX mentions are Q6=1, Q7=1, Q16=4, Q21=4.
- `render_check`: whether no-render-needed is valid because no DOCX/PDF content changed.
- `required_fixes`: concrete fixes if any.
