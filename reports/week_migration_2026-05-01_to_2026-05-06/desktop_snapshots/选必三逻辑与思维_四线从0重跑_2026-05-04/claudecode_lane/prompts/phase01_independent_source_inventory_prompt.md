# ClaudeCode Phase 01 Prompt

你是本轮飞哥政治庄园四线工作流中的 `ClaudeCode 20x` 生产 lane B。你是独立生产 workhorse，不是 reviewer，也不是 Codex 的附属摘要器。

## 工作目录

`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`

你不是独自在工作区里工作。不要回滚、删除、覆盖 Codex 或用户已有文件。你只写 `claudecode_lane/`、`04_suite_reports/claudecode_suite_reports/`、`05_coverage/` 中明确属于 ClaudeCode 的文件。

## 必读文件

1. `MASTER_REQUIREMENTS.md`
2. `USER_FRAMEWORK.md`
3. `00_control/NOTEBOOK_DIGEST.md`
4. `/Users/wanglifei/.codex/skills/feige-politics-garden/SKILL.md`
5. `/Users/wanglifei/.codex/skills/feige-politics-garden-book-orchestrator/SKILL.md`
6. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/SKILL.md`
7. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md`

## 本轮用户要求

- 内容质量必须对标已成功的哲学宝典。
- 思维部分要完全模仿哲学宝典：每一个思维和方法都像哲学的原理方法论一样处理。
- 不能只写框架或摘要，必须穷尽每一道题。
- 推理部分要先分类题型，再把所有题放在对应题型下面。
- 旧稿只用于定位源材料和查漏，不继承结论。

## Phase 01 任务

先只做独立源材料盘点和候选题定位，不生成最终学生版。

1. 扫描以下 source roots：
   - `/Users/wanglifei/Desktop/北京高考政治`
   - `/Users/wanglifei/Desktop/2024模拟题`
   - `/Users/wanglifei/Desktop/2025模拟题`
   - `/Users/wanglifei/Desktop/2026模拟题`
   - `/Users/wanglifei/GaokaoPolitics/2025各区模拟题`
2. 定位用户上传的两份框架 PDF 或其本轮可用副本：
   - `逻辑与思维 思维部分 原文件`
   - `逻辑与思维 推理部分（原文件）`
3. 对每个候选源标注：
   - 年份、区、阶段、文件类型
   - paper / answer / rubric / lecture / framework / old_artifact_locator
   - 思维部分候选、推理部分候选、边界排除、待回源
   - 是否需要 OCR/渲染/表格/图片/扫描处理
4. 对旧线文件只能标注为 `old_artifact_locator` 或 `old_failure_reference`，不能作为证据。

## 输出文件

必须写：

- `claudecode_lane/progress.md`
- `claudecode_lane/source_inventory_phase01.csv`
- `claudecode_lane/thinking_candidate_phase01.md`
- `claudecode_lane/reasoning_candidate_phase01.md`
- `claudecode_lane/source_gap_and_blockers_phase01.md`
- `04_suite_reports/claudecode_suite_reports/phase01_inventory_report.md`

## 禁止

- 禁止写最终学生版。
- 禁止声称“已穷尽”。
- 禁止把普通参考答案叫正式细则。
- 禁止把上一版内容当结论。
- 禁止因为某个 PDF 工具不可用就放弃，必须尝试替代处理或记录具体 blocker。

完成后在 `claudecode_lane/progress.md` 写清下一步建议：哪些源应优先回源、哪些套卷必须先处理、哪些题型最可能漏。
