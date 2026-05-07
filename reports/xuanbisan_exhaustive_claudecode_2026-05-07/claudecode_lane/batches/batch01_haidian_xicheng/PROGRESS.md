# Batch01 海淀/西城 穷尽闭合 PROGRESS

## 启动 — 2026-05-07

任务边界：本批只处理 5 套海淀/西城套卷的全部候选题，按用户穷尽口径产出 4 类结论 (`入正文 / 同类索引 / blocked / excluded`)，并对可融合题写厚内容。不写终稿、不写 PASS、不生成 Word/PDF。

控制源已读：

- `codex_lane/CODEX_EXHAUSTIVE_DECISION_MATRIX.csv` (535 行) — 抽出本批候选 122 行；其中 65 行为 phase05 evidence-archive (B-choice / A-formal) + 同类索引镜像；57 行为 blocked/excluded 主行。
- `codex_lane/CODEX_EXHAUSTIVE_CANONICAL_DECISION_MATRIX.csv` (363 行) — 与上行重叠后保留的最终主行。
- `codex_lane/CODEX_SIGNAL_CLOSURE_MATRIX.csv` (74 行) — 信号闭合主行；本批所属信号已逐套 cross-check。
- `phase12_362_control_base_rescan_matrix.csv`、`phase12_expanded_body_FROM_362_control_matrix.csv`、`phase05_thinking_signal_archive.csv`、`phase05_reasoning_typology_archive.csv` — 用于补侧线信号/同类索引证据。

硬规则记事本已读：

- `feige-politics-garden/SKILL.md` 共有规则 + ClaudeCode 厚内容矿优先 (二十二、二十三)。
- `feige-politics-garden-xuanbisan/SKILL.md` 选必三流程与硬样本。
- `feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md` 二十一 (框架版结构)、二十二 (复盘)、二十三 (套卷闭环监督)。
- 本 run 小本本 (穷尽口径、528 行控制基底、73 行思维信号矩阵)。

## 套卷推进

| suite_id | 候选行数 | 已扫源文件 | 已读细则 | 已读试卷 | 状态 |
|---|---|---|---|---|---|
| S-2024海淀二模 | 24 | ✓ | ✓ 227192d22e10241b（028细则） | ✓ 027_海淀二模 完整文本 | 闭合 |
| S-2024西城一模 | 26 | ✓ | ✓ f7bcf000f212cc69（025细则） | ✓ 024_西城一模 完整文本+表格 | 闭合 |
| S-2025海淀二模 | 4（12/13/20+UNPARSED） | ✓ | ✓ fc56fdd304fde118（009/010/011细则一致） | ✓ render page_04/page_07 + supplemental answer source page9 | 闭合（suite-level visual blocker 标注 UNPARSED-PAPER 留待 OCR） |
| S-2025海淀期末 | 23 | ✓ | ✓ 4b22b6c78aaddb3e（015细则 pptx 12421 字） | ✓ b960993a71bd93ca + CHOICE-01_extracts 完整试卷 | 闭合 |
| S-2025西城二模 | 24 | ✓ | ✓ cfb0f19ef38aafd7（037细则） | ✓ 06c08602a2f5c20b 完整试卷+答案 | 闭合 |

## 优先厚写题 (已确认证据等级)

### 已锁定为入正文 (A-formal / B-choice-signal / L4)

- Q-2024海淀二模-17(1) — A-formal — 028 海淀二模细则 — 时间利用调查 — `SCIENCE_ONLY_SOURCE_SUPPORTED` 锁定 (按 17 锁定，不复活三模块设问)。
- Q-2024海淀二模-17(2) — A-formal — 同上 — 思维抽象/思维具体 (调查了解阶段 vs 分析研究阶段 = 感性具体 -> 思维抽象 -> 思维具体)。
- Q-2025海淀期末-17(1) — 待读细则确认 — 进入正文。
- Q-2025海淀期末-18 — 待读细则确认 — 进入正文。
- Q-2025西城二模-16(2) — A-formal — L4_LOCKED_FOR_FUSION — 待读西城二模细则。
- Q-2025西城二模-16(3) — A-formal — L4_LOCKED_FOR_FUSION — 同上。
- Q-2024西城一模-19(2)/19(3)/19(5) — A-formal — 待读 f7bcf000f212cc69。
- Q-2025海淀二模-20 — A-formal — L4_LOCKED_FOR_FUSION — 辩证思维复合题硬样本 (分析综合/整体性/动态性/辩证否定)。
- Q-2025海淀二模-12/13 — B-choice-signal — render page_04 已确认 — 待 render 选项细节。
- Q-2025西城二模-6 — B-choice-signal — body_after_362_repair (新候选) — 待选项还原。

## 已识别 blocker

- Q-2025海淀二模-UNPARSED-PAPER — 试卷 PDF 文本层稀薄；本批以 supplemental render + 老 thinking_signal_archive 作为映射基础，仅对题号 12/13/20 三题入正文；其他题号无可靠入选证据。
- 大批选择题为 visual_missing — 选项未完整识别；本批不会硬塞入正文，仅在选项确实可还原 (DOCX XML / render / 已 lock 的 phase05 archive) 时才入正文。

## 下一步（已完成）

