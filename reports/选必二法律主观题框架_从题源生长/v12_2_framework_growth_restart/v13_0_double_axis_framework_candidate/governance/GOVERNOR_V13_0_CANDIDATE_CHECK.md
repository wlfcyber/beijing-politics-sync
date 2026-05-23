# 06 Governor v13.0 Candidate Check

生成时间：2026-05-23 14:35 +08:00

状态：`v13_0_double_axis_candidate_markdown_csv_complete_docx_pdf_pending`

## Gate 表

| gate | result | evidence |
|---|---|---|
| 错误 GPT 账号捕获排除 | pass | Round04 adjudication 已标记 `INVALID_FOR_GATE_WRONG_CHATGPT_ACCOUNT` |
| GPT Pro 网页输出有效 | pass | `gpt_round04_double_axis_framework_review_pro_web_raw_fullpage_clipboard.md` |
| Claude Opus 4.7 Adaptive 网页输出有效 | pass | `claude_round04_double_axis_framework_review_opus47_web_raw_fullpage_clipboard.md` |
| v12.2 保留为回滚基线 | pass | v12.2 目录未覆盖，本版另建 v13.0 目录 |
| 42题 A轴主标签 | pass | missing=0 |
| 42题 B轴动作标签 | pass | missing=0 |
| 启用 A轴节点支持数 | pass | under_supported=0；A1 为基础层不计 primary 门槛 |
| 开放容器未晋升 | pass | `04_开放容器与不晋升题附录.md` |
| DOCX/PDF v13.0 交付 | pending | 本候选里程碑尚未生成 v13.0 DOCX/PDF |

## Governor 结论

v13.0 的 Markdown 和 CSV 双轴候选版已经存在，可以作为新的框架候选基线。不得宣称 `final_baodian_pdf_delivered` 或 `TASK_COMPLETE`，因为 v13.0 DOCX/PDF 和渲染检查尚未完成。
