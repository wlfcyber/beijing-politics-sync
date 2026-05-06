# Batch04M Remaining — Conflicts for Codex A

Lane: ClaudeCode B (independent verification)
Coverage: 15 remaining suites

## Conflict Items

### C1 — Evidence-tier 多档分级（结构性，跨四批）

本批共出现 5 种证据等级，与既有 04A-04L 不完全同构：

- **P0_scoring_pdf**（FS25Y, YQ25Y）— 标准 PDF 细则 + 替代规则 + 链式赋分.
- **P0_scoring_docx**（FT24E, SJS25Y, SY25Y）— DOCX 细则 + 采点采意 + 替代项 + 负向条款.
- **P0_scoring_pptx**（FT25E）— PPTX 含正式评分标准说明（**与教研讲座 PPTX 不同 tier**）.
- **P0_scoring_pdf_guarded**（FT24Y）— cap-tier rubric（aspect-count → 段位分），无 per-pt 切分.
- **P0_scoring_docx_guarded**（FT25Y, CP25E）— DOCX 含正式细则但缺模块标签 / 显式负向 / 选必一仅承接 fallback.
- **P0_scoring_pptx_guarded**（CP25E）— PPTX 细则但缺选必一显式标签.
- **P1_reference_answer_only_pptx**（SJS24Y）— 教研讲座 pptx，仅含 reference + 答题模板，**不可促进**.
- **P1_reference_answer_only**（SY24E）— 仅参考答案文本，**不可促进**.

建议 fusion schema 引入：
```
evidence_tier ∈ {
  P0_scoring_pdf, P0_scoring_docx, P0_scoring_pptx,
  P0_scoring_*_guarded (with guard_reasons[]),
  P1_reference_answer_only,
  prompt_only_blocker,
  boundary_only,
  excluded
}
guard_reasons ⊆ {cap_tier_no_per_pt, missing_module_tag, anti_hit_negative_list, dual_coded, fallback_only}
```

### C2 — 2026丰台期末 Q20 LAC 五大工程 prompt vs rubric 缺口
Codex A's prompt 第 90 行说"Codex A found a prompt, but may not have found current scoring for this Q20"。Lane B 独立验证：

- prompt **YES** found — deck `SRC_45c50fff4444` p.64 / L406-424 含完整题面（团结/发展/文明/和平/民心五大工程 + 利益汇合点 + 党的二十大新型国际关系）.
- rubric **NO** — deck p.65 起跳到一道 9 分综合"五年规划"题（与 8 分 LAC 题不匹配）；deck 中 2022 北京卷"四大全球倡议"rubric 是教学 anchor 不是 2026 LAC rubric.
- 配套 paper file `SRC_371641aaa3a7` (107 B) 抽取失败.

**建议 Codex A**：
1. 确认 lane B 判断（rubric 在该 deck 中确实缺失），共同标记 `prompt_only_blocker`.
2. 启动 source hunt：检查是否存在另一份独立的 2026丰台期末 答案/评分 doc/pdf（区教研室原版细则）.
3. 在术语层登记 prompt 中的 9 个候选学科用语（联合国为核心国际体系 / 国际法为基础国际秩序 / 全球发展倡议 / 多边贸易体制 / 全球安全倡议 / 全球文明倡议 / 全人类共同价值 / 新型国际关系 / 利益汇合点 + 中拉命运共同体）作为 placeholder，**不可作为原子在矩阵中赋分**.

### C3 — Source mis-tag: 2024丰台一模 vs 2025丰台一模
`SRC_066dbcf5b765` 与 `SRC_ef312c0ead76` 在 batch04M extraction logs 同时出现于 `2024丰台一模_*` 与 `2025丰台一模_*` 两组前缀，但内容（header/Q20/政策时点）确认为 **2025丰台一模 only**。

- **建议 Codex A SOURCE_LEDGER 修订**：
  - 删除 `2024丰台一模 / SRC_066dbcf5b765` 与 `2024丰台一模 / SRC_ef312c0ead76` 映射.
  - 保留 `2025丰台一模 / SRC_066dbcf5b765` 与 `2025丰台一模 / SRC_ef312c0ead76`.
  - 2024丰台一模 Q20 (供应链共赢链) 的真正 P0 源为 `SRC_04f136a5f8d1`（已抓取，原子已入码 cap-tier guarded）.

