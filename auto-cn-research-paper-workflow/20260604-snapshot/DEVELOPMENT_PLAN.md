# DEVELOPMENT_PLAN

## Plan

1. Browser readiness: run the Chrome CDP probe against the current Mac browser session and record the result in the active trial run.
2. Control files: add minimal task-control files for this non-politics workflow snapshot so repository execution remains inside the master-governor boundary.
3. Skill sync: copy only the changed `auto-cn-research-paper` skill files from the installed skill into the repository snapshot and the local paper-workspace snapshot.
4. Verification: run all skill tests in the installed, repository, and workspace copies.
5. Gate matrix: run `workflow_gate_matrix.py` on the active trial run with the Mac material search root.
6. Report: summarize current pass/fail status, including material availability, citation anchors, topic gate, source provenance, and visible GPT/Claude review gates.

## Non-Goals

- No Beijing politics source/rubric/content edits.
- No Git commit or push unless the user explicitly asks.
- No final paper completion claim unless `final_user_goal_ready=yes` is freshly produced.
