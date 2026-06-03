# Boundary / Excluded 边界与排除汇总

- status: 本文件汇总本 run 中被 B 线判 `excluded` 或 `blocked` 的 question 行，给出原因与后续处理建议。详情可对照 `COVERAGE_MATRIX.csv` 的 `decision`、`blocked_reason` 与 `framework_node_or_reasoning_family` 字段。
- 总数: 30 excluded + 1 blocked + 3 index（B-choice-signal index 三条已在各自 reasoning_choice entry 中以 `decision=index` 标出）。

## blocked(1 条)

| Q | 套卷 | 题号 | 缺什么 | 处理 |
| --- | --- | --- | --- | --- |
| Q0030 | 2024北京高考 | 19(2) | 缺正式细则/评标，本机 run 内不可用 | 待用户提供正式细则后再开题；不进 student body；不冒充 A-formal。 |

## excluded(30 条)

按原因归类：

### A. 思维选择题(user scope confirmed)

按用户范围与硬规则记事本第十五条，思维选择题默认不进入思维宝典正文，也不挂到推理册正文：

- Q0004 / Q0017（通州期末 11、9 choice_trap）
- Q0032 / Q0034 / Q0035 / Q0036（2026顺义一模 3/5/6/7）
- Q0037 / Q0039 / Q0040（2026朝阳一模 3/6/7）
- Q0074（2024石景山一模 6）
- Q0077 / Q0078（2024西城一模 12/13）
- Q0079（2024朝阳一模 7）
- Q0086 / Q0087 / Q0092（2024顺义二模 3/5/2）
- Q0090（2024丰台一模 10）
- Q0095 / Q0099（2026门头沟一模 5/7）
- Q0103（2026石景山一模 2）
- Q0108 / Q0110（2025丰台二模 12/14）
- Q0118 / Q0120（2026朝阳二模 5/7）
- Q0122（2026海淀二模 3）
- Q0131（2026西城二模 6）
- Q0133（2026石景山二模 6）
- Q0136（2026顺义二模 5）

理由统一为 `out_of_thinking_handbook_scope_user_confirmed`。如 Codex 在 fusion 阶段判定其中某条具备稳定推理形式且证据等级允许，可单独申请改挂为 reasoning_choice body，但需要在 fusion_candidates 写明 add_framework_node_mount 或 keep_as_index。

### B. B-compilation(无独立区卷正式细则)

- Q0070（2024房山一模 20(1)）：分类汇编孤证，缺原区正式题源/细则对应关系，按 hard-rule notebook 第二条不作独立证据。

## index(3 条)

详见 `entries/reasoning_choice.jsonl` 中以 `INDEX` 后缀命名的三条：

- `RC-2026-HAIDIAN-2MO-Q4-INDEX` (Q0123)
- `RC-2026-SHUNYI-2MO-Q6-INDEX` (Q0137)
- `RC-2026-SHUNYI-2MO-Q7-INDEX` (Q0138)

理由统一为 `b_choice_signal_audit_field_only_not_student_body`。

## 后续处理建议

- blocked 条目的解锁前提：用户提供 2024 北京高考 19(2) 的正式细则或评标。
- excluded 思维选择题的处理：保留在 COVERAGE_MATRIX 中作为审计可追溯条目；不进入任何 student body；如有教学价值，可考虑出现在“边界陷阱”附录而非正文。
- B-compilation 条目的处理：如未来用户提供该区原卷与正式细则，可重开 Q0070；目前继续 excluded。
