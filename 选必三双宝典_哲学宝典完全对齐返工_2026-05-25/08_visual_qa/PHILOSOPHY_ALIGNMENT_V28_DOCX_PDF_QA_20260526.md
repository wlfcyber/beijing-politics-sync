# V28 Word/PDF QA

verdict: `DOCX_PDF_REFRESHED_NOT_FINAL`

## 文件

- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.docx`
- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.pdf`
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.docx`
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.pdf`

桌面同步文件夹：

- `/Users/wanglifei/Desktop/选必三双宝典_Word版_20260526`

## 核验结果

- 思维 PDF：29 页；`材料触发点=65`、`设问=65`、`为什么能想到=65`、`答案落点=65`、`主观题=65`、`选择题=0`。
- 推理 PDF：49 页；`材料触发点=83`、`设问=83`、`为什么能想到=83`、`答案落点=83`、`主观题=47`、`选择题=36`。
- `2024西城一模 第19题第（5）问`：思维 PDF 命中 1；推理 PDF 命中 0。
- V28 新增多节点条目已进入 PDF：`2024东城一模 18(3)`、`2026延庆一模 18(2)`、`2026石景山一模 17(2)`、`2026丰台二模 21` 均可检出。
- 学生正文/PDF 中 `real_call_pending`、`blocked_advisor`、`source-lock`、`正式细则`、`细则` 均为 0。

## Word 域提示处理

用户反馈 Word 反复提示“该文档包含的域可能引用了其他文件。是否更新该文档中的这些域?”。本轮已处理：

- 修改 `tools/build_handbook_docs.py`，不再写入 `w:updateFields=true`。
- 移除当前两个 DOCX 中的 `w:updateFields` 设置。
- 用 Microsoft Word 重新打开 DOCX 测试，未再出现该提示。
- 用 Microsoft Word 重新导出两本 PDF。

## 阻断

- GPT Pro 真实审核仍未完成。
- Claude V27 verdict 为 `P2_POLISH`，不是 PASS。
- V28 是本地内容错挂修补与交付件刷新，不能称最终版。
