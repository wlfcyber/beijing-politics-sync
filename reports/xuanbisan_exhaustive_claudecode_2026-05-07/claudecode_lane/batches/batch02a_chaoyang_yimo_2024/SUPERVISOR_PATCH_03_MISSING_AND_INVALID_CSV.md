# Supervisor Patch 03 - Batch02a 缺文件且 CSV 转义失效

时间：2026-05-07 13:40

Batch02a 已从中间文件推进到部分正式文件，但仍不能验收。

当前机器 QA 结论：

- `QUESTION_DECISIONS.csv` 存在 23 条数据行，但至少 2 行字段数不等于表头 8 列，原因是 `decision_reason` 含英文逗号未正确 CSV 转义。
- 缺失：`FRAMEWORK_NODE_MATRIX_SUMMARY.csv`
- 缺失：`entries/batch02a_entries.jsonl`
- 缺失：`suite_reports/*.md` 或正式套卷报告目录
- 缺失：`BATCH02A_ACCEPTANCE.md`
- `PROGRESS.md` 已写“这些文件完成”，但目录证据不支持。

纠偏要求：

1. 立刻用结构化 CSV 写入器重写 `QUESTION_DECISIONS.csv`，不得手写逗号拼接。
2. `needs_codex_recheck` 列只允许 `yes/no`。
3. 补齐 `FRAMEWORK_NODE_MATRIX_SUMMARY.csv`。
4. 补齐 `entries/batch02a_entries.jsonl`，每行必须含：
   `question_id, type, framework_node, material_signal, trigger_logic, answer_sentence, evidence_level, needs_codex_recheck, source_batch`。
5. 建立 `suite_reports/` 并写入 `S-2024朝阳一模.md`；或者如果只保留单文件 `SUITE_REPORT.md`，必须同步写出 `BATCH02A_ACCEPTANCE.md` 并在 acceptance 中说明与标准目录差异。推荐按标准目录写。
6. 不准写 `PASS`、不准写终稿、不生成 Word/PDF。

Codex 监管结论：Batch02a 当前状态为 `PARTIAL_OUTPUTS_WITH_INVALID_CSV_AND_MISSING_FILES`，不能并入融合。
