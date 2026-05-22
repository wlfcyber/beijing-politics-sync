# V6.7 学生使用版 DOCX QA

- DOCX: `/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长/12_final_baodian/选必二法律主观题满分训练宝典_v6_7_学生使用版_20260521.docx`
- QuickLook 首屏缩略图: `/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长/12_final_baodian/word_pdf_v6_7_student/qlthumb/选必二法律主观题满分训练宝典_v6_7_学生使用版_20260521.docx.png`
- Paragraphs: 1451
- Tables: 34
- Headings: 327

## 结构检查

- DOCX exists: PASS
- QuickLook thumbnail exists: PASS
- Has title: PASS
- Has 27 core boundary: PASS
- Has 38 non-core boundary: PASS
- No raw reference_only: PASS
- No raw source-check: PASS
- No candidate wording: PASS

## 渲染说明

- `render_docx.py` 路线失败：本机缺少 `soffice`/LibreOffice。
- Microsoft Word AppleScript 导出 PDF 超时，未生成可用 PDF。
- 已生成 QuickLook 首屏缩略图并人工查看：首屏标题、边界说明、速记表清晰，无明显重叠或空白。
- 因无法完成全页 PNG 渲染，本 DOCX 只能标为“结构 QA + 首屏缩略图 QA 通过”，不能标为全页视觉 QA 通过。
