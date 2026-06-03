# 预处理验收报告

- 小本本检查：已创建 `00_飞哥选必二法律与生活要求小本本.md`；本轮脚本不覆盖该文件。
- 覆盖检查：本轮扫描 `54` 套，每套均写入 `SOURCE_MATCH_LEDGER.csv` 并带 `has_xuanbier / no_xuanbier / uncertain / excluded` 状态。
- 跳过检查：确认 `no_xuanbier` `3` 套，写入 `NO_XUANBIER_SUITES.md`。
- 不确定检查：`MISSING_OR_UNCERTAIN.md` 记录 `15` 条套卷/OCR/自动抽题问题。
- 选择题检查：输出 `48` 道；总览句与错项句字段均已填充；其中 `37` 道未自动锁定可靠答案，已单列待核。
- 主观题检查：输出 `37` 道；细则缺失 `0` 道。
- 证据检查：主观题证据类型分布 `{'formal_or_scoring_source': 34, 'reference_answer': 1, 'unknown': 2}`；`reference_answer` 不等同于正式细则。
- 旧线隔离检查：本轮输出声明旧选必二作废；脚本来源只扫原始三年模拟题目录和新目录缓存，不读取旧 `选必二_*.md`。
