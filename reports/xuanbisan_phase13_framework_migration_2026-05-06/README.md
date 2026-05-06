# 选必三 Phase13 框架版迁移包

迁移时间：2026-05-06  
本机原工作目录：`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`

## 用途

本目录用于把本轮选必三《逻辑与思维》从 Phase12 clean candidate 到 Phase13 框架版返工的关键材料迁移到 GitHub，方便新线程、新电脑或其他模型继续接力。

## 迁移范围

- `run_control/`：本轮硬性要求记事本、Final Acceptance、progress、四线闭合门、Governor gates、模型建议日志。
- `phase12_clean_candidate/`：77 条学生清洁候选稿、双索引、traceability、build audit、构建脚本。
- `phase12_external_packets/`：给外部 GPT/Claude 审查用的 clean candidate 上传包和 manifest。
- `phase12_gpt_review/`：Phase12 clean candidate 相关 GPT prompt/raw/digest/index；不迁移早期大量截图，以免普通 Git 过度膨胀。
- `phase13_codex/`：Codex 本地按框架轴生成的候选稿、挂载矩阵、审计报告和构建脚本。
- `phase13_claude_cowork/`：Claude Cowork 长 prompt、第二轮内嵌源材料任务状态、Cowork 生成的框架稿、挂载矩阵、review report、patch queue。
- `phase13_claudecode/`：ClaudeCode 可见窗口/终端返工提示词。
- `source_templates/`：哲学宝典结构模板和“与哲学宝典结构对比”文件，用来防止选必三再次退回按大题排序。

## 当前硬结论

- 之前 77 条 clean candidate 虽然内容可用，但正文结构不合格：不能以“主观题/选择题 -> 地区时间 -> 大题”为主体。
- Phase13 必须以框架为主体：`思维类型 -> 思维特点/小方法 -> 固定分析流程 -> 对应模拟题`。
- 推理部分必须以题型为主体：`题型 -> 规则口令 -> 常见陷阱 -> 解题动作 -> 对应模拟题`。
- 地区、年份、题号只作为 traceability 和检索排序，不作为最终宝典正文主轴。
- 本包仍是候选与迁移包，不授权 Word/PDF/final/PASS。

## 同步的技能

本次还同步了本机当前 live skill：

- `skills/feige-politics-garden/`
- `skills/feige-politics-garden-book-orchestrator/`
- `skills/feige-politics-garden-xuanbier/`
- `skills/feige-politics-garden-xuanbisan/`

其中 `feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md` 已写入 2026-05-06 框架版结构硬规则。

## 下一步建议

1. 以 `phase13_claude_cowork/phase13_cowork_framework_rewrite.md` 和 `phase13_codex/phase13_framework_student_candidate.md` 做对照。
2. 先处理 `phase13_claude_cowork/phase13_cowork_patch_queue.csv` 中的 15 个 patch。
3. 再让 GPT-5.5 Pro 与 Claude Opus 4.7 Adaptive 复审“框架轴是否真正像哲学宝典”。
4. 复审通过后，才允许进入最终 clean Markdown，再谈 Word。

