# Batch04M Remaining — Missing & Blockers

Lane: ClaudeCode B
Coverage: 15 remaining suites
Date logical anchor: 2026-05-04

## Hard Blockers

### B1 — 2026丰台期末 Q20 (LAC 五大工程) rubric absent
- **Source state**: deck `SRC_45c50fff4444` (`/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026丰台期末/细则/细则.pdf`) carries the LAC "五大工程" Q20 prompt **verbatim** at p.64 / extracted-text L406–424. Companion paper file `SRC_371641aaa3a7` extracted only 107 bytes (failed extraction).
- **Gap**: Pages immediately following the LAC Q20 prompt (p.65 onward) contain a **different** 9-pt question (五年规划 / 综合 — "是什么/为什么/如何做" + 党的领导/制度优势/全过程人民民主), confirmed by sample answer card `水平四：9 分` at L443. The deck is a 区期末试卷分析 (district exam-analysis), interleaving multiple years' anchors and target-year questions. The LAC Q20 rubric is **not in this deck**.
- **Disposition**: `prompt_only_blocker`. **Do NOT promote.** Mark for follow-up source hunt (a separate 期末 答案/评分 PDF/Word may exist outside `2026各区期末和期中/2026丰台期末/细则/`).
- **Inferred terms (placeholder, NOT promotable)**: 联合国为核心的国际体系 + 国际法为基础的国际秩序; 全球发展倡议; 多边贸易体制; 全球安全倡议; 全球文明倡议; 全人类共同价值; 新型国际关系; 利益汇合点; 中拉命运共同体.

### B2 — 2024丰台一模 source mis-tag (cross-batch hygiene)
- **State**: `batch04M_text_2024丰台一模_SRC_066dbcf5b765.txt` and `..._SRC_ef312c0ead76.txt` are **mis-tagged**. Content header reads "2025.3" / "2025 北京丰台高三一模 政治 2025.03"; Q20 references 《北京市外商投资条例》 (a 2025-era policy). These two SRCs are **2025丰台一模 only**.
- The genuine 2024丰台一模 P0 scoring is `SRC_04f136a5f8d1` (correctly named; 供应链共赢链 Q20).
- **Disposition**: 2024丰台一模 Q20 (供应链) processing succeeded via `SRC_04f136a5f8d1`. The duplicate 2024-tagged 2025 sources can be ignored.
- **Recommendation to Codex A SOURCE_LEDGER hygiene**: drop the `2024丰台一模 / 066dbcf5b765` and `2024丰台一模 / ef312c0ead76` mappings; keep only their `2025丰台一模 / *` counterparts.

## Soft Gaps (fusion may need Codex A second pass)

### G1 — 2024丰台一模 Q20 cap-tier rubric (no per-pt 切分)
- 4 aspect bundles (基础设施/金融创新/平台贸易投资自由化便利化/数字化绿色低碳) + 1 closure 修辞.
- Rubric scores by aspect-count: 3→6-7, 2→4-5, 1→2-3. **No 1-pt atomization possible.**
- Atoms落 `_guarded` aspect-bundles, structurally parallel to 2026石景山一模 (04L) 等级赋分 pattern.
- Codex A may want to label these as `aspect_bundle_atom` rather than `point_atom` to distinguish from 04K-style P0 docx.

### G2 — 2024石景山一模 Q19(2) reference-only (pptx slide deck)
- `SRC_f887d1b620c6` 是教研讲座 PPTX，含答案 + 答题模板图，**无评分标准说明 / 等级 / 必采点 / 分值切分**.
- 3 reference fragments listed as boundary, **NOT promotable** per project rule.
- Codex A may search for an alternative P0 source (区教研室单独细则文件) if available; otherwise this Q remains at boundary.

### G3 — 2024顺义二模 reference-only
- `SRC_0eb74816f25f` 仅 5832 字 参考答案，无评分标准说明 / 分值切分。
- Q19(2) 4 个选必一 reference fragments listed as boundary, **NOT promotable**. Q18 选必一 thread weak.
- Codex A may search for 教研室原始评分细则 PDF/PPTX；当前批次冻结。

### G4 — 2025丰台一模 Q20 hard negative-list
- 主码 4×2pt（便利投资/便利贸易/吸引人才/优惠政策）属 **经济与社会 模块**；本 lane 仅承接选必一 fallback。
- 题面双模块标签 + rubric 显式负向：堆积新型国际关系/HMC/经济全球化发展者**不给分**.
- Codex A 应在 fusion 跨题对齐中显式登记此负向规则，防止 fusion 把本 Q 的 2 个市场两种资源 fallback 与 04L/SJS25Y 等正向 atoms 混合误增权。

