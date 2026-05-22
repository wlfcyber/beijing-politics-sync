# Source Manifest Processing Log

generated_at: 2026-05-19T00:00:00+08:00
source_files_seen: 403
failed_or_ocr_gap_rows: 51

## Source Roots
- /Users/wanglifei/Desktop/2024模拟题 :: exists
- /Users/wanglifei/Desktop/2025模拟题 :: exists
- /Users/wanglifei/Desktop/2026模拟题 :: exists
- /Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中 :: exists
- /Users/wanglifei/GaokaoPolitics/2024各区模拟题 :: exists
- /Users/wanglifei/GaokaoPolitics/2025各区模拟题 :: exists
- /Users/wanglifei/GaokaoPolitics/2026各区模拟题 :: exists

## Missing Roots
- none

## File Type Counts
- doc: 18
- docx: 137
- pdf: 165
- pptx: 53
- rtf: 2
- unknown: 26
- xlsx: 2

## Suspected Role Counts
- answer: 15
- evaluation_standard: 58
- lecture: 16
- marking_report: 31
- paper: 85
- subjective_rubric: 103
- unknown: 81
- user_framework: 14

## Text Layer Status Counts
- corrupted: 8
- image_pdf: 39
- no_text_layer: 4
- old_word: 18
- ppt: 51
- text_layer: 257
- unknown: 26

## Archive Notes
- no archives found inside approved raw source roots

## Tool Notes
- PDF extraction: PyMuPDF text extraction.
- DOC/DOCX/RTF/PPTX extraction: python-docx, python-pptx, or macOS textutil.
- OCR: tesseract is unavailable in PATH; text-empty PDFs were rendered to 00_manifest/rendered_pages and recorded in failed_files.csv.
- Old 选必二 generated artifacts are not used as evidence in this manifest step.
