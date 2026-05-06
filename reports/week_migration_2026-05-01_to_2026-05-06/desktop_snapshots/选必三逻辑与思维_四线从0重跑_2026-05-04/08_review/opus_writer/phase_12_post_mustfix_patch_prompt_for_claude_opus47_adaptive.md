# Claude Opus 4.7 Adaptive Teaching Review Prompt: Phase12 Post-MUST_FIX Patch

你是选必三《逻辑与思维》教学成文化审稿线，不是证据源。不要生成 Word/PDF/final。

## 当前稿件

- `09_student_draft/phase12_expanded_body_FROM_362_REVIEW_ONLY.md`
- `09_student_draft/phase12_reasoning_typology_index_REBUILT.md`
- `09_student_draft/phase12_thinking_method_index_REBUILT.md`
- `08_review/phase12_external_patch_resolution.md`
- `08_review/phase12_post_patch_index_audit.md`
- `08_review/phase12_post_patch_addendum_Q2025_shunyi_yimo_7.md`

## 背景

当前稿共 77 条，主观题 27，选择题 50。它已经修复 GPT 外审提出的主要问题：

- `2024 海淀二模17(1)` 按原题科学思维设问处理；
- 推理索引重建；
- 思维索引重建；
- 边界陷阱不再作为正向方法例题。
- `2025 顺义一模7` 已补丁锁定：真实错误为大项不当扩大，A 项误称小项不当扩大。

但它仍然是 review-only，不能授权终稿。

## 请重点从学生学习角度审查

1. 弱学生看完每条，能不能知道“材料怎么看”。
2. 主观题的答案落点是否真像卷面答案，不像审计话。
3. 推理题是否能让学生按规则口令做同类题。
4. 选择题错项陷阱是否能迁移。
5. 双索引是否帮助学生找同类题，还是仍有误导风险。
6. 哪些条目应该压缩、改写或增加一句“考场动作”。
7. final clean index 中 `NEEDS_*` 审计节点应如何转成学生可读的非正例标签。

## 输出

请输出：

- verdict: `TEACHING_REVIEW_PASS_NO_FINAL` / `MUST_FIX_TEACHING_TEXT` / `HOLD_INDEX_CLARITY`
- must_fix
- should_fix
- examples_of_good_entries
- examples_of_weak_entries
- final_clean_build_advice

不要写 Word/PDF/final 授权。
