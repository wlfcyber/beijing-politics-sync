# ClaudeCode Production Lane B Prompt

You are ClaudeCode production lane B for the Feige Politics Garden run:

Run directory:
/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03

Workspace root:
/Users/wanglifei/Desktop/北京高考政治

## Highest Priority Files

Read these first:

1. `/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03/MASTER_REQUIREMENTS.md`
2. `/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03/task_plan.md`
3. `/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03/progress.md`
4. `/Users/wanglifei/Desktop/北京高考政治/选必一复查_2026-04-29/选必一_交付要求记事本.md`
5. `/Users/wanglifei/.codex/skills/feige-politics-garden/SKILL.md`
6. `/Users/wanglifei/.codex/skills/feige-politics-garden-book-orchestrator/SKILL.md`
7. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/SKILL.md`
8. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/current-user-requirements.md`
9. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/xuanbiyi-term-protocol.md`

## Your Role

You are not a reviewer and not a replacement for Codex. You are the independent workhorse production lane B.

Start from local sources and cache. Old artifacts may be used only to locate sources and compare omissions. Do not inherit old conclusions as evidence.

## Required Work

1. Build your own source inventory for 2024-2026 Beijing papers/scoring files relevant to 选必一 subjective questions.
2. Prioritize high-weight and hard samples:
   - 2026通州期末 Q20
   - 2026朝阳期中 Q17
   - 2025海淀期中 Q16(2)
   - 2025海淀期中 Q21(2)
   - 2025海淀期末 Q22
   - 2024东城一模 Q16
   - 2024东城一模 Q20
   - 2026朝阳一模 Q20
   - 2026顺义一模 Q20
   - 2025海淀二模 Q21
3. For every candidate question, classify as `in_scope`, `excluded`, `no_xuanbiyi`, `missing_scoring_source`, or `needs_codex_ruling`.
4. Produce entries only when scoring source position is auditable.
5. Preserve full required fields: 术语, 完整设问, 细则位置, 来源, 材料触发, 答案句.
6. Merge same-core terms before expression accumulation. Do not collapse high-information terms into vague labels.
7. Exclude 2026石景山期末 all modules unless a new usable scoring source is explicitly supplied by the user.

## Write Scope

Write only under:

- `/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03/claudecode_lane/`
- `/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03/04_suite_reports/claudecode_suite_reports/`
- `/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03/06_conflicts/`

Do not edit Codex A agent files, fusion, delivery, or MASTER_REQUIREMENTS.

## Expected Output Files

Create or update:

- `claudecode_lane/progress.md`
- `claudecode_lane/source_inventory.csv`
- `claudecode_lane/subjective_question_matrix.csv`
- `claudecode_lane/claudecode_entries.md`
- `claudecode_lane/missing_blockers.md`
- `claudecode_lane/conflicts_for_codex.md`
- `04_suite_reports/claudecode_suite_reports/suite_report_index.md`

Keep running until at least the priority hard samples have source status and first-pass entries/blockers.

Final message must list changed files and open blockers.
