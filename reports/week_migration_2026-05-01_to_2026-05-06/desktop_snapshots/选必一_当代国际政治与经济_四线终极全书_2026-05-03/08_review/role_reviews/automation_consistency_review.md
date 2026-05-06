# 自动化一致性核查报告

> Supersession note, 2026-05-04 02:24 CST: this was the pre-delivery automation report. Its warnings about 09_delivery path registration and Word/PDF release were closed later. Current final automation status is `PASS` in `automation_consistency_final_sync_20260504.md`.

role: Codex A 自动化检测者  
scope: SOURCE_LEDGER / COVERAGE_MATRIX / fusion combined / six-bucket clusters / 09_delivery 学生讲义 / progress / task_plan / 督工验收状态  
verdict: PASS_WITH_WARNINGS

## 1. 结构计数

| artifact | 物理行数 | 数据行数 | 坏行 | 重复关键键 | 结论 |
|---|---:|---:|---:|---:|---|
| SOURCE_LEDGER.csv | 206 | 205 | 0 | ledger_id 重复 0 | PASS |
| COVERAGE_MATRIX.csv | 76 | 75 | 0 | suite+question_no 重复 0 | PASS |
| fusion/all_scoring_atoms_combined_20260504.csv | 212 | 211 | 0 | 未发现结构坏行 | PASS |
| fusion/six_bucket_core_clusters_20260504.csv | 41 | 40 | 0 | 未发现结构坏行 | PASS |

坏行口径：CSV 解析失败、列数不等于表头、空白数据行、关键键重复。

## 2. 跨表一致性

- all_scoring_atoms 中 `source_ledger_refs` 指向 SOURCE_LEDGER 的缺失数：0。
- all_scoring_atoms 中出现的题目，均能在 COVERAGE_MATRIX 中找到对应题目级覆盖行：0 个缺口。
- six_bucket_core_clusters 汇总 `atom_count` = 191，`guarded_atom_count` = 44。
- progress.md、task_plan.md、reports/督工验收状态.md 均记录当前融合候选为 191 条，并说明 Word/PDF/FINAL 尚未放行；与 six_bucket_core_clusters 的 191 条口径一致。

注意：all_scoring_atoms 总数据行为 211，其中包含 reference_only、boundary_only、excluded_boundary_subpoint、result_expression_only 等非主线行。若用严格主线口径排除这些状态，主线条数回到 191；与 cluster 表和控制文件一致。

## 3. 石景山排除闭合

- COVERAGE_MATRIX 中 `2026石景山期末 all` 标为 `excluded`，证据状态为 `user_confirmed_excluded_no_scoring`。
- SOURCE_LEDGER 未发现 2026石景山期末被作为有效 source 行继续入账。
- all_scoring_atoms、six_bucket_core_clusters、09_delivery 学生讲义未发现 2026石景山期末进入主线。
- 现有“石景山”相关内容为 2026石景山一模 Q20 与 2024石景山一模 Q19(2)，不属于用户确认排除的 2026石景山期末；其中 2024石景山一模已按 reference/boundary 口径处理。

结论：石景山期末排除闭合，未发现误入主线。

## 4. 主线题数与整题汇总

- 09_delivery 学生讲义中按题训练主线题节：47。
- `**整题汇总卷面答案**` 块：47。
- `**本题命中框架**` 块：47。
- `**条目拆解**` 块：47。

结论：主线题数与整题汇总数量自洽。

补充口径：six_bucket_core_clusters 的 `source_questions` 去重后为 50 个题源；其中 3 个没有进入 09_delivery 的按题训练主线，但出现在“慎用与跨模块表达积累”部分：

- 2024东城一模 Q16
- 2024东城一模 Q20
- 2025海淀期末 Q22

这与此前“降为拓展迁移/慎用边界”的处理一致，不构成主线漏题。但建议在控制文件中明确“47 主线题 + 3 慎用迁移题源”的口径，避免后续自动化把 50 与 47 判为冲突。

## 5. 学生稿后台污染扫描

09_delivery 学生讲义未发现以下后台/证据污染词：

- P0/P1/P2/P3
- 参考答案
- 评分细则 / 评分 / 细则 / 讲评
- OCR / debug / SOURCE / ledger / coverage
- source 路径类英文后台词

扫描到“路径”26 次，均为学生可读语境，如“发展路径”“和平路径”“做法或路径”，未发现文件路径污染。

## 6. Warning 项

W1. 控制文件登记路径与当前核查路径不完全一致  
progress.md、task_plan.md、reports/督工验收状态.md 主要登记的是 `07_student_doc/选必一_完整学生讲义_干净候选稿_20260504.md`，而本轮核查对象包含 `09_delivery/选必一_当代国际政治与经济_完整学生讲义_20260504.md`。两者从内容状态看应为同一候选链路的后续交付稿，但控制文件尚未显式登记 09_delivery 路径。

建议：后续由总控/交付线程补一行路径映射或状态登记，说明 09_delivery 文件是否为 07_student_doc 干净候选稿的交付版。

W2. all_scoring_atoms 中 boundary/reference 行仍带 final_bucket/final_core_cluster  
检测到 reference_only / boundary_only 等非主线状态行仍有 `final_bucket` 与 `final_core_cluster`。当前 09_delivery 已把相关内容放入慎用/边界位置或排除主线，不构成本轮污染；但若后续脚本只按 final_bucket 聚合、不按 promotion_status 过滤，可能把 reference_only/boundary_only 误拉回主表。

建议：后续自动化消费 all_scoring_atoms 时硬性过滤 `promotion_status`，主线只取 candidate / candidate_with_fixes / candidate_with_guard 等放行状态；reference_only、boundary_only、excluded、prompt_only、result_expression_only 不得进入主线题节。

## 7. 结论

本轮一致性核查结论为 PASS_WITH_WARNINGS：

- CSV 结构、行数、坏行、重复键：通过。
- SOURCE_LEDGER 与 all_scoring_atoms 引用关系：通过。
- COVERAGE_MATRIX 与题目覆盖关系：通过。
- 2026石景山期末排除：闭合。
- 主线 47 题与 47 个整题汇总：自洽。
- 191 条融合候选与 six_bucket_core_clusters / 控制文件：自洽。
- 需后续补齐的不是正文内容，而是控制文件路径登记与自动化过滤口径。
