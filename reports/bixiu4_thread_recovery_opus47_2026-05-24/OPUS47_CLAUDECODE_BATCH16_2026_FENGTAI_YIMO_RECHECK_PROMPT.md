# Opus 4.7 ClaudeCode Recheck Prompt - Batch16 2026丰台一模

You are the ClaudeCode production lane for the 必修四政治庄园 recovery thread.

Required runtime target: Claude Opus 4.7, max effort, adaptive thinking. If your runtime cannot prove that model/effort/thinking configuration, say so explicitly. Do not count Sonnet, Haiku, or model-unknown output as valid evidence.

## Hard Rules

- Do not write the forbidden strict-final acceptance status.
- Do not treat ordinary reference answers as detailed rubrics.
- For choice questions, distinguish objective answer-key evidence from subjective scoring-rubric evidence.
- Codex and ClaudeCode are both production lines. You are not a passive reviewer; verify the batch as a production lane.
- GPTPro web / external Claude Opus review remains `real_call_pending` unless actually completed elsewhere.

## Base Folder

`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible`

## Files To Inspect

Batch16 artifacts:

- `reports\bixiu4_thread_recovery_opus47_2026-05-24\batch16_2026_fengtai_yimo_apply_20260525.py`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH16_2026_FENGTAI_YIMO_SOURCE_TRANSCRIPTION_20260525.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\COVERAGE_FUSION_BATCH16_2026_FENGTAI_YIMO_CODEX_20260525.md`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `reports\bixiu4_thread_recovery_opus47_2026-05-24\word_render_qa_20260525_batch16_word\render_manifest.json`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\docx_insert_ledger.csv`
- `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\04_fusion_audit\student_patch_entries.accepted.jsonl`
- Current DOCX/PDF under `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\`

Primary source packet:

- `reports\overnight_2026-04-25\objective_answer_source_closure.md`
- `reports\overnight_2026-04-25\downloaded_evidence\2026_fengtai_yimo_with_answers.pdf`
- `reports\overnight_2026-04-25\downloaded_evidence_pages\2026_fengtai_yimo_with_answers_page_09.png`
- `C:\Users\Administrator\Desktop\2026各区模拟题\2026各区一模\2026丰台一模\试卷\丰台一模.pdf`
- `C:\Users\Administrator\Desktop\2026各区模拟题\2026各区一模\2026丰台一模\细则\2026丰台一模细则.pptx`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\26649804f1de31f5_2026丰台一模细则.md`

## Expected Batch16 Decisions To Verify

1. The objective answer key is `1B 2A 3D 4A 5A 6D 7B 8C 9D 10C 11D 12B 13A 14A 15C`.
2. Q4 answer A is accepted only under `实践是认识的基础` for correct item ①; item ② is 选必三综合思维 and must not be counted as a 必修四 philosophy node.
3. Q5 answer A is accepted under:
   - `根据固有联系建立新的具体联系`
   - `认识对实践的反作用`
4. Q6 answer D is accepted under `联系的多样性` for correct item ③; item ④ is culture/aesthetic support only.
5. Q1-Q3, Q7-Q15, Q17-Q20 are closed as module boundaries and not inserted.
6. Q16 early blocked/unknown rows are now resolved by source review: formal PPT scoring supports contradiction, link/system, value judgment/value choice, two-point/key-point, and related reasonable points. Existing DOCX Q16 entries are registered, not duplicated.
7. Q21 is registered as existing DOCX coverage only, with evidence level `answer-version reference answer + broad PPT angle`; do not upgrade it to point-by-point scoring-rule evidence.
8. Matrix has 33 `2026丰台一模` rows and 0 open-ish rows for this suite. Ledger/accepted contain 15 `2026丰台一模` records.
9. Render QA evidence says current PDF has 247 rendered pages, label counts DOCX/PDF are `2292/2292`, Q4/Q5/Q6 headings are located on rendered pages, and page 2 is the intentional divider if pixel threshold flags it.

## Required Output

Write a concise Markdown result with:

- `model_gate`: pass only if you can prove Opus 4.7 max effort/adaptive thinking from runtime evidence; otherwise `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- `content_result`: pass / pass_with_notes / fail.
- `sonnet_haiku_used`: must be `no`.
- `answer_key_check`: whether the key and source are real and sufficient for objective-choice placement only.
- `matrix_check`: whether Q4/Q5/Q6 accepted rows, Q16 registered-existing closure, Q21 evidence boundary, and exclusions are coherent.
- `docx_ledger_accepted_check`: whether the four new choice entries and 11 existing registrations are present in current DOCX, ledger, and accepted JSONL.
- `boundary_check`: whether any non-必修四哲学 item was wrongly admitted.
- `render_check`: whether current render evidence is sufficient and whether page 2 is a real blank defect or intentional divider.
- `required_fixes`: concrete fixes if any.
