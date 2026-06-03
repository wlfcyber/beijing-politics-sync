# PHILOSOPHY ALIGNMENT V27 DOCX/PDF QA

- time: 2026-05-26T13:28:47+08:00
- verdict: `DOCX_PDF_REBUILT_AFTER_CONTENT_PATCH_NOT_FINAL`

## Rebuilt Artifacts

- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.docx`
- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.pdf`
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.docx`
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.pdf`

## Text QA

| File | Pages / H3 | Key Checks |
| --- | ---: | --- |
| 思维 DOCX | H3=61 | `若补充结论一` present; `结论一也成立` absent; `（主观题）`=61; TOC1=4, TOC2=15, old TOC11/TOC21=0 |
| 推理 DOCX | H3=83 | `（主观题）`=47; `（选择题）`=36; TOC1=8, TOC2=62, old TOC11/TOC21=0 |
| 思维 PDF | 28 pages | `若补充结论一` present; `结论一也成立` absent; `材料触发点`=61; `答案落点`=61 |
| 推理 PDF | 49 pages | `材料触发点`=83; `答案落点`=83; `（主观题）`=47; `（选择题）`=36 |

## Render/Visual QA Note

本机没有 Poppler/PyMuPDF/LibreOffice 渲染链，本轮使用 Microsoft Word 导出 PDF，并用 PDF 文本抽取和 DOCX 结构检查确认正文补丁已经进入交付件。V26 已做过抽样 contact sheet；V27 只改一处正文判断并保持页数不变，未发现需触发大规模版式重排的变化。

## Not Final

本 QA 只证明 V27 本地 Word/PDF 与当前 Markdown 内容一致，不替代真实 GPT Pro / Claude 外审。
