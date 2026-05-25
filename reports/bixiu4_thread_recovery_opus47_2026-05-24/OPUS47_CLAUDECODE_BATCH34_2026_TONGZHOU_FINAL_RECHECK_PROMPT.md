# ClaudeCode Opus 4.7 Recheck Prompt - Batch34 2026通州期末

You are the ClaudeCode production lane for the 必修四哲学宝典 recovery run.

Required model lane:
- Count evidence only if this run is actually executed with `claude-opus-4-7`, `--effort max`, and runtime logs show adaptive/thinking evidence.
- Sonnet, Haiku, or model-unknown output is not qualified ClaudeCode evidence.
- If runtime evidence cannot fully prove Opus 4.7 max effort/adaptive thinking, return `model_gate: BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

Files to inspect:
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\COVERAGE_FUSION_BATCH34_2026_TONGZHOU_FINAL_CODEX_20260525.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\BATCH34_2026_TONGZHOU_FINAL_SOURCE_TRANSCRIPTION_20260525.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\FORMAT_RENDER_QA_20260524.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_thread_recovery_opus47_2026-05-24\word_render_qa_20260525_batch34_word\render_manifest.json`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\data\preprocessed_corpus\gpt_sources\44537714bd68a7c1_2026通州期末细则.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\data\preprocessed_corpus\gpt_sources\7f3083ea306ea1e9_2026北京通州高三_上_期末政治_教师版.md`

Check these claims:
1. Batch34 has exactly 49 matrix rows for `2026通州期末`: 29 body rows and 20 boundary rows.
2. Body rows are exactly:
   - Q5 -> `人民群众`
   - Q5 -> `系统观念 / 系统优化`
   - Q7 -> `发展的观点 / 发展的普遍性`
   - Q7 -> `量变与质变 / 适度原则`
   - Q8 -> `根据固有联系建立新的具体联系`
   - Q8 -> `矛盾就是对立统一`
   - Q9 -> `系统观念 / 系统优化`
   - Q16 -> `一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一`
   - Q16 -> `物质决定意识`
   - Q16 -> `规律的客观性`
   - Q16 -> `尊重客观规律与发挥主观能动性相结合`
   - Q16 -> `主观能动性 / 意识的能动作用`
   - Q16 -> `联系的普遍性 / 联系的观点（总）`
   - Q16 -> `联系的客观性`
   - Q16 -> `联系的多样性`
   - Q16 -> `系统观念 / 系统优化`
   - Q16 -> `整体与部分`
   - Q16 -> `发展的观点 / 发展的普遍性`
   - Q16 -> `事物发展是前进性与曲折性的统一`
   - Q16 -> `量变与质变 / 适度原则`
   - Q16 -> `辩证否定 / 守正创新`
   - Q16 -> `人民群众`
   - Q16 -> `价值判断与价值选择`
   - Q21 -> `人民群众`
   - Q21 -> `规律的客观性`
   - Q21 -> `系统观念 / 系统优化`
   - Q21 -> `联系的普遍性 / 联系的观点（总）`
   - Q21 -> `实践与认识（总）`
   - Q21 -> `价值判断与价值选择`
3. Q5, Q7, Q8 and Q9 rows must be treated as answer-key/objective evidence only, not subjective scoring rubrics.
4. Q16 and Q21 body rows must be supported by formal scoring/rubric text; ordinary teacher references cannot substitute for rubric support.
5. Q1-Q4, Q6, Q10-Q15, Q17-Q20, Q16 culture-only points, and Q21 non-philosophy points are boundary-excluded.
6. Q21 broad `矛盾观` must not be forced into `两点论与重点论`, `主要矛盾和次要矛盾`, or any other concrete contradiction node without a more precise scoring landing.
7. Render QA is coherent: manifest says PDF pages/rendered PNGs `280/280`, no blank-like body page, label counts `2787/2787`, and visible headings `29/29`.
8. Whole-project status must remain non-final; do not claim final acceptance.

Return only a short Markdown verdict with these exact keys:

- `content_result`: one of `pass`, `pass_with_notes`, `fail`, `blocked`
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED` unless runtime evidence fully proves Opus 4.7 max/adaptive and no nonqualified model evidence is used
- `coverage_verdict`: short sentence
- `render_verdict`: short sentence
- `required_corrections`: bullet list, or `none`
- `notes`: caveats, especially objective-choice-only evidence, broad formal support rows, and the removed Q21 contradiction-node issue
