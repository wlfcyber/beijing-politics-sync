# PHILOSOPHY_FORMAT_V4_HARD_ALIGNMENT_PATCH_20260526

verdict: `FORMAT_ALIGNMENT_ADVANCED_V4_NOT_FINAL`

## Trigger

继续按用户“格式内容上都要完全对齐哲学宝典”的目标自查时，重新对比哲学宝典 Word 本体与两本选必三 Word，发现上一版仍有几处格式硬差距：

- 选必三封面和正文页有运行页眉，哲学宝典没有运行页眉，封面更干净。
- 选必三页脚是 `第 N 页`，哲学宝典视觉形态是居中 `— N —`。
- 选必三目录样式在 Word 中显示为 `TOC 11/TOC 21`，哲学宝典本体存在并使用 `toc 1/toc 2`。
- 选必三正文标签色为蓝色 `1F4E79`，哲学宝典四标签色为 `21574C`。
- 选必三正文 Normal 字体为宋体/Times New Roman，哲学宝典 Normal 字体体系为 Microsoft YaHei/Arial。
- 长标题在 PDF 封面中把“宝典”拆成两行，视觉上不够像哲学宝典。
- Markdown/Word 中部分四标签后无空格，哲学宝典四标签后有自然空格。

## Patch Applied

修改 `tools/build_handbook_docs.py`：

- 正文字体改为 `Microsoft YaHei`，西文改为 `Arial`；封面标题仍保留黑体 + Times New Roman。
- Heading 样式按哲学宝典本体调整：
  - Heading 1：18pt，`1F4E79`
  - Heading 2：14pt，`2F6F9F`
  - Heading 3：11.5pt，`3A6278`
- 正文四标签色改为 `21574C`。
- 移除运行页眉；设置首页不同页眉页脚，封面页无页脚。
- 页脚改为居中 `— PAGE —`。
- 强制创建 `TOC1/toc 1` 与 `TOC2/toc 2` 样式，避免 Word 中出现 `TOC 11/TOC 21`。
- 标题过长时自适应降为 19pt，避免封面断词。
- 目录备用页码同步为新版 PDF 实际页码，防止打开 Word 时不更新域导致旧页码显示。

机械清理两本 Markdown：

- 为 `【材料触发点】`、`【设问】`、`【为什么能想到】`、`【答案落点】`、`【完整题干与选项】`、`【答案】`、`【正确理由】`、`【诱人错项和错因】` 后补自然空格。

## Current DOCX Structural Evidence

### 思维宝典

- Pages in PDF: 34
- Margins: `1191/1219/1134/1219 dxa`
- Header: empty
- First-page footer: empty
- Footer style: `— PAGE —`
- Styles: `toc 1` x4, `toc 2` x15, `Heading 1` x4, `Heading 2` x15, `Heading 3` x61
- TOC fields: 19 `PAGEREF`, 19 internal hyperlinks, 19 bookmarks
- TOC style XML: `TOC1/toc 1`, `TOC2/toc 2`

### 推理宝典

- Pages in PDF: 50
- Margins: `1191/1219/1134/1219 dxa`
- Header: empty
- First-page footer: empty
- Footer style: `— PAGE —`
- Styles: `toc 1` x8, `Heading 1` x8, `Heading 2` x61, `Heading 3` x80
- TOC fields: 8 `PAGEREF`, 8 internal hyperlinks, 8 bookmarks
- TOC style XML: `TOC1/toc 1`, `TOC2/toc 2`

## PDF Text Evidence

- 思维 PDF page 1 starts with title/subtitle/signature/preface only; no running header and no page footer.
- 推理 PDF page 1 starts with title/subtitle/signature/preface only; no running header and no page footer.
- Page 2 of both PDFs begins with `— 2 —` and `目录`.
- PDF text layer scan: forbidden/backend terms hit 0 for both books.

## Boundary

本补丁解决的是最新发现的格式硬差距，不新增题源、不改变知识实质、不替代真实 GPT Pro / Claude 审查。由于本轮 PDF 页码和版式已变化，上一轮本地 fresh-context 通过只能作为正文迁移能力参考；严格说，最新版 V4 PDF 尚未重新跑 fresh-context 盲测。因此当前仍不得称最终版。
