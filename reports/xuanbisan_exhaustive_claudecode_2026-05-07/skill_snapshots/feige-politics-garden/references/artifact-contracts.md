# Artifact Contracts

Use these contracts for any new book/module workflow.

## Run Directory

Recommended location:

`<project-root>/reports/<book-slug>_<YYYY-MM-DD_HHmm>/`

Default project root:

`~/Desktop/飞哥的政治庄园/`

The run directory is disposable but must contain enough state to resume after context compression.

## Project Folder

The project folder carries visible role work across threads.

Required top-level files/folders:

- `PROJECT_MANIFEST.md`
- `reports/`
- `threads/`
- `artifacts/`
- `sources/`

## Thread Registry

Every run must include `THREAD_REGISTRY.md`.

Columns:

```csv
Role,Agent/Thread ID,Assignment,Write scope,Status,Last report
```

When real subagents are spawned, record their IDs immediately. When the app UI is used to open separate visible threads manually, paste or link those thread IDs/labels. If thread creation fails or capacity is exhausted, record `not spawned: <reason>` rather than pretending the role exists.

## Required Status Values

Use only these values in `SOURCE_LEDGER.csv` and `COVERAGE_MATRIX.csv` unless the user defines a project-specific extension:

- `unseen`
- `inventory-only`
- `included`
- `objective-key-only`
- `module-boundary-excluded`
- `reference-only`
- `source-missing`
- `ocr-needed`
- `duplicate-or-drift`
- `blocked`
- `superseded`

## SOURCE_LEDGER.csv Columns

```csv
suite_id,year,district,stage,file_path,file_type,source_type,question_range,status,notes
```

`source_type` examples:

- `paper`
- `objective-answer-key`
- `rubric`
- `marking-report`
- `lecture-scoring`
- `reference-answer`
- `archive-copy`
- `web-source`

## COVERAGE_MATRIX.csv Columns

```csv
suite_id,question,book_module,question_type,evidence_source,status,artifact_location,decision_reason,next_action
```

Every relevant question must receive one row. If the question belongs to a different book/module, use `module-boundary-excluded`.

## Role Report Schema

Each role report should contain:

- `Scope read`
- `Files inspected`
- `Findings`
- `Merge candidates`
- `Blockers`
- `Decision: pass/fail/blocked/needs-merge`

Worker merge candidates must contain:

- source suite and question number,
- source type and evidence strength,
- material information,
- rubric/scoring point or wrong-option statement,
- logic chain,
- proposed artifact location.

## Plan/Progress Contract

`DEVELOPMENT_PLAN.md` and `PROGRESS.md` must share the same step IDs.

Rules:

- A step can be checked only after a real file read, source classification, merge, render, or validation has happened.
- Do not mark all steps complete at the end without incremental evidence.
- If a step is skipped, record why in `DECISION_LOG.md`.

## Governor Checklist

The governor must reject completion if any of these are true:

- a relevant suite/question is unclassified,
- a main-question entry lacks a scoring source,
- a choice-question entry lacks a reliable answer key,
- a material-to-knowledge chain lacks source suite or question number,
- a source was excluded without a reason,
- a role blocker was not escalated once,
- the user framework was overwritten or ignored,
- Word deliverables were not rendered when requested,
- final counts conflict without explanation.

## Final Acceptance Report

Required sections:

- Deliverables
- Scope and source roots
- Coverage summary by status
- Role findings disposition
- Merged additions
- Checked exclusions
- Remaining blockers or evidence boundaries
- Render/validation results

The final line must be exactly:

```text
TASK_COMPLETE
```

Use that line only when the workflow is objectively closed under the declared scope and statuses.
