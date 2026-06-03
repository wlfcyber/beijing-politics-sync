# NEXT_REWRITE_QUEUE_CLAUDECODE_FUSION_20260526

audit_time: 2026-05-26T04:52:00+08:00

verdict: `NEXT_REWRITE_REQUIRED_BEFORE_FINAL`

## 当前反思结论

当前两本 Word/PDF 已经比旧版更接近哲学宝典的外壳：

- 封面、前言、目录、正文顺序已修正；
- A4、页码目录、DOCX 内部跳转书签已补；
- 思维正文已改为 `思维类型 -> 小方法节点 -> 主观题`；
- 推理正文已改为 `推理形式 -> 同类题`；
- 两本都补入了节点/章节导引。

但这仍不能证明“完全对齐哲学宝典”。哲学宝典真正的成功不只是四标题和目录，而是：

- 来源覆盖厚；
- 同一节点下密集挂题；
- 每题都能从材料信号自然走到方法/原理；
- ClaudeCode 厚内容与 Codex 证据裁决融合；
- 外审与 Confucius 只看成品也能通过。

当前缺口最硬的是：本 run 还没有真实 ClaudeCode 厚内容生产 lane，也没有 Codex/ClaudeCode 融合报告。因此下一轮不能继续只改 Word 样式。

## Rewrite Queue

### RQ-01 ClaudeCode B 线厚内容矿

status: `prepared_not_run`

执行文件：

- `11_claudecode_thick_lane_packet/CLAUDECODE_THICK_CONTENT_PROMPT_20260526.md`

必须产物：

- `claudecode_lane/entries/thinking_main.jsonl`
- `claudecode_lane/entries/reasoning_main.jsonl`
- `claudecode_lane/entries/reasoning_choice.jsonl`
- `claudecode_lane/suite_reports/*.md`
- `claudecode_lane/COVERAGE_MATRIX.csv`
- `claudecode_lane/framework_node_matrix.csv`
- `claudecode_lane/fusion_candidates.md`

验收重点：

- 不能只做 reviewer；
- 不能只给意见；
- 必须能被 Codex 吸收进正文。

### RQ-02 Codex 融合厚内容

status: `blocked_until_b_lane_exists`

融合时必须统计：

- Codex 当前保留条目数；
- ClaudeCode 新增条目数；
- ClaudeCode 替换 Codex 薄条目数；
- ClaudeCode 仅补材料触发条目数；
- ClaudeCode 仅补答案落点条目数；
- ClaudeCode 选择题错项补丁数；
- 拒绝条目及原因。

输出：

- `fusion/CODEX_CLAUDECODE_FUSION_REPORT_20260526.md`
- `fusion/TRACEABILITY_MATRIX.csv`
- 融合后两本 clean Markdown。

### RQ-03 思维宝典厚度补齐

status: `requires_b_lane_and_source_backcheck`

当前方向：

- 继续保持思维只收主观大题；
- 但每个核心小方法节点不能只有一两个题；
- 同题可复挂，但每次复挂都必须针对该节点重写四要件。

重点节点：

- 科学思维：客观性、预见性、可检验性、探索性与方法更新、整体安排；
- 辩证思维：整体性、动态性、分析与综合、质量互变、辩证否定；
- 认识发展历程：感性具体、思维抽象、思维具体；
- 创新思维：三新、发散聚合、逆向、超前、联想、迁移和想象、改变条件与建立新联系。

硬样本：

- `2026顺义一模 Q19(2)`
- `2025海淀二模 Q20`
- `2026朝阳期中 Q21(2)`
- `2024海淀二模 Q17(1)`

### RQ-04 推理宝典“题库归档感”继续削弱

status: `requires_b_lane_and_external_review`

当前推理册已从规则表向触发链调整，但仍需要用 B 线内容验证：

- 每类推理是否真挂尽同形题；
- 主观题是否都有完整设问和逻辑形式；
- 选择题是否每题都能让学生看到“题干信号 -> 推理形式 -> 正误判断”；
- `2025顺义一模 Q7` 是否稳定锁为大项不当扩大纠错样本。

重点类型：

- 充分条件；
- 必要条件；
- 三段论；
- 类比；
- 归纳；
- 概念/定义/外延；
- 逻辑规律；
- 论证评价与逻辑错误。

### RQ-05 真实外审与盲测

status: `real_call_pending`

必须分别完成：

- GPT Pro 真实审查；
- Claude 真实审查；
- fresh-context 学生包独立作答；
- grader 包评分；
- 错因修订；
- 二轮验证。

外审意见只能经 Codex 回源核验后进入正文。

### RQ-06 最终 Word/PDF 重建

status: `blocked_until_fusion_and_review`

融合后才允许重建最终 Word/PDF。

重建后必须复查：

- 封面、前言、目录、正文顺序；
- 页码目录；
- DOCX 内部链接；
- A4 与边距；
- 题干、选项、答案落点是否断裂；
- 禁词；
- 视觉抽样；
- Governor；
- Confucius artifact-only 学会性。

## Bottom Line

当前两本可以给用户查看，但不能叫“完全对齐哲学宝典”。下一轮真正有效的动作不是再美化当前 Word，而是运行 `11_claudecode_thick_lane_packet`，形成可融合厚内容，再由 Codex 回源裁决和重建最终稿。
