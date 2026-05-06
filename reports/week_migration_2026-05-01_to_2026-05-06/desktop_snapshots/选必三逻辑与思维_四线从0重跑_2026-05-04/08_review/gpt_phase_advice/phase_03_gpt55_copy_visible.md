ChatGPT



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

text
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


我会给出有条件放行的 commander packet，只推进源清单、题目清点和覆盖矩阵，暂不允许学生稿或排版成品生产。
Thought for 10m 4s
结论：CONDITIONAL GO
可以启动纠偏后的 Phase 01 生产，但只能进入“源清点、题目挂载、覆盖矩阵、双 lane 独立生产”的阶段。
严禁进入最终学生稿、Word/PDF 成品稿、PASS 宣告。
当前状态满足启动条件：已有四线重跑目录、主要求、用户框架、start card、source ledger 初稿、Governor startup patch。
当前状态不满足成品条件：ClaudeCode lane B 尚未返回，Claude Opus 尚未介入，覆盖矩阵未到 suite/question 级，推理部分尚未逐题挂题型，Word/PDF 未验证，Governor 与 Confucius 未硬 gate。

因此判定为：

CONDITIONAL GO for Phase 01 source inventory and independent production scaffolding.
STOP for final student-facing draft.
STOP for Word/PDF generation.
STOP for PASS.
1. STOP / GO / CONDITIONAL GO 判断
1.1 当前判定
CONDITIONAL GO
允许做：
Codex lane A 独立源清点。
ClaudeCode lane B 独立源清点。
suite/question 级覆盖矩阵搭建。
思维部分与推理部分的结构框架重建。
推理部分“题型挂题”体系设计。
对旧稿进行 failure audit，但旧稿只能作为问题定位材料，不能作为证据母稿。
生成内部审查对象，不生成学生最终稿。
禁止做：
禁止宣称已穷尽所有题。
禁止把旧版内容继承为底稿。
禁止让 Claude Opus 直接扩写最终宝典。
禁止制作 Word/PDF 成品。
禁止提交 Governor final PASS。
禁止把分类总结当成推理部分宝典。
禁止把“条目数量”当成“题目覆盖率”。
1.2 转入 GO 的最低条件
只有同时满足以下条件，才能从 CONDITIONAL GO 升级为 GO：
G1: Codex lane A source inventory completed.
G2: ClaudeCode lane B source inventory completed.
G3: 两条 inventory 已做 diff，冲突项已标红。
G4: 覆盖矩阵已到 suite/question 级。
G5: 每道题已有唯一题号或稳定定位符。
G6: 每道题已归属到思维部分、推理部分或交叉题。
G7: 推理部分每题已挂到至少一个题型节点。
G8: 选择题有完整选项与可靠答案来源。
G9: 主观题有材料触发点、设问、知识调用路径、答案落点。
G10: Governor 确认没有用旧稿充当证据。
2. Codex lane A 下一步生产任务
Codex lane A 的任务是“本地总控生产主线”，重点是建立可审查、可回滚、可 diff 的覆盖体系。当前不要写学生成品稿。
2.1 Codex lane A 立即任务
A1. 建立 source registry
输出文件建议：
A_source_registry.md
A_source_registry.json
A_source_inventory_notes.md
每个 source object 至少包含：
source_id:
source_type: PDF / DOCX / PPTX / image / scan / table / old_artifact_locator
file_path:
file_name:
section_scope: 思维部分 / 推理部分 / 混合 / 未判定
provenance_status: raw_source / locator_only / derived_artifact / unusable
text_extraction_status:
visual_fallback_required: yes / no
contains_questions: yes / no / unknown
contains_answer_key: yes / no / unknown
contains_scoring_rubric: yes / no / unknown
risk_notes:
硬规则：
旧 artifact 只能标记为 locator_only 或 failure_reference。
不允许把旧稿内容写入 raw_source。
框架 PDF 可以作为课程框架来源，但不能自动替代真题来源。
每份文件都要有读取状态，失败也要登记失败原因。
A2. 建立 suite registry
输出文件建议：
A_suite_registry.md
A_suite_registry.json
suite 指“一套题、一份试卷、一份讲义、一份专项练习、一组同源材料”。
每个 suite 至少包含：

suite_id:
source_id:
suite_name:
exam_year:
exam_region:
exam_stage: 一模 / 二模 / 期末 / 专项 / 高考真题 / 模拟 / 未判定
document_location:
question_count_detected:
question_count_confirmed:
answer_key_status:
rubric_status:
section_scope:
requires_visual_processing:
confidence_level:
open_issues:
必须做到：
不以文件名猜题量。
每套题必须经过人工式结构确认。
PDF、图片、漫画、表格、材料页必须进入 visual fallback 队列。
发现同一题跨多个文件出现时，要建立 duplicate map。
A3. 建立 question coverage matrix
输出文件建议：
A_question_coverage_matrix.xlsx
A_question_coverage_matrix.md
A_question_coverage_matrix.json
每道题至少一行：
question_id:
suite_id:
source_id:
stable_locator: 页码 / 题号 / 图片编号 / 文档段落位置
question_type: 选择题 / 主观题 / 材料题 / 图表题 / 漫画题 / 组合题
section_scope: 思维 / 推理 / 交叉
knowledge_node_primary:
knowledge_node_secondary:
reasoning_type_primary:
reasoning_type_secondary:
has_full_stem:
has_full_options:
has_answer_key:
has_rubric:
material_trigger_points:
question_ask:
why_think_of_this:
answer_landing_points:
student_error_traps:
status: raw / classified / drafted / reviewed / blocked
lane_A_notes:
lane_B_notes:
conflict_status:
硬规则：
每道题必须有 stable locator。
没有 locator 的题不能进入宝典。
选择题无完整选项，不得生成选择题解析。
主观题无设问，不得生成答案落点。
只有知识点名而无材料触发点，判为未完成。
推理题只写“属于归纳推理”不合格，必须挂到具体题型和解题步骤。
A4. 思维部分生产框架
思维部分需要恢复哲学宝典式结构。每题条目必须包含：
题目定位:
知识原理:
方法论或操作规则:
材料触发点:
设问指向:
为什么能想到这个知识:
答案落点:
可迁移口令:
易错陷阱:
同类题索引:
思维部分不能写成章节摘要。必须体现“材料如何触发知识调用”。
A5. 推理部分生产框架
推理部分由 Codex lane A 先搭骨架，暂不做最终语言润色。骨架格式见第 6 节。
A6. 产出 lane A review packet
Codex lane A 完成 Phase 01 后，必须提交给 GPT-5.5 Pro 的对象：
A_source_registry
A_suite_registry
A_question_coverage_matrix
A_reasoning_typology_map
A_unresolved_source_failures
A_duplicate_question_map
A_blocked_questions_list
A_sample_10_question_drafts
其中 A_sample_10_question_drafts 必须包含：
思维部分选择题 2 道。
思维部分主观题 2 道。
推理部分选择题 2 道。
推理部分主观题 2 道。
图表、漫画、表格或扫描材料题至少 1 道。
一题多法或跨知识点题至少 1 道。
3. ClaudeCode lane B 下一步生产任务
ClaudeCode lane B 的任务是“独立复核生产线”，不能复制 Codex lane A 的判断。它要独立读源、独立建 inventory、独立标记题目与缺口。
3.1 ClaudeCode lane B 当前任务状态
Phase 00 显示：
ClaudeCode lane B Phase 01 independent source-inventory task is still running.
因此下一步是完成并提交独立 inventory，不得进入写稿阶段。
3.2 ClaudeCode lane B 立即任务
B1. 独立 source inventory
输出：
B_source_inventory.md
B_source_inventory.json
B_source_failures.md
要求：
不引用 Codex lane A 的 source_id 作为判断依据。
自行列出全部发现的原始文件。
对每个文件给出读取状态。
对 PDF、图片、PPT、Word、扫描件分别标注处理风险。
标出哪些材料含题目，哪些含答案，哪些含评分说明。
B2. 独立 suite/question 识别
输出：
B_suite_question_inventory.md
B_suite_question_inventory.json
每条至少包含：
detected_suite:
detected_question:
source_locator:
question_type:
section_scope:
answer_key_detected:
rubric_detected:
visual_required:
confidence:
ClaudeCode lane B 的核心责任是发现 Codex lane A 漏掉的题，特别是：
PDF 中页眉页脚附近题号。
图片中的漫画题。
PPT 内嵌题。
Word 表格题。
扫描材料中被 OCR 漏掉的选项。
一题多问中的第二问、第三问。
同一材料下多个设问。
答案页与题目页分离的套题。
“思维”与“推理”交叉题。
推理题中被误标为普通材料题的题。
B3. 与 Codex lane A diff
ClaudeCode lane B 完成后，Codex 总控必须生成：
A_B_source_diff.md
A_B_suite_diff.md
A_B_question_diff.md
A_B_classification_diff.md
diff 维度：
source missing in A
source missing in B
suite missing in A
suite missing in B
question missing in A
question missing in B
question count mismatch
answer key mismatch
section classification mismatch
reasoning type mismatch
locator mismatch
visual processing mismatch
硬规则：
A 与 B 不一致时，不得自动取多数。
不一致项进入 conflict_queue。
conflict 未解决，相关题不得进入最终稿。
A 与 B 都没有答案来源的题，不得编造答案。
A 与 B 都漏掉但 Governor later发现的题，触发回滚。
4. Claude Opus 什么时候可以介入、只能做什么、不能做什么
4.1 介入时机
Claude Opus 现在不能介入最终成品化。
它只能在以下对象齐备后介入：
C1: A_source_registry completed.
C2: B_source_inventory completed.
C3: A_B_diff completed.
C4: question_coverage_matrix 至少完成 first locked pass.
C5: 每道进入样稿的题都有 source locator。
C6: blocked_questions_list 已单独列出。
C7: Governor 确认旧稿没有作为证据母稿。
推荐介入节点：
Phase 02 after source and coverage lock, before final Word/PDF.
4.2 Claude Opus 可以做什么
Claude Opus 的角色是“教学文本成品化”，不是源审查官。允许做：
把 Codex lane A 与 ClaudeCode lane B 已确认的题目条目改写成学生可读表达。
将“材料触发点、设问、为什么能想到、答案落点”串成教学链条。
将推理部分规则口令改成可背、可迁移的表达。
优化章节导语、题型导语、学习方法提示。
合并同类题的复盘，但必须保留每道题独立条目。
对语言做降噪，删除 pipeline、audit、source ledger 等内部术语。
统一术语风格，例如“判断依据”“调用路径”“落点句式”“易错陷阱”。
为每个题型补“先看什么、再判什么、最后怎么写”的步骤化说明。
对主观题答案落点做学生化表达，但不得改变原始评分点。
生成“考场口令”和“错因提醒”。
4.3 Claude Opus 不能做什么
严格禁止：
不得新增题目。
不得删除题目。
不得自行判断答案正确性。
不得补全缺失选项。
不得补写缺失评分细则。
不得把没有 source locator 的题写进正文。
不得把旧稿改写为新稿。
不得合并多道题导致逐题覆盖消失。
不得把推理部分压缩为题型总述。
不得在学生稿中出现 source registry、coverage matrix、Governor、Confucius、lane A、lane B 等内部语言。
4.4 Claude Opus 输入格式
交给 Claude Opus 的包必须是“锁定题目包”，不是杂乱源文件：
opus_input_packet:
  locked_question_entries:
  source_locator_per_question:
  verified_answer_key:
  verified_rubric_or_answer_points:
  reasoning_typology_map:
  blocked_questions_excluded:
  style_rules:
  forbidden_actions:
