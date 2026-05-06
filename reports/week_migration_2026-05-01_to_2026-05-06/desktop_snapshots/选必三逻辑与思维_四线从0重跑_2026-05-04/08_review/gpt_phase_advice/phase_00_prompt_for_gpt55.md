# Prompt For GPT-5.5 Pro Commander

你是 GPT-5.5 Pro，担任“北京高考政治教研整本书四线工作流”的总指挥和压力测试官。请注意：你不是源证据裁判，不要编造任何本地文件、题目或评分细则。你的任务是审查流程、分工、风险和验收门槛，给 Codex 本地总控一份可执行 commander packet。

背景：

- 用户已成功做过一本“哲学宝典”，质量标准是逐题穷尽、按原理/方法论组织、材料触发点 -> 设问 -> 为什么能想到 -> 答案落点，最终 Word/PDF 经过版式验收。
- 现在要重跑选必三《逻辑与思维》，范围包括“思维部分”和“推理部分”。
- 用户强烈批评上一版：内容质量不能和哲学宝典比，没有穷尽每一道题，推理部分只是分类总结而没有把所有题挂到对应题型下面，而且没有真实执行四线工作流。
- 本轮要求严格四线：Codex 生产 lane A + ClaudeCode 生产 lane B + Claude Opus 教学文本成品化 + GPT-5.5 Pro 内容总审稿/压力测试。Governor 和 Confucius 是最终硬 gate。
- 当前只是启动纠偏阶段，没有最终学生稿。

请基于下面的 Phase 00 summary，输出：

1. STOP / GO / CONDITIONAL GO 判断。
2. Codex lane A 下一步生产任务。
3. ClaudeCode lane B 下一步生产任务。
4. Claude Opus 什么时候可以介入、只能做什么、不能做什么。
5. GPT-5.5 Pro 后续必须审查哪些 trigger objects。
6. 推理部分应如何做成“题型 -> 全部题目 -> 规则口令 -> 易错陷阱 -> 解题步骤”的宝典，而不是题型总述。
7. 你认为最可能导致再次失败的 10 个风险。
8. 必须阻断最终 PASS 的验收 gate。

请尽量具体，给出可执行清单。

---

Phase 00 summary:

```text
phase_name: Phase 00 startup correction
phase_goal: Restore full four-lane workflow for 选必三《逻辑与思维》思维部分 + 推理部分 after the user rejected the previous output as too shallow.
completed_actions:
- Read router skill, whole-book orchestrator skill, whole-book SOP, 选必三 branch skill, hard-rule notebook, and document QA rules.
- Created a fresh run folder for four-lane from-zero rerun.
- Wrote master requirements, user framework, start card, notebook digest, and Codex internal five-role ledgers.
- Started ClaudeCode production lane B with a bounded Phase 01 independent source-inventory task.
- Created Codex source inventory notes and first-pass source ledger.
- Ran Governor startup patch: final PASS is blocked until source inventory, coverage, ClaudeCode, Claude Opus, GPT-5.5 Pro, Governor, Confucius, and Word/PDF validation are real.
unfinished_actions:
- ClaudeCode lane B Phase 01 is still running.
- GPT-5.5 Pro real commander response for this new run is not yet saved.
- Claude Opus real teaching-text lane has not yet run.
- Coverage matrix is not yet populated at suite/question level.
- No final student-facing draft has been produced in this new run.
source_coverage_summary:
- First-pass inventory found raw framework PDFs for 思维部分 and 推理部分.
- The current source ledger intentionally treats old artifacts as locator-only, not evidence.
- Most real exam sources still need reopening and suite/question classification.
non_text_material_summary:
- Framework PDFs require render/OCR/visual fallback because local PDF text extraction tools are limited.
- Future suite processing must handle PDF, Word, PPT, image, table, scan, and cartoon sources by alternative tools if one tool fails.
current_governor_status:
- G0 partial pass.
- Final PASS blocked.
three_uncertainties:
1. Final product default is one combined book with separated chapters, but user may later request two volumes.
2. Framework PDF raw copies exist in current run; original WeChat temp paths may be volatile.
3. Fresh source scan must determine whether newer 2026二模/later materials exist.
known_failure_to_prevent:
- Old output treated as hidden mother version.
- Concept summary replacing trigger-chain宝典.
- Entry count replacing suite/question coverage.
- Same question multi-method missed.
- Choice questions without full options and reliable answer key.
- Reasoning section classifies methods but fails to attach every question.
- Student artifact contains audit/pipeline language.
- Word file generated without real validation.
```
