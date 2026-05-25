# ClaudeCode Opus 4.7 Recheck Prompt - Batch30 2026朝阳期末

You are the ClaudeCode production lane for the 必修四哲学宝典 recovery run.

Required model lane:
- Count evidence only if this run is actually executed with `claude-opus-4-7`, `--effort max`, and runtime logs show adaptive/thinking evidence.
- Sonnet, Haiku, or model-unknown output is not qualified ClaudeCode evidence.
- If runtime evidence cannot fully prove Opus 4.7 max effort/adaptive thinking, return `model_gate: BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

Files to inspect:
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\COVERAGE_FUSION_BATCH30_2026_CHAOYANG_FINAL_CODEX_20260525.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH30_2026_CHAOYANG_FINAL_SOURCE_TRANSCRIPTION_20260525.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\FORMAT_RENDER_QA_20260524.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\word_render_qa_20260525_batch30_word\render_manifest.json`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\data\preprocessed_corpus\gpt_sources\487b2d15b3a3ac2b_2026朝阳期末细则.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\data\preprocessed_corpus\gpt_sources\e1a49527cb4c175f_2026北京朝阳高三_上_期末政治.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH30_2026_CHAOYANG_FINAL_OCR_LINES_20260525.md`

Check these claims:
1. Batch30 has exactly 10 body rows for `2026朝阳期末`: 2 recovered existing DOCX entries and 8 newly inserted entries.
2. Q16 keeps the existing `辩证否定 / 守正创新` row and adds `一切从实际出发`、`规律的客观性`、`联系的普遍性`、`发展的观点`、`矛盾就是对立统一`.
3. Q16 broad rows must be treated as formal broad-angle/term support from rubric line 21, not inflated into detailed point-by-point scoring rules.
4. Q21 keeps `整体与部分` and adds `系统观念 / 系统优化`、`联系的普遍性 / 联系的观点（总）`、`人民群众`; these must be directly supported by rubric lines 152-158.
5. Q1-Q15 must not become objective-choice body rows because no reliable answer key was found.
6. Q17, Q18(1), Q18(2), Q19, Q20, and Q21 non-philosophy policy points are boundary-excluded by formal rubric module or point scope.
7. Render QA is coherent: manifest says PDF pages/rendered PNGs match, no body blank page, label counts match, and visible headings are 10/10.

Return only a short Markdown verdict with these exact keys:

- `content_result`: one of `pass`, `pass_with_notes`, `fail`, `blocked`
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED` unless runtime evidence fully proves Opus 4.7 max/adaptive and no nonqualified model evidence is used
- `coverage_verdict`: short sentence
- `render_verdict`: short sentence
- `required_corrections`: bullet list, or `none`
- `notes`: caveats, especially no-answer-key choice rows and Q16 broad-angle rows
