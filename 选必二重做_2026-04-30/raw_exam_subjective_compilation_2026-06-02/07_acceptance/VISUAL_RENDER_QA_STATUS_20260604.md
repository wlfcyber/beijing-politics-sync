# VISUAL_RENDER_QA_STATUS_20260604

## Target

- Desktop DOCX: `C:\Users\Administrator\Desktop\选必二法律与生活_主观题细则宝典_学生版_20260604.docx`
- Repo DOCX: `05_output\选必二法律与生活_主观题细则宝典_学生版_20260604.docx`
- Current DOCX size: 107177 bytes.

## Renderer Status

- LibreOffice / `soffice`: not available in this Windows environment.
- Word COM smoke test: passed. Word version `16.0`, path `C:\Program Files\Microsoft Office\Root\Office16`.
- DOCX open / repaginate test: passed. Open 0.31s, repaginate 0.39s, Word-computed pages 57, paragraphs 921, tables 60.
- Full Word PDF export: timed out after 240s and produced no full PDF.
- Word PDF export page 1: succeeded.
- Word PDF export page 2: timed out after 60s.
- Word PDF export pages 1-10: timed out after 120s.
- Word-converted temporary DOCX pages 1-10 export: still timed out after 120s.

Conclusion: the DOCX opens and paginates in Word, but the PDF export path is not usable for this file in the current environment. The failure is an export-pipeline limitation, not a document-open failure.

## Word Visible Screenshot QA

Because PDF/LibreOffice rendering was unavailable, I used visible Microsoft Word rendering as the fallback visual gate.

- Screenshot directory: `07_acceptance\word_visible_page_screenshots_20260604`
- Page screenshots: 57 files, `page_001.png` through `page_057.png`.
- Screenshot dimensions: all page screenshots validated at 2576 x 1408 or equivalent large-window size; invalid count 0.
- Contact sheets: `contact_sheet_01.png` through `contact_sheet_05.png`.
- Human visual scan:
  - Contact sheets for pages 1-57 inspected.
  - Detailed pages inspected: page 002 quick-reference section, page 004 body start, page 046 dense body page, page 055 appendix start.
  - No gross blank pages, horizontal table overflow, page-wide clipping, severe overlap, or broken card/table structure observed.

## Formatting Mark Caveat

The visible Word screenshots show local Word formatting marks, especially manual line-break arrows. These are not document text:

- XML text scan counts: U+21B5, U+21A9, U+21B2, and pilcrow U+00B6 all equal 0.
- The visible arrows come from this machine's Word view setting for non-printing formatting marks and do not print as student-facing characters.

## Remaining Limitation

This is stronger than the previous structural-only check, but it is still not the official `render_docx.py` / LibreOffice PNG gate. The current verified scope is:

- DOCX opens in Word.
- Word computes 57 pages.
- All 57 visible Word page screenshots exist and were visually scanned.
- No obvious gross layout failure was found.

Not verified:

- LibreOffice-rendered page PNGs.
- A full exported PDF.
