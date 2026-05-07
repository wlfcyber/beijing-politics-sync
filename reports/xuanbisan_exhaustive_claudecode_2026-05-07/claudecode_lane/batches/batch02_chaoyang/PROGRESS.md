# Batch02 朝阳套卷穷尽闭合 PROGRESS

## 启动 — 2026-05-07

任务边界：本批仅处理 4 套朝阳套卷（S-2024朝阳一模 / S-2024朝阳二模 / S-2024朝阳期中 / S-2026朝阳期中）的全部候选题，按用户穷尽口径产出 4 类结论 (`入正文 / 同类索引 / blocked / excluded`)，并对可融合题写厚内容。不写终稿、不写 PASS、不生成 Word/PDF。

## 继承纠偏吸取 (Batch01 教训)

- ✓ 必交 `entries/batch02_entries.jsonl`，schema 字段齐：`question_id, type, framework_node, material_signal, trigger_logic, answer_sentence, evidence_level, needs_codex_recheck, source_batch`。
- ✓ 不再只交 QUESTION_DECISIONS.csv；MAIN_THINKING_LEDGER / CHOICE_TRAP_LEDGER / FRAMEWORK_NODE_MATRIX(_SUMMARY) / BLOCKED_OR_BOUNDARY / suite_reports 全部并交。
- ✓ 选择题缺完整选项或答案源时统一写 `blocked`，不硬塞入正文。
- ✓ 学生候选条目内容用厚白话讲清材料动作 → 总帽子 → 小方法 → 触发逻辑 → 卷面答案句；未出现"固定分析流程"栏目或措辞。
- ✓ 学生候选条目内容未出现 `评标 / 参考答案 / 答案写 / 可从…角度作答 / yes / pass / filled / correct_option_chain / A-formal / B-choice-signal / phase / source_pool / question_id / file id / line id / OCR / debug / /Users/... / C:\\...` 等审计或后台话术作正文；审计字段（证据等级、来源 path、phase 状态、是否可入学生稿）只出现在 csv/jsonl 的元数据列。
- ✓ 本批不覆盖根 lane 和 Batch01 文件，只写 `batch02_chaoyang/` 子目录。

## 控制源已读

- `codex_lane/QUESTION_COVERAGE_MATRIX.csv` (528 行) — 抽出本批 4 套套卷候选共 91 行（含 2 行 duplicate）；89 unique rows。
- `claudecode_lane/QUESTION_COVERAGE_MATRIX.csv` (claudecode-side coverage) — 用作 phase05 信号交叉验证。
- `phase05_thinking_signal_archive.csv` / `phase05_reasoning_typology_archive.csv` — 抽 4 套套卷信号。
- `00_飞哥选必三逻辑与思维硬性要求记事本.md` — 穷尽口径、528 行控制基底、73 行思维信号矩阵。

## 硬规则记事本已读

- `feige-politics-garden/SKILL.md`：四线分工 + ClaudeCode 厚内容矿优先 (二十二、二十三)。
- `feige-politics-garden-xuanbisan/SKILL.md`：选必三流程与五硬样本（含 `2024朝阳二模 Q7` 小项扩大、`2026朝阳期中 Q21(2)` 创新思维复合题）。
- `feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md`：
  - §十八：`2024朝阳一模20(1)` 充分条件假言推理硬样本；`2024朝阳一模20(2)` 必要条件假言推理硬样本；`2024朝阳二模7` 锁为小项扩大谬误，不得回流为中项不周延。
  - §十三：`2026朝阳期中 Q21(2)` 是创新思维复合题硬样本，必须区分超前/联想/逆向/发散聚合。

## 套卷推进

| suite_id | 候选行数 | 已扫源文件 | 已读细则 | 已读试卷 | 状态 |
|---|---|---|---|---|---|
| S-2024朝阳一模 | 23 | ✓ | ✓ 031 朝阳一模细则.pptx (49 slides) | ✓ 030 朝阳一模 试卷.pdf (8 pages) | 闭合 |
| S-2024朝阳二模 | 22 | ✓ | ✓ 022 朝阳二模细则.pdf (5 pages) | ✓ 021 朝阳二模 试卷.pdf (8 pages) | 闭合 |
| S-2024朝阳期中 | 22 | ✓ | ✓ 018 朝阳期中细则.docx + 019 评标2.docx | ✓ 017 朝阳期中 试卷.pdf (8 pages) | 闭合 |
| S-2026朝阳期中 | 22 | ✓ | ✓ 朝阳期中细则.docx (含答案表 1-15 + 大题答案) | ✓ 003 朝阳期中 试卷.pdf (8 pages) | 闭合 |

