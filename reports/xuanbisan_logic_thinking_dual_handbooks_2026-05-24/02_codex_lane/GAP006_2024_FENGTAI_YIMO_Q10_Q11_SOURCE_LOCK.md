# GAP006 Source Lock: 2024丰台一模 Q10-Q11

Status: `source_locked_pending_external_review`

This file advances GAP006 at the local source-evidence level only. It does not close the 2024 backlog, GPT Pro, Claude, Governor, Confucius, or final delivery gates.

## Source

- paper-with-answer cache: `gpt_sources/5f5486bfc3baab2b_2024北京丰台高三一模政治试题及答案.md`
- prompt lines:
  - Q10: `5f5486bfc3baab2b_2024北京丰台高三一模政治试题及答案.md:106-112`
  - Q11: `5f5486bfc3baab2b_2024北京丰台高三一模政治试题及答案.md:113-120`
- answer-key lines: `5f5486bfc3baab2b_2024北京丰台高三一模政治试题及答案.md:287-292`
- source type: paper-with-answer PDF extraction

## Q0090 2024丰台一模 Q10

Evidence level: `A-support`

Prompt evidence:

- Q10 lists scientists drawing inspiration from music theory and musical structures: Lagrange, Heisenberg, and Newlands.
- option A says抽象思维与形象思维有互补性.
- answer key locks Q10 = A.

Local decision:

- Promote as Q0090, a thinking choice row.
- It can train the positive signal: when scientific discovery is inspired by artistic image/material, do not split abstract thinking and image thinking into two isolated worlds; they can complement each other.
- Because no independent objective-question rubric explanation was recovered, keep it as `A-support`.

## Q0091 2024丰台一模 Q11

Evidence level: `A-support`

Prompt evidence:

- Q11 describes rivers as a necessary condition for life habitability on Earth, then asks what the Mars-river research shows.
- option D says rivers are a necessary condition for life habitability on Earth; without rivers, life would not arise.
- answer key locks Q11 = D.

Local decision:

- Promote as Q0091, a reasoning choice row on necessary-condition judgment.
- It belongs in the reasoning handbook.
- Because no independent objective-question rubric explanation was recovered, keep it as `A-support`.

## Gate Decision

Add Q0090-Q0091 to the coverage matrix and source-packet queue.

Add Q0090 to `MAIN_THINKING_LEDGER.csv` and `CHOICE_TRAP_LEDGER.csv`.

Add Q0091 to `REASONING_FORM_LEDGER.csv`, `CHOICE_TRAP_LEDGER.csv`, and the reasoning body draft.

Keep both rows `source_locked_pending_external_review` until real GPT Pro and Claude review are captured.
