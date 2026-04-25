# ROLE_CONTRACTS — 必修四哲学 Claude Code v2

本轮在单一 Claude Code 主线程中以"角色契约"形式执行，不存在"资料组织者"角色。降级原因详见 DECISION_LOG.md。

## 决策者
- 写入：HANDOFF_QUEUE.md、DECISION_LOG.md、threads/决策者.md
- 职责：定批次与停止条件；防止只做几套卷就停。

## 监管者
- 写入：GOVERNOR_CHECKLIST.md、FINAL_ACCEPTANCE_REPORT.md、threads/监管者.md
- 否决条件：
  - 未保留母版四行体例；
  - 主框架被讲义结构（核心判断 / 当材料里出现 / 答题路径）替换；
  - 一个 relevant 套卷未分类；
  - 主观题作为 included 但缺评分来源；
  - 触发条目缺来源套卷或题号；
  - Word 未渲染检查；
  - 出现 `可替代 / 反向筛查 / 教学提醒` 节标题；
  - 计划/进度/台账/矩阵冲突且未解释。

## 补丁者
- 写入：threads/补丁者.md、DECISION_LOG.md
- 职责：检查"一题多哲学点"漏归类。

## 劳动者
- 写入：SOURCE_LEDGER.csv、COVERAGE_MATRIX.csv、threads/劳动者.md
- 资料清点为劳动者前置工作。
- 职责：
  - 缓存优先；
  - 缓存不足以做证据判断时回原文件并在 DECISION_LOG.md 记录；
  - 把每道哲学题落到 COVERAGE_MATRIX；
  - 在 Markdown 中保留母版四行体例；
  - 选择题正确项哲学触发也按四行体例登记。

## 自动化检测者
- 写入：threads/自动化检测者.md、GOVERNOR_CHECKLIST.md
- 职责：
  - 比对 DEVELOPMENT_PLAN 与 PROGRESS 的 STEP_ID；
  - 比对 SOURCE_LEDGER 行数与 manifest 行数；
  - 扫描 COVERAGE_MATRIX 状态；
  - Word 渲染抽样校验；
  - 拒绝"未读缓存就批量重新转换原文件"行为；
  - 拒绝主框架被讲义结构替换。
