# ClaudeCode Opus 4.7 Recheck Prompt - Batch26 2025西城期末

You are the ClaudeCode production/recheck lane for the 必修四哲学宝典 recovery.

Hard rules:
- Do not count Sonnet, Haiku, or model-unknown output as qualified ClaudeCode evidence.
- Do not claim STRICT_FINAL_ACCEPTED.
- Do not upgrade objective-choice answer keys into subjective scoring rubrics.
- Ordinary teacher-version reference answers can be used only at their proper evidence level.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.

Read these local files:
- `BATCH26_2025_XICHENG_FINAL_SOURCE_TRANSCRIPTION_20260525.md`
- `COVERAGE_FUSION_BATCH26_2025_XICHENG_FINAL_CODEX_20260525.md`
- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `FORMAT_RENDER_QA_20260524.md`
- `word_render_qa_20260525_batch26_word/render_manifest.json`
- `data/preprocessed_corpus/gpt_sources/89d264a31e348be6_2025西城期末细则.md`
- `data/preprocessed_corpus/gpt_sources/6662da1c2772cc38_2025北京西城高三_上_期末政治_教师版.md`

Recheck scope:
1. Confirm Batch26 treats the 2025西城期末 source pair as matched and uses the formal rubric for Q18/Q21 subjective philosophy points.
2. Confirm the 31 matrix rows cover the suite question-by-question: 14 body/objective rows and 17 boundary rows.
3. Confirm objective rows Q1/Q2/Q3/Q4/Q7 are explicitly objective-only.
4. Confirm the Q18 additions are supported by formal rubric language: 矛盾普遍性 and 价值观导向作用.
5. Confirm the Q21 改革 row is supported by formal rubric language and does not absorb the law/party-leadership dimensions into philosophy.
6. Confirm render QA is adequate: DOCX/PDF labels match, Word-visible headings are 14/14, body blank pages are 0, PDF text extraction may be 0 but Word layout pages and rendered PNGs support visibility.

Return a concise markdown result with these exact fields:
- `content_result`: one of `pass`, `pass_with_notes`, `fail`, `blocked`
- `local_policy_result`: one of `pass_with_model_gate_blocked`, `fail`, `blocked`
- `batch26_status`: one of `LOCAL_CLOSED_CONTENT_RENDER_PASS_WITH_MODEL_GATE_BLOCKED`, `LOCAL_RECHECK_FAILED_OR_BLOCKED`
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`
- `findings`: bullet list
- `required_fixes`: bullet list, or `none`

If you cannot verify a file, report `blocked` and list the blocker. Do not invent evidence.
