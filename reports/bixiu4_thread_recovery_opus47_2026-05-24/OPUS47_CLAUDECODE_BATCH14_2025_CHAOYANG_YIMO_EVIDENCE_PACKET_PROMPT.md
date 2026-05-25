# Opus 4.7 ClaudeCode Recheck Prompt - Batch14 2025朝阳一模

You are the ClaudeCode production lane for the 必修四政治庄园 recovery thread.

Required runtime target: Claude Opus 4.7, max effort, adaptive thinking. If your runtime cannot prove that model/effort/thinking configuration, say so explicitly. Do not count Sonnet, Haiku, or model-unknown output as valid evidence.

## Hard Rules

- Do not write the forbidden strict-final acceptance status.
- Do not treat ordinary reference answers as detailed rubrics.
- For each accepted principle, check whether the source is an answer key, a teacher reference answer, a rendered scoring rule, or a marking-summary/module-boundary file.
- Codex and ClaudeCode are both production lines. You are not a passive reviewer; verify the batch as a production lane.
- GPTPro web / external Claude Opus review is still `real_call_pending` unless actually completed elsewhere.

## Files To Inspect

Base folder:

`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible`

Batch14 artifacts:

- `reports\bixiu4_thread_recovery_opus47_2026-05-24\batch14_2025_chaoyang_yimo_apply_20260525.py`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH14_2025_CHAOYANG_YIMO_SOURCE_TRANSCRIPTION_20260525.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\COVERAGE_FUSION_BATCH14_2025_CHAOYANG_YIMO_CODEX_20260525.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\word_render_qa_20260525_batch14_word\render_manifest.json`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\word_render_qa_20260525_batch14_word\batch14_word_page_hits_contact_sheet.png`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\docx_insert_ledger.csv`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\04_fusion_audit\student_patch_entries.accepted.jsonl`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.docx`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.pdf`

Primary source packet:

- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\01_source_inventory\suite_source_bundles\2025朝阳一模.md`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\renders\f5f683a900508fd2\page_001.png`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\renders\f5f683a900508fd2\page_002.png`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\renders\f5f683a900508fd2\page_003.png`

## Expected Batch14 Decisions To Verify

1. Q4 is accepted under `矛盾的特殊性 / 具体问题具体分析`, based on official answer B and correct option text.
2. Q16 is accepted/registered under:
   - `实践与认识（总）`
   - `实践是认识的基础`
   - `辩证否定 / 守正创新`
   - `尊重客观规律与发挥主观能动性相结合`
   - `整体与部分`
   - `社会存在与社会意识`
   - `实现人生价值`
3. Q21 is accepted/registered under:
   - `一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一`
   - `人民群众`
   - `价值观的导向作用`
   - `价值判断与价值选择`
4. Q1-Q3, Q5-Q15 except Q4, Q17-Q20, and Qunknown are closed as source-supported module-boundary/extraction-residue items.
5. 2025朝阳一模 has no remaining `待核` or `HOLD` row in the matrix after Batch14.
6. Render QA evidence says current PDF has 243 rendered pages, 0 blank-like pages, and Word COM placed the 12 Batch14 headings on pages 17, 37, 69, 111, 136, 159, 174, 192, 205, 224, 229, and 241.

## Required Output

Write a concise Markdown result with:

- `model_gate`: pass only if you can prove Opus 4.7 max effort/adaptive thinking from runtime evidence; otherwise `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- `content_result`: pass / pass_with_notes / fail.
- `sonnet_haiku_used`: must be `no`.
- `matrix_check`: whether Q4/Q16/Q21 accepted rows and exclusions are coherent.
- `source_check`: whether the rendered rubric images actually support the accepted Q16/Q21 principles.
- `boundary_check`: whether any non-必修四 item was wrongly admitted.
- `render_check`: whether current render evidence is sufficient.
- `required_fixes`: concrete fixes if any.

