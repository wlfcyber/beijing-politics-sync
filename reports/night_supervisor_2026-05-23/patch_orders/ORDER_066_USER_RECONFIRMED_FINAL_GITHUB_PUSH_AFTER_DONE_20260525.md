# ORDER_066_USER_RECONFIRMED_FINAL_GITHUB_PUSH_AFTER_DONE_20260525

Issued: 2026-05-25 19:53 +08

User instruction: `做完后推到github上`

Status: `FINAL_GITHUB_PUSH_RECONFIRMED_BUT_DEFERRED`

## Binding Rule

After all active Beijing politics lines are actually done, push the final results and process logs to:

- `origin`: `https://github.com/wlfcyber/beijing-politics-sync.git`

This order does not authorize an early push. It reinforces `ORDER_063_FINAL_GITHUB_UPLOAD_AFTER_ALL_THREADS_20260525.md`.

## Before Push

The final upload worker must:

1. Confirm all active lines have reached strict terminal or user-approved terminal/blocker state.
2. Generate an exact selective upload scope covering final deliverables, coverage matrices, model-review records, Governor/Confucius reports, Word/PDF QA, patch orders, snapshots, and process logs.
3. Exclude browser profiles, cookies, local session files, credentials, tokens, `.env`, app config backups, and unrelated Desktop files.
4. Run the required sensitive-pattern scan over the exact upload scope.
5. Proceed only after writing `NO_SECRET_PATTERN_MATCHES`.
6. Commit and push, then write `github_upload_YYYYMMDD_HHMM.md` with branch, commit hash, pushed scope, and scan result.

## Current State At Issuance

- Bixiu4 migrated recovery thread is still active and not strict-final.
- Latest observed Bixiu4 status: local matrix/body risks are being reduced, but GPTPro web review, Claude Opus 4.7 web/app full artifact review, ClaudeCode model confirmation, and final manual typography gate remain open.
- Xuanbiyi and Xuanbier still retain external/governance delivery gaps from the supervisor baseline unless later snapshots prove otherwise.

## Prohibited

- Do not write `STRICT_FINAL_ACCEPTED` while any hard gate remains open.
- Do not push to GitHub while any active line is still running or in fake-closure/candidate-only state.
- Do not include credentials, browser/session state, or unrelated local files in the upload scope.
