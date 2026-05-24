# 07 Render QA Report v13.10

Status: `v13_10_final_baodian_integrated_pdf_rendered_docx_generated_with_docx_render_caveat`

Date: 2026-05-23

## Produced Files

- Combined Markdown: `选必二法律与生活_法律宝典_v13_10_Confucius框架终版.md`
- DOCX candidate: `选必二法律与生活_法律宝典_v13_10_Confucius框架终版.docx`
- HTML print source: `选必二法律与生活_法律宝典_v13_10_Confucius框架终版.html`
- PDF delivery: `选必二法律与生活_法律宝典_v13_10_Confucius框架终版.pdf`
- PDF page renders: `rendered_pdf_pages/page-001.png` through final page

## Verification

| check | result | evidence |
|---|---|---|
| traceability row count | pass | `TRACEABILITY_MATRIX_v13_10_final.csv` has 42 rows |
| Markdown card count | pass | `02_42题双轴重标与解析宝典_v13_10.md` has 42 `###` cards |
| v13.10 framework gate | pass | Confucius local reader closure says `FRAMEWORK_PASS` and delivery patch verified |
| open-container separation | pass | `04_开放容器与不晋升题附录_v13_10.md` exists outside the 42-card body |
| real GPT/Claude boundary | pass | no new GPT/Claude call claimed; real captured Round03/Round05/Round06/Round07 outputs are referenced |
| HTML print source | pass | `选必二法律与生活_法律宝典_v13_10_Confucius框架终版.html` |
| PDF generated | pass (1549009 bytes) | `选必二法律与生活_法律宝典_v13_10_Confucius框架终版.pdf` |
| PDF text coverage | pass | required tokens: v13.10, Confucius, CC0251, locked core, A4+A6 |
| PDF pages rendered | pass (30 pages -> 30 PNG) | `rendered_pdf_pages/` |
| blank-page check | pass | blank-like pages: none |
| DOCX generated / structural check | pass (88684 bytes; paragraphs=1003; tables=19) | python-docx open check |
| DOCX Word COM open check | pass: Word COM opened read-only; pages=55; paragraphs=1684 | `qa_word_com_check.txt` |
| DOCX Word export / Print-to-PDF visual render | not passed / not claimed | `qa_word_export_render_report.md`: Word export and Microsoft Print to PDF hung without producing a QA PDF on 2026-05-24 |
| DOCX direct render via `render_docx.py` | not passed / not claimed | not passed: render_docx failed; LibreOffice/soffice unavailable on this machine. python.exe : Traceback (most recent call last): |

## Governor Note

The PDF delivery is rendered from the v13.10 HTML print source and then rasterized to page PNGs for blank-page and sample visual checks. The DOCX exists and is structurally readable. A 2026-05-24 Word-export rerun confirmed that Word COM can open and paginate the DOCX, but Word PDF export and Microsoft Print to PDF hung without producing a QA PDF. This machine also has no LibreOffice/soffice path, so DOCX direct visual-render QA is not claimed.
