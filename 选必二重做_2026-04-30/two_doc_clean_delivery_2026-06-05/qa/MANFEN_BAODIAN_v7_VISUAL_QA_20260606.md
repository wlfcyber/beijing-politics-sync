# 满分宝典 v7 视觉与结构 QA

- Date: 2026-06-06 CST
- DOCX: `C:\Users\Administrator\Desktop\选必二法律与生活_满分宝典_v7_0606_A轴细则版.docx`
- PDF: `C:\Users\Administrator\Desktop\选必二法律与生活_满分宝典_v7_0606_A轴细则版.pdf`
- PDF pages: 75

## Local structural checks

- 74/74 example headings present; missing titles 0; extra titles 0.
- A1-A10 order PASS; A-axis structure issues 0.
- A-axis focus bullets 40; per-question answer labels 74.
- Original question images embedded: 24.
- DOCX scan: zip OK; tables 0; drawings 24; media 24; non-white fills 0.
- MD forbidden scan PASS for: 来源：本轴, 按细则, 评分提醒, 半句不算, 附中版, 该层分, 满分不超过, 不得分, 按处理, C:/Users/Administrator, 得分不如, 五点中写出.

## Opus-required patch check

- 2026 延庆一模第18题第1问 now includes the original question image.
- The missing AI 仿冒公众人物直播营销名词解释 and 北京 M 公司/李某 case facts are transcribed into the material text.
- This removes the v6 issue where the case could only be inferred from answer points.

## Visual spot checks

- Render method: Word COM exported PDF, then PyMuPDF page image render for visual inspection.
- `render_docx.py` could not run because LibreOffice/soffice is unavailable on this machine.
- Spot pages rendered: 7, 8, 59, 64, 73, 74, 75.
- 2026 延庆一模第18题第1问: image renders, material text continues, no overlap observed.
- 2025 门头沟一模第20题: source image renders.
- 2026 海淀一模第18题第3问: source image renders.
- 2026 石景山一模第18题: image initially forced an isolated heading page; v7 final scales this high image to 5.6 inches and starts the example on a new page. Final check shows title, 原题图, image, and material start on the same page.

## Boundary

- This is a local QA PASS for v7 structure and rendering fallback.
- It is not final delivery closure until Claude Cowork source/rubric review, Claude Opus 4.8 Max re-check, and GPT-5.5 Pro final review are cleanly completed.
