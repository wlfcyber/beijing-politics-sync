# Automation Checker - Batch04B 西城预融合

time: 2026-05-03 21:16 CST

verdict: PASS

## 检查结果

- `fusion/scoring_atom_table_batch04B_xicheng_prelim.csv`：18 rows，14 columns，列宽一致。
- `COVERAGE_MATRIX.csv`：23 rows，11 columns，列宽一致。
- `SOURCE_LEDGER.csv`：114 rows，9 columns，列宽一致。
- Batch04B coverage 新增 7 行均有对应 source-ledger 证据来源；主候选有 P0 细则源和 P3 题面源，`2025西城一模 Q18` 保持边界。
- `07_student_doc/` 未检出 Batch04B 新内容关键词：`2026西城一模`、`2025西城一模 Q21`、`2025西城二模`、`2025西城期末`、`2024西城二模`、`2024西城一模`、`零关税`、`反补贴`、`自贸区3.0`。
- 原自动化检测者线程句柄失效且恢复失败，本报告由 Codex 本地按同一检测职责补写；未替代 Governor 或 Confucius。

## 状态边界

- 允许：Batch04B 主候选更新为 `candidate_with_fixes`，继续进入后续东城/朝阳扩展或更大融合。
- 禁止：学生稿发布、Word/PDF、FINAL_ACCEPTANCE、coverage close。