Claude Opus 输出必须带结构标签：
student_text_entry:
  question_id:
  title:
  knowledge_call:
  material_trigger:
  question_ask:
  why_this_knowledge:
  answer_landing:
  trap_warning:
  transfer_formula:
  opus_change_notes:
5. GPT-5.5 Pro 后续必须审查的 trigger objects
GPT-5.5 Pro 的任务是内容总审稿与压力测试，不充当源证据裁判。它审查流程完整性、覆盖逻辑、风险、题型挂载、学生稿质量门槛。
必须审查以下 trigger objects：

5.1 Phase 01 source trigger objects
T01_A_source_registry
T02_B_source_inventory
T03_A_B_source_diff
T04_source_failure_log
T05_locator_only_artifact_list
审查点：
是否把旧 artifact 误列为 evidence。
是否有文件未分类。
是否有 PDF、图片、PPT、Word、扫描件未进入 fallback 计划。
是否存在“读取失败但未阻断”的源。
是否存在“框架 PDF 替代真题源”的风险。
5.2 Suite/question coverage trigger objects
T06_A_suite_registry
T07_B_suite_question_inventory
T08_A_B_question_diff
T09_question_coverage_matrix
T10_duplicate_question_map
T11_blocked_questions_list
审查点：
是否到 suite/question 级。
是否每题有 stable locator。
是否每题有题型、知识点、设问类型。
是否一题多问被拆开。
是否同题重复被正确映射。
是否交叉题被双挂载。
是否 blocked questions 被排除出正文。
5.3 思维部分 trigger objects
T12_thinking_part_question_entries
T13_thinking_principle_method_map
T14_thinking_material_trigger_map
T15_thinking_sample_drafts
审查点：
是否逐题处理。
是否有材料触发点。
是否解释为什么能想到该知识。
是否有答案落点。
是否有易错陷阱。
是否避免章节摘要化。
5.4 推理部分 trigger objects
T16_reasoning_typology_map
T17_reasoning_question_attachment_matrix
T18_reasoning_rule_slogans
T19_reasoning_trap_matrix
T20_reasoning_step_templates
T21_reasoning_all_question_entries
审查点：
是否所有推理题都挂到题型。
是否每个题型下面列出全部题。
是否每道题有规则口令。
是否每道题有易错陷阱。
是否有解题步骤。
是否保留一题多法。
是否把形式逻辑题与非形式推理题区分清楚。
是否把“归纳、类比、演绎、三段论、复合判断、假言推理、模态或关系判断”等节点处理到可解题层级。
5.5 Claude Opus trigger objects
T22_opus_input_packet
T23_opus_student_text_output
T24_opus_change_log
T25_internal_language_leak_check
审查点：
Opus 是否只改写已锁定题。
是否新增、删除或合并题。
是否改变评分点。
是否漏掉 trigger chain。
是否出现内部流程语言。
是否把宝典语言写成空泛鸡汤。
5.6 最终成品 trigger objects
T26_final_student_draft_md
T27_final_docx
T28_final_pdf
T29_layout_validation_report
T30_Governor_gate_report
T31_Confucius_gate_report
T32_final_PASS_packet
审查点：
Word 与 PDF 内容是否一致。
目录、页眉、分页、表格、题号是否稳定。
选择题选项是否完整。
主观题答案点是否没有断裂。
学生稿是否无 audit/pipeline 语言。
Governor 与 Confucius 是否真实执行。
是否存在“版式通过但内容未通过”的假 PASS。
6. 推理部分如何做成宝典
核心要求：
题型 -> 全部题目 -> 规则口令 -> 易错陷阱 -> 解题步骤
推理部分的失败根因通常是“先讲题型，再举几个例题”。本轮必须改成“每一个题型节点下面挂全部题，每一道题都有可复现解法”。
6.1 推理部分总目录结构
建议结构：
推理部分总表
  1. 概念与判断基础题
  2. 性质判断与换质换位题
  3. 三段论推理题
  4. 联言判断与联言推理题
  5. 选言判断与选言推理题
  6. 假言判断与假言推理题
  7. 充分条件、必要条件、充要条件题
  8. 归纳推理题
  9. 类比推理题
  10. 求同法、求异法、共变法、剩余法题
  11. 反证法、归谬法、矛盾分析题
  12. 综合推理与一题多法题
  13. 材料逻辑链条题
  14. 易混题型复盘
具体题型名称应由本地题源决定，上面只是骨架。不能为了套目录而强行分类。若题源里没有某类题，保留到“未出现或暂未纳入”记录，正文不空写。
6.2 每个题型节点必须有 7 个组件
每个题型章固定格式：
题型名称:
考查规则:
规则口令:
本题型全部题目清单:
逐题精讲:
易错陷阱总表:
迁移训练口令:
其中“本题型全部题目清单”必须列出所有 question_id：
本题型全部题目清单
Q-R-001
Q-R-004
Q-R-009
Q-R-015
...
只要 coverage matrix 显示属于该题型，正文必须出现。若题进入 blocked 状态，要在内部 blocked list 中说明，不能悄悄遗漏。
6.3 每道推理题的条目模板
每道题必须按以下模板生产：
题目定位:
  suite_id:
  question_id:
  source_locator:

题型归属:
  primary_type:
  secondary_type:
  one_question_multi_method: yes / no

规则口令:
  一句话可背规则。

材料触发点:
  题干中哪个词、哪句话、哪个结构触发该推理规则。

设问指向:
  问的是判断真假、推出结论、找逻辑错误、补充前提、评价论证，还是选择正确推理。

为什么能想到:
  从材料触发点到规则调用的中间推导。

解题步骤:
  Step 1: 抽取逻辑形式。
  Step 2: 判断条件关系或判断类型。
  Step 3: 套用有效推理式或排除无效式。
  Step 4: 回到选项或答案落点。
  Step 5: 写出规范表达。

答案落点:
  选择题写选项与排除理由。
  主观题写评分点与表达句式。

易错陷阱:
  本题最容易错在哪里。

同类题:
  同一题型下的其他 question_id。
6.4 推理题必须先抽形式，再回材料
推理部分特别容易写成政治材料分析。必须强制执行：
材料语言 -> 逻辑形式 -> 推理规则 -> 选项/答案
示例规则，不引用具体题源：
看到“只要 P 就 Q”，先写成 P -> Q。
看到“只有 P 才 Q”，先写成 Q -> P。
看到“P 或 Q”，先判断相容选言还是不相容选言。
看到“并且”，先判断联言支是否都真。
看到“所有 S 都是 P”，先判断能否换位、换质或进入三段论。
看到“这个对象像那个对象”，先判断类比根据是否充分。
看到“几个样本推出一般结论”，先判断归纳样本是否代表充分。
看到“现象随因素变化而变化”，先考虑共变法。
看到“多个场合共同因素”，先考虑求同法。
看到“一个场合有、另一个场合无”，先考虑求异法。
6.5 推理题型挂载矩阵
必须生成：
reasoning_question_attachment_matrix
字段：
question_id:
suite_id:
stem_locator:
primary_reasoning_type:
secondary_reasoning_type:
rule_slogan:
logical_form:
valid_inference_pattern:
invalid_pattern_to_avoid:
answer_key:
draft_status:
review_status:
验收规则：
coverage matrix 中 section_scope = 推理 的每道题，必须出现在 attachment matrix。
attachment matrix 中每道题，必须出现在正文。
正文每道题，必须回指到 matrix。
matrix 与正文题号不一致，直接阻断。
一题多法必须双挂载，不得只挂一个节点。
“综合题”不能成为逃避分类的垃圾桶，必须说明综合在哪些规则上。
6.6 题型章示范骨架
第三章 假言推理题

一、题型规则
充分条件假言判断：P -> Q。
有效式：
1. 肯定前件，可以肯定后件。
2. 否定后件，可以否定前件。
无效式：
1. 肯定后件，不能肯定前件。
2. 否定前件，不能否定后件。

二、规则口令
前真推后真，后假推前假；后真不返推，前假不断后。

三、本题型全部题目
Q-R-003
Q-R-011
Q-R-018
Q-R-026

四、逐题精讲
Q-R-003
题目定位:
材料触发点:
设问指向:
为什么能想到:
解题步骤:
答案落点:
易错陷阱:
同类题:

