你现在是“选必二《法律与生活》主观题框架从题源生长工程”的独立专项审计者。

本轮只审查 v1.1 句子级压测后仍为 FAIL 的 4 道题。你的任务不是写最终框架，也不是扩写宝典，而是判断这 4 道题应该如何处理：

1. 是否应补入核心代码本；
2. 是否只能进入开放容器；
3. 是否应作为边界题从选必二法律主观题核心框架中排除；
4. 是否需要再次回源拆细则原子。

【输入包】
`fail4_targeted_adjudication_20260519.zip`

包内包括：
- `merged_subjective_law_questions.csv`
- `merged_material_atoms_subjective.csv`
- `merged_rubric_atoms_subjective.csv`
- `provisional_codebook_v1_1_after_cc0364_split_20260519.csv`
- `framework_v1_1_question_by_question_sentence_pressure_test_20260519.csv`
- `fail4_source_adjudication_20260519.csv`
- `FAIL4_TARGETED_ADJUDICATION_README.md`

【必须审查的 question_id】
- `CC0143_2025_朝阳_一模_19`
- `CC0276_2026_房山_二模_17`
- `RECOVER_2026_西城_二模_18_2`
- `RECOVER_2026_西城_二模_18_3`

【硬规则】
1. 只研究主观题。
2. 不分析选择题。
3. 不写最终框架。
4. 不写宝典正文。
5. 参考答案不得冒充评分细则；但本轮四题均有 formal 或已标明证据等级，请复核是否合理。
6. 不能因为题里有“法治”“法律”“权利”“责任”就强行进选必二核心。
7. 不能把明显必修三/综合法治/国家治理能力现代化题硬塞进选必二《法律与生活》核心框架。
8. 也不能因为它低频就漏掉真正的消费者权益、合同、侵权、责任边界等选必二法律得分机制。
9. 每条判断必须引用 question_id 和具体 rubric_atom_id；没有证据编号不得作核心建议。

【逐题问题】
对每道 FAIL 题回答：

1. 它是否真属于选必二《法律与生活》主观题核心语料？
2. 如果是，它最应归入哪个既有 code_id，还是需要新增候选 code？
3. 如果只能开放容器，理由是什么？
4. 如果应排除核心，理由是什么？
5. 它的细则原子是否已经足够拆分？如不足，请列出需要拆分/删除/降级的 atom_id。
6. 学生最先必须判断什么？
7. 该题会不会诱导学生写成必修三法治建设题？
8. 该题会不会诱导学生写成法考化复杂分析？
9. 它若进入核心代码本，会不会误导同类题？

【输出格式】
请输出 CSV 或 Markdown 表格，字段固定为：

question_id
final_recommendation：promote_core / revise_existing_code / open_container_only / exclude_core / source_check_needed
recommended_code_id_or_new_label
supporting_rubric_atom_ids
supporting_material_atom_ids
evidence_level
module_boundary_decision
what_student_must_judge
why_not_bixiusan_or_why_is_bixiusan
risk_if_promoted
risk_if_excluded
needed_atom_patch
reason

【最终结论】
给出：

1. 哪些题可以进入核心代码本；
2. 哪些题只能开放容器；
3. 哪些题应排除核心；
4. 哪些题需要回源补原子；
5. 当前是否允许基于 65 题继续生成 framework_v2。

再次强调：本轮禁止输出最终框架。
