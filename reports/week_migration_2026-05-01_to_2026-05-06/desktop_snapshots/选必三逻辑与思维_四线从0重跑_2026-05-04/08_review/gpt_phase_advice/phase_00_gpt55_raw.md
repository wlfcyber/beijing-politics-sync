## 结论：CONDITIONAL GO

可以启动纠偏后的 Phase 01 生产，但只能进入“源清点、题目挂载、覆盖矩阵、双 lane 独立生产”的阶段。
严禁进入最终学生稿、Word/PDF 成品稿、PASS 宣告。

当前状态满足启动条件：已有四线重跑目录、主要求、用户框架、start card、source ledger 初稿、Governor startup patch。
当前状态不满足成品条件：ClaudeCode lane B 尚未返回，Claude Opus 尚未介入，覆盖矩阵未到 suite/question 级，推理部分尚未逐题挂题型，Word/PDF 未验证，Governor 与 Confucius 未硬 gate。

因此判定为：

```text
CONDITIONAL GO for Phase 01 source inventory and independent production scaffolding.
STOP for final student-facing draft.
STOP for Word/PDF generation.
STOP for PASS.
```

---

# 1. STOP / GO / CONDITIONAL GO 判断

## 1.1 当前判定

```text
CONDITIONAL GO
```

允许做：

1. Codex lane A 独立源清点。
2. ClaudeCode lane B 独立源清点。
3. suite/question 级覆盖矩阵搭建。
4. 思维部分与推理部分的结构框架重建。
5. 推理部分“题型挂题”体系设计。
6. 对旧稿进行 failure audit，但旧稿只能作为问题定位材料，不能作为证据母稿。
7. 生成内部审查对象，不生成学生最终稿。

禁止做：

1. 禁止宣称已穷尽所有题。
2. 禁止把旧版内容继承为底稿。
3. 禁止让 Claude Opus 直接扩写最终宝典。
4. 禁止制作 Word/PDF 成品。
5. 禁止提交 Governor final PASS。
6. 禁止把分类总结当成推理部分宝典。
7. 禁止把“条目数量”当成“题目覆盖率”。

## 1.2 转入 GO 的最低条件

只有同时满足以下条件，才能从 CONDITIONAL GO 升级为 GO：

```text
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
```

---

# 2. Codex lane A 下一步生产任务

Codex lane A 的任务是“本地总控生产主线”，重点是建立可审查、可回滚、可 diff 的覆盖体系。当前不要写学生成品稿。

## 2.1 Codex lane A 立即任务

### A1. 建立 source registry

输出文件建议：

```text
A_source_registry.md
A_source_registry.json
A_source_inventory_notes.md
```

每个 source object 至少包含：

```text
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
```

硬规则：

1. 旧 artifact 只能标记为 `locator_only` 或 `failure_reference`。
2. 不允许把旧稿内容写入 `raw_source`。
3. 框架 PDF 可以作为课程框架来源，但不能自动替代真题来源。
4. 每份文件都要有读取状态，失败也要登记失败原因。

### A2. 建立 suite registry

输出文件建议：

```text
A_suite_registry.md
A_suite_registry.json
```

suite 指“一套题、一份试卷、一份讲义、一份专项练习、一组同源材料”。

每个 suite 至少包含：

```text
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
```

必须做到：

1. 不以文件名猜题量。
2. 每套题必须经过人工式结构确认。
3. PDF、图片、漫画、表格、材料页必须进入 visual fallback 队列。
4. 发现同一题跨多个文件出现时，要建立 duplicate map。

### A3. 建立 question coverage matrix

输出文件建议：

```text
A_question_coverage_matrix.xlsx
A_question_coverage_matrix.md
A_question_coverage_matrix.json
```

每道题至少一行：

```text
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
```

硬规则：

1. 每道题必须有 stable locator。
2. 没有 locator 的题不能进入宝典。
3. 选择题无完整选项，不得生成选择题解析。
4. 主观题无设问，不得生成答案落点。
5. 只有知识点名而无材料触发点，判为未完成。
6. 推理题只写“属于归纳推理”不合格，必须挂到具体题型和解题步骤。

### A4. 思维部分生产框架

思维部分需要恢复哲学宝典式结构。每题条目必须包含：

```text
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
```

思维部分不能写成章节摘要。必须体现“材料如何触发知识调用”。

