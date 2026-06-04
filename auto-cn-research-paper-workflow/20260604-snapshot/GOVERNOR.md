# GOVERNOR

- lane: `auto-cn-research-paper-workflow/20260604-snapshot`
- status: in_progress
- current_allowed_step: Complete post-redownload verification, sync generated artifacts, and prepare final review packets only.
- content_boundary: No Beijing politics source, rubric, teaching-document, or student-facing content edits.
- completion_rule: This lane is not complete unless tests are freshly checked and `workflow_gate_matrix.py` reports `final_user_goal_ready=yes`.

## Active Watchpoints

- Do not promote copied Windows paths into current Mac evidence.
- Do not count title/abstract-only sources as formal full text.
- Do not count CLI/API advisor calls as final GPT/Claude web/App approvals.
- Do not use material-count success as a substitute for topic, citation, source-provenance, and external-review gates.
- Current matrix state: `topic_selection_ready=yes`, `paper_material_ready=yes`, `final_user_goal_ready=no`.
- Current hard blockers: citation-level final page anchors and visible GPT/Claude pass reviews.
