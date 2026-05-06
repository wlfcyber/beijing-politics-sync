# Strict-4 Redwords Local Decision And Patch Log

## 2026-05-04 21:55 CST External Closure Addendum

Final strict-4 closure is no longer merely local.

- GPT-5.5 Pro was captured from the correct same ChatGPT Pro `Opus4.6 vs 4.7` conversation. Verdict: `NEEDS_FIX`.
- GPT must-fix 1 was accepted: framework/category headings in the question loop must be black, while only `踩分词` and answer-sentence scoring words are red. The generator now renders numbered items as black `框架归类`.
- GPT must-fix 2 was accepted: every red word in the question loop must reverse-trace to that question's scoring terms. `tools/audit_redword_source_trace.py` now reports `PASS`, bad-context red spans 0, unsourced question red spans 0, suspect rows 0.
- Claude Opus 4.7 Adaptive was captured after the GPT patch from the correct same `学生文档审稿意见` conversation, model visible as Opus 4.7 Adaptive. Verdict: `PASS`.
- Claude should-fix items were locally patched: `顺应各国人民愿望` was added to the 2025海淀期中 Q21(2) answer sentence,同一层备用提醒 was added for high-density alternative scoring terms, student-facing `点位性质` now distinguishes formal/colored/image/reference-style source type, and `同槽` no longer appears in student output.
- Final artifacts were regenerated at 21:48 and Word-open/save checked afterward.

Final local verdict: `PASS_AFTER_REAL_GPT_FIX_AND_REAL_CLAUDE_PASS`.

time: 2026-05-04 21:02 CST
run: `选必一_当代国际政治与经济_四线终极全书_2026-05-03`
target artifact: `09_delivery/选必一_当代国际政治与经济_完整学生讲义_最终闭环版_20260504.md`

## Lane B Challenge Result

ClaudeCode B completed and exited with `PASS_WITH_GUARDS`.

Accepted flags:

1. C1 `2026通州期末 Q20` 第2点：not a framework-copy blocker after local source裁决. The user notebook pins the six-point Tongzhou rubric, and the local atom row points to `2026通州期末_Q20_SRC_35ef9424281a`. Codex patched the answer sentence so the point itself now visibly contains `和平与发展成为时代主题`、`经济全球化深入发展`、`顺应各国人民愿望`, while preserving governance-deficit/material wording.
2. C2 `2026西城期末 Q20` 角度二第1项：formal evidence card records `和平发展合作共赢是时代潮流 / 非传统安全威胁`. Codex patched the卷面句 and summary so `非传统安全威胁` appears in the actual answer sentence, not only in the red-word list.
3. C3 `2026顺义一模 Q20` 国际政治3分同一功能位：local extraction notes and atom table identify this as an equivalent/replacement pool. Codex retained the pool but added a student-facing usage boundary: `任选一组贴材料写，不必四串全背`.
4. G1 technical source labels: student-facing卷面层级 now says `答案示例性质`、`朝阳讲评 PPT 第N页点位`、`试题分析 PPT 第64页第N点`、`海淀题面表格细则` instead of raw `PPTX slide...` / `image...` / `guarded` labels.
5. G2 `2025海淀期中 Q21(2)` #3: `本题命中框架` now adds `本题红字落点：国际影响力、话语权不断提升`, preventing students from treating the whole综合国力 framework sentence as the exact colored scoring phrase.

## Regenerated Artifacts

- Markdown: `09_delivery/选必一_当代国际政治与经济_完整学生讲义_最终闭环版_20260504.md`
- DOCX: `09_delivery/选必一_当代国际政治与经济_完整学生讲义_最终闭环版_20260504.docx`
- PDF: `09_delivery/选必一_当代国际政治与经济_完整学生讲义_最终闭环版_20260504.pdf`
- Audit matrix: `08_review/role_reviews/all_question_rubric_point_repair_matrix_20260504.csv`

## Fresh QA

- main training questions: 47
- question-level scoring summaries: 47
- rubric-point audit rows: 197
- unique audit questions: 47
- reverse red-term coverage missing: 0
- main Markdown red spans: 3805
- DOCX red runs: 4249
- PDF pages: 146
- forbidden student-term scan: PASS
- Microsoft Word open/save: PASS for the selected DOCX only
- QuickLook DOCX thumbnail: PASS, `09_delivery/quicklook_strict4_20260504/`
- canonical `render_docx.py`: BLOCKED because `soffice`, `libreoffice`, and `brew` are unavailable on this Mac.

## Local Verdict

Codex A local production and source裁决 for the strict red-word delta: `PASS`.

This does not by itself satisfy the real GPT-5.5 Pro or real Claude Opus 4.7 Adaptive lanes.
