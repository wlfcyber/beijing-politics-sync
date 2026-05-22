# Framework growth ledger

| round | status | evidence_batch | GPT output | Claude output | cross critique | Codex adjudication | verdict |
|---|---|---|---|---|---|---|---|
| round01 | adjudicated_candidate | batch_01 + batch_02 + batch_03 | captured: `model_outputs/gpt_round01_independent_framework.md` | captured: `model_outputs/claude_round01_independent_framework.md` | captured: `cross_critiques/gpt_critiques_claude_round01.md` + `cross_critiques/claude_critiques_gpt_round01.md` | `codex_adjudication/CODEX_ROUND01_ROUND02_ADJUDICATION.md` | candidate_pending_source_check |
| round01_source_check | codex_source_checked | pending IDs from candidate framework | same Round 01 GPT output, no new model call | same Round 01 Claude output, no new model call | no new cross critique | `codex_source_checks/pending_source_check_20260522.md` | candidate_source_checked_round01_not_final |
| round03_payloads | payloads_prepared | source-check overlay + coverage delta | `web_payloads/GPT_ROUND_03_SOURCE_CHECK_REVIEW_FULL_PASTE_PAYLOAD.md` pending submission | `web_payloads/CLAUDE_ROUND_03_SOURCE_CHECK_REVIEW_FULL_PASTE_PAYLOAD.md` pending submission | not started | `codex_source_checks/coverage_delta_after_source_check_20260522.md` | round03_real_call_pending |

## Current instruction

Round 01 real model council is complete and locally adjudicated. The next work is not a new fake council; it is local source hygiene and, if the framework is changed again, a new real GPT/Claude evidence cycle.
