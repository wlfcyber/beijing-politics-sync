# Thread Defect Patches

Use this reference when a task is long-running, delegated, resumed, or overnight.

## 1. Context Compression Loss

Failure mode: after hours of work or a sleep period, the conversation may compact. Subtle state such as why a source was excluded, which role had vetoed completion, or which files were rendered can disappear.

Patch:

- Treat on-disk control files as the source of truth, not chat memory.
- Before any long phase, write `TASK_BRIEF.md`, `DEVELOPMENT_PLAN.md`, `PROGRESS.md`, and `HANDOFF_QUEUE.md`.
- After every meaningful phase, update `PROGRESS.md` and `HANDOFF_QUEUE.md`.
- After a resume or compaction, read `TASK_BRIEF.md`, `PROGRESS.md`, `HANDOFF_QUEUE.md`, and the newest user message before doing more work.
- Final answer must be based on `FINAL_ACCEPTANCE_REPORT.md`, not memory.

## 2. Roles Becoming Decorative

Failure mode: roles produce reports, but their findings do not constrain the final merge. A governor says “not pass yet,” but the main thread still finishes.

Patch:

- Every role report must end with `pass`, `fail`, `blocked`, or `needs-merge`.
- The main thread must create a merge matrix listing every role finding and its disposition: merged, rejected with reason, blocked, or superseded by better evidence.
- Patcher runs after merge, not only before merge.
- Governor runs after patcher and has veto. Completion is impossible while any governor veto remains unresolved.

## 3. Worker Blockers Accepted Too Early

Failure mode: a worker checks local folders, cannot find a source, and marks a blocker. Later the main thread may find it online or in a zip/archive, meaning the original blocker was premature.

Patch:

- Use a blocker-escalation pass before final acceptance:
  - local canonical folder,
  - duplicate folders,
  - zip archives,
  - rendered pages for scan-only PDFs,
  - OCR/text extraction,
  - approved web or public source search when allowed.
- Record the searches in `DECISION_LOG.md` or a dedicated source-closure report.
- If only a reference answer is found, close only the objective-answer or existence gap; do not close the rubric gap.

## 4. “Exhaustion” Ambiguity

Failure mode: “都穷尽了吗” is treated as “all available rows were processed,” while the user means every suite/question was accounted for.

Patch:

- Define exhaustion as classification coverage.
- `COVERAGE_MATRIX.csv` must classify every suite/question as `included`, `module-boundary-excluded`, `objective-key-only`, `reference-only`, `source-missing`, `ocr-needed`, `duplicate-or-drift`, or `blocked`.
- Final answer must separate “included in framework” from “checked and excluded.”

## 5. Reference Answer vs Rubric Confusion

Failure mode: answer PDFs are tempting to use as scoring rubrics, especially when no rubric is present.

Patch:

- Source type is mandatory in `SOURCE_LEDGER.csv`.
- `reference-only` material can support existence, objective answer keys, or teacher comparison, but cannot create main-question scoring points.
- If a reference answer is used at all, write the boundary next to the artifact entry.

## 6. Ledger/Artifact Count Drift

Failure mode: a ledger says 1445 rows but the actual artifact contains 1429. The final document may repeat one number and hide the mismatch.

Patch:

- Programmatically count artifact rows before final.
- Record both ledger and artifact counts if they differ.
- Use the artifact body as the final count unless a repair pass reconciles the ledger.
- Do not claim row-level exhaustion when historical count drift remains unreconciled.

## 7. Wide Table Rendering Failure

Failure mode: DOCX tables render as a one-character-wide vertical strip in artifact-tool or Word layout.

Patch:

- For dense Chinese study notes, default to paragraph blocks with bold labels instead of wide tables.
- If tables are used, render immediately; if narrow/vertical text appears, convert to block layout.
- Final DOCX acceptance requires rendered PNG inspection plus a simple blank-page/tiny-file check.

## 8. Subagent Limits And Write Conflicts

Failure mode: a requested automation role cannot spawn because the thread limit is reached; multiple workers may also edit the same artifact.

Patch:

- Prefer independent visible role threads when the user requests them, and register them in `THREAD_REGISTRY.md`.
- Main thread owns automation if subagent capacity is limited.
- Assign workers read-only findings by default.
- Only the main thread merges into cumulative artifacts unless a worker is explicitly given a disjoint write set.
- Close role agents after their findings are integrated.

Visibility rule:

- If real independent threads are available, use them for 决策者、资料组织者、劳动者、补丁者、监管者.
- If not available, create files under `threads/` with the same role names and record the downgrade reason.

## 9. User Framework Drift

Failure mode: Codex quietly uses a generic textbook outline and loses the user's custom framework.

Patch:

- `USER_FRAMEWORK.md` is created before analysis.
- Every merge must point to a user-framework location or explicitly state “no fitting location yet.”
- Unknown parts of the user's system are placeholders, not invented categories.

## 10. Final Answer Overclaiming

Failure mode: final response says “完成/穷尽” while residual blockers remain.

Patch:

- Final response must use three buckets:
  - completed and merged,
  - checked and excluded with reason,
  - blocked or evidence-insufficient.
- `TASK_COMPLETE` is permitted only when all rows are classified and final deliverables pass validation. It does not mean blocked rows disappeared; it means they are explicitly classified.
