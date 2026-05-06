# ClaudeCode Lane B Phase07 Locked Packet Audit

You are ClaudeCode Lane B for the user's Beijing Gaokao politics 选必三《逻辑与思维》四线从0重跑.

Runtime requirement: Claude Opus 4.7 max/adaptive thinking. Caller will launch with `--model opus --effort max`. This is audit-only. Do not write student稿, teaching prose, Word/PDF, or final PASS.

## Workspace

```text
/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04
```

Write all outputs only under:

```text
claudecode_lane/opus47_phase07_locked_packet_audit/
```

## Highest Rules

1. Phase07 is locked Opus input packet preparation only.
2. Opus is still not allowed to write teaching text.
3. Student稿, Word/PDF, final PASS, and 宝典成品 claims remain forbidden.
4. Audit whether Codex A correctly splits 74 evidence rows into include / hold.
5. Audit that all 288 L0 rows are excluded.
6. Audit that all 13 cross rows remain double-mounted.
7. Audit hard locks:
   - Q-2024西城一模-11 answer B and pairing B=①③; retired wrong pairing must not appear as Q11 correct pairing.
   - Q-2025海淀二模-12 answer D + render_008_page_04 + supplemental answer table page 9.
   - Q-2025海淀二模-13 answer C + render_008_page_04 + supplemental answer table page 9.
   - Q-2026顺义一模-3 must not enter reasoning input.

## Read These Files

```text
08_review/gpt_phase_advice/phase_06_gpt55_digest.md
08_review/gpt_phase_advice/phase_06_gpt55_raw.md
06_conflicts/phase06_laneB_warning_patch_resolution.md
06_conflicts/phase05_patch_freeze_after_laneB_warnings.md
05_coverage/phase07_locked_opus_input_packet.csv
05_coverage/phase07_opus_input_thinking_entries.csv
05_coverage/phase07_opus_input_reasoning_entries.csv
05_coverage/phase07_opus_input_cross_entries.csv
05_coverage/phase07_cross_mount_opus_policy.md
05_coverage/phase07_L3_hold_list.csv
05_coverage/phase07_L3_promote_or_hold_decision.md
05_coverage/phase07_L0_excluded_from_opus_input.csv
05_coverage/phase07_L0_exclusion_summary.md
06_conflicts/phase07_hard_lock_audit.md
06_conflicts/phase07_hard_lock_audit.csv
05_coverage/phase07_opus_input_boundary_rules_FINAL_FOR_PACKET.md
05_coverage/phase07_Governor_locked_packet_gate.md
05_coverage/phase07_Confucius_locked_packet_value_gate.md
05_coverage/phase07_GPT_commander_review_packet.md
codex_lane/phase07_local_audit/phase07_codexA_local_audit.md
```

You may compare to Phase06 inputs:

```text
05_coverage/phase06_evidence_lock_register.csv
05_coverage/phase06_thinking_framework_fusion.csv
05_coverage/phase06_reasoning_typology_fusion.csv
05_coverage/phase06_cross_mount_lock.csv
05_coverage/phase06_L0_blocker_retention_register.csv
```

## Required Part A: Phase06 Warning Patch Ack

Produce:

```text
claudecode_lane/opus47_phase07_locked_packet_audit/phase06_warning_patch_ack.csv
claudecode_lane/opus47_phase07_locked_packet_audit/phase06_warning_patch_ack.md
```

CSV fields:

```text
finding_id,patch_point,result,details
```

Check these eight items:

```text
F01 Q-2026朝阳期中-13 answer_action is no longer only D.
F02 Q-2026丰台一模-4 method is 分析与综合；综合思维.
F03 Q-2026朝阳期中-11 rule_slogan is no longer only A and is a 三段论补大前提 rule.
F04 Q-2026朝阳期中-13 rule_slogan is no longer only D and contains 类比/联想/感性具体 boundary.
F05 duplicated/generic answer_action count is zero.
F06 letter-only answer_locator count is zero.
F07 L0 summary contains all 8 blocker groups, including zero-count groups.
F08 Phase05 patch freeze is acknowledged by Lane B Phase06 audit.
```

## Required Part B: Phase07 Locked Packet Audit

Produce:

```text
claudecode_lane/opus47_phase07_locked_packet_audit/phase07_laneB_locked_packet_audit.csv
claudecode_lane/opus47_phase07_locked_packet_audit/phase07_laneB_locked_packet_audit.md
claudecode_lane/opus47_phase07_locked_packet_audit/phase07_laneB_locked_packet_audit_findings.csv
claudecode_lane/opus47_phase07_locked_packet_audit/phase07_laneB_locked_packet_audit_blockers.md
claudecode_lane/opus47_phase07_locked_packet_audit/progress.md
```

Audit CSV fields:

```text
check_id,scope,result,severity,details
```

Findings CSV fields:

```text
finding_id,severity,file,row_or_section,issue,required_patch
```

Required checks:

1. Packet has 74 rows.
2. Packet permission counts match Codex claim: include=4, include_as_packet_candidate=25, hold_answer_locator_risk=25, hold_reasoning_form_risk=20.
3. Packet has no `student_permission` other than `no`.
4. Packet has no `opus_permission` other than `packet_only`.
5. All 70 L3 rows appear in `phase07_L3_hold_list.csv`.
6. At least one L3 is held; all L3 are not blindly included.
7. All 288 L0 rows appear in L0 exclusion file and no L0 appears in input entries.
8. Thinking input entries include only include/included-candidate rows and contain critical fields.
9. Reasoning input entries include only include/included-candidate rows and contain critical fields.
10. Q-2026顺义一模-3 is not in reasoning input.
11. Q11/Q12/Q13 hard locks pass.
12. All 13 cross rows appear in cross input policy; no cross row has `forbidden_single_mount` other than `yes`.
13. Boundary rules forbid Opus from adding/deleting/changing answers/status/single-mounting/generating student稿/Word/PDF.
14. Governor/Confucius gates do not authorize student稿 or Opus prose.

Final markdown verdict must be exactly one of:

```text
PASS_PHASE07_WITH_NO_BLOCKERS
PASS_PHASE07_WITH_WARNINGS
PATCH_PHASE07_BEFORE_GPT
BLOCK_RETURN_TO_PHASE06_OR_SOURCE
```

Again: do not write teaching text. Do not create Word/PDF. Do not mark final complete.
