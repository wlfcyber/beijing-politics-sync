# Phase 02 Blockers

status: active

## Evidence Recheck Backlog

- `pending_content_recheck`: 94 source files.
- `P2_teaching_or_lecture_pending_role_check`: 7 source files.
- `unknown_needs_visual_check`: 9 source files.
- `unknown_needs_current_no_module_check`: 2 source files, both currently tied to 2026海淀期末.

## Known Suite-Level Blockers

| suite | blocker | current decision |
|---|---|---|
| 2026石景山期末 | User confirmed no usable scoring rules. | excluded unless user provides new scoring source. |
| 2026海淀期末 | User confirmed no 选必一; current-run file rows still need a no-module check record. | not in main table until checked. |
| 2026西城期末 Q20 | ClaudeCode draft says original paper/prompt not found and uses inferred wording. | cannot merge; must find original question or mark unresolved. |
| 2024东城一模 Q16/Q20 | Notebook says must include; current matrix still only candidate-level. | high-priority Phase 02 recheck. |

## Resolved During Phase 02

| suite | previous blocker | resolution |
|---|---|---|
| 2025海淀期中 Q16(2)/Q21(2) | Notebook said image/table scoring material exists; current matrix had not located it. | Resolved: `细则.docx` contains 8 embedded images and 7 tables. `image2.png` confirms Q16(2) trade-friction/global-governance scoring point; `image8.png` confirms Q21(2) “变/不变” scoring table. Added 6 Codex entries and marked source `SRC_cda046c2d36d` as `P0_verified_rubric`. |

## ClaudeCode Runtime Blocker

- Previous ClaudeCode run stopped with `413 Request too large (max 32MB)`, caused by a large PDF/image payload.
- Restarted with `CLAUDECODE_PHASE02_RESTART_PROMPT.md`, strict no-large-binary rule, and no budget cap.

## Not Blockers

- GPT-5.5 Pro Phase 01 advice is now saved and digested; GPT delay no longer blocks local Phase 02 evidence work.
- Final document generation is intentionally not started; it is blocked by Phase 02 evidence matrix completion, not by tooling failure.
