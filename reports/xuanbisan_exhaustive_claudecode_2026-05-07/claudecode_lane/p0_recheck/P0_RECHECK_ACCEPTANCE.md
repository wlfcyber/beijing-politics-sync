# P0 复核验收 - Codex corrected

## 总量核验

- P0 rows 总数：**19**
- CSV 行宽：已由 Codex 修复，所有数据行均为 12 列。
- JSONL 行数：**19**
- can_enter_fusion：`{'yes': 19}`

## decision 分布

`{'confirmed': 6, 'confirmed_with_patch': 13}`

## evidence_level 分布

`{'A-formal': 15, 'A-support': 3, 'B-choice-signal': 1}`

## Codex 纠偏

- `Q-2026顺义一模-19-1`：ClaudeCode 误判 source_insufficient；Codex 回源到 `2026顺义一模细则.pptx::SLIDE8`，确认有完整三段论推论和阅卷细则，已改为 `confirmed_with_patch / A-formal / can_enter_fusion=yes`。
- `Q-2026顺义一模-19-2`：ClaudeCode 误称细则空；Codex 回源到 `SLIDE9`，确认三性参考答案与分值结构，已恢复 A-formal。
- `Q-2025东城期末-18-2`：Codex 回源到 `2025东城期末细则.pptx::SLIDE29`，确认正式阅卷细则，已恢复 A-formal。
- `Q-2026通州期末-19-2`：Codex 回源到 `2026通州期末细则.pptx::SLIDE4-5`，确认正式细则，已恢复 A-formal。

## 残留缺口

- `source_insufficient`：0
- `wrong_framework`：0
- `block_from_student_body`：0
- `downgrade_to_index`：0
- 仍需后续融合阶段处理的提示：2026东城期末 Q17(2) 主张2 可另加“必要条件假言推理”辅助节点；丰台一模 Q18(2) 学生稿仍需回原图补题面背景。

## 边界声明

- 是否生成 Word：**no**
- 是否生成 PDF：**no**
- 是否授权终稿 / final / PASS / 最终版 / 宝典成品：**no**
- 是否覆盖前面批次 / delivery：**no**
- 本报告只证明 P0 回源复核修补闭合，不代表全书终稿或 Word/PDF 交付。
