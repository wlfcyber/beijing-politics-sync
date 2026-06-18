# CLAUDECODE_TASK_BRIEF

你是 ClaudeCode 复核线，模型要求：opus4.8max 或当前环境中可真实使用的最高 Opus 4.8 Max 等价档。

## 必须先读

1. `/Users/wanglifei/Desktop/北京高考政治/reports/master_governor/latest_master_governor_report.md`
2. `/Users/wanglifei/Desktop/北京高考政治/reports/master_governor/PROJECT_GOVERNOR_THREE_LAYER_SOP.md`
3. `/Users/wanglifei/Desktop/北京高考政治/reports/master_governor/worker_daily_orders.md`
4. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/SKILL.md`
5. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/current-user-requirements.md`
6. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/xuanbiyi-term-protocol.md`
7. 本 run 的 `TASK_BRIEF.md`、`DEVELOPMENT_PLAN.md`、`PROGRESS.md`、`00_control/SOURCE_LEDGER.csv`、`governor/GOVERNOR.md`、`acceptance/ACCEPTANCE_CRITERIA.md`

## 任务

回到桌面原文件 `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`，从头到尾按文档顺序逐题逐条复核。

每个条目检查：

- 术语是否来自评分细则/评标/阅卷细则/阅卷总结原词。
- 完整设问是否完整。
- 细则位置是否可回查，是否含套卷、题号、点位、分值或证据层级。
- 来源是否准确。
- 材料触发是否解释题目关系为什么触发该术语。
- 答案句是否可直接写在答题纸上，且包含术语、本题材料事实、因果/作用/结论。
- 同类项是否应合并，差异是否保留为表述积累。
- 是否有跨模块误入选必一主链。

## 输出

把结果写入本目录下的 `claudecode_findings.md`，格式：

```markdown
# ClaudeCode Findings

- model_used: <真实模型名>
- run_time: <开始和结束时间>
- source_docx_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e

## Findings

| doc_order | question_ref | term_or_heading | status | problem | evidence_pointer | suggested_fix |
|---|---|---|---|---|---|---|
```

不要把普通参考答案当评分细则。找不到证据就写 `BLOCKED`。
