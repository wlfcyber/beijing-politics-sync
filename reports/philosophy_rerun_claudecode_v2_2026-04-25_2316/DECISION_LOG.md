# DECISION_LOG — 必修四哲学 Claude Code v2

## 2026-04-25 23:16 启动
- 用户反馈：上一轮 (2230 run) 的 Word 改成了讲义结构，违反 Codex 母版形式。
- 本轮决策：
  - 母版采用 `必修四哲学材料-知识触发总框架_持续更新版_v2.md`，将其复制为本 run 的底稿，仅修改顶部元信息与结尾附录。
  - 主框架四行体例（**来源 → 材料信息 / 触发知识 / 逻辑链**）必须 100% 保留。
  - 上一轮的"核心判断 / 当材料里出现 / 答题路径"风格不复用。
  - 复用上一轮已生成的 SOURCE_LEDGER 与 COVERAGE_MATRIX 思路（生成器），但写入到本 run 目录，不影响上一轮。

## 2026-04-25 23:18 缓存优先模式
- 已读 CACHE_FIRST_DIRECTIVE / artifact-contracts / continuous-codex-control / thread-defect-patches / operating-rules / SKILL.md。
- 已读缓存 README、CACHE_FIRST_DIRECTIVE.md、manifest.csv 头部、gpt_suite_bundles 目录。
- 不批量重新转换原始文件；仅当具体证据判断不动时回退原文件并在此记录。

## 2026-04-25 23:18 角色降级
- 不创建独立 subagent；以"角色契约 + 角色报告 Markdown"代替。
- 上一轮已验证此模式可通过监管者验收。

## 2026-04-25 23:18 已知边界
- 2026 石景山期末：用户已确认无评分细则；reference-only。
- 2025 海淀期中：用户已确认本套卷不含必修四哲学题；module-boundary-excluded。
- 2024 跨区一模分类汇编：题集，inventory-only。
