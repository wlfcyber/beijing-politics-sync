# Prompt For Claude Code V2: Rerun Philosophy While Preserving Codex Framework Style

你上一次生成的 `C:\Users\Administrator\Desktop\哲学大框架_ClaudeCode重跑版.docx` 用户不满意。问题不是“没有做成 Word”，而是你改变了 Codex 原本更适合教研沉淀的呈现形式：你把它改成了较压缩的讲义式结构，例如“核心判断 / 当材料里出现 / 答题路径”。用户明确说更喜欢 Codex 的框架。

现在请重跑一次，但必须保留 Codex 的呈现形式。

## Non-Negotiable Style Requirement

先读：

1. `C:\Users\Administrator\Desktop\claudecode_philosophy_rerun_package\CODEX_PRESENTATION_STYLE_GUIDE.md`
2. `C:\Users\Administrator\.codex\skills\feige-politics-garden\assets\current-artifacts\必修四哲学材料-知识触发总框架_持续更新版_v2.md`

把第 2 个文件当作**母版**。你可以补证据、纠错、重排、增加边界说明，但不能改变它的基本呈现方式。

主文档必须继续采用这种条目结构：

```markdown
1. **来源**：<套卷> 第<题号>（`<细则/阅卷报告/讲评来源>`）
   - 材料信息：...
   - 触发知识：...
   - 逻辑链：...
```

不要把主文档改成以下样子：

- `核心判断`
- `当材料里出现`
- `典型给分材料`
- `答题路径`
- 只保留几个代表例子的讲义

这些东西如果你觉得有用，只能放到附录，不能替代“来源—材料信息—触发知识—逻辑链”的主框架。

## First Read Workflow Rules

读这些规则：

1. `C:\Users\Administrator\.codex\skills\feige-politics-garden\SKILL.md`
2. `C:\Users\Administrator\.codex\skills\feige-politics-garden\references\cache-first-directive.md`
3. `C:\Users\Administrator\.codex\skills\feige-politics-garden\references\artifact-contracts.md`
4. `C:\Users\Administrator\.codex\skills\feige-politics-garden\references\continuous-codex-control.md`
5. `C:\Users\Administrator\.codex\skills\feige-politics-garden\references\thread-defect-patches.md`
6. `C:\Users\Administrator\.codex\skills\feige-politics-garden\references\operating-rules.md`

读缓存说明：

1. `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\CACHE_FIRST_DIRECTIVE.md`
2. `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\README.md`
3. `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\manifest.csv`
4. `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_index.jsonl`

## Output Goal

重新生成：

`C:\Users\Administrator\Desktop\哲学大框架_ClaudeCode重跑版_v2_保留Codex形式.docx`

同时生成对应 Markdown：

`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\philosophy_rerun_claudecode_v2_<timestamp>\哲学大框架_保留Codex形式.md`

控制文件放在同一 run directory：

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

## What To Do Differently From Your Previous Run

1. 不要重新设计文档结构。
2. 不要把大量来源条目压缩成少数“典型材料”。
3. 不要把 Codex 的“持续更新框架”改成普通学生讲义。
4. 不要删除旧框架中已经有证据支撑的条目。
5. 每个知识点下保留多个来源条目；这正是用户需要的教研积累。
6. 对每个新增或保留条目，都写完整四行：来源、材料信息、触发知识、逻辑链。
7. 把你想写的“怎么答题”融入逻辑链，而不是另起一套答题路径栏目。

## Cache Rule

缓存优先，不是缓存唯一。

- 先用 `preprocessed_corpus`。
- 优先读 `gpt_suite_bundles` 和 `gpt_sources`。
- 扫描 PDF 优先用 `renders\<hash>\page_*.png`。
- 如果缓存看不懂、不完整、图不清、文本乱、或者不足以支撑证据判断，回原始 Word/PDF/PPT 查证。
- 回原文件时记录：查了哪个缓存、为什么不够、打开了哪个原文件、确认了什么证据。

## Evidence Rules

- 主观题只能用评分细则、阅卷规则、评标、讲评中明确可作为评分依据的内容。
- 普通参考答案不能冒充评分细则，除非用户明确确认可用。
- 选择题正确项或错肢进入哲学框架时，也必须有来源套卷和题号，并说明为什么属于必修四哲学。
- 非哲学题不要硬塞，写入覆盖矩阵并标注 `module-boundary-excluded`。

## Roles

不要创建“资料组织者”角色。用户指定角色只有：

- 决策者
- 监管者
- 补丁者
- 劳动者
- 自动化检测者

如果 Claude Code 支持真实 agents，就创建这些真实角色并登记到 `THREAD_REGISTRY.md`。如果不支持，创建同名角色报告文件并在 `DECISION_LOG.md` 记录降级。

职责：

- 决策者：按优先级推进，不让任务停在几套卷。
- 劳动者：处理缓存与原文件证据，重跑哲学相关题。
- 补丁者：检查一个材料触发多个答题点但只归入一个框架节点的漏项。
- 监管者：按来源、题号、评分依据、逻辑链和覆盖矩阵验收。
- 自动化检测者：检查计划/进度、来源台账、覆盖矩阵、最终报告和 Word 渲染是否一致。

## Priority

1. 主观题大于选择题。
2. 海淀 > 西城 > 东城 > 朝阳 > 郊区。
3. 有明确评分细则的主观题优先。
4. 选择题只提取哲学相关且可复用的正确项/错肢触发链。

## Required Final Shape

Markdown 和 Word 都必须保留如下主结构：

```markdown
# 必修四哲学材料-知识触发总框架（Claude Code 重跑，保留 Codex 形式）
**最后更新**：...
**用途**：...
**框架来源**：...

## 使用规则
...

## 已纳入试卷
...

## 课件总框架（便于后续增量更新时对齐）
### 一、唯物论
...

## 触发总表
### 一、唯物论
#### 物质决定意识，意识对物质具有能动作用
1. **来源**：...
   - 材料信息：...
   - 触发知识：...
   - 逻辑链：...
```

后面按模块继续：

- 唯物论
- 辩证法
- 认识论
- 历史唯物主义
- 价值观 / 人生观

长篇套卷级复核记录放到附录，不能打断主框架。

## Word Requirements

Word 不是重新设计风格，而是把上述 Markdown 框架转成可读文档：

- 标题层级对应 Markdown。
- 每条 `来源/材料信息/触发知识/逻辑链` 保留为分层段落。
- 不用宽表格承载主体内容。
- 来源索引和覆盖矩阵可以放附录。
- 必须渲染检查，确认无乱码、截断、窄竖排表格、异常空白页。

## Final Acceptance

完成前必须满足：

- `SOURCE_LEDGER.csv` 覆盖 relevant source files。
- `COVERAGE_MATRIX.csv` 覆盖 relevant philosophy questions or excludes non-philosophy questions。
- 所有 included 主观题都有评分来源。
- 所有 included 条目都有来源套卷和题号。
- 补丁者已检查多答题点漏归类。
- 监管者无 unresolved veto。
- Word 已渲染检查。
- `FINAL_ACCEPTANCE_REPORT.md` 最后一行只有 `TASK_COMPLETE`。

## Start

请现在开始，不要只输出计划。先创建 run directory 和控制文件，然后把旧 Codex Markdown 作为母版复制到本轮 Markdown 草稿中。接着读取缓存索引，按优先级重跑证据、补漏和修正。每完成一个最小真实步骤后，更新 `PROGRESS.md` 和 `HANDOFF_QUEUE.md`。
