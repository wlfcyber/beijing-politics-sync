# ROLE_CONTRACTS — 必修四哲学 Claude Code 重跑版

本轮在单一 Claude Code 主线程中以"角色契约"形式执行多角色，不存在"资料组织者"角色。

## 决策者
- 写入范围：`HANDOFF_QUEUE.md`、`DECISION_LOG.md`。
- 职责：定义本轮处理对象的优先级、批次划分、停止条件；防止只做几套卷就停。
- 决策约束：必须在批次启动前指明该批次目标套卷与目标题号；批次结束后必须写下下一批次。
- 退出条件：所有 55 套卷在 COVERAGE_MATRIX 都被打上终态。

## 监管者
- 写入范围：`GOVERNOR_CHECKLIST.md`、`FINAL_ACCEPTANCE_REPORT.md`。
- 职责：按"飞哥的政治庄园"操作规则与 artifact-contracts 严格验收。
- 否决条件（任意一条命中即否决）：
  - 一个 relevant 套卷未分类；
  - 一道主观题作为 included，但缺评分来源；
  - 一条材料-原理链缺来源套卷或题号；
  - 套卷被排除但未写排除原因；
  - Word 文件未渲染检查；
  - 出现 `可替代/反向筛查/教学提醒` 字样；
  - 普通参考答案被写成评分细则；
  - 计划/进度/台账/矩阵之间数值或状态冲突且未解释。
- 必须出具 pass / fail / blocked 的终审结论。

## 补丁者
- 写入范围：`threads/补丁者.md`、`DECISION_LOG.md`。
- 职责：在劳动者每完成一批后，专门检查"一个材料触发多个哲学点但只挂在一个节点"的漏项。
- 必须输出：补丁清单（题号 + 缺挂的原理 + 证据来源 + 是否成功补入框架）。

## 劳动者
- 写入范围：`SOURCE_LEDGER.csv`、`COVERAGE_MATRIX.csv`、`threads/劳动者.md`。
- 资料清点是劳动者的前置工作（不存在独立资料组织者）。
- 职责：
  - 按缓存优先原则读 `gpt_suite_bundles\*.md`、`gpt_sources\*.md`、`renders\<hash>\page_*.png`、`texts\*.txt`；
  - 缓存不足以判证据时，回原始文件并在 DECISION_LOG.md 记录；
  - 把每道相关哲学题落到 COVERAGE_MATRIX，并写明评分来源、材料、触发原理、逻辑链、最终归框位置；
  - 选择题正确项哲学触发也按同结构登记。

## 自动化检测者
- 写入范围：`threads/自动化检测者.md`、`GOVERNOR_CHECKLIST.md`。
- 职责：
  - 比对 DEVELOPMENT_PLAN.md 与 PROGRESS.md 的 STEP_ID 是否完全对齐；
  - 比对 SOURCE_LEDGER.csv 行数与 manifest.csv 行数差异并解释；
  - 比对 COVERAGE_MATRIX.csv 中是否存在未分类行；
  - 检查 Word 已生成、渲染抽样无乱码、不含三类禁用标签；
  - 拒绝任何"未读缓存就批量重新转换原文件"的行为。

## 共同纪律
- 任何角色都不得把 evidence-insufficient 的内容写成已完成。
- 任何角色都不得把普通参考答案当评分细则。
- DECISION_LOG.md 中保留所有"为什么没纳入 / 为什么回退到原文件 / 为什么放弃"的痕迹。
