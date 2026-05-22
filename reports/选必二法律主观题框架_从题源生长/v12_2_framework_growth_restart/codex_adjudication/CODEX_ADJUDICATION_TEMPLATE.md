# Codex adjudication template

## Inputs checked

- [ ] GPT Round 01 output exists.
- [ ] Claude Round 01 output exists.
- [ ] GPT critique of Claude exists.
- [ ] Claude critique of GPT exists.
- [ ] Evidence pack version is unchanged during the model calls.

## Candidate changes

| change_id | source_model | proposed_change | supporting_question_ids | evidence_strength | accept_modify_reject_pending | reason |
|---|---|---|---|---|---|---|

## Required decisions

1. High-frequency trunk nodes accepted.
2. Open containers accepted.
3. Reference-only questions quarantined.
4. Next-backfill six questions: promote / keep pending / downgrade.
5. Coverage delta from v12.1.
6. Student-start language risk.
7. Evidence hygiene risk.

## Verdict

Allowed verdicts only:

- `blocked_advisor`
- `candidate_pending_cross_critique`
- `candidate_pending_evidence_adjudication`
- `framework_candidate_v12_2`

Do not write final PASS, final baodian, DOCX, PDF, or TASK_COMPLETE in this file.

