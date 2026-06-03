# PHILOSOPHY_FORMAT_V4_DOCX_PDF_QA_20260526

verdict: `QA_SAMPLE_PASS_V4_NOT_FINAL`

## Files Checked

- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.docx`
- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.pdf`
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.docx`
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.pdf`

## DOCX Structure QA

| 项目 | 思维宝典 | 推理宝典 |
| --- | --- | --- |
| margins dxa | `1191/1219/1134/1219` | `1191/1219/1134/1219` |
| first page header/footer | empty / empty | empty / empty |
| running header | empty | empty |
| footer | `— PAGE —` | `— PAGE —` |
| TOC style names | `toc 1`, `toc 2` | `toc 1`, `toc 2` |
| TOC style IDs | `TOC1`, `TOC2` | `TOC1`, `TOC2` |
| PAGEREF fields | 19 | 8 |
| internal links | 19 | 8 |
| bookmarks | 19 | 8 |

## PDF QA

| 项目 | 思维宝典 | 推理宝典 |
| --- | --- | --- |
| PDF pages | 34 | 50 |
| text chars | 35573 | 47653 |
| forbidden/backend hits | 0 | 0 |
| page 1 | title/subtitle/signature/preface only | title/subtitle/signature/preface only |
| page 2 | `— 2 —` + TOC | `— 2 —` + TOC |

Forbidden/backend scan included:

`候选稿门禁`、`答案表`、`待回源`、`以原卷为准`、`题干触发点`、`先写`、`要写`、`本题需要`、`设问要求`、`采分点`、`A-formal`、`B-choice`、`source-lock`、`Codex`、`Claude`、`GPT`、`PAGEREF`。

## Visual QA

Generated contact sheet:

- `08_visual_qa/双宝典_philosophy_format_v4_contact_sheet_20260526.png`

Sample pages:

- 思维：page 1, 2, 3, 18, 34
- 推理：page 1, 2, 3, 26, 50

Visual sample result:

- no black pages
- no obvious overlap
- no obvious truncation
- cover title no longer breaks `宝典`
- TOC visible with dotted leaders and page numbers
- footer starts from page 2, matching philosophy-like frontmatter cleanliness

## Boundary

这是抽样视觉 QA，不是逐页人工校读；最新版式 V4 尚未重新跑 fresh-context 盲测，真实 GPT Pro / Claude 仍为 `real_call_pending`。
