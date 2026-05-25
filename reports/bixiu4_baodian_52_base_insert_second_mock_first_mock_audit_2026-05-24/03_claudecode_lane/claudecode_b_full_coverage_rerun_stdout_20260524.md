本轮 ClaudeCode B 全量重跑产物已落到 `03_claudecode_lane/`：

**1. `claudecode_b_full_coverage_rerun_20260524.csv`（50 行 ≈ 49 套题级行 + 1 表头）**
按 `suite,year,phase,question_no,status,existing_coverage,proposed_framework_node,evidence_level,action,reason` 给出 35 套覆盖矩阵；状态分布：covered_in_base 24 / covered_by_patch 11 / boundary_excluded 6 / need_evidence(HOLD) 7 / should_add 0。

**2. `claudecode_b_full_coverage_rerun_20260524.md`**
- A 部分：4 个重点核验二模题（海淀/西城/顺义/石景山二模 Q16/Q17(3)）+ 其余 4 套二模题逐题厚度复核，全部 KEEP，无 REWRITE/DELETE。
- B 部分：高风险节点（主次矛盾 / 两点论重点论 / 主流支流 / 辩证否定 / 量变质变 / 实践认识 / 反作用 / 价值观 / 人民群众 / 系统优化）逐项核到入栏位置；2024-2026 一模全部落入 covered_in_base / covered_by_patch / boundary_excluded / HOLD 四种状态之一。
- 严格规则自检 6 项全过。

**3. `claudecode_b_full_coverage_insert_candidates_20260524.jsonl`**
本轮在严格证据口径下 0 条新增/重写：强细则一模候选全部已落地或属于 already_in_base / culture_boundary / module_boundary；剩余 HOLD 项均为弱参考答案 / 题号待定 / OCR 重残 / 选必三边界，按硬规则不立条。

ClaudeCode B 本轮已到融合审核前，不代表最终 PASS。
