# V58 DOCX/PDF QA

time: `2026-05-27T03:21:00+08:00`

verdict: `DOCX_PDF_REFRESHED_FOR_CONTENT_REVIEW_NOT_FINAL`

## Files

- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.docx`
- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.pdf`
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.docx`
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.pdf`

同步桌面文件夹：

- `/Users/wanglifei/Desktop/选必三双宝典_Word版_20260526/`

## Counts

Markdown:

- 思维册：`###=86`，`材料触发点=86`，`设问=86`，`为什么能想到=86`，`答案落点=86`
- 推理册：`###=83`，`材料触发点=83`，`设问=83`，`为什么能想到=83`，`答案落点=83`

PDF:

- 思维册：37 页，文本层可检索到 V58 补挂题：`2026海淀一模 第17题第（2）问`、`2025门头沟一模 第21题第（1）问`、`2024丰台二模 第18题第（2）问`
- 推理册：51 页

## Word Field Prompt Check

两本 DOCX：

- `updateFields=false`
- `PAGEREF=0`

说明：V58 仍保留普通页码能力，但目录页码不再依赖动态 `PAGEREF`，打开时不应再弹“是否更新域”。若用户端 Word 个性化设置仍弹窗，应优先检查 Word 全局“打开时更新自动链接/域”的偏好，而不是把它当成正文缺陷。

## Visual Check

LibreOffice/`soffice` 不在本机命令路径中，`documents/render_docx.py` 无法直接从 DOCX 渲染。替代流程：

1. 用 Microsoft Word 导出两本 PDF。
2. 用 PyMuPDF 从 PDF 渲染抽样页 PNG。
3. 抽检封面、前言、目录、V58 新增内容所在页和尾页。

抽样页：

- 思维册：1、2、5、6、9、37 页。
- 推理册：1、2、3、51 页。

抽样结论：未见页面空白、明显重叠、未定义书签、页码丢失或水印遮盖正文的硬缺陷。

## Forbidden Scan

思维 Markdown 未命中：

- `方法更新`
- `整体安排`
- `科学思维的综合运用`
- `辩证思维的综合运用`
- `整体性与系统观念`
- `动态性与质量互变`
- `改变条件与建立新联系`
- `特征与三新`
- `未定义书签`
- `（主观题，`
- `（选择题，`

## Hashes

- 思维 DOCX：`70ac8f556c8cf2b274f6ad328a483f66696a32da03e0bfe42f5109955820b592`
- 思维 PDF：`44b6162635a53129bd3f54e2fac17d3aea4ebe51e9b1acd452c0eb53802f4470`
- 推理 DOCX：`1592f8f3a6e9a984eab8d2a61fec1211380707f3c9df6d1b112ecc9dfd4756b9`
- 推理 PDF：`6058d7904f516eb21665c1f7b83c95cf715dc1756265e8cabc81e7ba7166d90b`

## Limit

本 QA 只证明 V58 文件已刷新并通过本地抽检，不代表最终内容 PASS。
