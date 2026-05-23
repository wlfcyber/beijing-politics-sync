# Claude Zero-Baseline Iterative Test Round05 Progress

Status: `v13_5_real_claude_captured_passed_high_score_lock_but_v13_6_required`

- Created: 2026-05-23
- Test type: targeted stress retest after v13.5 high-score lock patch
- Selected questions: CC0200_2025_西城_二模_18, CC0157_2025_朝阳_期末_20, CC0084_2025_东城_二模_19, CC0189_2025_石景山_一模_20, CC0305_2026_海淀_一模_18_3
- Payload: `web_payloads/CLAUDE_ZERO_BASELINE_ITERATIVE_TEST_ROUND05_PAYLOAD.md`
- Local answer key not sent to Claude: `codex_adjudication/LOCAL_ANSWER_KEY_NOT_SENT_TO_CLAUDE.md`
- Acceptance target: structural A/B errors = 0; hidden-key rough total >= 45/50; Claude no longer requests a new framework-level patch for the four Round04 gaps.

## Completion

- Real Claude output captured:
  - `model_outputs/claude_zero_baseline_iterative_test_round05_opus47_raw.md`
  - `model_outputs/claude_zero_baseline_iterative_test_round05_opus47_visible_output_screenshot.png`
- Codex hidden-key adjudication:
  - `codex_adjudication/CODEX_EVALUATION_OF_CLAUDE_ITERATIVE_TEST_ROUND05.md`
- Result: v13.5 resolved Round04 gaps, but Claude and Codex still identified 95+ line-precision gaps. v13.6 required.