### A5. 推理部分生产框架

推理部分由 Codex lane A 先搭骨架，暂不做最终语言润色。骨架格式见第 6 节。

### A6. 产出 lane A review packet

Codex lane A 完成 Phase 01 后，必须提交给 GPT-5.5 Pro 的对象：

```text
A_source_registry
A_suite_registry
A_question_coverage_matrix
A_reasoning_typology_map
A_unresolved_source_failures
A_duplicate_question_map
A_blocked_questions_list
A_sample_10_question_drafts
```

其中 `A_sample_10_question_drafts` 必须包含：

1. 思维部分选择题 2 道。
2. 思维部分主观题 2 道。
3. 推理部分选择题 2 道。
4. 推理部分主观题 2 道。
5. 图表、漫画、表格或扫描材料题至少 1 道。
6. 一题多法或跨知识点题至少 1 道。

---

# 3. ClaudeCode lane B 下一步生产任务

ClaudeCode lane B 的任务是“独立复核生产线”，不能复制 Codex lane A 的判断。它要独立读源、独立建 inventory、独立标记题目与缺口。

## 3.1 ClaudeCode lane B 当前任务状态

Phase 00 显示：

```text
ClaudeCode lane B Phase 01 independent source-inventory task is still running.
```

因此下一步是完成并提交独立 inventory，不得进入写稿阶段。

## 3.2 ClaudeCode lane B 立即任务

### B1. 独立 source inventory

输出：

```text
B_source_inventory.md
B_source_inventory.json
B_source_failures.md
```

要求：

1. 不引用 Codex lane A 的 source_id 作为判断依据。
2. 自行列出全部发现的原始文件。
3. 对每个文件给出读取状态。
4. 对 PDF、图片、PPT、Word、扫描件分别标注处理风险。
5. 标出哪些材料含题目，哪些含答案，哪些含评分说明。

### B2. 独立 suite/question 识别

输出：

```text
B_suite_question_inventory.md
B_suite_question_inventory.json
```

每条至少包含：

```text
detected_suite:
detected_question:
source_locator:
question_type:
section_scope:
answer_key_detected:
rubric_detected:
visual_required:
confidence:
```

ClaudeCode lane B 的核心责任是发现 Codex lane A 漏掉的题，特别是：

1. PDF 中页眉页脚附近题号。
2. 图片中的漫画题。
3. PPT 内嵌题。
4. Word 表格题。
5. 扫描材料中被 OCR 漏掉的选项。
6. 一题多问中的第二问、第三问。
7. 同一材料下多个设问。
8. 答案页与题目页分离的套题。
9. “思维”与“推理”交叉题。
10. 推理题中被误标为普通材料题的题。

### B3. 与 Codex lane A diff

ClaudeCode lane B 完成后，Codex 总控必须生成：

```text
A_B_source_diff.md
A_B_suite_diff.md
A_B_question_diff.md
A_B_classification_diff.md
```

diff 维度：

```text
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
```

硬规则：

1. A 与 B 不一致时，不得自动取多数。
2. 不一致项进入 `conflict_queue`。
3. conflict 未解决，相关题不得进入最终稿。
4. A 与 B 都没有答案来源的题，不得编造答案。
5. A 与 B 都漏掉但 Governor later发现的题，触发回滚。

---

# 4. Claude Opus 什么时候可以介入、只能做什么、不能做什么

## 4.1 介入时机

Claude Opus 现在不能介入最终成品化。
它只能在以下对象齐备后介入：

```text
C1: A_source_registry completed.
C2: B_source_inventory completed.
C3: A_B_diff completed.
C4: question_coverage_matrix 至少完成 first locked pass.
C5: 每道进入样稿的题都有 source locator。
C6: blocked_questions_list 已单独列出。
C7: Governor 确认旧稿没有作为证据母稿。
```

推荐介入节点：

```text
Phase 02 after source and coverage lock, before final Word/PDF.
```

## 4.2 Claude Opus 可以做什么

Claude Opus 的角色是“教学文本成品化”，不是源审查官。允许做：

