# Codex Lane A 自动化检测台账 - After Fusion Batch01

检测时间：2026-05-03 19:10 CST

运行目录：`/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03`

角色：Codex production lane A 内部智能体【自动化检测者】

检测范围：`task_plan.md`、`progress.md`、`00_control/PROGRESS_LEDGER.jsonl`、`SOURCE_LEDGER.csv`、`COVERAGE_MATRIX.csv`、`06_conflicts/ab_difference_table_batch01.md`、`fusion/*.md`、`fusion/scoring_atom_table_batch01.csv`、`claudecode_lane/*`、ClaudeCode screen 状态。

## 1. 总判定

状态：`FUSION_BATCH01_EXISTS_BUT_CONTROL_TABLES_STALE`

Batch01 已经进入 fusion candidate 阶段，新增文件可读；ClaudeCode screen 已退出；ClaudeCode Lane B 首轮产物已落盘；Codex A worker、patcher、governor Batch01 产物也已落盘。

但 `SOURCE_LEDGER.csv` 与 `COVERAGE_MATRIX.csv` 仍停留在启动态，和 `progress.md`、`PROGRESS_LEDGER.jsonl`、`fusion/*` 当前状态不一致。不得据此宣称 coverage closed、FINAL_ACCEPTANCE PASS、学生终稿、Word/PDF 完成。

## 2. 核心文件一致性

| 文件 | 行数/状态 | 当前含义 | 检测结论 |
|---|---:|---|---|
| `task_plan.md` | 51 | current_phase 为 Batch01 fusion candidate；明示终稿/Word/PDF/coverage close blocked | 一致，仍是运行中 |
| `progress.md` | 27 | 记录 ClaudeCode 退出、A/B 对比、fusion base 写入、Opus capture blocked | 一致，说明 Batch01 已推进 |
| `00_control/PROGRESS_LEDGER.jsonl` | 14 | 记录 `claudecode_lane_b_completed_first_pass`、`ab_difference_table_written`、`fusion_candidate_batch01_written` | 一致，事件流完整 |
| `SOURCE_LEDGER.csv` | 91 | 90 条数据全部 `located_needs_read_recheck` | 不一致，未同步 worker/fusion 已核读状态 |
| `COVERAGE_MATRIX.csv` | 12 | 11 条数据仍为 `running / waiting_for_worker_entries / not_started / not_promoted` | 明显不一致，已落后于 Batch01 实际进度 |
| `06_conflicts/ab_difference_table_batch01.md` | 50 | A/B 差异表可读，列出 still open | 可用，但仍有开放项 |
| `fusion/fusion_candidate_batch01.md` | 227 | `candidate_with_fixes`，列出下一工作队列 | 可读，不能作为学生终稿 |
| `fusion/merge_register_batch01.md` | 189 | `draft_not_promoted`，列出 Next Required Patches | 可读，状态谨慎 |
| `fusion/module_boundary_notes_batch01.md` | 62 | `active_guardrail` | 可读 |
| `fusion/scoring_atom_table_batch01.csv` | 27 physical lines | 25 个非空 atom，1 表头，1 空行 | atom 数正确；物理行数不是 25 |

## 3. ClaudeCode 状态

screen 状态：`EXITED`

- `screen -ls`：No Sockets found。
- 进程表未见 `claude -p --verbose --output-format stream-json` 继续运行。
- `progress.md` 和 `PROGRESS_LEDGER.jsonl` 均记录 ClaudeCode Lane B completed first pass。

ClaudeCode Lane B 产物状态：

| 文件 | 行数 | 结论 |
|---|---:|---|
| `claudecode_lane/progress.md` | 58 | 可读，声明 10 个优先硬样本首轮完成 |
| `claudecode_lane/source_inventory.csv` | 42 | 可读，41 条数据 |
| `claudecode_lane/subjective_question_matrix.csv` | 16 | 可读，15 条数据 |
| `claudecode_lane/claudecode_entries.md` | 414 | 可读 |
| `claudecode_lane/missing_blockers.md` | 120 | 可读 |
| `claudecode_lane/conflicts_for_codex.md` | 131 | 可读 |
| `04_suite_reports/claudecode_suite_reports/suite_report_index.md` | 87 | 可读 |

## 4. Batch01 CSV 检查

`fusion/scoring_atom_table_batch01.csv`：

- CSV 解析行数：27 行。
- 非空数据行：25 条 atom。
- 表头：1 行。
- 空行：1 行。
- atom 范围：`ATOM-B01` 到 `ATOM-B25`。
- `promotion_status`：25 条均为 `candidate_with_fixes`。
- bucket 分布：政治多极化 3，时代背景 2，联合国 1，中国 10，理论 4，经济全球化 5。

结论：如果要求是“25 个融合原子”，则 PASS；如果要求是“文件物理行数必须 25 行”，则 FAIL。当前更合理判定为 25 个非空 atom 已满足，但建议删除末尾空行或在台账中统一称“25 atoms”。

## 5. 禁入词与学生化风险

### 5.1 fusion atom 答案句

对 `answer_sentence_fusion` 列扫描 `采分点 / 要落到 / 材料中 / 本题需要 / 设问要求 / 细则要求 / 证据层级 / v7 / debug / audit / 模型聊天 / 本地路径`，未发现命中。

### 5.2 fusion md 文件

- `fusion/fusion_candidate_batch01.md` 命中 `Claude` 8 次、`GPT` 2 次，均在状态说明/审稿说明中。
- `fusion/merge_register_batch01.md` 命中 `audit` 2 次，均在教师/审计层说明中。

结论：作为内部 fusion 候选文件可以存在；若后续生成学生版，必须剥离 Claude/GPT/audit/证据层级/路径/后台状态语。

