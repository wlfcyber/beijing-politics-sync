# DEVELOPMENT_PLAN

1. 锁定用户二级框架与哲学宝典样式源。
2. 从 Claude 修订稿与 ENTRY_INDEX 建立可修订条目数据。
3. 将 25 号核查 run 中的明确错误、来源阻塞、待人工确认项写入修订矩阵。
4. 先修硬错：设问改写、得分层次错误、无来源分值分配、过粗细则层级。
5. 对 235 条逐条生成 `PASS / ISSUE_FIXED / BLOCKED / NEEDS_MANUAL` 证据状态。
6. 生成 Markdown 终极稿，严格使用用户二级框架。
7. 按哲学宝典样式生成 DOCX。
8. 渲染 DOCX 做版面检查；若 LibreOffice 不可用，做 OOXML/Quick Look 结构检查并明确说明。
9. 输出最终 DOCX、Markdown、修改清单、残余阻塞清单。
