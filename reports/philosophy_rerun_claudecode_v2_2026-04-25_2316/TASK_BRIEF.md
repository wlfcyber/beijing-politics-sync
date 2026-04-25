# TASK_BRIEF — 必修四哲学 Claude Code v2（保留 Codex 形式）

## 任务来源
用户在 2026-04-25 反馈：上一轮 Claude Code 生成的 `C:\Users\Administrator\Desktop\哲学大框架_ClaudeCode重跑版.docx` 被改成了较压缩的讲义式结构（"核心判断 / 当材料里出现 / 典型给分材料 / 答题路径"），不符合 Codex 教研沉淀框架的呈现风格。本轮必须保留 Codex 母版的"持续更新框架"形式。

## 母版
`C:\Users\Administrator\.codex\skills\feige-politics-garden\assets\current-artifacts\必修四哲学材料-知识触发总框架_持续更新版_v2.md`

母版可以做：补证据、纠错、重排、增加边界说明。
母版不能做：换成讲义结构、把多个来源条目压缩成几个典型例子、删除已有证据条目、把"持续更新框架"改成"学生讲义"。

## 主交付（必交付）
- `C:\Users\Administrator\Desktop\哲学大框架_ClaudeCode重跑版_v2_保留Codex形式.docx`
  - 章节顺序：标题与元信息 → 使用规则 → 已纳入试卷 → 课件总框架（便于后续增量更新时对齐）→ 触发总表 → 附录：套卷级三线闭环记录 → 覆盖矩阵与证据边界。
  - 触发总表必须保留母版四行体例：
    1. **来源**：<套卷> 第<题号>（`<细则/阅卷报告/讲评来源>`）
       - 材料信息：……
       - 触发知识：……
       - 逻辑链：……
  - 不允许出现 `可替代`、`反向筛查`、`教学提醒` 三类节标题。
  - 不允许把主框架替换为"核心判断 / 当材料里出现 / 答题路径"等讲义形式（仅可作为可选附录）。
  - 渲染必须可读，无乱码、无窄竖排表格、无空白异常页。

## 同时生成
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\philosophy_rerun_claudecode_v2_2026-04-25_2316\哲学大框架_保留Codex形式.md` — Word 的来源 Markdown，必须与 Word 同结构同内容。

## 控制文件
本 run 目录内必须维护：
- `TASK_BRIEF.md`、`USER_FRAMEWORK.md`、`DEVELOPMENT_PLAN.md`、`PROGRESS.md`、`ROLE_CONTRACTS.md`、`THREAD_REGISTRY.md`、`SOURCE_LEDGER.csv`、`COVERAGE_MATRIX.csv`、`DECISION_LOG.md`、`HANDOFF_QUEUE.md`、`GOVERNOR_CHECKLIST.md`、`FINAL_ACCEPTANCE_REPORT.md`
- `threads/决策者.md`、`threads/监管者.md`、`threads/补丁者.md`、`threads/劳动者.md`、`threads/自动化检测者.md`

## 范围
- 三年北京模拟题：`2024各区模拟题`、`2025各区模拟题`、`2026各区模拟题`，55 个 suite_key，173 个源文件。
- 缓存：`C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus`。

## 缓存优先
1. 读 `manifest.csv` / `gpt_index.jsonl`；
2. 套卷级证据用 `gpt_suite_bundles\*.md`；
3. 单文件级证据用 `gpt_sources\*.md`；
4. 扫描 PDF 用 `renders\<hash>\page_*.png`；
5. 缓存看不懂、不完整、图不清、文本乱、或不足以做证据判断时回原文件，并在 `DECISION_LOG.md` 写明：查了哪个缓存、为什么不够、打开了哪个原文件、确认了什么证据。
6. 不允许在没有读缓存前批量重新转换原始文件。

## 角色（不存在"资料组织者"）
- 决策者：定优先级、批次、停止条件，防止只做几套卷就停。
- 劳动者：处理缓存与原文件证据，重跑哲学相关题；资料清点为劳动者前置工作。
- 补丁者：检查"一题多哲学点"漏归类。
- 监管者：按来源、题号、评分依据、逻辑链、覆盖矩阵严格验收，可否决。
- 自动化检测者：检查计划/进度、来源台账、覆盖矩阵、最终报告与 Word 渲染一致性。

## 完成判据
- SOURCE_LEDGER.csv 覆盖所有 relevant source files；
- COVERAGE_MATRIX.csv 覆盖所有 relevant philosophy questions（或为非哲学题写明排除原因）；
- 所有 included 主观题都有评分来源；
- 所有 included 条目都有来源套卷与题号；
- 补丁者已检查多答题点漏归类；
- 监管者无 unresolved veto；
- Word 已生成并渲染检查；
- FINAL_ACCEPTANCE_REPORT.md 最后一行只有 `TASK_COMPLETE`。

## 反作弊
- 母版结构不允许被讲义结构替换；
- 普通参考答案不能冒充评分细则；
- evidence-insufficient 不能写为已完成；
- STEP_XX 必须配对推进，不允许结尾一次性勾完。
