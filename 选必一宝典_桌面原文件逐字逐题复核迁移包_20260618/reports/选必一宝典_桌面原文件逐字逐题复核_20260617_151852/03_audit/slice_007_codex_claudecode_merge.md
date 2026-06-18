# Slice 007 Codex + ClaudeCode Merge

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- scope: doc_order 31-35 only
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_docx_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- claudecode_trace_completed: 04_claudecode/slice_007_claudecode_findings.md
- claudecode_model_seen: claude-opus-4-8
- claudecode_debug_completed: 04_claudecode/slice_007_quick_debug.log
- source_backcheck_notes: 05_source_backcheck/slice_007/source_backcheck_slice007_notes.md
- merge_time: 2026-06-17T17:20:20+08:00

## Boundary

This merge covers five entries only. It does not imply full-book acceptance. The desktop DOCX remains the locked source and was only read/hashed.

ClaudeCode correctly held all five rows at LOW_EVIDENCE from the slice-only view because no formal source was included inside the slice prompt. Codex then backchecked local original sources and upgraded the evidence state to source-backed NEEDS_FIX for all five entries: the scoring layers are real, but the desktop rows still lack independent `术语` and `细则位置` fields and several rows need exact layer boundaries.

## Source Backcheck

| source_id | source file | role in this slice | evidence |
|---|---|---|---|
| SRC_RUBRIC_2026_YANQING_YIMO_Q19_2 | /Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026延庆一模/细则/细则.docx | formal_rubric_for_doc_order_31 | Lines 102-110 confirm theory logic 4分 and value meaning 4分. |
| SRC_RUBRIC_2026_SHIJINGSHAN_ERMO_Q18 | /Users/wanglifei/Desktop/2026模拟题/2026各区二模/2026石景山二模/细则/石景山区高三政治第二次模拟考试答案评分细则(1).doc | formal_rubric_for_doc_order_32 | Lines 49-50 confirm basis 4分 and meaning 4分. |
| SRC_RUBRIC_2025_DONGCHENG_ERMO_Q20 | /Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025东城二模/细则/细则.pdf | formal_rubric_for_doc_order_33 | Lines 165-177 confirm background 2分, spirit 4分, action 2分. |
| SRC_RUBRIC_2026_SHUNYI_YIMO_Q20 | /Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026顺义一模/细则/细则.pptx | formal_rubric_for_doc_order_34 | Slide 9 confirms common interests 1分, international politics 3分, international economy 3分. |
| SRC_RUBRIC_2024_CHAOYANG_ERMO_Q20_PDF | /Users/wanglifei/Desktop/2024模拟题/2024朝阳二模/细则/细则.pdf | formal_rubric_for_doc_order_35_duplicate_Q0026 | Lines 190-208 confirm the common-interest angle inside the 5分 consensus-how layer. |

## Entry Findings

### Q0031 / doc_order 31 / 2026延庆一模Q19(2)

- merged_status: NEEDS_FIX
- ClaudeCode raw: LOW_EVIDENCE; slice shows 4+4 structure but source was not visible; ref should be Q19(2).
- Codex qualification: Formal rubric found. Common interests are source-backed as one theory-logic angle, but the current row must not stand for the whole 8分 answer.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 NEEDS_FIX; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Add independent 术语 and 细则位置; mark theory logic 4分 versus value meaning 4分; keep common interests as one national-interest angle.

### Q0032 / doc_order 32 / 2026石景山二模Q18

- merged_status: NEEDS_FIX
- ClaudeCode raw: LOW_EVIDENCE; slice structure is self-consistent but source was not visible, and it flagged a textbook wording risk around 国家实力.
- Codex qualification: Formal rubric found. It confirms common interests inside the 依据4分 layer and confirms the 意义4分 layer; the desktop answer is too compressed for the full question.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 NEEDS_FIX; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Add exact 依据4分/意义4分 position and the two meaning dimensions; do not present the common-interest sentence as the whole 8分 response.

### Q0033 / doc_order 33 / 2025东城二模Q20

- merged_status: NEEDS_FIX
- ClaudeCode raw: LOW_EVIDENCE; slice shows background/spirit/action but source was not visible.
- Codex qualification: Formal marking material found. It confirms the 2+4+2 essay layers and names common interests as 2分 within the spirit layer.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Add independent 术语 and 细则位置; keep common interests as part of the spirit layer, not the whole essay.

### Q0034 / doc_order 34 / 2026顺义一模Q20

- merged_status: NEEDS_FIX
- ClaudeCode raw: LOW_EVIDENCE; it saw the 1+3+3 split but lacked formal source.
- Codex qualification: Formal PPTX source found. `共同利益` is a required 1分 layer, followed by international politics 3分 and international economy 3分.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Add exact 7分 split and preserve the 1分/3分/3分 boundaries.

### Q0035 / doc_order 35 / 2024朝阳二模Q20

- merged_status: NEEDS_FIX
- ClaudeCode raw: LOW_EVIDENCE; it identified duplicate-group relation with Q0026 but lacked source.
- Codex qualification: Formal PDF source already used in slice 006 and rechecked here. This row is the common-interest how-layer angle, not Q0026's climate-risk why layer.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Add exact consensus-how 5分 layer position and keep it separate from the same-question climate-risk row.

## Slice Acceptance

- entries reviewed this slice: 5
- field rows reviewed this slice: 40
- PASS rows added: 18
- NEEDS_FIX rows added: 17
- LOW_EVIDENCE rows added: 0
- PENDING_BOOK_LEVEL rows added: 5
- full-book status: IN_PROGRESS

Next minimal step: prepare and run slice 008 for doc_order 36-40, with source backcheck and ClaudeCode trace separated.
