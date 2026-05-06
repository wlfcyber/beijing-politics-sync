# ClaudeCode Production Lane B Continuation Prompt - Batch04K 2026房山一模

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

Process Batch04K:

- `2026房山一模 Q19`
- Scoring source: `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026房山一模/细则/细则.docx`
- Paper source: `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026房山一模/试卷/试卷.pdf`

Codex A visual check confirms the full prompt:

`结合材料，运用《当代国际政治与经济》知识，分析海南自贸港封关是如何助力国际循环的。（8分）`

Known scoring structure to verify from the DOCX:

- Consumption/market side, 2 points: `发挥超大规模市场优势` -> `降低成本提高效率`; `货物、服务贸易升级` / `要素自由流动` / `优化资源配置` / `贸易投资自由化便利化`.
- Production side, 2 points: `技术研发` -> `提升企业竞争力` -> `产业升级` / `优化产业结构` -> `融入全球产业分工和合作`.
- Investment side, 2 points: `优化营商环境` -> `吸引外商投资` / `引进来`.
- China-solution side, 2 points: `制度型开放` (1 point) -> `提供助力国际循环中国方案` / `以国内大循环吸引全球资源要素` / `增强国内国际两个市场两种资源联动效应` (1 point).

Important ambiguity to resolve:

- Codex A saw a note like `表示1-5，每个2分，总分不超过6分` near the mechanism items. Recheck whether this cap applies only to the first three mechanism groups and whether the `制度型开放 + 中国方案/双循环/两市场两资源` group supplies the remaining 2 points. Do not silently flatten the scoring structure.

Boundary checks:

- `Q16(1)` contains opening/globalization expressions but is an `经济与社会` location-development question. Boundary only unless you find explicit 当代国际政治与经济 scoring.
- `Q20` is a broad integrated level-scored question; examples may mention `中国智慧、中国方案`, but do not promote it into a point-by-point Xuanbiyi scoring slot unless the source has a scoring position.

## Write Scope

Write only under:

- `claudecode_lane/`
- `04_suite_reports/claudecode_suite_reports/`
- `06_conflicts/`

Do not edit Codex A files, fusion, student docs, delivery, or global control ledgers.

## Expected Output Files

- `claudecode_lane/progress_batch04K.md`
- `claudecode_lane/batch04K_fangshan2026_matrix.csv`
- `claudecode_lane/batch04K_fangshan2026_entries.md`
- `claudecode_lane/batch04K_missing_blockers.md`
- `claudecode_lane/batch04K_conflicts_for_codex.md`
- `04_suite_reports/claudecode_suite_reports/batch04K_fangshan2026_suite_report.md`

Final response must list changed files, promoted candidates, boundary-only questions, exclusions, source-grade cautions, and blockers.
