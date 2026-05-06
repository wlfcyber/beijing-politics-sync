# ClaudeCode Production Lane B Continuation Prompt — Batch04H 2026门头沟一模

Run identity:
/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03

You are ClaudeCode production lane B for this exact run. Another thread may also be using GPT, Claude, or ClaudeCode. Do not mix outputs, logs, browser context, or prior-thread conclusions across threads. Use only this run directory and write only in this run directory.

Workspace root:
/Users/wanglifei/Desktop/北京高考政治

## Read First

- `00_control/CROSS_THREAD_TOOL_GUARD.md`
- `MASTER_REQUIREMENTS.md`
- `task_plan.md`
- `progress.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden/SKILL.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-book-orchestrator/SKILL.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/SKILL.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/current-user-requirements.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/xuanbiyi-term-protocol.md`

## Mission

Process Batch04H:

- `2026门头沟一模 Q20`
- Secondary boundary check: `2026门头沟一模 Q21` only for whether the 当代国际政治与经济 4-point chunk should be boundary-only or candidate.
- P0 scoring source: `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026门头沟一模/细则/细则.docx`
- P3 paper source: `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026门头沟一模/试卷/试卷.pdf`

Q20 full prompt:

`结合材料，运用《当代国际政治与经济》知识，分析海南自贸港全岛封关为何能为中国经济发展注入新动能、为世界经济开放发展注入新活力。`

Known P0 structure to preserve and verify from the scoring source:

- `为什么 = 原因 + 意义`
- Cause/theory 2 points: use subject terms such as `对外开放基本国策`, `互利共赢战略`, `经济全球化`, `高水平对外开放`.
- China-side significance 2 points: from the Hainan closure materials, e.g. zero-tariff scope/cost reduction/trade facilitation, processing value-added and industrial-chain upgrading/new productive forces, port management/customs-time/business environment, domestic-international circulation/two markets and two resources/open economy advantage.
- World-side significance 2 points: market access/world market space, institutional opening and high-level opening example, global industrial-chain/supply-chain stability, international division of labor/cooperation, open world economy.
- Logic 1 point.

Important scoring guards:

- If only China-side or only world-side significance is answered, score cap is 4.
- If the answer only recites textbook theory and does not connect to Hainan Free Trade Port closure, score cap is 5.
- Do not collapse high-information phrases into vague labels. Keep complete expressions such as `贸易自由化便利化`, `制度型开放`, `开放型世界经济`, `国内国际双循环`, `国内国际两种市场两种资源联动`, and `高水平对外开放`.

## Write Scope

Write only under:

- `claudecode_lane/`
- `04_suite_reports/claudecode_suite_reports/`
- `06_conflicts/`

Do not edit Codex A files, fusion, student docs, delivery, or global control ledgers.

## Expected Output Files

- `claudecode_lane/progress_batch04H.md`
- `claudecode_lane/batch04H_mengtougou2026_matrix.csv`
- `claudecode_lane/batch04H_mengtougou2026_entries.md`
- `claudecode_lane/batch04H_missing_blockers.md`
- `claudecode_lane/batch04H_conflicts_for_codex.md`
- `04_suite_reports/claudecode_suite_reports/batch04H_mengtougou2026_suite_report.md`

Final response must list changed files, promoted candidates, boundary-only questions, exclusions, and blockers.
