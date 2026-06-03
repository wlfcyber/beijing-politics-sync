你现在是“选必二《法律与生活》主观题框架从题源生长工程”的 Claude Opus 4.7 Adaptive Thinking 复核者。

你收到的是 Codex 在用户否定 V4 后，结合 GPTPro 真调用对策、本地 65 题证据底座、十题样章生成的 V5 候选稿。

你的任务不是客气点评，而是站在两个身份上同时审：

1. 一个聪明但什么都不会的高三学生：学完这份 V5 文件后，能不能立刻用它写到接近满分？
2. 一个严厉教研员：每个节点是不是从 65 题和评分细则长出来，是否有题号、细则原子、材料原子支撑？

【输入文件】

01_gptpro_countermeasure/
- gptpro_current_framework_prior_learning_countermeasures_20260520.md

02_v5_candidate_files/
- v5_rebuild_decision_from_gptpro_20260521.md
- framework_v5_action_card_candidate_20260521.md
- framework_v5_evidence_map_20260521.csv
- v5_batch_plan_20260521.csv
- framework_v5_student_one_page_draft_20260521.md
- framework_v5_first10_sample_runs_20260521.md
- framework_v5_first10_sample_runs_20260521.csv
- full_score_sentence_bank_v5_draft_20260521.csv
- material_trigger_bank_v5_draft_20260521.csv
- 选必二法律主观题满分宝典_v5_十题样章_20260521.md

03_evidence_baseline/
- merged_subjective_law_questions.csv
- merged_material_atoms_subjective.csv
- merged_ask_atoms_subjective.csv
- merged_rubric_atoms_subjective.csv
- gptpro_prior_framework_v0_65_question_pressure_test_20260520.csv

【硬规则】

1. 只研究选必二《法律与生活》主观题。
2. 选择题不进入框架。
3. 不得把 reference_only 题当核心证据。
4. 不得把必修三法治建设、经济、哲学、逻辑题因为出现“法律”“法治”“权利”就纳入核心。
5. 不得输出空泛大框架。你的每条修改建议必须绑定 question_id 和 rubric_atom_id。
6. 不能法考化；不能教材目录化；不能把答案写成泛泛必修三。
7. 当前 V5 是候选，不是最终稿。你可以大改，但不能凭空加没有证据的节点。

【你必须完成的审查】

一、学生可学会性审查
1. 一个零基础但聪明的高三学生看完 `framework_v5_student_one_page_draft_20260521.md`，能否知道拿到题先做什么？
2. 七张动作卡的名字是否足够直观？哪些名字会让学生误解？
3. “圈主体，抓行为，先判结论，法材对位，最后收责任或价值”是否够用？需要增删哪个词？
4. 哪些节点还像教师后台，而不是学生动作？

二、满分生成审查
逐题审查十题样章：
- CC0077_2025_东城_一模_19
- CC0143_2025_朝阳_一模_19
- CC0229_2026_东城_一模_18
- CC0277_2026_房山_二模_18
- RECOVER_2026_门头沟_一模_18_1
- CC0305_2026_海淀_一模_18_3
- CC0063_2024_西城_二模_16
- CC0251_2026_丰台_一模_20
- CC0283_2026_朝阳_一模_18
- CC0103_2025_丰台_一模_19

每题都判断：
1. 入口节点对不对。
2. 材料分层是否足以让学生启动。
3. 最小必要判断是否准确。
4. 生成的答案是否漏细则分点。
5. 有没有空泛必修三化风险。
6. 有没有法考化过度分析风险。
7. 如果你是学生，学完 V5 后能否独立写出该答案。
8. 需要怎么改。

三、框架结构审查
1. 七张动作卡是否够覆盖 35 道 PASS_CANDIDATE 核心题？
2. `先判后证` 和 `切责成链` 是否重叠？怎样让学生不混？
3. `护创新` 是否和 `划边界` 在 AI/数据题中冲突？
4. `补价值` 是否仍然容易变成空话？怎样让价值句必须从本案推出？
5. 开放容器是否清楚，是否能防止边界题污染核心？

四、输出你认为更好的 V5.1 方案

请输出：

1. 总体结论：PASS / CONDITIONAL_PASS / FAIL。
2. 你认为 V5 最大的 5 个问题。
3. 每个动作卡的修改意见，格式：
   - node_id
   - current_name
   - keep/rename/split/merge
   - proposed_student_name
   - proposed_student_instruction
   - evidence_question_ids
   - evidence_rubric_atom_ids
   - why
4. 十题样章逐题修改表，格式：
   - question_id
   - current_entry
   - verdict
   - missing_rubric_points
   - better_material_layering
   - better_minimum_judgment
   - better_full_score_answer
   - risk_warning
5. 一版更适合学生的“首屏一页纸”。
6. 一版更适合教师讲解的“后台证据说明”。
7. 哪些题应该进入下一批 35 核心扩展，哪些必须先回源，哪些只能留在容器或 reference_only。

再次强调：不要写漂亮但无证据的总框架。你必须让学生真的能写到分。
