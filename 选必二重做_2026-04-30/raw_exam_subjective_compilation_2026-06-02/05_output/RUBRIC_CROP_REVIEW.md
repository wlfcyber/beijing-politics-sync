# RUBRIC_CROP_REVIEW

timestamp: 2026-06-02T14:35:05+08:00

## Current Image Packet

- Word document: `05_output/选必二法律与生活_习题汇编_2024-2026_图片版.docx`
- Image ledger: `05_output/image_packet_assets/image_packet_report.csv`
- Builder: `tools/build_image_packet_docx.py`

## Structural Checks

- Entries: 60
- Word `Heading 2` question headings: 60
- Inline images: 135
- Floating/anchored images: 0
- PDF rubric assets that are neither local crops nor locked-text fallback images: 0
- Forbidden text-section markers absent from Word body: `【材料】`, `【设问】`, `【细则】`, `分数分布`

## PDF Rubric Handling

- PDF rubric source rows: 18
- Original PDF local-crop rows: 17
- Original PDF local-crop images: 22
- PDF rubric rows converted to locked-rubric-text images because the available original scan was incomplete or no reliable full original crop could be made: 1

### Original PDF Local Crops

- E001 2024 · 东城 · 一模 · 第19题
- E002 2024 · 东城 · 二模 · 第19题第1问
- E003 2024 · 东城 · 二模 · 第19题第2问
- E005 2024 · 朝阳 · 二模 · 第17题
- E015 2025 · 东城 · 一模 · 第19题
- E016 2025 · 东城 · 二模 · 第19题
- E021 2025 · 房山 · 一模 · 第19题
- E034 2025 · 西城 · 期末 · 第19题
- E041 2026 · 东城 · 一模 · 第18题
- E042 2026 · 东城 · 二模 · 第19题
- E047 2026 · 朝阳 · 期末 · 第18题第1问
- E050 2026 · 海淀 · 一模 · 第18题第3问
- E051 2026 · 海淀 · 二模 · 第18题第2问
- E055 2026 · 西城 · 二模 · 第18题第1问
- E056 2026 · 西城 · 二模 · 第18题第2问【待确认】
- E057 2026 · 西城 · 二模 · 第18题第3问【待确认】
- E059 2026 · 通州 · 一模 · 第20题

### PDF Locked-Text Fallback Rows

- E024 2025 · 朝阳 · 期末 · 第20题

## Spot Checks

- E001/E002/E003: right-half answer-page crops tightened to the exact 19题/19题第1问/19题第2问 segments.
- E005 p2/p3: main rubric crop plus one-line continuation crop; no next-question text visible after margin reduction.
- E041 p7/p8: retained the two original rubric-detail pages; false-positive p9 and p11 excluded.
- E042 p2/p3: cover page skipped; retained only rubric/marking-detail crops.
- E047: cropped only 18(1), stopping before 18(2).
- E051 p54/p55: retained answer paragraph plus score-distribution table, with the full `总说` row visible.

## Residual Limitation

E024 remains a locked-rubric-text image. The visible original scan page only contains the beginning of 第20题 and cuts off the continuing rubric, so replacing it with an original crop would produce an incomplete细则 image.
