# Upload Scope 2026-05-25 Xuanbisan V98

Status: `SANITIZED_PROJECT_MIRROR`

This upload mirrors the portable project output for the 2026-05-24 选必三《逻辑与思维》双宝典 run.

## Included

- `reports/xuanbisan_logic_thinking_dual_handbooks_2026-05-24/`
- Final student Markdown, DOCX, and PDF artifacts under `08_delivery/final_v97/`.
- Source inventory, Codex lane ledgers, ClaudeCode production outputs, fusion audits, GPT Pro review records, Claude review records, Governor/Confucius checks, delivery status, logs needed for project reproducibility, and render QA evidence.

## Excluded

- `03_claudecode_lane/logs/claudecode_debug*.log`

Reason: one ClaudeCode debug log contained a real `Authorization: Bearer ...` token. The debug logs are local diagnostic process state and are not required for the portable teaching deliverable or governance chain.

## Boundary

This is a project-output mirror, not a full-machine backup. It excludes user profiles, browser profiles, `.codex`, `.claude`, caches, credentials, and system/session state.

## Verification

- Copied source tree with `claudecode_debug*.log` excluded.
- Will stage only this upload scope note and `reports/xuanbisan_logic_thinking_dual_handbooks_2026-05-24/`.
- Word outputs are intentionally included; use forced git add if ignored by repository policy.