### C4 — Reference-only sources 的处置统一规则（2 套受影响）

2024石景山一模 Q19(2) (pptx 教研讲座 + reference) 与 2024顺义二模 Q19(2) (docx 仅参考答案) — 两者都缺正式评分标准说明。

- Lane B 处置：**reference-only → NOT promotable**（依用户硬规则"reference answers cannot become rubrics"）.
- 但术语层信息丰富（4 个选必一术语：国际竞争实质 / 综合国力较量 / 国家利益 / 世界多极化 / HMC / 经济全球化趋势 / 比较优势 / 国际竞争新优势 / 合作共赢）.
- **建议 Codex A**：
  - 同意 lane B 处置：本批 fusion 不为这两套 Q 设原子.
  - 在术语 boundary 层登记 7 条 reference fragments，作为「跨题术语支证」(只供 fusion 验证术语保形，不增权).
  - 是否启动 source hunt 寻找正式 P0 由 Codex A 决定.

### C5 — 2025昌平二模 Q21 admit/reject 决议
题面**未明示**《当代国际政治与经济》或任一模块标签，但 rubric 注 (2) 把"两个市场两种资源 / 加强贸易合作 / 推动经济全球化发展 / 对外开放型经济发展水平" 标记为 cross-material 通用知识点。

Lane B 处置（**guarded admit**）：
- 选必一-exclusive atoms（A01/A04/A05/A06）入选必一主表 _guarded 子库.
- 经济与社会主码 atoms（A02/A07/A08）不入选必一主表，仅 boundary 登记.
- 两码双注 atoms（A03 营商环境 / A02 现代化产业体系）作为 dual_coded 边界条目.

**建议 Codex A**：裁定 admit 决议；如反对 admit，可将 CP25E-Q21 整体落 boundary_only.

### C6 — 2025丰台一模 Q20 hard negative-list 跨题外溢防护
rubric L124：「如学生堆积《当代国际政治与经济》新型国际关系、构建人类命运共同体、推动经济全球化发展等，**不给分**」。

这是本批**唯一**显式硬性负向规则（FT24E Q19 的"经济全球化/国际关系民主化"是软扣分，FT25Y Q20 是硬不给分）。

- **建议 Codex A**：fusion schema 中新增 `negative_atom_HARD` 字段；本 atom 不计分但**强制保留为元数据**，防止跨题误用。
- 跨题对齐时，FT25Y Q20 的负向不应外溢到 FT25E Q20 / SJS25Y Q17(2) / SY25Y Q20 等真正以 HMC/新型国际关系/经济全球化为核心的题。

### C7 — 跨套术语保形分歧（fusion schema 关键）
| 术语家族 | 变体 | 套件 | fusion 处置建议 |
|---|---|---|---|
| 经济全球化方向 | 五字（开放包容普惠平衡共赢）| YQ25Y A02 | entry_a |
| 经济全球化方向 | 三字（开放包容普惠）| SY25Y A4 | entry_b（不互替）|
| 经济全球化方向 | 双件套（普惠包容的）| SJS25Y A03 | entry_c |
| 经济全球化方向 | 亚太语境（更加包容、更可持续，更好惠及）| 04L SJS2026 一模 A03 | entry_d |
| 联合国系族 | 联合国为核心+国际法为基础双件套 | SJS25Y A04 | entry_a |
| 联合国系族 | 联合国宗旨和原则的框架（不可替代单形）| FS25Y A06 | entry_b（同族不同形）|
| 中国方案/智慧/力量 | 中国智慧、中国方案（双件套）| FT24E A2 | entry_a |
| 中国方案/智慧/力量 | 中国方案（独立标语）| SY25Y A4, FT26E prompt | entry_b |
| 中国方案/智慧/力量 | 中国力量（个别参考答案版）| FT24E reference | entry_c（次要变体）|
| 新型国际关系 | 原形（1 分）| FT25E A05 单形 | entry_a |
| 新型国际关系 | 三件套（相互尊重、公平正义、合作共赢）（2 分）| FT25E A05 详写 | entry_b（"具体写出"加分）|
| 多边主义 | 真正的多边主义（"真正的"必拿）| SJS25Y A04 | entry_a |
| 多边主义 | 多边主义（替代/单形）| YQ25Y A05 | entry_b |
| 国际关系民主化 | 主码 | SJS25Y A02 | entry_a |
| 国际关系民主化 | 替代项（替代新型国际关系 1 分）| FT25E A05b | entry_b（替代角色）|
| 义利观 | 正确义利观（"正确"必拿）| FS25Y A08 替代, SY25Y A4 | entry_a |

