# ClaudeCode Production Lane B Continuation Prompt - Batch04J 2026延庆一模

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

Process Batch04J:

- `2026延庆一模 Q19(2)`
- Scoring source: `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026延庆一模/细则/细则.docx`
- Paper source: `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026延庆一模/试卷/试卷.pdf`

Codex A visual check confirms the full prompt:

`结合材料二，运用《当代国际政治与经济》知识，说明中国“推动重塑全球能源治理格局”的理论逻辑和价值意蕴。（8分）`

Known scoring structure to verify from the DOCX:

- Theory logic: `1+1 x 2` = 4 points.
  - State-interest angle: `共同利益是国家间合作的基础` / `维护国家利益是主权国家对外活动的出发点` / `正确的义利观`.
  - Historical-tide angle: `时代主题` / `经济全球化趋势`.
- Value implication: one point 2 points, two points 4 points.
  - `人类命运共同体`
  - `共商共建共享的全球治理观`
  - `相互尊重、公平正义、合作共赢的新型国际关系`

Important source boundary:

- The answer paragraph also says `具有公共产品属性的中国方案`, but the scoring bullet does not list it as a separate formal slot. Treat it as expression accumulation or answer-sentence support unless you find an explicit scoring line.
- `一带一路`, `绿色基建`, `能源转型`, and `绿色发展指数` are material triggers/platforms, not standalone scoring terms unless the scoring source says so.

## Write Scope

Write only under:

- `claudecode_lane/`
- `04_suite_reports/claudecode_suite_reports/`
- `06_conflicts/`

Do not edit Codex A files, fusion, student docs, delivery, or global control ledgers.

## Expected Output Files

- `claudecode_lane/progress_batch04J.md`
- `claudecode_lane/batch04J_yanqing2026_matrix.csv`
- `claudecode_lane/batch04J_yanqing2026_entries.md`
- `claudecode_lane/batch04J_missing_blockers.md`
- `claudecode_lane/batch04J_conflicts_for_codex.md`
- `04_suite_reports/claudecode_suite_reports/batch04J_yanqing2026_suite_report.md`

Final response must list changed files, promoted candidates, boundary-only questions, exclusions, source-grade cautions, and blockers.
