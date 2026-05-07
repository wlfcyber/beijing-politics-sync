# Codex 套卷批次计划

Status: `IN_PROGRESS_NOT_FINAL`

本计划根据 `QUESTION_COVERAGE_MATRIX.csv` 的 534-row 当前判定生成，用来监督 ClaudeCode 小批次，不是学生稿结构。

## Batch01 海淀/西城

已启动 ClaudeCode PID `31540`。

- `S-2025海淀二模`: total 4, 入正文 3, blocked 0
- `S-2025海淀期末`: total 34, 入正文 4, 同类索引 11, blocked 15, excluded 4
- `S-2024海淀二模`: total 24, 入正文 3, blocked 12, excluded 9
- `S-2025西城二模`: total 34, 入正文 4, 同类索引 10, blocked 14, excluded 6
- `S-2024西城一模`: total 26, 入正文 5, blocked 17, excluded 4

验收要求：本批必须生成 `QUESTION_DECISIONS.csv`、`MAIN_THINKING_LEDGER.csv`、`CHOICE_TRAP_LEDGER.csv`、`FRAMEWORK_NODE_MATRIX.csv`、`BLOCKED_OR_BOUNDARY.md`、`suite_reports/`、`entries/`。

## Batch02 朝阳

- `S-2024朝阳一模`: total 23, 入正文 5, blocked 13, excluded 5
- `S-2024朝阳二模`: total 24, 入正文 4, blocked 14, excluded 5
- `S-2024朝阳期中`: total 22, 入正文 6, blocked 10, excluded 6
- `S-2026朝阳期中`: total 31, 入正文 7, 同类索引 6, blocked 10, excluded 8

## Batch03 东城

- `S-2025东城期末`: total 54, 入正文 5, 同类索引 30, blocked 7, excluded 12
- `S-2026东城一模`: total 31, 入正文 2, 同类索引 8, blocked 13, excluded 8
- `S-2026东城期末`: total 30, 入正文 3, 同类索引 5, blocked 11, excluded 11

## Batch04 丰台/顺义/通州

- `S-2025丰台期末`: total 46, 入正文 5, 同类索引 23, blocked 13, excluded 5
- `S-2026丰台一模`: total 6, 入正文 5, blocked 0, excluded 0
- `S-2025顺义一模`: total 92, 入正文 4, 同类索引 69, blocked 10, excluded 9
- `S-2026顺义一模`: total 24, 入正文 6, blocked 11, excluded 7
- `S-2026通州期末`: total 29, 入正文 6, 同类索引 7, blocked 11, excluded 5

## 监督口径

- `blocked` 不是删除，必须说明题面、选项、答案、细则、视觉核读或模块边界缺口。
- `同类索引` 不是正文题量，必须说明为什么不单独入正文。
- ClaudeCode 若 10 分钟无业务文件增长，下一轮改用单 suite prompt。