1. 把 Codex lane A 与 ClaudeCode lane B 已确认的题目条目改写成学生可读表达。
2. 将“材料触发点、设问、为什么能想到、答案落点”串成教学链条。
3. 将推理部分规则口令改成可背、可迁移的表达。
4. 优化章节导语、题型导语、学习方法提示。
5. 合并同类题的复盘，但必须保留每道题独立条目。
6. 对语言做降噪，删除 pipeline、audit、source ledger 等内部术语。
7. 统一术语风格，例如“判断依据”“调用路径”“落点句式”“易错陷阱”。
8. 为每个题型补“先看什么、再判什么、最后怎么写”的步骤化说明。
9. 对主观题答案落点做学生化表达，但不得改变原始评分点。
10. 生成“考场口令”和“错因提醒”。

## 4.3 Claude Opus 不能做什么

严格禁止：

1. 不得新增题目。
2. 不得删除题目。
3. 不得自行判断答案正确性。
4. 不得补全缺失选项。
5. 不得补写缺失评分细则。
6. 不得把没有 source locator 的题写进正文。
7. 不得把旧稿改写为新稿。
8. 不得合并多道题导致逐题覆盖消失。
9. 不得把推理部分压缩为题型总述。
10. 不得在学生稿中出现 source registry、coverage matrix、Governor、Confucius、lane A、lane B 等内部语言。

## 4.4 Claude Opus 输入格式

交给 Claude Opus 的包必须是“锁定题目包”，不是杂乱源文件：

```text
opus_input_packet:
  locked_question_entries:
  source_locator_per_question:
  verified_answer_key:
  verified_rubric_or_answer_points:
  reasoning_typology_map:
  blocked_questions_excluded:
  style_rules:
  forbidden_actions:
```

Claude Opus 输出必须带结构标签：

```text
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
```

---

# 5. GPT-5.5 Pro 后续必须审查的 trigger objects

GPT-5.5 Pro 的任务是内容总审稿与压力测试，不充当源证据裁判。它审查流程完整性、覆盖逻辑、风险、题型挂载、学生稿质量门槛。

必须审查以下 trigger objects：

## 5.1 Phase 01 source trigger objects

```text
T01_A_source_registry
T02_B_source_inventory
T03_A_B_source_diff
T04_source_failure_log
T05_locator_only_artifact_list
```

审查点：

1. 是否把旧 artifact 误列为 evidence。
2. 是否有文件未分类。
3. 是否有 PDF、图片、PPT、Word、扫描件未进入 fallback 计划。
4. 是否存在“读取失败但未阻断”的源。
5. 是否存在“框架 PDF 替代真题源”的风险。

## 5.2 Suite/question coverage trigger objects

```text
T06_A_suite_registry
T07_B_suite_question_inventory
T08_A_B_question_diff
T09_question_coverage_matrix
T10_duplicate_question_map
T11_blocked_questions_list
```

审查点：

1. 是否到 suite/question 级。
2. 是否每题有 stable locator。
3. 是否每题有题型、知识点、设问类型。
4. 是否一题多问被拆开。
5. 是否同题重复被正确映射。
6. 是否交叉题被双挂载。
7. 是否 blocked questions 被排除出正文。

## 5.3 思维部分 trigger objects

```text
T12_thinking_part_question_entries
T13_thinking_principle_method_map
T14_thinking_material_trigger_map
T15_thinking_sample_drafts
```

审查点：

1. 是否逐题处理。
2. 是否有材料触发点。
3. 是否解释为什么能想到该知识。
4. 是否有答案落点。
5. 是否有易错陷阱。
6. 是否避免章节摘要化。

## 5.4 推理部分 trigger objects

```text
T16_reasoning_typology_map
T17_reasoning_question_attachment_matrix
T18_reasoning_rule_slogans
T19_reasoning_trap_matrix
T20_reasoning_step_templates
T21_reasoning_all_question_entries
```

审查点：

1. 是否所有推理题都挂到题型。
2. 是否每个题型下面列出全部题。
3. 是否每道题有规则口令。
4. 是否每道题有易错陷阱。
5. 是否有解题步骤。
6. 是否保留一题多法。
7. 是否把形式逻辑题与非形式推理题区分清楚。
8. 是否把“归纳、类比、演绎、三段论、复合判断、假言推理、模态或关系判断”等节点处理到可解题层级。

## 5.5 Claude Opus trigger objects

```text
T22_opus_input_packet
T23_opus_student_text_output
T24_opus_change_log
T25_internal_language_leak_check
```

审查点：

