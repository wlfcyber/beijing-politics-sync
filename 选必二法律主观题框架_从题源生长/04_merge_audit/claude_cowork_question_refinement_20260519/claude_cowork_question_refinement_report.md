# Claude Cowork E — 选必二《法律与生活》全题完善审查报告

生成时间: 2026-05-19
作业基线: `reasoner_packet_suite_exhaustive_claudecode_corrected_20260519.zip`(用户上传的唯一有效输入包)
作业范围: 65 道核心法律主观题逐题审查；本轮**不写框架**、**不写代码本**、**不写候选框架/口诀/总图**。

环境限制说明: Cowork E 在沙箱环境内运行，**没有直接访问用户 Desktop 的能力**，因此无法读取 `/Users/wanglifei/Desktop/...` 下的 04_merge_audit / 05_reasoner_packets / patch_verification_report.md。本轮全部审查基于上传 zip 解包后的 10 个修正文件。

---

## 1. 整体盘点（已校验）

- 核心 question 数: **65**（与上游 ClaudeCode patch 一致）
- evidence_level 分布: `{'formal': 61, 'reference_only': 4}`
- material atoms: **541**（min 1 / max 24 / mean 8.3）
- ask atoms: **65**（每题 1 个，1:1）
- rubric atoms: **362**（min 1 / max 25 / mean 5.6）
- exam_stage 分布: `{'一模': 28, '二模': 23, '期末': 14}` — **核心层无任何"期中"条目**，与上游期中清理一致。
- 套卷矩阵 question_ids 并集 = 65 = 核心列表 = 矩阵 core_question_count 求和，闭环一致。
- 边界表 9 条均未流入核心；移出边界的 CC0051_2024_海淀_期中_21_1 与 RECOVER_2024_顺义_二模_17 **确认不在核心 65 题中**。
- 阶段修正题 8 条全部已写为 `exam_stage=期末`：
  - CC0244_2026_东城_期末_18, CC0245_2026_东城_期末_18_2
  - CC0317_2026_海淀_期末_18, CC0318_2026_海淀_期末_18_2, CC0319_2026_海淀_期末_19
  - CC0353_2026_西城_期末_17
  - CC0364_2026_通州_期末_19_1
  - RECOVER_2026_朝阳_期末_18_1
- 套卷矩阵确认 2026 朝阳/海淀 期中、期末 已正确拆分为四套独立 suite。
- 套卷矩阵中 `no_law_subjective_confirmed` 与 `midterm_boundary_no_core_after_claudecode_audit` 覆盖了用户要求的四个空期中（2024-朝阳-期中、2024-海淀-期中、2026-朝阳-期中、2026-海淀-期中）。

## 2. 完善审查发现总览

| 类别 | 数量 | 必修(must_fix=yes) | 影响 |
|---|---|---|---|
| question 级 patch 建议 | 72 | 34 | 设问字段空、material 与细则同文本、阶段/locator 复核 |
| material atom patch 建议 | 155 | 65 | material 实为细则/答案、OCR 噪声、评分关键词残留 |
| ask atom patch 建议 | 21 | 20 | 占位符设问、模块标错 |
| rubric atom patch 建议 | 98 | 26 | 单 atom 多句、>200 字超长、判断字段过短、kmv/no_mat 不一致 |
| locator/evidence 风险 | 101 | 36 | full-leak、empty ask、OCR/render、pending locator |

## 3. 关键问题（必须在送 GPT-5.5 Pro / Claude Opus 前修）

### 3.1 ask_text 字段为空（19 条）

以下 19 条记录的 `ask_text` 字段为空字符串，且其 ask atom 全部使用占位符 `ask_function_plain="不确定" / student_task_plain="从材料与法律证据中判断作答任务"`。这些占位符无法驱动 reasoner 推理：

`CC0019_2024_朝阳_一模_19; CC0077_2025_东城_一模_19; CC0084_2025_东城_二模_19; CC0092_2025_东城_期末_19_1; CC0131_2025_房山_一模_19; CC0157_2025_朝阳_期末_20; CC0180_2025_海淀_期末_20; CC0189_2025_石景山_一模_20; CC0195_2025_西城_一模_20; CC0213_2025_门头沟_一模_20; CC0214_2025_门头沟_一模_20_2; CC0245_2026_东城_期末_18_2; CC0276_2026_房山_二模_17; CC0277_2026_房山_二模_18; CC0317_2026_海淀_期末_18; CC0318_2026_海淀_期末_18_2; CC0319_2026_海淀_期末_19; CC0325_2026_石景山_一模_18; CC0353_2026_西城_期末_17`

