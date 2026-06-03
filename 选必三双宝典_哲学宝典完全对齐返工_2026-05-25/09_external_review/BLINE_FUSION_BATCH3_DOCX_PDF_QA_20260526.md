# B Line Fusion Batch3 DOCX/PDF QA 2026-05-26

verdict: `BATCH3_DOCX_PDF_REFRESHED_SAMPLE_QA_PASS_NOT_FINAL`

## 文件刷新

- 思维 Word：`07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.docx`
- 思维 PDF：`07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.pdf`
- 推理 Word：`07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.docx`
- 推理 PDF：`07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.pdf`
- Word 导出 PDF 时出现域更新提示，已选择“不更新”，保持手工页码目录稳定。

## PDF 文本层检查

- 思维 PDF：27 页，文本层约 36295 字符。
- 推理 PDF：40 页，文本层约 48429 字符。
- 禁词/后台词命中：0。
- 扫描词包含：`候选稿门禁`、`答案表`、`待回源`、`以原卷为准`、`题干触发点`、`先写`、`要写`、`本题需要`、`设问要求`、`采分点`、`question_id`、`A-formal`、`B-choice-signal`、`定义联项`、`AI 助教`、`电动汽车续航`、`人体免疫系统`、`企业风险控制`、`社区闲置厂房`。

## 本批靶向命中

- 思维 PDF 第 17 页命中：`传统产业是未来产业的基础和起点`。
- 思维 PDF 第 26 页命中：`野生近缘种`。
- 思维 PDF 第 25、26 页命中：`联想迁移`。
- 推理 PDF 第 25 页命中：`橘因水土不同`。
- 推理 PDF 第 28、29 页命中：`真包含`。
- 推理 PDF 第 28 页命中：`新型举国体制`。

## 视觉抽样

新增抽样图：

- `08_visual_qa/思维宝典_抽样视觉QA_contact_sheet_20260526_batch3.png`
- `08_visual_qa/推理宝典_抽样视觉QA_contact_sheet_20260526_batch3.png`

抽样页：

- 思维：1、2、15、24、25、26、27 页。
- 推理：1、2、25、26、34、35、40 页。

人工目检结论：封面、目录、类比章节、概念外延章节、逻辑规律章节、联想复挂页和尾页未见黑底、重叠、明显截断、页脚丢失或选项组大面积破碎。

## 仍未通过最终验收

- GPT Pro 真实审查：`real_call_pending`。
- Claude 真实审查：`real_call_pending`。
- fresh-context 零基础盲测尚未运行。
- Governor / Confucius 尚未以本批 Word/PDF 通过最终 artifact-only 验收。
