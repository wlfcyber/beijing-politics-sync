# Project Governor Three-Layer SOP

This is the mandatory project-wide control mechanism for `/Users/wanglifei/Desktop/北京高考政治` and the synced repo `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync`.

## Purpose

Prevent false closure, source-boundary drift, stale context reuse, and over-1M context failures by forcing every AI lane through the same three gates before touching project files.

## Report Inbox

Primary report location on this Mac:

- `/Users/wanglifei/Desktop/北京高考政治/reports/master_governor/`

Git-sync mirror:

- `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/master_governor/`

Every worker must read these files first when they exist:

- `latest_master_governor_report.md`
- `worker_daily_orders.md`
- `context_compression_manifest.csv`
- `adaptive_rules_ledger.md`
- `self_learning_register.csv`

## Layer 1: Project Master Governor

The master governor is the project-wide supervisor. It does not replace book/module skills or evidence review. It only decides whether a lane is safe to continue and what the next control action is.

Before any project task, check:

- latest master report exists and is not stale;
- the target lane appears in the report or has a newly created run folder;
- source ledger, progress, coverage, governor, and acceptance files are named;
- over-size files have context capsules when they exceed the threshold;
- unresolved `blocked_advisor`, `real_call_pending`, missing rubric, OCR, traceability, or false-closure flags are visible.

If the latest report is missing or stale, run:

```bash
python3 /Users/wanglifei/GaokaoPolitics/beijing-politics-sync/scripts/master_governor.py report \
  --workspace "/Users/wanglifei/Desktop/北京高考政治" \
  --sync-root "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync"
```

Do not treat this script as content evidence. It is a supervisor index and compression generator only.

## Layer 2: Skill And Notebook Gate

After Layer 1, load the relevant project skill:

- router / mixed-book / long run: `feige-politics-garden`
- whole-book four-lane run: `feige-politics-garden-book-orchestrator`
- 必修四: `feige-politics-garden-bixiu4`
- 选必一: `feige-politics-garden-xuanbiyi`
- 选必二: `feige-politics-garden-xuanbier`
- 选必三: `feige-politics-garden-xuanbisan`
- legacy/sync compatibility: `beijing-gaokao-politics-rubric`

Then read the current lane notebook or hard-rule file before source work. The notebook is the task-local rule source. If the user corrects a missed rule, write it into the notebook or current run control files before continuing.

Layer 2 must reject:

- using ordinary reference answers as rubrics without user confirmation;
- inheriting old conclusions after `从0`, `全部作废`, or `不继承旧结论`;
- mixing books/modules outside the user scope;
- counting GPT/Claude roleplay as real GPT-5.5 Pro or Claude Opus lanes;
- final student artifacts with audit/debug/source-path language.

## Layer 3: Run Execution Gate

Only after Layer 1 and Layer 2 can a worker touch the run's real files.

Required read set for any substantial lane:

- `TASK_BRIEF.md`
- `DEVELOPMENT_PLAN.md`
- `PROGRESS.md`
- `SOURCE_LEDGER.csv` or equivalent
- `COVERAGE_MATRIX.csv` / `QUESTION_COVERAGE_MATRIX.csv` or equivalent
- `DECISION_LOG.md`
- governor files
- final acceptance files, if present

Execution rule:

- advance one minimal complete step;
- write the real artifact first;
- then update progress/control files using stable step IDs;
- update governor notes before claiming completion;
- if the step needs missing source/rubric/user boundary, write `BLOCKED` with exact file/question reason.

## Daily Worker Protocol

Each subproject AI should start the day by reading:

1. `reports/master_governor/latest_master_governor_report.md`
2. `reports/master_governor/worker_daily_orders.md`
3. its own row/path in the report
4. its branch skill and notebook
5. its run control files

The worker may execute only the next action assigned to its lane or a narrower safe control-file repair. If its lane is missing from the report, it must write a registration note under its run directory and ask the master governor to refresh.

## Self-Learning And Adaptation

Self-learning means durable rule capture, not autonomous source invention.

Allowed adaptations:

- add a user correction as a hard rule;
- add a recurring failure pattern to `adaptive_rules_ledger.md`;
- create a new validation check for stale progress, false closure, missing traceability, oversized context, or forbidden evidence promotion;
- improve worker prompts or control-file templates after a recorded failure.

Forbidden adaptations:

- changing evidence hierarchy;
- promoting a reference answer into a rubric;
- deleting old blockers by summary;
- silently rewriting the user's framework;
- treating model advice as source evidence.

Every accepted adaptation must include:

- date;
- triggering failure or user correction;
- new rule;
- validation check;
- affected skill/run files.

## Context Compression

Files over the configured threshold, default 1 MB, must not be pasted whole into AI context. Use the master governor script to generate deterministic capsules:

- file metadata and hash;
- first and last lines;
- matched control/evidence/blocker lines;
- omitted-size notice.

The original file remains the evidence source. A capsule is an index for context transfer, not a substitute for source evidence when exact lines matter.

## Stop Rules

Stop and write `BLOCKED` instead of executing when:

- Layer 1 report is missing/stale and cannot be regenerated;
- the target lane has no control files and the task is substantial;
- source boundary is unclear and a wrong choice would contaminate the project;
- the user explicitly forbids a root or old artifact and the current process needs it;
- a final report claims closure while required governor/traceability/coverage/advisor files remain missing.
