# 选必三推理宝典重做版自查验收

- verdict: `PASS_LOCAL_STUDENT_LAYER_REBUILD_FROM_V17`
- base: V17 学生化推理宝典正文
- V87 role: 只作回源纠错索引，不作学生正文主体

## Student Layer Checks

- 四标题条目：材料触发点 83 / 设问 83 / 为什么能想到 83 / 答案落点 83
- 选择题标题：36
- 选择题答案句 `答案选`：36
- 选择题错项分析：36

## Pollution Gate

- `参考答案`: 0
- `题号 |`: 0
- `评标`: 0
- `评分标准`: 0
- `/Users`: 0
- `OCR`: 0
- `source_extracted`: 0
- `A-formal`: 0
- `B-choice-signal`: 0
- `correct_option_chain`: 0

## V87 High-risk Source Corrections Checked In Student Body

| item | expected | found | status |
|---|---:|---:|---|
| 2026海淀二模 第5题 | 答案选D | 答案选D | PASS |
| 2026海淀二模 第6题 | 答案选A | 答案选A | PASS |
| 2026海淀二模 第7题 | 答案选A | 答案选A | PASS |
| 2026石景山一模 第5题 | 答案选D | 答案选D | PASS |
| 2024东城一模 第7题 | 答案选A | 答案选A | PASS |
| 2024东城一模 第8题 | 答案选D | 答案选D | PASS |
| 2026丰台二模 第8题 | 答案选C | 答案选C | PASS |
| 2025顺义一模 第7题 | 答案选A | 答案选A | PASS |
| 2024朝阳二模 第7题 | 答案选D | 答案选D | PASS |

## DOCX Field Gate

- `fldChar`: 0
- `instrText`: 0
- `externalLink`: 0

## Visual / Openability QA

- DOCX Quick Look thumbnail generated: `qa/quicklook/选必三推理宝典_重做版_20260601.docx.png`。
- Microsoft Word PDF export succeeded; final PDF copied to both run delivery and Desktop short path.
- PDF text layer: 44 pages; `【材料触发点】=83`，`答案选=36`，`错项分析=36`，`参考答案/评标/评分标准=0`。
- PDF rendered sample pages `1/2/3/11/21/31/44` into `qa/pdf_render/contact_sheet.jpg`；抽样未见空白页、正文遮挡或明显断裂。
- `render_docx.py` LibreOffice path failed because this Mac has no `soffice`；本轮改用 Word PDF export + Quick Look + PyMuPDF page render QA。

## Boundary

- 本版不宣称 GPT Pro / Claude 真实外审 PASS。
- 本版内容未继承 V87 原题摘录包，只继承 V87 已发现的答案源风险点作为核对清单。
