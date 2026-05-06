# External Skill Absorption Report

Date: 2026-05-02

Downloaded for audit/reference:

- `external-skills/planning-with-files` from `https://github.com/OthmanAdi/planning-with-files.git`, commit `a3e52a1`
- `external-skills/superpowers` from `https://github.com/obra/superpowers.git`, commit `e7a2d16`

Absorbed into:

- `skills/feige-politics-garden-book-orchestrator/SKILL.md`
- `skills/feige-politics-garden-book-orchestrator/references/run-protocol.md`
- `skills/feige-politics-garden-book-orchestrator/references/control-files.md`
- `skills/feige-politics-garden-book-orchestrator/references/role-prompt-templates.md`
- `skills/feige-politics-garden-book-orchestrator/references/external-workflow-patterns.md`
- `skills/feige-politics-garden-book-orchestrator/scripts/init_book_run.py`

## What Was Adopted

- File-backed planning: `task_plan.md`, `findings.md`, `progress.md`.
- Save findings after source/visual reads.
- Re-read plan/findings before major decisions.
- Log every error and avoid repeating the same failed action.
- 3-strike error rule.
- Ask clarifying questions one at a time before whole-book runs.
- Propose 2-3 approaches when strategy is ambiguous.
- Dispatch agents only for independent domains with separated write scopes.
- Evidence-before-completion: no final claim without fresh validation.

## What Was Not Adopted

- Automatic hooks that inject local planning files into model context.
- Mandatory TDD.
- Mandatory git worktrees, commits, PRs, or branch finishing.
- Generic software-development ceremony that does not serve Beijing politics教研.
- Any external rule that overrides user instructions, lane notebooks, or 飞哥政治庄园 branch skills.

## Why This Helps 北京高考政治教研

- Long book runs survive context loss and overnight supervision.
- PDF/image/Word/OCR findings are preserved as text immediately.
- Claude Code and Codex can coordinate without trusting each other's summaries.
- Final document acceptance stays evidence-based and artifact-only.
