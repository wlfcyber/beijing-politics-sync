# BATCH04A — Self Audit Report

> 角色：ClaudeCode B 线厚内容矿工
> 套卷：S-2025顺义一模
> 日期：2026-05-07

本文件按 `codex_audit/audit_batch_dir.py` 的硬失败口径，登记本批次自检结论与残余事项。本批不写 `PASS`、不写终稿、不生成 Word/PDF；以下"自检通过"仅指 audit 脚本本批结构性硬失败为零，**仍需 Codex 复核与跨批融合**才能进入更高阶段。

## 1. 必交文件清单（按 audit 脚本 required[]）

| 文件 | 是否存在 | 备注 |
| --- | --- | --- |
| `PROGRESS.md` | 是 | 含启动段落、时间线、统计、与硬规则对照、自检清单 |
| `QUESTION_DECISIONS.csv` | 是 | 23 行；表头宽度 10；无宽度异常行 |
| `MAIN_THINKING_LEDGER.csv` | 是 | 1 行：Q-2025顺义一模-17-1（A-formal） |
| `CHOICE_TRAP_LEDGER.csv` | 是 | 4 行：Q3, Q5, Q6, Q7 |
| `FRAMEWORK_NODE_MATRIX.csv` | 是 | 11 行（5 题选必三 × 主挂 + 辅助挂） |
| `FRAMEWORK_NODE_MATRIX_SUMMARY.csv` | 是 | 6 行 |
| `BLOCKED_OR_BOUNDARY.md` | 是 | 1 同类索引 + 0 blocked + 18 excluded |
| `suite_reports/S-2025顺义一模.md` | 是 | 套卷报告，10 节 |
| `entries/batch04a_entries.jsonl` | 是 | 5 行；每行均含 9 必备字段，无 bad_json |
| `BATCH04A_ACCEPTANCE.md` | 是 | 本文件 |

## 2. audit 脚本硬失败检查（自检）

按 `audit_batch_dir.py` 的硬失败列表逐项核对：

- `missing_required_files`：未触发。required[] 文件全部存在。
- `missing_acceptance_file`：未触发。本文件即为 `*ACCEPTANCE*.md`，且不以 `SUPERVISOR_PATCH` 开头。
- `missing_suite_reports`：未触发。`suite_reports/S-2025顺义一模.md` 已落盘。
- `missing_entries_jsonl`：未触发。`entries/batch04a_entries.jsonl` 5 行。
- `invalid_csv_width`：未触发。QUESTION_DECISIONS.csv header 宽 10，全部数据行宽度一致。
- `invalid_terminal_decisions`：未触发。23 行的 `claudecode_decision` 全部 ∈ {入正文, 同类索引, blocked, excluded}（4 / 1 / 0 / 18）。
- `invalid_needs_codex_recheck`：未触发。23 行的 `needs_codex_recheck` 全部 ∈ {yes, no}。
- `invalid_jsonl_schema`：未触发。5 条 JSONL 每行均含 question_id, type, framework_node, material_signal, trigger_logic, answer_sentence, evidence_level, needs_codex_recheck, source_batch 9 个字段且全部非空；audit 脚本 type_counts 统计为 5 类。
- `forbidden_student_phrase`：第一次跑 audit 时命中 suite_report 中的"固定分析流程"自查表述（位于第 119 行），已删改为 prompt 黑名单的中性引用，重新自检不再出现该字串。

## 3. 决策分布

```
入正文       4   Q-2025顺义一模-5, -6, -7, -17-1
同类索引     1   Q-2025顺义一模-3
blocked      0
excluded    18   Q-2025顺义一模-1, -2, -4, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17-2, -18, -19-1, -19-2, -20, -21
合计        23
```

## 4. 证据级别分布

- A-formal_or_phase12_source_confirmed：1（Q17(1)，主观题，2025顺义一模细则给出 1+3 分分层）
- B-choice-signal：4（Q3、Q5、Q6、Q7，客观题答案在细则第一部分逐题列出）
- C-boundary_or_duplicate：18（excluded 边界记录，按设问归属判定）

## 5. 框架挂载映射

按 FRAMEWORK_NODE_MATRIX_SUMMARY.csv：

