# Governor Franklin Gate - Batch04E Haidian Qizhong

verdict: PASS_WITH_FIXES

scope: Batch04E 2024海淀期中补遗窄门验收。只审预融合表、合并登记、manual evidence notes、source ledger、coverage、worker triage；不宣布最终完成，不放行学生稿/Word/PDF/final/FINAL_ACCEPTANCE/coverage close。

read_files:
- `fusion/scoring_atom_table_batch04E_haidian_qizhong_prelim.csv`
- `fusion/merge_register_batch04E_haidian_qizhong_updates.md`
- `02_extraction/codex_extraction_logs/batch04E_haidian_qizhong_manual_evidence_notes.md`
- `SOURCE_LEDGER.csv`
- `COVERAGE_MATRIX.csv`
- `codex_lane/agents/worker/worker_batch04E_haidian_qizhong_triage.md`

## Gate Decision

Batch04E 不 FAIL，但不能直接 PASS。允许进入 Patcher/Fusion 返修，返修后才可把合格项推进到 `candidate_with_fixes` 或 `candidate_with_boundary_guard`。当前继续阻断学生稿、Word、PDF、final、FINAL_ACCEPTANCE、coverage close。

## Evidence Verdict

证据边界基本成立：
- `2024海淀期中 Q16(2)`：P0 为 `SRC_e3f88f68dd56` 细则 PDF 文本，P3 为 `SRC_132d9a876bce` 试卷视觉题面。细则明确该题为必修二4分 + 选必一2分，当前只抽“国际组织赋权 / 全球经济治理 / 规则制定”2分点，未把品牌、产品、成本、税收、市场调研等经济管理内容收入主链。
- `2024海淀期中 Q21(2)`：P0 为同一细则 PDF，P3 为试卷视觉题面。manual notes 与 worker 均给出 `变4分 + 不变5分` 结构；弱证据未被冒充为评分细则。

未发现硬性否决项：
- 未发现普通参考答案被单独冒充为评分细则。
- 未发现 2026 石景山期末混入。
- 未发现学生稿、Word、PDF、final 被放行；manual notes 与 worker 均写明 `student_doc_touched: no`。
- coverage/source ledger 仍为 prelim/pending，未假闭合。

## Atom-Level Findings

可保留但需带边界：
- `ATOM-HDQZ01`：可保持 `candidate_with_boundary_guard`。必须继续写明 Q16(2) 只收选必一2分，其他经济建议只作边界。

需返修后推进：
- `ATOM-HDQZ02`：可进入时代背景桶，但必须标明是 Q21(2) 的“变：世界之变”，不得替代“不变”侧外交政策。
- `ATOM-HDQZ03`：可进入中国桶，但必须标明是“中国之变”；`人类命运共同体` 只能作为中国之变变通或新时代外交理念，不得写成新中国外交一贯不变。
- `ATOM-HDQZ04`：可进入中国外交指导思想表述积累；必须保留“习近平外交思想”官方表述，不随意改写。
- `ATOM-HDQZ05`：可进入中国外交政策核心，但必须保留基本立场、宗旨、目标、基本准则四件套；国家性质只能作为辅助，不扩成政治与法治频次。
- `ATOM-HDQZ06`：可作为不变侧反霸权/反强权表达积累；不得泛化为所有外交题必答频次。

## Must-Fix Items

1. `ATOM-HDQZ02` - `ATOM-HDQZ06` 当前仍为 `candidate_prelim`。返修时需按功能改为 `candidate_with_fixes` 或必要的 `candidate_with_boundary_guard`，不得直接写入主表。

2. Q21(2) 必须持续保留 `变` / `不变` 双框架。入融合表时建议在 `merge_action` 或 `boundary_note` 明示：`HDQZ02-HDQZ04` 属于“变”，`HDQZ05-HDQZ06` 属于“不变”。

3. `人类命运共同体` 只能留在 `ATOM-HDQZ03` 的“中国之变/新时代外交理念变通”边界；不得并入 `ATOM-HDQZ05` 的不变侧，也不得在学生稿中写成“新中国外交一贯坚持人类命运共同体”。

4. Q16(2) 的 mixed-module 边界必须继续保留：品牌战略、产品创新、市场调研、成本降低、供应链基础设施、税收政策、企业管理等不计选必一主链频次。

5. `COVERAGE_MATRIX.csv` 中 Batch04E 仍为 `pending / batch04E_prelim_candidate`。后续只允许更新为 `pass_with_fixes` / `candidate_with_fixes` 等中间状态，不得写 coverage closed。

6. 后续如进入学生预览，必须另跑学生清洁扫描，禁止出现 `source_ledger_refs`、P0/P3、path、worker、governor、coverage、细则位置调试语等后台字段。

## Allowed Next Step

允许 Patcher/Fusion 对 Batch04E 做返修补丁和同类项合并更新；不允许进入学生稿、Word/PDF、final、FINAL_ACCEPTANCE 或 coverage close。

final_gate: PASS_WITH_FIXES

## 返修复验

recheck_verdict: PASS_AFTER_FIXES

复验时间：2026-05-03

复验范围：
- `fusion/scoring_atom_table_batch04E_haidian_qizhong_prelim.csv`
- `fusion/merge_register_batch04E_haidian_qizhong_updates.md`
- `COVERAGE_MATRIX.csv`

返修闭合确认：
- `fusion/scoring_atom_table_batch04E_haidian_qizhong_prelim.csv` 已无 `candidate_prelim`。
- `ATOM-HDQZ01` 保持 `candidate_with_boundary_guard`，仍只收 Q16(2) 选必一2分的国际组织赋权 / 全球经济治理 / 规则制定点，必修二与企业经营管理内容未入主链。
- `ATOM-HDQZ02` - `ATOM-HDQZ06` 均已改为 `candidate_with_fixes`。
- `ATOM-HDQZ02`、`ATOM-HDQZ03`、`ATOM-HDQZ04` 的 `merge_action` / `boundary_note` 已标明属于 `变` 侧框架。
- `ATOM-HDQZ05`、`ATOM-HDQZ06` 的 `merge_action` / `boundary_note` 已标明属于 `不变` 侧框架。
- `人类命运共同体` 仍留在 `ATOM-HDQZ03` 的“中国之变/新时代外交理念变通”边界中，未被移入 `ATOM-HDQZ05` 的不变侧。
- `merge_register` 已显式记录 `HDQZ02-HDQZ04` 属于变框架，`HDQZ05-HDQZ06` 属于不变框架，并保留 Q16(2) mixed-module 边界。

继续阻断：
- 不放行学生稿、Word、PDF、final、FINAL_ACCEPTANCE。
- 不允许 coverage close / source exhaustion close。
- `COVERAGE_MATRIX.csv` 中 Batch04E 行仍为 `pending / batch04E_prelim_candidate`；本复验只确认返修闭合，不宣布 coverage 闭合。

recheck_gate: PASS_AFTER_FIXES
