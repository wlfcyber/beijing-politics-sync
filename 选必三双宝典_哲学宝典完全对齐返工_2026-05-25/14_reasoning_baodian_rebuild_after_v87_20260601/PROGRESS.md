# PROGRESS

## 2026-06-01T00:20:00+08:00 Start

- status: `IN_PROGRESS`
- 已确认 V87 被撤回，不再作为最终版或可交付宝典。
- 本 run 路线：V17 学生化正文为主体，V87 回源核验表仅作纠错索引。
- 下一步：抽取 V17 文本并检查高风险答案源、选择题教学层和正文污染。

## 2026-06-01T00:45:00+08:00 Student-layer Rebuild Delivered

- status: `DELIVERED_FOR_USER_REVIEW`
- 已生成新的学生化推理宝典，不继承 V87 原题摘录包正文。
- 桌面交付：
  - `/Users/wanglifei/Desktop/选必三推理宝典_重做版_20260601.docx`
  - `/Users/wanglifei/Desktop/选必三推理宝典_重做版_20260601.md`
  - `/Users/wanglifei/Desktop/选必三推理宝典_重做版_20260601.pdf`
  - `/Users/wanglifei/Desktop/选必三推理宝典_重做版_自查验收_20260601.md`
- 文本门禁：`【材料触发点】=83`，`答案选=36`，`错项分析=36`，`参考答案/评标/评分标准/路径/OCR=0`。
- V87 高风险答案源点全部在新正文命中正确答案：海淀二模 5D/6A/7A，石景山一模 5D，东城一模 7A/8D，丰台二模 8C，顺义一模 7A，朝阳二模 7D。
- DOCX 域门禁：`fldChar=0`，`instrText=0`，`externalLink=0`，用于避免 Word 域更新提示。
- PDF 由 Microsoft Word 导出，44 页；已做文本层检查、Quick Look 缩略图和抽样页面渲染。
- 限制：本步不宣称 GPT Pro / Claude 真实外审 PASS；`render_docx.py` 因本机无 `soffice` 未能使用，已改用 Word/PDF/Quick Look 检查。
