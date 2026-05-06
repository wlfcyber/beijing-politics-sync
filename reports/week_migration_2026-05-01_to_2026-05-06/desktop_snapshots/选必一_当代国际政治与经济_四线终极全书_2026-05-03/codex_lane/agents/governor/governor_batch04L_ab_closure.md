# Governor A/B Closure - Batch04L 2026石景山一模 Q20

gate_file: `codex_lane/agents/governor/governor_batch04L_ab_closure.md`
gate_role: Codex A Governor
gate_scope: Batch04L 2026石景山一模 Q20 A/B closure
final_gate: PASS_WITH_GUARD

## 读取文件

Codex A prelim:

- `02_extraction/codex_extraction_logs/batch04L_shijingshan2026_manual_evidence_notes.md`
- `fusion/scoring_atom_table_batch04L_shijingshan2026_prelim.csv`
- `fusion/merge_register_batch04L_shijingshan2026_updates.md`
- `04_suite_reports/codex_suite_reports/batch04L_shijingshan2026_suite_report.md`
- `codex_lane/agents/governor/governor_gate_batch04L_shijingshan2026.md`

Patcher / control:

- `codex_lane/agents/patcher/patcher_review_batch04L_shijingshan2026.md`
- `codex_lane/agents/decision_maker/decision_batch04L_shijingshan2026.md`
- `codex_lane/agents/automation_checker/automation_status_batch04L_shijingshan2026.md`

ClaudeCode B:

- `claudecode_lane/progress_batch04L.md`
- `claudecode_lane/batch04L_shijingshan2026_matrix.csv`
- `claudecode_lane/batch04L_shijingshan2026_entries.md`
- `claudecode_lane/batch04L_missing_blockers.md`
- `claudecode_lane/batch04L_conflicts_for_codex.md`
- `04_suite_reports/claudecode_suite_reports/batch04L_shijingshan2026_suite_report.md`
- `claudecode_lane/logs/claudecode_batch04L_20260504_001538.stderr`
- `claudecode_lane/logs/claudecode_batch04L_20260504_001538.debug.log`

Ledger check:

- `SOURCE_LEDGER.csv` Batch04L rows
- `COVERAGE_MATRIX.csv` Batch04L rows

## 总结论

Batch04L 可以作为 `guarded` 候选进入总融合，但只能进入 guarded expression / guarded candidate 层。

不得升级为：

- 逐点评分细则
- 稳定主频
- 闭合频次
- 学生终稿或学生预览正式稿
- Word/PDF/final/FINAL_ACCEPTANCE
- coverage close

核心裁定：

1. Codex A、Patcher、ClaudeCode B 三线均确认 Q20 的来源是官方答案及评分参考，含关键词赋分公式、角度清单、等级表和示例段；不是逐点 rubric。
2. A/B 没有证据源硬冲突。B 线提出的 C1-C9 主要是合并路由、术语保形和 guard 元数据问题，均可通过 `candidate_with_guard` 和下游限制吸收。
3. Q20 的五类可用术语/表达可以进入总融合的 guarded 层，但必须附带“任选两个关键词；每关键词 1 个学科用语 + 合理分析；最高8分；等级表定档”的元数据保护。
4. 2026石景山一模不是已排除的 2026石景山期末；期末排除规则未被误用到一模，也不得用一模 guarded 证据反向恢复期末。

## A/B Closure 裁决

### 1. Evidence tier

裁决：闭合为 guarded source，无硬阻塞。

- Codex A：`P0_scoring_reference_level_guarded`
- ClaudeCode B：`P0_scoring_docx_guarded`

二者名称不同，但实质一致：官方答案及评分参考 + 等级题规则，不是逐点细则。总融合中应统一登记为：

`P0_official_scoring_reference_level_guarded`

不得写为 `P0_formal_scoring_rule`、`P0_formal_point_rubric` 或任何暗示逐点细则的标签。

### 2. 可进总融合的 guarded 候选

允许进入总融合 guarded 层：

- `维护共同利益`：共同关键词下的合作成立逻辑，可与共同利益核心合并。
- `共商共建共享`：必须写成或绑定为 `共商共建共享的全球治理观`，不得作为裸口号进入学生侧。
- `经济全球化（更加包容、更可持续，更好惠及地区全体人民）`：包容关键词下的经济全球化方向表达，可并入经济全球化方向家族的表述积累。
- `和平发展合作共赢`：开放/合作语境下的 guarded 表达，可与开放型区域经济环境、多边主义、世贸组织基本原则、破除贸易壁垒等合理分析配料挂接。
- `人类命运共同体`：仅角度清单内明示、示例未直接对位，允许入总融合 guarded optional expression，不得作为主证锚点。

