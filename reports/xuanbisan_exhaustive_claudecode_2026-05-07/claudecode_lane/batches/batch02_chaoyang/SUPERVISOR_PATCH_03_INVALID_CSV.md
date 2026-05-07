# Supervisor Patch 03 - Batch02 CSV 转义失效

时间：2026-05-07 13:38

`QUESTION_DECISIONS.csv` 现状：

- 表头为 8 列：`question_id,suite_id,original_qno,question_type,codex_current_decision,claudecode_decision,decision_reason,needs_codex_recheck`
- 但多行 `decision_reason` 含英文逗号且未加 CSV 引号，导致解析后 `needs_codex_recheck` 被理由文本污染。
- 典型污染行包括但不限于：
  - `Q-2024朝阳一模-6`
  - `Q-2024朝阳一模-20-1`
  - `Q-2024朝阳二模-2`
  - `Q-2024朝阳期中-7`
  - `Q-2026朝阳期中-12`

纠偏要求：

1. 不能用手写逗号拼接 CSV。
2. 重写正式 CSV 时必须使用结构化 CSV 写入器，或确保所有含逗号/引号/换行的字段正确转义。
3. `needs_codex_recheck` 列只允许 `yes/no`，不得出现理由文本。
4. `decision_reason` 必须完整保留，不得因为修 CSV 而截断证据理由。
5. 本 CSV 修正未完成前，Batch02 不能进入融合。

Codex 监管结论：Batch02 当前状态追加为 `INVALID_CSV_QUOTING`。
