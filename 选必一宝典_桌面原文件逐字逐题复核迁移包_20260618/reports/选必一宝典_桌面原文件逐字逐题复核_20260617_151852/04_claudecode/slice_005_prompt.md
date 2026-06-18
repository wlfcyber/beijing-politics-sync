你是本项目的真实 ClaudeCode 复核线。模型目标：claude-opus-4-8 + effort=max；如当前环境只显示 alias，也必须报告实际可见模型名。

必须遵守：

1. 不改写、不覆盖 `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`。
2. 不声称全书完成；本次只复核 slice 005 的 5 个条目（doc_order 21-25）。
3. 普通参考答案不能冒充评分细则；没有正式评分细则/评标/阅卷总结/用户确认评分材料时，写 LOW_EVIDENCE 或 BLOCKED。
4. 审核每条的：术语/核心采分点、完整设问、细则位置、来源、材料触发、答案句、同类项合并、模块边界。
5. 特别注意：当前文档字段是【材料触发点】【设问】【为什么能想到】【答案落点】【同题组】，不是标准“术语/完整设问/细则位置/答案句”字段。判断这些字段是否足以满足选必一 hard rules。
6. 不把自己推理当作源证据。
7. 延续 slice 001-004 的已确认问题：缺独立【术语】和【细则位置】属于结构性风险，但仍需逐条判断是否还有内容级问题、证据层级问题、模块边界问题、同题组问题、内部计分问题或跨桶重复问题。
8. ClaudeCode 原始判断可以被 Codex 用正式源证据校正；如发现教材/细则冲突，必须先回查可见正式源或明确写成“待回源核对”，不要把自身推理当成定论。
9. 对 doc_order 21-25 特别关注：Q0021 是否只是“可采知识”并列清单；Q0022 是否混入必修二/生态文明/新发展理念；Q0023 等级题是否只有可用角度而非固定采分点；Q0024 背景层是否只是小论文第一层；Q0025 是否为综合经济形势题，选必一术语和必修二/经济学术语边界是否清楚。

先读取这些规则文件：

- `/Users/wanglifei/Desktop/北京高考政治/reports/master_governor/latest_master_governor_report.md`
- `/Users/wanglifei/Desktop/北京高考政治/reports/master_governor/PROJECT_GOVERNOR_THREE_LAYER_SOP.md`
- `/Users/wanglifei/Desktop/北京高考政治/reports/master_governor/worker_daily_orders.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/SKILL.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/current-user-requirements.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/xuanbiyi-term-protocol.md`
- `/Users/wanglifei/Desktop/北京高考政治/reports/选必一宝典_桌面原文件逐字逐题复核_20260617_151852/TASK_BRIEF.md`
- `/Users/wanglifei/Desktop/北京高考政治/reports/选必一宝典_桌面原文件逐字逐题复核_20260617_151852/03_audit/slice_004_codex_claudecode_merge.md`
- `/Users/wanglifei/Desktop/北京高考政治/reports/选必一宝典_桌面原文件逐字逐题复核_20260617_151852/04_claudecode/slice_005_input.md`

输出要求：

把复核结论写入：

`/Users/wanglifei/Desktop/北京高考政治/reports/选必一宝典_桌面原文件逐字逐题复核_20260617_151852/04_claudecode/slice_005_claudecode_findings.md`

格式：

```markdown
# ClaudeCode Slice 005 Findings

- model_used: <实际模型或可见 alias>
- effort: max
- scope: doc_order 21-25 only
- source_docx_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e

## Findings

| doc_order | entry_id | question_ref | status | problem | evidence_pointer | suggested_fix |
|---:|---|---|---|---|---|---|
```

status 只用：PASS、LOW_EVIDENCE、NEEDS_FIX、BLOCKED。结论后请追加一段“源证据边界”，说明哪些判断是从 slice 输入文本直接可见，哪些仍需 Codex 回原卷/细则确认。
