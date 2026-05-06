# 选必二 ClaudeCode 独立生产线 B 进度

> 单调递增；只追加，不覆盖。

## 2026-05-04 启动

- [x] 读完 `00_飞哥选必二法律与生活要求小本本.md`、`feige-politics-garden/SKILL.md`、`feige-politics-garden-xuanbier/SKILL.md`、`feige-politics-garden-book-orchestrator/SKILL.md`、本地 `TASK_BRIEF.md`。
- [x] 勘察三年源目录、`extracted_text/` 池、现有 Codex 产物存在性（仅做存在性确认，不读结论）。
- [x] 建立独立目录骨架与 `MASTER_REQUIREMENTS.md`。
- [ ] 独立 Source Ledger（基于真实源目录树 + extracted_text 文本读取）。
- [ ] 独立题包：主观题 + 选择题。
- [ ] 框架归位矩阵 + 缺口清单 + 命题路径反推。
- [ ] 真实模型审稿 prompt 包（real_call_pending）。
- [ ] 双 Word 交付（框架版 + 情境版）。
- [ ] Governor / Confucius / 洁净扫描 / FINAL_ACCEPTANCE。

## 已知硬性约束

- GPT-5.5 Pro / Claude Opus 4.7 Adaptive 真实外部调用：本会话不能完成 → 全部 gate 标 `real_call_pending`，由用户人工驱动。
- bash sandbox 不挂用户磁盘路径；本生产线全部用 Read/Write/Edit 直读直写。
- `2026石景山期末` 排除。
- 期中卷无选必二的标 `no_xuanbier`，不强收。

## 工作策略说明

- 本线证据来源以原始源目录文件名为准；文本读取通道使用 `选必二重做_2026-04-30/extracted_text/` 池（等同于我自跑 pdftotext / docx2txt 抽取的输出）。
- 每个 ledger 行必须能反查回原始源文件路径（`source_path` 字段）。
- 任何"参考答案"型证据全部标 `reference_answer`，不得推动主观题踩分句。
- 任何"评标 / 阅卷总结 / 讲评 / 分题细则"型证据标为 `marking_record` 或 `formal_rubric`（视具体内容定级）。
