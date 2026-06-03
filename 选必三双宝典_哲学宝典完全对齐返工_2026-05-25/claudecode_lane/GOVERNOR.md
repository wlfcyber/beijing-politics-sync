# GOVERNOR — ClaudeCode B 线（选必三双宝典）

run: `选必三双宝典_哲学宝典完全对齐返工_2026-05-25`
lane: `claudecode_lane/`
verdict: `B_LANE_THICK_MINING_FIRST_ROUND_READY_FOR_FUSION_NOT_END`

## 本 verdict 的意思

- 仅表示：B 线已交出可融合的厚内容矿包。Codex 可以开始裁决、回源核验、清洗和与 A 线 candidate Markdown / Word / PDF 做差异融合。
- 不表示：两本宝典已最终对齐哲学宝典；
- 不表示：可以生成最终 Word/PDF；
- 不表示：fresh-context 盲测、GPT Pro 真实审查、Claude 真实审查、Confucius、最终 acceptance 已通过。

## 已完成（B 线本轮硬性最小集）

- 17 份控制文件已读取并写入 `PROGRESS.md` 与 `DECISION_LOG.md`。
- `SOURCE_LEDGER.csv`、`COVERAGE_MATRIX.csv` 全量落盘，143 条 question 全部带 `body / index / blocked / excluded` 之一。
- `entries/thinking_main.jsonl`、`entries/reasoning_main.jsonl`、`entries/reasoning_choice.jsonl` 包含 8 个硬样本与节点最小覆盖。
- `suite_reports/` 写出 5 个硬样本套卷报告 + 边界/其他套卷汇总。
- `framework_node_matrix.csv` 思维 21 节点、推理 14 节点全部带挂载或 blocker。
- `blocked_or_boundary.md` 明确缺哪类证据。
- `fusion_candidates.md` 按 7 类对齐 Codex 现有薄点。

## 显式留作 Codex 与后续 lane 的硬阻断

- B 线没有重写非硬样本套卷的全量厚内容；只交出节点最小覆盖 + 硬样本最厚。Codex 融合时若发现某节点下 Codex 现稿与 B 线代表条目都偏薄，应回扫请 B 线补轮次，不要直接进 Word。
- B 线没有运行 Word/PDF；没有跑文本层禁词扫描；没有跑 PyMuPDF/视觉 QA。
- B 线没有调真实 GPT Pro / Claude；任何 `PASS / final / 终稿` 字样都属违规。
- `2024北京高考 Q19(2)` 与若干 `B-choice-signal` 条目仍在 `blocked / index`，待用户提供细则或外审升级后再开题。

## 否决条件（Codex 后续必须照此判断 B 线本包是否被否决）

任一发生，B 线本包视为不可融合，必须回退到 `B_LANE_CONDITIONAL_REPAIR_REQUIRED` 或 `B_LANE_REJECT_THIN_OR_UNTRACEABLE`：

- 学生字段中混入 `/Users/`、`C:\`、`OCR`、`debug`、`line id`、`file id`、`question_id`、`A-formal`、`B-choice-signal`、`评标`、`参考答案`、`答案写`、`PASS`、`final`、`候选稿门禁` 等污染词。
- coverage 出现 `not represented / needs review / 待定` 无裁决残留。
- 硬样本任一缺失或被错挂（特别是 `2024海淀二模 Q17(1)` 三模块并列、`2025顺义一模 Q7` 误正向描述）。
- `blocked` 条目未写 `blocked_reason` 或写成模糊话术。
- `fusion_candidates.md` 未按 7 类分；或没有指明对应 Codex 现稿位置与建议动作。
- 任一 jsonl 条目缺 `source_lock` 或 `evidence_level`。
