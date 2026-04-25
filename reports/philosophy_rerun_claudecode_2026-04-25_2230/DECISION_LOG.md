# DECISION_LOG — 必修四哲学 Claude Code 重跑版

## 2026-04-25 22:30 本轮启动
- 切换为 cache-first 模式：在所有重跑工作开始前已读 `CACHE_FIRST_DIRECTIVE.md`、`README.md`、`manifest.csv` 头部、`gpt_suite_bundles` 列表。
- 不批量重新转换原始 Word/PDF/PPT；仅当具体证据无法从缓存判定时回退到 raw 文件并在此记录。

## 2026-04-25 22:35 角色降级
- 决定不在主 Claude Code 会话内为各角色创建独立 subagent。
- 原因：
  - 本轮真正瓶颈是证据核定与 Word 渲染；
  - 多 subagent 并行写同一控制文件会引发覆盖冲突；
  - 主线程串行执行更易保留 STEP 配对推进与 governor 否决链；
  - subagent 内部不能直接写 SOURCE_LEDGER 与 COVERAGE_MATRIX 之外，再写入会增加合并工作。
- 降级方案：以"角色契约 + 角色报告 Markdown 文件"代替；本主线程在不同 STEP 显式切换角色身份，并各自负责约定写入域。

## 2026-04-25 22:40 v2 框架定位
- 旧框架 `必修四哲学材料-知识触发总框架_持续更新版_v2.md` 与旧错肢库属于飞哥政治庄园的延续资产。
- 本轮把 v2 视为对照基线：每条进入 Word 成品的内容必须能在 cache 或 raw 文件证据上重新核定；不允许照抄 v2 中没有可复核来源的条目。

## 2026-04-25 22:45 边界已知项
- `2026石景山期末`：用户已明确无评分细则，仅 `2026北京石景山高三（上）期末政治.pdf` 第 9-10 页含答案及评分参考；按 `reference-only` 处理。
- `2025海淀期中`：用户已明确无哲学题，按 `module-boundary-excluded` 处理。
- `2024 各区一模分类汇编`：4 份 docx + 1 份 doc 是按模块汇编的题集，不是独立套卷，按 `inventory-only` 处理。
