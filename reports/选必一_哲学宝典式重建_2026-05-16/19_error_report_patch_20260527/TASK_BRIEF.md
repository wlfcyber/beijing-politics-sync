# TASK_BRIEF

- run_id: 19_error_report_patch_20260527
- scope: Patch the 18_layout_score_layers_20260526 student handbook against the user's error report, including OCR verification for F-class items.
- source_base: ../18_layout_score_layers_20260526
- output_policy: Create a new version only; do not overwrite 18.

## User Corrections To Apply

- A-D classes from the user's error report: title/name fixes, prompt restoration, fabricated material removal, scoring-layer/score corrections.
- F class: perform OCR/source verification before deciding whether each item can be corrected, excluded, or recorded as still blocked.

## Boundaries

- Keep student-facing output clean: no backend paths, model names, audit/debug terms, or unverified source claims in the main document.
- Preserve the six-bucket structure unless a verified module-boundary issue requires exclusion from the student main body.
- Do not promote OCR guesses into facts without supporting source text or rendered-page evidence.
