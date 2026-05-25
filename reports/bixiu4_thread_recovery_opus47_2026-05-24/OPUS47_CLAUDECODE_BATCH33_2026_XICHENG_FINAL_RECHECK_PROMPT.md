# ClaudeCode Opus 4.7 Recheck Prompt - Batch33 2026西城期末

You are the ClaudeCode production lane for the 必修四哲学宝典 recovery run.

Required model lane:
- Count evidence only if this run is actually executed with `claude-opus-4-7`, `--effort max`, and runtime logs show adaptive/thinking evidence.
- Sonnet, Haiku, or model-unknown output is not qualified ClaudeCode evidence.
- If runtime evidence cannot fully prove Opus 4.7 max effort/adaptive thinking, return `model_gate: BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

Files to inspect:
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\COVERAGE_FUSION_BATCH33_2026_XICHENG_FINAL_CODEX_20260525.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH33_2026_XICHENG_FINAL_SOURCE_TRANSCRIPTION_20260525.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\FORMAT_RENDER_QA_20260524.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\word_render_qa_20260525_batch33_word\render_manifest.json`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH33_2026_XICHENG_FINAL_RUBRIC_OCR_TRANSCRIPTION_20260525.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH33_2026_XICHENG_FINAL_TEACHER_OCR_TRANSCRIPTION_20260525.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH33_2026_XICHENG_FINAL_PINGBIAO_PPTX_TRANSCRIPTION_20260525.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\data\preprocessed_corpus\gpt_sources\54715a1e650d940e_2026西城期末细则.md`

Check these claims:
1. Batch33 has exactly 39 matrix rows for `2026西城期末`: 20 body rows and 19 boundary rows.
2. Body rows are exactly:
   - Q3 -> `认识发展原理`
   - Q3 -> `实践与认识（总）`
   - Q4 -> `矛盾的普遍性和特殊性`
   - Q5 -> `联系的普遍性 / 联系的观点（总）`
   - Q16(1) -> `人民群众`
   - Q16(2) -> `物质决定意识`
   - Q16(2) -> `主观能动性 / 意识的能动作用`
   - Q16(2) -> `一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一`
   - Q16(2) -> `真理观`
   - Q16(2) -> `实践是认识的基础`
   - Q16(2) -> `认识对实践的反作用`
   - Q16(2) -> `矛盾的普遍性和特殊性`
   - Q16(2) -> `人民群众`
   - Q16(2) -> `价值观的导向作用`
   - Q16(2) -> `价值判断与价值选择`
   - Q16(2) -> `社会存在与社会意识`
   - Q21 -> `一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一`
   - Q21 -> `实践与认识（总）`
   - Q21 -> `发展的观点 / 发展的普遍性`
   - Q21 -> `人民群众`
3. Q3-Q5 rows must be treated as answer-key/objective evidence only, not subjective scoring rubrics.
4. Q16(1), Q16(2), and Q21 body rows must be supported by formal scoring/rubric text or marking PPT where stated, not ordinary teacher reference answers.
5. Q1-Q2, Q6-Q15, Q17-Q20, Q16(1) culture-only points, and Q21 non-philosophy points are boundary-excluded.
6. Render QA is coherent: manifest says PDF pages/rendered PNGs `277/277`, no blank-like body page, label counts `2719/2719`, and visible headings `20/20`.
7. The whole project must remain non-final; do not write or imply `STRICT_FINAL_ACCEPTED`.

Return only a short Markdown verdict with these exact keys:

- `content_result`: one of `pass`, `pass_with_notes`, `fail`, `blocked`
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED` unless runtime evidence fully proves Opus 4.7 max/adaptive and no nonqualified model evidence is used
- `coverage_verdict`: short sentence
- `render_verdict`: short sentence
- `required_corrections`: bullet list, or `none`
- `notes`: caveats, especially objective-choice-only evidence and formal-term/broad support rows