1. Opus 是否只改写已锁定题。
2. 是否新增、删除或合并题。
3. 是否改变评分点。
4. 是否漏掉 trigger chain。
5. 是否出现内部流程语言。
6. 是否把宝典语言写成空泛鸡汤。

## 5.6 最终成品 trigger objects

```text
T26_final_student_draft_md
T27_final_docx
T28_final_pdf
T29_layout_validation_report
T30_Governor_gate_report
T31_Confucius_gate_report
T32_final_PASS_packet
```

审查点：

1. Word 与 PDF 内容是否一致。
2. 目录、页眉、分页、表格、题号是否稳定。
3. 选择题选项是否完整。
4. 主观题答案点是否没有断裂。
5. 学生稿是否无 audit/pipeline 语言。
6. Governor 与 Confucius 是否真实执行。
7. 是否存在“版式通过但内容未通过”的假 PASS。

---

# 6. 推理部分如何做成宝典

核心要求：

```text
题型 -> 全部题目 -> 规则口令 -> 易错陷阱 -> 解题步骤
```

推理部分的失败根因通常是“先讲题型，再举几个例题”。本轮必须改成“每一个题型节点下面挂全部题，每一道题都有可复现解法”。

## 6.1 推理部分总目录结构

建议结构：

```text
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
```

具体题型名称应由本地题源决定，上面只是骨架。不能为了套目录而强行分类。若题源里没有某类题，保留到“未出现或暂未纳入”记录，正文不空写。

## 6.2 每个题型节点必须有 7 个组件

每个题型章固定格式：

```text
题型名称:
考查规则:
规则口令:
本题型全部题目清单:
逐题精讲:
易错陷阱总表:
迁移训练口令:
```

其中“本题型全部题目清单”必须列出所有 question_id：

```text
本题型全部题目清单
Q-R-001
Q-R-004
Q-R-009
Q-R-015
...
```

只要 coverage matrix 显示属于该题型，正文必须出现。若题进入 blocked 状态，要在内部 blocked list 中说明，不能悄悄遗漏。

## 6.3 每道推理题的条目模板

每道题必须按以下模板生产：

```text
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
```

## 6.4 推理题必须先抽形式，再回材料

推理部分特别容易写成政治材料分析。必须强制执行：

```text
材料语言 -> 逻辑形式 -> 推理规则 -> 选项/答案
```

示例规则，不引用具体题源：

```text
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
```

## 6.5 推理题型挂载矩阵

必须生成：

```text
reasoning_question_attachment_matrix
```

字段：

```text
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
```

验收规则：

1. coverage matrix 中 `section_scope = 推理` 的每道题，必须出现在 attachment matrix。
2. attachment matrix 中每道题，必须出现在正文。
3. 正文每道题，必须回指到 matrix。
4. matrix 与正文题号不一致，直接阻断。
5. 一题多法必须双挂载，不得只挂一个节点。
6. “综合题”不能成为逃避分类的垃圾桶，必须说明综合在哪些规则上。

## 6.6 题型章示范骨架

```text
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
```

该骨架必须被真实 question_id 填满。没有真实题号时不能生成假题号。

---

# 7. 最可能导致再次失败的 10 个风险

## 风险 1：旧稿变成隐形母版

表现：

```text
新稿语言、结构、例题顺序与旧稿高度相似。
```

后果：

```text
纠偏名义上重跑，实质上修补旧稿。
```

阻断措施：

```text
旧稿只能进入 failure audit 和 locator-only 列表。
任何正文内容必须回指新 coverage matrix。
```

## 风险 2：覆盖矩阵停留在条目级

表现：

```text
只统计知识点、题型、章节，没有统计每套题、每道题。
```

后果：

```text
看似内容很多，实际漏题无法发现。
```

阻断措施：

```text
必须 suite/question 双层编号。
没有 question_id 的内容不能进入正文。
```

## 风险 3：推理部分再次写成分类讲义

表现：

```text
先讲归纳、类比、演绎，每类配少数例子。
```

后果：

```text
用户核心批评没有解决。
```

阻断措施：

```text
每个题型下面必须列出全部题目清单。
reasoning_attachment_matrix 与正文逐项核对。
```

## 风险 4：PDF、图片、PPT、扫描题漏读

表现：

```text
文本抽取成功就停止，没有处理图表、漫画、表格、图片内文字。
```

后果：

```text
非文本材料题大概率丢失。
```

阻断措施：

