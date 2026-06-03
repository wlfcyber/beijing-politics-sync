# CLAUDECODE_THICK_CONTENT_PROMPT_20260526

请把以下内容原样交给 ClaudeCode B 线。它是生产 prompt，不是外审 prompt。

```text
你是飞哥政治庄园本轮选必三双宝典生产 B 线 ClaudeCode，不是 reviewer。

你的任务不是评价 Codex 现有 Word/PDF，也不是润色格式，而是补出可融合的厚内容矿。用户认为当前思维宝典和推理宝典都没有完全对齐哲学宝典；我们已经确认最大缺口之一是没有复刻 2026-05-02 必修四哲学宝典成功链路中的 “ClaudeCode 厚内容 -> Codex 融合裁决 -> 外审 -> Governor/Confucius”。

你必须先读：

1. /Users/wanglifei/Desktop/北京高考政治/reports/master_governor/latest_master_governor_report.md
2. /Users/wanglifei/Desktop/北京高考政治/reports/master_governor/worker_daily_orders.md
3. /Users/wanglifei/Desktop/北京高考政治/reports/master_governor/PROJECT_GOVERNOR_THREE_LAYER_SOP.md
4. /Users/wanglifei/Desktop/北京高考政治/reports/master_governor/CROSS_BOOK_WORKFLOW_V3_FOR_XUANBIER_XUANBISAN.md
5. /Users/wanglifei/.codex/skills/feige-politics-garden/SKILL.md
6. /Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/SKILL.md
7. /Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md
8. /Users/wanglifei/.codex/skills/feige-politics-garden-book-orchestrator/references/claudecode-first-fusion-workflow.md
9. /Users/wanglifei/Desktop/北京高考政治/选必三双宝典_哲学宝典完全对齐返工_2026-05-25/00_control/TASK_BRIEF.md
10. /Users/wanglifei/Desktop/北京高考政治/选必三双宝典_哲学宝典完全对齐返工_2026-05-25/00_control/DEVELOPMENT_PLAN.md
11. /Users/wanglifei/Desktop/北京高考政治/选必三双宝典_哲学宝典完全对齐返工_2026-05-25/00_control/PROGRESS.md
12. /Users/wanglifei/Desktop/北京高考政治/选必三双宝典_哲学宝典完全对齐返工_2026-05-25/00_control/GOVERNOR.md
13. /Users/wanglifei/Desktop/北京高考政治/选必三双宝典_哲学宝典完全对齐返工_2026-05-25/10_acceptance/FINAL_ACCEPTANCE_REPORT_20260526.md
14. /Users/wanglifei/Desktop/北京高考政治/选必三双宝典_哲学宝典完全对齐返工_2026-05-25/11_claudecode_thick_lane_packet/CLAUDECODE_THICK_CONTENT_TASK_BRIEF_20260526.md
15. /Users/wanglifei/Desktop/北京高考政治/选必三双宝典_哲学宝典完全对齐返工_2026-05-25/11_claudecode_thick_lane_packet/CLAUDECODE_THICK_CONTENT_MASTER_REQUIREMENTS_20260526.md
16. /Users/wanglifei/Desktop/北京高考政治/选必三双宝典_哲学宝典完全对齐返工_2026-05-25/11_claudecode_thick_lane_packet/CLAUDECODE_THICK_CONTENT_OUTPUT_SCHEMA_20260526.md
17. /Users/wanglifei/Desktop/北京高考政治/选必三双宝典_哲学宝典完全对齐返工_2026-05-25/11_claudecode_thick_lane_packet/CLAUDECODE_THICK_CONTENT_ACCEPTANCE_GATE_20260526.md

工作目录：

/Users/wanglifei/Desktop/北京高考政治/选必三双宝典_哲学宝典完全对齐返工_2026-05-25

输出目录：

/Users/wanglifei/Desktop/北京高考政治/选必三双宝典_哲学宝典完全对齐返工_2026-05-25/claudecode_lane

你可以使用 current run 的 SOURCE_LEDGER、QUESTION_COVERAGE_MATRIX、候选 Markdown、审计文件作定位索引，但不得直接继承旧正文结论。每个进正文的条目都要重新核对题面、材料、答案/细则或客观答案源、证据等级。

两本范围：

1. 思维宝典只收主观大题正文。结构按 思维类型 -> 小方法/触发链 -> 主观题。每条必须有 材料触发点 / 设问 / 为什么能想到 / 答案落点。选择题不进思维宝典正文，只能作为审计边界或进入推理宝典。

2. 推理宝典收主观大题和选择题。结构按 推理形式 -> 规则口令 -> 有效式/无效式 -> 对应题。主观题要写逻辑形式、规则触发、卷面理由；选择题必须有完整题干、完整四个选项、答案、正确理由、诱人错项和错因。

硬样本必须逐条处理：

思维：
- 2026顺义一模 Q19(2)
- 2025海淀二模 Q20
- 2026朝阳期中 Q21(2)
- 2024海淀二模 Q17(1)

推理：
- 充分条件假言推理至少一题
- 必要条件假言推理至少一题
- 三段论至少一题
- 类比推理至少一题
- 归纳推理至少一题
- 概念外延/定义至少一题
- 逻辑规律至少一题
- 2025顺义一模 Q7 必须锁为大项不当扩大谬误名称纠错

必须输出：

- claudecode_lane/PROGRESS.md
- claudecode_lane/DECISION_LOG.md
- claudecode_lane/SOURCE_LEDGER.csv
- claudecode_lane/COVERAGE_MATRIX.csv
- claudecode_lane/entries/thinking_main.jsonl
- claudecode_lane/entries/reasoning_main.jsonl
- claudecode_lane/entries/reasoning_choice.jsonl
- claudecode_lane/suite_reports/*.md
- claudecode_lane/framework_node_matrix.csv
- claudecode_lane/blocked_or_boundary.md
- claudecode_lane/fusion_candidates.md
- claudecode_lane/GOVERNOR.md

完成标准：

- 每个 coverage row 都有 body/index/blocked/excluded 决策。
- 每个核心思维节点和推理形式节点都有真实题挂载或 blocker。
- 学生字段不得出现路径、OCR/debug、评标、参考答案、A-formal、B-choice-signal、PASS、final、候选稿门禁、question_id 等污染。
- blocked 必须写清缺哪类证据。
- fusion_candidates 必须指出哪些内容可以替换 Codex 薄条目、补材料触发、补答案落点、补选择题错项，哪些应拒绝或只作索引。

不要生成 Word/PDF。不要写最终版。你的完成只表示可以交给 Codex 做融合。
```
