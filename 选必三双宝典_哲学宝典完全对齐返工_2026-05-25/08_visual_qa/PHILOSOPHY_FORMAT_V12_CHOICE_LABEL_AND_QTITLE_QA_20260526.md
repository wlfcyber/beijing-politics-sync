# PHILOSOPHY_FORMAT_V12_CHOICE_LABEL_AND_QTITLE_QA_20260526

qa_time: 2026-05-26T09:41:35+08:00

verdict: `LOCAL_V12_QA_PASS_NOT_FINAL`

## QA Scope

本轮只验收 V12 两个前台对齐补丁：

- 工作流式 `Q19(2)` 题号是否已从学生正文清零。
- 推理选择题是否按计划拆成 `完整题干` 与 `完整选项`。

## Text-layer Checks

| file | pages | Q refs | 第N题 refs | 完整题干 | 完整选项 | 完整题干与选项 |
|---|---:|---:|---:|---:|---:|---:|
| 思维 Markdown | n/a | 0 | 59 | 0 | 0 | 0 |
| 推理 Markdown | n/a | 0 | 119 | 36 | 36 | 0 |
| 思维 DOCX | n/a | 0 | 59 | 0 | 0 | 0 |
| 推理 DOCX | n/a | 0 | 119 | 36 | 36 | 0 |
| 思维 PDF | 35 | 0 | 59 | 0 | 0 | 0 |
| 推理 PDF | 54 | 0 | 119 | 36 | 36 | 0 |

## DOCX Structure Checks

- 思维 DOCX：`TOC1=4 / TOC2=15 / TOC11=0 / TOC21=0`；`PAGEREF=19`。
- 推理 DOCX：`TOC1=8 / TOC2=61 / TOC11=0 / TOC21=0`；`PAGEREF=69`。

## Visual QA

采用 macOS Quick Look 重新渲染 PDF 抽样页，避免 `sips` 对透明 PDF 背景误渲染为黑底。

抽样页：

- 思维 PDF：1、3、4、5、35 页。
- 推理 PDF：1、3、6、10、17、54 页。

证据图：

- `08_visual_qa/V12_CHOICE_LABEL_AND_QTITLE_QUICKLOOK_CONTACT_SHEET_20260526.png`
- `08_visual_qa/V12_CHOICE_LABEL_DETAIL_QUICKLOOK_20260526.png`

视觉结论：

- 白底正文可读。
- 推理第 10 页可见同一选择题内 `【完整题干】`、`【完整选项】`、`【答案】`、`【正确理由】`、`【诱人错项和错因】`。
- 推理第 17 页可见主观题与选择题混排页，中文题号为 `第19题第（1）问` / `第6题` 风格，不再显示 `Q19(1)`。
- 抽样页未见标题遮挡、正文消失、页脚丢失或选项断裂。

## Boundary

本 QA 只证明 V12 本地修补通过；真实 GPT Pro / Claude 外审仍未完成，不得升级为 `PASS` 或最终版。