```text
所有非文本对象进入 visual fallback queue。
读取失败必须登记，不能静默跳过。
```

## 风险 5：选择题缺选项仍写解析

表现：

```text
只有题干或只有答案，却生成排除法解析。
```

后果：

```text
解析不可验证，容易编造选项逻辑。
```

阻断措施：

```text
选择题必须 has_full_options = yes 且 has_answer_key = yes 才能写。
```

## 风险 6：主观题没有评分落点

表现：

```text
只有知识总结，没有材料对应句和评分点。
```

后果：

```text
不像哲学宝典，学生不能知道怎么得分。
```

阻断措施：

```text
主观题必须包含材料触发点、设问指向、为什么能想到、答案落点。
缺一项为 blocked。
```

## 风险 7：一题多问被当成一题

表现：

```text
第 1 问、第 2 问、第 3 问共用一个解析。
```

后果：

```text
漏掉小问，覆盖率虚高。
```

阻断措施：

```text
question_id 可以拆成 Q001-a、Q001-b、Q001-c。
每个小问单独挂知识点和答案落点。
```

## 风险 8：一题多法被单挂载

表现：

```text
某题同时涉及假言推理和归谬，只挂到假言推理。
```

后果：

```text
学生迁移能力下降，同类题索引断裂。
```

阻断措施：

```text
设置 primary_type 与 secondary_type。
综合题必须列出多个规则触发点。
```

## 风险 9：Claude Opus 过早介入导致文学化

表现：

```text
文本好读，但题目、答案、评分点被压缩或改写过度。
```

后果：

```text
漂亮但不可靠。
```

阻断措施：

```text
Opus 只处理 locked_question_entries。
Opus 输出必须与 question_id 一一对应。
```

## 风险 10：Word/PDF 版式通过掩盖内容未通过

表现：

```text
有目录、有页眉、有 PDF，但覆盖、题号、答案核对没有完成。
```

后果：

```text
形式完成，实质失败。
```

阻断措施：

```text
版式验收只能排在内容 gate 之后。
Governor 和 Confucius 未通过，不得生成 final PASS。
```

---

# 8. 必须阻断最终 PASS 的验收 gate

以下任一 gate 未通过，最终 PASS 必须阻断。

## Gate 0：启动真实性 gate

```text
G0.1 新 run folder 存在。
G0.2 master requirements 存在。
G0.3 四线角色已登记。
G0.4 旧稿被标记为 locator-only 或 failure reference。
G0.5 Governor startup patch 已写明 final PASS blocked。
```

未通过结果：

```text
STOP
```

## Gate 1：源证据 gate

```text
G1.1 A_source_registry 完成。
G1.2 B_source_inventory 完成。
G1.3 A_B_source_diff 完成。
G1.4 每个 raw source 有读取状态。
G1.5 读取失败有 failure log。
G1.6 框架 PDF、真题源、答案源、评分源分开登记。
G1.7 old artifact 没有进入 evidence pool。
```

阻断条件：

```text
任何 source provenance 不清。
任何读取失败被静默跳过。
任何旧稿内容被当作证据。
```

## Gate 2：suite/question 覆盖 gate

```text
G2.1 suite_registry 完成。
G2.2 question_coverage_matrix 完成。
G2.3 每道题有 question_id。
G2.4 每道题有 stable_locator。
G2.5 每道题有 section_scope。
G2.6 每道题有 question_type。
G2.7 一题多问已拆分。
G2.8 duplicate_question_map 完成。
G2.9 blocked_questions_list 完成。
```

阻断条件：

```text
只做到章节覆盖。
只做到知识点覆盖。
只有 entry count，没有 question coverage。
存在无 locator 正文题。
存在 coverage matrix 中有题但正文无题。
```

## Gate 3：答案与评分 gate

```text
G3.1 选择题有完整题干。
G3.2 选择题有完整选项。
G3.3 选择题有可靠答案 key。
G3.4 主观题有设问。
G3.5 主观题有答案来源或评分点来源。
G3.6 答案落点没有超出证据范围。
G3.7 缺答案题进入 blocked list。
```

阻断条件：

```text
缺选项仍写选择题解析。
缺答案仍给确定选项。
缺评分点仍写“标准答案”。
```

## Gate 4：思维部分宝典 gate

