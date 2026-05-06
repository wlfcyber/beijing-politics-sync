# Findings

Record source discoveries here, especially after PDF/image/browser/OCR/visual reads.

## Source Findings

## 2026-05-04 Phase 03 Visual/OCR Findings

- Local OCR tool check: `tesseract`, `ocrmypdf`, `pytesseract`, PyObjC Vision/Quartz are not available in the current shell; `sips` and PIL are available for image processing/contact sheets.
- Codex A generated contact sheets for blank-text PDFs:
  - `02_extraction/priority_queue_sources/renders/008_Desktop_2025模拟题_2025各区二模_2025海淀二模_试卷_试卷.pdf_contact.jpg`
  - `02_extraction/priority_queue_sources/renders/042_Desktop_2026模拟题_2026各区一模_2026丰台一模_试卷_试卷.pdf_contact.jpg`
- `2025海淀二模` paper visual inventory: Q1-Q22 visible across pages 01-08; Q20 is the key 选必三思维题 and is visible on page 07.
- `2026丰台一模` paper visual inventory: Q1-Q21 visible across pages 01-10; Q18(2) is the key 选必三推理题 and is visible on page 07.
- These visual findings are control/evidence rows only. They remain blocked from student-facing use until Lane B or second visual confirmation closes the relevant blockers.
