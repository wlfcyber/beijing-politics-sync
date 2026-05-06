你是 Claude Code，现在作为“飞哥政治庄园-选必一《当代国际政治与经济》”的独立复跑生产线运行。你不是 Codex 的替身，也不是只写建议；你要从本地源材料复核并产出可对照的证据线。

工作目录：

`/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_双线总控_2026-05-02`

本次写入隔离目录：

`/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_双线总控_2026-05-02/claudecode_lane/restart_2026-05-02_2202`

请先创建该目录下的 `entries/`、`suite_reports/`、`coverage/`、`blockers/`、`logs/`。不要覆盖 Codex 已有的 `codex_lane/entries/` 文件；根目录控制文件可读，必要状态写入你自己的隔离目录。

必须先读：

1. `MASTER_REQUIREMENTS.md`
2. `TASK_BRIEF.md`
3. `USER_FRAMEWORK.md`
4. `USER_QUESTIONS.md`
5. `SOURCE_LEDGER.csv`
6. `COVERAGE_MATRIX.csv`
7. `progress.md`
8. `findings.md`
9. `00_control/START_CARD.md`
10. `00_control/GOVERNOR_GATES.md`
11. `/Users/wanglifei/Desktop/北京高考政治/选必一复查_2026-04-29/选必一_交付要求记事本.md`
12. `/Users/wanglifei/.codex/skills/feige-politics-garden/SKILL.md`
13. `/Users/wanglifei/.codex/skills/feige-politics-garden-book-orchestrator/SKILL.md`
14. `/Users/wanglifei/.codex/skills/feige-politics-garden-book-orchestrator/references/whole-book-sop.md`
15. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/SKILL.md`
16. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/current-user-requirements.md`
17. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/xuanbiyi-term-protocol.md`

源目录：

- `/Users/wanglifei/Desktop/2024模拟题`
- `/Users/wanglifei/Desktop/2025模拟题`
- `/Users/wanglifei/Desktop/2026模拟题`

本次任务分三段推进，不要只停在计划：

## A. 独立复核 Codex 已有高价值条目

逐套复核以下文件对应的原题、细则和材料触发，不能只读 Codex 条目：

- `2026通州期末 Q20`
- `2026朝阳期中 Q17`
- `2025海淀期中 Q16(2) / Q21(2)`
- `2025海淀期末 Q22`
- `2024东城一模 Q16 / Q20`
- `2025海淀二模 Q21`
- `2026东城期末 Q20`
- `2026朝阳一模 Q20`
- `2026顺义一模 Q20`
- `2026丰台一模 Q19`
- `2026延庆一模 Q19(2)`
- `2026石景山一模 Q20`
- `2026西城一模 Q20(2)`
- `2026门头沟一模 Q20`

每套输出一个 `suite_reports/*.md`，每个可用术语输出 entry。entry 必须包含：

- `术语`
- `完整设问`
- `细则位置`
- `来源`
- `材料触发`
- `答案句`

## B. 专项追查 blocker 和边界冲突

1. `2026西城期末 Q20`：当前 Codex 发现有细则但缺完整题面。你必须从源目录和已提取文本中继续找完整题面；找不到就写 `blockers/2026西城期末_Q20_missing_full_prompt.md`，不得用细则或模型补题面。
2. `2026朝阳期中 Q17`：检查 `经济平稳可持续发展 / 高质量发展` 等术语是否属于选必一主链，还是应降级为必修二边界说明。
3. `2026石景山期末`：保持全模块排除，除非找到用户确认的新评分细则；普通参考答案不能推翻排除。

## C. 输出可融合结果

在隔离目录下生成：

- `entries/*.md`
- `suite_reports/*.md`
- `coverage/claudecode_coverage_matrix.csv`
- `blockers/*.md`
- `conflicts_for_codex.md`
- `phase_restart_summary.md`

`phase_restart_summary.md` 必须写清：

- 你复核了哪些源文件；
- 哪些条目确认可用；
- 哪些条目和 Codex 不一致；
- 哪些需要 Codex 回源裁决；
- 是否处理了 PDF、Word、PPT、图片、扫描、表格等非纯文本材料；
- 还缺什么。

硬规则：

- 从本地源证据决定事实，不从 Codex 草稿继承结论。
- 普通参考答案不能冒充评分细则。
- 外部模型建议不是证据。
- 学生字段不得出现路径、debug、OCR、复查、采分点、设问要求、细则要求、材料中等后台话术。
- 如果一个工具失败，换工具；至少尝试两种合理路径后才能标 blocker。
- 不要声明完成整本书终局；本次是独立复跑线重启与可融合成果生产，完成后等待 Codex Governor 融合。

现在开始。先建隔离目录，再读规则和源材料，持续推进到上述输出文件存在为止。
