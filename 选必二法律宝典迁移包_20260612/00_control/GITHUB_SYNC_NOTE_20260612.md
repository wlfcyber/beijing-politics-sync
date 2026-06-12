# GitHub 同步说明 2026-06-12

本目录用于把“选必二法律宝典 / 法律主观题框架线”的可接手文件迁移到 GitHub，方便另一台机器直接 `git pull` 后接手。

## 本次同步范围

本包保留三组文件：

- `v13_10_final_baodian_integrated/`：带 DOCX/PDF 的 v13_10 Confucius 框架终版包，含渲染 QA、最终报告和治理文件。
- `v14_5_final_markdown_baodian_claude_pass_hardened/`：最新 Markdown 候选宝典，含 42 题框架解析、开放容器、traceability、GPT/Claude 治理证据和 v14.5 Governor 记录。
- `v15_student_baodian_revision_20260604/`：学生本 Word 修订包，含 Claude 下载版、v15 学生本强化版、修订脚本和原同步说明。

## 当前主入口

另一台机器接手时优先看：

1. `v15_student_baodian_revision_20260604/选必二法律与生活_学生宝典_v15学生本强化版_20260604.docx`
2. `v15_student_baodian_revision_20260604/SYNC_REPORT_20260604.md`
3. `v14_5_final_markdown_baodian_claude_pass_hardened/00_READ_ME_FIRST.md`
4. `v14_5_final_markdown_baodian_claude_pass_hardened/选必二法律与生活_法律宝典_v14_5_最终Markdown候选版.md`

## 边界说明

本包是“可拉取交接包”，不是新的内容终审。沿用原有边界：

- v15 同步报告明确说明：v15 代表学生本形态修订和 GitHub 留档，不代表内容终审、真实学生实测或项目 Governor 最终闭环。
- v14.5 Governor 允许的说法是：`MARKDOWN_FRAMEWORK_AND_42_QUESTION_BAODIAN_EXTERNAL_MODEL_PASS_HARDENED_NO_DOCX_PDF`。它是最新 Markdown 候选，不声称 DOCX/PDF 交付。
- v13_10 是较早的带 DOCX/PDF 渲染包，用于回看可视化交付形态和历史治理闭环，不应压过 v14.5/v15 的后续修订边界。

## Word 文件

本包内 `.docx` 文件已作为迁移范围的一部分进入 GitHub；由于本仓库默认会忽略 Word 文件，提交时需要显式 force-add。
