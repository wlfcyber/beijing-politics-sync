# V29 DOCX/PDF QA

时间：2026-05-26T14:18:00+08:00

verdict: `DOCX_PDF_QA_PASS_LOCAL_NOT_FINAL`

## 文件

- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.docx`
- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.pdf`
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.docx`
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.pdf`

## DOCX 检查

- `updateFields`: 0。
- `document.xml` 中 `fldChar`: 0。
- `document.xml` 中 `instrText`: 0。
- `document.xml` 中 `PAGEREF`: 0。
- 页脚仍保留 `PAGE` 页码域，不涉及外部文件提示。
- 思维 DOCX：`TOC1` styleId=1、pStyle=4；`TOC2` styleId=1、pStyle=15；`TOC11/TOC21` styleId 与 pStyle 均为 0。
- 推理 DOCX：`TOC1` styleId=1、pStyle=8；`TOC2` styleId=1、pStyle=62；`TOC11/TOC21` styleId 与 pStyle 均为 0。
- 用 Microsoft Word 通过普通打开方式打开思维 DOCX，未出现“是否更新域”弹窗。

## PDF 检查

- 思维 PDF：29 页；`【材料触发点】` 65，`【设问】` 65，`【为什么能想到】` 65，`【答案落点】` 65。
- 推理 PDF：49 页；`【材料触发点】` 83，`【设问】` 83，`【为什么能想到】` 83，`【答案落点】` 83。
- PDF 学生正文扫描：`这题`、`这道题`、`单独挂题`、`必须在`、`第一段`、`第二段`、`第一层`、`第二层`、`第一步`、`第二步`、`题目不是`、`正式细则`、`source-lock`、`后台`、`候选`、`P2`、`real_call_pending`、`blocked_advisor` 均为 0。
- Quick Look 已生成两本 PDF 首页缩略图并人工查看：首页标题、署名、居中与留白正常。

## 仍不可写最终 PASS

- GPT Pro 真实审核仍未完成。
- Claude verdict 仍为 `P2_POLISH`。
- 本 QA 只能证明当前 DOCX/PDF 本地生成和打开体验通过，不能替代外审。
