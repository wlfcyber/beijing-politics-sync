# Opus 4.7 ClaudeCode Recheck Prompt - Batch15 2026房山一模选择题答案键补证

You are the ClaudeCode production lane for the 必修四政治庄园 recovery thread.

Required runtime target: Claude Opus 4.7, max effort, adaptive thinking. If your runtime cannot prove that model/effort/thinking configuration, say so explicitly. Do not count Sonnet, Haiku, or model-unknown output as valid evidence.

## Hard Rules

- Do not write the forbidden strict-final acceptance status.
- Do not treat ordinary reference answers as detailed rubrics.
- For choice questions, distinguish objective answer-key evidence from subjective scoring-rubric evidence.
- Codex and ClaudeCode are both production lines. You are not a passive reviewer; verify the batch as a production lane.
- GPTPro web / external Claude Opus review remains `real_call_pending` unless actually completed elsewhere.

## Files To Inspect

Base folder:

`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible`

Batch15 artifacts:

- `reports\bixiu4_thread_recovery_opus47_2026-05-24\batch15_2026_fangshan_yimo_choice_key_apply_20260525.py`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH15_2026_FANGSHAN_YIMO_CHOICE_KEY_SOURCE_TRANSCRIPTION_20260525.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\COVERAGE_FUSION_BATCH15_2026_FANGSHAN_YIMO_CHOICE_KEY_CODEX_20260525.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\word_render_qa_20260525_batch15_word\render_manifest.json`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\docx_insert_ledger.csv`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\04_fusion_audit\student_patch_entries.accepted.jsonl`
- current DOCX/PDF under `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\`

Primary source packet:

- `reports\overnight_2026-04-25\objective_answer_source_closure.md`
- `reports\overnight_2026-04-25\downloaded_evidence\2026_fangshan_yimo_with_answers.pdf`
- `reports\overnight_2026-04-25\downloaded_evidence_pages\2026_fangshan_yimo_with_answers_page_09.png`
- rendered paper pages under `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\renders\e37482eff39f3618\page_001.png` to `page_006.png`
- historical candidate note: `skills\feige-politics-garden-bixiu4\assets\current-artifacts\必修四哲学材料-知识触发总框架_持续更新版_v2.md` around lines 1813-1835

## Expected Batch15 Decisions To Verify

1. The objective answer key is `1C 2D 3B 4A 5C 6D 7B 8A 9D 10B 11D 12C 13B 14C 15A`.
2. Q2 answer D is accepted under:
   - `价值判断与价值选择`
   - `实现人生价值`
3. Q4 answer A is accepted under:
   - `实践是认识的基础`
   - `系统观念 / 系统优化`
4. Q6 answer D is not accepted into the current philosophy body. The old v2 candidate is downgraded because the official correct option is `超前思维`, a Logic and Thinking boundary. Near-neighbor认识论 material is not enough to count as a current answer landing.
5. Q1, Q3, Q5, Q7-Q15 are closed by official answer key and module-boundary reasoning.
6. M0880-M0894 no longer contain `NEED_ANSWER_KEY_BATCH12`.
7. Render QA evidence says current PDF has 245 rendered pages, 0 blank-like pages, and normalized title search finds Q2/Q4 titles in both DOCX and PDF.

## Required Output

Write a concise Markdown result with:

- `model_gate`: pass only if you can prove Opus 4.7 max effort/adaptive thinking from runtime evidence; otherwise `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- `content_result`: pass / pass_with_notes / fail.
- `sonnet_haiku_used`: must be `no`.
- `answer_key_check`: whether the key and source are real and sufficient for objective-choice placement only.
- `matrix_check`: whether Q2/Q4 accepted rows, Q6 downgrade, and all exclusions are coherent.
- `docx_ledger_accepted_check`: whether inserted headings are registered in current DOCX, ledger, and accepted JSONL.
- `boundary_check`: whether any non-必修四哲学 item was wrongly admitted.
- `render_check`: whether current render evidence is sufficient.
- `required_fixes`: concrete fixes if any.
