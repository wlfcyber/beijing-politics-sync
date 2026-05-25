# ClaudeCode B-line supplement: correct body-file paths for Shunyi 2026 ERMO

You already ran a focused B-line audit for Q0136-Q0140, but the prompt used obsolete body filenames.

Correct body files:
- `04_fusion/THINKING_BAODIAN_V2_BODY_DRAFT.md`
- `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md`

Scope:
- Only re-check Q0136-Q0140 against these two body draft files and the prior Shunyi B-line stdout log.
- Do not write or modify files.
- Output Markdown to stdout only.
- Do not claim final, pass, complete, publishable, Word, or PDF readiness.

Read:
- `03_claudecode_lane/logs/claudecode_2026_ermo_shunyi_stdout.log`
- `04_fusion/THINKING_BAODIAN_V2_BODY_DRAFT.md`
- `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md`
- `04_fusion/PROMOTION_QUALITY_CHECK.md`
- `02_codex_lane/GAP026_2026_SHUNYI_ERMO_Q5_Q6_Q7_Q18_1_Q21_SOURCE_LOCK.md`

Output:

## B-line Shunyi Body Supplement

### Correction of prior premise
State clearly that the body files do exist under `04_fusion` and whether this changes any prior blocker.

### Body-level audit by question
For Q0136-Q0140, say whether the current body draft placement is acceptable, needs revision, or should stay out of the body.

### Required ledger or body edits
List concrete edits needed, if any.

### Machine summary
Use this exact CSV-like table:
`question_id,body_status,required_edit,blocker_required`
