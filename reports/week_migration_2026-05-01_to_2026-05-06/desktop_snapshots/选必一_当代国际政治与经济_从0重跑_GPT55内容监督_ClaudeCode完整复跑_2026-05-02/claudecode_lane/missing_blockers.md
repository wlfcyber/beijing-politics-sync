# Missing / Blockers

RUN ID: xuanbiyi_zero_gpt55_claudecode_2026-05-02

This file records: suites with no usable scoring source, failed tool attempts, uncertain module boundaries, and evidence-boundary questions.

## Excluded By Policy (No Scoring Source)

| Suite | Reason |
|---|---|
| 2026石景山期末 | User confirmed no usable scoring rules; all modules excluded by policy |
| 2026海淀期末 | User confirmed no 选必一 content; excluded |

## Blockers Being Investigated

| Suite | Item | Blocker | Status |
|---|---|---|---|
| 2025海淀期末 | Q22 | 细则.pptx是小学教师研修课程PPT，非本题评分细则；正式细则下落不明 | 未解决 |
| 2026西城期末 | Q20 | 无独立试卷文件，Q20完整设问文字未找到；条目已以推断设问写入，待核实 | 待核实 |
| 2025海淀期中 | Q16(2)/Q21(2) | 仅找到参考答案文字，未找到图片/表格形式正式细则（用户提示另有图片细则） | 未解决 |
| 2024东城一模 | Q16/Q20 | 细则.pptx为"试题分析"演示文稿，非正式阅卷细则；内容已部分提取但证据层级较低 | 降级处理，继续寻找正式细则 |

## Source Read Failures

(Updated if a PDF/Word/PPT cannot be read after multiple tool attempts)

| Time | Item | Failure | Status |
|---|---|---|---|
| 2026-05-02 | Previous ClaudeCode run | Hit `413 Request too large (max 32MB)` after a large PDF/image payload was sent into the model request. | Restart required with strict no-large-binary rule. |

## Trial Paper Not Found

| Suite | Notes |
|---|---|
| 2026西城期末 | 无试卷文件夹；Q20设问根据细则答案结构推断 |
