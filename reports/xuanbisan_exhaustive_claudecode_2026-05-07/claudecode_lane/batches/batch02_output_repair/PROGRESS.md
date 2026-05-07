# Batch02 朝阳套卷正式产物修复 PROGRESS

## 启动 — 2026-05-07

修复批边界：本批仅修复 Batch02 朝阳大批的两类硬失败，不覆盖原 `batch02_chaoyang/` 大目录下的任何文件。本批所有产物只写入：

`reports/选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07/claudecode_lane/batches/batch02_output_repair/`

## 失败审计（来自原 batch02_chaoyang）

### 失败 A：PROGRESS.md 自称闭合，正式产物缺失

`batch02_chaoyang/PROGRESS.md` 第 33-40 行写了 4 套套卷"闭合"+89 unique rows，第 91-104 行罗列了"最终交付清单"，但落盘只有 `QUESTION_DECISIONS.csv` 与 `MAIN_THINKING_LEDGER.csv`，缺：

- `CHOICE_TRAP_LEDGER.csv`
- `FRAMEWORK_NODE_MATRIX.csv`
- `FRAMEWORK_NODE_MATRIX_SUMMARY.csv`
- `BLOCKED_OR_BOUNDARY.md`
- `suite_reports/*.md`
- `entries/batch02_entries.jsonl`
- `BATCH02_ACCEPTANCE.md`

证据：`SUPERVISOR_PATCH_02_MISSING_OUTPUTS.md` 第 6-15 行 + 当前目录文件列表。

### 失败 B：QUESTION_DECISIONS.csv 转义失效

`batch02_chaoyang/QUESTION_DECISIONS.csv` 表头 8 列正确，但 `decision_reason` 列含大量英文逗号且未加 CSV 引号，导致解析时 `decision_reason` 被切断、`needs_codex_recheck` 列被理由文本污染。证据：

- 典型污染行：Q-2024朝阳一模-6 / Q-2024朝阳一模-20-1 / Q-2024朝阳二模-2 / Q-2024朝阳期中-7 / Q-2026朝阳期中-12 等。
- `SUPERVISOR_PATCH_03_INVALID_CSV.md` 第 7-14 行明确锁定 `INVALID_CSV_QUOTING`。

## 修复策略（max-effort + adaptive-thinking）

1. **审计**：先逐行核对原 `batch02_chaoyang/QUESTION_DECISIONS.csv` 89 unique rows 的 8 列字段；提取 `question_id, suite_id, original_qno, question_type, codex_current_decision, claudecode_decision, decision_reason, needs_codex_recheck` 的真实数据。
2. **结构化写入**：所有 CSV 一律用 Python `csv.writer` 写入（`QUOTE_MINIMAL`），不再手写逗号拼接；带逗号、引号、换行的字段自动加双引号转义。
3. **强制约束**：
   - `needs_codex_recheck` 只允许 `yes` / `no`，不得出现理由文本；
   - `claudecode_decision` 只允许 `入正文 / 同类索引 / blocked / excluded`；
   - `decision_reason` 完整保留原证据理由，不因修 CSV 截断。
4. **逐套补齐**：依据原批 `MAIN_THINKING_LEDGER.csv`（已存在且 csv.writer 写入）+ 原批 `PROGRESS.md` "优先厚写题清单"，重建：
   - `MAIN_THINKING_LEDGER.csv`（继承原 20 行内容，schema 不变）
   - `CHOICE_TRAP_LEDGER.csv`（12 道选择题厚陷阱，9 列）
   - `FRAMEWORK_NODE_MATRIX.csv`（详挂载行）
   - `FRAMEWORK_NODE_MATRIX_SUMMARY.csv`（聚合视图）
   - `BLOCKED_OR_BOUNDARY.md`（2 blocked + 2 同类索引 + 65 excluded 分类汇总）
   - `suite_reports/S-2024朝阳一模.md`、`S-2024朝阳二模.md`、`S-2024朝阳期中.md`、`S-2026朝阳期中.md`
   - `entries/batch02_entries.jsonl`（每条厚内容一行 JSON，含 9 必需字段）
