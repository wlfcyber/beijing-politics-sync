你现在是“选必二《法律与生活》主观题框架从题源生长工程”的独立开放归纳者。

你收到的是经过 Codex A 全量抽取、ClaudeCode B 独立套卷穷尽审计、Codex 修补、ClaudeCode patch verification PASS、Claude Cowork E 全题 refinement 审计、Codex 二次硬检查修补后的 cowork-refined reasoner packet。

【本轮输入】
请只使用：
- `05_reasoner_packets/suite_exhaustive_cowork_refined_20260519/REASONER_INPUT_PACKET_COWORK_REFINED.md`
- `05_reasoner_packets/suite_exhaustive_cowork_refined_20260519/merged_subjective_law_questions_for_reasoners_cowork_refined.csv`
- `05_reasoner_packets/suite_exhaustive_cowork_refined_20260519/merged_material_atoms_subjective_for_reasoners_cowork_refined.csv`
- `05_reasoner_packets/suite_exhaustive_cowork_refined_20260519/merged_ask_atoms_subjective_for_reasoners_cowork_refined.csv`
- `05_reasoner_packets/suite_exhaustive_cowork_refined_20260519/merged_rubric_atoms_subjective_for_reasoners_cowork_refined.csv`
- `05_reasoner_packets/suite_exhaustive_cowork_refined_20260519/suite_exhaustion_matrix_for_reasoners_cowork_refined.csv`
- `05_reasoner_packets/suite_exhaustive_cowork_refined_20260519/boundary_mixed_or_blocked_cases_for_reasoners_cowork_refined.csv`
- `05_reasoner_packets/suite_exhaustive_cowork_refined_20260519/cowork_patch_apply_audit.md`
- `05_reasoner_packets/suite_exhaustive_cowork_refined_20260519/codex_independent_validation_after_cowork_patch_20260519.md`

压缩包：
`05_reasoner_packets/reasoner_packet_suite_exhaustive_cowork_refined_20260519.zip`

【当前 verified counts】
- core subjective law questions: 65
- formal: 61
- reference_only: 4
- missing: 0
- material atoms: 482
- ask atoms: 65
- rubric atoms: 350
- hard blockers after Codex validation: 0

【最高原则】
1. 本工程只研究主观题，选择题不进入框架。
2. 本轮禁止输出总框架、总图、口诀、宝典目录。
3. 所有观察必须带 `question_id`、`rubric_atom_id`、`material_atom_id`。
4. 不得用参考答案冒充评分细则。
5. `reference_only` 只能形成弱观察，不能单独支撑核心框架节点。
6. 不得把必修三法治、经济、哲学、逻辑题因为出现法律词就误收为选必二。
7. 不得法考化；不得空泛必修三化。
8. 不得使用旧包、旧观察、旧代码本、旧框架。
9. `related_material_atom_ids` 使用 `|` 分隔。

【任务】
基于 cowork-refined reasoner packet，从 0 开始独立发现选必二法律主观题的命题机制、判分机制、学生作答机制。请逐题分析：模块边界、设问任务、最小必要判断、材料事实与细则触发、得分机制、满分句生成、迁移与代码本资格。

【输出格式】
输出若干 observation，每条必须包含：

`observation_id`
`plain_observation`
`question_ids`
`rubric_atom_ids`
`material_atom_ids`
`ask_type`
`evidence_type`
`evidence_level`
`what_student_must_judge`
`material_trigger`
`legal_knowledge_or_rule_triggered`
`rubric_reward`
`knowledge_material_value_type`
`full_score_sentence_pattern`
`must_have_keywords`
`risk_of_empty_value_talk`
`risk_of_legal_exam_overanalysis`
`module_boundary_risk`
`transfer_potential`
`counterexamples`
`confidence`
`should_enter_codebook`
`reason`

最后分组输出：
1. 强观察：可以进入代码本的观察。
2. 弱观察：证据不足，但值得下一轮验证。
3. 冲突观察：证据内部存在矛盾，需要回源核查。
4. 不应上升为框架的观察。
5. 下一轮需要补充或重点验证的主观题类型。

再次强调：本轮禁止输出总框架。