Q-R-011
...
该骨架必须被真实 question_id 填满。没有真实题号时不能生成假题号。
7. 最可能导致再次失败的 10 个风险
风险 1：旧稿变成隐形母版
表现：
新稿语言、结构、例题顺序与旧稿高度相似。
后果：
纠偏名义上重跑，实质上修补旧稿。
阻断措施：
旧稿只能进入 failure audit 和 locator-only 列表。
任何正文内容必须回指新 coverage matrix。
风险 2：覆盖矩阵停留在条目级
表现：
只统计知识点、题型、章节，没有统计每套题、每道题。
后果：
看似内容很多，实际漏题无法发现。
阻断措施：
必须 suite/question 双层编号。
没有 question_id 的内容不能进入正文。
风险 3：推理部分再次写成分类讲义
表现：
先讲归纳、类比、演绎，每类配少数例子。
后果：
用户核心批评没有解决。
阻断措施：
每个题型下面必须列出全部题目清单。
reasoning_attachment_matrix 与正文逐项核对。
风险 4：PDF、图片、PPT、扫描题漏读
表现：
文本抽取成功就停止，没有处理图表、漫画、表格、图片内文字。
后果：
非文本材料题大概率丢失。
阻断措施：
所有非文本对象进入 visual fallback queue。
读取失败必须登记，不能静默跳过。
风险 5：选择题缺选项仍写解析
表现：
只有题干或只有答案，却生成排除法解析。
后果：
解析不可验证，容易编造选项逻辑。
阻断措施：
选择题必须 has_full_options = yes 且 has_answer_key = yes 才能写。
风险 6：主观题没有评分落点
表现：
只有知识总结，没有材料对应句和评分点。
后果：
不像哲学宝典，学生不能知道怎么得分。
阻断措施：
主观题必须包含材料触发点、设问指向、为什么能想到、答案落点。
缺一项为 blocked。
风险 7：一题多问被当成一题
表现：
第 1 问、第 2 问、第 3 问共用一个解析。
后果：
漏掉小问，覆盖率虚高。
阻断措施：
question_id 可以拆成 Q001-a、Q001-b、Q001-c。
每个小问单独挂知识点和答案落点。
风险 8：一题多法被单挂载
表现：
某题同时涉及假言推理和归谬，只挂到假言推理。
后果：
学生迁移能力下降，同类题索引断裂。
阻断措施：
设置 primary_type 与 secondary_type。
综合题必须列出多个规则触发点。
风险 9：Claude Opus 过早介入导致文学化
表现：
文本好读，但题目、答案、评分点被压缩或改写过度。
后果：
漂亮但不可靠。
阻断措施：
Opus 只处理 locked_question_entries。
Opus 输出必须与 question_id 一一对应。
风险 10：Word/PDF 版式通过掩盖内容未通过
表现：
有目录、有页眉、有 PDF，但覆盖、题号、答案核对没有完成。
后果：
形式完成，实质失败。
阻断措施：
版式验收只能排在内容 gate 之后。
Governor 和 Confucius 未通过，不得生成 final PASS。
8. 必须阻断最终 PASS 的验收 gate
以下任一 gate 未通过，最终 PASS 必须阻断。
Gate 0：启动真实性 gate
G0.1 新 run folder 存在。
G0.2 master requirements 存在。
G0.3 四线角色已登记。
G0.4 旧稿被标记为 locator-only 或 failure reference。
G0.5 Governor startup patch 已写明 final PASS blocked。
未通过结果：
STOP
Gate 1：源证据 gate
G1.1 A_source_registry 完成。
G1.2 B_source_inventory 完成。
G1.3 A_B_source_diff 完成。
G1.4 每个 raw source 有读取状态。
G1.5 读取失败有 failure log。
G1.6 框架 PDF、真题源、答案源、评分源分开登记。
G1.7 old artifact 没有进入 evidence pool。
阻断条件：
任何 source provenance 不清。
任何读取失败被静默跳过。
任何旧稿内容被当作证据。
Gate 2：suite/question 覆盖 gate
G2.1 suite_registry 完成。
G2.2 question_coverage_matrix 完成。
G2.3 每道题有 question_id。
G2.4 每道题有 stable_locator。
G2.5 每道题有 section_scope。
G2.6 每道题有 question_type。
G2.7 一题多问已拆分。
G2.8 duplicate_question_map 完成。
G2.9 blocked_questions_list 完成。
阻断条件：
只做到章节覆盖。
只做到知识点覆盖。
只有 entry count，没有 question coverage。
存在无 locator 正文题。
存在 coverage matrix 中有题但正文无题。
Gate 3：答案与评分 gate
G3.1 选择题有完整题干。
G3.2 选择题有完整选项。
G3.3 选择题有可靠答案 key。
G3.4 主观题有设问。
G3.5 主观题有答案来源或评分点来源。
G3.6 答案落点没有超出证据范围。
G3.7 缺答案题进入 blocked list。
阻断条件：
缺选项仍写选择题解析。
缺答案仍给确定选项。
缺评分点仍写“标准答案”。
Gate 4：思维部分宝典 gate
G4.1 思维部分每题有材料触发点。
G4.2 每题有设问指向。
G4.3 每题有为什么能想到。
G4.4 每题有答案落点。
G4.5 每题有易错陷阱。
G4.6 每题有同类题索引或说明。
G4.7 内容按原理/方法论组织，但不牺牲逐题覆盖。
阻断条件：
概念摘要替代逐题解析。
只写原理，不写材料触发。
只写答案，不写调用路径。
Gate 5：推理部分宝典 gate
G5.1 reasoning_typology_map 完成。
G5.2 reasoning_question_attachment_matrix 完成。
G5.3 推理题全部挂到题型。
G5.4 每个题型列出全部 question_id。
G5.5 每道题有规则口令。
G5.6 每道题有逻辑形式抽取。
G5.7 每道题有解题步骤。
G5.8 每道题有易错陷阱。
G5.9 一题多法双挂载。
G5.10 综合题说明综合规则。
阻断条件：
推理部分只做题型总述。
题型下没有全部题目清单。
coverage matrix 与 reasoning matrix 不一致。
正文少于 matrix 题数。
Gate 6：双 lane diff gate
G6.1 A_B_source_diff 已解决。
G6.2 A_B_question_diff 已解决。
G6.3 A_B_classification_diff 已解决。
G6.4 unresolved_conflict_queue 为空，或相关题进入 blocked list。
G6.5 Governor 记录每个冲突的处理结论。
阻断条件：
A 与 B 有冲突但直接进入正文。
用 Codex 结果覆盖 ClaudeCode 结果且无理由。
用 ClaudeCode 结果覆盖 Codex 结果且无理由。
Gate 7：Claude Opus 成品化 gate
G7.1 Opus 只接收 locked_question_entries。
G7.2 Opus 输出与 question_id 一一对应。
G7.3 Opus 没有新增题。
G7.4 Opus 没有删除题。
G7.5 Opus 没有改动答案 key。
G7.6 Opus 没有改动评分点含义。
G7.7 Opus 没有合并题目导致覆盖消失。
G7.8 学生稿无 pipeline 语言。
阻断条件：
Opus 直接读旧稿扩写。
Opus 输出没有 question_id 对照表。
Opus 学生化表达改变答案含义。
Gate 8：GPT-5.5 Pro 压力测试 gate
GPT-5.5 Pro 必须执行以下压力测试：
P1: 随机抽查 20 道题，检查 coverage -> 正文 -> 答案落点一致。
P2: 专门抽查推理部分 20 道题，检查题型挂载与规则口令。
P3: 抽查所有 blocked questions，确认未进入正文。
P4: 抽查所有 visual fallback source，确认非文本题未漏。
P5: 抽查所有一题多问，确认小问拆分。
P6: 抽查所有一题多法，确认双挂载。
P7: 搜索内部词泄漏。
P8: 检查旧稿继承痕迹。
P9: 检查正文题号与 matrix 题号一致。
P10: 检查 Word/PDF 生成前内容 gate 是否完成。
阻断条件：
任一压力测试发现系统性问题。
同类错误出现 2 次以上。
随机抽查发现正文题无 locator。
推理部分抽查发现题型下缺题。
Gate 9：Governor gate
Governor 必须硬判：
GOV_PASS_SOURCE
GOV_PASS_COVERAGE
GOV_PASS_REASONING_ATTACHMENT
GOV_PASS_THINKING_TRIGGER_CHAIN
GOV_PASS_OPUS_BOUNDARY
GOV_PASS_NO_INTERNAL_LANGUAGE
GOV_PASS_DOCX_VALIDATION
GOV_PASS_PDF_VALIDATION
阻断条件：
Governor 只给结论，没有证据对象。
Governor 没有逐 gate 记录。
Governor 对 unresolved conflict 放行。
Governor 对 Word/PDF 未验证放行。
Gate 10：Confucius gate
Confucius 必须从学生学习价值角度审查：
C_PASS_EXAM_USABILITY
C_PASS_TRIGGER_CHAIN
C_PASS_MEMORIZABLE_RULES
C_PASS_TRANSFERABILITY
C_PASS_ERROR_PREVENTION
C_PASS_NO_EMPTY_SUMMARY
C_PASS_REASONING_STEP_CLARITY
阻断条件：
学生看完仍不知道材料为什么触发该知识。
学生看完仍不知道推理题第一步做什么。
学生看完只有知识点，没有题目迁移口令。
主观题答案落点不能直接用于考场表达。
Gate 11：Word/PDF validation gate
必须真实验证：
D1: DOCX 文件存在且可打开。
D2: PDF 文件存在且可打开。
D3: DOCX 与 PDF 内容一致。
D4: 目录结构正确。
D5: 题号连续且无重复。
D6: 表格不截断。
D7: 图片、漫画、图表显示正常。
D8: 页眉页脚无内部信息。
D9: 学生稿无 source ledger、lane、Governor、Confucius 等字样。
D10: 最终文件名、版本号、日期清晰。
阻断条件：
只生成 DOCX 未生成 PDF。
只生成 PDF 未核对 DOCX。
图片丢失。
表格溢出。
正文出现内部流程词。
Gate 12：Final PASS packet gate
最终 PASS 包必须包含：
final_PASS_packet:
  final_student_docx:
  final_student_pdf:
  source_registry_summary:
  suite_question_coverage_summary:
  reasoning_attachment_summary:
  blocked_questions_summary:
  A_B_diff_resolution_summary:
  GPT_review_summary:
  Governor_gate_report:
  Confucius_gate_report:
  layout_validation_report:
  known_limitations:
