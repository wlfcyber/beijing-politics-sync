# Batch04D 朝阳扩展 — Conflicts & Rulings Needed for Codex A

generated: 2026-05-03
lane: ClaudeCode production lane B
batch: Batch04D Chaoyang

---

## CONFLICT-D1: 2024朝阳一模 Q21 缺失于候选题目 CSV

**Type:** CSV gap — 需 Codex A 补录
**Severity:** 高（涉及已确认 in_scope 题目漏录）

**事实:**
- `05_coverage/batch04D_chaoyang_candidate_questions.csv` 中 2024朝阳一模 仅有 Q16–Q20 五行，Q21 完全缺失
- 读取 `SRC_4fc81e818683`（细则.pptx）slide 49 明确标注"21题【评分细则】4+5=9分"，第二问5分明确要求运用政治多极化/经济全球化知识
- ClaudeCode B 已在 `batch04D_chaoyang_matrix.csv` 第14行补录该题，分类为 `in_scope`，证据级别 P0

**Codex A 所需操作:**
1. 在 `05_coverage/batch04D_chaoyang_candidate_questions.csv` 补录 2024朝阳一模 Q21 行
2. 在 `COVERAGE_MATRIX.csv` 为该题新增一行（建议以 `batch04D_candidate_with_fixes` 状态入库）
3. 更新 `SOURCE_LEDGER.csv` 确认 SRC_4fc81e818683 的分类权重（已读，P0 pptx）

**已提供信息（ClaudeCode B 矩阵行）:**
```
suite: 2024朝阳一模
question: Q21
classification: in_scope
evidence_level: P0
evidence_source: SRC_4fc81e818683_slide49(21题【评分细则】)
score: 9（全题）/ 5（选必一部分）
bucket_primary: 中国;政治多极化;经济全球化
boundary_notes: 推进高水平对外开放=必修二边界;总体国家安全观=必修三边界
```

---

## CONFLICT-D2: 2024朝阳二模 Q20 —「统筹传统安全和非传统安全」是否计入选必一

**Type:** 边界裁定
**Severity:** 中（影响一个可选角度的归属）

**事实:**
- `SRC_df323259ba77`（2024朝阳二模 细则.pdf，P0）在 Q20 评分细则中将「统筹传统安全和非传统安全」列为1分可选角度，附注"也可得分"
- 该知识点在课程体系中主要归属：
  - 总体国家安全观 → 必修三《政治与法治》或选必三
  - 但传统/非传统安全分类框架在选必一中有独立表述（第四单元 国际安全）
- ClaudeCode B 矩阵已标注 `统筹传统安全非传统安全=1分可选项`，未计入主链条目，但在 entries.md 中保留为表述积累说明

**Codex A 所需操作:**
裁定「统筹传统安全和非传统安全」在本题（全球气候治理背景）中是否：
- A. 可以作为选必一第四单元独立术语计入，标注为可选（推荐：若认定在选必一有明确对应章节）
- B. 归属必修三/选必三边界，从本题选必一条目中删除（若认定主归属不在选必一）
- C. 保持当前状态（entries.md 中仅作表述积累，不纳入主核心点列表）

**当前 ClaudeCode B 处理:** 在条目正文中标注为"可选1分"，列入慎用提醒，未纳入核心点主链。

---

## CONFLICT-D3: 2025朝阳期末 Q21 证据级别裁定

**Type:** 证据级别裁定
**Severity:** 中（影响题目在最终交付物中的证据标注）

**事实:**
- 主细则 `SRC_49b23fecab97`（细则.pdf）文字提取为空白，P0 正式细则来源未找到
- P2 来源已确认：`2025朝阳期末/其他材料/朝阳高三期末2025.pptx` (非 CSV 登记来源)，通过 python-pptx 提取 slide 32-34，含逐条评分点和分值分布（总分8分，分5大维度，每维度评分词列表明确）
- 该 PPTX 属于"其他材料"目录，非细则/补充材料目录；证据规程下应归 P2（讲评材料含评分结构）

**Codex A 所需操作:**
1. 确认 P2 来源（朝阳高三期末2025.pptx）是否满足本题入库门槛
2. 若接受 P2，`COVERAGE_MATRIX.csv` 将该行标记为 `batch04D_candidate_with_fixes` 并注明 evidence_level=P2
3. 若要求 P0，则该题降级为 `missing_scoring_source` 待视觉渲染结果

**ClaudeCode B 当前处理:** 在矩阵中标注 P2，entries.md 中完整写入 P2 来源条目，条目页脚注明"证据级别 P2，主细则.pdf 空白，Codex A 需裁定最终接受级别"。

---

## CONFLICT-D4: 2025朝阳期末 Q21 —「推进高水平对外开放」评分细则中出现

**Type:** 边界确认
**Severity:** 低（已在 ClaudeCode B 处理中排除，但需 Codex A 知情）

**事实:**
- P2 PPTX slide 34 明确将「推进高水平对外开放」列为④营造良好外部经济环境维度的评分点之一
- 该词同时是必修二《经济与社会》边界词；本批次延续前序批次一贯处理：不纳入选必一主链
- PPTX 同一维度内「推动经济全球化朝着更加开放、包容、普惠、平衡、共赢的方向发展」已入库作为核心词

**Codex A 所需操作:**
确认「推进高水平对外开放」边界处理是否与前序批次（Batch01、Batch04A等）保持一致（均排除）。若一致，无需额外操作；若前序批次有过裁定变化，需同步本题处理。

---

## CONFLICT-D5: 2025朝阳期末 Q21 —「正确义利观」与「文化自信」归属

**Type:** 边界裁定
**Severity:** 低（正确义利观可入选必一；文化自信归选必三）

**事实:**
- P2 PPTX slide 34 将「正确义利观」和「文化自信」均列于⑤营造良好外部文化舆论环境维度
- 「正确义利观」：在选必一《当代国际政治与经济》第五单元（中国外交）有明确表述，可计入
- 「文化自信」：主归属选必三《文化传承与文化创新》，在选必一语境中属边界词，不计入主链

**Codex A 所需操作:**
1. 确认「正确义利观」在本批次是否已在前序批次（Batch04B/C）有入库先例（西城/东城题目）
2. 若有先例，本题「正确义利观」应与先例保持一致处理（ClaudeCode B 已纳入条目）
3. 确认「文化自信/讲好中国故事」边界排除与选必三一贯处理一致，写入模块边界记录
