# MANFEN_BAODIAN_STATUS

- generated_at: 2026-06-06 CST
- current_candidate: manfen_baodian_v7_0606_a_axis_student_candidate
- source_data: v45 calibrated source/rubric packets
- final_status: NOT_FINAL

## Outputs

- DOCX: `C:\Users\Administrator\Desktop\选必二法律与生活_满分宝典_v7_0606_A轴细则版.docx`
- PDF: `C:\Users\Administrator\Desktop\选必二法律与生活_满分宝典_v7_0606_A轴细则版.pdf`
- MD: `outputs/选必二法律与生活_满分宝典_v7_0606_A轴细则版.md`
- QA: `qa/MANFEN_BAODIAN_v7_0606_QA.md`
- visual QA: `qa/MANFEN_BAODIAN_v7_VISUAL_QA_20260606.md`
- tri-review status: `qa/MANFEN_BAODIAN_v7_TRI_REVIEW_STATUS_20260606.md`
- tri-review prompts: `qa/01_Claude_cowork_应用端逐题审核提示_v7.md`, `qa/02_Claude_Opus48Max_网页版整体审核提示_v7.md`, `qa/03_GPT55Pro_网页版终审提示_v7.md`
- v5 Claude Opus review: `qa/external_review_v5_20260606/claude_opus48max_response.md`
- v6 Claude Opus review after 9-chunk submission: `qa/external_review_v6_20260606/claude_opus48max_response_after_9chunk.md`
- v6 Claude Cowork submission status: `qa/external_review_v6_20260606/claude_cowork_submission_status.md`

## Local Evidence

- Structure: A1-A10 only; each A axis has `本轴知识和答题抓手`, then `相关例题（2024-2026）`.
- Coverage: 74/74 source questions included as example headings; missing titles 0; extra example headings 0.
- Axis counts: A1 5, A2 3, A3 8, A4 12, A5 15, A6 9, A7 3, A8 6, A9 4, A10 9.
- A-axis focus bullets: 40.
- Per-question answer labels: 74.
- Original question images embedded in DOCX: 24.
- DOCX structural scan: zip OK; 1161 XML paragraphs; 0 tables; 24 drawings; 24 media files; no color fills.
- UTF-8 forbidden-term scan: no hits in DOCX or MD for `来源：本轴`, `按细则`, `评分提醒`, `半句不算`, `附中版`, `该层分`, `满分不超过`, `不得分`, `按处理`, `C:/Users/Administrator`, `得分不如`, or `五点中写出`.
- Word-exported PDF fallback: 75 pages.
- Visual spot checks: 2026 延庆一模第18题第1问, 2025 门头沟一模第20题, 2026 海淀一模第18题第3问, 2026 石景山一模第18题 all rendered in the PDF fallback.

## v7 Changes From v6

- Applied Claude Opus required patch for `A2 · 2026 延庆 · 一模 · 第18题第1问`.
- Added the original question image for the 延庆 AI 仿冒公众人物题.
- Transcribed the missing AI 仿冒公众人物直播营销名词解释 and 北京 M 公司/主持人李某案情 into the material text.
- Removed residual student-facing scoring phrases `得分不如` and `五点中写出`.
- Scaled the 2026 石景山一模第18题 high source image and starts that example on a new page to avoid an isolated `原题图` heading page.

## External Review Gates

- Claude Cowork source/rubric-aware per-question review: PENDING; no clean v7 Cowork submission has been completed.
- Claude Opus 4.8 Max web/app overall review: v5 FAIL; v6 second 9-chunk review returned system-level PASS with one required pre-publication patch; v7 applies that patch, but clean v7 re-check is still PENDING.
- GPT-5.5 Pro web/app final review: PENDING; previous browser upload/text submission was blocked.

## Boundary

- This is a local v7 candidate, not final closure.
- `render_docx.py` is still blocked because LibreOffice/`soffice` is unavailable; Word COM PDF export plus PyMuPDF visual spot checks were used as fallback.
- Do not mark final until Claude Cowork, Claude Opus 4.8 Max, and GPT-5.5 Pro gates pass or the user explicitly waives a named gate.
