# Batch01 Entries Repair Report

修补范围：仅生成 `batch01_entries.jsonl`，不重跑 Batch01，不覆盖 `batch01_haidian_xicheng/` 下任何已有文件。

## 一、产出

- `batch01_entries.jsonl`
  - 总条目数：**31**
    - `main_thinking`：**20**（来自 MAIN_THINKING_LEDGER.csv 的 20 行）
    - `choice_trap`：**11**（来自 CHOICE_TRAP_LEDGER.csv 的 11 行）
  - 编码：UTF-8，每行一个 JSON 对象，使用 `ensure_ascii=False`

## 二、字段映射

### 2.1 main_thinking（来源：MAIN_THINKING_LEDGER.csv，11 列）

| JSONL 字段 | 源 CSV 字段 | 备注 |
|---|---|---|
| `question_id` | `question_id` | 直接映射 |
| `type` | — | 常量 `"main_thinking"` |
| `framework_node` | `框架落点` | 直接映射 |
| `material_signal` | `材料动作` | 中文含义映射（材料给出的动作/事实信号） |
| `trigger_logic` | `触发逻辑` | 直接映射 |
| `answer_sentence` | `答案句` | 直接映射 |
| `evidence_level` | `证据等级` | 直接映射 |
| `needs_codex_recheck` | （非本表字段） | 跨引用 `QUESTION_DECISIONS.csv[needs_codex_recheck]`，按 `question_id` 查表 |
| `source_batch` | — | 常量 `"batch01_haidian_xicheng"` |

源 CSV 中存在但未进入 JSONL 的字段（按要求只输出指定 schema）：
- `来源`、`完整设问`、`总帽子`、`小方法`、`题型标签`

### 2.2 choice_trap（来源：CHOICE_TRAP_LEDGER.csv，8 列）

| JSONL 字段 | 源 CSV 字段 | 备注 |
|---|---|---|
| `question_id` | `question_id` | 直接映射 |
| `type` | — | 常量 `"choice_trap"` |
| `framework_node` | `陷阱类型` | 中文含义映射；源表无 `框架落点` 列，`陷阱类型` 是最接近的"框架定位"语义。如需规范化的框架节点，参见 `FRAMEWORK_NODE_MATRIX.csv` |
| `material_signal` | `题干信号` | 直接映射 |
| `trigger_logic` | **（源表无对应字段）** | 留空 |
| `answer_sentence` | `正确项理由` | 中文含义映射（说明正确项理由 = 答案陈述） |
| `evidence_level` | **（源表无对应字段）** | 留空 |
| `needs_codex_recheck` | （非本表字段） | 跨引用 `QUESTION_DECISIONS.csv[needs_codex_recheck]`，按 `question_id` 查表 |
| `source_batch` | — | 常量 `"batch01_haidian_xicheng"` |

源 CSV 中存在但未进入 JSONL 的字段：
- `完整选项或选项单位`、`答案源`、`诱人错项`、`是否可入学生稿`

## 三、缺字段清单（按要求只列出，不编造）

### 3.1 choice_trap 全部 11 条均存在的缺字段

- `trigger_logic`：CHOICE_TRAP_LEDGER.csv 没有"触发逻辑"列。诱人错项分析（`诱人错项` 列）虽含识别陷阱的判断逻辑，但与 `trigger_logic` 的 main_thinking 语义（识别正解的触发依据）不完全等价，故不强行映射，留空。
- `evidence_level`：CHOICE_TRAP_LEDGER.csv 没有"证据等级"列。`FRAMEWORK_NODE_MATRIX.csv` 中这 11 个 `question_id` 的相关挂载行均为 `B-choice-signal`，但矩阵存在一题多挂载情形，未直接写入 JSONL，留空。

### 3.2 main_thinking 无缺字段

MAIN_THINKING_LEDGER.csv 的 20 行全部 6 个核心字段（框架落点、材料动作、触发逻辑、答案句、证据等级、question_id）齐全。

### 3.3 needs_codex_recheck 跨表查找结果

- 20 条 main_thinking、11 条 choice_trap 的 `question_id` **全部命中** `QUESTION_DECISIONS.csv`，无 missing。
- `yes` 命中：Q-2024海淀二模-5（choice_trap）、Q-2025海淀期末-5（choice_trap）。
- 其余 29 条 `needs_codex_recheck = "no"`。

## 四、解析备注

- `QUESTION_DECISIONS.csv` 共 101 行（去表头），全部按 8 列正确解析。
- `MAIN_THINKING_LEDGER.csv` 共 20 行（去表头），全部按 11 列正确解析（长字段 `完整设问` `材料动作` `触发逻辑` 在源中已用 `"..."` 包裹）。
- `CHOICE_TRAP_LEDGER.csv` 共 11 行（去表头），全部按 8 列正确解析。源表在内嵌长文本中以中文中点 `·`（U+00B7）替代英文逗号，避开了 CSV 转义问题；JSONL 原样保留。
- 解析器内置了"中间列折叠"兜底（针对未引用的列内逗号），本次实际触发次数：QUESTION_DECISIONS=0、MAIN_THINKING=0、CHOICE_TRAP=0。

## 五、未覆盖项（按本次任务范围）

- `BLOCKED_OR_BOUNDARY.md` 中的 `excluded` / `blocked` / `同类索引` 题目不进入本 JSONL（这些题不是 main_thinking、也不是 choice_trap）。
- `FRAMEWORK_NODE_MATRIX.csv` 仅作为本次跨引用候选源，未单独落 JSONL 节点条目。
- `Q-2025海淀二模-UNPARSED-PAPER`：suite-level visual blocker，未在两份 ledger 中出现，故不在 JSONL 内。

## 六、生成器

- `_repair_run.py`（本目录内）：可重跑、幂等。重跑会覆盖 `batch01_entries.jsonl`，不影响 `batch01_haidian_xicheng/` 任何文件。
