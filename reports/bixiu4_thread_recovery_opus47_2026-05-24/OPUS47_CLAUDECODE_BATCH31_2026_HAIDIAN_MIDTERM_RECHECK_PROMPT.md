# ClaudeCode Opus 4.7 Recheck Prompt - Batch31 2026海淀期中

You are the ClaudeCode production lane for the 必修四哲学宝典 recovery run.

Required model lane:
- Count evidence only if this run is actually executed with `claude-opus-4-7`, `--effort max`, and runtime logs show adaptive/thinking evidence.
- Sonnet, Haiku, or model-unknown output is not qualified ClaudeCode evidence.
- If runtime evidence cannot fully prove Opus 4.7 max effort/adaptive thinking, return `model_gate: BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

Files to inspect:
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\COVERAGE_FUSION_BATCH31_2026_HAIDIAN_MIDTERM_CODEX_20260525.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH31_2026_HAIDIAN_MIDTERM_SOURCE_TRANSCRIPTION_20260525.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\FORMAT_RENDER_QA_20260524.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\word_render_qa_20260525_batch31_word\render_manifest.json`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\data\preprocessed_corpus\gpt_sources\e65381bd22912637_2026海淀期中细则.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\data\preprocessed_corpus\gpt_sources\11cac42f979196cd_2025北京海淀高三_上_期中政治_教师版.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH31_2026_HAIDIAN_MIDTERM_RUBRIC_OCR_LINES_20260525.md`

Check these claims:
1. Batch31 has exactly 5 body rows for `2026海淀期中`: Q9 -> `人民群众`; Q22(2) -> `主观能动性 / 意识的能动作用`, `事物发展是前进性与曲折性的统一`, `社会发展的两大基本规律和基本矛盾`, `人民群众`.
2. Q9 must be treated as objective-choice-only evidence based on teacher answer key `9A`; it must not become a subjective scoring rubric.
3. Q22(2) body rows must be supported by formal scoring page_094, not by the ordinary teacher reference answer.
4. Q22(2) `社会发展的两大基本规律和基本矛盾` is a broad formal angle from `人类社会发展规律`; do not overclaim a detailed point-by-point rubric if the page only gives the broad term.
5. Q22(1), Q16-Q21, and Q22(2) non-philosophy points such as党的领导、制度优势、人民当家作主、人类命运共同体、民族精神 are boundary-excluded.
6. Render QA is coherent: manifest says PDF pages/rendered PNGs match, no body blank page, label counts match, and visible headings are 5/5.
7. The whole project must remain non-final; do not write or imply `STRICT_FINAL_ACCEPTED`.

Return only a short Markdown verdict with these exact keys:

- `content_result`: one of `pass`, `pass_with_notes`, `fail`, `blocked`
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED` unless runtime evidence fully proves Opus 4.7 max/adaptive and no nonqualified model evidence is used
- `coverage_verdict`: short sentence
- `render_verdict`: short sentence
- `required_corrections`: bullet list, or `none`
- `notes`: caveats, especially Q9 objective-only evidence and Q22(2) broad-angle rows
