# Claude Zero-Baseline Iterative Test Round04 Progress

Status: `v13_4_real_claude_captured_high_score_not_final_v13_5_required`

- Created: 2026-05-23
- Test type: targeted stress retest after v13.4 boundary decision patch
- Selected questions: CC0200_2025_西城_二模_18, CC0157_2025_朝阳_期末_20, CC0084_2025_东城_二模_19, CC0189_2025_石景山_一模_20, CC0305_2026_海淀_一模_18_3
- Payload: `web_payloads/CLAUDE_ZERO_BASELINE_ITERATIVE_TEST_ROUND04_PAYLOAD.md`
- Local answer key not sent to Claude: `codex_adjudication/LOCAL_ANSWER_KEY_NOT_SENT_TO_CLAUDE.md`
- Acceptance target: structural A/B errors = 0; hidden-key rough total >= 43/50; no unresolved framework-level patch required by Claude or Codex.

## Completion

- Real Claude output captured:
  - `model_outputs/claude_zero_baseline_iterative_test_round04_opus47_raw.md`
  - `model_outputs/claude_zero_baseline_iterative_test_round04_opus47_visible_output_screenshot.png`
- Codex hidden-key adjudication:
  - `codex_adjudication/CODEX_EVALUATION_OF_CLAUDE_ITERATIVE_TEST_ROUND04.md`
- Result: structural gate passed, but Claude and Codex still identified high-score framework gaps. v13.5 required.
