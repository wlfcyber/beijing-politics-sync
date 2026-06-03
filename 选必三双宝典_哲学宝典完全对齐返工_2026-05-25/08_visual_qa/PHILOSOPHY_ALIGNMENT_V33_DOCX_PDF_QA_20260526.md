# V33 DOCX/PDF QA

时间：2026-05-26T15:35:00+08:00

verdict: `DOCX_PDF_REFRESHED_WORD_PROMPT_FIXED_NOT_FINAL`

## 输出文件

- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.docx`
- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.pdf`
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.docx`
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.pdf`

## 文档层 QA

- 思维 DOCX：`updateFields=0`，`PAGEREF=0`，external relationships = 0。
- 推理 DOCX：`updateFields=0`，`PAGEREF=0`，external relationships = 0。
- 思维 DOCX：`未定义书签=0`，`分析与综合、整体性与系统观念=0`。
- 思维 DOCX 可检出新节点：`分析与综合`、`整体性与系统观念`、`动态性、质量互变与发展过程`、`矛盾分析与适度原则`。
- Word 设置核验：`update links at open=false`。
- Microsoft Word 真实打开桌面思维 DOCX：无“是否更新域”弹窗。

说明：DOCX 中仍保留页脚 `PAGE` 动态页码域，这是页码正常显示所需；本轮已关闭 Word 打开时的更新询问，并确保目录页码 `PAGEREF` 不再残留。

## PDF 文本 QA

- 思维 PDF：29 页，抽取文本 32387 字符。
- 推理 PDF：49 页，抽取文本 56516 字符。
- 思维 PDF：`未定义书签=0`。
- 思维 PDF：旧合并标题 `分析与综合、整体性与系统观念=0`。
- 思维 PDF 新节点命中：
  - `分析与综合`：19
  - `整体性与系统观念`：2
  - `动态性、质量互变与发展过程`：4
  - `矛盾分析与适度原则`：2

## 桌面同步

桌面目录：`/Users/wanglifei/Desktop/选必三双宝典_Word版_20260526`

SHA256：

- 思维 DOCX：`d6b3ec36821f942db1361f0c2678ad38bde30dd10105c2844d264181e1dc5650`
- 思维 PDF：`b60222f11851c5182e31c66b3fe66f468a93ba1966758518a8c8ea7b1ebf1cf5`
- 推理 DOCX：`18cb2632dd5304a0c96cb7abdbfc7cb4ef34227ce5cff7e5129621c0fbf5fddb`
- 推理 PDF：`e53b60b233cb291137c5d4b2f3d572dacef3a8d96257cbcd129ff4f14219c665`

以上 SHA 与 run 内 `07_docx_pdf` 输出一致。

## 结论边界

V33 通过本地 DOCX/PDF 文件体验与结构 QA，但不是最终验收；GPT Pro 真实审核、Claude PASS、V33 fresh-context 盲测均未完成。
