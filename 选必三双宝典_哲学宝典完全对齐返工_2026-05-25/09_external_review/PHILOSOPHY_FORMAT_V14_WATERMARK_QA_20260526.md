# PHILOSOPHY_FORMAT_V14_WATERMARK_QA_20260526

verdict: `LOCAL_VISUAL_QA_PASS_NOT_FINAL`

## Files Checked

- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.docx`
- `07_docx_pdf/选必三_逻辑与思维_思维宝典_哲学完全对齐版.pdf`
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.docx`
- `07_docx_pdf/选必三_逻辑与思维_推理宝典_哲学完全对齐版.pdf`

## Visual Sample

- Contact sheet: `08_visual_qa/V14_WATERMARK_CONTACT_SHEET_20260526.png`
- Render metrics: `08_visual_qa/V14_WATERMARK_RENDER_METRICS_20260526.txt`

Sampled pages:

- 思维 p1, p2, p3, p4, p22, p23, p35
- 推理 p1, p2, p3, p4, p5, p36, p54

## Results

- Watermark appears from the front-matter/body pages and remains light enough not to cover text.
- Cover pages remain clean.
- TOC pages keep dot leaders and page numbers.
- Body pages show no text overlap, black page, clipped heading, missing footer, or unreadable watermark.
- PDF page counts remain stable: 思维 `35`, 推理 `54`.

## Structural Checks

- 思维 DOCX watermark object count in headers: `1`
- 推理 DOCX watermark object count in headers: `1`
- 思维 directory paragraph styles: `TOC1=4 / TOC2=15 / TOC11=0 / TOC21=0`
- 推理 directory paragraph styles: `TOC1=8 / TOC2=61 / TOC11=0 / TOC21=0`
- Plain DOCX text `Q refs=0`; lettered work split headings `1A/1B/1C/1D=0`.

## Boundary

This is a local Word/PDF QA pass only. It does not satisfy GPT Pro or Claude real external review, and it does not upgrade the run to final.