1. ✓ 读 2024 西城一模、2025 海淀期末、2025 西城二模、2025 海淀二模 4 份细则 + 试卷（5 套全部读到细则 + 试卷文本，含表格/选项）。
2. ✓ 抽 phase05 thinking_signal_archive 与 reasoning_typology_archive 中本批套卷信号。
3. ✓ 展开 QUESTION_DECISIONS.csv（共 101 行候选；header 8 列、CSV 验证通过）。
4. ✓ 厚写 13 道优先题以及 6 道延伸题（共 20 行 MAIN_THINKING_LEDGER + 11 行 CHOICE_TRAP_LEDGER + 31 行 entries.jsonl）。
5. ✓ 写 5 套 suite_reports + framework matrix（45 行节点挂载）+ blocked 文档。

## 最终交付清单

| 文件 | 行数 | 说明 |
|---|---|---|
| `PROGRESS.md` | 本文件 | 套卷闭环+推进记录（不写 PASS） |
| `QUESTION_DECISIONS.csv` | 102 行（含表头）/ 8 列 | 每个候选题给出 `入正文/同类索引/blocked/excluded` 结论与理由；列：question_id, suite_id, original_qno, question_type, codex_current_decision, claudecode_decision, decision_reason, needs_codex_recheck |
| `MAIN_THINKING_LEDGER.csv` | 21 行（含表头）/ 11 列 | 10 道主观题厚内容、20 个挂载节点；列：question_id, 来源, 完整设问, 材料动作, 总帽子, 小方法, 触发逻辑, 答案句, 证据等级, 框架落点, 题型标签 |
| `CHOICE_TRAP_LEDGER.csv` | 12 行（含表头）/ 9 列 | 11 道选择题厚陷阱分析；列：question_id, 题干信号, 完整选项或选项单位, 答案源, 正确项理由, 诱人错项, 陷阱类型, 是否可入学生稿, needs_codex_recheck |
| `FRAMEWORK_NODE_MATRIX.csv` | 46 行（含表头）/ 6 列 | 45 条 (framework_node, 挂载题id) 详挂载行 |
| `FRAMEWORK_NODE_MATRIX_SUMMARY.csv` | 34 行（含表头）/ 11 列 | 33 个 unique framework_node 的聚合视图，列：framework_node, parent_path, 入正文题, 选择题陷阱题, 辅助挂载题, 辅助理解题, 同类索引题, blocked题, excluded题, 证据等级集合, 备注 |
| `BLOCKED_OR_BOUNDARY.md` | — | 79 条 excluded + 1 条 suite-level blocked + 2 条同类索引边界，逐题写明所属其他模块 |
| `suite_reports/` | 5 个 .md | 每套套卷一份闭环报告 |
| `entries/batch01_entries.jsonl` | 31 行 | 每条厚内容一行 JSON（subjective + choice 两类，每行含 question_id, type, framework_node, material_signal, trigger_logic, answer_sentence, evidence_level, needs_codex_recheck, source_batch + 中文 alias 字段；JSONL 语法+必需字段全部验证通过） |

## 套卷统计

- 候选总数：101 题（去重后）
- 入正文：18 题（5 道 2024海淀二模 + 5 道 2024西城一模 + 3 道 2025海淀二模 + 5 道 2025海淀期末 + 4 道 2025西城二模 = 22；去掉与多挂载共用题数后实际 question_id = 22 — 注：MAIN_THINKING_LEDGER 主观题 `入正文` 10 个 + CHOICE_TRAP_LEDGER 选择题 `入正文` 11 个 + Q-2024海淀二模-5 同时进 main/choice 两边作 choice = 实际 unique 入正文 question_id 22 个；与 QUESTION_DECISIONS.csv 中 `入正文` 决定相同 18 行的差距 = 主观+选择共 22 但 csv 行 = 18 因部分多子题合并表述）
- 同类索引：2 题（Q-2024海淀二模-21 综合短文 + Q-2025海淀期末-22 综合短文 含质量互变规律节点 fusion-only attach）
- blocked：1 个 suite-level（Q-2025海淀二模-UNPARSED-PAPER） + 1 个矩阵冗余项（Q-2024海淀二模-19(2)实际无子题，标 excluded 闭合）
- excluded：79 题（逐题列出所属模块；非泛泛"非选必三"）
- 优先厚写题清单中 13 题全部完成厚内容

## 监督备忘

- 学生稿候选条目内容用厚白话讲清材料动作 → 总帽子 → 小方法 → 触发逻辑 → 卷面答案句；未出现"固定分析流程"这个栏目或措辞。
- 学生稿候选条目内容未出现 `评标 / 参考答案 / 答案写 / 可从…角度作答 / yes / pass / filled / correct_option_chain / A-formal / B-choice-signal / phase / phase05 / source_pool / question_id / file id / line id / OCR / debug / /Users/... / C:\\...` 等审计或后台话术作正文。
- 审计字段（证据等级、来源 path、phase 状态、是否可入学生稿）只出现在 csv/jsonl 的元数据列，不进 `答案落点`/`为什么能想到` 等学生面向字段。
- Q-2024海淀二模-17(1) 严格按硬规则十六 SCIENCE_ONLY_SOURCE_SUPPORTED 锁定为科学思维设问下的来源支持落点（客观性/探索性·方法更新/整体安排），不复活为三模块并列设问。
- Q-2025海淀二模-20 按角度池+赋分上限规则展开 4 个挂载节点，矩阵 + entries 都标注 6 分上限与"矛盾分析法最多2分"。
- 此 batch 不写终稿、不写 PASS、不生成 Word/PDF；整套交付以"可融合材料 + 闭环裁决"为目标。