- 思维部分 / 创新思维 / 逆向思维 / 边界陷阱：1 题（Q3，同类索引）
- 推理部分 / 简单判断 / 联言判断与其矛盾命题：1 题（Q5）
- 推理部分 / 概念与判断（主项·联言·划分·关系判断综合）：1 题主挂 + 2 个辅助挂载 = 3 行（Q6）
- 推理部分 / 三段论（大项不当扩大-硬样本）：1 题主挂 + 2 个辅助挂载 = 3 行（Q7）
- 推理部分 / 复合判断的演绎推理：1 题主挂 + 2 个辅助挂载 = 3 行（Q17(1)）
- 边界外（excluded 18 题）：18 行（不进入选必三任何节点）

总挂载：11 行 + 18 行 excluded 汇总 = 29 行（FRAMEWORK_NODE_MATRIX.csv 仅写入 11 个有挂载的行；excluded 在 SUMMARY 中合并汇总）。

## 6. 与候选 CSV 的差异

- 候选 CSV 中 Q-2025顺义一模-3 标为 `excluded_keep_out / out_of_scope`；本批结合 D 项"运用逆向思维"干扰项的边界训练价值，将其调整为"同类索引"，挂到创新思维-逆向思维-边界陷阱节点。理由写入 BLOCKED_OR_BOUNDARY.md 第一节。
- 候选 CSV 中除 Q5、Q6、Q7、Q17(1) 外，其余 11 题选择题 + 7 题主观题被标为 `blocked_keep_out / answer_missing` 或 `excluded_keep_out / out_of_scope`，evidence 标为 missing_or_blocked。本批回源到教师版试卷 PDF 转录文本与 2025顺义一模细则文本，确认题面、答案与（主观题）评分细则齐备，因此不再保留 blocked 状态，按设问归属直接 excluded（非选必三）。

## 7. 给 Codex 的复核要点

- Q3 的"同类索引 vs excluded"：本批选择"同类索引"。理由：D 项"运用逆向思维"是模块边界陷阱训练样本，对学习选必三创新思维-逆向思维章节有训练价值。Codex 在融合阶段可独立判断是否保留该索引。
- Q17(1) 的细则对照：本批已提取"条件 1 分（既……又……） + 理由 3 分（判断类型 1 分 + 至少一个具体分析 2 分）"。Codex 在融合阶段可对照原 docx 细则文件（`2025各区模拟题/2025各区一模/2025顺义一模/细则/2025顺义一模细则.docx`）确认未漏其它给分点。
- Q7 的硬样本锁定：本批主挂"大项不当扩大"，辅助挂载"中项不周延""四概念"，与硬规则记事本第十九节"2025顺义一模 7 三段论谬误名称纠错硬样本"一致。Codex 在 final clean index 阶段应避免把 A 项陷阱（误称小项不当扩大）回流为正向"小项不当扩大"挂载点。
- 18 题 excluded 的边界归属：每题已写明设问与所属模块（必修二/三/四 + 选必一/二）。Codex 在跨批融合时可作为非选必三套卷对照样本，不需要在选必三正文中保留。

## 8. 残余事项 / 不写完成

- 本批仅闭合 S-2025顺义一模 一套；batch04 整批的丰台期末与通州题目仍在原 batch04 目录中，本批未触及。
- Codex 复核未跑、跨批融合未做、Word/PDF 未生成。
- 因此本文件**不写"完成 / 闭合 / 验收 / PASS / 终稿"**；仅按本批 prompt 与 audit 脚本要求形成"结构性自检通过 / 待 Codex 复核与融合"中性表述。

## 9. 自检结论（中性表述）

- audit 脚本本批跑出的 `BATCH_QA_STRUCTURALLY_OK_NOT_FINAL` 仅表示结构性可作融合输入；不授权 Word/PDF 终稿。
- 23 个 unique question_id 均已落入终态决策；4 入正文 + 1 同类索引共 5 条 JSONL 条目厚度齐备；BLOCKED_OR_BOUNDARY.md 与 suite_reports 已完成。
- 本批移交 Codex 复核与跨批融合；任何下游阶段（融合、Opus 教学化、GPT 外审、Governor、Confucius、Word/PDF）需另行启动。
