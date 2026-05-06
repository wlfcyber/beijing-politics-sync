# Word/PDF QA After Global Rubric-Point Repair

time: 2026-05-04 16:55 CST

## Outputs

- Markdown: `/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03/09_delivery/选必一_当代国际政治与经济_完整学生讲义_最终闭环版_20260504.md`
- DOCX: `/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03/09_delivery/选必一_当代国际政治与经济_完整学生讲义_最终闭环版_20260504.docx`
- PDF: `/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03/09_delivery/选必一_当代国际政治与经济_完整学生讲义_最终闭环版_20260504.pdf`

## Checks

- Markdown structure: 47 main questions, 47 scoring-point summaries, 197 rubric-point rows.
- Reverse term coverage: 197 / 197 audit rows found inside their corresponding question sections.
- DOCX structure: open/save in Microsoft Word succeeded; document XML present; red run count = 4326.
- PDF text QA: 146 pages; first-sample scoring terms extract from PDF text.
- Forbidden-term scan: PASS.

## Render Fallback

`render_docx.py` could not run because LibreOffice `soffice` is not installed on this Mac. This is a recorded fallback, not a render PASS. Validation used Microsoft Word open/save, DOCX OOXML checks, generated PDF QA, and text extraction.
