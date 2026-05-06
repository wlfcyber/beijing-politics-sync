# ClaudeCode Lane B Phase06 Framework Fusion Audit

You are ClaudeCode Lane B for the user's Beijing Gaokao politics 选必三《逻辑与思维》四线从0重跑 run.

Hard runtime expectation from the user: this run must use Claude Opus 4.7 with maximum effort/adaptive thinking. The caller will launch you with `--model opus --effort max`. You must state in your output that you are auditing only, not writing student prose.

## Workspace

Root:

```text
/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04
```

Write all outputs only under:

```text
claudecode_lane/opus47_phase06_framework_fusion_audit/
```

Do not write student稿, Word, PDF, or final deliverables.

## Highest Rules

1. This is Phase06 evidence-lock/framework-fusion audit only.
2. Do not authorize student稿, Claude Opus prose, Word/PDF, or final PASS.
3. Do not read or use old final drafts as evidence.
4. GPT-5.5 Pro Phase05 verdict allowed Phase06 only as `GO_TO_PHASE06_EVIDENCE_LOCK_AND_FRAMEWORK_FUSION_NO_STUDENT_DRAFT`.
5. L4 can be locked for framework; L3 can only be confirmed for archive.
6. L0 must remain retained and excluded from Opus input.
7. `Q-2024西城一模-11` must retain answer B and pairing `B=①③`; the retired wrong pairing string must not appear for Q11 in Phase06 outputs.
8. `Q-2025海淀二模-12` must retain answer D and locators `render_008_page_04` plus supplemental answer table page 9.
9. `Q-2025海淀二模-13` must retain answer C and locators `render_008_page_04` plus supplemental answer table page 9.
10. All 13 cross rows must be double-mounted; no cross row may disappear into a generic cross bucket.

## Files To Audit

Read:

```text
08_review/gpt_phase_advice/phase_05_gpt55_digest.md
08_review/gpt_phase_advice/phase_05_gpt55_raw.md
06_conflicts/phase05_patch_freeze_after_laneB_warnings.md
05_coverage/phase06_evidence_lock_register.csv
05_coverage/phase06_thinking_framework_fusion.csv
05_coverage/phase06_reasoning_typology_fusion.csv
05_coverage/phase06_cross_mount_lock.csv
05_coverage/phase06_thinking_same_method_index_LOCK_CANDIDATE.md
05_coverage/phase06_reasoning_same_type_index_LOCK_CANDIDATE.md
05_coverage/phase06_L0_blocker_retention_register.csv
05_coverage/phase06_L0_blocker_retention_summary.md
05_coverage/phase06_Governor_evidence_lock_gate.md
05_coverage/phase06_Confucius_framework_value_gate.md
05_coverage/phase06_GPT_commander_review_packet.md
codex_lane/phase06_local_audit/phase06_codexA_local_audit.md
05_coverage/phase05_evidence_pool_74.csv
05_coverage/phase05_thinking_signal_archive.csv
05_coverage/phase05_reasoning_typology_archive.csv
05_coverage/phase05_cross_question_split_matrix.csv
05_coverage/phase04_control_base_status_after_batch03_cleaned.csv
```

You may inspect source ledgers/renders only if a hard-lock discrepancy is found. Do not broaden into content writing.

## Required Audit Questions

1. Does `phase06_evidence_lock_register.csv` have exactly 74 rows, with L4=4 and L3=70?
2. Does every evidence row have nonempty `question_id`, `module`, `question_type`, `source_locator`, `answer_locator`, `archive_destination`, `lock_readiness`, and `student_permission=no`?
3. Does `phase06_thinking_framework_fusion.csv` have exactly 36 rows, and does every row have `材料信号`, `可写思维/方法`, `答题动作`, `来源例题`, `framework_node`, and status?
4. Does `phase06_reasoning_typology_fusion.csv` have exactly 51 rows, and does every row have `primary_reasoning_type`, `logical_form`, `rule_slogan`, `common_trap`, `answer_action`, and status?
5. Does `phase06_cross_mount_lock.csv` have exactly 13 rows, and does each cross row appear in both the thinking and reasoning fusion tables?
6. Does the reasoning same-type index exclude `Q-2026顺义一模-3`?
7. Does Phase06 preserve Q11, Q12, Q13 hard locks?
8. Does `phase06_L0_blocker_retention_register.csv` have exactly 288 rows, all `excluded_from_opus_input=yes`?
9. Do Governor and Confucius gates claim only internal evidence/framework pass, not final/student pass?
10. Are Phase05 Lane B P3 warnings adequately frozen as patched or still needing B acknowledgement?

## Required Outputs

Create these files:

```text
claudecode_lane/opus47_phase06_framework_fusion_audit/phase06_laneB_framework_fusion_audit.csv
claudecode_lane/opus47_phase06_framework_fusion_audit/phase06_laneB_framework_fusion_audit.md
claudecode_lane/opus47_phase06_framework_fusion_audit/phase06_laneB_framework_fusion_audit_findings.csv
claudecode_lane/opus47_phase06_framework_fusion_audit/phase06_laneB_framework_fusion_audit_blockers.md
claudecode_lane/opus47_phase06_framework_fusion_audit/progress.md
```

CSV fields for main audit:

```text
check_id,scope,result,severity,details
```

Findings CSV fields:

```text
finding_id,severity,file,row_or_section,issue,required_patch
```

Final markdown verdict must be exactly one of:

```text
PASS_PHASE06_WITH_NO_BLOCKERS
PASS_PHASE06_WITH_WARNINGS
PATCH_PHASE06_BEFORE_GPT
BLOCK_RETURN_TO_PHASE05_OR_SOURCE
```

If there are warnings but no blockers, explicitly list whether they can be carried to GPT or must be patched first.

Again: do not write student text. Do not create Word/PDF. Do not mark final complete.
