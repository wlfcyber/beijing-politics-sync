# CLAUDECODE_THICK_CONTENT_TASK_BRIEF_20260526

run: `选必三双宝典_哲学宝典完全对齐返工_2026-05-25`

status: `prepared_not_run`

## Why This Lane Exists

用户要求不是“有一本能看的 Word”，而是两本选必三宝典在格式和内容上都完全对齐哲学宝典。

当前 Codex 已生成两本候选 Word/PDF，并做了多轮结构、目录、节点导引、禁词和视觉 QA 补丁；但本 run 的最终验收仍判为：

`NOT_COMPLETE_HARD_GAPS_REMAIN`

最大硬缺口之一是：尚未复刻哲学宝典成功工作流中的 `ClaudeCode 厚内容矿 -> Codex 融合裁决 -> 外审 -> Governor/Confucius`。

因此本包的目标是启动正式 ClaudeCode B 线厚内容生产，而不是让 ClaudeCode 做轻量 reviewer。

## Role

ClaudeCode B 线身份：

- 不是 reviewer；
- 不是只看现有 Word/PDF 给意见；
- 不是改格式；
- 是从题源和 current run ledger 出发，独立补出可融合的厚内容矿。

Codex 后续身份：

- 总控；
- 回源核验；
- 与 Codex A 线现有稿做差异融合；
- 学生版清洗；
- DOCX/PDF 重建；
- Governor / Confucius / 外审门禁。

## Scope

同时处理两本：

1. 思维宝典
   - 只收主观大题正文；
   - 严格遵循用户给的思维框架 PDF；
   - 最终结构必须是 `思维类型 -> 小方法/触发链 -> 主观题`；
   - 每题必须呈现 `材料触发点 / 设问 / 为什么能想到 / 答案落点`；
   - 不能把选择题陷阱库写进思维宝典正文。

2. 推理宝典
   - 收主观大题和选择题；
   - 最终结构必须是 `推理形式 -> 规则口令 -> 有效式/无效式 -> 对应题`；
   - 主观题必须有真实设问、材料/题干触发、逻辑形式、答案落点；
   - 选择题必须有完整题干、完整选项、答案、正确理由、诱人错项和错因。

## Input Boundaries

可用作定位索引：

- `00_control/SOURCE_LEDGER.csv`
- `00_control/QUESTION_COVERAGE_MATRIX.csv`
- `05_candidate_md/选必三_逻辑与思维_思维宝典_哲学完全对齐候选稿.md`
- `05_candidate_md/选必三_逻辑与思维_推理宝典_哲学完全对齐候选稿.md`
- `06_candidate_audit/`
- `02_alignment_audit/`
- 旧 run：`选必三双宝典_哲学对齐重做_2026-05-25/`

不可直接继承为正文结论：

- V98 或旧学生正文；
- 旧外审的泛化结论；
- 未回源的题型归类；
- 普通参考答案冒充评分细则；
- Codex 当前候选稿中的任何条目，除非 ClaudeCode 或后续 Codex 重新核验其题面、答案/细则和证据等级。

## Hard Samples

思维硬样本必须逐条处理，并输出可并入正文的厚条目：

- `2026顺义一模 Q19(2)`
- `2025海淀二模 Q20`
- `2026朝阳期中 Q21(2)`
- `2024海淀二模 Q17(1)`

推理硬样本至少覆盖：

- 充分条件假言推理；
- 必要条件假言推理；
- 三段论；
- 类比推理；
- 归纳推理；
- 概念外延/定义；
- 逻辑规律；
- `2025顺义一模 Q7` 三段论谬误名称纠错。

## Required Output Location

ClaudeCode 必须在本 run 下新建或写入：

`claudecode_lane/`

建议结构：

- `claudecode_lane/PROGRESS.md`
- `claudecode_lane/DECISION_LOG.md`
- `claudecode_lane/SOURCE_LEDGER.csv`
- `claudecode_lane/COVERAGE_MATRIX.csv`
- `claudecode_lane/entries/thinking_main.jsonl`
- `claudecode_lane/entries/reasoning_main.jsonl`
- `claudecode_lane/entries/reasoning_choice.jsonl`
- `claudecode_lane/suite_reports/*.md`
- `claudecode_lane/framework_node_matrix.csv`
- `claudecode_lane/blocked_or_boundary.md`
- `claudecode_lane/fusion_candidates.md`
- `claudecode_lane/GOVERNOR.md`

## Done Means

本 B 线完成只意味着“可进入 Codex 融合”，不意味着最终版完成。

必须同时满足：

- 每一条 current-run coverage row 都有 `body / index / blocked / excluded` 决策；
- 思维正文候选只含主观题；
- 推理正文候选含主观题和选择题，选择题四选项完整；
- 每个核心思维节点和推理形式节点都有真实题挂载或 blocker；
- blocked 有具体 source / answer / rubric / OCR / boundary 原因；
- 学生字段无路径、OCR、debug、评标、参考答案、PASS、final、question_id 等污染；
- 输出足以与 Codex A 线现有候选稿做逐项融合。