阻断条件：
没有 known_limitations。
没有 blocked_questions_summary。
没有 A_B diff resolution。
没有 Governor 或 Confucius 独立 gate。
Codex 本地总控可直接执行的下一步清单
1. Freeze current Phase 00 files.
2. Mark old artifacts as locator_only or failure_reference.
3. Complete A_source_registry.
4. Complete A_suite_registry.
5. Complete A_question_coverage_matrix first pass.
6. Wait for ClaudeCode lane B Phase 01 inventory.
7. Generate A_B_source_diff and A_B_question_diff.
8. Resolve conflicts or move affected questions to blocked list.
9. Build reasoning_typology_map from actual detected questions.
10. Build reasoning_question_attachment_matrix.
11. Produce 10-question sample packet for GPT-5.5 Pro pressure test.
12. Do not start Claude Opus until locked_question_entries exist.
13. Do not generate student final draft.
14. Do not generate Word/PDF.
15. Keep Governor final PASS blocked.
Final operative instruction:
Proceed only with Phase 01 inventory, coverage, diff, and reasoning attachment scaffolding.
Do not produce final student-facing manuscript until every question has been located, classified, attached, and gate-checked.

你是 GPT-5.5 Pro，继续担任“飞哥政治庄园”选必三《逻辑与思维》四线从0重跑的总指挥/内容审稿人。请基于下面 Phase 02 阶段报告，判断是否允许进入下一阶段：全量逐套逐题扫描与分类。请严格审稿，不要安慰。

背景：工作目录 /Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04。本轮要求完全模仿成功的哲学宝典工作流；从0开始；旧稿只可定位，不继承结论；思维部分按“材料信号 -> 可写思维/方法 -> 答题动作 -> 来源例题”；推理部分按“题型 -> 规则 -> 常见陷阱 -> 同类真题归档 -> 解题动作”。四线：Codex总控+生产、ClaudeCode独立生产/复核、GPT-5.5 Pro阶段指挥/压力测试、Claude/Opus后续成文化但必须等证据锁定。你上轮给的是 CONDITIONAL GO：允许 source inventory、coverage/diff、reasoning attachment、有限样本回源；禁止学生稿、Word/PDF、PASS。

Phase 02 已完成：
1. 两份用户框架PDF学习：思维PDF 14页、推理PDF 21页，文本层很薄，已全部渲染并视觉初读，写入 framework_visual_digest.md。结论：思维部分可仿哲学宝典；推理部分必须做题型树，不能只写抽象总结。
2. Codex lane A 五个硬样本回源：HS01 2026顺义一模Q19(2) 科学思维特征，锁客观性+预见性+可检验性；HS02 2025海淀二模Q20 辩证思维，原卷文本层弱，已视觉核读，细则/讲评/评标锁定三个可选角度池；HS03 2026朝阳期中Q21(2) 创新思维，锁超前+联想+逆向/转换性思考，发散+聚合为有效路径；HS04 2026通州期末Q11 选择题，锁完整题干四选项与答案C，考感性具体->思维抽象->思维具体；HS05 2026东城期末Q17(2) 推理部分，形式逻辑综合，锁矛盾律+充分条件假言推理误用+三段论中项不周延。
3. ClaudeCode lane B 独立复核：没有读取Codex Phase02结论，独立输出 phase02_hard_sample_crosscheck.md、phase02_hard_sample_matrix.csv、phase02_disagreements_and_blockers.md、phase02_hard_samples_report.md。总体一致，但提出5个分歧候选和4个阻塞项。
4. Codex A/B融合：写入 phase02_AB_fusion.md、resolved_conflicts.md、unresolved_conflicts.md。融合裁决：HS01 LOCKED；HS02 LOCKED_PENDING_VISUAL；HS03 LOCKED；HS04 LOCKED；HS05 LOCKED且归推理部分不入思维主链。
5. 关键纠错：HS02 海淀二模Q20不能写成“三点全部必答/3点×2分”。二次回源发现：主细则表格列三个角度：分析与综合/系统优化/整体性；质量互变/动态性；辩证否定。讲评PDF明确“从3个角度选择2个，每一角度按照1+2赋分”。评标实录明确辩证否定有效、辩证思维特征角度可替代给分。融合结论：最终文档应写成“三个可选角度池，优先选材料最顺的两条写深；辩证否定是高价值补充/替代角度”，不能写成三点全部必答。
6. 优先队列56个原始源文件批量抽取完成：PDF 21、PPTX 17、DOCX 17、RTF 1；全部extracted，missing=0，errors=0。PDF用PyMuPDF文本+命中页渲染；PPTX用python-pptx；DOCX用python-docx；RTF用textutil。说明后续不能以文件格式复杂为借口跳过。

当前未解除阻塞：HS02原卷仍需最终视觉/模型审稿确认后才能进学生稿；HS01 Q19(1)可能是推理候选，后续全量扫描要处理；PPTX内嵌学生答卷图片/图形批注尚未全部视觉读取，若涉及边界案例必须补；top-level SOURCE_LEDGER.csv仍含旧稿locator行，最终PASS前必须换成干净raw-source registry；全书coverage目前只做五个硬样本，不可声称穷尽；2026二模在已扫source roots未发现，必须保持missing/blocked，除非新文件出现。

请给出：
1. 是否允许进入下一阶段“全量逐套逐题扫描与分类”？用 GO / CONDITIONAL GO / NO-GO。
2. 下一阶段必须产出的文件清单。
3. 下一阶段扫描顺序：思维部分与推理部分怎么并行/分工。
4. 现在最大的内容风险是什么。
5. 是否同意HS02融合结论；不同意请指出如何改。
6. 对推理部分宝典结构给硬要求，避免再次写成泛泛总结。

我会只判定是否进入全量扫描分类，不把硬样本成功扩大为全书放行。重点审查前置条件、剩余阻塞和下一阶段硬 gate。
Thought for 4m 35s
1. 阶段判断：CONDITIONAL GO
允许进入下一阶段：全量逐套逐题扫描与分类。
但只允许进入扫描、分类、挂载、差异复核阶段。严禁进入学生稿、Claude/Opus 成文化、Word/PDF、最终 PASS。
判断理由很明确：

