# Decision Maker Phase 03 Batch 02 Plan

Run: 选必一《当代国际政治与经济》四线终极全书 2026-05-03

Role: Codex production lane A / 决策者

Status: `decision_only_not_source_processing`

## Phase 3 下一步瓶颈

当前 Phase 3 的真实瓶颈不是继续扩写学生文档，而是 `B-only closed candidates` 尚未被 Codex A 本轮亲自回源复核。Batch 01 已形成 `candidate_with_fixes`，但 Governor 明确禁止直接进入稳定主表、学生终稿、Word/PDF、coverage closed 或 FINAL_ACCEPTANCE。

下一步应先解除三个门：

1. B-only 四题源证据门：2026朝阳一模 Q20、2026顺义一模 Q20、2025海淀二模 Q21、2025海淀期末 Q22 必须由 Codex A 劳动者逐题复核。
2. Batch 01 修补门：Q17 模块边界、source ledger 回链、2025海淀期中 Q21(2) 图片备注分类仍需在融合层显式处理。
3. section_batch 门：只有 Batch 02 四题至少形成 `confirmed_source / P2_keep_labeled / blocked_no_scoring_source` 的明确状态，并经补丁者和 Governor 复核后，才允许生成用于 GPT/Claude 评审的 `section_batch` 草案。

## Batch 02 劳动者复核顺序

### 1. 2025海淀二模 Q21

优先级：P0 最高，先做。

理由：

- ClaudeCode B 标为正式评分细则 + 评标实录，若 Codex A 复核成立，将立即补强当前最薄的 `联合国` 桶。
- 它会影响多个已建 merge group：`符合《联合国宪章》宗旨和原则`、`推动构建人类命运共同体`、`贡献中国智慧、中国方案`、中国的联合国身份与国际格局地位。
- 选必一 skill 样例本身把该题作为高价值样本，适合先用来校准 Batch 02 的证据格式。

劳动者只需复核：完整设问、评分材料类型、评分结构是否分为“中国需要联合国 / 联合国需要中国”、每个点的分值或任答关系、是否有评标实录可作补充说明。

### 2. 2026朝阳一模 Q20

优先级：P0 第二。

理由：

- ClaudeCode B 和技能样例均指向正式细则，且该题含必答点：`当前国际竞争的实质是以经济和科技实力为基础的综合国力较量` 与 `坚持创新驱动发展战略`。
- 它会补强 `理论` 桶，也会影响 `经济全球化开放、包容、普惠、平衡、共赢方向`、`两个市场两种资源`、`中国智慧/正能量` 等后续合并。
- 该题是判断“能力来源型设问”如何写材料触发和答案句的硬样本，优先于同类表述积累。

劳动者只需复核：必答/选答结构、必答点是否捆绑计分、经济全球化方向是否为细则原词、是否出现人类命运共同体或中国智慧中国方案类可合并点。

### 3. 2026顺义一模 Q20

优先级：P0 第三。

理由：

- 正式评标材料若复核成立，将补强 `共同利益是国家合作的基础`，并校准 `正确义利观` 与 `共同利益` 的 non-merge 边界。
- 它与 2026朝阳一模 Q20 共享 `推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展` 候选，应在朝阳一模之后做对照复核，避免同核心误拆或误合并。
- 它会补强“深层逻辑型设问”的材料触发模板。

劳动者只需复核：正式评标 PPT 是否可读、国际政治角度和国际经济角度是否分层、`共同利益` 是否必答、`正确义利观 / 人类命运共同体 / 经济全球化方向` 各自的证据位置。

### 4. 2025海淀期末 Q22

优先级：第四，低于前三个 P0 候选。

理由：

- ClaudeCode B 标为 P2 教师研修 PPT/可选知识点，正式评标未找到。它可补入，但必须显式保留 P2 标签。
- 该题主要给 `人类命运共同体`、`中国智慧中国方案` 增加综合短文场景变体，不应抢在 P0 正式细则题前面。
- 若复核发现只有“可选用知识”而无评分点，应保留为 `P2_keep_labeled` 或 `reference_for_expression_only`，不得提高为 P0 频次。

劳动者只需复核：完整设问、PPT 页码、是否明确列出选必一、人类命运共同体和中国智慧中国方案是否是可用知识还是评分点、是否存在正式评标缺口。

## 叫醒策略

1. 先叫醒劳动者：按上述顺序做 `worker_batch02_source_recheck`，每题输出状态，不写学生化正文。
2. 劳动者完成 2025海淀二模 Q21 和 2026朝阳一模 Q20 后，立即叫醒补丁者做中段扫描，重点查 UN 桶合并、国际竞争实质与创新驱动是否被拆错、经济全球化方向是否保留最高信息量原词。
3. 劳动者完成 2026顺义一模 Q20 后，再叫醒补丁者做 non-merge 扫描：`正确义利观` 不得并入 `共同利益`，`和平与发展时代主题` 不得并入中国外交宗旨。
4. 劳动者完成 2025海淀期末 Q22 后，叫醒 Governor 做 Batch 02 gate。Governor 不需要等 Opus 或 GPT 捕获。
5. 自动化检测者只在 Batch 02 文件写齐后启动，核对 source notes、ledger 回链、scoring atom 追加表、merge register 更新、coverage 状态是否一致。
6. ClaudeCode B 暂不重启。只有当 Codex A 连续两条路线找不到 B 所称 P0 正式细则时，才以“定位源文件/页码”为目标重启或新开 ClaudeCode 定向检查。

## section_batch 裁决建议

当前裁决：`DO_NOT_ENTER_SECTION_BATCH_YET`。

条件放行：完成以下条件后，允许生成 `section_batch_draft_for_external_review`，但仍不得生成学生终稿、Word/PDF、coverage closed 或 FINAL_ACCEPTANCE PASS。

1. 四题都有明确 Codex A 状态：`confirmed_source`、`P2_keep_labeled` 或 `blocked_no_scoring_source`。
2. 前三题 P0 候选中，凡进入主链的点均完成 source notes 和 ledger 回链。
3. 2025海淀期末 Q22 即使只保留 P2，也必须在 section_batch 中显式标注证据层级，不参与 P0 频次膨胀。
4. Patcher 完成 Batch 02 merge/non-merge 扫描。
5. Governor 对 Batch 02 至少给出 `PASS_WITH_FIXES`。
6. Batch 01 遗留修补项至少在 fusion 层标注：Q17 模块边界、source ledger 回链缺口、2025海淀期中 Q21(2) 图片备注分类。

## 不应阻塞 Batch 02 的事项

- Claude Opus 响应未捕获，不阻塞 Batch 02 源复核。
- GPT-5.5 Pro 评审不阻塞源证据闭环；它只在 section_batch 草案生成后介入内容压力测试。
- 2025海淀期末 Q22 找不到 P0 正式评标，不阻塞前三个 P0 候选进入 Batch 02 融合；它按 P2 或 blocked 状态处理。
- 频次终表、Word/PDF、最终学生版措辞、Confucius 学会性验收均不在 Batch 02 决策范围内。

## 下一轮决策者只看

- 四题是否已按顺序复核。
- 哪些点从 B-only 升为 Codex-A-locked。
- 哪些点降级为 P2、reference-only 或 blocked。
- Merge register 是否需要新增 `共同利益`、`中国的联合国地位`、`联合国三大支柱/作用`、`经济全球化开放包容普惠平衡共赢方向` 等组。
- 是否满足 `section_batch_draft_for_external_review` 的条件放行门。
