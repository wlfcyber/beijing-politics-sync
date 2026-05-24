# 06 Governor v13.10 Final Check

生成时间：2026-05-23 23:55 +08:00

状态：`v13_10_final_baodian_integrated_pdf_rendered_docx_generated_with_docx_render_caveat`

## Gate 表

| gate | result | evidence |
|---|---|---|
| v13.10 一页考场卡 | pass | `00_v13_10_一页考场卡_学生先读版.md` |
| v13.10 框架章 | pass | `01_双轴法律主观题框架章_v13_10_Confucius三轮修复版.md` |
| 42题逐题解析 | pass | `02_42题双轴重标与解析宝典_v13_10.md` 有 42 道 locked core 正文题 |
| 每题字段 | pass | question id、区年卷题、设问动作、A/B入口、命题路径、评分锚点、材料触发、答案骨架、学生预警、副入口状态均保留 |
| 开放容器分离 | pass | `04_开放容器与不晋升题附录_v13_10.md` 单列，不进入 42 题正文 |
| 真实 GPT/Claude 治理 | pass | Round03/Round05/Round06/Round07 捕获输出均按原文件引用 |
| Confucius 学生试读 | pass | 五轮本地试读最终为 `FRAMEWORK_PASS` |
| traceability | pass | `traceability/TRACEABILITY_MATRIX_v13_10_final.csv` |
| DOCX generated | pass with render caveat | DOCX direct render QA 只有 LibreOffice/soffice 可用时才能声明通过 |
| DOCX Word export visual render | not passed / not claimed | `qa_word_export_render_report.md`: 2026-05-24 rerun hung before producing a QA PDF |
| PDF generated and rendered | pass | `07_RENDER_QA_REPORT_v13_10.md` |

## Governor Verdict

当前允许状态为：`v13_10_final_baodian_integrated_pdf_rendered_docx_generated_with_docx_render_caveat`。

若状态仍为 pending，不得宣称 v13.10 DOCX/PDF 已完整交付。若状态为 `v13_10_final_baodian_integrated_pdf_rendered_docx_generated_with_docx_render_caveat`，可宣称 v13.10 宝典 Markdown/HTML/DOCX/PDF 已生成，PDF 已页面渲染检查，DOCX 已生成但 direct render QA 因本机缺 LibreOffice/soffice 不声明通过。

2026-05-24 addendum: Word COM export/Print-to-PDF was retried for DOCX visual QA and blocked before producing a QA PDF. This does not downgrade the existing PDF-rendered delivery, but it also does not upgrade the DOCX render caveat.
