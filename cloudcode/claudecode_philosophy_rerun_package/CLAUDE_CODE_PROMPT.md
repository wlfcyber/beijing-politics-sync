# Prompt For Claude Code: Rerun Beijing Gaokao Politics Philosophy Research

你现在接手一个北京高考政治教研任务。请不要把它当作普通总结任务。你要按“飞哥的政治庄园”工作流，重新跑一遍必修四哲学研究，产出可验收的成品。

## First Read These Files

先读这些规则文件：

1. `C:\Users\Administrator\.codex\skills\feige-politics-garden\SKILL.md`
2. `C:\Users\Administrator\.codex\skills\feige-politics-garden\references\cache-first-directive.md`
3. `C:\Users\Administrator\.codex\skills\feige-politics-garden\references\artifact-contracts.md`
4. `C:\Users\Administrator\.codex\skills\feige-politics-garden\references\continuous-codex-control.md`
5. `C:\Users\Administrator\.codex\skills\feige-politics-garden\references\thread-defect-patches.md`
6. `C:\Users\Administrator\.codex\skills\feige-politics-garden\references\operating-rules.md`

再读缓存说明：

1. `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\CACHE_FIRST_DIRECTIVE.md`
2. `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\README.md`
3. `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\manifest.csv`
4. `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_index.jsonl`

## Core Goal

重跑必修四哲学研究，目标是在桌面产出一个高质量 Word 成品：

`C:\Users\Administrator\Desktop\哲学大框架_ClaudeCode重跑版.docx`

同时保留支撑性 Markdown 和验收文件，放在：

`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\philosophy_rerun_claudecode_<timestamp>\`

如果你发现原来哲学框架、错肢库、文化框架之间有交叉证据，也可以生成补充 Markdown，但主交付是哲学大框架 Word。

## Hard Rules

1. **缓存优先，不是缓存唯一。**
   - 先用 `preprocessed_corpus`。
   - 优先读 `gpt_suite_bundles` 和 `gpt_sources`。
   - 扫描 PDF 优先用 `renders\<hash>\page_*.png`。
   - 如果缓存看不懂、不完整、图不清、文本乱、或者不足以支撑证据判断，回原始 Word/PDF/PPT 查证。
   - 回原文件时必须记录：查了哪个缓存、为什么不够、打开了哪个原文件、确认了什么证据。

2. **不要重复批量转换原始文件。**
   - 除非缓存缺失、hash 变化、或针对具体证据必须回原文件，否则不要重新批量转换 Word/PDF/PPT。

3. **不能编造评分细则。**
   - 主观题只能用评分细则、阅卷规则、评标、讲评中明确可作为评分依据的内容。
   - 普通参考答案不能冒充评分细则，除非用户明确确认可用。

4. **每条哲学框架内容必须可追溯。**
   每条结论至少包含：
   - 来源套卷
   - 年份、区、考试阶段
   - 题号
   - 材料信息
   - 评分点或评分依据
   - 从材料到哲学原理/方法论的逻辑链
   - 放入框架的位置

5. **穷尽不是“都写进框架”。**
   穷尽是所有相关套卷/题目都被分类：
   - `included`
   - `module-boundary-excluded`
   - `reference-only`
   - `objective-key-only`
   - `source-missing`
   - `ocr-needed`
   - `duplicate-or-drift`
   - `blocked`

6. **不要创建“资料组织者”角色。**
   用户指定角色只有：
   - 决策者
   - 监管者
   - 补丁者
   - 劳动者
   - 自动化检测者

   资料清点是劳动者的前置工作，自动化检测者负责检查清点是否完整。

## Required Control Files

在本轮 run directory 里创建并维护：

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

`DEVELOPMENT_PLAN.md` 和 `PROGRESS.md` 必须使用相同的 `STEP_XX`。只有完成真实读取、分类、合并、写作、渲染或验证后，才能把步骤标为完成。

## Roles

如果 Claude Code 支持 subagents / task agents，请创建真实角色；不要只在主线程里假装分工。登记到 `THREAD_REGISTRY.md`。

如果当前环境不支持真实 agent，就在 `DECISION_LOG.md` 写明降级原因，并创建独立角色报告文件：

- `threads/决策者.md`
- `threads/监管者.md`
- `threads/补丁者.md`
- `threads/劳动者.md`
- `threads/自动化检测者.md`

职责：

- 决策者：决定下一批处理对象，防止只做几套卷就停。
- 劳动者：按缓存和原文件证据处理所有哲学相关题目。
- 补丁者：检查一个材料触发多个答题点但只归入一个框架节点的漏项。
- 监管者：按证据、题号、来源、逻辑链、覆盖矩阵严格验收。
- 自动化检测者：检查计划/进度、来源台账、覆盖矩阵、最终报告、Word 渲染结果是否一致。

## Priority

处理优先级：

1. 主观题大于选择题。
2. 海淀 > 西城 > 东城 > 朝阳 > 郊区。
3. 有明确评分细则的主观题优先。
4. 选择题只提取哲学相关且可复用的错肢/正确项触发链，除非用户要求完整错肢库。

## Source Roots

原始材料路径：

- `C:\Users\Administrator\Desktop\2024各区模拟题`
- `C:\Users\Administrator\Desktop\2025各区模拟题`
- `C:\Users\Administrator\Desktop\2026各区模拟题`

缓存路径：

- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus`

现有研究库：

- `C:\Users\Administrator\Desktop\beijing_politics_research`

旧哲学成果可作为对照，但不能无验证照抄：

- `C:\Users\Administrator\.codex\skills\feige-politics-garden\assets\current-artifacts\必修四哲学材料-知识触发总框架_持续更新版_v2.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden\assets\current-artifacts\北京高考政治错肢库_持续更新版.md`

## Expected Output Structure

Word 成品建议结构：

1. 封面与使用说明
2. 框架总览
3. 唯物论
4. 认识论
5. 辩证法
6. 历史唯物主义
7. 价值观与人生价值
8. 综合题型：材料如何触发多个哲学答题点
9. 高频失分点与审题提醒
10. 来源索引
11. 覆盖说明与证据边界

不要用过宽大表格塞满 Word。密集中文内容优先用分层段落、短表格、编号块和来源索引。Word 必须渲染检查，不能只生成 docx 就结束。

## Final Acceptance

最终完成前必须满足：

- `SOURCE_LEDGER.csv` 覆盖所有 relevant source files。
- `COVERAGE_MATRIX.csv` 覆盖所有 relevant philosophy questions or clearly excludes non-philosophy questions。
- 所有 included 主观题都有评分来源。
- 所有 included 条目都有来源套卷和题号。
- 补丁者已检查多答题点漏归类。
- 监管者无 unresolved veto。
- Word 已生成并渲染检查，无乱码、截断、窄竖排表格、空白异常页。
- `FINAL_ACCEPTANCE_REPORT.md` 最后一行只有 `TASK_COMPLETE`。

如果仍有 blocker，可以完成分类和边界说明，但不能把 evidence-insufficient 内容说成已完成。

## Start Now

请立即开始，不要只输出计划。先创建 run directory 和控制文件，然后读取缓存索引，推进第一批高优先级套卷。每轮完成一个最小但真实的步骤后更新 `PROGRESS.md` 和 `HANDOFF_QUEUE.md`。
