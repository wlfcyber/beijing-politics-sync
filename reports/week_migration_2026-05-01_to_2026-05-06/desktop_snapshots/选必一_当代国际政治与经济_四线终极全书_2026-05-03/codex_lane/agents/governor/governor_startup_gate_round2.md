# Codex-A Governor Startup Gate Round 2

Run: 选必一《当代国际政治与经济》四线终极全书 2026-05-03

Role: Codex production lane A / 监管者-Governor

结论：LIMITED PASS / 条件放行

允许从 Phase 1C/Phase 2 进入“源读取与首批条目草案”。不允许放行学生版终稿、coverage 闭合、Word/PDF、FINAL_ACCEPTANCE PASS。所有首批条目只能是 `draft/not_promoted`，必须逐源核读后再由 Governor 复检。

## 已读依据

- `MASTER_REQUIREMENTS.md`
- `task_plan.md`
- `00_control/RUN_MANIFEST.yaml`
- `RUN_MANIFEST.json`
- `00_control/NOTEBOOK_DIGEST.md`
- `USER_FRAMEWORK.md`
- `00_control/PROGRESS_LEDGER.jsonl`
- `progress.md`
- `codex_lane/agents/ROLE_LEDGER.md`
- `codex_lane/agents/patcher/patcher_merge_and_multipoint_report.md`
- `01_source_inventory/SOURCE_INVENTORY.csv`
- `SOURCE_LEDGER.csv`
- `COVERAGE_MATRIX.csv`
- `03_entries/evidence_level_index.csv`
- `03_entries/priority_subjective_question_matrix.csv`
- `04_suite_reports/suite_completion_matrix.csv`
- `05_coverage/*.csv`
- `05_coverage/missing_questions.md`
- `05_coverage/unresolved_blockers.md`
- `feige-politics-garden-xuanbiyi/SKILL.md`
- `feige-politics-garden-xuanbiyi/references/current-user-requirements.md`
- `feige-politics-garden-xuanbiyi/references/xuanbiyi-term-protocol.md`

## Round 2 数据状态

- `00_control/NOTEBOOK_DIGEST.md` 已从空壳返修为 16 条硬检查，覆盖六桶、P0/P1 边界、石景山排除、总说/分说、答案句风险词。
- `USER_FRAMEWORK.md` 已写入六桶、核心采分点字段、同核心合并原则和硬样本。
- `01_source_inventory/SOURCE_INVENTORY.csv`：1372 条候选文件记录。
- `SOURCE_LEDGER.csv`：90 条首批源定位记录，覆盖 11 个题号；其中 `P0_candidate=24`、`P1_reference_only_until_confirmed=4`、`P2_teaching_or_lecture=5`、`P3_paper_text=57`，状态均为 `located_needs_read_recheck`。
- `COVERAGE_MATRIX.csv`：11 条首批工作行，全部 `not_promoted`，不是闭合表。
- `03_entries/evidence_level_index.csv`：11 条，全部 `read_source_and_assign_P0_P1_P2_or_blocked` / `not_promoted`。
- `04_suite_reports/suite_completion_matrix.csv`：11 条，全部 `not_closed`。
- `FINAL_ACCEPTANCE_REPORT.md` 仍为 `Status: not_started`。

## 启动闸门复检表

