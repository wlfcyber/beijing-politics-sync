# Batch02 朝阳受控融合输入验收说明

结论：本目录是 Codex 受控融合输入，不是终稿，不授权 Word/PDF。

## 来源

- `QUESTION_DECISIONS.csv`: 来自 Codex 对 ClaudeCode Batch02 破损 CSV 的机械转义修复。
- 厚内容 ledgers: 来自 ClaudeCode Batch02 原始厚内容输出。
- `entries/batch02_entries.jsonl`: 由 Codex 从厚内容 ledgers 机械打包。

## 统计

- 判定表数据行：90
- 入正文：20
- 同类索引：2
- blocked：2
- excluded：66
- entries：32（{'subjective': 20, 'choice': 12}）

## 限制

- 原 ClaudeCode Batch02 的 `QUESTION_DECISIONS.csv` 仍保留为破损原件，本目录只作为融合可读版本。
- 因 Batch02 原件仍缺正式 entries 和 suite reports，后续融合必须引用本目录并保留来源说明。
- 学生正文必须从 ledgers/entries 再做框架化改写，不能直接复制审计文档。