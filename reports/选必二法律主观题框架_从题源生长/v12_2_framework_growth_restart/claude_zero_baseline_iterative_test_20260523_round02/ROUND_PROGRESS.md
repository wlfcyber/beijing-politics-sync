# Claude Zero-Baseline Iterative Test Round02 Progress

Status: `real_claude_capture_completed_codex_evaluated_v13_3_required`

- Created: 2026-05-23
- Test type: targeted stress retest after v13.2 zero-baseline toolbox patch
- Selected questions: CC0200_2025_西城_二模_18, CC0157_2025_朝阳_期末_20, CC0084_2025_东城_二模_19, CC0189_2025_石景山_一模_20, CC0305_2026_海淀_一模_18_3
- Payload: `web_payloads/CLAUDE_ZERO_BASELINE_ITERATIVE_TEST_ROUND02_PAYLOAD.md`
- Local answer key not sent to Claude: `codex_adjudication/LOCAL_ANSWER_KEY_NOT_SENT_TO_CLAUDE.md`
- Acceptance target: structural A/B errors = 0; rough total around 42/50; no single item below 7/10.
- Real Claude raw capture: `model_outputs/claude_zero_baseline_iterative_test_round02_opus47_raw.md`
- Real Claude screenshot: `model_outputs/claude_zero_baseline_iterative_test_round02_opus47_visible_output_screenshot.png`
- Codex evaluation: `codex_adjudication/CODEX_EVALUATION_OF_CLAUDE_ITERATIVE_TEST_ROUND02.md`
- Result: v13.2 improved A/B and B1 shape, but rough score is 40.5-41.5/50. v13.3 is required for responsibility-trigger table, standard exam terms, and B1 multi-case total-entry rule.
