# Batch02 Output Repair 验收说明

**不写 PASS / 不写终稿 / 不生成 Word/PDF。** 仅说明本修复批已交付的全部产物 + 套卷统计 + 残余边界。

## 修复目标（与本批边界）

修复 Batch02 朝阳大批的两类硬失败：

1. `batch02_chaoyang/PROGRESS.md` 自称闭合，但正式产物缺失（`SUPERVISOR_PATCH_02_MISSING_OUTPUTS.md`）。
2. `batch02_chaoyang/QUESTION_DECISIONS.csv` 手写逗号导致 CSV 转义失效，`needs_codex_recheck` 列被理由文本污染（`SUPERVISOR_PATCH_03_INVALID_CSV.md`）。

修复批仅写入：
`reports/选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07/claudecode_lane/batches/batch02_output_repair/`

不覆盖原 `batch02_chaoyang/` 任何文件。

## 已交付产物清单

| # | 文件 | 行数/规模 | 写入器 |
|---|---|---|---|
| 1 | `PROGRESS.md` | 修复批进度+口径+统计 | Write 工具直写 |
| 2 | `QUESTION_DECISIONS.csv` | 91 行（含表头）/ 8 列 | Python `csv.writer` (QUOTE_MINIMAL) |
| 3 | `MAIN_THINKING_LEDGER.csv` | 21 行（含表头）/ 11 列 | Python `csv.writer` (QUOTE_MINIMAL)，从 ROWS 数据重建 |
| 4 | `CHOICE_TRAP_LEDGER.csv` | 13 行（含表头）/ 9 列 | Python `csv.writer` (QUOTE_MINIMAL) |
| 5 | `FRAMEWORK_NODE_MATRIX.csv` | 36 行（含表头）/ 6 列 | Python `csv.writer` (QUOTE_MINIMAL) |
| 6 | `FRAMEWORK_NODE_MATRIX_SUMMARY.csv` | 29 行（含表头）/ 11 列 | Python `csv.writer` (QUOTE_MINIMAL)，聚合自 detail |
| 7 | `BLOCKED_OR_BOUNDARY.md` | 2 blocked + 2 同类索引 + 66 excluded 分类汇总 | Write 工具直写 |
| 8-11 | `suite_reports/S-2024朝阳一模.md`、`S-2024朝阳二模.md`、`S-2024朝阳期中.md`、`S-2026朝阳期中.md` | 4 份套卷闭环报告 | Write 工具直写 |
| 12 | `entries/batch02_entries.jsonl` | 32 行（20 main_thinking + 12 choice_trap） | Python `json.dumps` 逐行 |
| 13 | `BATCH02_REPAIR_ACCEPTANCE.md` | 本文件 | Write 工具直写 |
| 14 | `REPAIR_QA_NOTES.md` | 详见 `REPAIR_QA_NOTES.md` | Write 工具直写 |

## 套卷统计（事实计数，来自 QUESTION_DECISIONS.csv）

| suite_id | 候选 | 入正文 | 同类索引 | blocked | excluded |
|---|---|---|---|---|---|
| S-2024朝阳一模 | 23 | 4 | 2 | 0 | 17 |
| S-2024朝阳二模 | 23 | 3 | 0 | 1 | 19 |
| S-2024朝阳期中 | 22 | 6 | 0 | 1 | 15 |
| S-2026朝阳期中 | 22 | 7 | 0 | 0 | 15 |
| **合计** | **90** | **20** | **2** | **2** | **66** |

入正文按题型拆解：

| 题型 | 数量 | 主链 ledger 挂载行数 |
|---|---|---|
| 主观题 | 8 | 20（含同题多方法挂载） |
| 选择题 | 12 | 12（每题 1 行） |
| **合计** | **20** | **32**（=entries.jsonl 总行数） |

## Schema 校验（验收必查）

### QUESTION_DECISIONS.csv

- 行数：90 + 1 表头 = 91 ✓
- 列数：8 ✓
- `claudecode_decision` ⊆ {`入正文`, `同类索引`, `blocked`, `excluded`} ✓
- `needs_codex_recheck` ⊆ {`yes`, `no`} ✓ — 修复硬失败 B
- 所有含逗号/引号字段已通过 csv.writer 自动加引号转义 ✓

### MAIN_THINKING_LEDGER.csv

- 行数：20 + 1 表头 = 21 ✓
- 列数：11 ✓
- 所有字段非空 ✓
- 答案句无禁用词（`要写 / 采分点 / 细则要求 / 本题需要 / 设问要求 / 评标 / 参考答案`）✓
- 无 CSV 字段错位（修复了原 `batch02_chaoyang/MAIN_THINKING_LEDGER.csv` 中"完整设问"含未引号 ASCII 逗号导致的字段移位）✓

