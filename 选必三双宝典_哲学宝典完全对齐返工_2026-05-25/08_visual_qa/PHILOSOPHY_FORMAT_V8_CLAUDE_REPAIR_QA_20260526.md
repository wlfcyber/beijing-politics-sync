# PHILOSOPHY_FORMAT_V8_CLAUDE_REPAIR_QA_20260526

- version: V8 Claude real-review repair
- source_review: `09_external_review/CLAUDE_REAL_REVIEW_RAW_FORMAT_V7_20260526.md`
- adjudication: `09_external_review/CLAUDE_REAL_REVIEW_ADJUDICATION_V8_20260526.md`
- docx_dir: `07_docx_pdf`
- contact_sheet: `08_visual_qa/双宝典_philosophy_format_v8_claude_repair_contact_sheet_20260526.png`

## Rebuild

- rebuilt DOCX with `tools/build_handbook_docs.py`;
- exported PDFs through Microsoft Word;
- accepted Word's field-update prompt so internal PAGEREF / TOC fields could refresh.

## Current Artifacts

- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.docx`
- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.pdf`
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.docx`
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.pdf`

## Structural QA

- 思维 PDF: 34 pages.
- 推理 PDF: 52 pages.
- 推理主观题 `【设问】`: 44/44.
- Forbidden/backend scan hits in student PDFs: 0 for:
  - `本卡`
  - `本节点`
  - `错项卡`
  - `全错项卡`
  - `复挂`
  - `这一处只`
  - `同一题在这里`
  - `这一题在这里`
  - `这里抓`
  - `这里看`
  - `不再重复写`
  - `思维方法链`
  - `哲学宝典式`
  - `错项专项`

## Claude P1 Spot Checks

- `2026丰台一模 Q18(2)` `【设问】` 已在 PDF 文本层检出。
- `2025丰台期末 Q9` 所在节点已改为 `不相容选言推理无效式辨析`，未再出现 `本卡`、`错项专项`、`全错项卡`。
- `2026门头沟一模 Q6` EAST 题干已修复 `磁约 / 束`、`再 / 次` 异常断词；PDF 仍按正常版面在 `磁约束` 后换行，不属于词内断裂。
- `2026朝阳一模 Q5` 体育题干已修复 `排 / 球` 与 `赛 / 场` 词内断裂；PDF 文本层检出 `校园足球、篮球和排球`，未检出 `排\n球` 或 `赛\n场`。

## Visual QA

抽样页已渲染为 contact sheet：

- 思维 p1、p2、p4、p24、p26、p28、p34
- 推理 p1、p3、p4、p9、p23、p41、p47、p52

抽样结果：未见黑页、明显遮挡、页脚丢失、目录页码缺失或正文重叠。推理 p47 的体育题干已能正常显示 `排球` 与 `赛场`。

## Remaining Gate

本轮只是 V8 本地修补与 QA，不是最终通过：

- Claude 需要对 V8 重新真审后才能解除 `P1_REVISE`。
- GPT Pro 真实审查仍为 `real_call_pending / blocked_advisor`。
- V8 还需重新同步 fresh-context 包并按最终门禁复测。