Phase 02 已证明四线机制开始真实运转。Codex lane A 做了硬样本回源，ClaudeCode lane B 独立复核，随后做了 A/B 融合与冲突处理。
五个硬样本覆盖了关键风险类型：思维主观题、辩证思维可选角度、创新思维、选择题完整选项、推理综合题。
HS02 的纠错说明流程有效，已经阻止了把可选角度池误写成三点必答。
56 个优先原始源文件已批量抽取，且 missing=0、errors=0，说明下一阶段没有理由因格式复杂而停滞。
但当前只完成五个硬样本，coverage 尚未全量到 suite/question 级。旧稿 locator 行仍在 top-level SOURCE_LEDGER.csv，PPTX 内嵌图片和图形批注尚未全部视觉读取，HS02 仍有 LOCKED_PENDING_VISUAL 状态。
因此结论是：
CONDITIONAL GO for 全量逐套逐题扫描与分类
NO-GO for 学生稿
NO-GO for Claude/Opus 成文化
NO-GO for Word/PDF
NO-GO for PASS
进入下一阶段的边界条件：
1. 所有题必须从 raw source 回源。
2. 旧稿只能定位，不能继承结论。
3. 所有题必须有 stable locator。
4. 推理题必须进入题型挂载矩阵。
5. 思维题必须进入材料信号链矩阵。
6. 无答案、无选项、无细则、视觉未核读的题必须进入 blocker。
7. HS02 不得进入学生稿，直到最终视觉确认完成。
2. 下一阶段必须产出的文件清单
建议将下一阶段命名为：
Phase 03 full suite question scan and classification
必须产出以下文件。缺任一类，不能进入后续成文化阶段。
2.1 干净源文件总账
phase03_raw_source_registry.csv
phase03_raw_source_registry.md
phase03_locator_only_removed_or_isolated.md
phase03_source_reading_methods.md
phase03_source_failures_and_fallbacks.md
硬要求：
1. top-level SOURCE_LEDGER.csv 中旧稿 locator 行必须剥离。
2. raw source、locator only、旧稿 failure reference 必须分表。
3. 每个原始文件必须标明读取方法。
4. 每个 PDF 必须标明文本读取与命中页渲染状态。
5. 每个 PPTX 必须标明 slide 文本、内嵌图片、图形批注是否处理。
6. 每个 DOCX 必须标明正文、表格、图片题是否处理。
7. RTF 必须标明转换与读取状态。
2.2 套题级总账
phase03_suite_registry.csv
phase03_suite_registry.md
phase03_suite_duplicate_map.csv
phase03_missing_expected_sources.md
phase03_2026_二模_missing_or_blocked.md
每个 suite 至少包含：
suite_id
source_id
文件名
地区
年份
考试阶段
题目范围
是否含思维部分
是否含推理部分
题目页范围
答案页范围
评分细则页范围
讲评页范围
题量检测值
题量确认值
视觉风险等级
是否进入全量扫描
必须单独记录：
1. 2026 二模在已扫 source roots 未发现。
2. 未发现不等于不存在。
3. 除非新文件出现，否则进入 missing/blocked。
2.3 逐题覆盖矩阵
phase03_question_coverage_matrix.csv
phase03_question_coverage_matrix.xlsx
phase03_question_coverage_matrix.md
每题至少一行。字段必须包含：
question_id
suite_id
source_id
stable_locator
原始题号
题型：选择题 / 主观题 / 图表题 / 漫画题 / 组合题 / 讲评题
部分归属：思维 / 推理 / 交叉 / 待判
是否完整题干
是否完整选项
是否有答案
是否有评分细则
是否有讲评
是否需要视觉核读
是否已视觉核读
知识节点
题型节点
材料信号
设问动作
答案落点状态
推理规则状态
blocked_status
blocked_reason
lane_A_classification
lane_B_classification
A_B_conflict_status
final_classification
硬要求：
1. 不能只统计题目数量。
2. 不能只统计知识点数量。
3. 必须到每一道题。
4. 一题多问拆成子题，例如 Q21-1、Q21-2。
5. 一题多法必须有 primary 与 secondary 挂载。
2.4 思维部分材料信号链矩阵
phase03_thinking_signal_chain_matrix.csv
phase03_thinking_signal_chain_matrix.md
字段必须包含：
question_id
suite_id
stable_locator
思维知识节点
材料信号
可写思维或方法
答题动作
设问类型
为什么能想到
答案落点
来源例题
同类题
易错点
是否可入学生稿
验收口径：
材料信号 -> 可写思维/方法 -> 答题动作 -> 来源例题
任何思维题缺少材料信号或答题动作，不能进入宝典正文。
2.5 推理部分题型挂载矩阵
phase03_reasoning_typology_tree.md
phase03_reasoning_question_attachment_matrix.csv
phase03_reasoning_question_attachment_matrix.xlsx
phase03_reasoning_rule_slogans.md
phase03_reasoning_trap_matrix.md
phase03_reasoning_action_templates.md
字段必须包含：
question_id
suite_id
stable_locator
原始题号
primary_reasoning_type
secondary_reasoning_type
logical_form
rule_slogan
valid_pattern
invalid_pattern_or_trap
same_type_question_ids
answer_key
explanation_status
blocked_status
硬要求：
1. coverage matrix 中归为推理的题，必须全部出现在 attachment matrix。
2. attachment matrix 中的题，后续正文必须逐题出现。
3. 推理综合题不能只写综合，必须拆出具体规则。
4. HS05 这类题必须挂矛盾律、充分条件假言推理误用、三段论中项不周延。
5. HS01 Q19(1) 必须作为推理候选进入扫描，不得漏掉。
2.6 视觉补读队列
phase03_visual_fallback_queue.csv
phase03_visual_fallback_results.md
phase03_pptx_embedded_image_review.md
phase03_pdf_render_review_log.md
phase03_docx_table_and_image_review.md
必须覆盖：
1. PDF 命中页。
2. PPTX 内嵌学生答卷图片。
3. PPTX 图形批注。
4. DOCX 表格题。
5. 图片题、漫画题、图表题。
6. 文本层薄弱的原卷。
阻断规则：
视觉未核读的边界题，不能进入 LOCKED。
视觉未核读但不影响分类的题，可以进入 PENDING_VISUAL。
视觉未核读且影响答案或题干完整性的题，必须 BLOCKED。
2.7 A/B 独立扫描与差异文件
phase03_laneA_full_scan.csv
phase03_laneB_full_scan.csv
phase03_AB_question_diff.csv
phase03_AB_classification_diff.csv
phase03_AB_source_diff.csv
phase03_resolved_conflicts.md
phase03_unresolved_conflicts.md
phase03_blocked_questions.csv
冲突类型至少包括：
1. A 有题，B 无题。
2. B 有题，A 无题。
3. A/B 题号不同。
4. A/B locator 不同。
5. A/B 部分归属不同。
6. A/B 知识节点不同。
7. A/B 推理题型不同。
8. A/B 答案不同。
9. A/B 对是否需要视觉核读判断不同。
10. A/B 对是否可入学生稿判断不同。
2.8 阶段审查包
phase03_GPT_commander_review_packet.md
phase03_Governor_interim_gate.md
phase03_Confucius_interim_learning_value_check.md
GPT-5.5 Pro 阶段审查包必须包含：
1. raw source registry 摘要。
2. suite registry 摘要。
3. 总题量。
4. 思维题量。
5. 推理题量。
6. 交叉题量。
7. blocked 题量与原因。
8. A/B 冲突数量与类型。
9. 视觉待核读题量。
10. HS02 当前状态。
11. 2026 二模 missing 状态。
12. 推理题型树覆盖情况。
13. 思维材料信号链覆盖情况。
3. 下一阶段扫描顺序：思维部分与推理部分如何并行分工
下一阶段不能按先思维、后推理的串行方式做。原因：一部分题会交叉，尤其是科学思维、逻辑规则、论证评价、假言推理、辩证思维与形式逻辑结合题。应采用“同源逐套扫描，双矩阵并行挂载”。
3.1 总体顺序
第一步：清源
第二步：定 suite
第三步：逐套逐题切题
第四步：思维矩阵与推理矩阵并行挂载
第五步：A/B diff
第六步：冲突裁决
第七步：blocked list 锁定
第八步：提交 Phase 03 审查包
3.2 Codex lane A 分工
Codex lane A 做主生产线：
1. 生成 canonical source_id。
2. 生成 suite_id。
3. 逐套切出全部 question_id。
4. 建立 phase03_question_coverage_matrix。
5. 对每题做初判：思维 / 推理 / 交叉 / 待判。
6. 对思维题填 thinking_signal_chain_matrix。
7. 对推理题填 reasoning_question_attachment_matrix。
8. 建立 visual_fallback_queue。
9. 标记 blocked questions。
10. 生成 laneA_full_scan。
Codex lane A 的重点是完整性：
宁可多列待判题，不能漏题。
宁可把边界题列入交叉，不能提前单线归类。
宁可 BLOCKED，不能编答案。
3.3 ClaudeCode lane B 分工
ClaudeCode lane B 做独立生产和复核线：
1. 不读取 lane A 分类结论。
2. 自行扫描 56 个 raw source。
3. 自行建立 suite/question inventory。
4. 自行标注思维、推理、交叉、待判。
5. 自行识别 PPTX 图片、表格、批注、视觉风险。
6. 自行提出 missing source、missing question、classification conflict。
7. 输出 laneB_full_scan。
ClaudeCode lane B 的重点是抓漏：
1. 漏题。
2. 漏小问。
3. 漏选项。
4. 漏答案页。
5. 漏讲评页。
6. 漏 PPTX 图片题。
7. 漏交叉题。
8. 漏推理候选题。
9. 漏同题重复。
10. 漏边界冲突。
3.4 思维部分扫描规则
每一道思维题先进入以下判断链：
1. 材料中出现什么信号。
2. 这个信号可调用哪一类思维或方法。
3. 设问要求学生做什么动作。
4. 答案应落在哪些句子或评分点。
5. 来源例题如何回指。
思维部分分类节点建议先设为：
1. 科学思维特征。
2. 科学思维方法。
3. 辩证思维。
4. 分析与综合。
5. 质量互变。
6. 适度原则。
7. 简单肯定否定到辩证否定。
8. 创新思维。
9. 联想思维。
10. 发散思维与聚合思维。
11. 逆向思维。
12. 超前思维。
13. 综合或交叉。
14. 待判。
每题必须填：
材料信号
可写思维/方法
答题动作
来源例题
例如 HS02 这种题，必须写成：
材料信号：题干中存在动态过程、整体布局、阶段推进、问题解决、旧方案突破等信号。
可写角度池：分析与综合/系统优化/整体性，质量互变/动态性，辩证否定。
答题动作：从三个角度中选择材料最顺的两个写深。
来源例题：2025 海淀二模 Q20。
状态：LOCKED_PENDING_VISUAL，暂不入学生稿。
3.5 推理部分扫描规则
每一道推理候选题都必须先抽逻辑结构：
材料语言 -> 逻辑形式 -> 推理规则 -> 有效式/无效式 -> 答案动作
推理部分分类节点建议先设为：
1. 概念外延与定义。
2. 判断类型识别。
3. 性质判断。
4. 换质推理。
5. 换位推理。
6. 三段论。
7. 联言判断与联言推理。
8. 相容选言推理。
9. 不相容选言推理。
10. 充分条件假言推理。
11. 必要条件假言推理。
12. 充要条件假言推理。
13. 假言连锁推理。
14. 二难推理或复合推理。
15. 矛盾律。
16. 排中律。
17. 同一律。
18. 归纳推理。
19. 类比推理。
20. 求同法。
21. 求异法。
22. 共变法。
23. 剩余法。
24. 论证评价。
25. 逻辑错误辨析。
26. 综合推理。
27. 待判。
推理题不能只填知识节点。必须填：
logical_form
rule_slogan
valid_pattern
trap
answer_action
same_type_question_ids
例如 HS05 不能只写形式逻辑综合，必须拆成：
1. 矛盾律。
2. 充分条件假言推理误用。
3. 三段论中项不周延。
3.6 并行后的融合规则
A/B 融合时必须按以下顺序裁决：
1. 先裁题目是否存在。
2. 再裁题干和选项是否完整。
3. 再裁答案来源。
4. 再裁部分归属。
5. 再裁知识节点。
6. 再裁推理类型。
7. 最后裁是否可入学生稿。
不能先讨论表达好坏。当前阶段不允许写最终表达。
4. 现在最大的内容风险
最大风险是：全量扫描阶段把“题目存在性覆盖”误当成“宝典可写性覆盖”。
具体表现会是：

