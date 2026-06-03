# CLAUDECODE B 线文件审计

audit_time: `2026-05-26T05:31:30+08:00`

verdict: `B_LANE_OUTPUT_RECEIVED_CONDITIONAL_REPAIR_REQUIRED_BEFORE_FUSION`

## 结论

ClaudeCode B 线已经从 `prepared_not_run` 进入真实产出状态，`claudecode_lane/` 下的厚内容矿文件已落盘，可作为下一步 Codex 融合的参考输入。

但本包不能直接进入学生版融合，更不能据此重建最终 Word/PDF。Codex 文件审计发现 B 线自检未覆盖的硬问题：`COVERAGE_MATRIX.csv` 仍有两处 `待Codex回源细化` 残留，且 `PROGRESS.md` 早段仍声称 `思维 21 个节点、推理 14 个题型节点`，与最终自检 `思维 20 节点 + 推理 13 节点 = 33` 不一致。

## 文件存在性

- `SOURCE_LEDGER.csv`: present, 143 rows
- `COVERAGE_MATRIX.csv`: present, 147 rows
- `entries/thinking_main.jsonl`: present, 31 valid JSON entries
- `entries/reasoning_main.jsonl`: present, 31 valid JSON entries
- `entries/reasoning_choice.jsonl`: present, 23 valid JSON entries
- `suite_reports/`: present, 7 files
- `framework_node_matrix.csv`: present, 33 rows
- `blocked_or_boundary.md`: present
- `fusion_candidates.md`: present
- `PROGRESS.md` / `DECISION_LOG.md` / `GOVERNOR.md`: present

## Codex 复核结果

- JSONL 语法：3 个 entries 文件均可解析，无坏行。
- Coverage 决策：147 行均有合法 `decision` 与 `handbook_target`。
- Coverage 口径：143 个原始 question 行 + 4 个 cross-mount 行 = 147 coverage rows。B 线控制文件应显式说明这个口径，不能只写 143。
- 节点矩阵：实际 33 节点，`covered=29 / covered_by_support=3 / blocked_no_question=1`。
- 学生字段禁词：B 线自检显示 15 个禁词在 student-facing 字段中 0 命中；Codex 后续融合仍需重新扫描最终 Markdown/DOCX/PDF。

## 必须修补或由 Codex 融合时硬拦截

1. `COVERAGE_MATRIX.csv` 第 84 行：
   - `BCV0083,2024海淀一模,Q0083,...,思维(待Codex回源细化),...`
   - 问题：`body` 行仍有 `待Codex`，不能称为无待定残留。
   - 处理：进入融合前必须改成具体思维节点，或降级为 `blocked` 并写清 `blocked_reason`。

2. `COVERAGE_MATRIX.csv` 第 85 行：
   - `BCV0084,2024朝阳二模,Q0084,...,推理+思维交叉(待Codex回源细化),...`
   - 问题：`body` 行仍有 `待Codex`，且 primary target 是 `reasoning_main`，但另有 `Q0084(thinking-mount)` 交叉挂载。
   - 处理：进入融合前必须拆成明确推理形式与明确思维节点，或降级阻断。

3. `PROGRESS.md` 早段节点数声明：
   - 早段写 `思维 21 个节点、推理 14 个题型节点`。
   - D14 写 `思维 20 节点 + 推理 13 节点共 33 行`。
   - 处理：以 D14 与实际 `framework_node_matrix.csv` 为准；早段声明不得作为验收依据。

4. B-choice-signal body 风险：
   - `reasoning_choice.jsonl` 中仍有低证据选择题 body 或占位条目，例如 `RC-2025-FENGTAI-FINAL-Q9`。
   - 处理：Codex 融合时不得把占位题面、占位选项、占位答案写入学生正文；必须回源补全，否则转 index/boundary。

## 可进入下一步的内容

- 四个思维硬样本的多节点拆分思路可作为融合参考：
  - `2026顺义一模 Q19(2)`
  - `2025海淀二模 Q20`
  - `2026朝阳期中 Q21(2)`
  - `2024海淀二模 Q17(1)`
- 推理硬样本与选择题错因模板可作为融合参考：
  - `2025顺义一模 Q7`
  - 充分条件、必要条件、三段论、类比、归纳、概念外延/定义、逻辑规律等节点代表条目
- `fusion_candidates.md` 可作为下一步 Codex 差异融合入口，但其中所有建议必须经 Codex 回源核验后进入正文。

## 下一步门禁

next_status: `CODEX_FUSION_ALLOWED_ONLY_WITH_REPAIR_GATES`

Codex 下一步可以开始融合，但必须先做：

1. 处理 coverage 两处 `待Codex` 残留。
2. 明确 147 coverage rows 的口径。
3. 对 `B-choice-signal` 和占位 choice body 做降级或回源补全。
4. 用 B 线 `fusion_candidates.md` 逐条改写候选 Markdown，而不是直接复制 JSONL。
5. 重新生成 DOCX/PDF，并重跑文本层、目录、页码、抽样视觉 QA。
6. 真实 GPT Pro / Claude、fresh-context 盲测、Governor/Confucius 未完成前，仍不得写 `PASS` 或 `最终版`。
