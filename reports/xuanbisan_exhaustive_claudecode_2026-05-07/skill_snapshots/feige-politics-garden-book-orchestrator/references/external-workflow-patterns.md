# External Workflow Patterns Absorbed

This reference records the useful parts absorbed from two external skill families and how they should be adapted for Beijing Gaokao politics教研. Do not load or run the external skills automatically; use this as the local, safer interpretation.

Downloaded reference copies:

- `external-skills/planning-with-files` at commit `a3e52a1`
- `external-skills/superpowers` at commit `e7a2d16`

## From planning-with-files

Adopt:

- Use the filesystem as working memory for long tasks.
- Create `task_plan.md`, `findings.md`, and `progress.md` in the run folder.
- Re-read the plan before major decisions.
- After every two source-reading actions, persist findings to disk.
- Log all errors and avoid repeating the same failed action.
- Use a 3-strike rule: diagnose/fix, try a different method, rethink/escalate.

Adaptation:

- `task_plan.md` is a working-memory plan, not the final authority. `MASTER_REQUIREMENTS.md` remains the highest run-specific rule.
- `findings.md` stores source discoveries and visual/OCR notes; final student content still comes from audited entries and fusion outputs.
- `progress.md` is a session log; `PROGRESS.md` remains the formal status board.
- Do not enable automatic hooks that inject local file contents into context. Read planning files deliberately.

## From Superpowers brainstorming

Adopt:

- Before a whole-book run, ask clarifying questions one at a time until scope, framework, evidence boundary, and output contract are clear.
- For ambiguous strategy, propose 2-3 approaches with tradeoffs and a recommendation.
- Record the accepted design in `USER_FRAMEWORK.md`, `MASTER_REQUIREMENTS.md`, and `DECISION_LOG.md`.

Adaptation:

- Do not require formal user approval for every tiny design section once the user has authorized overnight execution.
- For Beijing politics, the design gate is about book/module boundary, evidence boundary, framework shape, source roots, and final document contract, not software architecture.

## From Superpowers dispatching-parallel-agents

Adopt:

- Dispatch one worker per independent domain.
- Give each worker a narrow scope, complete local context, write boundaries, and expected output.
- Review and integrate worker results instead of trusting worker success summaries.

Adaptation:

- Good parallel domains: separate suites, source recovery vs Word rendering, independent advisor review, Confucius artifact-only reading.
- Bad parallel domains: two workers editing the same final Word, two workers making competing framework decisions without a governor, or workers sharing incomplete source assumptions.

## From Superpowers verification-before-completion

Adopt:

- Evidence before claims.
- Before saying complete, identify what proves completion, run/read the check, and cite the result.
- Agent success reports are not enough; verify artifacts and control files directly.

Adaptation:

- Verification commands may be document/render checks rather than unit tests.
- Final completion requires artifact-only teaching verification, not just script exit codes.

## From Superpowers writing/executing plans

Adopt:

- Plans should contain concrete phases, exact files, expected outputs, and verification steps.
- Execution should follow the written plan and update checkboxes/status.
- Stop and ask only when the plan has a real blocker or source-boundary uncertainty.

Adaptation:

- Do not import TDD, commit frequency, PR workflow, or git-worktree requirements into teaching runs unless the task is actually software development.
- For教研, each task should produce audited source outputs, suite reports, coverage rows, student-facing entries, or validation artifacts.

## Explicitly Not Adopted

- Mandatory TDD for all work.
- Mandatory git worktrees, commits, PR review, or branch finishing.
- Automatic hooks that read local planning files on every tool call.
- Any rule that overrides user instructions or 飞哥政治庄园 branch skills.
- Generic software-development labels in final student documents.
