# CLAUDECODE_THICK_CONTENT_ACCEPTANCE_GATE_20260526

status: `prepared_not_run`

## Gate Verdict Values

ClaudeCode B 线完成后，Codex 只能给以下 verdict：

- `B_LANE_ACCEPT_FOR_FUSION`
- `B_LANE_CONDITIONAL_REPAIR_REQUIRED`
- `B_LANE_REJECT_THIN_OR_UNTRACEABLE`
- `B_LANE_NOT_RUN`

当前 verdict: `B_LANE_NOT_RUN`

## Minimum Acceptance Checks

### 1. Real Production Evidence

- 是否存在 `claudecode_lane/PROGRESS.md`。
- 是否存在 `claudecode_lane/DECISION_LOG.md`。
- 是否存在 `claudecode_lane/SOURCE_LEDGER.csv`。
- 是否存在 `claudecode_lane/COVERAGE_MATRIX.csv`。
- 是否存在 `claudecode_lane/entries/`。
- 是否存在 `claudecode_lane/suite_reports/`。
- 是否存在 `claudecode_lane/framework_node_matrix.csv`。
- 是否存在 `claudecode_lane/blocked_or_boundary.md`。
- 是否存在 `claudecode_lane/fusion_candidates.md`。

缺任一项，不得进入融合。

### 2. Scope Coverage

- `thinking_main` 只含主观题正文候选。
- `reasoning_main` 含主观推理题。
- `reasoning_choice` 含选择题推理/逻辑题。
- 每个 coverage row 都有 `body / index / blocked / excluded`。
- 不得有 `not represented`、`needs review`、`待定` 无裁决残留。

### 3. Philosophy Alignment

思维条目必须通过：

- `材料触发点` 不是材料摘抄；
- `设问` 是真实设问；
- `为什么能想到` 是材料动作到小方法的触发逻辑；
- `答案落点` 是能直接写到答题纸上的句子。

推理条目必须通过：

- 有逻辑形式或错误式；
- 有规则触发；
- 有卷面理由；
- 选择题有完整选项；
- 诱人错项逐项写错因。

### 4. Hard Samples

必须显式检查：

- `2026顺义一模 Q19(2)`：科学思维客观性、预见性、可检验性是否拆开。
- `2025海淀二模 Q20`：辩证思维复合题是否拆到分析综合、整体性、动态性/质量互变、辩证否定。
- `2026朝阳期中 Q21(2)`：创新思维是否拆到超前、联想、逆向、发散聚合等。
- `2024海淀二模 Q17(1)`：只能作为科学思维设问下的来源支持落点，不能伪造三模块并列设问。
- `2025顺义一模 Q7`：三段论谬误名称纠错必须锁为大项不当扩大，不能误写成小项不当扩大正例。

### 5. Student Cleanliness

学生字段不得出现：

- `/Users/`
- `C:\`
- `OCR`
- `debug`
- `line id`
- `file id`
- `question_id`
- `A-formal`
- `B-choice-signal`
- `评标`
- `参考答案`
- `答案写`
- `PASS`
- `final`
- `候选稿门禁`

审计字段可以保留证据等级和路径，但不得混入学生版字段。

### 6. Fusion Completeness

`fusion_candidates.md` 必须说明：

- 哪些 ClaudeCode 条目比 Codex 现有稿更厚；
- 哪些应替换 Codex 薄条目；
- 哪些只补材料触发；
- 哪些只补答案落点；
- 哪些补选择题错项；
- 哪些因证据不足被拒绝；
- 哪些只是 index 或 boundary。

## Final Warning

即使本 Gate 通过，也只表示可以进入 Codex 融合。还必须继续完成：

- Codex 回源核验；
- Codex/ClaudeCode 融合报告；
- GPT Pro 真实审查；
- Claude 真实审查；
- Word/PDF 重建；
- Governor；
- Confucius fresh-context 盲测；
- 最终 acceptance。
