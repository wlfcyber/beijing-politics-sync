# Task Plan

Goal: Run 选必一 当代国际政治与经济 through Codex + Claude Code evidence lanes into a final teaching document.

## Current Status

- status: in_progress
- current_phase: Phase 3 Dual production by suite/question

## Phases

- [x] Phase 0: Intake and user framework lock
- [x] Phase 1: Workspace, notebooks, and master requirements
- [x] Phase 2: Source inventory and evidence map
- [ ] Phase 3: Dual production by suite/question
- [ ] Phase 4: Advisor review and governor checks
- [ ] Phase 5: Fusion into student artifact
- [ ] Phase 6: Word/PDF production and visual QA
- [ ] Phase 7: Confucius artifact-only learning verification
- [ ] Phase 8: Final acceptance report

## Decisions Made

- 2026-05-02: Route selected as 飞哥政治庄园整本书总控 + 选必一《当代国际政治与经济》branch.
- 2026-05-02: Old 选必一 v12 artifacts are not final evidence; they may be read only for hard user corrections, known exclusions, and formatting lessons.
- 2026-05-02: Core output is 主观题细则术语学生版 unless user explicitly expands to choice questions.
- 2026-05-02: Source roots are `/Users/wanglifei/Desktop/2024模拟题`, `/Users/wanglifei/Desktop/2025模拟题`, `/Users/wanglifei/Desktop/2026模拟题`.
- 2026-05-02: Phase 3 started on high-priority rows; first drafted suites are `2026通州期末 Q20` and `2026朝阳期中 Q17`.
- 2026-05-02: User clarified Codex must also run production, not only supervise. Current entries already under `codex_lane/` count as Codex production and must continue that way.
- 2026-05-02: High-priority pinned rows now drafted through `2025海淀期末 Q22` and `2024东城一模 Q16/Q20`; next Phase 3 step is broader high-evidence suite expansion.
- 2026-05-02: Broader expansion started; drafted `2026东城期末 Q20`, `2026朝阳一模 Q20`, `2026顺义一模 Q20`, and `2025丰台期末 Q20`.
- 2026-05-02: Visual-render expansion added `2026丰台一模 Q19` and `2025海淀二模 Q21`; `2026西城期末 Q20` is blocked until a full paper prompt is found.
- 2026-05-02: Second 2026 expansion batch added `2026延庆一模 Q19(2)`, `2026石景山一模 Q20`, `2026西城一模 Q20(2)`, and `2026门头沟一模 Q20`.

## Errors Encountered

| Attempt | Error/Symptom | Different Next Step | Resolution |
|---|---|---|---|
| 1 | Claude Phase 2 command exited 0 with empty stdout/stderr and no report. Cause appears to be variadic CLI parsing: prompt was consumed by `--add-dir`. | Move prompt after a non-variadic option or feed prompt through stdin; avoid placing prompt immediately after `--add-dir` or `--tools`. | Retrying with corrected argument order. |
| 2 | ClaudeCode restart failed with `--output-format=stream-json requires --verbose`. | Patch launcher to add `--verbose`; preserve failed stderr as attempt1. | Relaunched through detached `screen` session. |
| 3 | Plain `nohup` detached process did not stay alive in this execution environment. | Use `/usr/bin/screen -dmS` with explicit logs and PID file. | `screen` launch confirmed with active Claude process and growing stream log. |

## Active Restart State

- Codex control: in progress.
- Codex production: 15 existing entry files / 89 entries are draft evidence, not final.
- ClaudeCode: `xuanbiyi_claudecode_2202`, PID recorded in `logs/claude_xuanbiyi_restart_2202.pid`, output isolated under `claudecode_lane/restart_2026-05-02_2202/`.
- Next Codex action: source-search `2026西城期末 Q20` full prompt and Governor review `2026朝阳期中 Q17` boundary terms.