5. **自检**：CSV 行数 / 列数 / 引号闭合 / JSONL 每行 `json.loads` 通过 / `needs_codex_recheck` 限定值审计。

## 修复范围（与硬规则锁定）

| suite_id | 候选行数 | 入正文 | 同类索引 | blocked | excluded |
|---|---|---|---|---|---|
| S-2024朝阳一模 | 23 | 4 (Q6/Q7/Q20-1/Q20-2) | 2 (Q4/Q9) | 0 | 17 |
| S-2024朝阳二模 | 23 | 3 (Q7/Q19-1/Q19-2) | 0 | 1 (Q6) | 19 |
| S-2024朝阳期中 | 22 | 6 (Q7/Q8/Q9/Q10/Q18/Q19) | 0 | 1 (Q11) | 15 |
| S-2026朝阳期中 | 22 | 7 (Q11/Q12/Q13/Q14/Q15/Q20/Q21-2) | 0 | 0 | 15 |
| 合计 | 90 | 20 | 2 | 2 | 66 |

注：
- 原 `batch02_chaoyang/PROGRESS.md` 第 108 行写"候选总数 89"，但实际 CSV 含 90 行 question_id（S-2024朝阳二模 含 23 个 question_id：Q1-15 + Q16-1/Q16-2 + Q17 + Q18 + Q19-1/Q19-2/Q19-3 + Q20）。修复批以实际数据为准。
- S-2024朝阳期中 Q19 1 个 question_id → ledger 4 个挂载点；S-2026朝阳期中 Q20 1 个 question_id → ledger 4 个挂载点；S-2026朝阳期中 Q21-2 1 个 question_id → ledger 5 个挂载点。20 = 入正文 question_id 总数（含 8 主观题 + 12 选择题）。
- MAIN_THINKING_LEDGER 行数 = 20 个挂载行（8 主观题 question_id, 含同题多方法挂载）；CHOICE_TRAP_LEDGER 行数 = 12 行（12 道选择题，每题 1 行）；FRAMEWORK_NODE_MATRIX 行数 = 35 行（详挂载，含 2 辅助挂载）；FRAMEWORK_NODE_MATRIX_SUMMARY 行数 = 28 行（unique framework_nodes）。

## 硬样本锁定（从原批继承）

- `Q-2024朝阳一模-20(1)` 充分条件假言推理-否定后件式（§十八硬样本）。
- `Q-2024朝阳一模-20(2)` 必要条件假言推理-肯定后件式（§十八硬样本）。
- `Q-2024朝阳二模-7` 三段论小项不当扩大；选项 A "娱乐工具都是思想政治教育的工具" — 小项"娱乐工具"前提中不周延、结论中扩大；不得回流为中项不周延（§十八硬样本）。
- `Q-2024朝阳期中-18` 楚王不完全归纳/轻率概括 + 晏子类比推理（双知识点）。
- `Q-2024朝阳期中-19` 创新思维多角度（超前/逆向/联想/发散+聚合）。
- `Q-2026朝阳期中-20` 辩证思维多角度（矛盾分析法/分析与综合/质量互变/动态性）。
- `Q-2026朝阳期中-21(2)` 创新思维多角度（超前/联想/逆向/三新/发散+聚合）— §十三试跑硬样本。

## 修复执行节拍