处置: 对每条逐一从 `full_question_text` 解析出原始设问句，回写到 `ask_text` 字段并重写 ask atom 的 `ask_function_plain / student_task_plain / module_requirement / requires_*` 五个字段。

### 3.2 material_text == rubric_text 全文泄漏（8 条）

下列 8 题的 `material_text` 与 `rubric_text`(及 `answer_text`) 完全相同，意味着 material atoms 实际上是从细则/答案文本中拆出来的句子，并非案件材料事实：

| question_id | level | mat_count | 风险 |
|---|---|---|---|
| CC0019_2024_朝阳_一模_19 | formal | 6 | atoms 是"诚信原则要求合同当事人..."等答案要点 |
| CC0092_2025_东城_期末_19_1 | formal | 6 | atoms 含"评分细则""[page 12]""• 思路1.充电桩方案..." |
| CC0214_2025_门头沟_一模_20_2 | formal | 4 | atoms 含"20（2）裁判理由共4分""①法律规定1分..." |
| CC0245_2026_东城_期末_18_2 | formal | 15 | atoms 含"维权途径2分""[slide 57]""三个角度 4分" |
| CC0317_2026_海淀_期末_18 | formal | 7 | atoms 是"该合同条款无效""(6 分)"等答案句 |
| CC0318_2026_海淀_期末_18_2 | formal | 4 | atoms 含"[page 3] 3" |
| CC0319_2026_海淀_期末_19 | formal | 3 | atoms 是"根据反不正当竞争法规定..."等答案句 |
| CC0353_2026_西城_期末_17 | reference_only | 2 | atoms 即细则两句 |

处置: 必须从 paper 原 PDF/PPTX 回源 OCR 重抽 material_text；若 formal 状态下源回不来，则该条临时降级为 `reference_only` 或剥离至 boundary，不得在 formal 框架内使用。

### 3.3 material_text 实为答案分点（2 条）

| question_id | level | 现象 |
|---|---|---|
| CC0131_2025_房山_一模_19 | formal | material_text 以 "19. 【答案】" 开头，14 个 atoms 全是 ①②③ 答案分点 |
| CC0180_2025_海淀_期末_20 | formal | material_text 以 "20．（6分） ①生产者产品责任..." 开头，atoms 是答案要点 |

处置: 同 3.2，回源重抽。

### 3.4 ask_text 与本记录子问题模块不一致（1 条 — 严重）

- **CC0364_2026_通州_期末_19_1**: `ask_text="根据材料，判断推理①和②的逻辑正误，并结合《逻辑与思维》知识说明理由。"` — 这是 19(2) 的《逻辑与思维》设问，但 `question_id` 与细则 `R_..._01` 对应的是 **19(1) 的法律部分**（"一、法理依据3分：依据民法典，相邻权利人..."）。
- ask atom `module_requirement="法律与生活(默认)"` 但 ask_text 文字指向逻辑模块，存在**模块错挂风险**。同套细则 `R_..._02 ~ _08` 才是 19(2) 的逻辑评分。
- 处置: 用 OCR/源回核拿到 19(1) 的真实法律设问填入 ask_text；并把现有的 R_..._02 ~ _08 这 7 条逻辑评分 atom 从核心法律 rubric 表移走（不属于 19_1）。

### 3.5 pending_locator_check 与 weak_reference_only 状态

- `merge_status='pending_locator_check'`: 10 条 — 必须在 reasoner 阶段前过一次 locator 复核（已在 patch CSV 中逐条记录）。
- `merge_status='weak_reference_only'`: 2 条（CC0162_2025_海淀_一模_18, CC0311_2026_海淀_二模_18_2）— 保持 reference_only，不允许在 reasoner 输出中升 formal。

### 3.6 paper_file 字段空（14 条）

主要是子问条目（_2 / _3）继承父问 paper，以及 OCR 阻塞条目。建议显式补齐字段（patch_type=update，must_fix=no），不必阻塞 reasoner。

## 4. 中等问题（建议在 reasoner 阶段前清理但不强制阻塞）

### 4.1 单 rubric atom 但 phrase 过长且多句聚合（17 题）

