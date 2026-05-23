# 选必一 2026二模工作流闭环复核

复核日期：2026-05-23

## 结论

本轮 2026 各区二模回填满足既定工作流的主体要求：源目录完整纳入清点，Codex 与 ClaudeCode 分别独立生成厚稿，GPT Pro 形成主融合稿，ClaudeCode/Claude Opus 4.7 对 GPT 融合稿作二次复核并给出 PASS，最终稿与证据包已同步到 GitHub。

需要保留的边界说明：本轮闭环对象是选必一主观题术语宝典的内容与证据链，不包括 Word 页面级视觉渲染闭环；当前环境缺少可用 LibreOffice 渲染链，只完成 DOCX 结构打开检查。

## 源范围复核

桌面源目录：`C:\Users\Administrator\Desktop\2026各区模拟题\2026各区二模`

源目录清点结果：

- 原始文件：22 个
- 区县文件夹：8 个
- 提取 manifest：22 行

ClaudeCode 独立运行日志确认其读取范围为 8 个区、22 个原始文件，并分别处理 docx、pptx、PDF、OCR 图像 PDF 和 legacy `.doc`。

## 入库与暂不入库

正式入库批次：`03_fusion/BATCH_014_FINAL_AFTER_GPT_AND_CLAUDE.md`

本轮正式入库 8 道题、34 条主链题例：

- 2026朝阳二模 Q20(1)：2 条
- 2026朝阳二模 Q20(2)：4 条
- 2026东城二模 Q20(3)：5 条
- 2026房山二模 Q20：6 条
- 2026海淀二模 Q20(2)：6 条
- 2026石景山二模 Q18：4 条
- 2026西城二模 Q19(1)：4 条
- 2026西城二模 Q19(2)：3 条

暂不入链 2 题：

- 2026丰台二模 Q20：PPT 阅卷细则未定位到该题对应评分块。
- 2026顺义二模 Q20：源目录仅有 PDF 试卷，无答案、评标、阅卷细则、讲评 PPT 或教师细则。

最终主表未出现丰台、顺义来源的 BATCH014 入链条目。

## 字段与分类复核

BATCH014 复核结果：

- 条目数：34
- 唯一术语：34
- 唯一来源题：8
- 必备字段缺失：0
- 非六桶桶位：0
- 答案句后台语言命中：0
- 暂不入链来源误入主表：0

六桶分布：

- 时代背景：3 条
- 理论：3 条
- 经济全球化：11 条
- 政治多极化：11 条
- 中国：5 条
- 联合国：1 条

重点错例钉死结果：

- `国际新秩序 / 新型国际关系` 位于政治多极化。
- `提供中国方案` 独立位于中国，不与新型国际关系混放。
- `正确的义利观 / 正确义利观` 本轮位于中国。
- 经济全球化保留 11 个细分节点，没有把不可替代表述粗暴合并。

## 模型与流程证据

工作流证据文件：

- 源包：`08_2026_second_mock_backfill/01_source_packet/CLAUDECODE_ORIGINALS_TASK.md`
- Codex 独立厚稿：`08_2026_second_mock_backfill/03_codex_independent/CODEX_INDEPENDENT_THICK_DRAFT.md`
- ClaudeCode 独立厚稿：`08_2026_second_mock_backfill/02_claudecode_independent/CLAUDECODE_ORIGINALS_THICK_DRAFT.md`
- 差异对照：`08_2026_second_mock_backfill/04_diff_and_fusion/CODEX_CLAUDECODE_DIFF.md`
- GPT Pro 审核提示：`08_2026_second_mock_backfill/05_gpt_pro_packet/GPT_PRO_REVIEW_PROMPT.md`
- GPT Pro 捕获输出：`08_2026_second_mock_backfill/05_gpt_pro_packet/GPT_PRO_OUTPUT_CAPTURE.md`
- GPT Pro 归一化稿：`08_2026_second_mock_backfill/05_gpt_pro_packet/GPT_PRO_OUTPUT_NORMALIZED_FOR_CLAUDE.md`
- ClaudeCode/Opus 复核任务：`08_2026_second_mock_backfill/06_claudecode_after_gpt_review/CLAUDECODE_GPT_REVIEW_TASK.md`
- ClaudeCode/Opus 复核输出：`08_2026_second_mock_backfill/06_claudecode_after_gpt_review/claudecode_gpt_review_stdout.txt`
- 最终入库批次：`03_fusion/BATCH_014_FINAL_AFTER_GPT_AND_CLAUDE.md`

模型锁证据：

- ClaudeCode 独立厚稿 debug 日志含 `model=claude-opus-4-7`。
- ClaudeCode/Opus 复核 debug 日志含 `model=claude-opus-4-7`。
- 复核输出明确给出 `PASS`。

GPT Pro 证据边界：

- 本地保留了 GPT Pro 审核提示、捕获输出、归一化稿和最终入库稿。
- `GPT_PRO_OUTPUT_NORMALIZED_FOR_CLAUDE.md` 与 `BATCH_014_FINAL_AFTER_GPT_AND_CLAUDE.md` 均含 34 个术语条目、34 个来源字段、36 个细则位置字段。
- 当前本地文件能证明 GPT Pro 输出被捕获并进入后续 Claude/Opus 复核链；模型档位依赖当时 ChatGPT Pro 页面操作记录，不像 ClaudeCode debug log 一样有 CLI 级模型字段。

## GitHub 同步

当前本地 HEAD 与远端 `origin/main` 一致：

`b19195ecaa6b221c33afed24591ad06888ae9ef8`

此前提交：`Add xuanbiyi 2026 second mock backfill`

