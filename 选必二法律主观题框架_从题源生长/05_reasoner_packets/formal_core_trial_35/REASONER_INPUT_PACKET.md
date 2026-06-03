# REASONER_INPUT_PACKET

## 工程目标

从 2024-2026 北京各区选必二《法律与生活》主观题与 formal 评分证据中，开放归纳命题机制、判分机制和学生作答机制。本轮只做观察，不写框架。

## Scope

- 只研究主观题。
- 选择题不进入框架，不分析错项。
- 不预设“一核二线三问四步五域”“动作库”“故事卡”“法律关系路由”。
- 不按教材目录先搭框架。
- 参考答案不得冒充评分细则。

## Data Range

- merged canonical candidates: 74
- reasoner formal subset: 35
- formal total in merged: 54
- reference_only total in merged: 3
- missing total in merged: 17
- locator/OCR risk excluded from reasoner subset: 22
- module boundary disputes excluded from reasoner subset unless resolved formal: 35

## Input Files

- merged_subjective_law_questions_for_reasoners.csv
- merged_material_atoms_subjective_for_reasoners.csv
- merged_ask_atoms_subjective_for_reasoners.csv
- merged_rubric_atoms_subjective_for_reasoners.csv
- merge_audit_report_for_reasoners.md

## Unified Task

基于每一道题的 question_id、rubric_atom_id、material_atom_id，逐题分析模块边界、设问任务、最小必要判断、材料事实与细则触发、得分机制、满分句生成、迁移与代码本资格。

## Output Requirement

每条 observation 必须包含 evidence ids；没有 question_id、rubric_atom_id、material_atom_id 的观察不得进入下一轮。最后分为强观察、弱观察、冲突观察、不应上升为框架的观察、下一轮需补充题型。

本轮禁止输出总框架。
