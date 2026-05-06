# Governor Batch04C Dongcheng Fix Closure Gate

verdict: PASS_WITH_GUARD

scope: Batch04C 东城返修后窄门禁。只根据 `fusion/scoring_atom_table_batch04C_dongcheng_prelim.csv`、`fusion/merge_register_batch04C_dongcheng_updates.md`、`COVERAGE_MATRIX.csv`、`SOURCE_LEDGER.csv` 裁定推进权限；不裁定学生稿、Word/PDF、final、coverage close。

## Closure Decision

允许：
- Batch04C 主候选推进到 `candidate_with_fixes`。
- Coverage 中 Batch04C 主候选可从 `pending/prelim_candidate` 改为 `pass_with_guard/candidate_with_fixes`。
- `2026东城一模 Q19(3)` 必须继续保持 `boundary_only`，不得入选必一主链频次。

继续阻断：
- 学生稿 / 学生预览终稿 / Word / PDF / final / FINAL_ACCEPTANCE。
- coverage close / source exhaustion close。
- 把本门禁解释为 Patcher 全闭环或可直接入学生正文。

## Fix Closure Findings

返修项已闭合：
- 全球倡议已挂入同一父核心 `全球倡议系统推动构建人类命运共同体`，并保留四大全球倡议的 4+2+1 结构与三大倡议的路径+效果结构，未制造虚假独立频次。
- 2024东城二模 Q20 已拆为 `ATOM-DC07A/07B/07C` 三个倡议子槽，来源仍标为 `P0_marking_summary_docx_with_visual_paper_prompt`，视觉源只作题面支撑。
- 2026东城期末 Q20 的全球发展、安全、文明、治理倡议与系统推动层均标为 `candidate_with_fixes`，但以父核心合并，不再散落到错误桶。
- 2025东城一模 Q20 保留经济全球化完整五词方向；高水平对外开放和高质量发展仍只在 boundary note 中作边界表述。
- 2025东城期末 Q20 明确“不得使用试卷普通解析冒充细则”，P3 试卷后附解析未被升为 P0。
- `ATOM-DC-B01` 仍为 `boundary_only`，boundary note 明确未来产业、高水平对外开放、产业链韧性和高质量发展不直接计入选必一主链频次。

## Evidence Boundary

主候选可推进但必须保留证据标签：
- `ATOM-DC01` - `ATOM-DC06`: `P0_formal_scoring_rule_pptx` + P3 paper support。
- `ATOM-DC07A` / `ATOM-DC07B` / `ATOM-DC07C` / `ATOM-DC08`: P0 阅卷总结 + P3 visual prompt support。
- `ATOM-DC09` - `ATOM-DC18`: P0 formal scoring PDF/text + P3 paper support。

边界项：
- `ATOM-DC-B01`: `P0_formal_scoring_rule_pptx_but_mixed_module`，仅作 mixed-module boundary observation。

不得计频：
- 2024东城二模 Q20 的视觉题面源。
- 2025东城期末 Q20 的普通解析/参考答案。
- 2026东城一模 Q19(3) 中的未来产业、新质生产力、产业链韧性、高质量发展。

## Coverage State

当前 `COVERAGE_MATRIX.csv` 中 Batch04C 主候选仍为 `pending/prelim_candidate`，`2026东城一模 Q19(3)` 为 `boundary_only`。本门禁允许后续把主候选推进为 `pass_with_guard/candidate_with_fixes`；不得把任何 Batch04C 行写成 coverage closed。

final_gate: PASS_WITH_GUARD
