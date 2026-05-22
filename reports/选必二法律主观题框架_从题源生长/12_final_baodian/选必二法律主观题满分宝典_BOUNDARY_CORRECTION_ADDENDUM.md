# 选必二法律主观题满分宝典边界恢复补丁

生成时间：2026-05-19T14:30:00+08:00

## 补丁结论

本补丁 supersedes 原宝典中“37 道正文、13 道开放容器、20 道边界复核”的最终题量口径。原口径只是 v1 压测状态，不是最终法律题源总量。

经本地回源和 GPT-5.5 Pro 边界恢复复核后，当前采用分层计数：

- 严格闭合核心：48 道。
- 核心 + 开放/弱示范容器：53 道。
- `CC0229_2026_东城_一模_18` rubric atoms 已用 F0153/F0146 修复，且宝典对应段落已重生成。
- `CC0094_2025_东城_期末_19_3`、`CC0259_2026_丰台_期中_19_LAW`、`CC0118_2025_丰台_期末_18_2_LAW` 等仍是拆分/重抽/待补证据，不计入闭合题量。

## 必须修正的旧宝典条目

1. `CC0250_2026_丰台_一模_19`：从宝典和开放容器删除。本题主干是人类命运共同体、可持续发展，不是选必二法律主观题。
2. `CC0094_2025_东城_期末_19_3`：不得整题作为开放容器。它是法律与政治混合小问，且当前 rubric atoms 串到新能源、欧盟、贸易保护。必须先拆出相邻关系法律 2 分层。
3. `CC0229_2026_东城_一模_18`：rubric atoms 已用 F0153/F0146 修复为知识产权、调解、惩罚性赔偿、恶意诉讼等细则原子，宝典对应段落也已重生成。
4. `CC0373_2026_顺义_一模_17`：父题编号是 Q17 政治题，法律题应拆为 `CC0373_2026_顺义_一模_18`，只接收 Q18 劳动就业歧视与竞业限制细则。

## 当前可用文件

- `10_framework_validation/framework_v2_boundary_recovery_delta_after_gpt.csv`
- `10_framework_validation/framework_v2_boundary_recovery_delta_after_gpt.md`
- `10_framework_validation/atom_mapping_patch_queue.csv`
- `10_framework_validation/boundary_recovery_after_gpt_report.md`

## 使用禁令

在补丁队列完成前，原 `选必二法律主观题满分宝典.md` 和 `.docx` 只能作为 provisional draft，不得作为课堂最终发放版。
