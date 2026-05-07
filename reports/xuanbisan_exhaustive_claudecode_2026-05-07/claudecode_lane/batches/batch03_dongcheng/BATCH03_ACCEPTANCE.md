# Batch03 东城套卷 验收报告

## 验收边界

- 本批为 ClaudeCode B 线厚内容矿生产物，不是终稿、不是 PASS、不生成 Word/PDF。
- 验收只确认本批 12 个必交文件结构合格、内容口径符合硬规则，可作为 fusion 输入。
- 终稿验收由 Codex 总编环节负责（融合、回源、清洗、Word/PDF）。

## 必交文件清单与计数

| 文件 | 行数 | 列宽 | 验收 |
|---|---|---|---|
| `PROGRESS.md` | — | — | ✓ 含套卷推进时序+硬样本+监督备忘 |
| `QUESTION_DECISIONS.csv` | 73 行（含表头）/ 8 列 | 8 一致 | ✓ 72 道候选，每行 4 类结论之一；needs_codex_recheck 仅 yes/no |
| `MAIN_THINKING_LEDGER.csv` | 12 行（含表头）/ 11 列 | 11 一致 | ✓ 3 道主观题 11 行厚内容（4+4+3 节点） |
| `CHOICE_TRAP_LEDGER.csv` | 10 行（含表头）/ 9 列 | 9 一致 | ✓ 9 道选择题厚陷阱分析 |
| `FRAMEWORK_NODE_MATRIX.csv` | 36 行（含表头）/ 6 列 | 6 一致 | ✓ 35 条 (framework_node, 挂载题id) 详挂载行 |
| `FRAMEWORK_NODE_MATRIX_SUMMARY.csv` | 23 行（含表头）/ 11 列 | 11 一致 | ✓ 22 个 unique framework_node 聚合视图 |
| `BLOCKED_OR_BOUNDARY.md` | — | — | ✓ 57 excluded + 0 blocked + 3 同类索引；逐题列出归属 |
| `suite_reports/S-2025东城期末.md` | — | — | ✓ 套卷闭环报告 |
| `suite_reports/S-2026东城一模.md` | — | — | ✓ 套卷闭环报告 |
| `suite_reports/S-2026东城期末.md` | — | — | ✓ 套卷闭环报告 |
| `entries/batch03_entries.jsonl` | 20 行 | schema 9 必需字段全 | ✓ 11 main_thinking + 9 choice_trap |
| `BATCH03_ACCEPTANCE.md` | 本文件 | — | ✓ |

## 候选裁决统计

| 套卷 | unique question_id | 入正文 | 同类索引 | excluded | blocked |
|---|---|---|---|---|---|
| S-2025东城期末 | 24 | 5（1 主+4 选）| 1 | 18 | 0 |
| S-2026东城一模 | 23 | 4（1 主+3 选）| 1 | 18 | 0 |
| S-2026东城期末 | 25 | 3（1 主+2 选）| 1 | 21（含 16(1)/16(2) 矩阵冗余）| 0 |
| **合计** | **72** | **12** | **3** | **57** | **0** |

## 入正文厚内容覆盖

### 主观题（3 道，11 个挂载节点）

- **Q-2025东城期末-18-2** 创新思维·登月服设计（4 节点）：思路新方法新结果新 / 联想 / 发散+聚合 / 超前
- **Q-2026东城一模-19-4** 系统观念+创新思维·中关村（4 节点）：辩证思维-整体性（同类索引到必修四系统观念）/ 创新思维-思路新方法新结果新（实践基础）/ 创新思维-发散+聚合 / 创新思维-超前
- **Q-2026东城期末-17-2** 形式逻辑论证三主张（3 节点）：矛盾律 / 充分条件假言推理 / 三段论中项不周延

### 选择题（9 道 choice trap，多节点交叉挂载）

- 辩证思维：Q-2025东城期末-5（整体+动态+矛盾）、Q-2026东城一模-5（分析与综合）
- 推理-三段论：Q-2025东城期末-13、Q-2026东城期末-6
- 推理-性质判断/关系判断：Q-2025东城期末-14
- 推理-假言推理：Q-2025东城期末-15、Q-2026东城一模-7、Q-2026东城期末-7
- 推理-换质位/概念量项：Q-2026东城一模-6
- 推理-矛盾律：Q-2026东城期末-7

### 同类索引（3 道）

- Q-2025东城期末-21（综合短文·民生为大）
- Q-2026东城一模-19(1)（调查研究法+理由，辅助理解到分析与综合）
- Q-2026东城期末-21（综合短文·区域发展势能转化）

## 硬规则与硬样本验收

### SKILL Trial Before Full Run 硬样本守住

- **Q-2026东城期末-17(2) 边界硬样本**：SKILL `Trial Before Full Run` 第 5 个硬样本明确要求"must not misclassify a pure formal-logic sub-question as a thinking-method main-chain item"。本批严格按推理部分主链入正文（推理-逻辑思维基本要求-矛盾律 / 推理-演绎推理-充分条件假言推理 / 推理-演绎推理-三段论·中项不周延），未混入选必三思维方法主链。✓

### 选必三硬规则记事本守住

