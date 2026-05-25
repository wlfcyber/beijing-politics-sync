# SONNET_INVALIDATION_LEDGER

Status: `SONNET_EVIDENCE_INVALIDATED`

Timestamp: 2026-05-24 22:57 +08

## Invalidated Calls

| time +08 | source prompt | recorded command/model | invalidated output | disposition |
|---|---|---|---|---|
| 2026-05-24 22:01 | `03_claudecode_lane/PROMPT_VERIFY_GPTPRO_WEB_FIXES_20260524.md` | `claude.exe -p --model sonnet` | `03_claudecode_lane/claudecode_verify_gptpro_web_fixes_20260524.md` | invalid as qualified ClaudeCode evidence; may be used only as a non-authoritative reference pointer |
| 2026-05-24 22:09 | `03_claudecode_lane/PROMPT_VERIFY_BATCH03_CLEANUP_20260524.md` | `claude.exe -p --model sonnet` | `03_claudecode_lane/claudecode_verify_batch03_cleanup_20260524.md` | invalid as qualified ClaudeCode evidence; may be used only as a non-authoritative reference pointer |

## Rule Applied

- Sonnet, Haiku, and model-unknown outputs cannot satisfy the required ClaudeCode lane for this recovery.
- Any later file that cites the two invalidated outputs as `ClaudeCode PASS` must be downgraded or rechecked.
- Replacement evidence must prove Opus 4.7 max effort / adaptive thinking in `MODEL_EVIDENCE_LEDGER.md`.

## Immediate Impact

- The current acceptance status remains below strict final.
- The old latest ClaudeCode narrow recheck statements are not accepted as hard evidence until rerun under a confirmed Opus 4.7 max-effort/adaptive-thinking configuration.
- GPTPro web scoped fixes may remain locally applied, but their invalidated ClaudeCode verification is not a closing gate.

Decision: `fail`

The failed item is the model qualification of the two listed ClaudeCode calls, not necessarily the content of their findings. Content can be reconsidered only after source-backed Codex verification or a qualified Opus 4.7 rerun.
