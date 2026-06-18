# Slice 005 Codex + ClaudeCode Merge

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- scope: doc_order 21-25 only
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_docx_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- claudecode_trace: 04_claudecode/slice_005_real_verbose.stream.jsonl
- claudecode_model_seen: claude-opus-4-8
- claudecode_cost_seen: total_cost_usd=2.11803125
- merge_time: 2026-06-17T16:41:12+08:00

## Boundary

This merge covers five entries only. It does not imply full-book acceptance. The desktop DOCX remains the locked source and was only read/hashed.

ClaudeCode found 2 NEEDS_FIX and 3 LOW_EVIDENCE entries from the slice text and the run ledger state. Codex then backchecked local original sources and corrected the evidence state:

- Q0021 now has a local formal/marking source for 2026通州一模Q19, but the source confirms that "和平与发展" is only one optional knowledge item inside a broad "knowledge/measures 4分 + material function 4分" rubric. The row still needs evidence-level repair.
- Q0022 has a visible 2026西城期末Q20 scoring page. It confirms a 2+3+3 structure, but the desktop entry's layer text is partly inaccurate and includes 必修二 terms without module-boundary marking.
- Q0023 formal 2024海淀二模 scoring text only gives broad available angles for Q18(1); the desktop row's "霸权主义/强权政治" core remains a material inference, not a named rubric point.
- Q0024 formal 2025东城二模 Q20 source was found and confirms the 2+4+2 structure. This upgrades ClaudeCode's LOW_EVIDENCE to source-backed NEEDS_FIX because the desktop entry still lacks independent fields and exact evidence-level labels.
- Q0025 2024朝阳一模 Q21 PPTX confirms the 4+5 structure. It also confirms that the row is mixed 必修二 + 选必一 and requires module-boundary repair.

## Source Backcheck

| source_id | source file | role in this slice | evidence |
|---|---|---|---|
| SRC_RUBRIC_2026_TONGZHOU_YIMO_Q19 | /Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026通州一模/细则/26 通州一模评标.pdf | formal marking material for Q19 | extracted page 12: measures/knowledge 4分 + material analysis/function 4分; available knowledge includes 时代主题, 共同利益, 多边贸易体制, 经济全球化方向, 正确义利观, 国际关系民主化, 共商共建共享, 人类命运共同体, 中国特色大国外交 |
| SRC_RUBRIC_2026_XICHENG_QIMO_Q20 | /Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026西城期末/细则/细则.pdf | formal scoring reference for Q20 | rendered page 4-5: role/practice 2分; why participate 3分 with 4 choose 3; effects 3分 |
| SRC_RUBRIC_2024_HAIDIAN_ERMO_Q18_DOCX | /Users/wanglifei/Desktop/2024模拟题/海淀二模/细则/细则.docx | formal answer/scoring text for Q18 | extracted lines 46-48: Q18(1) can answer from 时代主题, 世界多极化, 人类命运共同体, 国际组织; no fixed point for 霸权主义/强权政治 found |
| SRC_RUBRIC_2025_DONGCHENG_ERMO_Q20 | /Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025东城二模/细则/细则.pdf | formal rubric for Q20 | extracted page 4-5: first layer background 2分; broad disciplinary background only 1分; second layer spirit 4分; third layer action 2分 |
| SRC_RUBRIC_2024_CHAOYANG_YIMO_Q21_PPTX | /Users/wanglifei/Desktop/2024模拟题/2024朝阳一模/细则/细则.pptx | formal rubric/marking PPTX for Q21 | extracted slides 48-49: economic situation 4分; opening a new situation 5分 from political multipolarity and economic globalization dimensions |

## Entry Findings

### Q0021 / doc_order 21 / 2026通州一模Q19

- merged_status: NEEDS_FIX
- Codex qualification: Formal marking material was found, so this is not merely unlocated. It confirms ClaudeCode's core concern: "和平与发展时代主题" is only one of many available knowledge items, not an independent must-score point.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Mark the source as "knowledge/measures 4分 + material function 4分"; label "和平与发展" as optional available knowledge, not a standalone core. Rebuild the same-question group from the rubric, not from a ten-item bucket union.

### Q0022 / doc_order 22 / 2026西城期末Q20

- merged_status: NEEDS_FIX
- Codex qualification: Source page confirms a 2+3+3 scoring structure, but not exactly the desktop row's simplified "是什么-为什么-效果" text. The "why" layer has 4 choose 3: international background, common interests, Chinese concepts, and international obligations. The desktop row also mixes 必修二 terms in the role/practice layer.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 NEEDS_FIX; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 NEEDS_FIX.
- repair needed: Fix the prompt title/book name and score display; split the source layers accurately; mark "和平发展合作共赢是时代潮流/非传统安全威胁" as 角度2内1分 option; move or boundary-label 绿色发展/新发展理念/有为政府/有效市场.

### Q0023 / doc_order 23 / 2024海淀二模Q18(1)

- merged_status: LOW_EVIDENCE
- Codex qualification: Formal source exists, but it supports only broad available angles. It does not make "霸权主义和强权政治、单边主义" a named scoring term for this question. The desktop row's self-warning that this is a level essay and not a fixed point is correct.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 LOW_EVIDENCE; 来源 LOW_EVIDENCE; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Either change the core to a source-listed angle such as 世界多极化/全球治理民主化, or label "霸权主义/强权政治" as material-inference expression only. Keep the level-essay evidence label.

### Q0024 / doc_order 24 / 2025东城二模Q20

- merged_status: NEEDS_FIX
- Codex qualification: Formal source was found and confirms the desktop row's broad 2+4+2 structure. The exact background layer is "国际局势变乱交织、局部动荡不断、面临诸多问题和挑战" for 2分, with broad disciplinary background such as 和平与发展/世界多极化 only 1分. The current core label is too loose and lacks source position.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 PASS; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 PASS.
- repair needed: Replace the core phrase with the formal background-layer wording, or explicitly label the current "百年变局与外部风险挑战" as a container. Add 细则位置: Q20 小论文第一层 背景2分; broad disciplinary background 1分 fallback.

### Q0025 / doc_order 25 / 2024朝阳一模Q21

- merged_status: NEEDS_FIX
- Codex qualification: Formal PPTX confirms 4+5. It also confirms the entry is a mixed economic-situation/opening question. The desktop row currently pulls the 1分 "外部环境日趋严峻、风险挑战增多" economic-situation point into the 选必一时代背景 bucket and carries 必修二 material across the same group without boundary labels.
- field result: 术语/核心采分点 NEEDS_FIX; 完整设问 PASS; 细则位置 NEEDS_FIX; 来源 NEEDS_FIX; 材料触发 PASS; 答案句 NEEDS_FIX; 同类项合并 PENDING_BOOK_LEVEL; 模块边界 NEEDS_FIX.
- repair needed: Mark the first 4分 economic-situation layer as mixed/mostly 必修二. Keep only the 选必一-relevant political multipolarity and genuine economic-globalization items in the main table; boundary-label 高水平对外开放, 双循环, 超大规模市场, 新发展理念, 高质量发展.

## Slice Acceptance

- entries reviewed this slice: 5
- field rows reviewed this slice: 40
- PASS rows added: 16
- NEEDS_FIX rows added: 17
- LOW_EVIDENCE rows added: 2
- PENDING_BOOK_LEVEL rows added: 5
- full-book status: IN_PROGRESS

Next minimal step: prepare and run slice 006 for doc_order 26-30, keeping source backcheck and ClaudeCode traces separate.