Codex A 表中的 `贸易和投资自由化便利化 / 区域经济一体化 / 开放型经济格局` 可作为“开放”关键词下的 guarded 机制表达/合理分析积累进入，但不得按独立逐点细则计频；应与 B 线提示的 `开放型区域经济环境 / 世贸组织基本原则 / 破除贸易壁垒 / 多边主义` 做同题配料整理。

### 3. 必须随同进入总融合的 meta guard

ClaudeCode B 拆出的元数据必须随 Batch04L 一起进入总融合记录：

- `scoring_formula_meta`：1 个关键词 = 1 个学科用语 + 合理分析 = 4 分；2 个关键词最高 8 分。
- `question_hard_cap_meta`：题面要求从 `共同 / 开放 / 包容` 中任选两个；写三个关键词不得视为三组独立加分。
- `level_table_meta`：等级表只用于定档，不是独立赋分 atom。
- `boundary_only_expression`：示例段修辞只做合理分析配料，不独立计频。

没有这些 meta guard，Batch04L 不得进入学生侧或主频统计。

### 4. Boundary-only / excluded

继续只作边界或排除：

- Q16：经济与社会，no_xuanbiyi。
- Q17：必修四哲学/文化 + 选必三，no_xuanbiyi。
- Q18：选必二法律与生活，no_xuanbiyi。
- Q19：必修三政治与法治；`共建共治共享社会治理格局` 不得与 Q20 `共商共建共享` 合并。
- Q21：生态环境法典复合等级题；即便出现“中国智慧 / 中国方案”修辞，也不得入选必一主表。
- B 线 ATOM-08/09/10：示例段修辞配料，只能 boundary_only_expression。

## A/B 差异处理

### C1 evidence tier

已闭合：保留 guarded source，禁止升级逐点细则。

### C2 HMC 归族

已闭合：可入人类命运共同体族的 guarded 支证，不作主证锚点；主证让位于逐点细则来源。

### C3 Q19/Q20 撞形

已闭合：必修三 `共建共治共享社会治理格局` 与选必一 `共商共建共享的全球治理观` 分开登记，不合并。

### C4 题面 hard-cap 与赋分公式

已闭合：作为总融合必带元数据；若未来学生稿使用，必须显式绑定两个关键词和对应学科用语。

### C5 示例段修辞

已闭合：示例段修辞不独立赋分，仅作为合理分析配料挂到相应学科用语。

### C6 HMC / 和平发展合作共赢强弱差异

已闭合：`和平发展合作共赢` 有角度清单且示例中有合作共赢展开，guard 强度高于 `人类命运共同体`；`人类命运共同体` 仅保留为角度清单内 optional guarded expression。

### C7 Q21 中国智慧 / 中国方案

已闭合：不进选必一主表，不作为 Batch04L 候选 atom。

### C8 开放型术语变体

已闭合：`开放型区域经济环境`、`开放型经济格局`、`开放型经济新体制` 不互相替换；Batch04L 保留亚太语境。

### C9 中国方案/全球治理族

已闭合为路由建议：Batch04L 可进入 `china_global_governance_family` 的 guarded 支证层，但不得抢逐点细则源的主证位置。

## 下游硬性限制

1. Batch04L 只能在总融合中标为 `candidate_with_guard` 或等价状态。
2. 总融合不得把 Batch04L 写成 `candidate_with_fixes`、`P0_formal_scoring_rule`、`closed_frequency`、`stable_main_frequency`、`included_final`。
3. 学生侧不得写“石景山 Q20 五个必答点”或“五个逐点细则”。
4. 学生侧若未来使用，必须呈现为“从共同/开放/包容中任选两个关键词，每个关键词用一个学科术语加材料分析”的可选路径。
5. HMC、和平发展合作共赢不得作为万能帽；必须绑定亚太合作、共同发展、开放合作、普惠包容等材料关系。
6. `共商共建共享` 下游必须补足全球治理语境，推荐写作 `共商共建共享的全球治理观`。
7. `贸易和投资自由化便利化 / 区域经济一体化` 只能作开放关键词下 guarded 机制表达，不得脱离本题作为独立逐点频次。
8. Q21 的中国智慧、中国方案继续 boundary-only；不得回流至 Q20 或主表。
9. 不得改动学生稿、Word、PDF、final、FINAL_ACCEPTANCE、coverage close。
10. 若未来发现真正逐点细则，必须重拆 Batch04L atom、重定 evidence tier、重跑 Patcher/Governor；不能在本 closure 上直接升级。

## Governor 终裁

final_gate: PASS_WITH_GUARD

允许：Batch04L 2026石景山一模 Q20 作为 guarded 候选进入总融合。

禁止：升级为逐点细则、稳定主频、闭合频次、学生终稿、Word/PDF/final/FINAL_ACCEPTANCE、coverage close。

本次只写 Governor closure 文件；未改学生稿、fusion、coverage/source ledger。
