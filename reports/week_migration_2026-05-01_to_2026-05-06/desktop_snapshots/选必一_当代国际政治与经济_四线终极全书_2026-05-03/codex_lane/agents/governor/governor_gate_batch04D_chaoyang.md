# Governor Franklin Gate - Batch04D Chaoyang

verdict: PASS_WITH_FIXES

scope: Batch04D 朝阳窄门验收。只审预融合证据、合并登记、manual evidence notes、source ledger、coverage、worker triage；不宣布最终完成，不放行学生稿/Word/PDF/final/FINAL_ACCEPTANCE/coverage close。

read_files:
- `fusion/scoring_atom_table_batch04D_chaoyang_prelim.csv`
- `fusion/merge_register_batch04D_chaoyang_updates.md`
- `02_extraction/codex_extraction_logs/batch04D_chaoyang_manual_evidence_notes.md`
- `SOURCE_LEDGER.csv`
- `COVERAGE_MATRIX.csv`
- `codex_lane/agents/worker/worker_batch04D_chaoyang_triage.md`

## Gate Decision

Batch04D 不 FAIL，但不能直接 PASS。当前允许进入返修后的 `candidate_with_fixes` 准备态；必须先完成下列返修项，再由后续 Governor 窄门确认是否可把 coverage / fusion 状态从 `prelim_candidate` 推进为 `candidate_with_fixes`。

继续阻断：
- 学生稿、学生预览终稿、Word、PDF、final、FINAL_ACCEPTANCE。
- coverage close / source exhaustion close。
- 把 `2025朝阳期末 Q21` 等级答案或普通宽口径答案升为 P0 主链。
- 把 2026 石景山期末任何内容回补入本批或后续融合。

## Evidence Verdict

可作为主候选但需带 fixes 的范围：
- `ATOM-CY01` - `ATOM-CY06`：2025朝阳二模 Q21。P0 正式细则 docx + P3 题面，三层结构成立；周边工作不得拆成虚假频次。
- `ATOM-CY07` - `ATOM-CY11`：2024朝阳二模 Q20。P0 细则 PDF/docx + P3 题面，全球气候治理原则/背景/路径成立；同槽替代表述不得拆成多个必答频次。
- `ATOM-CY12` - `ATOM-CY13`：2024朝阳一模 Q21。P0 PPTX 主证据成立，但混模块边界必须保留。
- `ATOM-CY15` - `ATOM-CY17`：2025朝阳一模 Q20。P0 扫描细则 PDF 已视觉核读，题面 P3 支持成立；绿色化、数字化、现代产业体系不得升主链。
- `ATOM-CY18` - `ATOM-CY22`：2026朝阳期末 Q20。P0 扫描细则 PDF + P3 视觉题面成立；四角度必须保留背景+目标层，不得压成“更有作为”总帽。
- `ATOM-CY23` - `ATOM-CY24`：2024朝阳期中 Q20(3)。P0 docx/rtf 细则 + P3 题面成立；只处理第三问，前两问经济与社会不入主链。

必须降级或隔离：
- `ATOM-CY-B01`：2025朝阳期末 Q21。当前 `P1_level_answer_or_reference_only / reference_only` 判定正确。题面可读不等于有逐点细则，后附宽口径答案不得升 P0 主链。

## Hard-Negative Checks

- 弱证据冒充评分细则：未发现 Batch04D 主候选把 P3 题面直接当作 P0；但 `2024朝阳一模 Q21` 的宽口径补充 docx 在 ledger 中仍写成 `P0_formal_scoring_rule_text`，需要返修为 support/reference，不得作为独立 P0 术语来源。
- 参考答案冒充细则：`2025朝阳期末 Q21` 已降为 reference_only；`2024朝阳一模 Q21` 宽口径参考支持源需要降格标注。
- 2026石景山混入：在本批六个被审文件中未见石景山回补。
- 学生版混入后台字段：manual notes 写明 `student_doc_touched: no`，worker 写明未修改 `07_student_doc/`、未生成 Word/PDF；本门禁不放行学生版。后续若入学生预览，必须另跑清洁扫描。
- coverage/source ledger 闭合：当前 Batch04D coverage 仍为 `pending / batch04D_prelim_candidate / reference_only`，未闭合；这符合本门禁阶段，但不得宣称 coverage closed。
- 合并同类项丢失核心信息：merge register 保留经济全球化完整五词、贸易投资便利化、供应链安全稳定、周边命运共同体、全球治理不同功能，方向可接受；但仍有下列局部信息/边界需返修。

## Must-Fix Items

