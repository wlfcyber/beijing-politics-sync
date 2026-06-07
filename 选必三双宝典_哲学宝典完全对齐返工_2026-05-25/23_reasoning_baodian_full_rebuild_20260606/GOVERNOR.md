# GOVERNOR

## Verdict

verdict: `PASS_CONTENT_DOCX_AND_WORD_PDF_RENDER`

## Checks

- 83 条推理题覆盖：83/83。
- 每条含题目材料信息、设问/选项、细则要点、为什么能想到、考生优秀答案：缺失 0 条。
- 每个小题型前有做题方法：62 段。
- 未发现 `/Users`、`C:\\`、`OCR`、`source_extracted`、`A-formal`、`B-choice-signal` 等后台/路径字段：命中 0。
- DOCX 结构验收：zip 完整，段落可提取，83/83 字段计数通过，后台/路径词命中 0。
- Microsoft Word PDF 导出：成功，PDF 大小 2445055 bytes。
- PDF 页面验收：143 页，空白页 0，字段计数仍为 83/83/83/83/83/62，后台/路径词命中 0。
- 视觉抽样：全页缩略图、首/中/末页样张已检查，未见黑页、大片空白、明显错位或文字截断；第 143 页为末条答案结束后的自然留白。

## Boundary

- 接受范围：Markdown 成稿、DOCX 结构、Word 导出 PDF、PDF 页面非空与抽样视觉验收。
- LibreOffice 不作为本轮验收依据；本机 LibreOffice 对最小 DOCX 也无法成功转 PDF。
- 尚未完成外部模型真实审查。
