# ClaudeCode Prompt: Opus 4.8 Max Dynamic Workflow

你现在是 VS Code ClaudeCode 的正式生产 lane。请使用 Claude Opus 4.8，Max / ultracode / highest effort，并启动 dynamic workflow。关键词：workflow。

在开始内容工作前，先在本 run 写入 `02_claudecode_logs/MODE_CONFIRMATION.md`，记录你能看到或能确认的 model、effort、dynamic workflow 状态。如果不能确认是 Opus 4.8 + Max/ultracode + dynamic workflow，请立即写 `BLOCKED:model_or_workflow_not_confirmed`，不要处理题源。

## Project And Run

Workspace:

`/Users/wanglifei/Desktop/北京高考政治`

Run directory:

`/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/opus48_dynamic_workflow_subjective_compilation_2026-05-29`

## Mandatory Startup Gate

先读这些文件，不得跳过：

1. `/Users/wanglifei/Desktop/北京高考政治/reports/master_governor/latest_master_governor_report.md`
2. `/Users/wanglifei/Desktop/北京高考政治/reports/master_governor/worker_daily_orders.md`
3. `/Users/wanglifei/Desktop/北京高考政治/reports/master_governor/PROJECT_GOVERNOR_THREE_LAYER_SOP.md`
4. `/Users/wanglifei/Desktop/北京高考政治/reports/master_governor/CROSS_BOOK_WORKFLOW_V3_FOR_XUANBIER_XUANBISAN.md`
5. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbier/SKILL.md`
6. `/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/00_飞哥选必二法律与生活要求小本本.md`
7. 本 run 的 `TASK_BRIEF.md`、`DEVELOPMENT_PLAN.md`、`PROGRESS.md`、`00_control/*.csv`、`06_governor/GOVERNOR_CHECKLIST.md`

## User-Locked Requirements

- 只处理 2024、2025、2026 三年北京模拟题中的选必二《法律与生活》法律主观题。
- 源目录只从这里起步：
  - `/Users/wanglifei/Desktop/2024模拟题`
  - `/Users/wanglifei/Desktop/2025模拟题`
  - `/Users/wanglifei/Desktop/2026模拟题`
- 本轮目标是“习题 + 细则汇编”：每一道法律主观题下面附对应细则。
- 用户明确说：所有题均有细则，不可能没有。找不到就继续找，不得把“没找到”写成最终事实。
- 可接受的细则/评分证据包括：正式评分细则、评标、阅卷总结、讲评 PPT/文档、答案变通说明、分题细则、用户确认的评分来源。
- 普通参考答案不能冒充细则，除非文件本身是评分/讲评/评标/阅卷性质或用户确认。
- 旧选必二成果全部作废；旧文件只能作定位线索或错漏对照，不能继承旧结论、旧框架、旧题型表述、旧频次统计或旧正文。
- 可以边整理边思考命题规律和候选框架，但框架只能是 `candidate_framework`，必须从题源和细则反推，不能先定框架。

## Dynamic Workflow Decomposition

请把 workflow 拆成并行但写集隔离的 subagents：

1. `source-inventory-agents`
   - 按年份/区/考试阶段扫描原始文件。
   - 输出 `00_control/SOURCE_LEDGER.csv`。

2. `question-extraction-agents`
   - 找出每一道选必二法律主观题及小问。
   - 每题写一个 `03_source_packets/<question_id>.md`。
   - 保留完整材料、完整设问、题号、页码/位置、原始文件路径。

3. `rubric-search-agents`
   - 为每道题找对应细则/评分证据。
   - 搜索范围要包括同目录、同套卷答案、细则、评标、阅卷、讲评、PPT、Word、PDF、图片、OCR 文本和必要的原始渲染。
   - 写 `00_control/RUBRIC_SEARCH_LEDGER.csv`。
   - 若暂未找到，只能标 `needs_deeper_search`，并写清已搜路径和下一步，不得标最终 missing。

4. `compilation-agents`
   - 生成 `04_outputs/选必二法律主观题_习题与细则汇编_20260529.md`。
   - 生成 `04_outputs/选必二法律主观题_习题与细则汇编_20260529.csv`。
   - 每题结构：
     - 题目编号与来源
     - 完整材料
     - 完整设问
     - 对应细则原文
     - 细则来源与证据类型
     - 本题法律关系/争点/规则要件/事实匹配/责任或程序落点/法治价值

5. `pattern-framework-agents`
   - 只在已有 question/rubric packets 基础上总结规律。
   - 输出 `05_framework_candidate/选必二考题规律与候选框架_20260529.md`。
   - 必须按题号引用证据，不得写成定稿宝典。

6. `verification-agents`
   - 检查旧成果污染、题源遗漏、细则未锁、重复计数、普通答案冒充细则、框架无证据。
   - 更新 `06_governor/GOVERNOR_CHECKLIST.md` 和 `07_acceptance/FINAL_ACCEPTANCE_REPORT.md`。

## Status Rules

- 每完成一个真实产物，再更新 `PROGRESS.md`。
- 不要只说“已完成”，必须写文件。
- 最终只允许输出以下之一：
  - `STEP_DONE:<step_id>`：一个最小完整步骤完成；
  - `BLOCKED:<exact_reason>`：被模型/权限/源文件/细则定位阻塞；
  - `TASK_COMPLETE`：全部 deliverables 与 Governor 验收完成。

## First Required Action

请立即启动 dynamic workflow，但先做 STEP_00：

1. 确认 Opus 4.8 + Max/ultracode/highest effort + dynamic workflow；
2. 写 `02_claudecode_logs/MODE_CONFIRMATION.md`；
3. 然后开始 STEP_01 source inventory。
