# Slice 006 Codex + ClaudeCode Merge

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- scope: doc_order 26-30 only
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_docx_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- claudecode_trace_completed: 04_claudecode/slice_006_claudecode_findings.md
- claudecode_model_seen: claude-opus-4-8
- claudecode_debug_completed: 04_claudecode/slice_006_quick_debug.log
- claudecode_stalled_attempts: 04_claudecode/slice_006_stalled_attempt_note.md; 04_claudecode/slice_006_retry1_failed_note.md
- source_backcheck_notes: 05_source_backcheck/slice_006/source_backcheck_slice006_notes.md
- merge_time: 2026-06-17T17:09:44+08:00

## Boundary

This merge covers five entries only. It does not imply full-book acceptance. The desktop DOCX remains the locked source and was only read/hashed.

ClaudeCode completed a concise third attempt after two real opus/max attempts stalled or produced no usable output. The completed ClaudeCode findings were based on the slice text and therefore marked Q0026-Q0029 LOW_EVIDENCE and Q0030 NEEDS_FIX. Codex then backchecked local original sources and corrected the evidence state:

- Q0026 has a formal 2024朝阳二模 Q20 PDF rubric. It confirms the 2+1+5 structure and the current core phrase as a 1分 why layer, so the row is source-backed but still needs independent fields and layer repair.
- Q0027 has a formal 2025东城一模 Q20 marking page and matches the user-pinned 4+2+2 structure. It still needs independent fields and module-boundary labels for 必修二-leaning alternatives.
- Q0028 formal source confirms a keyword/level rubric rather than a fixed common-interest scoring point, so LOW_EVIDENCE remains.
- Q0029 visible PPTX source is reference-answer style without point-by-point scoring; LOW_EVIDENCE remains and the answer/core should use the visible phrase about expanding common interests.
- Q0030 has a formal 2025丰台期末 Q20 scoring slide confirming 4+2+2, but the current core and answer sentence need exact wording and value-meaning repair.

## Source Backcheck

| source_id | source file | role in this slice | evidence |
|---|---|---|---|
| SRC_RUBRIC_2024_CHAOYANG_ERMO_Q20_PDF | /Users/wanglifei/Desktop/2024模拟题/2024朝阳二模/细则/细则.pdf | formal_rubric_for_doc_order_26 | Slice 006: extracted page 5 lines 181-208 confirm principles 2分 and consensus why1/how5分. |
| SRC_RUBRIC_2024_CHAOYANG_ERMO_Q20_DOCX_SUPP | /Users/wanglifei/Desktop/2024模拟题/2024朝阳二模/细则/补充材料/细则.docx | supplemental_reference_for_doc_order_26 | Slice 006: supplemental DOCX gives short answer only; PDF has detailed scoring. |
| SRC_RUBRIC_2025_DONGCHENG_YIMO_Q20 | /Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025东城一模/细则/细则.pdf | formal_marking_material_for_doc_order_27 | Slice 006: extracted lines 170-180 confirm user-pinned 4+2+2 three-layer structure. |
| SRC_RUBRIC_2026_SHIJINGSHAN_YIMO_Q20 | /Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026石景山一模/细则/细则.doc | formal_level_rubric_for_doc_order_28 | Slice 006: extracted lines 49-69 confirm keyword/level scoring, available angles, no fixed common-interest point. |
| SRC_RUBRIC_2026_FENGTAI_YIMO_Q19 | /Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026丰台一模/细则/细则.pptx | pptx_reference_answer_for_doc_order_29_low_evidence | Slice 006: extracted slides 41-42 give reference answer; no fixed point-by-point scoring found. |
| SRC_RUBRIC_2025_FENGTAI_QIMO_Q20 | /Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025丰台期末/细则/细则.pptx | formal_scoring_pptx_for_doc_order_30 | Slice 006: extracted slide 52 confirms 4+2+2 split and exact point wording. |

## Entry Findings