| step | 文件 | 写入器 | 状态 |
|---|---|---|---|
| 1 | `PROGRESS.md` | Write 工具直写 | 完成 |
| 2 | `QUESTION_DECISIONS.csv` | Python `csv.writer` (QUOTE_MINIMAL) | 完成 |
| 3 | `MAIN_THINKING_LEDGER.csv` | Python `csv.writer` (继承原 20 行) | 完成 |
| 4 | `CHOICE_TRAP_LEDGER.csv` | Python `csv.writer` | 完成 |
| 5 | `FRAMEWORK_NODE_MATRIX.csv` | Python `csv.writer` | 完成 |
| 6 | `FRAMEWORK_NODE_MATRIX_SUMMARY.csv` | Python `csv.writer` | 完成 |
| 7 | `BLOCKED_OR_BOUNDARY.md` | Write 工具直写 | 完成 |
| 8 | `suite_reports/*.md` (4 份) | Write 工具直写 | 完成 |
| 9 | `entries/batch02_entries.jsonl` | Python `json.dumps` 逐行 | 完成 |
| 10 | `BATCH02_REPAIR_ACCEPTANCE.md` | Write 工具直写 | 完成 |
| 11 | `REPAIR_QA_NOTES.md` | Write 工具直写 | 完成 |
| 12 | schema/行数自检 | Python 脚本 | 完成 |

## 输出硬规则（再次声明）

- ✓ 不写 `PASS`、不写终稿、不生成 Word/PDF。
- ✓ 不覆盖 `batch02_chaoyang/` 大目录任何文件。
- ✓ `QUESTION_DECISIONS.csv` 的 `needs_codex_recheck` 只允许 `yes/no`。
- ✓ `entries/batch02_entries.jsonl` 每行合法 JSON，含 9 字段：`question_id, type, framework_node, material_signal, trigger_logic, answer_sentence, evidence_level, needs_codex_recheck, source_batch`。
- ✓ 学生候选厚内容不出现"固定分析流程"措辞。
- ✓ 证据不足→`blocked`，不硬塞入正文。
- ✓ 纯形式逻辑/推理题入推理索引/choice trap，不混入思维方法主链。
- ✓ 学生候选条目正文不出现 `评标 / 参考答案 / 答案写 / 可从…角度作答 / yes / pass / filled / correct_option_chain / A-formal / B-choice-signal / phase / source_pool / question_id / file id / line id / OCR / debug / /Users/... / C:\\...` 等审计/后台话术。

## 监督备忘

- 本批是 Batch02 输出修复批，不重新做证据裁决；裁决结论沿用 `batch02_chaoyang/` 已锁定的 4 类口径（入正文/同类索引/blocked/excluded）。
- 所有 CSV 必须能被 `csv.DictReader` 正确解析，且 `needs_codex_recheck` 字段唯一值集合 ⊆ {`yes`, `no`}。
- 修复批不替代原批；后续融合时，Codex 应优先读取本目录下的修复版 CSV / JSONL，原批的破损 CSV 仅供溯源。

## 关于 SUPERVISOR_PATCH_01_SELF_CLAIMED_NO_OUTPUTS.md

监督进程在 2026-05-07 13:44 写入了 `SUPERVISOR_PATCH_01_SELF_CLAIMED_NO_OUTPUTS.md`，反映当时只有 `PROGRESS.md` 落盘、其余 13 个文件缺失的中间状态。该 patch 已在后续逐步写入 13 个产物（CSV/JSONL/MD）后被解决。

完整自检日志写入了 `REPAIR_QA_NOTES.md` 第七节（复查命令），监管者可重跑验证：
- QUESTION_DECISIONS.csv: 90 rows × 8 cols ✓
- MAIN_THINKING_LEDGER.csv: 20 rows × 11 cols ✓
- CHOICE_TRAP_LEDGER.csv: 12 rows × 9 cols ✓
- FRAMEWORK_NODE_MATRIX.csv: 35 rows × 6 cols ✓
- FRAMEWORK_NODE_MATRIX_SUMMARY.csv: 28 unique nodes × 11 cols ✓
- entries/batch02_entries.jsonl: 32 valid JSON entries ✓
- 4 个 suite_reports + BLOCKED_OR_BOUNDARY + BATCH02_REPAIR_ACCEPTANCE + REPAIR_QA_NOTES 全部写出 ✓
- needs_codex_recheck 列唯一值 = {yes, no} ✓ — 修复硬失败 B
- 14 个必交文件全部存在 ✓ — 修复硬失败 A