下列条目仅有 1 个 rubric atom，但 phrase 长 155–552 字、含 3–13 句，违反"一句一拆"原则：

`CC0011_2024_丰台_二模_17 (481/11); CC0019_2024_朝阳_一模_19 (238/5); CC0040_2024_海淀_一模_19 (155/4); CC0045_2024_海淀_二模_19 (193/3); CC0063_2024_西城_二模_16 (545/5); CC0092_2025_东城_期末_19_1 (286/0—列表式); CC0103_2025_丰台_一模_19 (467/8); CC0195_2025_西城_一模_20 (410/3); CC0200_2025_西城_二模_18 (552/13); CC0206_2025_西城_期末_19 (348/2); CC0276_2026_房山_二模_17 (408/2); CC0317_2026_海淀_期末_18 (174/4); CC0318_2026_海淀_期末_18_2 (176/1); CC0319_2026_海淀_期末_19 (261/3); CC0332_2026_石景山_二模_19 (309/4); CC0340_2026_西城_一模_17 (282/1); CC0353_2026_西城_期末_17 (172/2)`

格式 `(phrase_len/n_句号)`。处置: split 为更小颗粒度。

### 4.2 多 rubric atom 但单个 phrase >200 字（共 33 个 atom）

详见 `claude_cowork_rubric_atom_patch_suggestions.csv` 中 patch_type=split 的 29 行（4.1 与 4.2 已合并去重）。

### 4.3 material atom 含 OCR/页码/slide 标识

material_phrase 中含 `[page X]`、`[slide X]`、`高三年级（思想政治）`、`第X页/共X页` 共 27 个 atom，建议 `delete`。

### 4.4 material/rubric atom 含细则评分关键词

例 `M_CC0245_2026_东城_期末_18_2_08: "三个角度可选择， 两个角度充分4分 三个角度不充分4分。"` — 已在 patch CSV 中标注为 update。

### 4.5 ask atom 模块字段 `不确定`

共 3 个 ask atom 的 `module_requirement="不确定"`(CC0131_2025_房山_一模_19、CC0195_2025_西城_一模_20、另一同样为空 ask_text 的子集) — 应明确为 `法律与生活`。

### 4.6 rubric atom 的 kmv 与 can_be_written_without_material 不一致

- kmv 包含 material 但 no_mat=uncertain — 共若干例（详见 rubric patch CSV）。
- kmv=knowledge 但 no_mat=no — 同上。
- 处置: kmv 包含 material 时 no_mat 应为 `no`；kmv=knowledge 单一时应允许 `yes/uncertain`。

### 4.7 rubric atom 的 judgment 字段过短（16 个 atom）

`what_judgment_student_must_make_before_writing` 长度 <15 字，多数是 `判断法律关系/行为性质/责任承担或程序路径(回源细化)` 这种通用模板。应在 reasoner 阶段前替换为具体判断（如"先判定甲乙是否存在劳动关系并区分劳动者/劳务者"）。

## 5. 元数据/边界审查结论

### 5.1 65 题 question_id / year / district / exam_stage / question_no / sub_question_no 稳定性

- 全部 65 条无重复 question_id；无核心条目仍带"期中"标签。
- year/district/exam_stage/question_no/sub_no 与 question_id 字符串高度自洽。
- 8 条"阶段修正"题（用户列出的 7 条 + RECOVER_2026_朝阳_期末_18_1）已全部为 `exam_stage=期末`。
- 未发现 question_no 与 full_question_text 起始题号不匹配的情况。

### 5.2 套卷矩阵与边界表

- suite_exhaustion_matrix 65 行 core_question_count 求和 = 65，与 questions.csv 完全一致。
- boundary_mixed_or_blocked_cases 9 行（5 个 UNCERTAIN_MIXED + 1 BLOCKED + 1 STAGE_CONFLICT + 2 DOWNGRADED_TO_BOUNDARY + 1 UNCERTAIN_LOGIC）— 全部解释完整，无歧义。
- 真正无选必二法律主观题的期中已正确处理：
  - 2024-朝阳-期中: `no_law_subjective_confirmed` (notes 已说明主观题为文化/哲学/逻辑/经济)
  - 2024-海淀-期中: `midterm_boundary_no_core_after_claudecode_audit` (CC0051 已下沉)
  - 2026-朝阳-期中: `no_law_subjective_confirmed`(True 2026朝阳期中 only)
  - 2026-海淀-期中: `no_law_subjective_confirmed`(True 2026海淀期中 only)
