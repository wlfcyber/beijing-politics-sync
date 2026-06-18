# Slice 004 Codex + ClaudeCode Merge

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- scope: doc_order 16-20 only
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_docx_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- claudecode_trace: 04_claudecode/slice_004_real_verbose.stream.jsonl
- claudecode_model_seen: claude-opus-4-8
- claudecode_cost_seen: total_cost_usd=1.98628325
- merge_time: 2026-06-17T16:24:21+08:00

## Boundary

This merge covers five entries only. It does not imply full-book acceptance. The desktop DOCX remains the locked source and was only read/hashed.

ClaudeCode found 2 NEEDS_FIX and 3 LOW_EVIDENCE entries. Codex then backchecked local original sources and qualified the evidence state:

- Q0016 now has a local lecture PDF page that visibly contains a scoring table for 2026海淀二模Q20(2), but the desktop entry still mis-presents a 1-point alternative as the core and lacks independent hard-rule fields.
- Q0017 formal 房山一模细则 was found and confirms the 4+3+1 chain, including 高水平对外开放 and 和平与发展的国际潮流. The desktop entry still needs boundary labeling and chain weighting repair.
- Q0018 顺义一模 PPTX source confirms the 国政经角度 2分 position. The entry must mark this as an integrated-question angle, not an independent must-score term.
- Q0019 丰台期末 source confirms level grading, not point-by-point scoring. It remains low evidence for independent term extraction.
- Q0020 海淀期中 teacher answer confirms a 6分 reference answer. No formal fixed scoring split was found; the desktop entry's own "未确认" warning remains controlling.

## Source Backcheck

| source_id | source file | role in this slice | evidence |
|---|---|---|---|
| SRC_RUBRIC_2026_HAIDIAN_ERMO_Q20_COMMENTARY | /Users/wanglifei/Desktop/2026模拟题/2026各区二模/2026海淀二模/细则/26海淀高三政治二模讲评.pdf | lecture PDF with visible scoring table for Q20(2) | rendered page 81 shows Q20(2) prompt; rendered page 82 shows 7分 scoring table: 必要性知识 1分 may write 时代主题/全球化多极化/共同利益; 重要性 1分; material 1分; concrete measures any two 2分; material 1分 |
| SRC_RUBRIC_2025_FANGSHAN_YIMO_Q18 | /Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025房山一模/细则/细则.pdf | formal rubric for Q18(2) | extracted text lines 98-103: first chain 4分, second chain 3分, logic 1分 |
| SRC_RUBRIC_2026_SHUNYI_YIMO_Q21 | /Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026顺义一模/细则/细则.pptx | scoring PPTX for Q21 | extracted text lines 550-556: 国政经角度 2分, with 和平与发展/和平发展道路/多边主义/人类命运共同体/中国智慧中国方案 |
| SRC_RUBRIC_2026_FENGTAI_QIMO_Q21 | /Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026丰台期末/细则/细则.pdf | level rubric for Q21 | extracted pages 53-62: knowledge angle includes 时代主题, 多边主义, 共商共建共享, 新型国际关系; scoring is level-based 7-8/5-6/2-4/0-1 |
| SRC_TEACHER_2026_HAIDIAN_QIZHONG_Q22 | /Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026海淀期中/试卷/试卷.docx | teacher reference answer, not formal rubric | extracted text lines 185 and 219: Q22(1) asks why 全球治理倡议 gains recognition; reference answer gives one 6分 answer chain |

## Entry Findings

### Q0016 / doc_order 16 / 2026海淀二模Q20(2)

- merged_status: NEEDS_FIX
- Codex qualification: The scoring table is now source-backed by the lecture PDF, but it confirms ClaudeCode's core concern. "和平与发展/时代主题" is only within 必要性知识 1分 and is interchangeable with 经济全球化/世界多极化/共同利益. It is not an independent high-weight must-score core.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Add source type, page/point/score evidence, and mark "和平与发展仍是时代主题" as "背景及原因/必要性 1分内并列替代项", not as a standalone core row.

### Q0017 / doc_order 17 / 2025房山一模Q18(2)

- merged_status: NEEDS_FIX
- Codex qualification: Formal source confirms the two chains: first chain 4分 from 国际竞争实质 to 创新型、开放型世界经济/经济全球化; second chain 3分 from 和平与发展的国际潮流 to 联合国宗旨原则/人类命运共同体/国际交流合作/正确义利观/全球治理; logic 1分.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 NEEDS_FIX.
- repair needed: Keep the second chain as a legitimate 3分 source-backed chain, but do not let this row hide the 4分 economy/globalization main chain. Mark 高水平对外开放/对外开放基本国策 as a module-boundary item unless the final handbook explicitly keeps it as source quotation rather than 选必一主术语.

### Q0018 / doc_order 18 / 2026顺义一模Q21

- merged_status: NEEDS_FIX
- Codex qualification: The PPTX source confirms the 国政经角度 2分 text, so this is no longer merely unlocated. The problem is classification: the entry is an integrated-question angle, with multiple parallel phrases inside only 2分. It cannot be presented as one independent must-score core.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 NEEDS_FIX; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 LOW_EVIDENCE.
- repair needed: Mark "综合题/选必一国政经角度2分/任意角度" in 细则位置. If keeping the row, the answer should carry the full angle cluster instead of only "顺应时代潮流乘势而上".

### Q0019 / doc_order 19 / 2026丰台期末Q21

- merged_status: LOW_EVIDENCE
- Codex qualification: The local source confirms a level rubric, not a point rubric. "时代主题" is listed as one optional knowledge angle among 多边主义、共商共建共享、新型国际关系等. It has no independent point value or must-answer threshold.
- field result: 术语/核心采分点 LOW_EVIDENCE; 完整设问 PASS; 细则位置 LOW_EVIDENCE; 来源 LOW_EVIDENCE; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Label this as level-scoring/optional knowledge angle. Do not use it as evidence for an independent "和平与发展仍是时代主题" score point.

### Q0020 / doc_order 20 / 2026海淀期中Q22(1)

- merged_status: LOW_EVIDENCE
- Codex qualification: The teacher DOCX contains the Q22(1) prompt and reference answer, but this is not a formal scoring rule. The desktop entry's own "不展示固定分值层次/未确认" warning remains correct.
- field result: 术语/核心采分点 LOW_EVIDENCE; 完整设问 PASS; 细则位置 LOW_EVIDENCE; 来源 LOW_EVIDENCE; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Keep only as teacher-reference/answer-chain material unless a formal rubric is found. Do not assert "必要性2分-重要性4分" or any fixed split.

## Slice Acceptance

- entries reviewed this slice: 5
- field rows reviewed this slice: 40
- PASS rows added: 17
- NEEDS_FIX rows added: 11
- LOW_EVIDENCE rows added: 7
- PENDING_BOOK_LEVEL rows added: 5
- full-book status: IN_PROGRESS

Next minimal step: prepare and run slice 005 for doc_order 21-25, keeping source backcheck and ClaudeCode traces separate.
