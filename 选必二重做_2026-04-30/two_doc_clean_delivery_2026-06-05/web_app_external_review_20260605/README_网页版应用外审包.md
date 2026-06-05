# 选必二 v7 网页版/应用外审包

本包用于满足“Claude Opus 4.8 Max 和 GPT-5.5 Pro 只能用网页版或应用才算”的正式外审要求。

## 包内文件

- `outputs/`：两份 v7 学生稿 DOCX 和 Markdown。
- `qa/`：本地 QA、渲染 QA、CLI 外审作废说明。
- `gpt55_chunks/`：GPT-5.5 Pro 分块终审提示。
- `00_CLAUDE_OPUS48MAX_WEB_REVIEW_PROMPT.md`：Claude 正式复审入口提示。
- `00_GPT55PRO_WEB_REVIEW_SEQUENCE.md`：GPT-5.5 Pro 正式终审顺序。

## 当前状态

- 本地 v7 已生成。
- 本地硬噪音扫描通过。
- 本地 DOCX 渲染通过：汇编 137 页，宝典 143 页。
- CLI 外审结果全部作废，不计入正式闭环。
- 下一步必须使用 Claude 网页版/应用和 ChatGPT 网页版/应用重新取得有效 verdict。
