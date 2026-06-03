# GOVERNOR

## Active Verdict

verdict: `ACCEPT_LOCAL_STUDENT_LAYER_REBUILD_FOR_USER_REVIEW`

## Hard Vetoes

- 禁止把 V87 的 `83/83 PASS` 当成宝典验收。
- 禁止交付原题摘录包、答案表包、审计包形态的正文。
- 禁止学生版出现大量 `参考答案`、`题号 | 答案 |`、`评标`、`评分标准`、路径、OCR、debug。
- 禁止删除选择题的 `正确理由` 和 `诱人错项和错因`。
- 禁止未核对 V87 高风险答案源修正项就复制旧稿。

## Acceptance Needed

- V17 学生化主体通过文本门禁。
- V87 高风险修正项在新稿中逐项通过。
- 桌面 DOCX/MD 可打开且指向正确文件。
- 若 PDF 未重新生成，必须说明 PDF 状态，不得虚称完整视觉 QA。

## 2026-06-01T00:45:00+08:00 Governor Note

接受：

- 新交付以 V17 学生化正文为主体，已恢复选择题教学层：`答案选=36`，`错项分析=36`。
- V87 的回源表只作为答案源风险核对清单使用，没有把 V87 摘录包正文带入学生版。
- 学生版污染扫描通过：`参考答案`、`题号 |`、`评标`、`评分标准`、`/Users`、`OCR`、`source_extracted` 均为 `0`。
- V87 明确发现或提示过的高风险答案源点全部在新正文通过。
- 新 DOCX 无域、无外链：`fldChar=0`，`instrText=0`，`externalLink=0`。
- Word PDF 导出成功；PDF 文本层和抽样渲染通过。

限制：

- 本接受不是 GPT Pro / Claude 真实外审 PASS。
- 本接受只覆盖推理宝典本轮重做，不覆盖思维宝典。
- LibreOffice 渲染器不可用，未使用 `render_docx.py` 完成全页 DOCX PNG 渲染；本轮以 Word 导出 PDF + PDF 渲染抽样 + Quick Look 作为替代检查。
