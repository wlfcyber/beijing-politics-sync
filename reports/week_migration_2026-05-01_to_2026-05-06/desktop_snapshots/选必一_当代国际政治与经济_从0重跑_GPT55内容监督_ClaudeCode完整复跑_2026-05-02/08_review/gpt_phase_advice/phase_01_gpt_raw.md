# 下一阶段指挥包

## 1. stop/go 判断

**CONDITIONAL GO。**

可以进入 Phase 02，但入口条件是：

```text
先补齐 G10：
1. 将本次 GPT phase advice 原文保存。
2. Codex 写 codex_response_to_advice。
3. 将本指挥包逐条转成本地 task_plan。
4. 在 DECISION_LOG 记录：GPT 仅为战略建议层，本地证据裁决权归 Codex。
```

G10 未补齐前，可以继续本地源文件扫描和矩阵建设，但不得宣称 Phase 01 正式关闭。

Phase 02 建议命名：

```text
Phase 02：选必一主观题源锁定与 P0/P2 证据矩阵建设
```

---

## 2. 下一阶段第一优先级

第一优先级是 **从 177 个源文件中锁定真正服务于选必一主观题评分术语积累的有效证据池**。

核心目标：

```text
1. 确认哪些套卷含选必一主观题。
2. 确认每道选必一主观题对应的 P0/P2/user-confirmed 证据状态。
3. 建立 suite-by-suite、question-by-question 的题源矩阵。
4. 将 P0 候选 98 个重新区分为：
   a. 真评分细则
   b. 阅卷细则
   c. 评标/评分规则
   d. 答案及评分参考
   e. 名称疑似但证据等级待核
5. 将 P2 讲评/教学材料区分为：
   a. 明确引用阅卷口径
   b. 普通讲评
   c. 学生讲义式表达
6. 把 2026 通州期末 Q20 和 2026 朝阳期中 Q17 作为硬样本，验证抽取字段、术语粒度、评分语言边界。
```

本阶段不要急着写终稿。先把证据池、题号、术语条目、证据等级锁住。

---

## 3. Codex 生产线任务

Codex 生产线本阶段要自跑完整一条证据链，不能只等 ClaudeCode。

### 3.1 源文件矩阵

建立或更新：

```text
SOURCE_LEDGER
SOURCE_INVENTORY
SUITE_QUESTION_MATRIX
EVIDENCE_LEVEL_RECHECK
XUANBIYI_SUBJECTIVE_INDEX
```

每个 source 至少记录：

```text
source_id
year
district_or_exam_scope
exam_type
file_type
raw_category
candidate_evidence_level
verified_evidence_level
contains_xuanbiyi
contains_subjective_question
question_numbers_detected
has_scoring_detail
has_reference_answer
has_teaching_or_lecture
has_pdf_visual_risk
has_ppt_visual_risk
has_image_or_table
needs_ocr
status
blocker
```

### 3.2 P0 候选复核

对 98 个 P0 候选逐个复核，禁止只按文件名判断。

复核结果必须落入：

```text
P0_verified_scoring_rule
P0_verified_marking_detail
P0_verified_rubric
P1_reference_answer
P2_teaching_or_lecture
P3_paper_only
unknown_needs_visual_check
excluded_not_relevant
```

重点防错：

```text
“答案及评分参考”不得自动进入 P0。
“讲评材料”不得自动进入 P0。
PPT 中出现答案语言，也不得自动进入 P0。
只有明确评分、阅卷、细则、评标、赋分规则的内容才进入 P0。
```

### 3.3 选必一主观题索引

建立：

```text
xuanbiyi_subjective_entries_phase02.jsonl
```

每条至少包含：

```text
entry_id
source_id
year
district_or_exam_scope
exam_type
question_no
sub_question_no
question_type
module
unit_or_topic
material_trigger
scoring_term
term_function
why_this_term
answer_landing
evidence_level
evidence_source_type
needs_visual_check
needs_claudecode_compare
old_final_quality_reference_used
status
```

注意：旧终稿只允许作为质量参照字段，不允许成为 evidence_source_type。

### 3.4 两个硬样本处理

对已做样本进行标准化复查：

```text
2026 通州期末 Q20：
六个术语条目逐条确认：
1. 是否来自选必一主观题。
2. 是否有 P0/P2/user-confirmed 支撑。
3. 每个术语的材料触发点是否清楚。
4. 每个术语是否能转成学生可迁移表达。
5. 是否存在参考答案语言被误判为评分细则。

2026 朝阳期中 Q17：
三个关系条目逐条确认：
1. 关系术语是否有本地证据。
2. 关系判断是否依赖题干材料。
3. 答案落点是否可迁移。
4. 是否需要补图、补表、补 OCR 或补 PPT 讲评证据。
```

