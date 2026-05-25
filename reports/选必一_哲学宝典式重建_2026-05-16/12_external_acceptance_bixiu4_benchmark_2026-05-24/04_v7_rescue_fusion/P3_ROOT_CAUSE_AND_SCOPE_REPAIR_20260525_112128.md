# P3 root cause and scope repair

## Why it looked broken after being usable earlier

Two independent blockers overlapped.

1. External gate blocker: Chrome extension can list tabs, but ChatGPT page claim/read timed out and reset the browser-control kernel. Claude auth is at a Google account chooser, so Codex did not select credentials. Therefore current SHA has not yet received a true GPT Pro / Claude App final review.
2. Local evidence-join blocker: the P2 heading evidence index matched only the current strict P0 row pattern. Older batch-ledger rows and rendered-image sources were not joined back, so some real source-locked headings appeared unmatched.

## False entry found and repaired

Problem heading in final student Markdown:

- `2026顺义一模Q19(3)` under `核心答题点：人才是综合国力竞争和自主创新的关键资源`

Root cause:

- The phrase `人才是第一资源；综合国力竞争说到底是人才竞争；人才是衡量一个国家综合国力的重要指标；人才是自主创新的关键` exists in `2026顺义一模细则`.
- But it belongs to 顺义 Q19(3) `经济与社会` future-industry recommendation/reasoning task, not to a subjective question asking `运用《当代国际政治与经济》知识，从国家利益角度说明我国为什么把人才工作摆在重要位置`.
- The student entry therefore mixed a real rubric fragment with a wrong/non-source prompt and should not remain in the 选必一 main chain.

Repair applied:

- Removed the `2026顺义一模Q19(3)` student example from the final Markdown.
- Changed the core heading frequency from `出现2次` to `出现1次`.
- Renumbered the remaining `2025东城一模Q21` example to `### 1`.

Post-repair quick checks:

- `2026顺义一模Q19(3)` in final Markdown: `0`
- `2026石景山期末` in final Markdown: `0`
- `TODO/FIXME/待补/待核` in final Markdown: `0`
- core heading count remains `136`
- all H3 examples now `372`

Status:

- This repair removes one false positive from the student body. It does not close the real GPT Pro / Claude App final gate.
