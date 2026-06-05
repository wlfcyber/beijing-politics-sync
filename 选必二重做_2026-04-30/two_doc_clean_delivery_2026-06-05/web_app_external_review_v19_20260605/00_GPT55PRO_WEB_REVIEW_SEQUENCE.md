# GPT-5.5 Pro 网页版/应用正式终审顺序 v19

请在 ChatGPT 网页版或 ChatGPT 应用中选择 GPT-5.5 Pro。本次终审不得使用 `pro-cli` 或任何 CLI 结果；附件中的 `INVALID_CLI_EXTERNAL_REVIEW_NOTE_20260605.md` 仅说明旧 CLI 记录作废。

## 先上传/参考的文件

- `outputs/选必二法律与生活_试题细则汇编_学生可发版_v19.docx`
- `outputs/选必二法律与生活_试题细则汇编_学生可发版_v19.md`
- `outputs/选必二法律与生活_AB双轴学生宝典_学生可发版_v19.docx`
- `outputs/选必二法律与生活_AB双轴学生宝典_学生可发版_v19.md`
- `qa/TWO_DOC_CLEAN_DRAFT_QA_v19_20260605.md`
- `qa/RENDER_QA_v19_20260605.md`
- `qa/INVALID_CLI_EXTERNAL_REVIEW_NOTE_20260605.md`

## 分块终审

为避免一次性上下文过大，请依次提交 `gpt55_chunks/` 下 24 个分块提示：

1. `GPT55_CHUNK_PROMPT_compilation_01_of_12_v19.md`
2. `GPT55_CHUNK_PROMPT_compilation_02_of_12_v19.md`
3. `GPT55_CHUNK_PROMPT_compilation_03_of_12_v19.md`
4. `GPT55_CHUNK_PROMPT_compilation_04_of_12_v19.md`
5. `GPT55_CHUNK_PROMPT_compilation_05_of_12_v19.md`
6. `GPT55_CHUNK_PROMPT_compilation_06_of_12_v19.md`
7. `GPT55_CHUNK_PROMPT_compilation_07_of_12_v19.md`
8. `GPT55_CHUNK_PROMPT_compilation_08_of_12_v19.md`
9. `GPT55_CHUNK_PROMPT_compilation_09_of_12_v19.md`
10. `GPT55_CHUNK_PROMPT_compilation_10_of_12_v19.md`
11. `GPT55_CHUNK_PROMPT_compilation_11_of_12_v19.md`
12. `GPT55_CHUNK_PROMPT_compilation_12_of_12_v19.md`
13. `GPT55_CHUNK_PROMPT_baodian_01_of_12_v19.md`
14. `GPT55_CHUNK_PROMPT_baodian_02_of_12_v19.md`
15. `GPT55_CHUNK_PROMPT_baodian_03_of_12_v19.md`
16. `GPT55_CHUNK_PROMPT_baodian_04_of_12_v19.md`
17. `GPT55_CHUNK_PROMPT_baodian_05_of_12_v19.md`
18. `GPT55_CHUNK_PROMPT_baodian_06_of_12_v19.md`
19. `GPT55_CHUNK_PROMPT_baodian_07_of_12_v19.md`
20. `GPT55_CHUNK_PROMPT_baodian_08_of_12_v19.md`
21. `GPT55_CHUNK_PROMPT_baodian_09_of_12_v19.md`
22. `GPT55_CHUNK_PROMPT_baodian_10_of_12_v19.md`
23. `GPT55_CHUNK_PROMPT_baodian_11_of_12_v19.md`
24. `GPT55_CHUNK_PROMPT_baodian_12_of_12_v19.md`

每块返回后，请保留原文结果。若任一块出现 `FAIL` 或 BLOCKING defects，停止终审并回到 Codex 修稿。

## 所有分块都无阻断后提交最终综合提示

把所有分块结果一并给 GPT-5.5 Pro，并要求输出：

1. final_verdict: PASS / CONDITIONAL_PASS / FAIL。
2. 是否可以作为学生可发版交付: YES / NO。
3. 是否仍有 BLOCKING 必改项。
4. 是否仍需本地补图或教师裁决。
5. 若 PASS，请明确写出“无阻断缺陷，可交付”。
