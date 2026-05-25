# ClaudeCode Opus 4.7 Recheck Prompt - Batch28 2026丰台期末

You are the ClaudeCode production lane for the 必修四哲学宝典 recovery run.

Required model lane:
- Count evidence only if the run is actually executed with `claude-opus-4-7`, `--effort max`, and runtime logs show adaptive/thinking evidence.
- Sonnet, Haiku, or model-unknown output is not qualified ClaudeCode evidence.
- If runtime evidence cannot fully prove Opus 4.7 max effort/adaptive thinking, return `model_gate: BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

Files to inspect:
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\COVERAGE_FUSION_BATCH28_2026_FENGTAI_FINAL_CODEX_20260525.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH28_2026_FENGTAI_FINAL_SOURCE_TRANSCRIPTION_20260525.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\FORMAT_RENDER_QA_20260524.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\word_render_qa_20260525_batch28_word\render_manifest.json`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\data\preprocessed_corpus\gpt_sources\dbc93cbfd3a93eff_2026丰台期末细则.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\skills\beijing-gaokao-politics-rubric\assets\current-artifacts\必修四哲学材料-知识触发总框架_持续更新版_v2.md`

Check these claims:
1. Batch28 has exactly 18 body rows for `2026丰台期末`: 4 recovered existing Q16 DOCX entries and 14 newly inserted entries.
2. Q1/Q2/Q4 are labeled objective-only and rely on the recorded answer-closure artifact, not subjective scoring rubrics.
3. Q16 additions are directly supported by the formal rubric lines 46-54.
4. Q22 additions are limited to rubric-listed philosophy terms; broad or term-only rows are labeled as broad/term support and not overstated.
5. Q17-Q21 and Q22 non-philosophy points are correctly boundary-excluded.
6. Render QA is coherent: manifest says PDF pages/rendered PNGs match, no body blank page, label counts match, visible headings are 18/18.

Return only a short Markdown verdict with these exact keys:

- `content_result`: one of `pass`, `pass_with_notes`, `fail`, `blocked`
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED` unless runtime evidence fully proves Opus 4.7 max/adaptive and no nonqualified model evidence is used
- `coverage_verdict`: short sentence
- `render_verdict`: short sentence
- `required_corrections`: bullet list, or `none`
- `notes`: caveats, especially objective-only and broad/term-support rows
