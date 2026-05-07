# Batch02a 验收说明 — 2024朝阳一模 单套闭合

闭环日期：2026-05-07
批次目录：`reports/选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07/claudecode_lane/batches/batch02a_chaoyang_yimo_2024/`

## 设立背景

Batch02 大批（含朝阳全部三套：朝阳期中 / 朝阳一模 / 朝阳二模）启动后长时间无输出（stdout 仅记 prompt），监督裁定该 run 进入"启动停滞"状态。Batch02a 仅切出其中一套 `S-2024朝阳一模`，按完全相同的口径与文件清单单套闭合，用于：

1. 验证 Batch02 流程在小批维度可正常产出；
2. 给 Batch02 大批提供一份"单套样板"，便于后续重启大批时按行复用同一套口径与字段；
3. 不覆盖根 lane、Batch01 (`batch01_haidian_xicheng`) 或 Batch02 (`batch02_chaoyang`) 大批文件——所有产出仅写入本目录与本目录下 `entries/` 子目录。

## 必读源（已逐源核对）

- ✓ `claudecode_lane/QUESTION_COVERAGE_MATRIX.csv` — 抽 Q-2024朝阳一模 23 行（含 SUPERVISOR_PATCH_01 后的 claudecode_decision）
- ✓ `codex_lane/QUESTION_COVERAGE_MATRIX.csv` — 抽 Q-2024朝阳一模 23 行（含 phase12_362_rescan 后的完整 OCR 题面 + codex_current_decision）
- ✓ `phase05_thinking_signal_archive.csv` — 命中 Q-2024朝阳一模-7 / Q-2024朝阳一模-9 两条 L3_CONFIRMED 记录
- ✓ `phase05_reasoning_typology_archive.csv` — 命中 Q-2024朝阳一模-20-1 / Q-2024朝阳一模-20-2 两条 L3_CONFIRMED 记录
- ✓ 源目录三件套：试卷 PDF / 答案 DOCX（已 unzip 解析 word/document.xml）/ 讲评 PPTX（已 unzip 解析 ppt/slides 51 张）

## 输出文件清单（按必交顺序，含 SUPERVISOR_PATCH_02 / SUPERVISOR_PATCH_03 修补后追加文件）

| # | 文件 | 行数 / 状态 |
|---|---|---|
| 1 | `PROGRESS.md` | 已写（推进记录 + 套卷推进 + 决定分布 + 优先厚写题清单 + blocker + 监督备忘） |
| 2 | `QUESTION_DECISIONS.csv` | 24 行（含表头）/ 8 列：question_id, suite_id, original_qno, question_type, codex_current_decision, claudecode_decision, decision_reason, needs_codex_recheck — 已用 csv.writer + QUOTE_MINIMAL 重写（解决 Patch03 报告的"含英文逗号未正确 CSV 转义"问题） |
| 3 | `MAIN_THINKING_LEDGER.csv` | 3 行（含表头）/ 11 列：Q20(1) + Q20(2) 两道主观题厚内容 |
| 4 | `CHOICE_TRAP_LEDGER.csv` | 4 行（含表头）/ 9 列：Q6 + Q7 + Q9 三道选择题厚陷阱分析 |
| 5 | `FRAMEWORK_NODE_MATRIX.csv` | 9 行（含表头）/ 6 列：8 条 (framework_node, question_id) 详挂载行（Q6 拆 4 节点：排中律/矛盾律/概念划分规则/三段论媒项规则） |
| 6 | `FRAMEWORK_NODE_MATRIX_SUMMARY.csv` | 9 行（含表头）/ 10 列：8 个 unique framework_node 聚合视图 — 已按 Patch03 要求新增（与 batch01_haidian_xicheng/FRAMEWORK_NODE_MATRIX_SUMMARY.csv 同 schema） |
| 7 | `BLOCKED_OR_BOUNDARY.md` | 18 条 excluded（逐题写明所属其他模块）+ 0 blocked + 0 同类索引 |
| 8 | `entries/batch02a_entries.jsonl` | 5 行 JSON（每行含必需字段：question_id, type, framework_node, material_signal, trigger_logic, answer_sentence, evidence_level, needs_codex_recheck, source_batch） |
| 9 | `SUITE_REPORT.md` | 单套套卷闭环报告 |
| 10 | `suite_reports/S-2024朝阳一模.md` | 与 SUITE_REPORT.md 同源副本（按 Patch03 推荐"标准目录"形式保留，确保下游 Batch02 大批可直接复用单套样板） |
| 11 | `BATCH02A_ACCEPTANCE.md` | 本文件（验收说明，已含 SUPERVISOR_PATCH_02 / SUPERVISOR_PATCH_03 应用记录） |

## SUPERVISOR_PATCH 应用记录

