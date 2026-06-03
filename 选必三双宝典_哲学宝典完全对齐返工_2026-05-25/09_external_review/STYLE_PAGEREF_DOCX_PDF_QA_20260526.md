# STYLE_PAGEREF_DOCX_PDF_QA_20260526

verdict: `QA_SAMPLE_PASS_NOT_FINAL`

## Scope

本轮 QA 覆盖 `STYLE_PAGEREF_ALIGNMENT_PATCH_20260526` 后重新生成的两本 DOCX/PDF。

## Files

- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.docx`
- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.pdf`
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.docx`
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.pdf`

## DOCX Structure

| 文件 | `PAGEREF` | 内部链接 | 书签 | 页边距 dxa |
| --- | ---: | ---: | ---: | --- |
| 思维宝典 | 19 | 19 | 19 | 1191/1219/1134/1219 |
| 推理宝典 | 8 | 8 | 8 | 1191/1219/1134/1219 |

## PDF QA

| 文件 | PDF 页数 | 文本层字符数 | 禁词/后台词命中 |
| --- | ---: | ---: | --- |
| 思维宝典 | 27 | 36189 | 0 |
| 推理宝典 | 41 | 48288 | 0 |

扫描词包括：`候选稿门禁`、`答案表`、`待Codex`、`待回源`、`正式版必须`、`以原卷为准`、`题干触发点`、`先写`、`要写`、`本题需要`、`设问要求`、`采分点`、`REVIEW_ONLY`、`correct_option_chain`、`source_pool`、`question_id`、`A-formal`、`B-choice-signal`、`/Users/`、`OCR`、`debug`、`P0`、`P1`、`PASS`、`final`、`定义联项`、`AI 助教`、`电动汽车续航`、`人体免疫系统`、`企业风险控制`、`社区闲置厂房`、`使用口令`。

## Visual Samples

- `08_visual_qa/双宝典_style_pageref_patch_v2_contact_sheet_20260526.png`

抽样页：

- 思维宝典：p1、p2、p3、p13、p27
- 推理宝典：p1、p2、p3、p20、p41

抽样观察：封面页、目录页、正文页、末页均可读；未见黑页、重叠、明显截断或页脚丢失。

## Boundary

本 QA 只证明本轮 Word/PDF 结构与抽样视觉通过；真实 GPT Pro / Claude 外审仍未完成。
