# GitHub 同步交接：选必二法律与生活 v35 双文档

同步时间：2026-06-05 晚

## 本次同步目标

把 2026-06-04 至 2026-06-05 的选必二《法律与生活》双文档清理成果上传到 GitHub，保证另一台机器可拉取继续工作。

## 已纳入同步的核心内容

- run 控制文件：`TASK_BRIEF.md`、`DEVELOPMENT_PLAN.md`、`PROGRESS.md`、`GOVERNOR_STATUS.md`、`COVERAGE_STATUS.md`、`DECISION_LOG.md`、`EXTERNAL_REVIEW_LEDGER.md`。
- 当前学生可发候选 Word 本体：
  - `outputs/选必二法律与生活_试题细则汇编_学生可发版_v35.docx`
  - `outputs/选必二法律与生活_AB双轴学生宝典_学生可发版_v35.docx`
- v35 及历史迭代的 Markdown 正文稿，便于跨设备比对和继续修订。
- v35 PDF 校样：
  - `qa/rendered_compilation_v35/选必二法律与生活_试题细则汇编_学生可发版_v35.pdf`
  - `qa/rendered_baodian_v35/选必二法律与生活_AB双轴学生宝典_学生可发版_v35.pdf`
- QA、复核、裁决记录：v33/v34/v35 抽取表、复核表、QA 报告和渲染 QA 摘要。
- 当前构建/抽取工具脚本：`tools/*.py`、`tools/*.js`。
- Claude/web 外审用的文本包和提示词记录；其中 CLI 外审记录仅作为历史错误记录，不作为有效外审结论。

## 明确未纳入同步的内容

- 约 5.7G 的历史渲染缓存、逐页 PNG、旧版 PDF 全量堆积。
- 旧版 v1-v34 的 Word/PDF 大文件本体；这些版本只保留 Markdown、QA 和必要记录。
- 本机临时缓存、`.codex` 会话状态、`__pycache__` 等运行残留。

这些排除项不影响回家继续工作；当前可编辑交付件以 v35 两份 Word 和对应 Markdown 为准。

## 当前质量边界

v35 是“当前候选版”，不是最终锁定版。仍需继续处理或外部复核的点：

- E009 / E043 / E051 的正式细则分值分布仍有待最终确认。
- 2026 顺义一模 18 题的分值拆分仍需确认。
- E057 是否跨模块吸收仍需最终决策。
- GPT-5.5 Pro 与 Claude Opus 4.8 Max 的最终外审必须使用网页版或应用；CLI 结果不得算数。

## 回家后建议入口

先打开本目录下：

1. `PROGRESS.md`
2. `GITHUB_SYNC_HANDOFF_20260605.md`
3. `outputs/选必二法律与生活_试题细则汇编_学生可发版_v35.docx`
4. `outputs/选必二法律与生活_AB双轴学生宝典_学生可发版_v35.docx`

然后按 `EXTERNAL_REVIEW_LEDGER.md` 继续网页版/应用外审。
