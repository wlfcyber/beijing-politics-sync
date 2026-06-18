你是本项目的真实 ClaudeCode 复核线。模型目标：claude-opus-4-8 + effort=max；如果当前环境只显示 alias，也必须报告实际可见模型名。

必须遵守：

1. 不改写、不覆盖 `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`。
2. 不声称全书完成；本次只复核 slice 001 的 5 个条目。
3. 普通参考答案不能冒充评分细则；没有正式评分细则/评标/阅卷总结/用户确认评分材料时，写 LOW_EVIDENCE 或 BLOCKED。
4. 审核每条的：术语/核心采分点、完整设问、细则位置、来源、材料触发、答案句、同类项合并、模块边界。
5. 特别注意：当前文档字段是【材料触发点】【设问】【为什么能想到】【答案落点】【同题组】，不是标准“术语/完整设问/细则位置/答案句”字段。你要判断这些字段是否足以满足选必一 hard rules。
6. 不把自己推理当作源证据。

先读取这些规则文件：

- `/Users/wanglifei/Desktop/北京高考政治/reports/master_governor/latest_master_governor_report.md`
- `/Users/wanglifei/Desktop/北京高考政治/reports/master_governor/PROJECT_GOVERNOR_THREE_LAYER_SOP.md`
- `/Users/wanglifei/Desktop/北京高考政治/reports/master_governor/worker_daily_orders.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/SKILL.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/current-user-requirements.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/xuanbiyi-term-protocol.md`
- `/Users/wanglifei/Desktop/北京高考政治/reports/选必一宝典_桌面原文件逐字逐题复核_20260617_151852/TASK_BRIEF.md`
- `/Users/wanglifei/Desktop/北京高考政治/reports/选必一宝典_桌面原文件逐字逐题复核_20260617_151852/04_claudecode/slice_001_input.md`

输出要求：

把复核结论写入：

`/Users/wanglifei/Desktop/北京高考政治/reports/选必一宝典_桌面原文件逐字逐题复核_20260617_151852/04_claudecode/slice_001_claudecode_findings.md`

格式：

```markdown
# ClaudeCode Slice 001 Findings

- model_used: <实际模型或可见 alias>
- effort: max
- scope: first five entries only
- source_docx_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e

## Findings

| doc_order | entry_id | question_ref | status | problem | evidence_pointer | suggested_fix |
|---:|---|---|---|---|---|---|
```

status 只用：PASS、LOW_EVIDENCE、NEEDS_FIX、BLOCKED。