```text
G4.1 思维部分每题有材料触发点。
G4.2 每题有设问指向。
G4.3 每题有为什么能想到。
G4.4 每题有答案落点。
G4.5 每题有易错陷阱。
G4.6 每题有同类题索引或说明。
G4.7 内容按原理/方法论组织，但不牺牲逐题覆盖。
```

阻断条件：

```text
概念摘要替代逐题解析。
只写原理，不写材料触发。
只写答案，不写调用路径。
```

## Gate 5：推理部分宝典 gate

```text
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
```

阻断条件：

```text
推理部分只做题型总述。
题型下没有全部题目清单。
coverage matrix 与 reasoning matrix 不一致。
正文少于 matrix 题数。
```

## Gate 6：双 lane diff gate

```text
G6.1 A_B_source_diff 已解决。
G6.2 A_B_question_diff 已解决。
G6.3 A_B_classification_diff 已解决。
G6.4 unresolved_conflict_queue 为空，或相关题进入 blocked list。
G6.5 Governor 记录每个冲突的处理结论。
```

阻断条件：

```text
A 与 B 有冲突但直接进入正文。
用 Codex 结果覆盖 ClaudeCode 结果且无理由。
用 ClaudeCode 结果覆盖 Codex 结果且无理由。
```

## Gate 7：Claude Opus 成品化 gate

```text
G7.1 Opus 只接收 locked_question_entries。
G7.2 Opus 输出与 question_id 一一对应。
G7.3 Opus 没有新增题。
G7.4 Opus 没有删除题。
G7.5 Opus 没有改动答案 key。
G7.6 Opus 没有改动评分点含义。
G7.7 Opus 没有合并题目导致覆盖消失。
G7.8 学生稿无 pipeline 语言。
```

阻断条件：

```text
Opus 直接读旧稿扩写。
Opus 输出没有 question_id 对照表。
Opus 学生化表达改变答案含义。
```

## Gate 8：GPT-5.5 Pro 压力测试 gate

GPT-5.5 Pro 必须执行以下压力测试：

```text
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
```

阻断条件：

```text
任一压力测试发现系统性问题。
同类错误出现 2 次以上。
随机抽查发现正文题无 locator。
推理部分抽查发现题型下缺题。
```

## Gate 9：Governor gate

Governor 必须硬判：

```text
GOV_PASS_SOURCE
GOV_PASS_COVERAGE
GOV_PASS_REASONING_ATTACHMENT
GOV_PASS_THINKING_TRIGGER_CHAIN
GOV_PASS_OPUS_BOUNDARY
GOV_PASS_NO_INTERNAL_LANGUAGE
GOV_PASS_DOCX_VALIDATION
GOV_PASS_PDF_VALIDATION
```

阻断条件：

```text
Governor 只给结论，没有证据对象。
Governor 没有逐 gate 记录。
Governor 对 unresolved conflict 放行。
Governor 对 Word/PDF 未验证放行。
```

## Gate 10：Confucius gate

Confucius 必须从学生学习价值角度审查：

```text
C_PASS_EXAM_USABILITY
C_PASS_TRIGGER_CHAIN
C_PASS_MEMORIZABLE_RULES
C_PASS_TRANSFERABILITY
C_PASS_ERROR_PREVENTION
C_PASS_NO_EMPTY_SUMMARY
C_PASS_REASONING_STEP_CLARITY
```

阻断条件：

```text
学生看完仍不知道材料为什么触发该知识。
学生看完仍不知道推理题第一步做什么。
学生看完只有知识点，没有题目迁移口令。
主观题答案落点不能直接用于考场表达。
```

## Gate 11：Word/PDF validation gate

必须真实验证：

```text
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
```

阻断条件：

```text
只生成 DOCX 未生成 PDF。
只生成 PDF 未核对 DOCX。
图片丢失。
表格溢出。
正文出现内部流程词。
```

## Gate 12：Final PASS packet gate

最终 PASS 包必须包含：

```text
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
```

阻断条件：

```text
没有 known_limitations。
没有 blocked_questions_summary。
没有 A_B diff resolution。
没有 Governor 或 Confucius 独立 gate。
```

---

# Codex 本地总控可直接执行的下一步清单

```text
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
```

Final operative instruction:

```text
Proceed only with Phase 01 inventory, coverage, diff, and reasoning attachment scaffolding.
Do not produce final student-facing manuscript until every question has been located, classified, attached, and gate-checked.
```
