# V5.9 双审门禁修补报告

生成时间：2026-05-21 04:42 CST

## 输入

- GPTPro V5.8 终审：`06_open_observations/gptpro_v5_8_final_gate_review_20260521.md`，裁定 PASS / YES_WITH_GUARDS。
- Claude Opus V5.8 终审：`06_open_observations/claude_opus_v5_8_final_gate_review_20260521.md`，裁定 PASS / YES_WITH_GUARDS。
- 比较表：`07_cross_validation/v5_8_gptpro_claude_final_gate_comparison_20260521.md`。

## 已执行修补

1. 学生稿生成 V5.9：补 5 道 low-frequency 题视觉红线；修 RECOVER_2026_西城_二模_18_3 边界话术；修 CC0103 裸写法治中国风险；替换 AI 题“侵权构成要件”为“侵权责任成立条件”。
2. 逐题运行 CSV 生成 V5.9：`minimum_judgment` 全部改为 `主卡=...；辅卡=...；先判=...` 格式，不再保留旧 `X + Y` 多卡写法；CC0223 `material_trigger` 删除“原卷无答案/分析/详解”之后的讲解文本。
3. CC0150 证据底座清洗副本：剔除 R12-R24 跨模块 rubric atoms，另存 excluded 文件，不覆盖 canonical。
4. CC0223 材料原子清洗副本：M09-M24 标为 audit/reference explanation，不作为材料触发；另存 audit 文件，不覆盖 canonical。
5. 27 核心细则对账留痕已在 STEP_94 生成；本轮保留其 `PASS_WITH_MANUAL_CHECK` 语义复核提示。

## 新输出

- `12_final_baodian/选必二法律主观题满分训练宝典_v5_9_27核心38题保分索引_双审门禁修补版_20260521.md`
- `12_final_baodian/question_by_question_framework_runs_v5_9_27core65guard_20260521.csv`
- `04_merge_audit/merged_rubric_atoms_subjective_v5_9_cleaned_cc0150_20260521.csv`
- `04_merge_audit/cc0150_cross_module_rubric_atoms_excluded_v5_9_20260521.csv`
- `04_merge_audit/merged_material_atoms_subjective_v5_9_cleaned_cc0223_20260521.csv`
- `04_merge_audit/cc0223_reference_explanation_material_atoms_marked_audit_v5_9_20260521.csv`

## 仍未关闭

- 还未生成 Word/PDF，因此 GPTPro/Claude 的 `YES_WITH_GUARDS` 中关于视觉红线、目录、表格溢出、reference_only/boundary 醒目标识的 QA 仍未验收。
- 17 个 `PASS_WITH_MANUAL_CHECK` 核心题需要在 Word/PDF 前做语义复核或抽样盲测确认。
- 38 非核心中的 source-check 题仍不得升核心；`CC0245` 计入 source_check_pending 但视觉红线为 DUPLICATE-CROSSREF，成稿说明必须写清。

## Codex 裁决

V5.9 可以作为 Word/PDF 候选输入；不得改口为“65 题全部核心满分闭环”。
