# BLINE_FUSION_BATCH1_DOCX_PDF_QA_20260526

timestamp: `2026-05-26T05:45:50+08:00`

verdict: `DOCX_PDF_REBUILT_AFTER_BATCH1_VISUAL_QA_SAMPLE_PASS_NOT_FINAL`

## Rebuilt Files

- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.docx`：`2026-05-26 05:41:39`，72K
- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.pdf`：`2026-05-26 05:42:53`，464K，27 页
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.docx`：`2026-05-26 05:41:39`，84K
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.pdf`：`2026-05-26 05:43:35`，604K，40 页

## Text-Layer Checks

思维 PDF 宽松关键词检索结果：

- `顺义一模`：第 3、4 页；
- `海淀二模 Q20`：第 10、11 页；
- `朝阳期中`：第 11、19、20、22、23、25、26 页；
- `海淀二模 Q17`：第 6、9、10、18 页；
- `客观性`、`预见性`、`可检验性`、`发散思维`、`逆向思维` 均能在文本层检出。

注：Word 导出的 PDF 会在标题中插入空格，例如 `2026 朝阳期中`，因此精确字符串 `2026朝阳期中(2025-11) Q21(2)` 不适合直接作为 PDF 文本层检索条件。

## Visual QA

新抽样图：

- `08_visual_qa/思维宝典_抽样视觉QA_contact_sheet_20260526_blinefusion1_targeted.png`
- `08_visual_qa/推理宝典_抽样视觉QA_contact_sheet_20260526_blinefusion1_targeted.png`

抽样页：

- 思维：1、2、3、10、19、20、22、25、26、27 页，覆盖封面、目录、科学思维硬样本、海淀 Q20、朝阳 Q21(2) 多节点、末页；
- 推理：1、2、3、11、21、34、40 页，覆盖封面、目录、主要章节入口和末页。

抽样结论：

- 未见页面大面积空白、黑屏、内容重叠或明显截断；
- 思维 Q21(2) 的三新、发散聚合、超前、联想迁移想象、逆向节点均已进入 PDF；
- 页眉页脚存在，目录页可见；
- Word 辅助树会把加粗文本读成 Markdown 样式标记，但 PDF 文本层和渲染页未见前台 `**` 星号残留。

## Synced Packages

- `09_external_review/` 四个 Word/PDF 已同步为本批重建版本；
- `09_external_review/选必三双宝典_外审包_real_call_pending_20260526.zip` 已刷新，时间戳 `2026-05-26 05:45:50`；
- `06_governor_confucius/fresh_context_blind_test/student_packet_20260526/thinking_handbook.pdf` 已刷新；
- `06_governor_confucius/fresh_context_blind_test/student_packet_20260526/reasoning_handbook.pdf` 已刷新；
- `06_governor_confucius/fresh_context_blind_test/student_packet_20260526.zip` 已刷新，时间戳 `2026-05-26 05:45:50`。

## Remaining Gates

- 本 QA 只覆盖本批重建后的抽样视觉和文本层，不是全书逐页人工审读；
- 推理册仍未完成 B 线厚内容差异融合；
- GPT Pro / Claude 真实审查仍为 `real_call_pending`；
- fresh-context 盲测尚未实际作答；
- 最终 Governor / Confucius 尚未通过，不得写 `PASS` 或最终版。