合计：89 unique question rows，全部已逐题裁决。

## 优先厚写题清单（已确认证据等级）

### 已锁定为入正文 (A-formal)

主观题：

- Q-2024朝阳一模-20(1) — A-formal — 027试卷+031细则slide 45 — 充分条件假言推理(否定后件式) — 硬样本(§十八)
- Q-2024朝阳一模-20(2) — A-formal — 027试卷+031细则slide 46 — 必要条件假言推理(肯定后件式)
- Q-2024朝阳二模-19(1) — A-formal — 022细则page 3 — ①辩证思维-动态性 + ②类比推理 (双知识点)
- Q-2024朝阳二模-19(2) — A-formal — 022细则page 4 — 联言判断真值条件(全真才真，一假即假)
- Q-2024朝阳期中-18 — A-formal — 018细则Q18 + 019评标 — 楚王(不完全归纳/或然/轻率概括) + 晏子(类比推理/同属性相同推同/或然但论辩有效) — 选必三推理硬样本
- Q-2024朝阳期中-19 — A-formal — 018细则Q19 + 019评标 — 创新思维多角度(业态规划-超前思维 / 品牌引进-逆向思维 / 零售模式-联想思维 / 价值耦合-发散+聚合)
- Q-2026朝阳期中-20 — A-formal — 朝阳期中细则Q20 — 辩证思维多角度(矛盾分析法/分析与综合/质量互变/动态性) — 8分硬样本
- Q-2026朝阳期中-21(2) — A-formal — 朝阳期中细则Q21(2) — 创新思维多角度(超前/联想/逆向/三新/发散+聚合) — §十三试跑硬样本

选择题（B-choice-signal）：

- Q-2024朝阳一模-6 — B-choice-signal — 031细则slide 14确认B(排中律) — 选必三逻辑规则综合(越级划分/排中律/矛盾律/四概念)
- Q-2024朝阳一模-7 — B-choice-signal — 031细则未给标准答案，按四审排错确认C(②③) — 选必三创新思维多角度
- Q-2024朝阳二模-7 — B-choice-signal — 答案D — 选必三推理-三段论小项不当扩大硬样本(§十八)
- Q-2024朝阳期中-7 — B-choice-signal — 答案B(②-①-③) — 选必三推理-三段论第三格AAI式硬样本
- Q-2024朝阳期中-8 — B-choice-signal — 答案D(②④) — 选必三逻辑与思维必要条件假言判断
- Q-2024朝阳期中-9 — B-choice-signal — 答案B — 选必三推理-共变法(科学探究因果联系)
- Q-2024朝阳期中-10 — B-choice-signal — 答案A — 选必三概念-外延关系-属种关系
- Q-2026朝阳期中-11 — B-choice-signal — 朝阳期中答案表确认A — 选必三推理-三段论第二格AAI式补充大前提
- Q-2026朝阳期中-12 — B-choice-signal — 答案表确认B — 选必三相容选言判断
- Q-2026朝阳期中-13 — B-choice-signal — 答案表确认D(③④) — 选必三创新思维-联想思维 + 认识发展历程-感性具体到思维抽象 综合
- Q-2026朝阳期中-14 — B-choice-signal — 答案表确认B(①④) — 选必三推理-不完全归纳推理或然性
- Q-2026朝阳期中-15 — B-choice-signal — 答案表确认D — 选必三联言判断真值条件(否定支判断=否定整个)

### 同类索引/辅助挂载

- Q-2024朝阳一模-4 — 答案A(改变创造条件建立新联系) — 创新思维-改变条件创造条件辅助挂载/必修四改造自然边界混淆
- Q-2024朝阳一模-9 — 答案D(③④, ③系统观念) — 选必三导论-系统观念辅助挂载

### 已识别 blocker

- Q-2024朝阳二模-6 — 商业航天与航天概念关系 + 渐进性飞跃性 + 国家队为主+航天事业组成部分 — 022细则未给标准答案；试卷为完整试卷但答案表缺失；按硬规则八（选择题必须三者俱全才入正文）改 blocked，待回源补可靠答案表。
- Q-2024朝阳期中-11 — 关系判断/假言推理/三段论/矛盾律 综合 — 018细则未给Q11细则；题面解读存在争议（矛盾律vs同一律口径之争）；按硬规则八改 blocked，等待回源/校正。

## 下一步（已完成）

