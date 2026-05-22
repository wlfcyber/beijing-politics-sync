你现在进入“选必二《法律与生活》主观题框架从题源生长工程”的候选框架阶段。

你将基于经过双模型交叉验证的 provisional_codebook_v0 生成候选主观题框架。

注意：
1. 现在可以提出候选框架，但不能脱离代码本。
2. 每个框架节点必须追溯到 code_id、question_id、rubric_atom_id、material_atom_id。
3. 不得凭法学常识、教材目录、漂亮概念生成节点。
4. 框架必须服务主观题作答，不服务选择题。
5. 框架必须能指导学生从材料生成满分答案。
6. 框架不能法考化。
7. 框架不能必修三化。
8. 框架不能只做教材目录。

【输入】
provisional_codebook_v0.csv
codebook_source_evidence_map.csv
merged_subjective_law_questions.csv
merged_material_atoms_subjective.csv
merged_ask_atoms_subjective.csv
merged_rubric_atoms_subjective.csv
gpt_claude_observation_comparison.md

【任务】
请生成 1—3 套候选主观题框架，并比较优劣。

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

请最后推荐一套你认为最值得压测的候选框架，并说明原因。