1. coverage matrix 有题号，但没有材料信号。
2. 推理题挂了题型，但没有 logical_form。
3. 主观题有知识点，但没有答案落点。
4. 选择题有答案，但没有完整四选项。
5. PPTX 图片题被标为 extracted，却没有视觉核读。
6. A/B 都抽到了同一题，却同时继承了同一个误判。
7. 旧稿 locator 行混在 raw source registry 中，后续污染证据池。
这比漏几个文件更危险。因为 Phase 02 已经证明文件读取问题暂时可控，真正的失败点会转移到内容层：
抽到了，不等于读懂了。
分类了，不等于可入宝典。
有题型，不等于有解题动作。
有答案，不等于有评分落点。
当前最容易复发的旧失败是推理部分。它会很自然地退化为：
题型讲解 + 少数例题 + 泛化陷阱
必须强制改为：
题型节点下挂全部题目，逐题写规则、陷阱、同类题、动作。
第二大风险是 HS02 式主观题。它提示本轮不能机械追求唯一标准答案。北京政治讲评与评标中可能存在：
角度池
替代给分
优先角度
材料最顺角度
评分弹性
所以主观题要区分：
必写点
可选角度池
高价值替代角度
不建议写角度
材料最顺路径
5. 是否同意 HS02 融合结论
同意，但状态必须保持为：
LOCKED_PENDING_VISUAL
我同意的部分：
1. 不能写成三点全部必答。
2. 不能写成 3点×2分。
3. 可以写成三个可选角度池。
4. 应优先选择材料最顺的两个角度写深。
5. 辩证否定可以作为高价值补充或替代角度。
6. 最终学生稿中应提示：不要把所有辩证思维知识机械堆上去。
需要微调的地方：
原融合表达：三个可选角度池，优先选材料最顺的两条写深；辩证否定是高价值补充/替代角度。

建议改为：三个可选角度池中，至少锁定两个与材料贴合度最高的角度展开；辩证否定经评标实录确认可作为有效替代或补充角度，但最终学生稿应标注其适用触发信号，避免学生见到改革、创新、突破就机械套辩证否定。
HS02 后续进入学生稿前，还必须补齐四件事：
1. 原卷视觉最终确认：题干、设问、材料无误。
2. 主细则表格截图或定位记录确认。
3. 讲评 PDF 中选择 2 个角度、每角度 1+2 赋分的定位确认。
4. 评标实录中辩证否定有效、辩证思维特征角度可替代给分的定位确认。
HS02 的宝典写法应采用：
题目定位：2025 海淀二模 Q20。
考查方向：辩证思维。
材料信号：整体推进、动态变化、阶段安排、问题解决、突破旧做法。
可选角度池：
  角度一：分析与综合 / 系统优化 / 整体性。
  角度二：质量互变 / 动态性。
  角度三：辩证否定。
考场策略：选材料最顺的两个角度写深。
易错陷阱：把三个角度全部当必答，或只背术语不扣材料。
当前状态：LOCKED_PENDING_VISUAL，暂不入学生稿。
6. 推理部分宝典结构硬要求
推理部分必须以“题型树 + 全题挂载 + 逐题动作”为唯一合法结构。任何只讲题型、不挂全部题的稿件，直接判失败。
6.1 推理部分总结构
必须生成四层结构：
第一层：题型树
第二层：每个题型的规则与口令
第三层：该题型下全部真题归档
第四层：每道题的解题动作
禁止结构：
1. 先讲归纳推理，再随便举几题。
2. 先讲类比推理，再配几个例子。
3. 三段论只写规则，不挂全部题。
4. 假言推理只写有效式和无效式，不逐题回到材料。
5. 综合题只写综合推理，不拆具体规则。
6.2 每个题型章必须包含
每个题型节点固定写成：
题型名称
考查规则
规则口令
常见陷阱
本题型全部题目清单
逐题归档
同类题迁移动作
其中“本题型全部题目清单”必须列出真实 question_id。不能用示例题代替全部题。
格式：

本题型全部题目清单：
Q-R-001
Q-R-007
Q-R-014
Q-R-022
后续正文中必须逐题出现：
Q-R-001
Q-R-007
Q-R-014
Q-R-022
缺一题，推理部分不通过。
6.3 每道推理题必须包含
逐题模板必须固定：
题目定位：
suite_id：
question_id：
stable_locator：

题型归属：
primary_reasoning_type：
secondary_reasoning_type：
是否一题多法：

材料信号：
题干中哪个词、哪句话、哪个结构触发该规则。

逻辑形式：
把材料语言转成 P、Q、S、M、P 等逻辑结构。

规则口令：
一句话记住本题规则。

有效式或无效式：
本题使用哪条有效推理式，或错在哪里。

解题动作：
Step 1：抽取对象、条件、结论。
Step 2：转成逻辑形式。
Step 3：套规则判断有效或无效。
Step 4：回到选项或设问。
Step 5：形成答案句。

答案落点：
选择题写正确项和排除理由。
主观题写可得分表达。

易错陷阱：
本题最容易误判的地方。

同类题：
列出同一题型下其他 question_id。
6.4 推理部分必须建立硬校验
必须执行四个一致性校验：
校验一：coverage matrix 中所有 section_scope=推理 的题，必须出现在 reasoning attachment matrix。
校验二：reasoning attachment matrix 中所有题，必须出现在推理宝典正文。
校验三：每个题型章的全部题目清单，必须等于 attachment matrix 中该题型题目集合。
校验四：正文每一道推理题，必须有 logical_form、rule_slogan、trap、answer_action。
任一不一致，不能进入 Claude/Opus。
6.5 推理综合题处理规则
综合题不能成为垃圾桶。每道综合题必须拆解：
综合题名称：形式逻辑综合
涉及规则：
  规则一：矛盾律
  规则二：充分条件假言推理
  规则三：三段论
每个规则对应的材料信号：
每个规则对应的错误类型：
每个规则对应的答案动作：
HS05 的最低合格写法：
HS05：2026 东城期末 Q17(2)
归属：推理部分
primary_type：形式逻辑综合
secondary_types：矛盾律；充分条件假言推理误用；三段论中项不周延
规则口令：
  矛盾律：同一时间、同一方面，不能既肯定又否定。
  充分条件：肯前可肯后，否后可否前；肯后、否前都无效。
  三段论：中项至少周延一次。
解题动作：
  先找互相冲突的判断。
  再把条件句写成 P -> Q。
  再检查是否肯后或否前。
  最后检查三段论中项是否周延。
6.6 推理题型树只能由真实题源反推
可以先用教材逻辑搭预设树，但最终正文题型树必须由真实题源修正。
执行要求：

1. 先建 provisional_reasoning_typology_tree。
2. 全量扫描后生成 observed_reasoning_typology_tree。
3. 没有真实题的节点不得在宝典正文中长篇展开。
4. 有真实题但预设树没有的节点，必须新增。
5. 交叉题必须双挂载。
6. 待判题必须列入 unresolved，不得消失。
6.7 推理部分最终进入成文化前的最低门槛
1. 推理题总数明确。
2. 每道推理题有 stable locator。
3. 每道推理题有题型归属。
4. 每道推理题有 logical_form。
5. 每道推理题有 rule_slogan。
6. 每道推理题有 trap。
7. 每道推理题有 answer_action。
8. 每道推理题有 same_type_question_ids。
9. 选择题有完整选项与答案。
10. 主观题有设问与评分落点。
达不到以上标准，Claude/Opus 不能介入。
最后裁决
CONDITIONAL GO
允许执行：
全量逐套逐题扫描
全量分类
思维材料信号链矩阵
推理题型挂载矩阵
A/B 独立 diff
视觉 fallback 队列
blocked questions 锁定
Phase 03 commander review packet
继续禁止：
学生稿
Claude/Opus 成文化
Word/PDF
最终 PASS
Phase 03 的核心验收句只有一句：
每一道题都必须能从 source locator 回到原题，并且能在思维链矩阵或推理挂载矩阵中找到自己的位置。

你是 GPT-5.5 Pro，作为飞哥政治庄园四线工作流里的“总指挥/内容压力测试官”。请你审阅本轮 Phase 03 的阻塞/差异包，给出下一步裁决。

## 背景

任务：从0重跑北京高考政治 选必三《逻辑与思维》，分成两个最终部分：

1. 思维部分：完全模仿已成功的哲学宝典做法。每个“思维/方法”像哲学原理方法论一样处理，形成“材料信号 -> 可写思维/方法 -> 答题动作 -> 来源例题”的学生可迁移体系。
2. 推理部分：按题型分类，把所有对应真题放在同类题型下面，例如三段论、充分/必要条件假言推理、联言/选言推理、归纳/类比、逻辑三律等；每类都要有规则口令、易错陷阱、解题动作、同类题归档。

用户明确批评过：上一版没有穷尽每一道题，内容质量远不如哲学宝典，属于偷懒。因此本轮必须严格四线：Codex A 自己跑、ClaudeCode B 独立跑、GPT-5.5 Pro 阶段指挥和内容审查、Claude/Opus 只在证据锁定后负责成品化表达。

当前日期：2026-05-04。
本轮目录：/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04

## 最高限制

- 这是 Phase 03 blocker/diff review，不是 PASS 包。
- 请不要批准学生稿、Claude/Opus 成文化、Word/PDF、最终 PASS。
- 你的建议必须回到本地证据矩阵和源文件，不要凭空新增事实。

## Phase 02 你此前给出的方向

你此前给出 CONDITIONAL GO，允许进入 full suite question scan and classification，要求：

- 每一道题必须能回到 source locator；
- 每一道题必须落到思维链矩阵、推理挂载矩阵，或 blocked list；
- HS02 等视觉题必须锁定到视觉确认后才能入稿；
- 推理部分需要 logical_form、rule_slogan、valid/invalid pattern/trap、answer_action、same_type_question_ids；
- 继续禁止学生稿、Opus 成文化、Word/PDF、最终 PASS。

## Phase 03 已完成工作

### Codex Lane A

- 正式 Phase03 初始矩阵：528 行 question/sub-question rows。
- thinking rows: 73。
- reasoning rows: 166。
- blocked rows: 42。
- visual blocker rows: 4。
- 视觉恢复种子：2025海淀二模 Q20、2026丰台一模 Q18(2)。
- 发现 A 线有噪声：重复行、answer/rubric/reference text 混入 question matrix。

