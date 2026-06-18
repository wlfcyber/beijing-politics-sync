# Slice 008 Codex + ClaudeCode Merge

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- scope: doc_order 36-40 only
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_docx_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- claudecode_trace_completed: 04_claudecode/slice_008_claudecode_findings.md
- claudecode_model_seen: claude-opus-4-8
- claudecode_debug_completed: 04_claudecode/slice_008_quick_debug.log
- source_backcheck_notes: 05_source_backcheck/slice_008/source_backcheck_slice008_notes.md
- merge_time: 2026-06-17T17:30:58+08:00

## Boundary

This merge covers five entries only. It does not imply full-book acceptance. The desktop DOCX remains the locked source and was only read/hashed.

ClaudeCode held rows 36, 37, 38, and 40 at LOW_EVIDENCE from the slice-only view, and marked row 39 NEEDS_FIX because the answer sentence over-amplifies common interests. Codex then backchecked local original sources. The scoring structures are source-backed, but the desktop rows still need independent `术语` and `细则位置` fields; Q0039 also needs content repair because common interests are only one subpoint inside the 和平发展 angle.

## Source Backcheck

| source_id | source file | role in this slice | evidence |
|---|---|---|---|
| SRC_RUBRIC_2026_HAIDIAN_ERMO_Q20_COMMENTARY | /Users/wanglifei/Desktop/2026模拟题/2026各区二模/2026海淀二模/细则/26海淀高三政治二模讲评.pdf | formal_commentary_scoring_table_for_doc_order_36 | Visual lines 5-14 confirm 7分 short-comment structure; common interests are one possible 1分 necessary-knowledge expression. |
| SRC_RUBRIC_2024_XICHENG_ERMO_Q19 | /Users/wanglifei/Desktop/2024模拟题/西城二模/细则/细则.docx | formal_rubric_for_doc_order_37 | Lines 97-104 confirm 1分总判断 plus 4分任取二点. |
| SRC_RUBRIC_2025_YANQING_YIMO_Q20_2 | /Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025延庆一模/细则/细则.docx | formal_rubric_for_doc_order_38 | Lines 87-89 confirm four 2分 angles. |
| SRC_RUBRIC_2026_CHAOYANG_QIMO_Q20 | /Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期末/细则/细则.pdf | formal_rubric_for_doc_order_39 | Visual lines 4-16 confirm four-angle 8分 rubric; current PDF text extraction is sparse, so rendered scoring page and same-source cache were preserved. |
| SRC_RUBRIC_2026_CHAOYANG_ERMO_Q20_2 | /Users/wanglifei/Desktop/2026模拟题/2026各区二模/2026朝阳二模/细则/202605朝阳高三政治二模阅卷细则(1).docx | formal_rubric_for_doc_order_40 | Lines 181-197 confirm three 2分 angles. |

## Entry Findings

### Q0036 / doc_order 36 / 2026海淀二模Q20(2)

- merged_status: NEEDS_FIX
- ClaudeCode raw: LOW_EVIDENCE; slice shows a 7分短评 and correctly limits `共同利益` to necessary knowledge, but lacked formal source.
- Codex qualification: Formal commentary pages found. The row is source-backed as one possible 背景及原因/必要性 1分 expression; it still needs exact `细则位置` and should not imply the whole 7分 answer is common interests.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Add independent 术语 and 细则位置; mark `共同利益` as one optional necessary-knowledge point within the 3分 background/meaning layer.

### Q0037 / doc_order 37 / 2024西城二模Q19

- merged_status: NEEDS_FIX
- ClaudeCode raw: LOW_EVIDENCE; it correctly read 5分 as 1分总判断 plus 4分任取二点, but source was not visible.
- Codex qualification: Formal rubric found. `国与国之间利益交汇、命运交织、休戚与共` is a source-backed 1分总判断 expression; it is not the full 5分 answer.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Add exact source and scoring position; keep common interests inside the 1分 total-judgment layer.

### Q0038 / doc_order 38 / 2025延庆一模Q20(2)

- merged_status: NEEDS_FIX
- ClaudeCode raw: LOW_EVIDENCE; slice shows four 2分 angles but lacked formal source.
- Codex qualification: Formal rubric found. Common interests are part of the 时代主题 2分 angle; the row is source-backed but structurally incomplete.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Add exact source and scoring position; preserve the 时代主题、经济全球化、多极化、人类命运共同体 four-angle boundaries.

### Q0039 / doc_order 39 / 2026朝阳期末Q20

- merged_status: NEEDS_FIX
- ClaudeCode raw: NEEDS_FIX; it flagged over-amplification of common interests in the answer sentence.
- Codex qualification: Formal rubric found. The 8分 answer is four separate angles. Common interests appear only inside the 和平发展 angle's target half, while the current material trigger and answer sentence mostly collapse the question into common interests and a single 周边命运共同体 chain.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 NEEDS_FIX; 答案句 NEEDS_FIX; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Reframe this row as one subpoint inside 和平发展背景+目标; restore the other material chains for 政治、经济、国家利益 if the entry is meant to summarize the full题.

### Q0040 / doc_order 40 / 2026朝阳二模Q20(2)

- merged_status: NEEDS_FIX
- ClaudeCode raw: LOW_EVIDENCE; it correctly read the 6分三角度 structure and raised a block-gap question.
- Codex qualification: Formal rubric found. Blocks 486-487 are blank extracted paragraphs, not missing content. The row is source-backed as angle 1, but still lacks independent `术语` and `细则位置`.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Add exact 6分 three-angle scoring position; note that `共同利益` is angle 1, alongside cooperation-win-win and China-solution angles.

## Slice Acceptance

- entries reviewed this slice: 5
- field rows reviewed this slice: 40
- PASS rows added: 18
- NEEDS_FIX rows added: 17
- LOW_EVIDENCE rows added: 0
- PENDING_BOOK_LEVEL rows added: 5
- full-book status: IN_PROGRESS

Next minimal step: prepare and run slice 009 for doc_order 41-45, with source backcheck and ClaudeCode trace separated.