| 检查项 | 结论 | Governor 判定 |
|---|---|---|
| Notebook 吸收 | PASS | 已转成可执行检查项，可作为 worker/patcher/Governor 的硬规则输入。 |
| 用户六桶框架 | PASS | `USER_FRAMEWORK.md` 已固定六桶、字段和硬样本，可进入源读取后的条目草案。 |
| 源库存 | PASS for Phase 2 | `SOURCE_INVENTORY.csv` 已有 1372 条候选文件，足够支撑首批源读取；但 raw inventory 不是 evidence ledger，不能直接产生术语。 |
| 首批 source ledger | LIMITED PASS | 已有 90 条定位记录和 11 个优先题号，足够进入“逐源读取”。但全部仍是 candidate/recheck 状态，不能进入正式主表。 |
| P0/P1 边界 | PASS with guard | P1 当前标为 `P1_reference_only_until_confirmed` 或 `P1_reference_answer`，未发现已升格为正式细则；后续草案必须继续保留 `reference-only`，直到逐页核到 P0 或用户确认评分材料。 |
| 2026 石景山期末误入 | PASS with guard | `2026石景山期末` 只出现在 raw inventory 的 `已放弃/.../答案及评分参考.pdf` 和控制文件排除说明中，未进入 `SOURCE_LEDGER.csv`、`COVERAGE_MATRIX.csv` 或 entries。后续不得从 raw inventory 拉入该套卷。 |
| 旧结论直接继承 | PASS with guard | priority matrix 保留了旧索引术语作“定位/查漏”，但各行均写明 `needs_source_recheck`，coverage/evidence index 均 `not_promoted`。允许用作找源线索，不允许直接生成正式术语。 |
| Codex-A 五角色 | LIMITED PASS | 决策者、补丁者、自动化检测者、Governor 均已有产物或状态记录；worker 仍为 `running` 且 `codex_lane/agents/worker/` 暂无文件。允许 worker 进入源读取和首批草案；首批草案生成后必须补齐 worker 产物并交 patcher/Governor 复检。 |
| ClaudeCode B 线 | PASS as challenge input | `screen` 会话 `xuanbiyi_fourlane_full_20260503` 存在，stream log 正在增长。B 线输出只能作为独立挑战/差异输入，本地事实仍以本轮 source ledger 和核读记录为准。 |
| 学生版风险词 | PASS but no release | `07_student_doc` 和 `09_delivery` 仍是标题壳，未检出风险词；但没有正文，不具备学生版验收意义。 |
| Coverage 假闭合 | PASS | coverage/suite/final 均保持 `not_promoted`、`not_closed`、`not_started`，未发现假闭合。继续禁止任何闭环宣称。 |

## 仍需盯死的 Round 2 风险

1. `SOURCE_LEDGER.csv` 中多行是自动定位，部分路径不含精确套卷名或来自旧运行目录。典型高风险：`2026朝阳期中 Q17` 混入 `2026朝阳期末` 路径；`2025海淀期末 Q22` 混入 `2025海淀期中` 路径；`2026朝阳一模 Q20` 混入 `2025朝阳一模` rendered pages。逐源读取第一步必须先核验套卷/题号是否真正匹配。
2. `RUN_MANIFEST.json` 仍为 `status: not_started`，而 `00_control/RUN_MANIFEST.yaml` 为 running/bootstrapping；这不阻塞源读取，但后续 automation checker 需复检状态一致性。
3. `automation_checker/automation_status.md` 是返修前状态，ROLE_LEDGER 也标为 stale；真实源读取开始后必须重跑自动化检测者。
4. `05_coverage/unresolved_blockers.md` 写着 “No final blockers yet”，但首批全部仍是 `source_located_needs_recheck`；这句话不能解释为无阻塞闭合，只能理解为尚未形成最终 blocker。

## 条件放行范围

允许：

- 逐个读取 `SOURCE_LEDGER.csv` 中首批 11 个题号的 P0/P1/P2/P3 源。
- 对每题生成“源读取记录”和“首批条目草案”，草案状态必须为 `draft/not_promoted`。
- worker 可以先处理 P0 硬样本和海淀/东城/朝阳重点题；每条必须写明源文件、页/幻灯片/段落位置、P0/P1/P2/P3、是否 blocked。
- patcher 可以在 worker 草案出现后做一材料多点、总说/分说、同核心误拆/误合并、六桶归位复查。
- ClaudeCode 输出可用于挑战缺口，但不能替代本地源核读。

禁止：

- 把任何 `P1_reference_only_until_confirmed` 写成评分细则术语。
- 从旧样例或旧索引术语直接生成正式条目。
- 从 raw inventory 拉入 `2026石景山期末`。
- 发布学生版终稿、Word/PDF、频次统计、coverage 闭合或 FINAL_ACCEPTANCE PASS。
- 将 `COVERAGE_MATRIX.csv` 当前 11 行解释为穷尽覆盖。

## 下一次 Governor 复检最低线

1. `worker/` 必须出现首批源读取产物或条目草案。
2. 每条草案必须能回链到 `SOURCE_LEDGER.csv` 的 source_id，并写清 P0/P1/P2/P3 或 blocked。
3. `SOURCE_LEDGER.csv` 中自动错配候选必须被确认、剔除或改为 blocked。
4. `evidence_level_index.csv` 必须从 “prior evidence for recheck” 升级为 “current evidence after reading”。
5. `COVERAGE_MATRIX.csv` 可以更新为 `drafted_not_promoted`，但不得出现 closed/pass/final。

Governor 签发：Round 2 条件通过。可以进入源读取与首批条目草案；不得进入学生版终稿或 coverage 闭合。