### G5 — 2025昌平二模 Q21 缺模块标签
- 题面只云"结合材料,说明上述举措对我国建设更高水平的开放型经济具有什么重要意义"，**未明示** 选必一 / 经济与社会 / 哲学等任何模块。
- Rubric 注 (2) 把 国内国际两个市场两种资源/加强贸易合作/推动经济全球化发展/对外开放型经济发展水平 标记为"**放到哪个材料都可以给分**"的开放知识点 → 选必一-exclusive 入码合规但 **guarded**.
- Codex A 应裁定：是否提升至选必一主表，或仅作为 dual-coded 经济与社会+选必一 双注。

### G6 — 跨套「经济全球化方向」语形分歧
- 4 个变体：
  - 延庆 2025 一模 Q20(2)：开放、包容、普惠、平衡、共赢（**五字头**）
  - 顺义 2025 一模 Q20 A4：开放、包容、普惠（**三字头**）
  - 石景山 2025 一模 Q17(2) A03：普惠包容的经济全球化（双件套合并）
  - 石景山 2026 一模 (04L) Q20 A03：更加包容、更可持续，更好惠及全体人民（亚太语境特化）
- Codex A 应在术语对齐表登记**不可互替**，分四 entry。

### G7 — 「联合国为核心 + 国际法为基础」 vs 「联合国宗旨和原则的框架」
- 2025石景山 Q17(2) A04：以联合国为核心的国际体系 + 以国际法为基础的国际秩序（双件套）
- 2025房山 Q18(2) A06：在联合国宗旨和原则的框架下（不可替代单形）
- Codex A 应在 UN 族下登记为**同族不同形**；fusion 不可互替，但可在术语保形规则中并列。

### G8 — 「中国方案 / 中国智慧」 vs 「中国力量」 vs 「义利观」
- 2024丰台二模 Q19 A2 细则版：贡献**中国智慧、中国方案**（参考答案版："中国智慧、中国力量" → 细则把"力量"替换为"方案"）。
- 2025顺义一模 Q20 A4：为重构公正合理的国际政治经济秩序提供**中国方案**.
- 2025房山 Q18(2) A08 替代项：**正确义利观** ↔ 加强国际交流合作.
- Codex A 应区分：
  - 「中国方案」（修辞标语，跨题广用）
  - 「中国智慧、中国方案」（双件套并列）
  - 「中国力量」（个别参考答案版本）
  - 「正确义利观」（独立学科用语，可作为国际交流合作/大国担当族替代项）

## Information Sufficient for Promotion

- Suites 2 / 3 / 7 / 8 / 9 / 11 / 12（2024丰台一模 Q20 / 2024丰台二模 Q19 / 2025丰台期末 Q20 / 2025延庆一模 Q20(2) / 2025房山一模 Q18(2) / 2025石景山一模 Q17(2) / 2025顺义一模 Q20）已抓全题面 + 评分标准说明 + 替代规则 + 负向引导（如有），原子可入矩阵；少数 _guarded 标签源自 cap-tier rubric 或缺模块标签。
- Suite 10（2025昌平二模 Q21）guarded 入码 — 仅 4 个选必一-exclusive 原子，4 个 boundary 经济与社会主码 不入选必一主表。
- Suite 6（2025丰台一模 Q20）仅 fallback 入选必一矩阵 + negative-list 显式登记，不入选必一主码原子.
- Suites 1 / 14 / 15（2026海淀期末 / 2024模块分类汇编 / 2026石景山期末）整体 boundary / excluded — 不进任何原子.
- Suites 4 / 5（2024石景山一模 Q19(2) / 2024顺义二模 Q19(2)）reference-only — 不进原子，仅术语层 boundary 登记.

## Post-Batch Source Hunts (可选)

| Suite | Hunt 目标 | 期望源 |
|---|---|---|
| 2026丰台期末 Q20 (LAC 五大工程) | 寻找独立 P0 评分细则 | 区教研室 docx / 各校阅卷参考 |
| 2024石景山一模 Q19(2) | 寻找正式 P0 (非教研讲座 pptx) | 区阅卷标准 doc/pdf |
| 2024顺义二模 Q19(2) | 寻找带分值切分的细则 | 区阅卷参考 docx |
| 2024丰台一模 Q20 | 已找到 P0_pdf_guarded — 无需再 hunt | — |
