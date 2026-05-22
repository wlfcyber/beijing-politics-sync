请读取已上传的 reasoner_packet_v2_full_context_20260519.zip。这是正式 v2 全上下文输入包，替代此前 35 题 trial 包。

关键口径：
1. 包内共有 74 道 merged canonical 主观题候选。
2. 其中 54 道 formal 可支撑强观察，3 道 reference_only 只能支撑弱观察，17 道 missing 只作待补证据和边界上下文，不得支撑 observation。
3. 本轮仍然禁止输出框架；只输出 observation。
4. 每条 observation 必须保留 question_id、rubric_atom_id、material_atom_id；缺编号不得进入代码本。
5. 不要沿用或提及此前 35 题 trial 输出。

# Unified Prompt: GPT-5.5 Pro / Claude Opus Open Observation

你现在是“选必二《法律与生活》主观题框架从题源生长工程”的独立开放归纳者。

你和另一位模型将收到完全相同的主观题证据材料，并回答完全相同的问题。你的任务不是写框架，而是基于主观题、答案、评分细则、评标、阅卷报告、讲评明确口径，独立发现选必二法律主观题的命题机制、判分机制和学生作答机制。

【最高原则】
1. 本工程目前只研究主观题。选择题不进入框架，不分析错项。
2. 框架只能从主观题题干、材料、设问、答案、评分细则、评标、阅卷报告、讲评明确口径中生长出来。
3. 教材目录、法学理论、已有框架、模型先验、漂亮概念，均不得作为结构来源。
4. 本轮禁止输出总框架、总图、口诀、宝典目录。
5. 所有观察必须有 question_id、rubric_atom_id、material_atom_id。
6. 没有证据编号的观察，不得进入下一轮。
7. 参考答案不得冒充评分细则。
8. 不得把主观题写成空泛必修三法治表达。
9. 不得把主观题分析成法考式复杂案例分析。
10. 不得使用任何此前预设结构，包括“一核二线三问四步五域”“动作库”“故事卡”“法律关系路由”。

【输入】
05_reasoner_packets/REASONER_INPUT_PACKET.md
05_reasoner_packets/merged_subjective_law_questions_for_reasoners.csv
05_reasoner_packets/merged_material_atoms_subjective_for_reasoners.csv
05_reasoner_packets/merged_ask_atoms_subjective_for_reasoners.csv
05_reasoner_packets/merged_rubric_atoms_subjective_for_reasoners.csv
05_reasoner_packets/merge_audit_report_for_reasoners.md

【逐题分析问题】

一、模块边界：为什么可以暂时进入选必二法律主观题候选？有没有可能其实是必修三法治建设题、经济题、哲学题或逻辑题？哪些信息支持它考的是选必二法律规则/制度？学生最可能误写成哪个模块？

二、设问任务：设问要求说明、评析、论证、建议、分析意义，还是其他？是否明确要求运用《法律与生活》知识？回答的是为什么、怎么看、怎么办、有何意义，还是其他？是否要求结合材料中的法律现象展开？

三、最小必要判断：学生要写对答案，最先必须判断什么？这是主体身份、双方关系、行为性质、权利义务、责任归属、程序路径、制度作用，还是其他？如果没判断会写偏到哪里？这个判断是否被答案或细则直接奖励？

四、材料事实与细则触发：对每个细则点说明原文、对应材料事实、无该事实能否写、是否需要转化为法律语言、转化过程是什么。

五、得分机制：奖励纯法律知识、材料分析、价值表达，还是混合？为什么得分？有无法律规则或制度依据？价值表达是否由法律规则推出？是否有空泛必修三化风险或法考化过度分析风险？

六、满分句生成：最贴近细则的学生答案句怎么写？必须保留哪些关键词？必须带入哪些材料信息？哪些高级表达不一定得分？能否迁移？

七、迁移与框架资格：这是个别题现象还是跨题现象？有哪些 question_id、rubric_atom_id、material_atom_id 支持？有无反例？上升为框架节点会不会误导学生？能否帮助学生审题、转法律语言、生成满分句？是否应进临时代码本？

【输出格式】
每条 observation 使用字段：observation_id, plain_observation, question_ids, rubric_atom_ids, material_atom_ids, ask_type, evidence_type, evidence_level, what_student_must_judge, material_trigger, legal_knowledge_or_rule_triggered, rubric_reward, knowledge_material_value_type, full_score_sentence_pattern, must_have_keywords, risk_of_empty_value_talk, risk_of_legal_exam_overanalysis, module_boundary_risk, transfer_potential, counterexamples, confidence, should_enter_codebook, reason

【最后输出】
1. 强观察：可以进入代码本的观察。
2. 弱观察：证据不足，但值得下一轮验证。
3. 冲突观察：证据内部存在矛盾，需要回源核查。
4. 不应上升为框架的观察。
5. 下一轮需要补充或重点验证的主观题类型。

再次强调：本轮禁止输出总框架。