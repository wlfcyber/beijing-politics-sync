# ClaudeCode T1 Visible Window Task: Phase11D Seed Audit And Next Batch Queue

You are the T1 Terminal ClaudeCode visible-window worker for the current 选必三《逻辑与思维》run.

Hard routing:

- Workdir: `/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`
- You are T1 Terminal ClaudeCode. Do not touch the user's separate VSCode ClaudeCode lane.
- Write only under: `claudecode_lane/phase11D_visible_seed_and_next_batch_audit/`
- Do not edit `09_student_draft/`, `outputs/`, `09_delivery/`, or any Word/PDF artifact.
- Do not generate `.docx`, `.pdf`, final, PASS, 终稿, 最终稿, 宝典成品.
- Your output is worker feedback only. Codex will separately source-verify before merging.

Read first:

1. `/Users/wanglifei/.codex/skills/feige-politics-garden/SKILL.md`
2. `/Users/wanglifei/.codex/skills/feige-politics-garden-book-orchestrator/SKILL.md`
3. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/SKILL.md`
4. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md`
5. `00_control/CLAUDECODE_THREAD_ROUTING_2026-05-05.md`
6. `claudecode_lane/phase11C_bad_word_content_audit_visible/four_element_gold_contract.md`
7. `claudecode_lane/phase11C_bad_word_content_audit_visible/next_rebuild_plan.md`
8. `09_student_draft/phase11D_seed_source_verified_04_REVIEW_ONLY.md`
9. `08_review/phase11D_seed_source_ledger.csv`
10. `08_review/phase11D_four_element_gate/phase11D_seed_source_verified_04_REVIEW_ONLY_four_element_gate.md`
11. `09_student_draft/phase11A_student_body_PATCHED_REVIEW_ONLY.md`
12. `09_student_draft/phase10_5_source_repair_priority_queue.md`
13. `09_student_draft/phase11B_batch01_student_body_30_REVIEW_ONLY.md`

Task A: audit the 8-entry Phase11D seed.

For each entry in `phase11D_seed_source_verified_04_REVIEW_ONLY.md`, check against the Gold Contract:

- material trigger: concrete source signal, not topical summary;
- question prompt: looks like real question wording, not template;
- why logic: teaches why this method is triggered, not term listing;
- answer landing: student can write it on paper; includes method term + material fact + effect/conclusion;
- choice question: includes correct option reason, tempting wrong option reason, and trap type;
- no internal audit terms or forbidden wording;
- module boundary is stable.

Output:

- `claudecode_lane/phase11D_visible_seed_and_next_batch_audit/phase11D_seed_audit_matrix.csv`
  - columns: `entry_title,entry_type,material_trigger,question_prompt,why_logic,answer_landing,choice_trap,boundary,student_cleanliness,verdict,must_fix,should_fix`
- `claudecode_lane/phase11D_visible_seed_and_next_batch_audit/phase11D_seed_audit_report.md`
  - include an overall verdict: `PASS_SEED_FOR_GPT_REVIEW_ONLY`, `MUST_FIX_SEED_BEFORE_EXPANSION`, or `BLOCKED_NEEDS_SOURCE`.

Task B: propose the next visible Phase11D batch, but do not edit the student draft.

Use the priority queue and Phase11A/11B review-only drafts to propose 10 next candidates. Prefer source-stable, high-value entries already in Phase11A/11B, especially L4/L3 source-verified thought-method entries. Do not promote P0 protected hold rows, hard-excluded rows, L0 rows, or entries that still need source recovery.

For each proposed candidate, explain why it should be next and what source checks are still needed.

Output:

- `claudecode_lane/phase11D_visible_seed_and_next_batch_audit/phase11D_next_batch_candidate_queue.csv`
  - columns: `rank,question_id,title,type,priority_reason,source_stability,expected_four_element_risk,do_not_promote_reason_if_any`
- `claudecode_lane/phase11D_visible_seed_and_next_batch_audit/phase11D_next_batch_rewrite_plan.md`
  - include a 10-row plan and any blocked rows.

Task C: optional sample rewrites.

If and only if you can do so without guessing source facts, write up to 5 review-only four-element sample rewrites under your output directory:

- `claudecode_lane/phase11D_visible_seed_and_next_batch_audit/phase11D_next_batch_sample_rewrites_REVIEW_ONLY.md`

Each sample must use exactly:

`【材料触发点】`
`【设问】`
`【为什么能想到】`
`【答案落点】`

If source evidence is insufficient, write `BLOCKED_NEEDS_SOURCE` instead of guessing.

Task D: progress.

Write:

- `claudecode_lane/phase11D_visible_seed_and_next_batch_audit/progress.md`
- `claudecode_lane/phase11D_visible_seed_and_next_batch_audit/phase11D_visible_status.md`

Final line of your Terminal response should be:

`T1_PHASE11D_VISIBLE_OUTPUTS_WRITTEN_NO_STUDENT_MERGE_NO_WORD`
