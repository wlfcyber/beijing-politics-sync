# Batch03a S-2025东城期末 ACCEPTANCE

> 本文件不写 PASS、不写终稿、不生成 Word/PDF。仅记录本批结构性闭合现场，作为可融合素材交给 Codex A 总控融合。

## 范围

- 套卷：`S-2025东城期末`（仅此一套）。
- 候选行：54（候选 CSV 中该套全部行）。
- unique question_id：24。
- 终判结论分布：入正文 5 / 同类索引 1 / blocked 0 / excluded 18。

## 必交文件

| 文件 | 状态 |
|---|---|
| `PROGRESS.md` | 已写 |
| `QUESTION_DECISIONS.csv` | 已写（24 行；csv.DictWriter；needs_codex_recheck∈{yes,no}） |
| `MAIN_THINKING_LEDGER.csv` | 已写（1 行：Q18-2 创新思维登月服 4 分） |
| `CHOICE_TRAP_LEDGER.csv` | 已写（4 行：Q5/Q13/Q14/Q15） |
| `FRAMEWORK_NODE_MATRIX.csv` | 已写（20 行节点挂载，正例 + 选择题陷阱 + 同类索引） |
| `FRAMEWORK_NODE_MATRIX_SUMMARY.csv` | 已写（按 framework_node 聚合 primary/trap/auxiliary） |
| `BLOCKED_OR_BOUNDARY.md` | 已写（blocker 0；excluded 18 按模块边界标注） |
| `suite_reports/S-2025东城期末.md` | 已写（套卷源 + 闭合统计 + 入正文厚条目 + 同类索引 + 硬样本配对） |
| `entries/batch03a_entries.jsonl` | 已写（5 行；每行 9 字段：question_id/type/framework_node/material_signal/trigger_logic/answer_sentence/evidence_level/needs_codex_recheck/source_batch） |
| `BATCH03A_ACCEPTANCE.md` | 本文件 |

## 自检要点（与 `codex_audit/audit_batch_dir.py` 对齐）

- `QUESTION_DECISIONS.csv` 每行 `claudecode_decision` ∈ {`入正文`, `同类索引`, `blocked`, `excluded`}。
- `QUESTION_DECISIONS.csv` 每行 `needs_codex_recheck` ∈ {`yes`, `no`}。
- CSV 各行字段宽度等于表头宽度（由 `csv.DictWriter` 保证）。
- `entries/batch03a_entries.jsonl` 每行可被 `json.loads` 解析；九个必需字段非空。
- 任何 `MAIN_THINKING_LEDGER.csv` / `CHOICE_TRAP_LEDGER.csv` / `FRAMEWORK_NODE_MATRIX.csv` / `entries/*.jsonl` / `suite_reports/*.md` / `BLOCKED_OR_BOUNDARY.md` / 本 ACCEPTANCE 文件均不含字符串 `固定分析流程`。

## 已锁定但需 Codex 复查的硬重点

- `Q-2025东城期末-18-2`：创新思维细则两层支持联想/聚合+发散/超前同时挂载；融合时优先保留三个小方法节点同时挂载，不要被压缩成"创新思维"单挂。
- `Q-2025东城期末-5`：辩证思维选择题三个小方法（整体性 + 动态性 + 矛盾分析法）按选项②④拆分挂载；①③两个干扰项分别归边界陷阱（必修四自在联系 / 必修四辩证否定观）。
- `Q-2025东城期末-13`：三段论同套同时考三种规则错误（中项不周延=正解、大项不当扩大、四概念）；与 `2024朝阳二模7`（小项不当扩大）合配三段论错误"三段套"。
- `Q-2025东城期末-14`：性质判断+关系判断综合题，正解出在"肯定判断谓项不周延"硬规则；A/B/C 三个干扰项各自承载一类边界陷阱（属种 vs 整体部分 / 反对称 vs 传递 / 外延一致性）。
- `Q-2025东城期末-15`：充分条件假言推理 vs 必要条件假言判断方向干扰；与 `2024朝阳一模20(1)`、`2025西城二模16(2)`、`2026通州期末19(2)` 共同构成假言推理选择题陷阱集合。

## 残余边界

- `Q-2025东城期末-21`：综合短文，按设问"综合运用所学"未独立给选必三思维方法分；保留为综合短文同类索引节点，不下挂选必三主链正文。
- 本批不接管推理硬样本 `2026东城期末 Q17(2)` 的形式逻辑边界（属下一批 `S-2026东城期末`）。
- 本批不生成 Word/PDF；不写 final、终稿、PASS、最终稿、宝典成品。

## 后续 codex 处理建议

- 把 5 条 `entries/*.jsonl` 行作为可融合的 thick body 候选直接合入选必三主链；其中 1 行主观题挂创新思维三个小方法节点，4 行选择题分别挂辩证思维 / 三段论 / 判断 / 假言推理对应节点。
- 同类索引行（Q21）转入综合短文索引节点；不进入选必三主链正文。
- 18 条 excluded 行按 `BLOCKED_OR_BOUNDARY.md` 中的模块归属移交对应模块的整体闭合工作（必修一/二/三/四、选必一、选必二）。
