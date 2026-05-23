# 06 Governor v13.0 Final Check

生成时间：2026-05-23 15:20 +08:00

状态：`v13_0_final_baodian_pdf_rendered_docx_generated_with_docx_render_caveat`

## Gate 表

| gate | result | evidence |
|---|---|---|
| 错误 GPT 账号捕获排除 | pass | Round04 adjudication 已标记 `INVALID_FOR_GATE_WRONG_CHATGPT_ACCOUNT` |
| GPT Pro 网页输出有效 | pass | `gpt_round04_double_axis_framework_review_pro_web_raw_fullpage_clipboard.md` |
| Claude Opus 4.7 Adaptive 网页输出有效 | pass | `claude_round04_double_axis_framework_review_opus47_web_raw_fullpage_clipboard.md` |
| v12.2 保留为回滚基线 | pass | v12.2 目录未覆盖，本版另建 v13.0 目录 |
| 42题 A轴主标签 | pass | `traceability/TRACEABILITY_MATRIX_v13_0_double_axis.csv` missing=0 |
| 42题 B轴动作标签 | pass | `traceability/TRACEABILITY_MATRIX_v13_0_double_axis.csv` missing=0 |
| 启用 A轴节点支持数 | pass | A2-A10 均至少 3 题；A1 为基础层不计 primary 门槛 |
| 开放容器未晋升 | pass | `04_开放容器与不晋升题附录.md` |
| PDF 交付 | pass | `选必二法律与生活_法律宝典_v13_0_双轴版.pdf` |
| PDF 渲染检查 | pass | `rendered_pdf_pages/page-001.png` through `page-030.png`; no blank-like pages; sampled 001/015/030 |
| DOCX 交付 | pass with caveat | `选必二法律与生活_法律宝典_v13_0_双轴版.docx`; Word COM opened read-only and computed 45 pages |
| DOCX 直渲染 | caveat | `render_docx.py` blocked by missing LibreOffice/soffice (`WinError 2`); do not claim DOCX-render-QA-passed |

## Governor 结论

v13.0 双轴法律宝典的 Markdown、CSV、DOCX、HTML、PDF 和 PDF 渲染检查文件均已生成。可用状态为 `v13_0_final_baodian_pdf_rendered_docx_generated_with_docx_render_caveat`。边界：DOCX 已生成且 Word 可打开，但本机缺少 LibreOffice，未完成 DOCX 直渲染 QA。
