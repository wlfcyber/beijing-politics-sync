# PHILOSOPHY_FORMAT_V14_WATERMARK_AND_FRAMEWORK_ORDER_AUDIT_20260526

verdict: `LOCAL_V14_WATERMARK_QA_PASS_NOT_FINAL`

## 本轮自审发现

1. 思维框架顺序需要以用户上传 PDF 为准，而不是只看本 run 早期 benchmark 中的概括句。
   - 用户框架 PDF：`/Users/wanglifei/Desktop/先前框架/逻辑与思维 思维部分 原文件 拷贝.pdf`
   - PDF text extraction shows the sequence: `科学思维 -> 辩证思维 -> 认识发展历程 -> 创新思维`.
   - 当前思维稿正文顺序与 PDF 一致：`一、科学思维 -> 二、辩证思维 -> 三、认识发展历程 -> 四、创新思维`。
   - 因此本轮不移动正文一级模块；只修正控制口径中可能诱导后续线程误改顺序的表述。

2. 哲学宝典本体含有浅色斜向 `飞哥正志讲堂` 水印，当前 V13 两本 DOCX/PDF 没有该水印。
   - 哲学参照：`/Users/wanglifei/Desktop/哲学宝典最终版 5.2双终极融合版_目录页码美化版_副本.docx`
   - 参照 DOCX header contains `PowerPlusWaterMarkObject_CodexFGZZJT`.
   - V13 DOCX header watermark count was 0.

## 本轮修补

- `tools/build_handbook_docs.py` 新增与哲学宝典同源的 VML watermark shape：
  - text: `飞哥正志讲堂`
  - fill: `#a6a6a6`
  - opacity: `19661f`
  - rotation: `315`
  - page-centered placement
- 保持封面首页清爽：当前 Word 仍使用 first-page header/footer 分离；水印从前言、目录、正文页起出现。
- 重建两本 DOCX，并用 Microsoft Word 导出 PDF。
- 重新归一化目录段落样式，保证目录正文仍用 `TOC1/TOC2`。

## 当前实测

- 思维 DOCX header watermark: `1`
- 推理 DOCX header watermark: `1`
- 思维 PDF pages: `35`
- 推理 PDF pages: `54`
- PDF rendered watermark is visible and light; no page shows black background, overlap, or unreadable body text.
- 思维 DOCX directory paragraph styles: `TOC1=4 / TOC2=15 / TOC11=0 / TOC21=0`
- 推理 DOCX directory paragraph styles: `TOC1=8 / TOC2=61 / TOC11=0 / TOC21=0`
- Plain DOCX text: `Q refs=0`, `1A/1B/1C/1D=0`
- 推理选择题 labels remain: `【完整题干】=36`, `【完整选项】=36`, `【完整题干与选项】=0`

## 继续阻断

- GPT Pro real review is still `real_call_pending / blocked_advisor`.
- Latest true Claude verdict is still V9 `CONDITIONAL_PASS`, not `PASS`.
- V14 is a local philosophy-format watermark and framework-order audit patch. It cannot be called final or complete.
