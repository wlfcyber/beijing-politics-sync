你现在进入“选必二《法律与生活》主观题框架从题源生长工程”的 codebook expansion source-check 阶段。

你收到的是 framework_v1 全题压测后的 PARTIAL rows 包。你的任务不是写最终框架，不是写宝典，而是检查 45 道 formal PARTIAL 题中，是否存在新的、可证据支撑的稳定判分机制，可以补入 provisional_codebook_v1。

【输入包】
请读取附件：codebook_expansion_partial_rows_20260519.zip

附件内包含：
- CODEBOOK_EXPANSION_INPUT_PACKET.md
- partial_formal_rows_for_codebook_expansion.csv
- reference_only_rows_not_for_core.csv
- framework_v1_question_by_question_test.csv
- provisional_codebook_v0_cowork_refined.csv
- framework_v1.md
- framework_v1_evidence_map.csv
- observations_needing_source_check.csv（如存在）

【当前事实】
- core subjective law questions: 65
- formal: 61
- reference_only: 4
- missing: 0
- framework_v1 direct PASS: 16
- formal PARTIAL requiring source-check: 45
- reference_only PARTIAL: 4，不能支撑核心 code
- current codebook rows: 7

【硬规则】
1. 本轮仍然禁止输出最终框架、框架总图、学生口诀、宝典目录。
2. 你只能提出“新增或修订 codebook observation”，不能直接造框架节点。
3. 每条可进入 codebook 的 observation 必须同时包含 question_id、rubric_atom_id、material_atom_id。
4. 没有 rubric_atom_id 或 material_atom_id 的观察不得进入 codebook。
5. reference_only rows 只能产生 weak/open observation，不能支撑 core code。
6. pending/source-check 旧观察不能直接升级，必须由本包 formal rubric atoms 重新支撑。
7. 不得按教材目录补节点。
8. 不得把必修三法治建设话语升级成选必二法律框架节点。
9. 不得把复杂法考构成要件当作高中主观题框架。
10. 若 45 道 formal PARTIAL 题只是“能被 v1 启动但无法形成稳定新机制”，请明确说不能升级，不要硬凑。

【逐 cluster 检查任务】
对 partial_formal_rows_for_codebook_expansion.csv 中的每个 cluster：
1. 这个 cluster 的设问/材料触发是什么？
2. 细则原子是否反复奖励同一个“学生最先必须判断”的动作？
3. 细则原子是否反复奖励同一种“材料事实 → 法律语言”的转化？
4. 细则原子是否反复奖励同一种满分句模式？
5. 它是现有 CODE_COWORK_001-007 的迁移，还是需要新增 code？
6. 若需要新增 code，证据是否足够强？
7. 是否存在必修三化风险或法考化风险？
8. 是否有 counterexample，说明不能上升？

【输出格式】
请输出若干条 expansion_candidate，每条字段如下：

candidate_id:
status: promote_to_codebook / revise_existing_code / keep_transfer_only / reject / uncertain
proposed_code_label:
plain_observation:
source_cluster_ids:
supporting_question_ids:
supporting_rubric_atom_ids:
supporting_material_atom_ids:
evidence_level: formal / reference_only / mixed / missing
what_student_must_judge:
material_trigger_pattern:
legal_knowledge_or_rule_pattern:
rubric_reward_pattern:
full_score_sentence_pattern:
must_have_keywords:
which_existing_code_if_revision:
risk_of_empty_value_talk:
risk_of_legal_exam_overanalysis:
module_boundary_risk:
counterexamples_or_limits:
confidence:
reason:

【最后输出】
1. 可新增到 provisional_codebook_v1 的候选观察。
2. 只能修订现有 code 的候选观察。
3. 只能保持 transfer/open-container 的 cluster。
4. 应明确 reject 的 cluster。
5. 仍需回源核查的题号。
6. 你对 framework_v1 能否修订为 v2 的建议，但不要写 v2 框架。
