# Codex Lane A 自动化检测台账 - After Batch03

检测时间：2026-05-03 19:45 CST

工作目录：`/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03`

角色：Codex A 内部【自动化检测者】

本次只检测 Batch03 2026西城期末 Q20 文件链，不删除、不覆盖、不回退任何他人产物。

## 1. 总判定

结论：`WARN`

Batch03 2026西城期末 Q20 的 worker 文件、Codex 总控预案、CSV 结构、SOURCE_LEDGER 视觉复核链、screen 状态均已具备，可以进入补丁者/Patcher 与 Governor 后续审查融合。

但仍有两类不能忽略的问题：

1. `COVERAGE_MATRIX.csv` 仍显示 `worker_status=batch03_worker_assigned`、`patcher_status=waiting_for_batch03_worker_entries`、`fusion_status=not_started`，与实际 `worker_batch03_entries.md` 已存在不一致。
2. `07_student_doc/section_batch_draft_for_external_review.md` 禁入词扫描命中 `设问要求` 2 次，外审草稿需要清洗后再送外部内容审查或学生化。

不得宣布最终完成、coverage closed、学生终稿、Word/PDF 或 FINAL_ACCEPTANCE PASS。

## 2. Worker 文件检查

| 文件 | 状态 | 行数 | 结论 |
|---|---:|---:|---|
| `codex_lane/agents/worker/worker_batch03_entries.md` | EXISTS | 119 | 可读，仅处理 2026西城期末 Q20。 |
| `codex_lane/agents/worker/worker_batch03_source_notes.csv` | EXISTS | 13 | 可读，14列，无坏行。 |

`worker_batch03_entries.md` 字段检查：

- `术语`：9 条。
- `完整设问`：10 次，其中 1 次为全题总设问，9 次为条目字段。
- `细则位置`：9 条。
- `来源`：9 条。
- `材料触发`：9 条。
- `答案句`：9 条。
- `证据状态`：9 条。

结论：worker entry 字段齐。文件使用协议字段 `术语`，不是旧 worker 字段名 `术语原词`，这符合选必一 skill 的正式输出单位。

## 3. Codex 总控预案检查

| 文件 | 状态 | 行数 | 结论 |
|---|---:|---:|---|
| `02_extraction/codex_evidence_cards/batch03_2026西城期末_Q20_evidence_card.md` | EXISTS | 73 | 可读；记录本轮视觉核读，不替代 Worker/Patcher/Governor。 |
| `fusion/scoring_atom_table_batch03_codex_prelim.csv` | EXISTS | 10 | CSV 可解析；9 条 prelim atoms。 |
| `fusion/merge_register_batch03_codex_prelim.md` | EXISTS | 96 | 可读；明确仍需 Worker/Patcher/Governor。 |

注意：`fusion/scoring_atom_table_batch03_codex_prelim.csv` 的 `promotion_status` 仍为 `candidate_pre_worker`，但 worker 已产出。下一步应由补丁者把 prelim 与 worker 输出逐项比较，不能直接拿 prelim 进主融合。

## 4. CSV 结构检查

### 4.1 `fusion/scoring_atom_table_batch03_codex_prelim.csv`

- 物理行数：10。
- 表头列数：14。
- 数据行：9。
- 行宽分布：全部 14 列。
- 坏行：0。
- 空行：0。

结论：PASS。

### 4.2 `codex_lane/agents/worker/worker_batch03_source_notes.csv`

- 物理行数：13。
- 表头列数：14。
- 数据行：12。
- 行宽分布：全部 14 列。
- 坏行：0。
- 空行：0。

结论：PASS。

## 5. SOURCE_LEDGER / COVERAGE_MATRIX

### 5.1 SOURCE_LEDGER

`SOURCE_LEDGER.csv` 已有 2026西城期末 Q20 当前视觉复核链，共 13 行相关记录：

- `2026西城期末_Q20_SRC_0eccc84583b5`
  - `source_type=P0_formal_scoring_pdf_visual`
  - `evidence_level=P0_formal_scoring_rule`
  - `status=rechecked_batch03_visual`
  - 说明：细则 PDF 第4-5页视觉核读，Q20 8分三角度细则确认，角度2为4选3。
- `2026西城期末_Q20_TEACHER_PDF_CURRENT`
  - `source_type=P3_paper_pdf_visual`
  - `evidence_level=P3_paper_text`
  - `status=rechecked_batch03_visual`
  - 说明：教师版第8页视觉核读，完整设问与 NDC 材料表确认。
- 参考答案 PDF 已标为 `reference_not_used_for_atoms_batch03`。
- 旧目录/截图 locator 行已标为 `redundant_old_locator_not_used_batch03`。

结论：SOURCE_LEDGER 视觉复核状态 PASS。

### 5.2 COVERAGE_MATRIX

`COVERAGE_MATRIX.csv` 已有 2026西城期末 Q20 行：

- `codex_status=source_rechecked_visual_batch03`
- `evidence_status=P0_formal_scoring_rule_visual_recheck`
- notes 写明教师版第8页题面、细则 PDF 第4-5页视觉核读完成，角度2为4选3。

但该行仍显示：

- `worker_status=batch03_worker_assigned`
- `patcher_status=waiting_for_batch03_worker_entries`
- `governor_status=startup_fail_until_batch03_review`
- `fusion_status=not_started`

