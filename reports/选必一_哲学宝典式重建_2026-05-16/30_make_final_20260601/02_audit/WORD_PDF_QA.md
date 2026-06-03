# Word/PDF QA

## Word Open Check

- File opened in Microsoft Word from Desktop:
  `/Users/wanglifei/Desktop/选必一_当代国际政治与经济_主观题术语宝典_最终版_20260601.docx`
- Word status bar: `第 1 页，共 312 页`
- Word word-count display: `261749 个字`

## PDF Export

- Exported through Word UI as:
  `/Users/wanglifei/Desktop/选必一_当代国际政治与经济_主观题术语宝典_最终版_20260601.pdf`
- PDF copied to run output:
  `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/30_make_final_20260601/03_outputs/选必一_当代国际政治与经济_主观题术语宝典_最终版_20260601.pdf`
- PDF page count via `pypdf`: 312
- PDF SHA256: `743a6db2448219aa784d7a1509f87cd6a7babdccb8357ee085a8fa3218491349`

## Render QA

`render_docx.py` could not run because `soffice` is not installed on this Mac. Fallback QA used Word UI + Word PDF export + PDFKit page render sampling.

Rendered sample pages:

- page 1: cover
- page 2: table of contents
- page 4: first content page
- page 30: economic globalization start
- page 98: political multipolarity start
- page 157: China start
- page 222: United Nations start
- page 312: final page

Sample renders are stored under:

`/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/30_make_final_20260601/02_audit/pdf_pages/`
