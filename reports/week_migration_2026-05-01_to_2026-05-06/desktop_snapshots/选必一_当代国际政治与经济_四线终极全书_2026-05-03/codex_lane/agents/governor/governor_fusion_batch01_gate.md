# Codex-A Governor Fusion Batch 01 Gate

Run: 选必一《当代国际政治与经济》四线终极全书 2026-05-03

Role: Codex production lane A / 监管者-Governor

结论：PASS_WITH_FIXES

Batch 01 融合候选可以进入 Batch02 源复核；可以准备 `section_batch` 内部草稿，但必须保持 `draft/candidate_with_fixes` 状态。不得进入学生终稿、Word/PDF、coverage closed、频次终版或 FINAL_ACCEPTANCE PASS。

## 已读依据

- `MASTER_REQUIREMENTS.md`
- `feige-politics-garden-xuanbiyi/SKILL.md`
- `feige-politics-garden-xuanbiyi/references/current-user-requirements.md`
- `feige-politics-garden-xuanbiyi/references/xuanbiyi-term-protocol.md`
- `06_conflicts/ab_difference_table_batch01.md`
- `fusion/scoring_atom_table_batch01.csv`
- `fusion/merge_register_batch01.md`
- `fusion/module_boundary_notes_batch01.md`
- `fusion/fusion_candidate_batch01.md`
- `08_review/gpt_phase_fallback_log.md`

## 核查结果

| 检查项 | 判定 | Governor 结论 |
|---|---|---|
| 证据边界 | PASS_WITH_FIXES | `scoring_atom_table_batch01.csv` 25 行均为 `candidate_with_fixes`；P0、P2、用户确认图片评分材料均有标签。仍缺少 `SOURCE_LEDGER.csv` 的 source_id/ledger_id 回链，正式 section_batch 送审前必须补。 |
| P2 标识 | PASS | 2024东城一模 Q16/Q20 共 5 条均标为 `P2_teaching_or_lecture`，merge register 明确不得静默计入 P0 频次。 |
| 海淀图片细则升级裁决 | PASS | 2025海淀期中 Q16(2)、Q21(2) 均标为 `user_confirmed_image_scoring_material` / `embedded_docx_image_verified`，不是普通文本答案冒充细则；B 线 P1 blocker 已由 Codex A 本地视觉证据覆盖。 |
| Q17 模块边界 | PASS_WITH_FIXES | `module_boundary_notes_batch01.md` 已把开放型经济、双循环、创新的新发展理念、高质量发展、政府经济职能、法律法规、产业结构优化升级等排除或降为 boundary support。section_batch 必须沿用这个边界，不得把这些词写成选必一主链核心。 |
| 通州 Q20 / 人类命运共同体 | PASS | merge register 和 fusion candidate 均明确 HMC 主归中国桶，不是“四大全球倡议”的下位项；全球治理观归政治多极化，正确义利观从同一 optional group 拆到中国桶。 |
| 学生稿禁入词 | PASS_WITH_FIXES | `fusion_candidate_batch01.md` 仍有“先判断是否需要写”“不能只写/还要写”这类教研口吻。它们可留在 fusion control 层，但进入 `section_batch` 学生向草稿前必须改写为迁移提示式表达。未发现 `debug/audit/模型聊天/采分点/要落到/材料中/v7/v8` 进入候选正文。 |
| GPT/Claude 外部审稿状态 | PASS_WITH_GUARD | `gpt_phase_fallback_log.md` 记录 Claude Opus 因屏幕锁定未捕获，且明确“不进入 student final 或 Word/PDF”。本地证据工作可继续；不得使用未捕获的 Claude 文本。 |

## 允许动作

1. 进入 Batch02 源复核，优先处理 B-only closed candidates：2026朝阳一模 Q20、2026顺义一模 Q20、2025海淀二模 Q21、2025海淀期末 Q22。
2. 继续维护 `fusion/scoring_atom_table_batch01.csv`、`merge_register_batch01.md`、`module_boundary_notes_batch01.md`，但不得改成 closed/final。
3. 准备 `section_batch` 内部草稿，前提是：
   - 保留证据层标签或在教师/审核层可回溯；
   - 移除 fusion 文本中的教研口吻；
   - 不把 P2/P0 混同；
   - 不把 Q17 boundary support 写成主链核心。

## 必须修补

1. 给 scoring atoms 增补 source-ledger 回链：至少能对应 `SOURCE_LEDGER.csv` 的 source_id/ledger_id 或明确写 `user_confirmed_image_scoring_material` 的图像来源记录。
2. 对 2025海淀期中 Q21(2) 图片备注作最终分类：`国际影响力话语权`、`人类命运共同体`、`国家利益` 是可用表述、替代表述，还是不累计提示，不能作为未判明的 standalone term 进入 section_batch。
3. 清理学生向草稿禁入表达：`先判断是否需要写`、`不能只写/还要写` 等要改成“适用情境/迁移动作”，不能保留为最终学生稿口吻。
4. `gpt_phase_fallback_log.md` 中 Claude Opus 捕获仍 pending；若 section_batch 需要外部教学化建议，必须后补或记录 waiver，不得假装已审。

## 禁止动作

- 禁止学生终稿、Word/PDF、频次统计终版、coverage closed、FINAL_ACCEPTANCE PASS。
- 禁止把 2024东城一模 P2 证据升格为 P0。
- 禁止把 2025海淀期中普通参考/文本答案升级为细则；只允许用户确认图片评分材料进入候选。
- 禁止把 Q17 的必修二、政治与法治、一般经济治理词塞入选必一主链。
- 禁止把 ClaudeCode B-only 候选直接并入主表或频次，必须先经 Codex A Batch02 源复核。
- 禁止使用未捕获的 Claude Opus 文本。

Governor 签发：Fusion Batch 01 通过但带修补项。可以进入 Batch02 源复核；section_batch 仅限内部草稿/待审稿，不得视为学生终稿或闭合产物。
