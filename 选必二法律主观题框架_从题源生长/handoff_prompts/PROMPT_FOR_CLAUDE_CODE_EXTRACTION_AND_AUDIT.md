# Claude Code B Prompt: 选必二《法律与生活》主观题框架从题源生长工程

你现在是“选必二《法律与生活》主观题框架从题源生长工程”的 Claude Code B：独立证据抽取者与审计者。

你不能默认相信 Codex 的结论。你要独立读取原始文件，独立抽取选必二法律主观题候选、答案、细则、材料原子、设问原子、细则原子。

本工程目前只研究主观题，选择题全部忽略。

## 当前 Mac 路径映射

Windows 输入目录在本机对应为：
- /Users/wanglifei/Desktop/2024模拟题
- /Users/wanglifei/Desktop/2025模拟题
- /Users/wanglifei/Desktop/2026模拟题
- /Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中
- /Users/wanglifei/GaokaoPolitics/2024各区模拟题
- /Users/wanglifei/GaokaoPolitics/2025各区模拟题
- /Users/wanglifei/GaokaoPolitics/2026各区模拟题

输出目录：
/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长

你可以把 Codex A 已生成的 00_manifest/source_manifest.csv 作为索引，但不能把 Codex A 的候选结论当作事实。你必须独立回源，尤其检查 Codex 是否漏题、误收、证据等级升级、页码题号错误、模块边界误判。

请输出：
- 01_subjective_candidates/all_candidate_subjective_law_questions_claudecode.csv
- 01_subjective_candidates/all_candidate_subjective_law_questions_claudecode.jsonl
- 02_material_atoms/material_atoms_subjective_claudecode.csv
- 02_material_atoms/ask_atoms_subjective_claudecode.csv
- 03_rubric_atoms/rubric_atoms_subjective_claudecode.csv
- 04_merge_audit/claudecode_independent_audit_report.md
- 04_merge_audit/claudecode_missing_from_codex.csv
- 04_merge_audit/claudecode_false_positive_candidates.csv
- 04_merge_audit/claudecode_evidence_level_disagreements.csv
- 04_merge_audit/claudecode_module_boundary_disagreements.csv
- 04_merge_audit/claudecode_locator_or_ocr_risks.csv

## 硬规则

1. 只研究主观题。
2. 不分析选择题。
3. 不写框架。
4. 不总结规律。
5. 不按教材目录归类。
6. 不使用预设结构。
7. 不得把参考答案冒充评分细则。
8. 必修三法治建设题、经济题、哲学题、逻辑题不得因为出现“法律”“权利”“责任”“法治”就误收为选必二。
9. 对扫描 PDF、图片 PDF、无文本层文件必须处理或记录失败原因。
10. 每个争议都要给出原始文件、页码、题号、理由。
11. 旧选必二成果全部作废，不得作为证据或结论。
12. 2026石景山期末继续排除，除非发现用户新提供的可用评分细则。

请严格区分 evidence_type 和 evidence_level：
- evidence_type: official_rubric / marking_rubric / evaluation_standard / grading_commentary / marking_report / lecture_explicit_scoring / teacher_reference_answer / student_answer_sample / missing
- evidence_level: formal / user_confirmed / reference_only / missing

formal 只给官方评分细则、阅卷细则、评标、阅卷报告、明确给分口径。
reference_only 只能作为辅助理解，不得单独支撑框架核心节点。
missing 不得进入归纳，只能进入待补证据清单。

## 候选主观题字段

question_id, year, district, exam_stage, source_paper_file, paper_page, question_no, sub_question_no, full_question_text, material_text, ask_text, answer_file, answer_page, answer_text, rubric_file, rubric_page, rubric_text, evidence_type, evidence_level, why_candidate_subjective_law_question, why_maybe_not_subjective_law_question, module_boundary_risk, confidence, source_locator, notes

## 原子字段

material_atoms 字段：material_atom_id, question_id, material_phrase, plain_description, subject_or_actor, action_or_event, affected_party, conflict_or_problem, legal_signal_if_any, possible_relevance_to_answer, source_locator, uncertainty

ask_atoms 字段：ask_atom_id, question_id, ask_text, ask_function_plain, module_requirement, requires_material_connection, requires_value_discussion, requires_behavior_evaluation, requires_solution_or_measure, student_task_plain, source_locator

rubric_atoms 字段：rubric_atom_id, question_id, rubric_or_answer_phrase, evidence_type, evidence_level, plain_reward_description, related_material_atom_ids, what_expression_is_rewarded, what_judgment_student_must_make_before_writing, legal_knowledge_or_rule_if_explicit, value_expression_if_explicit, knowledge_material_value_type, can_be_written_without_material, source_locator, uncertainty

## 审计报告必须给出

PASS / CONDITIONAL_PASS / FAIL，并说明：
1. Codex 是否漏题。
2. Codex 是否误收。
3. Codex 是否把 reference_only 升级成 formal。
4. 哪些题必须降级。
5. 哪些题不能进入 GPT/Claude 归纳。
6. 哪些题可以进入第一轮开放归纳。

请直接在输出目录写文件。完成后最后只简短报告已写文件清单和 PASS/CONDITIONAL_PASS/FAIL。