### 5.3 ClaudeCode Lane B 文件

`claudecode_lane/*.md` 中存在本地路径、`评标`、`证据层级`、`采分点` 等后台词。原因是 Lane B 文件是生产/审计文件，不是学生版。不得直接复制进学生终稿。

## 6. 明显状态矛盾

1. `progress.md` 与 `PROGRESS_LEDGER.jsonl` 表示 ClaudeCode 已退出且 Batch01 fusion candidate 已写入；但 `COVERAGE_MATRIX.csv` 仍把 11 行 `claudecode_status` 写成 `running`。
2. `fusion/*`、`worker_batch01_entries.md`、`patcher_batch01_review.md`、`governor_batch01_gate.md` 均显示 Batch01 已有 worker/patcher/governor/fusion 候选；但 `COVERAGE_MATRIX.csv` 仍为 `worker_status=assigned`、`patcher_status=waiting_for_worker_entries`、`governor_status=startup_fail_until_recheck`、`fusion_status=not_started`。
3. `SOURCE_LEDGER.csv` 90 条仍全部为 `located_needs_read_recheck`，但 worker source notes 已核读部分 P0/P2/user_confirmed_image_scoring_material 来源。说明 source ledger 没有同步提升或标注 batch evidence。
4. `fusion/scoring_atom_table_batch01.csv` 已有 P0/P2/user_confirmed_image_scoring_material 的 atom，但总覆盖层仍是 `evidence_status=not_promoted`。这个状态可以保守保留，但必须明确为“fusion candidate not promoted”，而不是“worker 未读源”。
5. `SOURCE_LEDGER.csv` 中仍大量保留旧目录路径作为定位线索；这可以作为 locator，但不能与 worker 本轮核读源证据混同。

## 7. 当前停工点

不是完全停工；下一步在 `fusion_candidate_batch01.md` 和 `merge_register_batch01.md` 中有明确队列：

1. Codex A Batch02：复核 B-only closed candidates，重点 `2026朝阳一模 Q20`、`2026顺义一模 Q20`、`2025海淀二模 Q21`、`2025海淀期末 Q22`。
2. 处理 `2025海淀期中 Q21(2)` 图片备注：判定是可积累表述变体，还是非累计提醒。
3. Claude Opus response 仍因 screen locked 未捕获，不能使用 Claude 文字。
4. Batch02 后再生成 sanitized section_batch 给 GPT-5.5 Pro/Claude Opus 做内容审查。

但控制台账存在停工风险：`COVERAGE_MATRIX.csv` 和 `SOURCE_LEDGER.csv` 不更新，会导致后续自动检测继续误报 running/not_started。

## 8. 叫醒任务模板

```text
你是 Codex production lane A 内部角色【决策者+台账同步员】。运行目录：
/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03

先读取：
1. codex_lane/agents/automation_checker/automation_status_after_fusion_batch01.md
2. progress.md
3. 00_control/PROGRESS_LEDGER.jsonl
4. codex_lane/agents/worker/worker_source_notes.csv
5. codex_lane/agents/worker/worker_batch01_entries.md
6. codex_lane/agents/patcher/patcher_batch01_review.md
7. codex_lane/agents/governor/governor_batch01_gate.md
8. 06_conflicts/ab_difference_table_batch01.md
9. fusion/scoring_atom_table_batch01.csv
10. fusion/fusion_candidate_batch01.md

任务：
只做台账同步和下一批派工，不写学生终稿。

必须更新：
- `COVERAGE_MATRIX.csv`：把 Batch01 涉及题目的 claudecode/worker/patcher/governor/fusion 状态从 running/not_started 更新为真实的 `completed_first_pass` / `batch01_candidate_with_fixes` / `not_promoted` 等保守状态。
- `SOURCE_LEDGER.csv` 或新增补充 ledger：把 worker_source_notes 已核读来源标成 P0/P2/user_confirmed_image_scoring_material 的本轮证据状态；保留旧路径仅作 locator。
- `00_control/PROGRESS_LEDGER.jsonl`：记录台账同步事件。

然后派发 Codex A Batch02 worker：
复核 `2026朝阳一模 Q20`、`2026顺义一模 Q20`、`2025海淀二模 Q21`、`2025海淀期末 Q22`，只写 worker/ 下的 Batch02 source notes 和 entries/blockers。禁止生成学生终稿、Word/PDF、coverage closed 或 FINAL_ACCEPTANCE PASS。
```

## 9. After Fusion Batch01 结论

Batch01 新增文件可读，ClaudeCode 已退出，25 个 fusion atoms 已形成；当前最大问题不是缺文件，而是控制台账没有同步真实进度。下一步应先同步 `COVERAGE_MATRIX.csv` / `SOURCE_LEDGER.csv` 的保守状态，再进入 Codex A Batch02 回源复核。

## 10. Codex Leader Sync Addendum

更新人：Codex leader

时间：2026-05-03 19:18 CST

自动化检测者指出的 `COVERAGE_MATRIX.csv` / `SOURCE_LEDGER.csv` stale 问题已经在检测报告之后修补：

- `COVERAGE_MATRIX.csv`：Batch01 行已更新为 `candidate_with_fixes`；Batch02 行已更新为 `source_locator_done_worker_batch02_running`。
- `SOURCE_LEDGER.csv`：Batch01 核读来源已同步为 P0 / P2 / user_confirmed_image_scoring_material 等保守状态；Batch02 locator 来源已同步为 locator-only 状态。
- `fusion/scoring_atom_table_batch01.csv`：新增 `source_ledger_refs` 回链列；新增 `BOUNDARY-B01` 记录 Q17 第二层分说2已看见但按模块边界排除。

这些修补仍不构成 coverage closed 或学生终稿放行。
