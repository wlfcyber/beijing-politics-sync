# GPT-5.5 Pro 网页版/应用正式终审顺序 v10

请在 ChatGPT 网页版或 ChatGPT 应用中选择 GPT-5.5 Pro。本次终审不得使用 `pro-cli` 或任何 CLI 结果；附件中的 `INVALID_CLI_EXTERNAL_REVIEW_NOTE_20260605.md` 仅说明旧 CLI 记录作废。

## 先上传/参考的文件

- `outputs/选必二法律与生活_试题细则汇编_学生可发版_v10.docx`
- `outputs/选必二法律与生活_试题细则汇编_学生可发版_v10.md`
- `outputs/选必二法律与生活_AB双轴学生宝典_学生可发版_v10.docx`
- `outputs/选必二法律与生活_AB双轴学生宝典_学生可发版_v10.md`
- `qa/TWO_DOC_CLEAN_DRAFT_QA_v10_20260605.md`
- `qa/RENDER_QA_v10_20260605.md`
- `qa/INVALID_CLI_EXTERNAL_REVIEW_NOTE_20260605.md`

## 分块终审

为避免一次性上下文过大，请依次提交 `gpt55_chunks/` 下 6 个分块提示：

1. `GPT55_CHUNK_PROMPT_compilation_01_of_3_v10.md`
2. `GPT55_CHUNK_PROMPT_compilation_02_of_3_v10.md`
3. `GPT55_CHUNK_PROMPT_compilation_03_of_3_v10.md`
4. `GPT55_CHUNK_PROMPT_baodian_01_of_3_v10.md`
5. `GPT55_CHUNK_PROMPT_baodian_02_of_3_v10.md`
6. `GPT55_CHUNK_PROMPT_baodian_03_of_3_v10.md`

每块返回后，请保留原文结果。若任一块出现 `FAIL` 或 BLOCKING defects，停止终审并回到 Codex 修稿。

## 六块都无阻断后提交最终综合提示

把六块结果一并给 GPT-5.5 Pro，并要求输出：

1. final_verdict: PASS / CONDITIONAL_PASS / FAIL。
2. 是否可以作为学生可发版交付: YES / NO。
3. 是否仍有 BLOCKING 必改项。
4. 是否仍需本地补图或教师裁决。
5. 若 PASS，请明确写出“无阻断缺陷，可交付”。
