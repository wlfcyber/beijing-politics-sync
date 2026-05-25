# ClaudeCode Opus 4.7 Recheck Prompt - Batch32 2026海淀期末

You are the ClaudeCode production lane for the 必修四哲学宝典 recovery run.

Required model lane:
- Count evidence only if this run is actually executed with `claude-opus-4-7`, `--effort max`, and runtime logs show adaptive/thinking evidence.
- Sonnet, Haiku, or model-unknown output is not qualified ClaudeCode evidence.
- If runtime evidence cannot fully prove Opus 4.7 max effort/adaptive thinking, return `model_gate: BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

Files to inspect:
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\COVERAGE_FUSION_BATCH32_2026_HAIDIAN_FINAL_CODEX_20260525.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH32_2026_HAIDIAN_FINAL_SOURCE_TRANSCRIPTION_20260525.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\FORMAT_RENDER_QA_20260524.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\word_render_qa_20260525_batch32_word\render_manifest.json`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\data\preprocessed_corpus\gpt_sources\7832041a93d37e1f_2026海淀期末细则.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\data\preprocessed_corpus\gpt_sources\ac3124113aec7062_2026北京海淀高三_上_期末政治_教师版.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH32_2026_HAIDIAN_FINAL_RUBRIC_OCR_LINES_20260525.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH32_2026_HAIDIAN_FINAL_TEACHER_OCR_LINES_20260525.md`

Check these claims:
1. Batch32 has exactly 22 body rows for `2026海淀期末`.
2. Objective-choice rows are exactly Q1 -> `实践与认识（总）`, Q2 -> `联系的普遍性 / 联系的观点（总）`, Q3 -> `认识发展原理`, Q4 -> `实践是认识的基础`; they must be treated as answer-key/objective evidence only, not subjective scoring rubrics.
3. Q16 body rows are `两点论与重点论`, `主观能动性 / 意识的能动作用`, `价值判断与价值选择`, `价值观的导向作用`, `实现人生价值`, `实践与认识（总）`, `实践是认识的基础`, `矛盾就是对立统一`.
4. Q17 body rows are `主观能动性 / 意识的能动作用`, `价值判断与价值选择`, `价值观的导向作用`, `发展的观点 / 发展的普遍性`, `根据固有联系建立新的具体联系`, `矛盾的普遍性和特殊性`, `联系的普遍性 / 联系的观点（总）`, `认识对实践的反作用`.
5. Q21 body rows are `人民群众` and `矛盾就是对立统一`.
6. Q16/Q17/Q21 rows must be supported by formal scoring/rubric text, not ordinary teacher reference answers.
7. Broad rows such as Q16 `两点论与重点论`, Q16 `实践是认识的基础`, and Q17 `根据固有联系建立新的具体联系` must be described as broad/formal-angle support, not overclaimed as narrow point-by-point scoring terms.
8. Q5-Q15 non-body rows, Q18-Q20, Q17 culture points, Q20(2) logic/超前思维, and Q21 non-philosophy points are boundary-excluded.
9. Render QA is coherent: manifest says PDF pages/rendered PNGs `273/273`, no blank-like body page, label counts `2667/2667`, and visible headings `22/22`.
10. The whole project must remain non-final; do not write or imply `STRICT_FINAL_ACCEPTED`.

Return only a short Markdown verdict with these exact keys:

- `content_result`: one of `pass`, `pass_with_notes`, `fail`, `blocked`
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED` unless runtime evidence fully proves Opus 4.7 max/adaptive and no nonqualified model evidence is used
- `coverage_verdict`: short sentence
- `render_verdict`: short sentence
- `required_corrections`: bullet list, or `none`
- `notes`: caveats, especially objective-choice-only evidence and broad-angle rows
