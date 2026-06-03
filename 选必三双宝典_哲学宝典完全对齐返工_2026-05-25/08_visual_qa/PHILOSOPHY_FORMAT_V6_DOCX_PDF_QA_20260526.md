# PHILOSOPHY_FORMAT_V6_DOCX_PDF_QA_20260526

verdict: `QA_SAMPLE_PASS_V6_NOT_FINAL`

## Files Checked

- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.docx`
- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.pdf`
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.docx`
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.pdf`

## DOCX Structure QA

| 项目 | 思维宝典 | 推理宝典 |
| --- | --- | --- |
| PAGEREF fields | `19` | `69` |
| internal links | `19` | `69` |
| bookmarks | `19` | `69` |
| zero fallback page fields | `0` | `0` |
| `哲学宝典` XML leakage | `0` | `0` |

## PDF QA

| 项目 | 思维宝典 | 推理宝典 |
| --- | --- | --- |
| PDF pages | `35` | `52` |
| page 1 | cover only | cover only |
| page 2 | `— 2 —` + `前言` | `— 2 —` + `前言` |
| TOC | page 3 | pages 3-4 |
| first body page | page 4 | page 5 |
| forbidden/backend hits | `0` | `0` |

Forbidden/backend scan included:

`哲学宝典`、`完全对齐`、`审计`、`后台`、`本包`、`外审`、`候选稿`、`答案表`、`待回源`、`以原卷为准`、`题干触发点`、`先写`、`要写`、`本题需要`、`设问要求`、`采分点`、`A-formal`、`B-choice`、`source-lock`、`Codex`、`Claude`、`GPT`、`PAGEREF`、`学生要`、`学生最容易`、`本题应先`、`提醒学生`。

## Visual QA

Generated contact sheet:

- `08_visual_qa/双宝典_philosophy_format_v6_contact_sheet_20260526.png`

Sample pages:

- 思维：page 1, 2, 3, 4, 35
- 推理：page 1, 2, 3, 4, 52

Visual sample result:

- cover, preface, TOC, first body and final pages render cleanly
- no black pages, overlap, obvious truncation or footer loss in sampled pages
- reasoning TOC now exposes H2 reasoning-form nodes rather than only 8 chapter headings

## Boundary

This V6 QA verifies the local patched DOCX/PDF surface after Claude P0/P1/P2 adjudication. It does not replace fresh-context blind testing or refreshed GPT Pro / Claude review.
