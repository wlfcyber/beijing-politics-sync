# RENDER_QA_LIMITATION_20260606

## Status

- DOCX generated: `delivery/选必三逻辑与思维_推理宝典_按类型完整题源细则优秀答案版_20260606.docx`
- DOCX text/zip QA: PASS.
- LibreOffice render QA: not usable on this machine.
- Microsoft Word PDF export: PASS.
- PDF page render QA from Word-exported PDF: PASS.

## Attempts

1. `render_docx.py` through LibreOffice with the original long path.
   - Result: timed out after about 4 minutes.
   - Output: no PNG/PDF.
2. `render_docx.py` through LibreOffice after copying the DOCX to a short temp path.
   - Result: timed out after about 6 minutes.
   - Output: no PNG/PDF.
3. Microsoft Word COM `ExportAsFixedFormat`.
   - Result: timed out after about 6 minutes.
   - Output: no PDF.
4. Simplified DOCX rebuild.
   - Result: DOCX paragraph count reduced from 2610 to 1210 while preserving all required field counts.
5. `render_docx.py` through LibreOffice after simplified rebuild.
   - Result: failed with exit code 1 on both the repo path and a short temp path.
   - Control check: a minimal smoke-test DOCX also failed to convert through LibreOffice, so this is a local LibreOffice conversion-chain problem rather than proof of DOCX content failure.
6. Microsoft Word COM `ExportAsFixedFormat` after simplified rebuild.
   - Result: PASS.
   - Output: `qa/word_export_simplified/reasoning_baodian_v23_word_export.pdf`.
7. PDF render QA from the Word-exported PDF.
   - Result: PASS.
   - Evidence: `qa/PDF_RENDER_QA_20260606.json`, `qa/pdf_render_qa/all_pages_contact_sheet.png`, and first/middle/last sample pages.

## Boundary

Do not claim LibreOffice acceptance for this DOCX. It is acceptable to claim Word-exported PDF page acceptance: 143 pages, no blank pages, all required marker counts preserved, and no forbidden backend/path terms detected.

## Next Repair Options

- If a LibreOffice-native proof is required later, repair the host LibreOffice conversion chain first, using a minimal DOCX as the control.
- If publication polish is requested, add a final human pagination pass in Word from the already exported PDF/page samples.
