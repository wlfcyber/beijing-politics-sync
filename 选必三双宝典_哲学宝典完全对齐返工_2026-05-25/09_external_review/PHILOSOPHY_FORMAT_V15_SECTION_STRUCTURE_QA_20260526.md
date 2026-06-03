# PHILOSOPHY_FORMAT_V15_SECTION_STRUCTURE_QA_20260526

status: `LOCAL_V15_VISUAL_AND_STRUCTURE_QA_PASS_NOT_FINAL`

## 文件

- 思维 DOCX：`07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.docx`
- 思维 PDF：`07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.pdf`
- 推理 DOCX：`07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.docx`
- 推理 PDF：`07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.pdf`

## 结构 QA

- 两本 DOCX 均为 2 sections，与哲学宝典一致。
- 两本 DOCX section page/margin/header/footer/different-first-page 配置均与哲学宝典一致。
- 两本 DOCX 已在 Word 导出 PDF 后重新归一化 TOC 样式：
  - 思维：`TOC1=4 / TOC2=15 / TOC11=0 / TOC21=0`。
  - 推理：`TOC1=8 / TOC2=61 / TOC11=0 / TOC21=0`。
- 两本 DOCX 继续保留 PAGEREF、书签和内部链接：
  - 思维：`PAGEREF=19 / bookmarks=19 / hyperlinks=38`。
  - 推理：`PAGEREF=69 / bookmarks=69 / hyperlinks=138`。

## PDF QA

- 思维 PDF：35 页，文本层门禁通过。
- 推理 PDF：54 页，文本层门禁通过。
- 推理选择题字段：`【完整题干】=36`、`【完整选项】=36`、`【完整题干与选项】=0`。
- 两本 PDF 未命中：
  - `Q refs`
  - `1A/1B/1C/1D`
  - `候选稿门禁`
  - `待回源`

## 视觉抽样

抽样图：

- `08_visual_qa/V15_SECTION_STRUCTURE_CONTACT_SHEET_20260526.png`
- `08_visual_qa/V15_SECTION_STRUCTURE_RENDER_METRICS_20260526.txt`

抽样页：

- 思维：第 1、2、3、5、8、17、35 页。
- 推理：第 1、2、3、5、15、36、54 页。

视觉结论：

- 封面、前言、目录、正文中段、末页均可读。
- 水印可见但不遮挡正文。
- 未见黑页、正文重叠、题干选项截断、页脚丢失。
- 目录和正文之间的 section 切换后页码、页脚、水印保持稳定。

## 限制

本 QA 只证明 V15 本地 Word/PDF 结构和抽样视觉通过；不证明 GPT Pro / Claude 真实外审通过，也不允许写 `PASS`、`TASK_COMPLETE` 或 `最终版`。

