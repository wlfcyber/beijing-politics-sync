# Governor Gate - Batch04M Remaining Prelim

gate_file: `codex_lane/agents/governor/governor_gate_batch04M_remaining.md`
gate_role: Codex A Governor
gate_scope: Batch04M remaining prelim 是否可进入候选融合门禁
final_gate: PASS_WITH_GUARD

## 读取文件

- `05_coverage/batch04M_remaining_candidates.csv`
- `05_coverage/batch04M_remaining_deep_scan_sources.csv`
- `05_coverage/batch04M_remaining_suite_term_hits.csv`
- `02_extraction/codex_extraction_logs/batch04M_remaining_manual_evidence_notes.md`
- `02_extraction/codex_extraction_logs/batch04M_remaining_deep_source_scan.md`
- `02_extraction/codex_extraction_logs/batch04M_remaining_suite_term_hits.md`
- `fusion/scoring_atom_table_batch04M_remaining_prelim.csv`
- `fusion/merge_register_batch04M_remaining_updates.md`
- `codex_lane/agents/worker/worker_batch04M_remaining_triage.md`
- `04_suite_reports/codex_suite_reports/batch04M_remaining_suite_report.md`
- `COVERAGE_MATRIX.csv` Batch04M rows
- `SOURCE_LEDGER.csv` Batch04M rows
- `current-user-requirements.md`
- `xuanbiyi-term-protocol.md`

## 总结论

Batch04M remaining prelim 可以进入候选融合门禁，但只能按分层状态推进：

- 正式评分细则/评标/明确逐点结构：可作为 `candidate_with_fixes` 进入候选融合。
- guarded 来源：只可作为 `candidate_with_guard` / 表述积累 / 低等级支证，不能升级为主频、稳定逐点细则或闭合频次。
- 2026丰台期末 Q20：必须保持 `blocked_prompt_only`，不得 promotion。
- 2026石景山期末：继续 `excluded`，不得恢复。

本轮不是整批 BLOCK，因为多数正式评分来源可进入候选融合；但由于本批同时含 guarded 来源、prompt-only blocker 和 excluded 套卷，结论不能给无条件 PASS。

## 可进入候选融合的正式评分组

以下题目可进入 `candidate_with_fixes`，但仍需后续 Patcher / A-B closure / 总融合复核：

- 2024丰台二模 Q19：`P0_formal_scoring_docx`，三角度各2分；可入负责任大国、南南合作、中国智慧中国方案、人类命运共同体相关表达。
- 2025丰台一模 Q20：`P0_formal_scoring_docx`，便利投资、便利贸易、吸引人才、优惠政策四个2分点；宏观双循环/两个市场两种资源只作兜底边界。
- 2025丰台期末 Q20：`P0_formal_scoring_pptx`，中非理论逻辑4分 + 价值意蕴4分；逐点结构清楚。
- 2025延庆一模 Q20(2)：`P0_formal_scoring_docx`，时代主题、经济全球化方向、多极化/HMC四组清楚。
- 2025房山一模 Q18(2)：`P0_formal_scoring_pdf`，两条主链 + 逻辑分；联合国框架、开放型世界经济等不可替代项须保留。
- 2025石景山一模 Q17(2)：`P0_formal_scoring_doc`，四个2分中国主张；可入全球治理观、国际关系民主化、普惠包容经济全球化、真正多边主义/联合国核心。
- 2025顺义一模 Q20：`P0_formal_scoring_docx`，四组2分；理念/世界贡献为任意点上限结构，不得堆满当必答。

这些行允许进入候选融合，不允许进入学生终稿、Word/PDF、final、FINAL_ACCEPTANCE 或 coverage close。

## 只准 guarded 进入的组

以下题目可以作为 `candidate_with_guard` 进入表述积累或低等级支证，不得升级主频：

- 2024丰台一模 Q20：`P0_scoring_docx_level_aspects_guarded`。来源是四方面等级说明/答案提示，不是固定逐点 rubric；供应链、贸易投资自由化便利化、经济全球化表达可积累，但不得按固定2分逐点计频。
- 2024石景山一模 Q19(2)：`P1_pptx_or_answer_reference_guarded`。有答案链但未见逐点评分细则；只作经济全球化、比较优势、资源配置、合作共赢表达积累。
- 2024顺义二模 Q19(2)：`P0_answer_only_mixed_module_guarded`。混合模块题，只收国际竞争、国家利益、世界多极化、人类命运共同体等选必一子链；不得把经济与社会/政治与法治内容带入主链。
- 2025昌平二模 Q21：`P0_formal_scoring_pptx_no_explicit_book_guard`。未显式限定选必一，虽含两个市场两种资源、全球经济治理、开放包容全球经济格局等可用表达，但只能 guarded 进入经济全球化/中国影响相关表述积累。

