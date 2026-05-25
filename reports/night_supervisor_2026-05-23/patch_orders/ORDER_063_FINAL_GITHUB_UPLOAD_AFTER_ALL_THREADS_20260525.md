# ORDER_063_FINAL_GITHUB_UPLOAD_AFTER_ALL_THREADS_20260525

Issued: 2026-05-25 13:11 +08

Status: `ACTIVE_FINAL_UPLOAD_ORDER`

## User Instruction

The user is leaving. Continue supervising all active Beijing politics threads. After all thread tasks have ended, upload both final deliverables and process logs to GitHub.

## Do Not Upload Yet

Do not push now while any line is still `RUNNING`, `CANDIDATE_DELIVERY_NEEDS_AUDIT`, `BLOCKED_ADVISOR`, `BLOCKED_SOURCE_BOUNDARY`, or `DELIVERED_WITH_GOVERNANCE_GAPS`.

Upload is allowed only after each active line has a clear terminal state:

- preferred terminal state: `STRICT_FINAL_ACCEPTED` with evidence;
- or explicit user-approved terminal/blocker state recorded in the final supervisor snapshot.

## Required Upload Scope

For each completed line, include:

- final student deliverables: Markdown, DOCX, PDF, rendered QA summaries, and final acceptance reports;
- process logs: coverage matrices, source/evidence ledgers, model-call records, GPT/Claude raw captures or pending/blocker logs, Governor/Confucius reports, Word/PDF QA, patch orders, heartbeat snapshots, and migration/recovery handoff files;
- supervisor metadata: latest `MASTER_REQUIREMENTS.md`, `THREAD_REGISTRY.md`, `HEARTBEAT_PROTOCOL.md`, all `ORDER_06x*` patch orders, and final `heartbeat_*` snapshots;
- upload report: a new `reports/night_supervisor_2026-05-23/github_upload_YYYYMMDD_HHMM.md` listing exact files included, excluded, commit hash, remote branch, and secret-scan result.

## Pre-Push Safety Gate

Before `git add`:

1. Generate an upload scope list.
2. Exclude local credentials, cookies, browser profile state, raw account data, private tokens, `.env`, app config backups, and unrelated Desktop files.
3. Run a text scan over the upload scope for at least:
   - `sk-`
   - `ghp_`
   - `github_pat_`
   - `ANTHROPIC_API_KEY`
   - `OPENAI_API_KEY`
   - `cookie`
   - `password`
   - `Authorization:`
4. The upload report must say either `NO_SECRET_PATTERN_MATCHES` or list the blocked files and stop.

## Git Procedure

Use the visible sync repo:

`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible`

Remote:

`origin https://github.com/wlfcyber/beijing-politics-sync.git`

Procedure:

1. `git status --short`
2. select only the required result/log files;
3. use `git add` and, where the repo intentionally ignores deliverables such as Word/PDF/zip, use `git add -f` only for selected final deliverables;
4. `git diff --cached --name-only` and write it into the upload report;
5. commit with a clear message such as `Upload completed Beijing politics handbook runs`;
6. push to the current branch's `origin`;
7. write the commit hash and remote branch into the final heartbeat snapshot.

## Final Report To User

After push, report:

- which lines ended and with what status;
- where the final deliverables are;
- GitHub remote/branch/commit;
- any files intentionally not uploaded and why;
- whether the secret scan passed.
