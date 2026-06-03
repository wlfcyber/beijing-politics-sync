你现在进入“选必二《法律与生活》主观题框架从题源生长工程”的候选框架阶段。

你将基于经过 Codex A、ClaudeCode B、Claude Cowork 题层修复，以及 GPT-5.5 Pro / Claude Opus 双模型开放观察交叉验证后的 `provisional_codebook_v0`，生成候选主观题框架。

注意：
1. 现在可以提出候选框架，但不能脱离代码本。
2. 每个框架节点必须追溯到 code_id、question_id、rubric_atom_id、material_atom_id。
3. 不得凭法学常识、教材目录、漂亮概念生成节点。
4. 框架必须服务主观题作答，不服务选择题。
5. 框架必须能指导学生从材料生成满分答案。
6. 框架不能法考化。
7. 框架不能必修三化。
8. 框架不能只做教材目录。
9. 旧 53/56/66/v3/ClaudeCode-corrected 模型输出、旧 framework_v1/v2、旧宝典均已作废为历史审计，不能作为框架来源。
10. 当前有效输入只有 cowork-refined 65 题包、7 条 provisional codebook、codebook evidence map、cross-validation 表和 pending/source-check 表。

【输入包】
请读取附件：
`candidate_framework_input_cowork_refined_20260519.zip`

附件内包含：
- `provisional_codebook_v0.csv`
- `provisional_codebook_v0.md`
- `codebook_source_evidence_map.csv`
- `codebook_risks.md`
- `merged_subjective_law_questions.csv`
- `merged_material_atoms_subjective.csv`
- `merged_ask_atoms_subjective.csv`
- `merged_rubric_atoms_subjective.csv`
- `gpt_claude_observation_comparison.md`
- `gpt_claude_observation_comparison.csv`
- `observations_needing_source_check.csv`
- `boundary_mixed_or_blocked_cases.csv`
- `suite_exhaustion_report.md`

【当前数据口径】
- core subjective law questions: 65
- formal: 61
- reference_only: 4
- missing: 0
- material atoms: 482
- ask atoms: 65
- rubric atoms: 350
- codebook rows: 7
- pending/source-check observations: 23，不能直接支撑核心节点，但可提醒开放容器或风险边界。

【任务】
请生成 1-3 套候选主观题框架，并比较优劣。

每套候选框架必须包括：
1. 框架名称，暂名即可。
2. 框架总逻辑。
3. 每个节点的功能。
4. 每个节点对应的 code_id。
5. 每个节点支持的 question_id 和 rubric_atom_id。
6. 每个节点的材料触发信号。
7. 每个节点要求学生完成的最小必要判断。
8. 每个节点如何生成满分句。
9. 每个节点的易错偏题风险。
10. 哪些题能顺利解决。
11. 哪些题解决不好。
12. 哪些节点证据强。
13. 哪些节点证据弱。
14. 是否有法考化风险。
15. 是否有必修三化风险。
16. 是否学生考场可启动。

【额外要求】
1. 7 条 codebook 之外的观察，不得变成核心节点；最多作为“开放容器待验证”或“风险提醒”。
2. 如果 7 条 codebook 不足以覆盖 65 题，请明确指出覆盖缺口，而不是凭空补节点。
3. 对 reference_only 题，只能说明可参考，不能宣称满分闭环。
4. 对 pending/source-check 观察，必须标明 pending，不得偷升格为 strong。
5. 最后推荐一套最值得压测的候选框架，并说明为什么它最适合全题压测。

请输出 Markdown。不要写最终宝典，不要写最终框架定稿。