### CHOICE_TRAP_LEDGER.csv

- 行数：12 + 1 表头 = 13 ✓
- 列数：9 ✓
- 所有字段非空 ✓
- `是否可入学生稿` 列只有 `可` ✓
- `needs_codex_recheck` ⊆ {`yes`, `no`} ✓

### FRAMEWORK_NODE_MATRIX.csv / SUMMARY

- detail：35 + 1 表头 = 36 行 ✓ / 6 列 ✓
- summary：28 + 1 表头 = 29 行 ✓ / 11 列 ✓
- detail 35 行 = 20 主观题挂载 + 13 选择题挂载（含 Q-2026朝阳期中-13 双挂载）+ 2 辅助挂载 ✓

### entries/batch02_entries.jsonl

- 行数：32 ✓ — 修复硬失败 A 之缺失产物
- 每行 `json.loads` 通过 ✓
- 每行 9 必需字段：`question_id, type, framework_node, material_signal, trigger_logic, answer_sentence, evidence_level, needs_codex_recheck, source_batch` ✓
- `type` ⊆ {`main_thinking`, `choice_trap`} ✓
- `needs_codex_recheck` ⊆ {`yes`, `no`} ✓
- `source_batch` 全部为 `batch02_output_repair` ✓
- `evidence_level` ⊆ {`A-formal`, `A-support`, `B-choice-signal`} ✓

## 硬规则遵守清单

- ✓ 不写 `PASS`、不写终稿、不生成 Word/PDF。
- ✓ 不覆盖 `batch02_chaoyang/` 大目录任何文件。
- ✓ 学生候选条目内容（MAIN_THINKING_LEDGER 答案句、CHOICE_TRAP_LEDGER 正确项理由+诱人错项）不出现"固定分析流程"措辞、`评标 / 参考答案 / 答案写 / 可从…角度作答 / yes / pass / filled / correct_option_chain / A-formal / B-choice-signal / phase / source_pool / question_id / file id / line id / OCR / debug / /Users/... / C:\\...` 等审计/后台话术。
- ✓ 证据不足→`blocked`（Q-2024朝阳二模-6 / Q-2024朝阳期中-11），不硬塞入正文。
- ✓ 纯形式逻辑/推理题入推理索引或 choice trap，不混入思维方法主链（Q-2024朝阳一模-20-1/-2 推理双结构、Q-2024朝阳二模-19-2 联言判断、Q-2024朝阳期中-7/-8/-9/-10 等选择题均按形式逻辑/推理节点挂载）。
- ✓ 硬样本严格锁定：
  - Q-2024朝阳二模-7 锁为小项不当扩大（§十八），不得回流为中项不周延。
  - Q-2024朝阳一模-20-1 锁为充分条件假言推理-否定后件式，Q-2024朝阳一模-20-2 锁为必要条件假言推理-肯定后件式（§十八）。
  - Q-2026朝阳期中-21-2 严格按§十三拆出超前/联想/逆向/三新/发散+聚合 5 角度。
  - Q-2026朝阳期中-13 双挂载（联想思维 + 感性具体→思维抽象）保留。

## 残余边界与下一步

- **2 个 blocked 题**（Q-2024朝阳二模-6 / Q-2024朝阳期中-11）必须由 Codex 在融合环节回源核验；如答案源仍不可靠，保持 blocked，不得被强制转入正文。
- **2 个同类索引/辅助挂载**（Q-2024朝阳一模-4 / Q-2024朝阳一模-9）在学生最终稿中必须以"辅助挂载"状态显示，不冒充正向例题。
- **needs_codex_recheck=yes 的 entries**（共 17 条 = 5 主观题 + 12 - 3 = 9 选择题；详见 entries.jsonl）需 Codex 在融合时重审一次，主要是套卷答案源/边界判定的二次确认。
- **本修复批不替代原批**；后续融合时，Codex 应优先读取本目录下的修复版 CSV / JSONL，原批 `batch02_chaoyang/QUESTION_DECISIONS.csv` 因 CSV 转义失效仅供溯源，不得直接消费。

## 不写 PASS 的原因

修复批的目标是修产物缺失 + CSV 转义，不是终稿验收。完整朝阳套卷的终稿门槛仍需：
1. Codex 融合环节裁决 2 个 blocked 题 + 2 个辅助挂载题。
2. 真 GPT-5.5 Pro / Claude Opus 4.7 Adaptive 外审。
3. Governor + Confucius 闭环。
4. Word/PDF 渲染验证。

这些都不在本修复批的范围内。