### 3.5 输出本阶段 Codex 产物

```text
phase02_codex_source_lock_report.md
source_ledger_updated.csv
suite_question_matrix.csv
evidence_level_recheck.csv
xuanbiyi_subjective_index.csv
xuanbiyi_subjective_entries_phase02.jsonl
hard_sample_review_2026_tongzhou_q20.md
hard_sample_review_2026_chaoyang_q17.md
phase02_blockers.md
```

---

## 4. ClaudeCode 独立线任务

以下内容建议由 Codex 转写为 ClaudeCode 本地任务。GPT 不直接命令 ClaudeCode。

### 4.1 ClaudeCode 本阶段目标

ClaudeCode 从 0 独立复跑，目标是建立另一份选必一主观题证据矩阵，用于和 Codex 线对照。

ClaudeCode 不应使用 Codex 已抽出的结论作为事实来源。它可以知道本轮范围、字段、证据等级规则和硬样本编号，但需要重新从源文件处理。

### 4.2 ClaudeCode 必跑范围

```text
1. 2024、2025、2026 三年原始题源。
2. 所有疑似含选必一主观题的套卷。
3. P0 候选评分/评标/细则文件。
4. P2 讲评/教学材料。
5. PDF、Word、PPT/PPTX、图片表格风险文件。
6. 2026 通州期末 Q20。
7. 2026 朝阳期中 Q17。
```

### 4.3 ClaudeCode 输出格式

建议要求 ClaudeCode 交付：

```text
claudecode_source_inventory_phase02.csv
claudecode_xuanbiyi_subjective_index.csv
claudecode_evidence_level_recheck.csv
claudecode_entries_phase02.jsonl
claudecode_suite_reports_phase02/
claudecode_hard_sample_tongzhou_q20.md
claudecode_hard_sample_chaoyang_q17.md
claudecode_blockers_phase02.md
claudecode_conflicts_suspected.md
```

### 4.4 ClaudeCode 必须显式报告

```text
1. 哪些 source 被判定为含选必一主观题。
2. 哪些 source 被排除，排除理由是什么。
3. 哪些 P0 候选实际只是参考答案。
4. 哪些 P2 讲评材料可能含阅卷口径。
5. 哪些 PDF/PPT/图片/表格尚未视觉校验。
6. 哪些题号不连续或无法确认。
7. 哪些条目与 Codex 两个硬样本可能冲突。
```

---

## 5. 需要 Claude/GPT 审稿的点

本阶段 GPT 和 Claude 只做审稿和策略审查，不裁决本地证据。

### 5.1 GPT phase advice 需要审的点

本阶段结束时，Codex 应向 GPT 提供脱敏 Phase 02 report，请 GPT 审：

```text
1. 证据矩阵是否足以进入术语条目批量生产。
2. P0/P1/P2/P3 边界是否有流程漏洞。
3. 是否存在把参考答案当评分细则的风险。
4. 是否遗漏了 PPT、PDF、图片、表格、OCR 风险。
5. 旧终稿质量参照是否可能污染从0重开。
6. 硬样本字段是否能支撑后续整本书批量处理。
```

### 5.2 GPT content review 暂不触发终稿审查

G11 的 outline、section_batch、final_markdown、word_pdf 还未到触发点。

本阶段只允许触发一个轻量内容预审：

```text
artifact：术语条目字段模板和两个硬样本学生化表达
目的：检查是否能服务“主观题评分术语积累”
不得视为 final Markdown content review
```

### 5.3 Claude 可审的点

Claude 可用于审两个方向：

```text
1. 术语条目是否适合学生记忆和迁移。
2. 两个硬样本是否形成清晰链条：
   材料触发点 → 评分术语 → 答案落点。
```

Claude 不审：

```text
1. 源文件真实性。
2. 证据等级真假。
3. 某题是否属于某区某年。
4. 本地 OCR 是否准确。
```

---

## 6. Governor 必查项

### 6.1 G10 必查

G10 当前未过，必须先补。

PASS 条件：

```text
1. GPT phase advice 原文已保存。
2. Codex 已写 codex_response_to_advice。
3. 每条建议已转为 accepted、partiallyaccepted、rejected、deferred。
4. 已采纳建议进入 task_plan。
5. 拒绝建议写明原因。
6. GPT 不作为 evidence authority 的边界写入 DECISION_LOG。
```

### 6.2 Phase 02 新增闸门

建议新增或临时启用：

```text
G2.5 Source Eligibility Gate
```

PASS 条件：

```text
1. 177 个文件均有 source_id。
2. 三年来源分布记录完整。
3. P0/P1/P2/P3/unknown 均有复核状态。
4. 选必一主观题候选套卷已列出。
5. 排除项有理由。
6. unknown 9 个有处理计划。
```