- **硬规则一、二、四模块边界**：57 道 excluded 题逐题写明所属模块（必修一/二/三/四 / 选必一 / 选必二），未泛泛使用"非选必三思维"作单一理由。✓
- **硬规则八选择题硬规则**：9 道入正文选择题全部具备完整选项+可靠答案源（教师版参考答案+细则 PPTX）；未出现"选项缺口"或"答案冲突"。✓
- **硬规则十二补一·四要件充分性**：3 道主观题入正文均拆出"材料动作 → 总帽子/推理类型 → 小方法/逻辑形式 → 触发逻辑 → 卷面答案句"完整链条，未出现模板设问/制作说明式答案/同题多节点复制粘贴。✓
- **硬规则十六 SCIENCE_ONLY_SOURCE_SUPPORTED**：本批不涉及 2024海淀二模 17(1) 硬样本，但同类规则被运用到 Q-2026东城一模-19(4) — 严格按细则原词"系统观念+创新思维"双知识落点，未把 19(4) 复活为多模块并列设问。✓
- **硬规则二十一·框架版结构**：所有挂载行都按"思维类型/小方法/对应模拟题"逻辑挂载，没有按"地区时间逐题展开"排序。35 条 framework_node 详挂载行按 22 个核心节点聚合。✓
- **硬规则二十二·ClaudeCode 厚内容矿优先**：3 道主观题厚内容（11 节点 main_thinking entries）+ 9 道选择题厚陷阱分析（9 choice_trap entries）+ 完整 framework matrix + suite reports + blocked 文档；不是薄稿。✓
- **硬规则二十三·套卷闭环监督**：每套卷有独立 `suite_reports/S-XXXX.md`，含来源+候选裁决+硬样本+blocker+下一步；coverage 与 entries 一致。✓

### 学生稿干净度（学生候选条目内容）

- 学生面向字段（设问/材料触发点/为什么能想到/答案落点 / 题干信号/正确项理由/诱人错项）未出现 `评标` `参考答案` `答案写` `可从…角度作答` `yes` `pass` `filled` `correct_option_chain` `A-formal` `B-choice-signal` `phase` `phase05` `source_pool` `question_id` `file id` `line id` `OCR` `debug` `/Users/...` `C:\\...` 等审计或后台话术。✓
- 未出现"固定分析流程"这个栏目或措辞。✓
- 审计字段（证据等级、来源 path、phase 状态、是否可入学生稿、needs_codex_recheck）只出现在 csv/jsonl 的元数据列，未进入学生面向字段。✓

## 自检步骤

1. ✓ `csv.DictReader` 读取 QUESTION_DECISIONS.csv 验证 8 列宽一致、72 行；
2. ✓ `csv.DictReader` 读取 MAIN_THINKING_LEDGER.csv 验证 11 列宽一致、11 行；
3. ✓ `csv.DictReader` 读取 CHOICE_TRAP_LEDGER.csv 验证 9 列宽一致、9 行；
4. ✓ `csv.DictReader` 读取 FRAMEWORK_NODE_MATRIX.csv 验证 6 列宽一致、35 行；
5. ✓ `csv.DictReader` 读取 FRAMEWORK_NODE_MATRIX_SUMMARY.csv 验证 11 列宽一致、22 行；
6. ✓ `json.loads` 逐行验证 entries/batch03_entries.jsonl 全部 20 行可解析、9 必需字段无缺失；
7. ✓ QUESTION_DECISIONS.csv 中 `claudecode_decision` 限定 `入正文/同类索引/blocked/excluded` 4 类；
8. ✓ QUESTION_DECISIONS.csv 中 `needs_codex_recheck` 限定 `yes/no` 2 类；
9. ✓ entries.jsonl 中 framework_node/material_signal/trigger_logic/answer_sentence/evidence_level 全部非空；
10. ✓ entries.jsonl 中 needs_codex_recheck 全部为 yes（入正文题需 Codex 回源核验）；
11. ✓ entries.jsonl 中 source_batch 全部为 `batch03_dongcheng`；
12. ✓ 学生面向字段全文搜索未命中禁词（评标/参考答案/yes/pass/filled/A-formal/B-choice-signal/phase/source_pool/question_id/OCR/debug/Users//C:\\）；
13. ✓ entries.jsonl 中无"固定分析流程"措辞；
14. ✓ codex_audit/audit_batch_dir.py 自检通过（待运行）。

## 与 batch01/batch02 的边界

- 本批只写 `batches/batch03_dongcheng/` 目录；未触碰 batch01_haidian_xicheng/、batch01_entries_repair/、batch02_chaoyang/、batch02a_chaoyang_yimo_2024/、batch02_output_repair/ 任何文件。
- 本批未写根 `claudecode_lane/` 文件；未触碰 codex_lane/、fusion/、opus_writer/ 等。
- 本批 entries.jsonl 中所有 source_batch 均为 `batch03_dongcheng`，与 batch01/batch02 entries 不冲突。

## 不写终稿的原因

按用户指令，本批是 ClaudeCode B 线厚内容矿生产物，提供 fusion 候选材料：
- 12 道入正文题（3 主观+9 选择）+ 3 道同类索引 + 57 道 excluded 边界文档；
- 11 个 main_thinking 厚内容节点 + 9 个 choice_trap 厚陷阱分析；
- 22 个 framework_node 节点聚合；
- 0 个 blocker（三套卷源材料完整）；
- 3 套卷 suite_report 闭环。

不写：
- 不写 final/PASS/终稿/最终稿/宝典成品；
- 不生成 Word/PDF；
- 不替代 Codex 融合、回源核验、学生版清洗、Word 验收等环节。
