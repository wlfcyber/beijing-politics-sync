# Slice 009 Codex + ClaudeCode Merge

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- scope: doc_order 41-45 only
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_docx_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- claudecode_trace_completed: 04_claudecode/slice_009_claudecode_findings.md
- claudecode_model_seen: claude-opus-4-8
- claudecode_debug_completed: 04_claudecode/slice_009_quick_debug.log
- source_backcheck_notes: 05_source_backcheck/slice_009/source_backcheck_slice009_notes.md
- merge_time: 2026-06-17T17:47:36+08:00

## Boundary

This merge covers five entries only. It does not imply full-book acceptance. The desktop DOCX remains the locked source and was only read/hashed.

ClaudeCode marked Q0041 PASS for the key trap that common interests are not a fixed score in the Haidian essay, and held Q0042-Q0045 at LOW_EVIDENCE because no formal source was visible inside the slice. Codex then backchecked local original sources. All five entries now have source evidence, but the desktop rows still need independent `术语` and `细则位置` fields; Q0042 also uses backstage scoring language in the material trigger and has unlabelled cross-module terms, while Q0045 has a subject-boundary problem around `中国智慧`.

## Source Backcheck

| source_id | source file | role in this slice | evidence |
|---|---|---|---|
| SRC_RUBRIC_2024_HAIDIAN_ERMO_Q18_DOCX | /Users/wanglifei/Desktop/2024模拟题/海淀二模/细则/细则.docx | formal_scoring_text_for_doc_order_41 | Lines 51-53 confirm Q18(1) is broad-angle essay scoring: 时代主题、世界多极化、人类命运共同体、国际组织等角度. |
| SRC_RUBRIC_2026_XICHENG_QIMO_Q20 | /Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026西城期末/细则/细则.pdf | formal_scoring_reference_for_doc_order_42 | Visual lines 3-14 confirm 2+3+3 scoring and `共同利益` as one 1分 why item. |
| SRC_RUBRIC_2026_TONGZHOU_YIMO_Q19 | /Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026通州一模/细则/26 通州一模评标.pdf | formal_marking_material_for_doc_order_43 | Lines 160-176 confirm knowledge/measures 4分 plus material function 4分; visual exam page confirms Q19 prompt. |
| SRC_RUBRIC_2025_CHAOYANG_ERMO_Q21 | /Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025朝阳二模/细则/细则.docx | formal_rubric_for_doc_order_44 | Lines 283-310 confirm 中国3分、区域3分、世界2分; common interests sit in the regional layer. |
| SRC_RUBRIC_2026_FANGSHAN_ERMO_Q20 | /Users/wanglifei/Desktop/2026模拟题/2026各区二模/2026房山二模/细则/26房山评标.docx | formal_rubric_for_doc_order_45 | Lines 134-146 confirm six 1分 directions plus 2分 material; `共同利益/共同发展` is one direction. |

## Entry Findings

### Q0041 / doc_order 41 / 2024海淀二模Q18(1)

- merged_status: NEEDS_FIX
- ClaudeCode raw: PASS for the key trap; it noted block506 still over-directs students to "先写共同利益".
- Codex qualification: Formal source confirms this is an 8分 essay/等级题. `共同利益` can be used as migration language for cooperation necessity, but it is not a fixed rubric item.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Add independent fields and weaken block506 to match the block512 migration boundary.

### Q0042 / doc_order 42 / 2026西城期末Q20

- merged_status: NEEDS_FIX
- ClaudeCode raw: LOW_EVIDENCE; it correctly read the 2+3+3 structure but lacked official scoring material.
- Codex qualification: Same-source visual read confirms 2+3+3 and `共同利益` as one 1分 item under the 3分 why layer. The desktop row is source-backed but needs repair because block516 says "答题要求角度2" inside material trigger and block522 includes cross-module `新发展理念/有为政府/有效市场` without boundary labels.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 NEEDS_FIX; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 NEEDS_FIX.
- repair needed: Rewrite the material trigger from source material, not backstage scoring language; preserve 2+3+3; boundary-label the cross-module practice terms.

### Q0043 / doc_order 43 / 2026通州一模Q19

- merged_status: NEEDS_FIX
- ClaudeCode raw: LOW_EVIDENCE; it correctly saw 4分知识/措施 + 4分材料作用 but lacked formal source.
- Codex qualification: Formal marking page confirms the 4+4 structure and the "必须答作用" ceiling. `共同利益是合作的基础` is one可采知识 under 镜头一; it must not become the whole answer.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Add exact source and scoring position; keep common interests as one knowledge item among the broader 元首外交 answer set.

### Q0044 / doc_order 44 / 2025朝阳二模Q21

- merged_status: NEEDS_FIX
- ClaudeCode raw: LOW_EVIDENCE; it correctly saw 中国3/区域3/世界2 but lacked formal source.
- Codex qualification: Formal rubric confirms the three-layer 8分 structure. `共同的国家利益是国际合作基础` is a 1分 option inside the 区域的发展需要 layer.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Add exact source and scoring position; do not index the whole three-layer why question as only a common-interest point.

### Q0045 / doc_order 45 / 2026房山二模Q20

- merged_status: NEEDS_FIX
- ClaudeCode raw: LOW_EVIDENCE; it correctly saw six 1分 directions plus material 2分 but lacked formal source and flagged a subject issue.
- Codex qualification: Formal rubric confirms `共同利益/共同发展` is exactly one 1分 direction. The desktop row's source-backed layer is usable, but block556's "中国智慧" phrasing is too loose because the prompt is about 世界数据组织完善全球数据治理、服务全球数字经济发展的智慧.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 NEEDS_FIX.
- repair needed: Add exact source and scoring position; rewrite the subject boundary as 世界数据组织/全球数据治理智慧, not generic 中国智慧.

## Slice Acceptance

- entries reviewed this slice: 5
- field rows reviewed this slice: 40
- PASS rows added: 17
- NEEDS_FIX rows added: 18
- LOW_EVIDENCE rows added: 0
- PENDING_BOOK_LEVEL rows added: 5
- full-book status: IN_PROGRESS

Next minimal step: prepare and run slice 010 for doc_order 46-50, with source backcheck and ClaudeCode trace separated.
