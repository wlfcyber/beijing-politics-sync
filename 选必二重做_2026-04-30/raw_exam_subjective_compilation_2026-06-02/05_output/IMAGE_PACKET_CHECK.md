# IMAGE_PACKET_CHECK

timestamp: 2026-06-02T14:35:05+08:00

## Outputs

- Image-only Word document: `05_output/选必二法律与生活_习题汇编_2024-2026_图片版.docx`
- Desktop convenience copy: `/Users/wanglifei/Desktop/选必二法律与生活_习题汇编_2024-2026_图片版.docx`
- Image packet ledger: `05_output/image_packet_assets/image_packet_report.csv`
- Image packet builder: `tools/build_image_packet_docx.py`
- Rubric crop review: `05_output/RUBRIC_CROP_REVIEW.md`

## Checks

- Entries: 60
- Word `Heading 2` question headings: 60
- Inline images: 135
- Floating/anchored images: 0
- Tables in Word: 0
- Forbidden text-section markers absent: `【材料】`, `【设问】`, `【细则】`, `分数分布`
- Every entry has at least one question image and at least one rubric image.
- PDF rubric assets that are neither local crops nor locked-text fallback images: 0
- Quick Look first-page thumbnail generated at `05_output/rendered_word/选必二法律与生活_习题汇编_2024-2026_图片版.docx.png`.

## Source Rendering Notes

- PDF question sources were rendered as original page images.
- PDF rubric sources are no longer admitted as full-page rubric screenshots: 17 PDF rubric rows use original local crops, while 1 row (`E024`) uses a locked-rubric-text small image because the visible original scan is incomplete.
- Non-PDF sources (`.docx`, `.doc`, `.pptx`) cannot be directly rasterized page-by-page in this local environment without LibreOffice/soffice; their locked source-packet text was rendered into non-editable images instead.
- The image packet ledger records these fallback cases in `question_note` and `rubric_note`.
