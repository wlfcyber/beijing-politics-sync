# ClaudeCode Phase 03 Lane B Prompt

你是 ClaudeCode 20x，负责本轮选必三《逻辑与思维》从0重跑的 **Lane B 独立生产线**。你不是审稿人，也不是只挑错；你必须独立处理原始源文件，生成自己的全量题目覆盖、思维部分矩阵、推理部分矩阵、视觉/OCR 阻塞清单和套卷报告。

## 最高优先级

工作目录：

`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`

必须读取：

- `MASTER_REQUIREMENTS.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden/SKILL.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-book-orchestrator/SKILL.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/SKILL.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md`
- `08_review/gpt_phase_advice/phase_02_gpt55_digest.md`
- `01_source_inventory/PRIORITY_SOURCE_QUEUE.md`
- `02_extraction/priority_queue_sources/priority_queue_extraction_manifest.csv`
- 两个用户框架 PDF 的提取和渲染结果：
  - `02_extraction/framework_pdfs/framework_visual_digest.md`
  - `02_extraction/framework_pdfs/text/`
  - `02_extraction/framework_pdfs/renders/`

允许读取原始源和抽取文本：

- `02_extraction/priority_queue_sources/text/`
- `02_extraction/priority_queue_sources/renders/`
- `00_source_pdfs/`
- `01_source_inventory/SOURCE_INVENTORY.csv`
- 原始路径：`/Users/wanglifei/Desktop/2024模拟题`、`/Users/wanglifei/Desktop/2025模拟题`、`/Users/wanglifei/Desktop/2026模拟题`、`/Users/wanglifei/GaokaoPolitics/2025各区模拟题`

## 严格禁止

为了保持 Lane B 独立性，本阶段不要读取 Codex Lane A 的 Phase 03 结论矩阵：

- 不读 `05_coverage/phase03_question_coverage_matrix.csv`
- 不读 `05_coverage/phase03_thinking_signal_chain_matrix.csv`
- 不读 `05_coverage/phase03_reasoning_question_attachment_matrix.csv`
- 不读 `05_coverage/phase03_blocked_questions.csv`
- 不读 `05_coverage/phase03_visual_fallback_blockers.md`
- 不读 `02_extraction/phase03_visual_recovery_seeds.csv`
- 不读 `04_suite_reports/codex_suite_reports/phase03_registry_and_question_inventory_report.md`

你可以自己重新扫描、重新渲染、重新 OCR/视觉检查，最后你的结果用于和 Codex Lane A 做 A/B diff。

## 本阶段任务

按 GPT-5.5 Pro Phase 02 的条件放行要求，做 Phase 03 全量逐套逐题扫描。目标不是写学生稿，而是回答这句话：

> 每一道题都必须能从 source locator 回到原题，并且能在“思维链矩阵”“推理挂载矩阵”或“blocked list”中找到位置。

你必须处理 56 个 priority source queue 中的原始文件。PDF、Word、PPT、扫描件、表格、漫画、图片都不能因为一个工具不可用就放弃。若文本层为空或太薄，必须使用 render page、OCR、视觉阅读或其他可用工具。

特别注意：manifest 里有试卷 PDF 文本层几乎为空的情况。不要把这种套卷判成“没题”；要从 rendered pages 恢复题号和题面，或者把它作为整套视觉/OCR 阻塞写入 blocked list。

## 输出要求

请写入以下文件，全部放在 `claudecode_lane/` 或 ClaudeCode suite report 目录中，不要覆盖 Codex Lane A 文件：

1. `claudecode_lane/phase03_laneB_source_registry.csv`
   - source_id, suite, source_role, path, text_path, render_dir, extraction_status, visual_or_ocr_need, notes

2. `claudecode_lane/phase03_laneB_suite_registry.csv`
   - suite_id, suite, source_ids, question_count_detected, question_count_confidence, has_thinking, has_reasoning, blank_or_thin_paper_status, next_action

3. `claudecode_lane/phase03_laneB_question_coverage_matrix.csv`
   - question_id, suite_id, source_locator, 原始题号, 题型, 部分归属, 题干完整性, 选项完整性, 答案/细则配对状态, 视觉核读状态, blocked_status, blocked_reason, excerpt

4. `claudecode_lane/phase03_laneB_thinking_signal_candidates.csv`
   - question_id, suite_id, source_locator, 思维知识节点, 材料信号, 可写思维或方法, 答题动作, 为什么能想到, 答案落点状态, evidence_level, 是否可入学生稿

5. `claudecode_lane/phase03_laneB_reasoning_attachment.csv`
   - question_id, suite_id, source_locator, 原始题号, primary_reasoning_type, secondary_reasoning_type, logical_form, rule_slogan, valid_pattern, invalid_pattern_or_trap, answer_key_or_scoring, evidence_level, same_type_question_ids, blocked_status

6. `claudecode_lane/phase03_laneB_visual_blockers.md`
   - 所有文本层薄、扫描、PPT图片、选项不全、漫画/表格需要视觉核读的项目。必须包含 render 路径和下一步。

7. `claudecode_lane/phase03_laneB_missing_and_conflicts.md`
   - 缺卷、缺答案、缺细则、模块边界不确定、疑似重复套卷、普通参考答案不能升格为细则等。

8. `04_suite_reports/claudecode_suite_reports/phase03_laneB_full_scan_report.md`
   - 总结本阶段：扫描源数量、套卷数量、问题行数、思维候选数、推理候选数、blocked 数、最大风险、下一步能否进入 A/B diff。

9. 更新 `claudecode_lane/progress.md`，追加 Phase 03 状态。

## 分类规则

思维部分：

- 模仿哲学宝典的证据结构，但不要写学生稿。
- 每个候选题必须走：材料信号 -> 可写思维/方法 -> 答题动作 -> 来源例题。
- 重点节点：科学思维、辩证思维、创新思维、超前思维、分析与综合、质量互变、辩证否定、整体性、动态性、联想、发散、聚合、逆向、迁移和想象、思维抽象与思维具体。

推理部分：

- 单独成章，不能被排除。按题型挂载每一道题。
- 至少识别：三段论、必要/充分/充分必要假言推理、联言、选言、归纳、类比、换质换位、周延、逻辑三律、概念/判断规则。
- 每一道推理题都写 `logical_form`、`rule_slogan`、`valid_pattern` 或 `invalid_pattern_or_trap`。
- 同类题要能合并，如“三段论的放一起、假言推理的放一起”。

边界：

- 2026石景山期末全模块排除，除非用户提供新正式细则。
- 普通参考答案不能叫评分细则。
- 旧稿只能当 locator，不能继承旧结论。
- 本阶段禁止学生稿、禁止 Word/PDF、禁止 final PASS。

## 自检

结束前必须自己检查：

- 每个 suite 是否有 registry 行；
- 每个 detected question 是否在 question coverage、thinking、reasoning 或 blocked 中有位置；
- 文本层为空/选项不全的纸面是否进入 visual blockers；
- 输出文件是否真实存在且非空；
- `phase03_laneB_full_scan_report.md` 是否明确写出不能进入学生稿，除非后续 A/B diff、GPT/Claude/Governor/Confucius 全部通过。
