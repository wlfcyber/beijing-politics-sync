# ClaudeCode 输出 QA

Verdict: `CONTROL_BASE_TERMINAL_CLOSED_BUT_EVIDENCE_BLOCKED`

## 关键问题

- Codex union coverage rows: 534
- ClaudeCode coverage rows: 534
- ClaudeCode pending conclusion rows: 0
- ClaudeCode evidence pending rows: 330
- Missing qids from Codex union: 0
- Suite reports: 17 / expected 17

## ClaudeCode 本轮结论分布

- `blocked`: 336
- `excluded`: 114
- `入正文`: 80
- `同类索引`: 4

## 缺失 qids

- none

## 缺失 suite_reports

- none

## 处理意见

- 若 verdict 仍为 HARD_FAIL，不允许 ClaudeCode 根任务宣称穷尽完成。
- 若 verdict 为 CONTROL_BASE_TERMINAL_CLOSED_BUT_EVIDENCE_BLOCKED，只表示 coverage 四类终态闭合；仍不授权终稿或 Word/PDF。
- evidence_level=pending 的 blocked 行必须保留 blocker，表示缺题面/选项/答案/细则/视觉核读；不得误写为入正文。
- Batch01 还必须补齐厚内容 ledgers、entries、blocked/boundary 文档，不能只交 QUESTION_DECISIONS。