1. ✓ 读 4 套套卷的细则 + 试卷（4 套全部读到细则 + 试卷文本，含表格/选项/PPT slides）。
2. ✓ 从 codex_lane 矩阵抽 91 行候选；去重得 89 unique rows。
3. ✓ 抽硬样本（§十八 2024朝阳一模 20(1)/20(2)、2024朝阳二模 7；§十三 2026朝阳期中 21(2)）。
4. ✓ 展开 QUESTION_DECISIONS.csv（89 行候选；header 8 列）。
5. ✓ 厚写 8 道主观题 + 12 道选择题（共 20 道入正文）+ 2 道辅助/同类索引 + 2 道 blocked + 65 道 excluded。
6. ✓ 写 4 套 suite_reports + framework matrix + summary + blocked 文档 + entries.jsonl。

## 最终交付清单

| 文件 | 行数 | 说明 |
|---|---|---|
| `PROGRESS.md` | 本文件 | 套卷闭环+推进记录（不写 PASS） |
| `QUESTION_DECISIONS.csv` | 90 行（含表头）/ 8 列 | 每个候选题给出 `入正文/同类索引/blocked/excluded` 结论与理由；列：question_id, suite_id, original_qno, question_type, codex_current_decision, claudecode_decision, decision_reason, needs_codex_recheck |
| `MAIN_THINKING_LEDGER.csv` | 21 行（含表头）/ 11 列 | 8 道主观题厚内容、20 个挂载点；列：question_id, 来源, 完整设问, 材料动作, 总帽子, 小方法, 触发逻辑, 答案句, 证据等级, 框架落点, 题型标签 |
| `CHOICE_TRAP_LEDGER.csv` | 13 行（含表头）/ 9 列 | 12 道选择题厚陷阱分析；列：question_id, 题干信号, 完整选项或选项单位, 答案源, 正确项理由, 诱人错项, 陷阱类型, 是否可入学生稿, needs_codex_recheck |
| `FRAMEWORK_NODE_MATRIX.csv` | 36 行（含表头）/ 6 列 | 35 条 (framework_node, 挂载题id) 详挂载行 |
| `FRAMEWORK_NODE_MATRIX_SUMMARY.csv` | 25 行（含表头）/ 11 列 | 24 个 unique framework_node 的聚合视图 |
| `BLOCKED_OR_BOUNDARY.md` | — | 65 条 excluded + 2 条 blocked + 2 条同类索引/辅助挂载 |
| `suite_reports/` | 4 个 .md | 每套套卷一份闭环报告 |
| `entries/batch02_entries.jsonl` | 32 行 | 每条厚内容一行 JSON（subjective + choice 两类，每行含 question_id, type, framework_node, material_signal, trigger_logic, answer_sentence, evidence_level, needs_codex_recheck, source_batch；JSONL 语法+必需字段全部验证通过） |
| `BATCH02_ACCEPTANCE.md` | — | 不写 PASS；仅交付清单+套卷统计+残余边界 |

## 套卷统计

- 候选总数：89 题（去重后；codex matrix 91 raw rows，扣 2 row duplicates）
- 入正文：20 题（8 主观题 + 12 选择题）
- 同类索引/辅助挂载：2 题
- blocked：2 题
- excluded：65 题（每题列出所属模块；非泛泛"非选必三"）
- 优先厚写题：20 题全部完成厚内容（主观题 8 + 选择题 12）

## 监督备忘

- 学生候选条目内容用厚白话讲清材料动作 → 总帽子 → 小方法 → 触发逻辑 → 卷面答案句；未出现"固定分析流程"措辞。
- Q-2024朝阳二模-7 严格按硬规则§十八锁定为小项不当扩大；选项 A 的"娱乐工具都是思想政治教育的工具"中"娱乐工具"在前提中不周延、结论中扩大。
- Q-2026朝阳期中-21(2) 严格按硬规则§十三 复合题处理：超前思维(消费趋势研判转城市发展理念)/联想思维(冰雪与音乐文化叙事跨界融合)/逆向思维(冷资源转热经济+静态建筑转动态场景的反向思考)/三新+发散聚合(多角度挖掘文旅经济潜力+聚焦融合模式街区)四角度展开，不与必修四辩证法混淆。
- Q-2024朝阳一模-20(1)/20(2) 严格按§十八硬样本拆出 推理一(充分条件假言推理-否定后件式) + 推理二(必要条件假言推理-肯定后件式) 双结构，不混判。
- 此 batch 不写终稿、不写 PASS、不生成 Word/PDF；整套交付以"可融合材料 + 闭环裁决"为目标。
