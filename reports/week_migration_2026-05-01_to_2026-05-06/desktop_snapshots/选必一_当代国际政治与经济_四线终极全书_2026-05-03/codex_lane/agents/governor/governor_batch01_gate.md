# Codex-A Governor Batch 01 Gate

Run: 选必一《当代国际政治与经济》四线终极全书 2026-05-03

Role: Codex production lane A / 监管者-Governor

结论：PASS_WITH_FIXES

Batch 01 可以进入补丁/融合候选，但不能原样直接进入稳定主表。必须先完成本报告列出的修补项；仍禁止学生终稿、Word/PDF、coverage closed、FINAL_ACCEPTANCE PASS。

## 已读依据

- `MASTER_REQUIREMENTS.md`
- `USER_FRAMEWORK.md`
- `00_control/NOTEBOOK_DIGEST.md`
- `00_control/EVIDENCE_PRIORITY_RULES.md`
- `codex_lane/agents/worker/worker_batch01_entries.md`
- `codex_lane/agents/worker/worker_source_notes.csv`
- `codex_lane/agents/governor/governor_startup_gate_round2.md`
- `feige-politics-garden-xuanbiyi/references/current-user-requirements.md`
- `feige-politics-garden-xuanbiyi/references/xuanbiyi-term-protocol.md`

## Batch 01 范围

- worker 条目数：25 条。
- source notes：12 行。
- 覆盖题目：2026通州期末 Q20、2026朝阳期中 Q17、2025海淀期中 Q16(2)、2025海淀期中 Q21(2)、2024东城一模 Q16、2024东城一模 Q20。

## 门禁检查

| 检查项 | 判定 | Governor 结论 |
|---|---|---|
| 必备字段 | PASS | 25 条均有完整设问、细则位置、来源、材料触发、答案句、证据状态。 |
| 证据状态 | PASS_WITH_GUARD | P0 formal scoring、用户确认图片评分材料、P2 teaching/analysis PPT 均已区分；未发现把普通参考答案升格为细则。融合候选必须继续保留这些证据标签。 |
| 答案句禁词 | PASS | 答案句未命中 `本题需要/设问要求/细则要求/采分点/要落到/材料中/v7/v8/debug/audit/模型聊天/后台/证据层级` 等禁词。 |
| 2026通州期末 Q20 | PASS | 六点完整：全球治理观、时代主题/经济全球化/顺应人民愿望、《联合国宪章》、国际秩序方向、人类命运共同体、中国智慧中国方案/大国担当。人类命运共同体单独列点，未错归为四大全球倡议替代项。 |
| 2026朝阳期中 Q17 | PASS_WITH_FIXES | 总说/分说结构基本完整：自力更生与开放、发展与安全、中国发展与世界发展均拆出。已排除“创新的新发展理念”和高质量发展/经济增长等部分边界项，但仍有跨模块词留在术语原词中，需修补后再入 fusion candidate。 |
| 2025海淀期中 Q16/Q21 | PASS | worker 使用 `user_confirmed_image_scoring_material`，写明 raw DOCX 内嵌图片哈希核验一致；文本答案只作可读支持，未冒充细则。 |
| 2024东城一模 Q16/Q20 | PASS_WITH_GUARD | P2 标注保守且清楚，未冒充 P0。可进入融合候选，但必须继续标为 P2/讲评PPT含给分信息，不得与正式评分细则混成同一证据层级。 |

## 必须修补后再融合

1. Q17 跨模块边界：以下词不应作为选必一主链核心术语直接融合，需移入边界说明、材料支撑或删出核心名：
   - `开放型经济 / 双循环`（worker 第81行）
   - `政府履行经济职能监管 / 完善法律法规`（worker 第99行）
   - `产业结构优化升级`（worker 第117行，第123行答案句也需谨慎处理）
2. 补 source_id/ledger 回链：worker 条目和 `worker_source_notes.csv` 当前有 source_path 和位置，但未写 `SOURCE_LEDGER.csv` 的 `source_id/ledger_id`。进入 fusion candidate 前，每条至少要能回链到 source notes 行；正式提升前必须回链到 source ledger。
3. 材料触发文字微修：部分材料触发用了“需要写/必须说明/回答……”等制作口吻。它们不在答案句中，暂不阻断 fusion candidate，但进入学生化或最终融合前应改成纯触发逻辑。
4. `术语原词` 字段可作为 worker 草案存在；进入正式融合表时应规范为 `术语：` 或 `核心采分点：`，并保留原词不压缩。

## 不允许的动作

- 不得把 Batch 01 宣称为 coverage closed。
- 不得生成或放行学生终稿、Word/PDF、频次统计终版、FINAL_ACCEPTANCE PASS。
- 不得把 2024东城一模 P2 证据写成 P0。
- 不得把 2025海淀期中普通文本答案单独升级为评分术语。
- 不得把 Q17 的必修二/政治与法治/一般经济治理词塞入选必一主链。

## 放行范围

允许进入：

- patcher 复查
- fusion candidate 草案
- 同核心合并候选表
- source-backed draft table

进入条件：

- 本报告“必须修补后再融合”4 项完成或在 fusion candidate 中逐条标注为 `boundary_pending`。
- fusion candidate 状态只能是 `draft/not_promoted` 或 `candidate_with_fixes`。

Governor 签发：Batch 01 不是 FAIL；可进入补丁/融合候选，但必须带修补项，不得直接放行终稿或覆盖闭合。
