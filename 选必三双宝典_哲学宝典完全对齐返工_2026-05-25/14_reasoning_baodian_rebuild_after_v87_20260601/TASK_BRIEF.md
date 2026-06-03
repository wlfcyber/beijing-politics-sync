# TASK_BRIEF

- run: `14_reasoning_baodian_rebuild_after_v87_20260601`
- created_at: 2026-06-01T00:20:00+08:00
- trigger: 用户否定 V87 推理“最终版”，要求重做。
- scope: 只处理选必三《逻辑与思维》推理宝典；不改思维宝典。

## User Requirement

V87 的问题不是个别格式，而是宝典形态失败：它把回源摘录包当成学生推理宝典。此 run 必须撤回 V87 final 口径，以 V17 学生化推理宝典为主体，用 V87 逐条回源表只做源题、答案、细则纠错补丁。

## Inputs

- 学生化主体：`07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.docx`
- 学生化 PDF：`07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.pdf`
- V17 QA：`09_external_review/PHILOSOPHY_CONTENT_V17_REASONING_CHOICE_DENSITY_QA_20260526.md`
- V87 回源核验表：`13_reasoning_clean_redo_20260531/qa/ORIGINAL_SOURCE_LINE_BY_LINE_VERIFY_20260531.csv`
- V87 自查：`13_reasoning_clean_redo_20260531/qa/SELF_CHECK_AFTER_USER_REJECTION_20260601.md`

## Output Contract

交付桌面短路径：

- `选必三推理宝典_重做版_20260601.docx`
- `选必三推理宝典_重做版_20260601.md`
- `选必三推理宝典_重做版_20260601.pdf`，若 PDF 与 DOCX 内容一致且可复用或可导出
- `选必三推理宝典_重做版_自查验收_20260601.md`

不得称 GPT/Claude 外审 PASS；不得称终极版，除非真实外审和完整视觉 QA 另行通过。
