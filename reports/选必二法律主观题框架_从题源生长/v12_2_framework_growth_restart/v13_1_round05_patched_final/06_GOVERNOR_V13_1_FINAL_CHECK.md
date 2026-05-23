# 06 Governor v13.1 Final Check

生成时间：2026-05-23 16:10 +08:00

状态：`v13_1_final_baodian_round06_confucius_checked_pdf_rendered_docx_generated_with_docx_render_caveat`

## Gate 表

| gate | result | evidence |
|---|---|---|
| GPT Pro Round05终审 | pass | `round05_v13_final_advisor_review/model_outputs/gpt_round05_v13_final_review_pro_web_raw.md`; verdict `ACCEPT_AFTER_MINOR_PATCHES` |
| Claude Opus Round05终审 | pass | `round05_v13_final_advisor_review/model_outputs/claude_round05_v13_final_review_opus47_web_raw.md`; verdict `ACCEPT_AFTER_MINOR_PATCHES` |
| Codex补丁裁决 | pass | `05_Round05_GPT_Claude_终审与补丁裁决.md` |
| 开放容器分离 | pass | `04_开放容器与不晋升题附录.md` keeps reference-only/backfill rows outside the 42 locked core |
| 42题A轴/B轴完整 | pass | `traceability/TRACEABILITY_MATRIX_v13_1_round05_patched.csv` |
| A2-A10支持数 | pass | 所有启用主干至少3题；A1为基础层 |
| DOCX生成 | pass with caveat | `选必二法律与生活_法律宝典_v13_1_Round05补丁终版.docx`; Word COM opened read-only and computed 45 pages / 1191 paragraphs |
| HTML打印源 | pass | `选必二法律与生活_法律宝典_v13_1_Round05补丁终版.html` rebuilt from `01` through `06`, including the open-container appendix |
| PDF渲染 | pass | `选必二法律与生活_法律宝典_v13_1_Round05补丁终版.pdf`; rendered to 26 PNG pages with no blank-like pages |
| PDF内容覆盖 | pass | PDF includes the 42-card handbook, open-container appendix, `ACCEPT_AFTER_MINOR_PATCHES`, Round05 governance, GPT Round06 appendix, and Confucius check |
| GPT Round06终评 | pass | `../round06_gpt_v13_1_final_eval_with_prior_framework/model_outputs/gpt_round06_v13_1_final_eval_with_prior_framework_raw.md`; verdict `ACCEPT_WITH_MINOR_PATCHES`; required two proposition-path patches applied |
| Confucius artifact-only闭环 | pass | `governor_confucius/CONFUCIUS_ARTIFACT_ONLY_CHECK_v13_1.md`; confirms zero-baseline path from material signal to answer skeleton, with DOCX render caveat preserved |
| DOCX直渲染 | not passed / not claimed | `render_docx.py` blocked by missing LibreOffice/soffice (`WinError 2`); Word-open check is recorded separately |

## Governor Verdict

v13.1 supersedes v13.0 as the current final legal-baodian candidate. The allowed final label is:

`v13_1_final_baodian_round06_confucius_checked_pdf_rendered_docx_generated_with_docx_render_caveat`

This means Markdown, traceability CSV, DOCX, HTML, PDF, PDF page-render QA, and Confucius artifact-only closure exist. It does not mean DOCX direct visual-render QA passed, because this Windows host lacks LibreOffice/soffice.
