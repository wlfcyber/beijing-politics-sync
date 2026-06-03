# WORD_PREVIEW_QA_20260528

## 结论

- DOCX 可由 Microsoft Word 正常打开。
- Word 状态栏显示：113 页，139286 个字。
- Quick Look 已生成首页预览 PNG：`render_preview/选必一_当代国际政治与经济_主观题术语宝典_237条_二级结构版_20260528.docx.png`
- 首页预览可见标题、二级结构说明、目录与二级容器；未见空白页或打开失败。

## 限制

- 本机未检出 `soffice` / LibreOffice，无法按 documents 渲染脚本完成全页 PNG 渲染。
- 尝试用 Microsoft Word 脚本导出 PDF 未成功，原因是当前 Word AppleScript `save as` 调用不兼容；未把 PDF 作为本轮交付口径。

## 本轮交付口径

本轮以 DOCX、Markdown、二级映射表和结构 QA 为正式交付；Word 打开性与首页预览通过，但不声明完成全页 PDF/PNG 渲染。

