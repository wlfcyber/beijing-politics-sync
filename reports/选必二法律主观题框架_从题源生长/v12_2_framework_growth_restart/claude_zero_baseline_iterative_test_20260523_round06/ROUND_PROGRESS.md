# Claude Zero-Baseline Iterative Test Round06 Progress

Status: `v13_6_real_claude_captured_passed_contract_precision_but_v13_7_required`

- Created: 2026-05-23
- Test type: targeted stress retest after v13.6 95plus precision patch
- Selected questions: CC0200_2025_西城_二模_18, CC0157_2025_朝阳_期末_20, CC0084_2025_东城_二模_19, CC0189_2025_石景山_一模_20, CC0305_2026_海淀_一模_18_3
- Payload: `web_payloads/CLAUDE_ZERO_BASELINE_ITERATIVE_TEST_ROUND06_PAYLOAD.md`
- Local answer key not sent to Claude: `codex_adjudication/LOCAL_ANSWER_KEY_NOT_SENT_TO_CLAUDE.md`
- Acceptance target: structural A/B errors = 0; hidden-key rough total >= 46/50; Claude no longer requests a new framework-level patch for Round04/Round05 gaps.

## Completion

- Real Claude output captured:
  - `model_outputs/claude_zero_baseline_iterative_test_round06_opus47_raw.md`
  - `model_outputs/claude_zero_baseline_iterative_test_round06_opus47_visible_output_screenshot.png`
- Codex hidden-key adjudication:
  - `codex_adjudication/CODEX_EVALUATION_OF_CLAUDE_ITERATIVE_TEST_ROUND06.md`
- Result: v13.6 resolved contract responsibility and base dual-chain precision, but Claude and Codex still identified B1/B3 final precision gaps. v13.7 required.
