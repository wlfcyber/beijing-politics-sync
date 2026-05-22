# DOCX/PDF QA - Student Pure V4

Timestamp: 2026-05-20T12:58:42+0800

## Files Checked

- Markdown: `12_final_baodian/选必二法律主观题满分宝典_学生纯净版_20260520.md`
- DOCX: `12_final_baodian/选必二法律主观题满分宝典_学生纯净版_20260520.docx`
- PDF: `12_final_baodian/word_pdf_v4/选必二法律主观题满分宝典_学生纯净版_20260520.pdf`
- Render samples: `12_final_baodian/word_pdf_v4/rendered_pngs/`

## Structural Checks

- Student pure DOCX: 753 paragraphs, 0 tables, 70,811 bytes.
- Student training DOCX: 959 paragraphs, 0 tables, 79,547 bytes.
- Student pure PDF exported through Microsoft Word: 54 pages, 827,652 bytes.
- PyMuPDF text extraction found 0 blank-text pages.
- Rendered sample pages: 1, 2, 3, 10, 20, 30, 40, 50, 53, 54.

## Student-Facing Clean Scan

The student pure Markdown was scanned for explicit backend/audit terms:

`评标|评分细则|阅卷细则|reference_only|evidence_level|source_clean|classification_trust|PASS_CORE|DEBUG|TODO|证据等级|参考答案|原答案| formal |rubric`

Result: no matches in the student pure Markdown.

## Acceptance Status

`VISUAL_QA_SAMPLE_PASS_WITH_GUARDS`

The DOCX/PDF pipeline is usable: Word export succeeded, PDF is not blank, and rendered sample pages are readable. This is not a full human page-by-page typography proofread; it is a technical/render acceptance plus sample visual check.

## Non-Negotiable Guard

This QA does not convert V4 into a four-lane final PASS. V4 still has:

- 65-question corpus: 61 formal, 4 reference_only, 0 missing.
- Classification trust: 39 high, 24 medium, 2 source_check.
- Pressure status: 32 PASS_CORE, 20 PASS_CORE_WITH_SOURCE_NOTE, 11 CONTAINER_NOT_CORE, 2 PARTIAL_SOURCE_CLEAN.
- Real GPTPro and Claude Opus V4 external second review: packet prepared, not yet cleanly captured.