- 2025-海淀-期中: `midterm_mixed_law_reference_not_core`(婚姻法/民法典材料但设问为法治知识/良法，参考答案为主)— 边界判断合理。

### 5.3 reference_only 四题独立审查（详见 `claude_cowork_reference_only_review.csv`）

- **CC0040_2024_海淀_一模_19**: 仅见教师参考答案；保留 reference_only；单 atom 可拆分。
- **CC0162_2025_海淀_一模_18**: 已 sentence-split 为 4 atoms；保留 reference_only。
- **CC0311_2026_海淀_二模_18_2**: 已 sentence-split 为 5 atoms；保留 reference_only。
- **CC0353_2026_西城_期末_17**: 最弱：material/rubric/answer 三者完全相同，只有 1 个未拆分的 rubric atom 和 2 个由细则文本切出的"material" atom；强烈建议优先回源否则在框架阶段予以剔除。

### 5.4 evidence_type/evidence_level 一致性

- question 与 rubric atom 的 evidence_level 全部一致（0 mismatch）。
- question 与 rubric atom 的 evidence_type 全部一致（0 type_diff）。
- 4 个 reference_only 题的 rubric_atom 全部为 `teacher_reference_answer` — 类型与状态一致。
- 未发现 formal 题被误用 `teacher_reference_answer` 类型；未发现 reference_only 题混入 `marking_rubric` 类型。

### 5.5 related_material_atom_ids 引用完整性

- 引用 0 失效（按 `|` 分隔解析）。
- 注: 该字段统一以 `|` 分隔（共 282 行），与其它表常用的 `;` 不同。建议在 reasoner schema 文档中显式声明此分隔符。

## 6. 是否还可能漏题

基于上传文件比对 + 边界表 + ClaudeCode missed-core 文件 + suite_exhaustion_matrix：

- ClaudeCode missed-core 文件中仅 1 项 `MISS_CC_2026_朝阳_期末_18_1`，已并入核心为 `RECOVER_2026_朝阳_期末_18_1`。
- 其他套卷在 matrix 中全部覆盖、显式标注状态。
- BLOCKED_2026_石景山_期末_17_SOURCE_EXCLUDED 与 STAGE_CONFLICT_2026_石景山_期中 是源阻塞或映射冲突，不构成漏题。
- 因此**当前未发现实质性漏题风险**；但 OCR/源阻塞条目（CC0245、CC0318、CC0353、CC0364 等）若回源成功，材料原子数量会增加，会带来新的 atom 而非新的题。

## 7. 是否有 reference_only 被误升 formal / formal 需要降级

- **没有 reference_only 被误升 formal**: 4 个 reference_only 全部保持 `teacher_reference_answer` + `reference_only` 类型 + 等级一致。
- **建议在源未回的情况下降级的 formal 候选**: 3.2 节 8 条 full-leak 中，已是 reference_only 的 CC0353 不变；formal 的 7 条若 OCR 回源失败，应临时降级为 reference_only 或剥离至 boundary。当前不主动改 evidence_level，但在 must_fix=yes 列表中。

## 8. 是否有阶段/区县/题号/小问错挂

- 阶段错挂: 已修正 7+1 条，全部为 `期末`，无残留。
- 区县错挂: 未发现。
- 题号/小问错挂: 未发现 question_id 与 question_no/sub_no 字段不一致的情况；但 CC0364_2026_通州_期末_19_1 的 ask_text 文字指向 19(2) 的逻辑模块，构成"小问内容错挂"——必须修正。

## 9. 文件清单

本目录下生成的 8 个交付物：

1. `claude_cowork_question_refinement_report.md`(本文)
2. `claude_cowork_question_patch_suggestions.csv` 72 行
3. `claude_cowork_material_atom_patch_suggestions.csv` 155 行
4. `claude_cowork_ask_atom_patch_suggestions.csv` 21 行
5. `claude_cowork_rubric_atom_patch_suggestions.csv` 98 行
6. `claude_cowork_locator_evidence_risks.csv` 101 行
7. `claude_cowork_reference_only_review.csv` 4 行
8. `claude_cowork_ready_for_reasoner_decision.md`(裁定与放行条件)
