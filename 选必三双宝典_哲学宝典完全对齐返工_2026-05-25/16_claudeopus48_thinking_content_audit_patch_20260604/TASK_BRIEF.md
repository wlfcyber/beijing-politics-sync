# TASK_BRIEF

- run: `16_claudeopus48_thinking_content_audit_patch_20260604`
- created_at: 2026-06-04
- trigger: 用户提供 Claude Opus 4.8 Max 审核表，要求“按照内容逐条完善修正”选必三思维宝典。
- audit input:
  - `/Users/wanglifei/Library/Application Support/Claude/local-agent-mode-sessions/2c0a1a14-78ce-4ddc-8f72-9d4f74dbff6e/703c2d6a-ade6-4ee8-94a4-92b2abb47bf1/local_784c886e-8842-48ae-918a-63ee3d8b7909/outputs/选必三思维宝典_内容审核报告.xlsx`
- base artifact:
  - Claude 实际上传底稿：`inputs/选必三_逻辑与思维_思维宝典_Claude上传底稿.docx`
  - Claude 抽取正文：`inputs/baodian_entries_from_claude.json`、`inputs/baodian_full_from_claude.txt`
  - 注：最初定位到的 2026-05-31 本地终极版只有 84 条；本审核表对象为 106 条，因此本 run 以 Claude 会话上传稿为直接修正对象。
- task:
  1. 读取审核表三张表：逐条核查表、覆盖遗漏表、汇总·方法·结论。
  2. 将审核意见拆成可执行处理账本：已修正、已满足、移出/改挂、需要原源进一步确认。
  3. 在不覆盖旧上传稿和旧终极版的前提下生成 Claude 审核修正版 Markdown/DOCX。
  4. 保持学生正文干净，不写入路径、OCR、审核状态、后台证据表述。
  5. 输出修正记录与 QA 报告，明确未能直接并入正文的原因。
- non-goal:
  - 不重做推理宝典。
  - 不把 Claude 审核表本身当成原试卷或原细则；涉及新增角度或争议归类时，正文只写能由既有锁源或当前材料支撑的表达。
  - 不覆盖 2026-05-31 旧交付文件。