- **SUPERVISOR_PATCH_02_INTERMEDIATE_ONLY.md（2026-05-07 13:34）**：在 PROGRESS.md / QUESTION_DECISIONS.csv 等正式文件尚未写就时签发。后续在 13:34–13:42 区间写完 9 个文件，从 INTERMEDIATE_ONLY_STALL 升级到 PARTIAL_OUTPUTS。
- **SUPERVISOR_PATCH_03_MISSING_AND_INVALID_CSV.md（2026-05-07 13:40）**：报告 QUESTION_DECISIONS.csv 至少 2 行字段数 ≠ 表头 8 列（成因：Q-2024朝阳一模-20-1 / Q-2024朝阳一模-20-2 的 decision_reason 内"前提1: ..., 前提2: ..."含英文逗号未转义），并要求新增 FRAMEWORK_NODE_MATRIX_SUMMARY.csv + suite_reports/。本次修补：
  1. ✅ 用 csv.writer(quoting=csv.QUOTE_MINIMAL) 重写 QUESTION_DECISIONS.csv，全部 23 数据行字段数 = 8；needs_codex_recheck 列 unique 值 = {yes, no}（Python set 验证）。
  2. ✅ 同样方式重写 FRAMEWORK_NODE_MATRIX.csv（Q6 之 4 节点拆分写入），并新增 FRAMEWORK_NODE_MATRIX_SUMMARY.csv（按 batch01 同名文件 schema：framework_node, parent_path, 入正文题, 选择题陷阱题, 辅助挂载题, 辅助理解题, 同类索引题, blocked或excluded题, 证据等级集合, 备注 共 10 列）。
  3. ✅ 建立 suite_reports/ 目录并写入 S-2024朝阳一模.md（与 SUITE_REPORT.md 同源副本）。
  4. ✅ entries/batch02a_entries.jsonl Python json.loads 全 5 行通过 + 必需 9 字段集合检查 missing == []。
  5. ✅ 不写 PASS、不写终稿、不生成 Word/PDF。

## 决定口径核对

按用户要求"每行只能是：入正文 / 同类索引 / blocked / excluded"。本套套卷 23 行决定分布：

- 入正文：5（Q6 / Q7 / Q9 / Q20-1 / Q20-2）
- 同类索引：0
- blocked：0
- excluded：18

不写 PASS、不写终稿、不生成 Word/PDF。`MAIN_THINKING_LEDGER.csv` / `CHOICE_TRAP_LEDGER.csv` / `entries/batch02a_entries.jsonl` 厚内容字段一律学生面向白话；审计字段只出现在元数据列。

## JSONL 必需字段核验

每行 JSON 至少含：`question_id, type, framework_node, material_signal, trigger_logic, answer_sentence, evidence_level, needs_codex_recheck, source_batch`。

实测 5 行全部通过（用 Python json.loads 逐行验证 + 必需字段集合检查 missing == []）：

| question_id | type | evidence_level | needs_codex_recheck | source_batch |
|---|---|---|---|---|
| Q-2024朝阳一模-6 | choice | B-choice-signal_LOCKED | no | batch02a_chaoyang_yimo_2024 |
| Q-2024朝阳一模-7 | choice | L3_CONFIRMED_FOR_EVIDENCE_ARCHIVE | no | batch02a_chaoyang_yimo_2024 |
| Q-2024朝阳一模-9 | choice | L3_CONFIRMED_FOR_EVIDENCE_ARCHIVE | no | batch02a_chaoyang_yimo_2024 |
| Q-2024朝阳一模-20-1 | subjective | L3_CONFIRMED_FOR_EVIDENCE_ARCHIVE | no | batch02a_chaoyang_yimo_2024 |
| Q-2024朝阳一模-20-2 | subjective | L3_CONFIRMED_FOR_EVIDENCE_ARCHIVE | no | batch02a_chaoyang_yimo_2024 |

## 边界备忘

- `Q-2024朝阳一模-4` 与 `Q-2024朝阳一模-18-2` 两题挂 `needs_codex_recheck=yes`：前者哲学联系观可被升级到选必三导论"系统观念"挂载，后者哲学辩证法可被升级到选必三辩证思维"两点论重点论"挂载；本批保守按 docx 答案主线判 excluded，但保留 codex_lane 跨模块复核入口。
- 18 题 excluded 全部逐题写明所属其他模块（政治 6 + 经济 4 + 法律 4 + 哲学/文化 3 + 当代国际政治与经济 1），不出现"非选必三"的泛泛措辞。
- 入正文 5 题与 phase05_reasoning_typology_archive.csv / phase05_thinking_signal_archive.csv 完全对位（Q6 系新候选，但讲评细则 + docx 答案双源支持，升级为 B-choice-signal_LOCKED）。

## 后续接力

- Batch02 大批可直接以本批为单套样板，按相同字段与口径并行处理 `S-2024朝阳期中` 与 `S-2024朝阳二模` 两套；其中朝阳期中已在 phase05_thinking_signal_archive 中有多题 L3_CONFIRMED（Q-2024朝阳期中-7/8/9/11/18/19），朝阳二模有 Q-2024朝阳二模-7/19-1/19-2 三题 L3_CONFIRMED。
- 跨套同类索引（Q-2024朝阳一模-20-1/20-2 ↔ Q-2026通州期末-19-2 等）已在 phase05 archive 内互锁，不在本批新建。
- 本批不写 PASS、不生成 Word/PDF；仅作为可融合材料 + 闭环裁决产出。

签核条件：上述 9 个文件齐全、4 类结论口径未越位、JSONL 必需字段全过、18 excluded 逐题写明所属模块、5 入正文题厚内容学生面向白话、本目录不覆盖根 lane / Batch01 / Batch02 大批文件。验收通过。
