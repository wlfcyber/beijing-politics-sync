# 给 GPT-5.5 Pro 的选必三学生清洁候选稿复审请求

请只审内容质量、学生可学性、题型/思维归类准确性和是否仍有审计话术残留，不要要求生成 Word。

本轮候选稿路径：

- 学生清洁候选正文：`09_student_draft/phase12_student_clean_candidate.md`
- 推理题型索引：`09_student_draft/phase12_reasoning_typology_index_STUDENT_CLEAN_CANDIDATE.md`
- 思维方法索引：`09_student_draft/phase12_thinking_method_index_STUDENT_CLEAN_CANDIDATE.md`
- 追溯矩阵：`08_review/phase12_student_clean_traceability_matrix.csv`
- 清洁构建审计：`08_review/phase12_student_clean_build_audit.md`

请重点检查：

1. 77 条是否仍显得穷尽、具体、像哲学宝典那样逐题可学。
2. 50 道选择题是否都有完整选项、正确项理由、错项陷阱。
3. 27 道主观题是否都有材料信号、可写方法/规则、为什么触发、答案落点、易错陷阱和同类题。
4. 推理索引是否仍有充分条件/必要条件、三段论大小项、边界陷阱误挂。
5. 思维索引是否仍把边界陷阱当正例。
6. 学生正文中是否还残留 review-only、source、phase、manual_lock、qid 等内部审计语言。

请给 verdict：

- CLEAN_PASS_TO_WORD_PREP
- PATCH_REQUIRED_NO_WORD

如果需要返修，请按 question title 精确列出 must_fix / should_fix。
