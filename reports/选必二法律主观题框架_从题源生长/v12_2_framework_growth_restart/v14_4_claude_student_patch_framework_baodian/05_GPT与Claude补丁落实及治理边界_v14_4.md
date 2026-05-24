# 05 GPT 与 Claude 补丁落实及治理边界 v14.4

## Real GPT Pro Gate

Status: `GPT_REVIEW_PASS_AFTER_PATCH_CAPTURED_AS_PATCH_SOURCE`

Evidence:

- `../v14_2_zero_baseline_framework_baodian/external_gate_attempts/GPT_PRO_REVIEW_PROMPT_v14_2_with_prior_framework.md`
- `../v14_2_zero_baseline_framework_baodian/external_gate_attempts/GPT_PRO_REVIEW_v14_2_WITH_PRIOR_FRAMEWORK_CAPTURE_20260524.md`

Boundary:

- GPT Pro did run in the user's Chrome Pro session and read the five uploaded files.
- Full raw transcript export failed after long output; the capture file records the visible verdict and patch list.
- v14.3 implemented GPT's minimum patch list.

## Real Claude Student Simulation Gate

Status: `CLAUDE_STUDENT_PASS_AFTER_PATCH_CAPTURED`

Evidence:

- `claude_student_simulation/CLAUDE_OPUS47_ZERO_BASELINE_STUDENT_RESULT_v14_3_20260524.md`

Boundary:

- Claude Opus 4.7 Adaptive ran as a zero-baseline smart student.
- It saw only the v14.3 framework and 8-question blind test pack, not the 42-question answer cards.
- It judged v14.3 could prevent major direction errors but still lacked enough student-facing rule detail for high marks.

## v14.4 Patch List

1. Split C axis into `C-rule` and `C-write`.
2. Added A-axis decision tree.
3. Added explicit A1 main-spine threshold.
4. Expanded mixed-question combinations from 4 to 8.
5. Added reverse-screening rule for approval/public notice/inspection as evidence rather than A10.
6. Added score-to-length map.
7. Added reference-example writing method.
8. Added five legal-detail cards: burden of proof, good-faith ride, punitive damages, minor tipping/large consumption, foreseeable business loss.
9. Removed student-facing 42-question distribution noise from the main framework.

## Remaining Boundary

v14.4 is a Markdown candidate after GPT and Claude patch application. It is not a DOCX/PDF delivery. It still should be run through a second Claude zero-baseline student simulation before claiming final external pass.