这些 guarded 行不得被写为 `P0_formal_scoring_rule`、`stable_main_frequency`、`closed_frequency`、`candidate_with_fixes` 或学生必背主频。

## 必须 BLOCK / Boundary / Excluded

### 2026丰台期末 Q20

裁决：BLOCK。

当前只找到题面与材料，未找到本题正式评分细则。即使 `SOURCE_LEDGER.csv` 的 source_type 有 `P0_candidate_scoring` 宽标签，也不能据此升级；应以 manual notes、candidate 表和 coverage 的 `prompt_found_current_scoring_missing` 为准。

下游必须保持：

- `blocked_prompt_only`
- 不 promotion
- 不进入 fusion atoms / merge register 主候选
- 不进入学生稿
- 等 ClaudeCode B source challenge 或后续找到正式评分细则后重审

### 2026石景山期末

裁决：EXCLUDED。

用户已确认全模块排除；本轮不得以任何 Batch04M 发现恢复或补入。继续保持：

- `excluded`
- `user_confirmed_excluded_no_scoring`
- 不处理、不补入、不作为候选融合来源

### 2026海淀期末

裁决：boundary only。

本轮复扫未发现选必一主观题；只作源穷尽边界，不补入主表。

### 2024模块分类汇编

裁决：source bundle boundary。

模块分类汇编不是 P0 评分细则源，不作为新题源 promotion。

## 关键风险复查

### 1. 参考答案冒充细则

当前 fusion 表对 guarded 来源基本保留了边界：`level_aspects_not_fixed_point_rubric`、`pptx_answer_no_point_rubric`、`mixed_module_answer_only`、`no_explicit_book_but_xuanbiyi_scoring_terms` 等标签存在。Governor 要求下游继续以这些边界为准。

尤其注意：2024石景山一模 Q19(2)、2024顺义二模 Q19(2) 不得因 source ledger 宽标 `P0_candidate_scoring` 被提升为正式逐点细则。

### 2. guarded 误升主频

未发现当前 fusion 表直接把 guarded 行标为主频；但下游必须防止：

- 2024丰台一模 Q20 的供应链四链变成固定逐点2分。
- 2024石景山一模 Q19(2) 的答案链变成 P0 逐点。
- 2024顺义二模 Q19(2) 的混合模块答案变成选必一全题主链。
- 2025昌平二模 Q21 因出现两个市场两种资源/全球经济治理而被无条件计主频。

### 3. 同类项抽象

merge register 当前保留了高信息量原则：完整五词方向不被短语替换；共商共建共享必须继承为全球治理观；完整新型国际关系不被裸词替代；HMC 不作万能帽。该方向可通过。

后续总融合必须继续保留：

- `开放、包容、普惠、平衡、共赢` 与 `开放包容普惠`、`普惠包容` 的层级差异。
- `共商共建共享的全球治理观` 与国内治理/社会治理词的边界。
- `人类命运共同体` 的具体 scoring slot 或 bounded expression role。

### 4. 学生稿与交付污染

本批 manual notes、worker triage、merge register 均显示未触碰学生文档。当前门禁继续阻断：

- 学生稿 / 学生预览正式稿
- Word / PDF
- final / FINAL_ACCEPTANCE
- coverage close

## 下游硬性限制

1. Batch04M 只能进入候选融合门禁，不得宣称最终闭合。
2. `candidate_with_fixes` 组可入候选融合，但仍需 Patcher、A/B closure、总融合复核。
3. `candidate_with_guard` 组只能 guarded 进入；不得升级主频或稳定逐点细则。
4. 2026丰台期末 Q20 必须保持 `blocked_prompt_only`，除非找到当前题正式评分细则并重跑 Governor。
5. 2026石景山期末必须保持 `excluded`，不得因一模或其他石景山材料被恢复。
6. SOURCE_LEDGER 的宽泛 `P0_candidate_scoring` 不得覆盖 candidate/evidence/fusion 中更细的 guarded/block 判断。
7. 不得提前改学生稿、Word、PDF、final、FINAL_ACCEPTANCE、coverage close。

## Governor 裁决

final_gate: PASS_WITH_GUARD

允许：正式评分组进入候选融合；guarded 组以 guarded 表述积累进入。

禁止：2026丰台期末 Q20 promotion；2026石景山期末恢复；任何 guarded 行升级为主频；学生稿/Word/PDF/final/coverage close。

本次只写 Governor gate 文件；未改其他产物。