结论：COVERAGE_MATRIX 对“视觉复核”状态一致，但对“worker 已完成”状态未同步。必须在进入后续融合前更新为 `batch03_entries_written / pending_batch03_patcher_review / pending_batch03_governor_gate / not_promoted` 之类的保守状态。

## 6. screen / ClaudeCode 检查

screen 状态：PASS。

- `screen -ls`：No Sockets found。
- 未见 `xuanbiyi_fourlane_full_20260503` active socket。
- 未见 ClaudeCode `claude -p --verbose --output-format stream-json` 进程。
- 仅可见 Claude 桌面应用进程，不属于 ClaudeCode screen 残留。

## 7. External Review Draft 禁入词扫描

文件：`07_student_doc/section_batch_draft_for_external_review.md`

扫描词包括：

`采分点 / 要落到 / 材料中 / 本题需要 / 设问要求 / 细则要求 / 证据层级 / v7 / debug / audit / 模型聊天 / /Users/wanglifei / 评标 / 本地路径 / Claude / GPT / P0/P1/P2/P3 / worker / fusion / Governor / Codex`

结果：

- 命中 `设问要求` 2 次：第 173 行、第 207 行。
- 未命中本地路径、模型名、证据层级、P0/P1/P2/P3、debug/audit 等后台词。

结论：WARN。外审稿整体较干净，但 `设问要求` 是选必一 skill 明确禁止进入学生答案句/学生化文本的后台式表达。送外部审查或学生化前需要替换为更自然的表达，例如“题目追问”或直接改写触发逻辑句。

## 8. 可以进入补丁者/Governor的前提

可以进入后续角色，但只能进入：

- `Patcher Batch03 Review`
- `Governor Batch03 Gate`
- `Batch03 worker vs Codex prelim comparison`
- `Batch03 fusion candidate with fixes`

不能进入：

- 学生终稿
- Word/PDF
- coverage closed
- 频次终版
- FINAL_ACCEPTANCE PASS

## 9. 下一步必须等待的人工/角色结论

1. 补丁者/Patcher 结论
   - 比较 `worker_batch03_entries.md` 与 `fusion/scoring_atom_table_batch03_codex_prelim.csv`。
   - 核查角度2 “4选3” 是否被误刷成四个必答频次。
   - 判断 `命运共同体 / 全人类共同价值 / 正确义利观 / 共商共建共享 / 真正的多边主义 / 互利共赢` 是同一评分槽的替代表述，还是需要拆入不同总表核心。
   - 检查 `促进全球可持续发展 / 建设清洁世界` 是否作为结果语言，而非独立高频核心。
   - 检查 `维护联合国核心作用 / 完善全球治理体系` 与既有联合国桶的合并方式。

2. Governor 结论
   - 判定 `绿色发展 / 新发展理念 / 有为政府 + 有效市场` 是否只能作为实践支撑/边界记录，不进入选必一核心术语主链。
   - 判定 Batch03 是否可进入 `fusion candidate_with_fixes`。
   - 明确不得把角度2四个可选点全部记为必答频次。

3. 台账同步
   - 更新 `COVERAGE_MATRIX.csv` 的 2026西城期末 Q20 行，反映 worker 已完成但 patcher/governor/fusion 尚未完成。
   - 必要时在 `00_control/PROGRESS_LEDGER.jsonl` 追加 `worker_batch03_returned` 和 `automation_after_batch03_warn` 事件。

4. 外审稿清洗
   - 清理 `07_student_doc/section_batch_draft_for_external_review.md` 第173、207行的 `设问要求` 表达。
   - 清洗后重新跑禁入词扫描，再送外部 review。

## 10. 叫醒任务模板

```text
你是 Codex A 内部角色【补丁者】。工作目录：
/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03

先读取：
1. codex_lane/agents/automation_checker/automation_status_after_batch03.md
2. codex_lane/agents/worker/worker_batch03_entries.md
3. codex_lane/agents/worker/worker_batch03_source_notes.csv
4. 02_extraction/codex_evidence_cards/batch03_2026西城期末_Q20_evidence_card.md
5. fusion/scoring_atom_table_batch03_codex_prelim.csv
6. fusion/merge_register_batch03_codex_prelim.md
7. SOURCE_LEDGER.csv
8. COVERAGE_MATRIX.csv

任务：
只写 `codex_lane/agents/patcher/patcher_batch03_review.md`。不要改 worker、fusion、ledger 或学生文档。

重点审：
- Batch03 worker 与 Codex prelim 是否一致。
- CSV 中 9 个 prelim atoms 与 worker 9 个条目是否一一对应。
- 角度2四选三是否被误判为必答频次。
- 绿色发展/新发展理念/有为政府+有效市场是否只能作实践支撑或边界记录。
- 联合国核心作用、共同利益、人类命运共同体/正确义利观/共商共建共享等是否应与既有 Batch01/02 核心合并。

输出 PASS / PASS_WITH_FIXES / FAIL，不得宣布最终完成。
```

## 11. 本轮结论

`WARN`：Batch03 文件链足以进入补丁者/Governor后续融合审查；但 `COVERAGE_MATRIX.csv` 未同步 worker 已完成，外审草稿仍有 2 处 `设问要求` 禁入词，必须在后续角色推进前记录并修正。
