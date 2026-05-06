# Claude Opus 4.7 Adaptive Phase12 77-Row Teaching Review Prompt

你是教学成文化审稿线，不是证据源。任何新表达必须能回到 Codex source lock。不要输出 Word/PDF/final。

本轮任务：审查选必三《逻辑与思维》Phase12 77 条 review-only 扩展正文。

硬背景：
- 29 条候选稿已被用户否决为题量过少，只能叫 controlled packet，不得称终稿。
- 已按你的 Phase12 指挥稿完成 74-row 全裁决、45 non-body repair、362-row rescan。
- 当前正文 77 条：主观题 27，选择题 50。
- 正文排序规则：主观题在前，选择题在后；每类内部按海淀、西城、东城、朝阳、丰台、其他区；年份 2026 > 2025 > 2024。
- 已生成双索引：思维方法索引、推理题型索引。
- 选择题完整选项可见性已修复：50 道选择题中 24 道显示完整 ①②③④ 选项单位，26 道显示 A/B/C/D 选项，修复队列为 0。
- 未找到可靠答案或视觉证据的题继续 blocked，没有逻辑猜答案。
- 请不要授权 Word/PDF/final；只做内容审查和下一步修补建议。

请重点审：
1. 77 条里有没有明显漏题、误入、重复或该 blocked 却入正文的题。
2. 主观题四要件是否像哲学宝典：材料信号、可写方法、为什么能想到、答案落点都足够具体。
3. 推理题是否有逻辑形式、规则口令、有效/无效式、错项陷阱。
4. 选择题是否都不是只写答案字母，而是有正确项理由和错项陷阱。
5. 双索引是否真正把同类题挂全，而不是只放代表例。
6. 哪些条目必须回源修复，哪些只是表达可优化。

请输出：
- verdict: GO_EXTERNAL_PATCH / MUST_FIX_CONTENT / HOLD_SOURCE_REPAIR / READY_FOR_FINAL_CLEAN_BUILD_BUT_NO_WORD
- must_fix
- should_fix
- source_or_scope_risks
- index_risks
- merge_policy
- next_commands_for_codex

需要审的文件：
- 09_student_draft/phase12_expanded_body_FROM_362_REVIEW_ONLY.md
- 09_student_draft/phase12_expanded_body_FROM_362_control_matrix.csv
- 09_student_draft/phase12_thinking_method_index.md
- 09_student_draft/phase12_reasoning_typology_index.md
- 09_student_draft/phase12_sort_key_matrix.csv
- 05_coverage/phase12_362_control_base_rescan_summary.md
- 08_review/phase12_codexA_local_review_gate.md
- governor_confucius/phase12_governor_gate.md
- governor_confucius/phase12_confucius_learning_gate.md

请特别用弱学生视角检查：是否看完能迁移到新题，哪些条目仍像审计话而不像卷面答案。