### Q0026 / doc_order 26 / 2024朝阳二模Q20

- merged_status: NEEDS_FIX
- ClaudeCode raw: ClaudeCode: LOW_EVIDENCE; detailed split visible but no source anchor in slice input; core only covers one consensus layer.
- Codex qualification: Formal rubric found. This upgrades ClaudeCode LOW_EVIDENCE to source-backed NEEDS_FIX: current core is a real 1分 consensus point, but the desktop entry lacks independent 术语/细则位置 and must keep the 1分 why layer separate from the 5分 how layer.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Add independent 术语 and 细则位置; mark Q20 基本原则2分 and 共识 why1分/how5分 separately; keep current core as the why-layer term, not the whole question.

### Q0027 / doc_order 27 / 2025东城一模Q20

- merged_status: NEEDS_FIX
- ClaudeCode raw: ClaudeCode: LOW_EVIDENCE; three-layer structure self-consistent but source anchor missing in slice input.
- Codex qualification: Formal rubric found and matches the user-pinned three-layer structure. Still NEEDS_FIX because the desktop row lacks independent 术语/细则位置 and the same-question group includes 必修二-leaning alternatives without boundary labels.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 NEEDS_FIX.
- repair needed: Add exact 细则位置: 第一层共同利益2分 plus economic/opening direction2分; second layer developing-country interests2分; third layer diplomacy/community2分. Boundary-label 高水平对外开放/高质量发展.

### Q0028 / doc_order 28 / 2026石景山一模Q20

- merged_status: LOW_EVIDENCE
- ClaudeCode raw: ClaudeCode: LOW_EVIDENCE; keyword/level question, not fixed scoring point.
- Codex qualification: Formal source exists but confirms ClaudeCode concern: this is a keyword/level question. It does not make 国家间共同利益是国家合作的基础 an independent fixed scoring term.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 LOW_EVIDENCE; 来源 LOW_EVIDENCE; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Label as level/keyword evidence. Repair core to source-listed 维护共同利益/common angle or mark current phrase as textbook expression, not fixed rubric term.

### Q0029 / doc_order 29 / 2026丰台一模Q19

- merged_status: LOW_EVIDENCE
- ClaudeCode raw: ClaudeCode: LOW_EVIDENCE; no fixed score layer visible, only可写方向.
- Codex qualification: Visible PPTX source is a reference-answer style page, not a fixed scoring split. It uses 致力于扩大同各国利益的汇合点 rather than the desktop core 国家间共同利益是国家合作的基础.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 LOW_EVIDENCE; 来源 LOW_EVIDENCE; 材料触发 PASS; 答案句 NEEDS_FIX; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Keep LOW_EVIDENCE unless a more precise marking page is found. Repair answer/core toward visible phrase 扩大同各国利益的汇合点 and do not turn 可写方向 into fixed 同题组.

### Q0030 / doc_order 30 / 2025丰台期末Q20

- merged_status: NEEDS_FIX
- ClaudeCode raw: ClaudeCode: NEEDS_FIX; answer落点 misses value-meaning half and layer wording needs repair.
- Codex qualification: Formal scoring slide found. The row remains NEEDS_FIX because the exact source phrase is 基于国家间共同利益构建中非命运共同体, not merely the generic cooperation-base phrase, and 答案落点 misses the value-meaning half.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 NEEDS_FIX; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Repair core to exact scoring expression; add value-meaning answer sentence for 新型国际关系/现代化/命运共同体; standardize layers as 4+2+2.

## Slice Acceptance

- entries reviewed this slice: 5
- field rows reviewed this slice: 40
- PASS rows added: 17
- NEEDS_FIX rows added: 14
- LOW_EVIDENCE rows added: 4
- PENDING_BOOK_LEVEL rows added: 5
- full-book status: IN_PROGRESS

Next minimal step: prepare and run slice 007 for doc_order 31-35, with source backcheck and ClaudeCode trace separated.
