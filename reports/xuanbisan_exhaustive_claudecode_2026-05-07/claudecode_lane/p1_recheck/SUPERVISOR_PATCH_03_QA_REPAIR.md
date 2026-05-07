# Supervisor Patch 03: P1 QA repair

Time: 2026-05-07 16:30 +08:00

ClaudeCode P1 relative relaunch produced the four required files, but Codex QA
found three repairable issues:

1. One Shunyi Q17(1) framework path omitted the `假言判断` level:
   `推理边界>判断>必要条件假言判断`.
2. The same wrong key appeared in the JSONL patches, evidence, and acceptance.
3. Acceptance/progress text mentioned banned boundary words while describing
   checks, which makes automated QA fail even though the student content itself
   does not use them.

Supervisor action:

- Normalize the Shunyi node to
  `推理边界>判断>假言判断>必要条件假言判断`.
- Remove the banned literal wording from progress/acceptance text.
- Preserve ClaudeCode's evidence and decisions wherever they already pass.
- Rerun Codex P1 QA before fusion.
