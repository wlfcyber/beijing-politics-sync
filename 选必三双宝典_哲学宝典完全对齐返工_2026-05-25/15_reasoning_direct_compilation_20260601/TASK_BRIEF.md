# TASK_BRIEF

- run: `15_reasoning_direct_compilation_20260601`
- created_at: 2026-06-01T00:55:00+08:00
- trigger: 用户要求“推理直接做成汇编吧”。
- scope: 只处理选必三《逻辑与思维》推理部分；不改思维宝典。

## Contract

将推理部分交付形态从“宝典”改为“题汇编”：按推理形式和小题型汇总 2024-2026 北京区卷相关主观题与选择题。

正文结构：

- 推理形式
- 小题型/规则位置
- 对应考题
- 题干/材料摘要
- 设问/选项
- 答案/细则要点

## Inputs

- V17 学生化推理稿：`07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.docx`
- V87 高风险源核验：`13_reasoning_clean_redo_20260531/qa/ORIGINAL_SOURCE_LINE_BY_LINE_VERIFY_20260531.csv`
- V88 已核对答案源的学生层正文：`14_reasoning_baodian_rebuild_after_v87_20260601/delivery/选必三推理宝典_重做版_20260601.md`

## Non-goals

- 不再称“推理宝典终极版”。
- 不做原始审计包展示。
- 不宣称 GPT Pro / Claude 真实外审 PASS。
