# ClaudeCode Opus 4.7 Recheck Prompt - Batch29 2026朝阳期中

You are the ClaudeCode production lane for the 必修四哲学宝典 recovery run.

Required model lane:
- Count evidence only if this run is actually executed with `claude-opus-4-7`, `--effort max`, and runtime logs show adaptive/thinking evidence.
- Sonnet, Haiku, or model-unknown output is not qualified ClaudeCode evidence.
- If runtime evidence cannot fully prove Opus 4.7 max effort/adaptive thinking, return `model_gate: BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

Files to inspect:
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\COVERAGE_FUSION_BATCH29_2026_CHAOYANG_MIDTERM_CODEX_20260525.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH29_2026_CHAOYANG_MIDTERM_SOURCE_TRANSCRIPTION_20260525.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\FORMAT_RENDER_QA_20260524.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\word_render_qa_20260525_batch29_word\render_manifest.json`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\data\preprocessed_corpus\gpt_sources\885e694cf464c22b_2026朝阳期中细则.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\data\preprocessed_corpus\gpt_sources\5a53b5c6863d7f95_2025北京朝阳高三_上_期中政治_教师版.md`

Check these claims:
1. Batch29 has exactly 24 body rows for `2026朝阳期中`: 11 recovered existing DOCX entries and 13 newly inserted entries.
2. Q4/Q7/Q14 are labeled objective-only and rely on teacher-version answer keys, not subjective scoring rubrics.
3. Q18 additions are supported by the formal scoring rubric lines 54-85: 矛盾、规律/实际/特殊性、主观能动性/物质决定意识/适度/实践、辩证否定/价值观/价值选择.
4. Q19 additions are supported by the formal scoring rubric lines 87-104. Contact/development/contradiction rows are labeled broad-angle where appropriate and are not overstated.
5. Q1-Q3, Q5-Q6, Q8-Q17, Q19 culture-only points, Q20, and Q21 non-philosophy points are correctly boundary-excluded. Q20 must remain excluded because it is 选必三《逻辑与思维》辩证思维方法, not 必修四 philosophy body.
6. Render QA is coherent: manifest says PDF pages/rendered PNGs match, no body blank page, label counts match, and visible headings are 24/24.

Return only a short Markdown verdict with these exact keys:

- `content_result`: one of `pass`, `pass_with_notes`, `fail`, `blocked`
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED` unless runtime evidence fully proves Opus 4.7 max/adaptive and no nonqualified model evidence is used
- `coverage_verdict`: short sentence
- `render_verdict`: short sentence
- `required_corrections`: bullet list, or `none`
- `notes`: caveats, especially objective-only and broad-angle rows
