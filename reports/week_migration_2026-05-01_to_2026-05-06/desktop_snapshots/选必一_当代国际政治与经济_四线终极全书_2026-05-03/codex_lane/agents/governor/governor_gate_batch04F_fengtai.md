# Governor Gate - Batch04F 2025 Fengtai Ermo

final_gate: PASS

scope: Batch04F 2025丰台二模窄门验收。只审用户列明文件；不编辑学生稿、不编辑 fusion 文件、不宣布最终完成、不放行 Word/PDF/final/FINAL_ACCEPTANCE/coverage close。

read_files:
- `05_coverage/batch04F_fengtai_candidate_questions.csv`
- `codex_lane/agents/worker/worker_batch04F_fengtai_triage.md`
- `02_extraction/codex_extraction_logs/batch04F_fengtai_manual_evidence_notes.md`
- `fusion/scoring_atom_table_batch04F_fengtai_prelim.csv`
- `fusion/merge_register_batch04F_fengtai_updates.md`
- `SOURCE_LEDGER.csv`
- `COVERAGE_MATRIX.csv`
- `06_conflicts/batch04F_claudecode_conflict_resolution.md`
- `claudecode_lane/progress_batch04F.md`
- `claudecode_lane/batch04F_fengtai_matrix.csv`
- `claudecode_lane/batch04F_fengtai_entries.md`
- `04_suite_reports/claudecode_suite_reports/batch04F_fengtai_suite_report.md`

## Gate Decision

Batch04F 通过本轮 Governor gate。允许 Q20 的 `FT01` - `FT04` 作为 P0 支撑的 fusion candidate 继续进入后续 Patcher/Fusion 状态更新；不需要返修后再复验。

仍然禁止：
- 学生稿 / 学生预览终稿 / Word / PDF / final / FINAL_ACCEPTANCE。
- coverage close / source exhaustion close。
- 把本 gate 解释为整书终态完成。

## Evidence Check

Q20 证据边界成立：
- 主证据为 `2025丰台二模_Q20_SRC_1543d8baa151`，即 P0 `20题.docx` formal marking document。
- `2025丰台二模_Q20_SRC_770de383c911` 仅作 P3 paper text support。其包含题面和参考答案，但 SOURCE_LEDGER 已明确“scoring authority remains 20题.docx”；未发现普通参考答案冒充评分细则。
- Codex A 与 ClaudeCode B 均确认 Q20 为 4 个角度 × 2 分，共 8 分。

排除/边界项成立：
- Q18：`no_xuanbiyi`。设问指定《经济与社会》，只作源穷尽边界记录。
- Q19(2)：`no_xuanbiyi`。设问指定《法律与生活》，只作源穷尽边界记录。
- Q21：`boundary_only` / `no_xuanbiyi`。综合等级题，示例虽有“一带一路/全球治理”表述，但评分主轴为“势”的智慧与哲学/综合论证，不提升为选必一频次。

## Atom Review

`ATOM-FT01` - PASS:
- 保留“最大发展中国家身份 -> 国际政治经济格局重要力量 -> 参与全球治理 -> 推动全球南方现代化”完整链条。
- 未把裸关键词“全球南方”当作 2 分 atom。

`ATOM-FT02` - PASS:
- bucket 为 `中国`，符合冲突裁决。
- 与 `FT03` 分开：FT02 是中国通过广义国际组织平台成为全球治理体系重要参与者、贡献者和改革者，不是联合国常任理事国专门角度。

`ATOM-FT03` - PASS:
- bucket 为 `联合国`。
- 保留“联合国常任理事国 + 《联合国宪章》宗旨原则 + 践行多边主义 + 维护多边体制权威性和有效性”完整链条。
- 未把裸关键词“联合国”当作 2 分 atom。

`ATOM-FT04` - PASS:
- bucket 为 `政治多极化`，符合冲突裁决。
- 保留“推动构建人类命运共同体 + 平等、开放、合作、共享 + 全球治理体制向更加公正合理方向发展”。
- 未压缩成空泛的“中国方案”或“全球治理正确方向”。

## Merge / Conflict Check

ClaudeCode B 与 Codex A 冲突已裁决：
- FT01 合并到中国身份/全球治理角色家族，作为“全球南方现代化”场景变体。
- FT02 归 `中国` 桶，不归泛化 `联合国`。
- FT03 保持 `联合国` 桶。
- FT04 归 `政治多极化`，中国/HMC 只作交叉引用。

合并同类项未丢失核心信息；四个 2 分角度均保留了评分位置、材料触发和答题链条。

## Coverage / Release Check

当前 `COVERAGE_MATRIX.csv` 中 Batch04F 仍为：
- Q18 `no_xuanbiyi`
- Q19(2) `no_xuanbiyi`
- Q20 `batch04F_prelim_candidate`
- Q21 `boundary_only`

这不是 coverage close。后续可以把 Q20 推进为 candidate 状态，但不得写 coverage closed，不得放行学生稿、Word/PDF、final 或 FINAL_ACCEPTANCE。

## Blocking Fixes

None for this gate.

final_gate: PASS
