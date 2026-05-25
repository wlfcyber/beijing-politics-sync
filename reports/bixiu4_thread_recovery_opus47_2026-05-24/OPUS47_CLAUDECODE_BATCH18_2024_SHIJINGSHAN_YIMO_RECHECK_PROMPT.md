# Opus 4.7 ClaudeCode Recheck Prompt - Batch18 2024石景山一模

You are the ClaudeCode production lane for the 必修四政治庄园 recovery thread.

Required runtime target: Claude Opus 4.7, max effort, adaptive thinking. If your runtime cannot prove that model/effort/thinking configuration, say so explicitly. Do not count Sonnet, Haiku, or model-unknown output as valid evidence.

## Hard Rules

- Do not write the forbidden strict-final acceptance status.
- Do not treat ordinary reference answers as detailed rubrics.
- For choice questions, distinguish objective answer-key evidence from subjective scoring-rubric evidence.
- Codex and ClaudeCode are both production lines. Verify the batch as a production lane, not as a passive reviewer.
- GPTPro web / external Claude Opus review remains `real_call_pending` unless actually completed elsewhere.
- Q16 source is teacher-version broad reference answer only unless you find a real scoring-rule source. Do not upgrade it into a point-by-point formal rubric.

## Base Folder

`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible`

## Files To Inspect

Batch18 artifacts:

- `reports\bixiu4_thread_recovery_opus47_2026-05-24\batch18_2024_shijingshan_yimo_apply_20260525.py`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH18_2024_SHIJINGSHAN_YIMO_SOURCE_TRANSCRIPTION_20260525.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\COVERAGE_FUSION_BATCH18_2024_SHIJINGSHAN_YIMO_CODEX_20260525.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\FORMAT_RENDER_QA_20260524.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\GOVERNOR_RECOVERY_REPORT_20260524.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\word_render_qa_20260525_batch18_word\render_manifest.json`
- current DOCX/PDF under `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\`

Primary source packet:

- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\01_source_inventory\suite_source_bundles\2024石景山一模.md`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_suite_bundles\2024各区模拟题__2024各区一模__2024石景山一模.md`
- `reports\选必一_哲学宝典式重建_2026-05-16\12_full_desktop_extract_20260524\2024\texts\2024各区一模__2024石景山一模__试卷__2024北京石景山高三一模政治（教师版带答案）.docx.txt`

## Expected Batch18 Decisions To Verify

1. The objective answer key is `1C 2B 3D 4A 5C 6A 7B 8B 9C 10A 11D 12D 13B 14C 15C`.
2. Q2 was newly inserted under `实践是认识的基础` as `31. 2024石景山一模 第2题（选择题）`, using only the objective answer key plus correct item ①: `农业生产实践具有历史性，其形式和水平不断发展`.
3. Q2 must not label the answer key as a subjective scoring rule. Item ③ is economy/productive-force background only and must not become a separate philosophy insertion.
4. Q3 is existing DOCX coverage under `社会存在与社会意识`; it should not be excluded as a false hit.
5. Q5 is existing DOCX coverage under `根据固有联系建立新的具体联系 / 把握本质和规律`.
6. Q16 remains existing DOCX coverage under development and recognition/cognition作用. The source only says `可从文化的继承与发展，文化自信，认识的作用，联系，发展等角度回答`; this is teacher-version reference-answer support, not detailed formal scoring rules.
7. Q1/Q4/Q6/Q7/Q11-Q15/Q17-Q20/Qunknown are closed as module boundaries or extraction residue. In particular, Q19(3) explicitly says `运用《逻辑与思维》知识` and stays selected-compulsory-3 boundary even though the answer mentions辩证否定观.
8. Matrix has 23 `2024石景山一模` rows and 0 open-ish rows for this suite.
9. Current DOCX mentions for `2024石景山一模` are total 5: Q2=1, Q3=1, Q5=1, Q16=2.
10. Render manifest should show Word COM PDF export ok, 247 pages rendered, DOCX/PDF label counts 2296/2296, Q2 located on PDF page 182, and only page 2 flagged as intentional foreword divider.

## Required Output

Write a concise Markdown result with:

- `model_gate`: pass only if you can prove Opus 4.7 max effort/adaptive thinking from runtime evidence; otherwise `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- `content_result`: pass / pass_with_notes / fail.
- `sonnet_haiku_used`: must be `no` for qualified evidence.
- `answer_key_check`: whether the key and source are real and sufficient for objective-choice placement only.
- `matrix_check`: whether Q2 insertion, Q3/Q5/Q16 existing coverage, Q19 boundary, and other exclusions are coherent.
- `docx_check`: whether current DOCX mentions are Q2=1, Q3=1, Q5=1, Q16=2.
- `render_check`: whether Batch18 render evidence is coherent and Q2 page 182 renders cleanly.
- `required_fixes`: concrete fixes if any.
