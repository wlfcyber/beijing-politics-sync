# 回退声明：退回 Codex + ClaudeCode 65 题证据层

时间：2026-05-20

## 用户裁决

用户明确否定后续学生版/宝典式框架稿：

- 认为当前学生稿仍然不能让学生看完就接近满分；
- 要求退回到 “Codex 和 ClaudeCode 生成出 65 套题” 的阶段。

## 当前 active baseline

本工程当前 active baseline 已回退到：

`STEP_29_CLAUDECODE_CORRECTED_CORPUS`

证据目录：

`04_merge_audit/suite_exhaustive_claudecode_corrected_20260519/`

当前已复制为回退工作副本：

`04_merge_audit/rollback_to_step29_claudecode_corrected_65_20260520/`

当前 reasoner 重启包副本：

`05_reasoner_packets/rollback_to_step29_claudecode_corrected_65_20260520/`

## 当前 canonical merged 文件状态

以下四个 canonical 文件已重新指向 STEP_29 基线：

- `04_merge_audit/merged_subjective_law_questions.csv`
- `04_merge_audit/merged_material_atoms_subjective.csv`
- `04_merge_audit/merged_ask_atoms_subjective.csv`
- `04_merge_audit/merged_rubric_atoms_subjective.csv`

当前计数：

- 主观题：65
- formal：61
- reference_only：4
- missing：0
- material atoms：541
- ask atoms：65
- rubric atoms：362

## 当前弃用范围

以下阶段不再作为当前框架/宝典基础：

- STEP_30B 之后的 Cowork-refined reasoner packet；
- STEP_31 之后的 GPT/Claude open observations；
- STEP_32 之后的 cross-validation/codebook；
- STEP_33 之后的 candidate frameworks；
- STEP_34 之后的 framework_v1/v2；
- STEP_50 之后的 guarded baodian；
- STEP_58 zero-baseline patch；
- STEP_59 GPTPro quality challenge；
- STEP_60 student battle baodian。

这些文件保留为历史和失败尝试，不删除、不继续缝补、不用于下一轮学生框架。

## 重要注意

STEP_29 之后曾发现过题面/材料层污染风险，并在 STEP_30A/30B 做过清洗。
本次按用户要求回到 Codex + ClaudeCode 65 题证据层，因此下一步不能立刻写框架。

下一步应是：

1. 只围绕 STEP_29 的 65 题做题卡级复核；
2. 检查每题题干、材料、设问、答案/细则是否分栏干净；
3. 如需要 ClaudeCode 正式复核，必须按用户新规则走 VS Code ClaudeCode，而不是 CLI；
4. 复核通过后，再从“学生如何启动”的角度重建框架。

