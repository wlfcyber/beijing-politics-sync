# Cross-Thread Tool Guard

time: 2026-05-03 22:36 CST

## Rule

Another thread may also be using GPT, Claude, and ClaudeCode. This run must stay isolated.

## Current Run Identity

- run directory: `/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03`
- ClaudeCode screen prefix: `xuanbiyi_claudecode_batch`
- ClaudeCode log prefix: `claudecode_batch`
- module: 选必一《当代国际政治与经济》

## Guardrails

- Do not use any GPT or Claude webpage response unless it was submitted from this thread with this run identity in the prompt header.
- Do not treat another thread's browser reply as evidence, review, or approval.
- Do not attach another thread's ClaudeCode screen/log/output to this run.
- All ClaudeCode B work must write only under this run's `claudecode_lane/`, `04_suite_reports/claudecode_suite_reports/`, or `06_conflicts/`.
- External GPT/Claude lanes remain advisory only. Codex A local evidence and Governor decide source facts, rubric status, and release gates.
- Before final student delivery, confirm external-review files, screen/log names, and control ledgers all point to this run directory.

## 2026-05-04 External Browser Coordination Addendum

- User confirmed another Codex thread is also actively using Safari/ChatGPT.
- This run must not touch Safari while the other thread is typing, switching conversations, uploading files, or recovering from wrong-thread drift.
- This run may only use Safari during an explicit stable window: the other thread is waiting for GPT to think, or the user confirms the browser is free.
- If Safari shows any conversation other than `Opus4.6 vs 4.7` at `https://chatgpt.com/c/69f7099a-36e0-839a-b579-db4d592f1848`, stop immediately and do not submit.
- The marker for this run's supplemental GPT request is `XBY1-GPT-DEEP-FINAL-20260504-1118`; only a response containing or clearly following that marker can count for this run.
- The 2026-05-04 11:18 attempt was submitted to the correct thread, but response capture was interrupted by cross-thread Safari conflict; it is not a PASS until the response is captured and locally adjudicated.
