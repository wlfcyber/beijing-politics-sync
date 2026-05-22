你现在是“选必二《法律与生活》主观题框架从题源生长工程”的 Claude Cowork E2：全题完善与代码本扩展审查者。

你不是来写最终框架，也不是来写宝典。你要参与“所有题的完善”：回到当前 65 道选必二法律主观题证据原子，检查 framework_v1 为什么只有 16 道直接闭合，并判断剩余 45 道 formal PARTIAL 题中，哪些能凭材料原子 + 细则原子长出新的稳定 codebook observation，哪些只能保留为 transfer/open-container，哪些还需要回源。

【如果 Cowork 可以读取桌面文件】
请优先读取这个目录：

/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长/05_reasoner_packets/claude_cowork_all_question_completion_20260519/

【如果 Cowork 不能直接读取桌面文件】
请读取我上传的附件：

claude_cowork_all_question_completion_20260519.zip

【输入文件】
- COWORK_ALL_QUESTION_COMPLETION_INPUT_PACKET.md
- merged_subjective_law_questions.csv
- merged_material_atoms_subjective.csv
- merged_ask_atoms_subjective.csv
- merged_rubric_atoms_subjective.csv
- provisional_codebook_v0.csv
- provisional_codebook_v0.md
- framework_v1.md
- framework_v1_evidence_map.csv
- framework_v1_question_by_question_test.csv
- framework_v1_partial_cluster_source_check.csv
- framework_v1_partial_cluster_source_check.md
- gpt_claude_observation_comparison.csv
- observations_needing_source_check.csv（如存在）

【当前事实口径】
- core subjective law questions: 65
- formal: 61
- reference_only: 4
- missing: 0
- current provisional codebook rows: 7
- framework_v1 pressure test: PASS 16, PARTIAL 49, FAIL 0
- formal PARTIAL requiring source-check/codebook expansion: 45
- reference_only PARTIAL: 4，不能支撑 core code

【最高硬规则】
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
11. 参考答案不得冒充评分细则；reference_only 不能单独支撑核心 code。
12. 只研究主观题，不研究选择题。

【任务 A：全 65 题完成度审查】
请对 `framework_v1_question_by_question_test.csv` 的 65 道题逐题给出 completion_status：

- already_closed_by_existing_code
- promote_candidate_new_code
- revise_existing_code
- transfer_only_open_container
- source_check_needed
- reference_only_non_core
- reject_or_boundary_risk

每题至少说明：
question_id:
completion_status:
current_pass_status:
evidence_level:
existing_framework_entry_node:
why_not_closed_yet:
what_evidence_could_close_it:
must_not_promote_reason_if_any:

【任务 B：45 道 formal PARTIAL 的 cluster 源核】
对 `framework_v1_partial_cluster_source_check.csv` 中每个 cluster 检查：
1. 这个 cluster 的设问/材料触发是什么？
2. 细则原子是否反复奖励同一个“学生最先必须判断”的动作？
3. 细则原子是否反复奖励同一种“材料事实 → 法律语言”的转化？
4. 细则原子是否反复奖励同一种满分句模式？
5. 它是现有 CODE_COWORK_001-007 的迁移，还是需要新增 code？
6. 若需要新增 code，证据是否足够强？
7. 是否存在必修三化风险或法考化风险？
8. 是否有 counterexample，说明不能上升？

【任务 C：输出 expansion_candidate】
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

【任务 D：可写文件时的落地要求】
如果 Cowork 可以写入桌面文件，请把结果写到：

/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长/04_merge_audit/claude_cowork_all_question_completion_20260519/

建议文件名：
- claude_cowork_all65_completion_table.csv
- claude_cowork_codebook_expansion_candidates.csv
- claude_cowork_transfer_only_or_open_container.csv
- claude_cowork_source_check_needed.csv
- claude_cowork_all_question_completion_report.md

如果不能写文件，请直接在对话中输出完整结果，我会手动保存。

【最后输出】
1. 可新增到 provisional_codebook_v1 的候选观察。
2. 只能修订现有 code 的候选观察。
3. 只能保持 transfer/open-container 的题或 cluster。
4. 应明确 reject 的题或 cluster。
5. 仍需回源核查的题号。
6. 你对 framework_v1 能否修订为 v2 的建议，但不要写 v2 框架。

再次强调：本轮禁止输出最终框架和宝典。