### 6.3 证据等级闸门

```text
1. P0 候选 98 个不得整体沿用候选身份。
2. 每个 P0_verified 必须有本地证据依据。
3. P1 参考答案不能升级为评分细则。
4. P2 讲评材料若进入术语条目，必须标明其证据功能。
5. P4 模型建议不得进入证据链。
```

### 6.4 非文本材料闸门

```text
1. PDF 是否需要截图或 OCR。
2. PPT/PPTX 是否读取文本框、图片、表格、备注。
3. 图片表格是否有视觉校验状态。
4. 未校验文件不得支撑 mustfixcontent 或核心术语结论。
```

### 6.5 G11 状态

本阶段 G11 不要求 PASS，但必须登记状态：

```text
outline：not_triggered
section_batch：not_triggered
final_markdown：not_triggered
word_pdf：not_triggered
```

不得写成已通过。

---

## 7. Confucius / 学生迁移验证点

本阶段不需要完整 Confucius 终稿验收，但需要做小样迁移测试。

测试对象：

```text
1. 2026 通州期末 Q20 六个术语条目。
2. 2026 朝阳期中 Q17 三个关系条目。
```

Confucius 只看学生化小样，不看审计材料。

检查问题：

```text
1. 我能不能看懂这个术语在题里为什么出现。
2. 我能不能从材料中找到触发点。
3. 我能不能知道这个术语在答案里承担什么功能。
4. 换一道相似国际政治或经济材料题，我能不能迁移使用。
5. 这像不像背答案句子。
6. 有没有只告诉我术语，却没告诉我什么时候用。
7. 有没有把评分细则、debug、OCR、source_id、状态字段暴露给学生。
```

小样通过标准：

```text
每个术语条目至少有：
材料触发点
术语名称
术语功能
答案落点
迁移提醒
易错边界
```

---

## 8. 最大风险和具体防错动作

### 最大风险

本阶段最大风险是 **P0 候选池膨胀导致评分术语失真**。

表现形式：

```text
1. 文件名像评分细则，内容实际是参考答案。
2. PPT 讲评语言被误当阅卷口径。
3. 旧终稿表达顺手，被无意识继承。
4. 题源矩阵还没闭合，就开始批量写术语。
5. PDF/PPT/图片没有视觉校验，漏掉设问或小问。
6. 两个硬样本先入为主，后续融合时压过 ClaudeCode 独立结果。
```

### 防错动作

```text
1. P0 候选必须逐个降噪，verified 后再使用。
2. 每条术语必须绑定 evidence_level 和 evidence_source_type。
3. 旧终稿只能填 quality_reference 字段，不能填 evidence 字段。
4. 未完成 suite_question_matrix 前，禁止生成整本书术语终稿。
5. PDF/PPT/图片/表格未视觉校验的条目，status 标为 provisional。
6. Codex 与 ClaudeCode 对硬样本冲突时，必须回源复核，不能按模型名望裁决。
7. 2026 通州 Q20 和 2026 朝阳 Q17 只能作为字段校准样本，不能代表全书结论。
8. unknown 9 个文件必须有处理状态，不能静默排除。
```

---

## 9. Codex 采纳前必须做的本地检查

Codex 在采纳本指挥包前，必须本地检查以下事项：

```text
1. 本指挥包原文已保存到 gpt_phase_advice。
2. codex_response_to_advice 已逐条消化。
3. G10 所需日志齐全。
4. SOURCE_LEDGER 中 177 个文件均有 source_id。
5. 2024、2025、2026 三年数量与当前扫描结果一致：
   2024：66
   2025：61
   2026：50
6. P0/P1/P2/P3/unknown 数量与当前扫描结果一致：
   P0候选：98
   P1：2
   P2：7
   P3：61
   unknown：9
7. P0 候选未被直接写成 P0_verified。
8. 2026 通州期末 Q20 六个术语条目有本地 evidence locator。
9. 2026 朝阳期中 Q17 三个关系条目有本地 evidence locator。
10. ClaudeCode 已独立运行，且其结果不会被 Codex 样本预设污染。
11. 旧终稿未覆盖新 run folder，也未进入 evidence 字段。
12. PDF、Word、PPT/PPTX、图片表格风险已进入 task_plan。
13. G11 四个触发项当前状态记录为 not_triggered，未误标 PASS。
14. 本阶段所有面向学生的小样不含 source_id、路径、debug、OCR 状态、评分细则字样。
```

本阶段结论：**允许进入 Phase 02，但先补 G10，再锁证据池和选必一主观题矩阵。未完成 P0 复核和题号矩阵前，不启动整本书术语批量终稿。**
