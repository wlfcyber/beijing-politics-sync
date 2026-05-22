# GPT Round 03 Recovery Packet

Status: `needed_to_close_final_model_gate`

Use this only because the 2026-05-22 Chrome automation attempts could not capture a reliable ChatGPT response.

## Goal

Close the GPT Round 03 source-check review gate for:

`final_framework_candidate/FRAMEWORK_BASELINE_v12_2_SOURCE_CHECKED.md`

## Required Real Call

Open a visible ChatGPT web conversation in the `必修四喂细则` project and use the strongest available GPT Pro mode. If the UI shows the exact `GPT-5.5 Pro` label, record it. If it only shows `进阶专业` / `专业`, record that exact visible label and keep the model-label caution.

Paste and submit:

`web_payloads/GPT_ROUND_03_SOURCE_CHECK_REVIEW_FULL_PASTE_PAYLOAD.md`

## Save Output

Save the complete response to:

`model_outputs/gpt_round03_source_check_review.md`

The capture header must include:

- capture time
- visible model/mode label
- conversation URL
- whether completion was natural
- whether the response gave a concrete verdict

## Required Post-Capture Codex Work

After GPT output is captured:

1. Compare GPT Round 03 with Claude Round 03 and local source evidence.
2. Update `codex_adjudication/CODEX_ROUND03_SOURCE_CHECK_ADJUDICATION.md`.
3. If GPT agrees no structural change is needed, move the status from `candidate_baseline_prepared_gpt_round03_pending` to `candidate_baseline_ready_for_final_governor`.
4. If GPT requests structural change, accept it only if local evidence improves coverage, trunk clarity, hard-case placement, student transfer, or evidence hygiene.
5. Update `governance/GOVERNOR_GATE_CHECK_v12_2.md`.
6. Commit and push.

## Current Known State

- Claude Round 03 is completed and says `accept_source_checked_candidate_no_structural_change`.
- Codex local source check says 42/42 core rows remain mapped.
- The current six-entrance framework is complete as a candidate, but final PASS remains blocked by this GPT gate.

