你现在是“选必二《法律与生活》主观题框架从题源生长工程”的独立代码本扩展审议者。

你收到的是同一套 65 道选必二法律主观题证据、当前 7 条 provisional codebook、framework_v1 压测结果、Claude Cowork 全题完善建议、以及 Codex 对 Cowork 点名 5 道阻断题的回源核查。

你的任务不是写最终框架，也不是写宝典。你的唯一任务是：独立判断 Cowork 提出的代码本扩展/修订建议，哪些有足够证据进入下一版 codebook，哪些只能作为开放容器，哪些必须拒绝或继续回源。

【最高硬规则】
1. 本轮禁止输出最终框架、框架 v2、口诀、学生版、教师稿、宝典目录或逐题满分答案。
2. 每个保留/修订/新增观察必须有 question_id、rubric_atom_id 或 corrected proposed_rubric_atom_id、material_atom_id。
3. 普通参考答案、reference_only 行不能单独支撑核心 code。
4. 不得把“学生问题及建议”“教学建议”“典型错误”当作评分细则原子。
5. 特别注意：CC0254 当前 canonical rubric atoms R01-R08 来自学生问题/建议段，不可作为 scoring atom；如需要使用 CC0254，只能使用 `codex_source_check_corrected_rubric_atom_plan.csv` 中的 PATCH_CC0254_*。
6. 特别注意：RECOVER_2026_房山_一模_17_1 的 2 分解释是“主体/内容/客体任一维度解释清楚即可”，不是三个维度累加。
7. 特别注意：CC0061 必须按 18(1)、18(2)、18(3) split/trim，不能整题当一个统一机制。
8. 你可以同意 Cowork，也可以反对 Cowork；必须给证据理由。
9. 不得用教材目录、法学常识、漂亮概念补节点。
10. 你的判断只是代码本扩展审议，不是最终框架裁决。

【输入文件】
请读取并交叉使用：
- `CODEBOOK_EXPANSION_AFTER_COWORK_SOURCECHECK_INPUT_PACKET.md`
- `merged_subjective_law_questions.csv`
- `merged_material_atoms_subjective.csv`
- `merged_ask_atoms_subjective.csv`
- `merged_rubric_atoms_subjective.csv`
- `provisional_codebook_v0.csv`
- `codebook_source_evidence_map.csv`
- `framework_v1_question_by_question_test.csv`
- `framework_v1_partial_cluster_source_check.csv`
- `claude_cowork_all65_completion_table.csv`
- `claude_cowork_codebook_expansion_candidates.csv`
- `claude_cowork_transfer_only_or_open_container.csv`
- `claude_cowork_source_check_needed.csv`
- `codex_source_check_five_blocked_rows.csv`
- `codex_source_check_corrected_rubric_atom_plan.csv`

【必须审议的 Cowork 建议】
1. Cowork 唯一新核心候选：`CODE_COWORK_008 知识产权/不正当竞争司法保护四步链`。
2. Cowork 四类 existing-code revision：
   - `CODE_COWORK_001` 增加表格/单元格题的“法理依据+事实分析+意义/保障作用”子型。
   - `CODE_COWORK_002` 增加“民法基本原则/具体法律制度/典型案例示范”分支。
   - `CODE_COWORK_007` 增加“违法行为识别+法律边界/诉讼请求+程序救济+实体责任承担”扩展。
   - `CODE_COWORK_004/006` 增加“多主体评析/无显式以事实为依据锚句但仍有法理依据”分支。
3. Cowork transfer/open-container rows 是否确实不能进核心。
4. Codex 源核五题是否允许支持扩码，支持到什么程度。

【逐项判断问题】
对每个候选/修订请回答：
1. 证据是否充分？
2. 支持题是否至少有 formal 细则或明确给分口径？
3. 相关 material atom 是否真的触发该 rubric reward？
4. 学生看到陌生题时是否能用这个观察启动？
5. 它能否帮助学生把材料转为法律语言？
6. 它能否生成接近细则的满分句？
7. 它是否会误导成必修三空泛法治表达？
8. 它是否会诱导法考化过度分析？
9. 它应该进入 codebook、修改 existing code、进入 open container、还是拒绝？

【输出格式】
请输出 Markdown，并同时给出一个可转 CSV 的表格。每条 decision 使用以下字段：

expansion_decision_id:
source_suggestion_id: Cowork candidate id / Cowork cluster id / Codex source-check id / self_found_from_packet
candidate_label:
decision: accept_new_code / revise_existing_code / open_container_only / reject / source_check_needed / split_before_use
new_or_revised_code_label:
affected_existing_code_ids:
supporting_question_ids:
supporting_rubric_atom_ids_or_patch_atom_ids:
supporting_material_atom_ids:
evidence_level_summary:
what_student_must_judge:
material_trigger_pattern:
legal_knowledge_or_rule_pattern:
rubric_reward_pattern:
full_score_sentence_pattern:
risk_of_empty_value_talk:
risk_of_legal_exam_overanalysis:
module_boundary_risk:
counterexamples_or_limits:
confidence:
reason:

【最后必须输出】
1. 可以进入下一版 codebook 的新增 code。
2. 可以修订 existing code 的修订项。
3. 只能进开放容器/迁移提醒的项。
4. 必须拒绝的项。
5. 仍需回源的项。
6. 对 Codex 下一步本地裁决的建议。

再次强调：本轮禁止写最终框架，禁止写宝典，禁止用没有 evidence id 的观察支撑任何 code。
