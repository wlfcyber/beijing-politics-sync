# DEVELOPMENT_PLAN

## Plan

1. 控制门禁：读取 master governor、worker orders、选必一 skill、hard-rule notebook 和本 run 控制文件。
2. 原文件锁定：记录桌面 Word 的路径、大小、mtime、sha256，不修改原文件。
3. Word 抽取：抽取正文、段落、表格、标题层级和可定位片段，建立条目候选清单。
4. 渲染核验：渲染 Word 为页面图像或 PDF，确认抽取文本与可见页面一致。
5. ClaudeCode 同步复核：准备独立任务包，真实启动/交付 ClaudeCode opus4.8max 复核，并保存运行痕迹和结论。
6. 逐题复核：按文档顺序逐条检查术语、完整设问、细则位置、来源、材料触发、答案句、合并逻辑、模块边界。
7. 差异合并：把 Codex 与 ClaudeCode 的发现合并为 `03_audit/QUESTION_AUDIT_LEDGER.csv` 和最终报告。
8. 控制闭环：更新 `PROGRESS.md`、governor、acceptance；未完成时只报告真实进度，不称完成。

## Minimal Step Rule

每次只推进一个最小完整步骤。真实产物先落盘，再更新 `PROGRESS.md` 和 governor。

## Current Minimal Step

Continue source-level review from doc_order 36 onward, with real ClaudeCode trace and Codex merge.
