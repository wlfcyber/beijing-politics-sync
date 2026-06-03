# EXTERNAL_REVIEW_MANIFEST_20260526

packet_time: 2026-05-26T13:46:42+08:00

status: `claude_v27_p2_polish_gpt_pending`

本包用于真实 GPT Pro / Claude 对齐审查。审查对象只限 V27 两本选必三宝典与哲学宝典对齐质量，不允许外审模型另起炉灶重做框架。

## 当前待审版本

- 版本：V27 content misclassification patch + philosophy-style question labels + student-language cleanup + DOC/PDF refresh
- 思维 PDF：28 页
- 推理 PDF：49 页
- Claude 真实外审状态：V27 已真实复审，verdict 为 `P2_POLISH`；Codex 已回源判定，未形成新的 confirmed content error。
- GPT Pro 真实外审状态：`real_call_pending / blocked_advisor`
- 最终声明：不得写 `PASS` 或 `最终版`。

## 待审文件

- `选必三_逻辑与思维_思维宝典_哲学完全对齐版.docx`
- `选必三_逻辑与思维_思维宝典_哲学完全对齐版.pdf`
- `选必三_逻辑与思维_推理宝典_哲学完全对齐版.docx`
- `选必三_逻辑与思维_推理宝典_哲学完全对齐版.pdf`
- `PHILOSOPHY_ALIGNMENT_V27_DOCX_PDF_QA_20260526.md`
- `V26_PHILOSOPHY_PARITY_LABEL_LANGUAGE_CONTACT_SHEET_20260526.png`
- `PHILOSOPHY_ALIGNMENT_V27_CONTENT_MISCLASSIFICATION_RECHECK_20260526.md`
- `PHILOSOPHY_ALIGNMENT_V26_PARITY_LABEL_LANGUAGE_20260526.md`
- `CONTENT_MISCLASSIFICATION_AUDIT_V23_DEEP_SOURCE_REPAIR_20260526.md`
- `CLAUDE_REAL_REVIEW_RAW_FORMAT_V17_20260526.md`
- `CLAUDE_REAL_REVIEW_ADJUDICATION_V18_20260526.md`
- `CLAUDE_REAL_REVIEW_RAW_V27_20260526.md`
- `CLAUDE_REAL_REVIEW_ADJUDICATION_V27_20260526.md`
- `GPT_PRO_REVIEW_PROMPT_20260526.md`
- `CLAUDE_REVIEW_PROMPT_20260526.md`
- `CURRENT_STATUS_REPORT_V27_20260526.md`
- `SOURCE_LEDGER.csv`
- `QUESTION_COVERAGE_MATRIX.csv`

## V27 相对 V26 的核心变化

- 内容判断修补：`2026顺义二模 Q18(1)` 不再写成 `结论一也成立`，改为区分“自相矛盾判断正确”和“确定性要求表述错误，应改为一致性要求”。
- V27 Markdown 已重新生成 DOCX/PDF，并同步桌面 Word 文件夹与本外审文件夹。

## V26 相对 V25 的核心变化

- 标题对齐：思维册 61 条三级题目标题全部补入 `（主观题）`，与哲学宝典题型标识一致。
- 推理册保留 47 个 `（主观题）` 与 36 个 `（选择题）`。
- 学生语言清理：去除 `题目要求`、`设问点名`、`官方细则`、`这题`、`题目不是` 等讲解/审稿口吻。
- 内容锁定保持不变：`2024西城一模 第19题第（5）问` 固定为超前思维，不作为科学思维或推理同一律条目。

## 基准核验

- 参考基准：`/Users/wanglifei/Desktop/哲学宝典最终版 5.2双终极融合版_目录页码美化版_副本.docx`
- 思维框架：`/Users/wanglifei/Desktop/先前框架/逻辑与思维 思维部分 原文件 拷贝.pdf`
- 哲学宝典正文实际使用四标题法：`材料触发点 / 设问 / 为什么能想到 / 答案落点`。
- 哲学宝典三级题目标题标注 `（主观题）/（选择题）`；V26 已同步这一点。

## 本地 QA 摘要

- 两本学生 MD/DOCX/PDF 禁词和后台痕迹扫描 0。
- 思维 Markdown/PDF 四标题各 61；推理 Markdown/PDF 四标题各 83。
- `2026顺义二模 Q18(1)` 补丁已进入思维 DOCX/PDF；`若补充结论一` 可检出，`结论一也成立` 为 0。
- 思维 DOCX H3=61，`（主观题）`=61。
- 推理 DOCX H3=83，`（主观题）`=47，`（选择题）`=36。
- 推理选择题条目 36，Markdown/PDF `答案选=36`、`错项分析=36`。
- DOCX 目录字段：思维 PAGEREF 19，推理 PAGEREF 70；TOC1/TOC2 样式正常，旧 TOC11/TOC21 为 0；水印均存在。
- 抽样视觉图显示封面、前言、目录、正文中段、选择题页和末页可读，无黑页、重叠、截断或页脚丢失。

## Claude V27 Real Review 摘要

- Claude verdict: `P2_POLISH`。
- Claude 确认 `2024西城一模 第19题第（5）问` 已正确挂入 `超前思维`。
- Claude 确认 `2026顺义二模 Q18(1)` V27 补丁方向正确。
- Codex 已回源核验 Claude 所列内容风险点：`2025顺义一模 Q7`、`2026石景山一模 Q6`、`2026海淀二模 Q7`、`2026顺义二模 Q18(1)`、`2026丰台一模 Q18(2)`、`2024东城一模 Q6`、`2024顺义二模 Q6` 均未形成新增正文错判。
- Claude 剩余意见主要是句首残留、教师列点笔法、错项模板、章节 H2 密度等 `P2_POLISH` 项。

## 必须输出的 verdict

外审只能给以下之一：

- `PASS`
- `CONDITIONAL_PASS`
- `P0_BLOCK`
- `P1_REVISE`
- `P2_POLISH`

在真实调用完成前，本 run 不得写 `PASS` 或 `最终版`。