1. `ATOM-CY14` 必须返修。`坚持独立自主`、`发展主动权`可保留为选必一边界候选；`增强自主创新能力`、`关键核心技术自主可控`不得作为选必一主链核心。处理方式：拆分为主链可用句 + boundary note，或整体降为 `candidate_with_fixes_boundary_guard`。

2. `2024朝阳一模 Q21_SRC_8a924a245316` 必须降格说明。manual notes 称其为“参考答案支持但较宽”，SOURCE_LEDGER 却标 `P0_formal_scoring_rule_text`。返修时应写明：P0 主证据为 PPTX；该 docx 只作宽口径支持/reference，不独立生成术语。

3. `ATOM-CY25` 必须防止计频。该条来自 2024朝阳期中 Q20(3) 短评总评/表达层，应作为“中国全球治理理念”的表述积累或边界记录，不得与逐点细则同权计入主链频次。

4. `ATOM-CY23` 术语需校正为“两个市场两种资源”。当前 `expression_variant` / `answer_sentence_fusion` 出现“两个市场两个资源”，入表前必须统一。

5. `2024朝阳二模 Q20` 的“企业绿色低碳技术创新”不得主链计频，但需在 boundary note 或 merge register 中明确记录为混模块/结果性角度，避免因合并而丢失原题评分信息。

6. `candidate_prelim` 状态不得直接进入主表。返修后，主候选才能改为 `candidate_with_fixes`；`ATOM-CY-B01` 必须继续 `reference_only`；coverage 只能改为 `pass_with_fixes` 或同等待复核状态，不得 close。

7. 后续若生成学生预览，必须先重跑学生清洁扫描，禁止出现 `source_ledger_refs`、P0/P1/P3、path、model、worker、governor、coverage、细则位置调试语等后台字段。

## Allowed Next Step

允许 Patcher / Fusion 对 Batch04D 做返修补丁和同类项合并更新；不允许进入学生稿、Word/PDF、final、FINAL_ACCEPTANCE 或 coverage close。

final_gate: PASS_WITH_FIXES

## 返修复验

recheck_verdict: PASS_AFTER_FIXES

复验时间：2026-05-03

复验范围：
- `fusion/scoring_atom_table_batch04D_chaoyang_prelim.csv`
- `fusion/merge_register_batch04D_chaoyang_updates.md`
- `SOURCE_LEDGER.csv`
- `COVERAGE_MATRIX.csv`

返修闭合确认：
- `fusion/scoring_atom_table_batch04D_chaoyang_prelim.csv` 已无 `candidate_prelim`；当前状态为 `candidate_with_fixes`、`candidate_with_fixes_boundary_guard`、`candidate_with_boundary_guard`、`candidate_p2_guard`、`reference_only`。
- `ATOM-CY14` 已降为 `candidate_with_fixes_boundary_guard`；核心改为“坚持独立自主，把发展主动权牢牢掌握在自己手中”，`增强自主创新能力`、`关键核心技术自主可控` 已写入 boundary note，不计选必一主链频次。
- `2024朝阳一模_Q21_SRC_8a924a245316` 已在 `SOURCE_LEDGER.csv` 降为 `P1_reference_answer_support / P1_reference_support_not_independent_rubric`；P0 主证据明确为 `SRC_4fc81e818683` 评分细则 PPTX。
- `2025朝阳期末 Q21` 已新增 P2 guard：`SOURCE_LEDGER.csv` 中 `2025朝阳期末_Q21_SRC_CY2025QIMO_PPTX` 为 `P2_teaching_lecture_with_point_scoring`，且 `ATOM-CY26` - `ATOM-CY29` 均为 `candidate_p2_guard`。原 P0 PDF `2025朝阳期末_Q21_SRC_49b23fecab97` 仍保持 `P1_level_answer_or_reference_only`，未被升为 P0 主链。
- `merge_register` 已记录企业绿色低碳技术创新、绿色化/数字化、2026朝阳期末背景+目标结构、2025朝阳期末 P2 guard 等边界；未发现合并同类项丢失核心信息。
- `ATOM-CY23` 已统一为“两个市场两种资源”；`ATOM-CY23` - `ATOM-CY25` 已带 `candidate_with_boundary_guard`，短评结构分、标题分、表达分不计术语频次。

继续阻断：
- 不放行学生稿、Word、PDF、final、FINAL_ACCEPTANCE。
- 不允许 coverage close / source exhaustion close。
- `COVERAGE_MATRIX.csv` 中 Batch04D 仍为 `pending / batch04D_prelim_candidate` 或 `batch04D_P2_candidate_with_guard` 状态；本复验只确认返修闭合，不宣布 coverage 闭合。
- `2025朝阳期末 Q21` 的 P2 guard 只能作为低等级候选和表述积累，不能冒充 P0 评分细则频次。

recheck_gate: PASS_AFTER_FIXES
