# Framework growth ledger

| round | status | evidence_batch | GPT output | Claude output | cross critique | Codex adjudication | verdict |
|---|---|---|---|---|---|---|---|
| round01 | adjudicated_candidate | batch_01 + batch_02 + batch_03 | captured: `model_outputs/gpt_round01_independent_framework.md` | captured: `model_outputs/claude_round01_independent_framework.md` | captured: `cross_critiques/gpt_critiques_claude_round01.md` + `cross_critiques/claude_critiques_gpt_round01.md` | `codex_adjudication/CODEX_ROUND01_ROUND02_ADJUDICATION.md` | candidate_pending_source_check |
| round01_source_check | codex_source_checked | pending IDs from candidate framework | same Round 01 GPT output, no new model call | same Round 01 Claude output, no new model call | no new cross critique | `codex_source_checks/pending_source_check_20260522.md` | candidate_source_checked_round01_not_final |
| round03_payloads | payloads_prepared | source-check overlay + coverage delta | `web_payloads/GPT_ROUND_03_SOURCE_CHECK_REVIEW_FULL_PASTE_PAYLOAD.md` pending submission | `web_payloads/CLAUDE_ROUND_03_SOURCE_CHECK_REVIEW_FULL_PASTE_PAYLOAD.md` pending submission | not started | `codex_source_checks/coverage_delta_after_source_check_20260522.md` | round03_real_call_pending |
| round03_claude_review | partial_real_review | source-check overlay + coverage delta | blocked: `model_outputs/gpt_round03_browser_attempt_blocked_20260522.md` | completed: `model_outputs/claude_round03_source_check_review_key_capture.md` | no new cross critique | `codex_adjudication/CODEX_ROUND03_SOURCE_CHECK_ADJUDICATION.md` | candidate_baseline_prepared_gpt_round03_pending |
| source_checked_baseline | candidate_written | 42/42 source-checked core + Claude Round 03 deltas | pending | used as completed one-sided review | no new cross critique | `final_framework_candidate/FRAMEWORK_BASELINE_v12_2_SOURCE_CHECKED.md` + `traceability/TRACEABILITY_MATRIX_v12_2.md` + `governance/GOVERNOR_GATE_CHECK_v12_2.md` | complete_candidate_pending_gpt_round03_and_governance |
| round03_gpt_review | completed_real_review | source-check overlay + coverage delta | captured: `model_outputs/gpt_round03_source_check_review.md` | completed: `model_outputs/claude_round03_source_check_review_key_capture.md` | no new cross critique needed; both reviewed same source-check delta | `codex_adjudication/CODEX_ROUND03_SOURCE_CHECK_ADJUDICATION.md` | complete_source_checked_framework_baseline_gpt_claude_reviewed |

## Current instruction

Round 01 real model council is complete and locally adjudicated. Round 03 now has both Claude and ChatGPT web review captures. The source-checked framework baseline is complete; final baodian/DOCX delivery is a separate document-production gate.
