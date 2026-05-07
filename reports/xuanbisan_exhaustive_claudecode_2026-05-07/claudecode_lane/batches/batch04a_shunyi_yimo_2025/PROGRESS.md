# PROGRESS — batch04a S-2025顺义一模

> 角色：ClaudeCode B 线厚内容矿工，单套闭合
> 套卷：S-2025顺义一模
> 起始：2026-05-07

## 启动段落

本批是 batch04 整批停在 `_candidates.csv` 的修复批，scope 收窄到 2025顺义一模 一套。候选 CSV 中本套 raw 92 行、unique question_id 23 个，每个 question_id 必须落入 `入正文 / 同类索引 / blocked / excluded` 四类终态之一。

启动前已完成：
- 阅读 `~/.codex/skills/feige-politics-garden/SKILL.md`、`~/.codex/skills/feige-politics-garden-xuanbisan/SKILL.md`、`xuanbisan-hard-rules-notebook.md`、`00_飞哥选必三逻辑与思维硬性要求记事本.md`、本批 prompt 与 audit 脚本。
- 把候选 CSV 中 S-2025顺义一模 的 92 行抽到本目录 `_shunyi_rows.csv`，确认 23 个 unique question_id：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17(1), 17(2), 18, 19(1), 19(2), 20, 21。
- 回源教师版试卷 PDF 转录文本与细则文本，得到 1–15 题客观答案与主观题分层细则；不再依赖旧候选 CSV 的 phase12_action 或 evidence_level，而以原卷 + 细则为终审。

## 时间线

- 14:33  收到 batch04a prompt；读取必读文件、`_candidates.csv` 中 S-2025顺义一模 92 行；建立目录与 todos。
- 14:34  抽取 92 行到 `_shunyi_rows.csv`；定位试卷与细则路径（`2025各区模拟题/2025各区一模/2025顺义一模/`）以及预处理 corpus 中的对应 txt。
- 14:38  通读教师版试卷文本与 2025顺义一模细则文本；逐题判断模块归属与决策。
- 14:40  完成决策表（4 入正文 / 1 同类索引 / 0 blocked / 18 excluded = 23）。
- 14:41  以 Python `csv.DictWriter` 与 `json` 写入 QUESTION_DECISIONS.csv、MAIN_THINKING_LEDGER.csv、CHOICE_TRAP_LEDGER.csv、FRAMEWORK_NODE_MATRIX.csv、FRAMEWORK_NODE_MATRIX_SUMMARY.csv、entries/batch04a_entries.jsonl。
- 14:43  写 BLOCKED_OR_BOUNDARY.md；写 suite_reports/S-2025顺义一模.md；正在写 PROGRESS.md（本文件）与 BATCH04A_ACCEPTANCE.md，随后运行 `codex_audit/audit_batch_dir.py` 自检。

## 闭合统计

- 入正文：4（Q5, Q6, Q7, Q17(1)，全部为推理部分；2025顺义一模本套未出现选必三思维方法主链题）
- 同类索引：1（Q3，创新思维-逆向思维 边界陷阱）
- blocked：0（教师版试卷与细则齐备，未触发题面/答案/细则缺口）
- excluded：18（必修二/三/四 + 选必一/二）
- 总计：23 = unique question_id 数量

## 已交文件

- `PROGRESS.md`（本文件）
- `QUESTION_DECISIONS.csv`（23 行 + 表头）
- `MAIN_THINKING_LEDGER.csv`（1 行：Q17(1)）
- `CHOICE_TRAP_LEDGER.csv`（4 行：Q3, Q5, Q6, Q7）
- `FRAMEWORK_NODE_MATRIX.csv`（11 行：5 题选必三 × 多节点辅助挂）
- `FRAMEWORK_NODE_MATRIX_SUMMARY.csv`（6 行：5 个选必三节点 + 1 行 excluded 边界汇总）
- `BLOCKED_OR_BOUNDARY.md`（同类索引/blocked/excluded 全部 19 题逐条理由）
- `suite_reports/S-2025顺义一模.md`（套卷报告）
- `entries/batch04a_entries.jsonl`（5 行：Q3, Q5, Q6, Q7, Q17(1)）
- `BATCH04A_ACCEPTANCE.md`（自检报告，待 audit 跑完后落盘）

