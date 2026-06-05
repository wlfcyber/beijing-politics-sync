# 选必二 v16 网页版/应用外审包

本包用于 Claude Opus 4.8 Max 和 GPT-5.5 Pro 网页版/应用复审。CLI 结果无效，不计入正式外审闭环。

## 内容

- `outputs/`: v16 两份学生稿 DOCX/MD。
- `qa/`: 本地 QA、渲染 QA、关键页截图/拼图、CLI 作废说明，以及 v16 渲染 PDF。
- `gpt55_chunks/`: GPT-5.5 Pro 分块审稿提示。图片路径已替换为“已内嵌”占位，避免网页审稿误判 Markdown 本地路径。
- `00_CLAUDE_OPUS48MAX_WEB_REVIEW_PROMPT.md`: Claude 网页/应用复审提示。
- `00_GPT55PRO_WEB_REVIEW_SEQUENCE.md`: GPT 网页/应用复审顺序。
