# Advisor Boundaries

Use this reference before sending sensitive, source-heavy, or Beijing Gaokao politics material to GPT Pro, ChatGPT Pro, Claude, Deep Research, or another external advisor.

## Evidence Priority

Use this priority model when external advice intersects with source-based work:

- `P0`: Formal scoring rubrics, marking rules, marking reports, or explicit marking-standard lecture/report fragments.
- `P1`: Official, district, or school reference answers and answer/scoring references. Do not call P1 a formal rubric unless the user confirms.
- `P2`: Lecture slides, teacher explanations, test analysis, and teaching materials.
- `P3`: Paper text, question materials, options, charts, cartoons, and tables.
- `P4`: AI summaries, GPT Pro advice, Deep Research output, advisor suggestions, and working drafts.

P4 never proves facts. It can only suggest what Codex should check locally.

## Allowed In Advisor Packs

Allowed:

- Goal, scope, mode, and final artifact target.
- User framework and hard rules.
- Source and coverage statistics.
- Short sanitized examples.
- Student draft excerpts.
- Explicit review questions.
- Known blockers and uncertainty.

## Forbidden In Advisor Packs

Forbidden:

- Accounts, secrets, environment variables, cookies, tokens, private keys, or raw auth material.
- Unnecessary local absolute paths.
- Raw browser profile data.
- Large raw exam passages.
- Large raw scoring-rule passages.
- Unverified conclusions presented as settled fact.
- Backend logs that reveal private file organization unless the user explicitly wants that shared.

## Decision Log Format

For each external suggestion, record:

```markdown
| Source | Suggestion | Decision | Local verification needed | Verification result | Enters final artifact |
|---|---|---|---|---|---|
| GPT Pro / Deep Research | ... | accept/reject/defer | ... | pass/fail/pending | yes/no |
```

## Beijing Politics Rules

For Beijing Gaokao politics work:

- Route by the named book or module first.
- Reopen local source chains when the user says the result is wrong, incomplete, or unsatisfactory.
- Do not let GPT Pro, Deep Research, or Claude decide rubric facts, source wording, module boundaries, or scoring levels.
- Use external advisors to find likely gaps, weak explanations, missing transfer steps, wrong-option traps, and possible student confusion.
- Convert every adopted advisor suggestion into a local source-check task.
- Keep backend verification material separate from student-facing handbooks unless the user asks to include it.
- Avoid inflated "final" claims until source lock, local verification, and user acceptance are actually achieved.

## Failure Handling

If the external lane stalls, closes, returns empty output, hits quota, loses auth, or becomes unavailable:

1. Save the symptom and timestamp.
2. Mark the lane `blocked_advisor` or `real_call_pending`.
3. Continue safe local evidence work only.
4. Retry the external lane later if the phase requires it.
5. Do not claim the phase passed because Codex simulated the missing external call.
