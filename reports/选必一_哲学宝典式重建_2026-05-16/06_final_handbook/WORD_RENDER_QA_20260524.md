# 选必一终稿 Word 页面渲染 QA

检查时间：2026-05-24

## 结论

PASS。

学生厚版与考前导航版均已完成 DOCX -> PDF -> PNG 页面渲染，并通过程序检查与视觉抽查。未发现空白页、整页裁切、明显重叠、表格溢出或页脚异常。

## 渲染链路

本机最初缺少 LibreOffice，已安装 `TheDocumentFoundation.LibreOffice 26.2.3.2`。`render_docx.py` 在 Windows 上直接调用仍不稳定：`soffice.exe` 会挂起；改用临时 shim 后，脚本传入的 `-env:UserInstallation=file://C:\...` 路径格式又导致 LibreOffice 返回失败。

因此采用等效且可复现的页面渲染链路：

1. 将正式 DOCX 复制为 ASCII 临时文件名，避免 LibreOffice 命令行输出和文件名编码干扰。
2. 用 `C:\Program Files\LibreOffice\program\soffice.com --headless --norestore --nodefault --nofirststartwizard --convert-to pdf` 导出 PDF。
3. 用 bundled Python 的 PyMuPDF/fitz 1.27.2.3 按 150 DPI 将 PDF 渲染为 `page-<n>.png`。
4. 用 PIL 对所有页面做尺寸、文件大小、非空白像素检查，并生成 contact sheet 逐组目检。

## 证据

| 文档 | PDF 大小 | PNG 页数 | PNG 尺寸 | 空白/近空白页 | 输出目录 |
|---|---:|---:|---|---:|---|
| 学生厚版 | 3,996,805 bytes | 200 | 1275 x 1650 | 0 | `word_render_qa_20260524_student_manual/` |
| 考前导航版 | 899,425 bytes | 20 | 1754 x 1241 | 0 | `word_render_qa_20260524_nav_manual/` |

视觉检查：

- 学生厚版：已查看 `contact_sheet_01.png` 至 `contact_sheet_10.png`，覆盖 p1-p200。
- 考前导航版：已查看 `contact_sheet_01.png`，覆盖 p1-p20。
- 原尺寸抽查：学生厚版 p1、p28、p100、p199；考前导航版 p5、p20。

## 保留说明

页面渲染 QA 已闭合；但这不是 `render_docx.py` 原脚本直接成功，而是在确认其 Windows 兼容问题后，用同一 DOCX -> PDF -> PNG 验收目标的等效链路完成。GPT Pro 终稿复核仍未闭合，不能因此把整项外部复核链声明为全 PASS。
