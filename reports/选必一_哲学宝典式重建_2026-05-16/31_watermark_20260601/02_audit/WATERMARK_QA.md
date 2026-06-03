# WATERMARK_QA

## Result

PASS.

## Files

- Source DOCX: `/Users/wanglifei/Desktop/选必一6.1最终版.docx`
- Watermarked DOCX: `/Users/wanglifei/Desktop/选必一6.1最终版_带水印.docx`
- Watermarked PDF: `/Users/wanglifei/Desktop/选必一6.1最终版_带水印.pdf`

## Checks

- DOCX source was not overwritten.
- DOCX contains one watermark header part with text `飞哥正志讲堂`.
- User reported the first watermark was too light in Word; final version uses darker VML fill `#7F7F7F` with opacity `.38`.
- One section has both default and first-page header references, covering the first page and the rest of the document.
- PDF exported through Microsoft Word from the watermarked DOCX.
- PDF page count: 313.
- Rendered sample pages: 1, 2, 50, 157, 313.
- Visual sample check: watermark is visible in PDF and Word editing view;正文 readable; no observed content overlap on sampled pages.

## Hashes

- source DOCX: `98d3a7d0de2b66cd5c41a3ab14753c1a489ff81b0a58c9eb7819ad47e32b74aa`
- watermarked DOCX: `b1cf99c36f8576734b63fec208975601d13202b3c095e955cff9eade37653bc4`
- watermarked PDF: `fffbe6f403b17e8a0131de4435ef26bcd22e4af6051ce38883d5919881515553`
