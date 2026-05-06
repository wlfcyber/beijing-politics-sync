# Decision Maker Batch04L Next Step - 2026石景山一模

裁决时间：2026-05-04
角色边界：Codex A 决策者；只做分工、瓶颈和放行建议；不改 fusion / student / delivery 文件；不宣布最终成品。

## 1. 当前状态裁决

Batch04L 可以继续推进，但只能作为 `guarded candidate / expression accumulation`，不能升级为正式逐点细则候选。

- 本套是 `2026石景山一模`，不是已排除的 `2026石景山期末`，可以处理。
- Q20 是唯一进入选必一范围的 guarded 候选：题面要求从“共同 / 开放 / 包容”任选两个关键词，说明中国倡议如何助推亚太合作。
- 现有来源为官方答案及评分参考，给出“每个关键词：1个学科用语 + 合理分析 = 4分；两个关键词最高8分”的等级题规则，并列出可用角度。
- 该来源不是逐点评分细则，不得把五个 atom 当成稳定的逐点赋分槽或频次来源。
- Q16、Q17、Q18、Q19 维持 `no_xuanbiyi_boundary`；Q21 维持 `composite boundary only`。
- 学生稿、Word/PDF、FINAL_ACCEPTANCE、coverage close 继续 BLOCK。

## 2. 是否只作为 guarded 候选

裁决：是，只能作为 guarded 候选。

当前五个 SJS26 atom 的正确身份如下：

- SJS26-01 `维护共同利益`：关键词“共同”下的合作成立逻辑。
- SJS26-02 `共商共建共享`：关键词“共同”下的区域治理行动表达。
- SJS26-03 `贸易和投资自由化便利化 / 区域经济一体化 / 开放型经济格局`：关键词“开放”下的经济全球化机制表达。
- SJS26-04 `推动经济全球化更加包容、更可持续，更好惠及地区全体人民`：关键词“包容”下的经济全球化方向表达。
- SJS26-05 `人类命运共同体 / 和平发展合作共赢`：角度列举项，只能作可选升华或表述积累，不能替代两个关键词的具体分析。

这些条目可以增强既有核心的表述积累，但不能写成“石景山一模 Q20 五个必答点”。若后续 ClaudeCode B 或 Patcher 找到真正逐点细则，再重新裁定；在此之前保持 `P0_scoring_reference_level_guarded`。

## 3. Batch04L ClaudeCode 启动顺序

Batch04L 的 ClaudeCode B 不应在 Batch04K ClaudeCode screen 仍活跃时启动。

当前可见状态：

- Batch04K ClaudeCode B 已产出 `progress_batch04K.md`、entries、matrix 等文件，且 progress 写明 Done / no blockers。
- 但 screen `xuanbiyi_claudecode_batch04K_20260504` 仍处于 Detached 活跃状态。

启动 L 的 B 线条件：

1. 先确认 Batch04K B 输出齐全并被 Codex A / Patcher / Governor 接收为 K 批 A/B 输入。
2. 确认 K 的 ClaudeCode screen 已退出、已停止，或至少被明确归档为不再写入。
3. 再启动 Batch04L 的独立 ClaudeCode B，prompt 必须写明 run identity、Batch04L、`2026石景山一模`，避免和 K 的房山输出混线。

不必等待 Batch04K 学生稿或最终交付，因为这些本来仍被全局 gate 阻断；但必须等待 K 的 B 线进程边界清干净，不能让 K、L 两个 ClaudeCode screen 并跑。

## 4. 等级题角度来源的防混规则

本批最大风险是把等级题角度来源当成逐点细则。后续所有角色按以下规则执行：

- `可从……角度`、`任选关键词`、`学科用语 + 合理分析` 是等级题评分结构，不是逐点采分表。
- Q20 不能按五个 atom 各自赋 2 分、不能计入正式频次、不能作为“必背五点”进入学生稿。
- “共同 / 开放 / 包容”是设问关键词，不是三个评分术语；术语必须来自角度中的学科用语。
- “人类命运共同体 / 和平发展合作共赢”只是角度池和升华表达，不是每组关键词答案的必写帽子。
- Q21 中的“中国智慧 / 中国方案 / 大国担当”只作生态环境法典综合等级题的示例表达，不得回流到选必一主链。
- 后续若做学生预览，必须改写为“关键词触发的可用表达积累”，而不是“逐点细则模板”。

## 5. 角色任务

Codex 生产：
- 暂停 Batch04L 主表正式合并，只保留 `candidate_with_guard` 预融合。
- 准备 Batch04L ClaudeCode prompt，但在 Batch04K screen 清理前不启动。
- K 的 B 线清理后，启动 L 的 A/B 复核，重点让 B 判定：Q20 是否只有等级题角度规则、是否存在隐藏逐点细则。

劳动者：
- 不重做整套卷；只复核 Q20 的完整设问、三个关键词、评分参考原文和 page 7/page 10 视觉锚点。
- 复核 Q16-Q19、Q21 的 boundary 处置，尤其 Q21 的中国方案示例不能误升格。

Patcher：
- 先本地核验 `细则.doc` 中 Q20 的原文结构，明确它是等级题规则还是逐点细则。
- 检查五个 atom 的 `boundary_note` 是否都保留“等级题角度来源，不作为逐点细则频次”。
- 若发现某 atom 被写成正式赋分点，退回修正为 guarded 表述积累。

Governor：
- Gate 建议：无 B 对照时最多给 `PASS_FOR_GUARDED_PREVIEW_ONLY`，不得给正式 closure。
- 若 B/Patcher 均确认“官方评分参考等级题，无逐点细则”，可给 `PASS_WITH_GUARD`，允许内部候选表述积累，但学生稿仍 blocked。
- 若 B 找到逐点细则，转入返修：重拆 scoring atoms、重写 merge register、更新 evidence level。
- 若 B 认为该文件只是普通参考答案且无评分规则，降级为 `reference-only / boundary`，不得保留 candidate。

自动化检测者：
- 监控是否仍有 Batch04K screen 活跃；活跃时不得启动 Batch04L ClaudeCode。
- 检查本轮是否误改 fusion/student/delivery；如有非授权变更，立即报 Governor。
- 后续检查 Batch04L 行状态不得出现 `candidate_with_fixes`、`P0_formal_scoring_rule`、`included_final` 等过度放行字样。

## 6. 可并行事项与阻断边界

可以并行：
- Patcher 做 Q20 原文结构核验。
- Governor 准备 guarded gate。
- 自动化检测者监控 K screen 和 L prompt 准备状态。
- Codex 生产预备 Batch04M source locator，但不得抢先改 coverage close 或学生稿。

不能并行越界：
- 不能启动 L 的 ClaudeCode B 与 K 的活跃 screen 并跑。
- 不能把 Q20 写入学生稿。
- 不能把五个 guarded atom 计作正式频次。
- 不能把 Q21 的“中国方案”示例带入选必一主表。
- 不能宣布 Batch04L 最终闭合。

## 7. 下一步最小执行顺序

1. Automation 先确认 Batch04K ClaudeCode screen 是否已真正退出或归档。
2. Patcher/Governor 同步完成 Batch04L guarded 预审。
3. K 的 B 线边界清理后，启动 Batch04L ClaudeCode B。
4. B 输出后做 A/B difference table：重点比对“等级题角度来源”是否保持 guarded。
5. 只有在 Patcher + Governor + A/B 复核均通过后，Batch04L 才能进入 `candidate_with_guard` 闭合；仍不得进入学生最终稿。