## 与硬规则的对照

- 第二节"证据边界"：A-formal 仅给 Q17(1)（细则明确分层 1+3 分）；其余 4 题为 B-choice-signal（细则第一部分客观答案已锁定）；Q3 同类索引 B-choice-signal 边界陷阱。无任何条目把普通参考答案冒充为 A-formal。
- 第四节"模块边界"：18 个 excluded 全部按设问 + 细则归属判定，未把"辩证""系统""创新""整体"等关键词当作选必三的归属依据。
- 第七节"答案句硬规则"：4 个入正文条目的 `answer_sentence` 写成考生卷面句（含"选 X：…"或"条件：…理由：…"），不出现"要写""落到""采分点""设问要求""材料中"等懒前缀。
- 第八节"选择题硬规则"：Q3、Q5、Q6、Q7 都同时给出题干信号、正确项理由、错项陷阱（A/B/C/D 全列）、陷阱类型；客观答案以细则为主，以教师版详解为辅。
- 第十二节补一"四要件充分性硬闸口"：未使用模板设问；`answer_sentence` 不是制作说明；同题多节点（Q6、Q7、Q17(1) 都有辅助挂载）每个挂载都对应该节点的具体小方法/小规则，不是同一段落复制粘贴。
- 第十九节"2025顺义一模 7 与 clean index 补丁"：Q7 主挂"大项不当扩大"，把"小项不当扩大"明确写为 A 项陷阱里的"误称"；同类索引/辅助挂载没有把该题正向挂到"小项不当扩大"。
- 第二十一节"框架版结构硬规则"：本套在选必三的挂载结构是"思维部分 / 创新思维 / 逆向思维 / 边界陷阱"+"推理部分 / 简单判断 / 联言矛盾"+"推理部分 / 概念与判断"+"推理部分 / 三段论"+"推理部分 / 复合判断的演绎推理"——按思维类型/题型挂题，不是按地区时间。本批没有"固定分析流程"字串。
- 第二十二节"ClaudeCode 厚内容优先"：所有入正文/同类索引条目都给出题干信号、触发逻辑、答案句、错项陷阱、框架挂载与证据级别，留出足够厚度供 Codex 融合。

## 自检清单

- 23 个 unique question_id 全部出现在 QUESTION_DECISIONS.csv，无遗漏（assert 已通过）。
- 决策值仅取 {入正文, 同类索引, blocked, excluded}。
- needs_codex_recheck 仅取 {yes, no}。
- 入正文条目 4 + 同类索引 1 = 5，全部出现在 entries/batch04a_entries.jsonl，每行包含 9 个必备字段。
- MAIN_THINKING_LEDGER 仅 Q17(1) 一行，符合"主观题入正文且属选必三"的定义。
- CHOICE_TRAP_LEDGER 包含 Q3（边界陷阱）、Q5、Q6、Q7 四行，符合"选择题入正文 + 同类索引"的定义。
- FRAMEWORK_NODE_MATRIX 11 行，覆盖主挂 + 辅助挂载 + 18 题 excluded 不再单列（excluded 在 SUMMARY 中合并汇总）。
- BLOCKED_OR_BOUNDARY.md 列出 1 同类索引 + 0 blocked + 18 excluded = 19 行，与 23 - 4 入正文 = 19 吻合。
- suite_reports/S-2025顺义一模.md 同时给出套卷概览、来源证据、决策表、入正文/同类索引要点、框架挂载分布、与候选 CSV 对照。
- BATCH04A_ACCEPTANCE.md 在最末调用 audit 脚本结果，未写 PASS / 终稿 / 完成 / 闭合 / 验收，仅按本批硬规则要求形成"自检通过 / 待 Codex 复核"中性表述。
