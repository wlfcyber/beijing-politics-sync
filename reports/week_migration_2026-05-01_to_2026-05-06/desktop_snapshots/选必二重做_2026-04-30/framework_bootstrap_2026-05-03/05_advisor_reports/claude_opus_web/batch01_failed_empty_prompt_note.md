# Excluded Failed Claude Attempt

- timestamp_context: 2026-05-03 Batch01 web/app run
- model_ui: Claude Opus 4.7 Adaptive
- status: excluded
- issue: The first Claude attempt produced an empty-prompt style reply because the long prompt was present as a pasted-text card but the submitted message did not direct Claude to use it clearly enough.
- correction: A second message explicitly instructed Claude to follow the complete pasted text, and Claude then produced the independent framework council report.
- evidence_policy: The failed empty-prompt attempt is not model advice, not framework evidence, and not counted in the workflow gate.