### ClaudeCode Lane B

- Phase03 独立全量扫描已完成，但实际更像 candidate scan：
  - source registry 56 sources；
  - suite registry 17 suites；
  - question/candidate rows 约 53/59；
  - thinking 10；
  - reasoning 27；
  - visual blockers 11；
  - missing/conflicts 5 类。
- Lane B 明确承认 14 unread sources、4 pending suites，不能算 every-question coverage。

### A/B Diff 结论

Verdict: NO_PASS_CONTINUE_EXTRACTION

Counts:

- Lane A question/subquestion rows: 528
- Lane A in-scope/cross keys: 122
- Lane B question/candidate rows: 59
- Common A/B keys: 46
- A-only in-scope/cross keys: 76
- B-only candidate keys: 7

Critical findings:

1. P1: Lane B is not literal every-question coverage; it is useful candidate scan only.
2. P1: Lane B initially missed 2026丰台一模 Q18(2).
3. P1: HS02 / 2025海淀二模 Q20 originally still needed Lane B visual confirmation.
4. P2: Lane B unread sources remain.
5. P2: Lane A has noisy duplicates and reference text mixed into question rows.
6. P2: 2026二模 materials are not found in current source boundary; record missing, do not claim nonexistence.

### Focused ClaudeCode Patch 完成

为修正两个 P1，已让 ClaudeCode 做窄补丁，禁止学生稿。

Patch result:

1. 2026丰台一模 Q18(2)
   - 原卷 042 render page_07 视觉确认：Q18(2) 是“分别分析以上推理的类型，判断是否正确，并说明理由。（6分）”。
   - 043 细则 SLIDE 35 明确：知识板块“逻辑与思维”。
   - 甲：必要条件假言推理，肯定后件式，前提真实，正确。
   - 乙：三段论推理，“带动居民消费”作为大项在前提中不周延、结论中周延，犯“大项不当扩大”，错误。
   - 结论：PASS_TO_FUSION / A-formal / VISUAL_CONFIRMED_LANE_B。

2. 2025海淀二模 Q20 / HS02
   - 原卷 008 render page_07 视觉确认：Q20 设问“结合材料，运用辩证思维知识，谈谈如何更好地坚持共享发展理念推进共同富裕。”
   - 009/010/011 三源一致：角度池，从 3 个角度中选 2；分析与综合/整体性、质量互变/动态性、辩证否定；矛盾分析法最多 2 分。
   - 明确不是三点全必答。
   - 结论：PASS_TO_FUSION / A-formal / VISUAL_CONFIRMED_LANE_B，HS02 Lane B visual lock 解除。

### Codex Lane A 去重拆分完成

脚本：02_extraction/phase03_dedup_split_laneA_matrix.py

结果：

- Input rows: 528
- Canonical paper/question rows: 358
- Support/reference rows split out: 46
- Duplicate/removed rows logged: 170
- Duplicate suite/question keys in input: 118
- Canonical in-scope or cross candidates: 119
- Canonical locked rows after focused patch context: A matrix本身仍需后续写回状态；补丁文件已确认两个锁定点可进入 fusion。

Meaning:

- 原卷题目矩阵和细则/讲评/参考支撑矩阵已经拆开；
- 这一步不等于学生稿晋级，只是后续融合底座变干净；
- 仍有 2026二模 missing、Lane B not every-question、A-only/B-only conflict、choice answer pairing、视觉/OCR全页题号恢复等任务。

## 需要你裁决的问题

请你用非常严格的总指挥口吻回答：

1. 当前是否可以从 Phase03 进入 Phase04“补缺式证据融合/同类题归档”？还是必须继续 Phase03 full every-question coverage？
2. 对 Lane B 不可能短时间变成 528 行 every-question matrix 的情况，你建议怎么做才不算偷懒？例如是否以 Codex A canonical 358 行作为 every-question control base，再让 ClaudeCode B 对 A-only 高风险/高价值题做 targeted independent verification？
3. 你认为下一步最优先的 5 个任务是什么？请按 P0/P1/P2 排序。
4. 对思维部分和推理部分分别给出“不许进学生稿”的硬门槛。
5. 你认为 2026丰台一模 Q18(2) 和 2025海淀二模 Q20 现在是否可以进入 fusion evidence pool？请只回答是否可以进 evidence fusion，不要批准学生稿。
6. 请给出一个短的 verdict，格式必须是：
   - GO_TO_PHASE04_TARGETED_FUSION
   - STAY_IN_PHASE03_FULL_COVERAGE
   - GO_BUT_WITH_BLOCKERS

请记住：本轮目标是最终达到哲学宝典级质量，不是快速糊一份。

我会按 gate 逻辑裁决，不把候选扫描等同于穷尽覆盖；重点看是否已有干净控制底座，是否允许用 targeted verification 替代 B 线全量重复扫描。
Thought for 5m 24s
裁决：GO_BUT_WITH_BLOCKERS
可以从 Phase03 进入 Phase04 的“补缺式证据融合 / 同类题归档”，但 Phase03 不能宣布 full every-question coverage 已完成。
下一阶段的性质必须改名为：
Phase04 targeted evidence fusion with open coverage blockers
允许做：
1. 用 Codex A canonical 358 行作为 every-question control base。
2. 用 canonical in-scope/cross 119 行作为内容融合主控制表。
3. 对 A-only、B-only、高风险视觉题、推理题、主观题做 targeted independent verification。
4. 开始同类题归档，但只能归档到 evidence pool，不得进入学生稿。
5. 对思维部分和推理部分建立 locked / pending / blocked 三态体系。
继续禁止：
1. 学生稿。
2. Claude / Opus 成文化。
3. Word / PDF。
4. 最终 PASS。
5. 声称已穷尽北京全部可获得材料。
6. 声称 Lane B 已完成 every-question coverage。
当前不能用 GO_TO_PHASE04_TARGETED_FUSION，因为 B 线还有 14 unread sources、4 pending suites，A-only 76 个 in-scope/cross keys 尚未被独立复核，A 线刚完成去重拆分，choice-answer pairing、视觉/OCR 全页题号恢复仍未收口。
也不必退回 STAY_IN_PHASE03_FULL_COVERAGE，因为 A 线 canonical base 已经把 528 噪声矩阵压成 358 个原卷题目行，支撑材料已拆出，两个 P1 视觉点也已补锁。继续要求 B 短期复制 528 行矩阵会浪费时间，且不会自动提高成品质量。
正确做法是：进入 Phase04，但把 Phase03 的未闭合项带入 Phase04 blocker gate，任何未锁定题不得进入学生稿。

1. 是否允许进入 Phase04
允许进入，但只能进入“带 blocker 的补缺式证据融合”。
当前状态判断：

Phase03 coverage base: usable but not closed
Lane A canonical matrix: usable as control base
Lane B independent scan: useful as candidate and risk detector, not full coverage
Focused patch: resolves two P1 visual blockers
A dedup split: improves matrix hygiene
Final student evidence lock: not yet
因此阶段裁决为：
Phase03 does not PASS.
Phase04 targeted fusion may start.
Student-facing production remains blocked.
Phase04 的第一原则：
A canonical base controls completeness.
B targeted verification controls independence.
Governor controls whether unresolved A-only evidence can ever move forward.
2. Lane B 无法短期变成 528 行 every-question matrix 时，怎样处理才不算偷懒
可以接受不让 Lane B 复制 528 行矩阵，但必须满足三个条件：
1. A canonical 358 行成为 every-question control base。
2. B 不再承担机械复刻任务，改为风险定向独立复核。
3. 每个未被 B 覆盖的 A 线条目必须有状态，不允许静默放行。
2.1 A canonical 358 行的合法定位
A canonical 358 行可以作为：
every-question control base
不能作为：
final truth base
也就是说，A 线可以控制“有哪些题”，但不能单独证明“这些题怎么讲、怎么归类、怎么入稿”。
必须新建状态表：

phase04_control_base_status.csv
字段至少包括：
canonical_question_id
suite_id
source_id
stable_locator
scope_status: in_scope / cross / out_of_scope / pending
A_status
B_status
fusion_status
verification_level
answer_pairing_status
visual_status
student稿_permission
blocker_reason
建议状态分级：
L0_BLOCKED
L1_A_ONLY_PENDING_B_TARGET
L2_A_B_COMMON
L3_A_PLUS_B_TARGET_CONFIRMED
L4_LOCKED_FOR_FUSION
L5_ELIGIBLE_FOR_FUTURE_STUDENT_DRAFT
当前最多只能推进到：
L4_LOCKED_FOR_FUSION
不得推进到学生稿。
2.2 Lane B targeted verification 的最低范围
Lane B 不需要复刻 528 行，但必须 100% 独立复核以下集合：
1. A-only in-scope/cross keys：76 个，全部复核。
2. B-only candidate keys：7 个，全部回源裁决。
3. A blocked rows：42 个，全部确认 blocked 原因。
4. A visual blockers 与 B visual blockers 的并集，全部视觉确认或继续 blocked。
5. 14 unread sources，至少做 source/suite 级补读，确认是否含 in-scope/cross 题。
6. 4 pending suites，必须给出 pending 原因、题量风险、是否影响 119 个主控制候选。
7. 所有推理主观题，全部复核。
8. 所有形式逻辑综合题，全部复核。
9. 所有选择题答案配对不稳的题，全部复核。
10. 所有 PPTX 内嵌图片、图形批注、学生答卷图片相关题，全部复核。
此外，必须做抽样哨兵：
A/B common keys 抽查不少于 15%。
A 判 out_of_scope 的 canonical rows 抽查不少于 10%。
如果抽样发现系统性漏判，立即扩大到对应 suite 全量复核。
这样处理才不算偷懒。原因是它保留了 B 线的独立性，同时把 B 的资源用在最容易导致失败的地方：漏题、误归类、视觉误读、答案错配、推理题误挂载。
2.3 A-only 题的处理规则
A-only 题不能自动进入锁定池。
规则：

