# Suite Report — Batch04L · 2026石景山一模

## Header
- Run: `选必一_当代国际政治与经济_四线终极全书_2026-05-03`
- Lane: ClaudeCode B
- Batch: 04L
- Suite: 2026石景山一模（北京·石景山区 2025-2026 学年高三统一练习一模；区分于已排除的 2026石景山期末）
- Primary question: Q20（8 分，等级赋分关键词解读题）
- Source files:
  - DOC: `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026石景山一模/细则/细则.doc`
  - PDF: `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026石景山一模/试卷/试卷.pdf`
- Evidence tier: **P0_scoring_docx_guarded**（无逐点细则；含官方学科用语清单 + 4 级等级表 + 3 段示例）

## Suite Composition

| Q | 模块 | 处置 |
|---|---|---|
| Q1–Q15 | 选择题（45 分；跨模块）| 非 Xuanbiyi 主体，本批跳过 |
| Q16 | 经济与社会（必修二，8 分）| **excluded** |
| Q17 | 哲学（必修四）+ 创新思维（选必三，14 分）| **excluded** |
| Q18 | 法律与生活（选必二，8 分）| **excluded** |
| Q19 | 政治与法治（必修三，8 分）| **excluded**（注意「共建共治共享社会治理格局」≠ 选必一「共商共建共享」）|
| **Q20** | **当代国际政治与经济**（选必一，8 分）| **candidate_for_fusion_guarded**（主目标）|
| Q21 | 复合（必修一/三/四 + 选必三，9 分）| **excluded**（即便含「中国智慧、中国方案」修辞按 prompt 不提升）|

## Q20 设问全文
> 我们可以从三个关键词"共同""开放""包容"，读懂这一推动亚太合作再出发的中国倡议。结合材料，运用《当代国际政治与经济》知识，任选两个关键词，说明中国倡议如何助推亚太合作。（8 分）

## Q20 赋分规则与可选角度（DOC 原文）
- 赋分公式："从1个'关键词'出发，使用1个学科用语+合理分析，得4分；从2个'关键词'出发……最高8分。"
- 学科用语清单（5 选 N）：共商共建共享 / 人类命运共同体 / 经济全球化 / 和平发展合作共赢 / 维护共同利益。
- 等级表：水平 4 (7-8) / 水平 3 (4-6) / 水平 2 (1-3) / 水平 1 (0)。
- 示例三段（共同 / 开放 / 包容），各举 1 种参考答法。

## 原子清单（11 条）

| atom_id | 性质 | 术语 | promotion |
|---|---|---|---|
| ATOM-01 | 学科用语-共同维度 | 共商共建共享 | candidate_for_fusion_guarded |
| ATOM-02 | 学科用语-全维度通用（示例未对位）| 人类命运共同体 | candidate_for_fusion_guarded |
| ATOM-03 | 学科用语-包容维度 | 经济全球化（更加包容、更可持续，更好惠及全体人民）| candidate_for_fusion_guarded |
| ATOM-04 | 学科用语-开放维度 | 和平发展合作共赢（多边主义/开放型区域经济环境/世贸组织基本原则/破除贸易壁垒/深化合作共赢配料链）| candidate_for_fusion_guarded |
| ATOM-05 | 学科用语-共同维度落点 | 维护共同利益 | candidate_for_fusion_guarded |
| ATOM-06 | 赋分公式元数据 | 1 关键词 = 4 分；2 关键词 = 8 cap | scoring_formula_meta |
| ATOM-07 | 等级表元数据 | 4 级等级表 7-8/4-6/1-3/0 | level_table_meta |
| ATOM-08 | boundary 共同示例修辞 | 共同维护/共同推进/共享繁荣 | boundary_only_expression |
| ATOM-09 | boundary 开放示例修辞链 | 多边主义/开放型区域经济环境/世贸组织基本原则/破除贸易壁垒 | boundary_only_expression |
| ATOM-10 | boundary 包容示例修辞链 | 解决发展不平衡问题/维护发展中国家正当权益 | boundary_only_expression |
| ATOM-11 | 题面 hard-cap 元数据 | 共同/开放/包容（任选 2）| question_hard_cap_meta |

## Promoted Guarded Candidates
全部 5 个学科用语原子（ATOM-01..05）均落 `candidate_for_fusion_guarded`：
- 共商共建共享、维护共同利益、经济全球化（含包容后缀）、和平发展合作共赢 → 示例段直接对位，guarded 信心相对强；
- 人类命运共同体 → 仅清单内、示例未对位，guarded 信心相对弱（需 Codex A 二次裁定）。

## Boundary-only Questions / Expressions
- ATOM-08/-09/-10 → 示例段修辞配料，承担"合理分析"配料而非独立学科用语。
- ATOM-09「开放型区域经济环境」需与中央"开放型经济格局"/"开放型经济新体制"区分跨语境术语形。

## Exclusions
- Q16/Q17/Q18/Q19/Q21 全部模块外排除。
- Q21「中国智慧、中国方案」按 prompt 第 58 行硬指令，不得提升至选必一主表（即便存在也属修辞，赋分槽不在选必一）。

## Source-grade Cautions
1. **整体 _guarded**：源未给逐点细则；不可与房山 04K P0 逐点 docx 同 tier 处置。
2. **赋分公式 + 题面 hard-cap 双 cap**：每关键词 4 分 × 任选 2 = 8 上限；写 3 个不加分。
3. **学科用语清单 5 选 N + 示例段三段对位**：示例非封闭分点，5 个学科用语任组合 2 个可达 8 分。
4. **术语保形**（不可压缩）：
   - 共商共建共享 / 人类命运共同体 / 和平发展合作共赢（9 字原形）/ 维护共同利益（动词形必拿）/ 开放型区域经济环境（亚太语境形）/ 世贸组织基本原则 / 维护发展中国家正当权益。
5. **跨题撞形警示**：Q19 必修三「共建共治共享社会治理格局」 ≠ Q20 选必一「共商共建共享」。
6. **Q21 修辞越界禁令**：即便 doc 表格补抽到「中国智慧、中国方案」字样，也不得入选必一矩阵。

## Blockers
- 无硬阻塞。详见 `claudecode_lane/batch04L_missing_blockers.md` 软隙记录（G1–G5：整批 _guarded、ATOM-02 弱对位、Q21 doc 表格抽取限制、Q19/Q20 撞形、开放型术语跨语境）。

## Files Written
- `claudecode_lane/progress_batch04L.md`
- `claudecode_lane/batch04L_shijingshan2026_matrix.csv`
- `claudecode_lane/batch04L_shijingshan2026_entries.md`
- `claudecode_lane/batch04L_missing_blockers.md`
- `claudecode_lane/batch04L_conflicts_for_codex.md`
- `04_suite_reports/claudecode_suite_reports/batch04L_shijingshan2026_suite_report.md`（本文件）

## Cross-thread Discipline Statement
仅在 `claudecode_lane/`、`04_suite_reports/claudecode_suite_reports/` 写入；未触碰 Codex A fusion / 学生稿 / delivery / 全局控制台 / SOURCE_LEDGER / RUN_MANIFEST / 06_conflicts 既有条目。