### C8 — 跨题族登记建议（中国全球治理大族）

延续 04L 的 `cluster_id = china_global_governance_family` 顶层族；本批扩展子族：

- **理论逻辑子族**（FT25E A01-A04）：和平与发展时代主题 + 国家间共同利益 + 平等互利 + 共商共建共享全球治理观.
- **价值意蕴子族**（FT25E A05-A07, YQ25Y A04, SJS25Y A04）：HMC / 新型国际关系 / 真正多边主义 / 联合国为核心.
- **国际竞争-开放子族**（FS25Y chain1, CP25E A01-A05, FT25Y FALLBACK）：国际竞争实质 + 高水平对外开放 + 创新型开放型世界经济 + 经济全球化.
- **大国责任子族**（FT24E, YQ25Y A03, SY25Y A3-4）：负责任大国 / 兼顾合理关切 / 大国担当 / 中国方案.
- **南南/区域合作子族**（FT24E A2-A3）：南南合作 / 区域合作 / 中非命运共同体（FT25E）/ 中拉命运共同体（FT26E placeholder）.
- **小而美子族**（SY25Y）：聚焦发展中国家紧迫需求 / 灵活快速响应 / 改善民生 / 文明互鉴.
- **供应链/产业链子族**（FT24Y aspect, YQ25Y A01, FT26E placeholder）：供应链产业链 / 全球产供链稳定畅通 / 多边贸易体制.
- **义利观子族**（FS25Y A08, SY25Y A3）：正确义利观（独立学科用语）.

**建议 Codex A**：在 fusion 主表中将 sub-cluster 显式标注；学生稿生成阶段可按 sub-cluster 平衡选取角度。

### C9 — Cap-tier rubric vs Per-pt rubric vs Chain rubric 三种结构

本批呈现三种 rubric 结构（fusion 应分别处理）：

1. **Cap-tier**（FT24Y, SJS25Y meta）— 角度数 → 段位分；不可 per-pt.
2. **Per-pt**（FT24E, FT25E, SJS25Y A01-A04, SY25Y, CP25E, YQ25Y, SJS2026-04L）— 1 分/2 分独立计分.
3. **Chain**（FS25Y）— 链式赋分（chain1=4 / chain2=3 / 逻辑=1），起点+不可替代节点+可替代节点+终点共计.

**建议 fusion schema**：
```
rubric_structure ∈ {cap_tier, per_pt, chain, mixed}
chain_meta = {chain_id, chain_total, anchors[], replaceable[], irreplaceable[], terminal}
cap_tier_meta = {n_aspects, aspect_to_score_map, downgrade_rules}
```

## Cross-thread Notes

- 本批所有结论仅写入 `claudecode_lane/`、`04_suite_reports/claudecode_suite_reports/`、`06_conflicts/`（如需）.
- 未触动 Codex A fusion / 学生稿 / 全局 ledger / DECISION_LOG / FINAL_ACCEPTANCE_REPORT.
- C3 (source mis-tag) 与 C2 (2026丰台期末 Q20 blocker) 涉及 SOURCE_LEDGER 修订，建议 Codex A 在 fusion 阶段前裁定.
- C5 (CP25E Q21 admit) 与 C7 (术语保形分歧) 涉及 fusion schema 与族库结构，待 Codex A 决议.