A-only + 高风险：必须 B targeted verify。
A-only + 主观题：必须 B targeted verify。
A-only + 推理题：必须 B targeted verify。
A-only + 选择题但答案/选项完整：可进 pending fusion，不可进 locked。
A-only + 无答案或无选项：blocked。
A-only + 视觉未核：blocked 或 pending_visual。
任何 A-only 题想进入未来学生稿，至少需要：
A raw source locator
B targeted verification
answer/rubric pairing
scope classification
Governor gate note
3. 下一步最优先 5 个任务
P0. 任务 1：冻结 A canonical control base，并给每一行赋状态
产出：
phase04_control_base_status.csv
phase04_canonical_358_index.md
phase04_in_scope_cross_119_index.md
phase04_support_reference_index.md
phase04_removed_duplicates_log.md
要求：
1. 358 行 canonical paper/question rows 固定为控制底座。
2. 46 行 support/reference rows 单独管理。
3. 170 行 duplicate/removed rows 保留日志，不得丢弃。
4. 119 个 in-scope/cross candidates 单独成主控制表。
5. 每一行必须标出 locked / pending / blocked / out_of_scope。
这一步不做完，Phase04 会再次把题目、细则、讲评、重复行混在一起。
P0. 任务 2：执行 Lane B targeted independent verification
产出：
phase04_laneB_targeted_verification_plan.md
phase04_laneB_targeted_verification_results.csv
phase04_Aonly_76_review.csv
phase04_Bonly_7_review.csv
phase04_unread_sources_patch.md
phase04_pending_suites_patch.md
必须覆盖：
A-only 76
B-only 7
14 unread sources
4 pending suites
visual blockers union
blocked rows
推理主观题
形式逻辑综合题
选择题答案配对风险题
硬门槛：
B 不能只确认 A 的结论。
B 必须回到源文件和 locator。
B 必须写出同意、不同意、无法确认三类结果。
无法确认的题不能进 locked fusion。
P0. 任务 3：完成 answer/rubric/visual 三重配对
产出：
phase04_answer_key_pairing_matrix.csv
phase04_rubric_pairing_matrix.csv
phase04_visual_confirmation_matrix.csv
phase04_blocked_questions_final_for_phase04.csv
每道题必须标明：
has_full_stem
has_full_options
has_answer_key
has_rubric_or_commentary
visual_required
visual_confirmed
can_enter_fusion
can_enter_student_draft
阻断规则：
选择题无完整四选项，不能进学生稿。
选择题无可靠答案，不能进学生稿。
主观题无设问，不能进学生稿。
主观题无细则、讲评或可定位答案依据，不能进学生稿。
视觉题未确认，不能进 locked。
P1. 任务 4：推理部分先建 attachment matrix，再做同类题归档
产出：
phase04_reasoning_attachment_matrix.csv
phase04_reasoning_typology_tree_observed.md
phase04_reasoning_same_type_archive.md
phase04_reasoning_logical_form_check.md
phase04_reasoning_trap_action_matrix.md
每个推理题必须有：
question_id
stable_locator
primary_reasoning_type
secondary_reasoning_type
logical_form
rule_slogan
valid_or_invalid_pattern
trap
answer_action
same_type_question_ids
fusion_status
这一任务是 Phase04 的核心。推理部分一旦先写“题型讲解”，必然复发旧失败。
P1. 任务 5：思维部分建立 signal-chain archive
产出：
phase04_thinking_signal_chain_matrix.csv
phase04_thinking_method_archive.md
phase04_thinking_answer_action_matrix.md
phase04_thinking_optional_angle_pool.md
每个思维题必须有：
材料信号
可写思维/方法
答题动作
答案落点
来源例题
同类题
易错陷阱
fusion_status
HS02 这类题必须额外标注：
必写角度
可选角度池
替代给分角度
不建议机械套用角度
评分弹性来源
4. 思维部分“不许进学生稿”的硬门槛
任何思维题出现以下任一情况，禁止进入学生稿。
1. 没有 stable locator。
2. 题干、设问、材料不完整。
3. 主观题没有答案依据、细则依据或讲评依据。
4. 需要视觉确认但尚未 visual_confirmed。
5. 只写知识点名称，没有材料信号。
6. 只写材料复述，没有可写思维/方法。
7. 只有答案结论，没有答题动作。
8. 没有说明为什么从材料能想到该思维方法。
9. 可选角度题被写成全部必答。
10. 替代给分角度被写成唯一标准答案。
11. 同一题多问没有拆成子题。
12. 旧稿结论参与了内容判断。
13. A/B 冲突未解决。
14. blocker_reason 尚未清空。
思维部分最低入稿模板：
题目定位
材料信号
可写思维/方法
答题动作
为什么能想到
答案落点
来源例题
同类题
易错陷阱
缺任何一项，都不能进入学生稿。
5. 推理部分“不许进学生稿”的硬门槛
任何推理题出现以下任一情况，禁止进入学生稿。
1. 没有 stable locator。
2. 题干或设问不完整。
3. 选择题没有完整选项。
4. 选择题没有可靠答案。
5. 主观题没有评分点、讲评依据或可定位答案依据。
6. 只标“推理部分”但没有具体题型。
7. 只标“形式逻辑综合”但没有拆出具体规则。
8. 没有 logical_form。
9. 没有 rule_slogan。
10. 没有 valid_or_invalid_pattern。
11. 没有 trap。
12. 没有 answer_action。
13. 没有 same_type_question_ids。
14. 一题多法没有 primary / secondary 挂载。
15. A/B 对题型或答案存在冲突且未裁决。
16. 视觉题未确认。
17. 推理题没有进入 reasoning_attachment_matrix。
18. reasoning_attachment_matrix 与同类题归档不一致。
推理部分最低入稿模板：
题目定位
题型归属
材料信号
逻辑形式
规则口令
有效式或错误式
解题动作
答案落点
易错陷阱
同类题
特别要求：
综合题不能只进“综合推理”。
每道综合题必须拆成具体规则。
例如：矛盾律、充分条件假言推理、必要条件假言推理、三段论、联言推理、选言推理、归纳、类比等。
6. 2026 丰台一模 Q18(2) 是否可以进入 fusion evidence pool
可以。
理由限于 evidence fusion 层面：

1. Lane B 已视觉确认原卷 042 render page_07。
2. 设问已确认：分别分析以上推理的类型，判断是否正确，并说明理由。
3. 043 细则 SLIDE 35 已确认知识板块为“逻辑与思维”。
4. 甲的类型、推理形式、正确性已经锁定。
5. 乙的类型、错误位置、错误名称已经锁定。
6. 结论为 PASS_TO_FUSION / A-formal / VISUAL_CONFIRMED_LANE_B。
进入 fusion evidence pool 的建议状态：
LOCKED_FOR_FUSION
NO_STUDENT_DRAFT_YET
不得据此批准学生稿。
7. 2025 海淀二模 Q20 是否可以进入 fusion evidence pool
可以。
理由限于 evidence fusion 层面：

1. Lane B 已视觉确认原卷 008 render page_07。
2. 设问已确认：结合材料，运用辩证思维知识，谈谈如何更好地坚持共享发展理念推进共同富裕。
3. 009 / 010 / 011 三源一致支持角度池。
4. 已确认从 3 个角度中选 2。
5. 已确认分析与综合/整体性、质量互变/动态性、辩证否定三个角度池。
6. 已确认矛盾分析法最多 2 分。
7. 已确认不能写成三点全必答。
8. 结论为 PASS_TO_FUSION / A-formal / VISUAL_CONFIRMED_LANE_B。
进入 fusion evidence pool 的建议状态：
LOCKED_FOR_FUSION
OPTIONAL_ANGLE_POOL_CONFIRMED
NO_STUDENT_DRAFT_YET
未来学生稿中必须写清：
三个可选角度池中选材料最顺的两个写深。
辩证否定是有效替代或补充角度。
矛盾分析法有上限，不能当主答案无限展开。
8. 当前最大内容风险
最大风险是：把 Phase04 的“证据融合”误操作成“内容成文化”。
当前已经有两个好消息：A 矩阵清洁度提高，两个 P1 视觉 blocker 解除。
这也会制造一个假象：好像可以开始写宝典了。这个判断是危险的。

真正的风险集中在三处：

1. A-only 76 个 in-scope/cross keys 尚未被独立复核。
2. 推理部分可能先形成题型树，再把少数题塞进去。
3. 思维部分可能把角度池、替代给分、材料信号写成普通知识点总结。
最容易再次失败的路径：
coverage matrix 有题号
reasoning matrix 有题型
thinking matrix 有知识点
然后直接让 Opus 润色
这会再次生成一份“看起来完整、实际不可迁移”的稿子。
下一阶段必须坚持：

先锁证据。
再归同类。
再写动作。
最后才成文化。
9. Phase04 的硬性推进口径
Phase04 可以启动，但只能做以下事情：
1. evidence fusion
2. targeted verification
3. same-type archive
4. thinking signal-chain archive
5. reasoning attachment archive
6. blocked list hardening
7. Governor interim gate
Phase04 不允许做：
1. 学生稿正文。
2. 章节导语。
3. 背诵版口令成品。
4. Word/PDF。
5. Opus rewrite。
6. PASS。
Phase04 结束时必须提交：
phase04_control_base_status.csv
phase04_laneB_targeted_verification_results.csv
phase04_answer_key_pairing_matrix.csv
phase04_rubric_pairing_matrix.csv
phase04_visual_confirmation_matrix.csv
phase04_thinking_signal_chain_matrix.csv
phase04_reasoning_attachment_matrix.csv
phase04_same_type_archive.md
phase04_blocked_questions_final.csv
phase04_Governor_interim_gate.md
phase04_GPT_review_packet.md
缺任何核心矩阵，禁止进入学生稿准备阶段。
短 verdict
GO_BUT_WITH_BLOCKERS

