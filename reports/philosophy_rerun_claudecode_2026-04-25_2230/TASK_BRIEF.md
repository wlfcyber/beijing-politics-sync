# TASK_BRIEF — 必修四哲学 Claude Code 重跑版

## 任务来源
用户在 2026-04-25 指派 Claude Code 接手北京高考必修四哲学研究的重跑工作，作为飞哥的政治庄园工作流的一次完整闭环。本轮目标不是从零重写，而是按"飞哥的政治庄园"流程对必修四哲学的材料—知识触发链做一次新一轮的证据校核、覆盖审计与可读化重组，并产出一份桌面级 Word 成品。

## 主交付（必交付）
- `C:\Users\Administrator\Desktop\哲学大框架_ClaudeCode重跑版.docx`
  - 高三学生取用版的哲学大框架。
  - 结构：封面与使用说明 / 框架总览 / 唯物论 / 认识论 / 辩证法 / 历史唯物主义 / 价值观与人生价值 / 综合题型：材料触发多哲学点 / 高频失分点与审题提醒 / 来源索引 / 覆盖说明与证据边界。
  - 不允许出现 `可替代`、`反向筛查`、`教学提醒` 三类节标题。
  - 渲染必须可读，无乱码、无窄竖排表格、无空白异常页。

## 支撑交付（保留）
本轮 run 目录全部控制文件：
- `TASK_BRIEF.md`
- `USER_FRAMEWORK.md`
- `DEVELOPMENT_PLAN.md`
- `PROGRESS.md`
- `ROLE_CONTRACTS.md`
- `THREAD_REGISTRY.md`
- `SOURCE_LEDGER.csv`
- `COVERAGE_MATRIX.csv`
- `DECISION_LOG.md`
- `HANDOFF_QUEUE.md`
- `GOVERNOR_CHECKLIST.md`
- `FINAL_ACCEPTANCE_REPORT.md`
- `threads/决策者.md`、`threads/监管者.md`、`threads/补丁者.md`、`threads/劳动者.md`、`threads/自动化检测者.md`

可选：补充 Markdown（哲学—文化—错肢交叉证据）。

## 范围与边界
- 涉及套卷范围：`2024各区模拟题`、`2025各区模拟题`、`2026各区模拟题` 三年模拟与期中期末，共 55 个套卷 bundle（见 SOURCE_LEDGER）。
- 必须分类（穷尽不是都纳入）：每个 relevant 套卷都被打上 `included` / `module-boundary-excluded` / `reference-only` / `objective-key-only` / `source-missing` / `ocr-needed` / `duplicate-or-drift` / `blocked` 中的一种。
- 主观题给分依据来源仅限：评分细则、阅卷报告、阅卷总结、阅卷讲评中明确可作给分依据的内容、用户已确认可用的参考答案。
- 选择题正确项哲学触发也并入框架；选择题错肢库在本轮可见但不是主交付。
- 不创建"资料组织者"角色；资料清点由劳动者完成、自动化检测者审核。
- 旧 v2 框架（`必修四哲学材料-知识触发总框架_持续更新版_v2.md`）与旧错肢库可作为对照基线，但每条进入本轮 Word 成品的内容都必须在缓存或原文件证据上重新核定。

## 缓存优先规则
1. 先读 `manifest.csv` / `gpt_index.jsonl` 找到相关源文件。
2. 套卷级别证据用 `gpt_suite_bundles\*.md`。
3. 单文件级证据用 `gpt_sources\*.md`。
4. 扫描型 PDF 用 `renders\<hash>\page_*.png` 读图。
5. 缓存看不懂、不完整、图不清、文本乱、或不足以作出证据判断时，回原始 Word/PDF/PPT 查证，并在 DECISION_LOG.md 记录：查了哪个缓存、为什么不够、打开了哪个原文件、确认了什么证据。
6. 不允许在没有检查缓存前批量重新转换原始文件。

## 角色（不存在"资料组织者"角色）
- 决策者：决定下一批处理对象，防止只做几套卷就停。
- 监管者：按证据、题号、来源、逻辑链、覆盖矩阵严格验收，可以否决。
- 补丁者：检查一个材料触发多个答题点但只归入一个框架节点的漏项。
- 劳动者：按缓存与原文件证据处理所有相关哲学题；资料清点是劳动者前置工作。
- 自动化检测者：检查计划/进度、来源台账、覆盖矩阵、最终报告、Word 渲染结果是否一致。

## 完成判据
- SOURCE_LEDGER.csv 覆盖所有 relevant source files。
- COVERAGE_MATRIX.csv 覆盖所有 relevant philosophy questions（或为非哲学题明确给出排除原因）。
- 所有 included 主观题都有评分来源。
- 所有 included 条目都有来源套卷和题号。
- 补丁者已检查多答题点漏归类。
- 监管者无 unresolved veto。
- Word 已生成并完成渲染检查（PNG 抽样无乱码、无窄竖排表格、无空白异常页）。
- FINAL_ACCEPTANCE_REPORT.md 最后一行只有 `TASK_COMPLETE`。

## 反作弊条款
- 不得把 evidence-insufficient 写成已完成。
- 不得把普通参考答案当评分细则。
- 不得伪造评分点或编造材料触发。
- 计划/进度的 STEP_XX 必须配对推进，不允许结尾一次性全打勾。
- Blocker 必须显性在 DECISION_LOG.md / GOVERNOR_CHECKLIST.md 中保留，而不是擦除。
