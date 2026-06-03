# Worker Daily Orders

- generated_at: 2026-06-03T20:07:20+08:00
- rule: 每个分项AI每天先读本文件，再读自己的 lane 控制文件。

## Global Orders

1. 不经过三层SOP，不得读取、改写、同步或压缩项目资料。
2. 如果你被分配到某一书目/模块，必须先读对应 skill 和 hard-rule notebook。
3. 如果你的 lane 有 `possible_false_closure`、`real_call_pending`、`blocked_advisor`、缺 governor、缺 coverage、缺 traceability，先修控制闭环，不继续写正文。
4. 如果要处理超过 1MB 的日志/报告/JSON，先读 context capsule 和 manifest，再按需要打开原文局部。
5. 每次只推进一个最小完整步骤，先产出真实文件，再更新 `PROGRESS.md` 和 governor。

## Lane Orders

### 选必二重做_2026-04-30/raw_exam_subjective_compilation_2026-06-02/06_governor

- next_action: resolve visible blockers before content production
- flags: missing_progress
- risk_hits: blocked; 待; pending

### 选必二重做_2026-04-30/raw_exam_subjective_compilation_2026-06-02/07_acceptance

- next_action: resolve visible blockers before content production
- flags: missing_progress; missing_governor; acceptance_without_coverage
- risk_hits: blocked; 待; pending

### 选必二重做_2026-04-30/raw_exam_subjective_compilation_2026-06-02

- next_action: resolve visible blockers before content production
- flags: oversized_control:选必二重做_2026-04-30/raw_exam_subjective_compilation_2026-06-02/00_control/SOURCE_LEDGER.csv; missing_governor
- risk_hits: blocked; 待; 缺; pending

### 选必三双宝典_哲学宝典完全对齐返工_2026-05-25

- next_action: resolve visible blockers before content production
- flags: none
- risk_hits: BLOCKED; blocked; real_call_pending; blocked_advisor; 待; 缺; +3 more

### 选必三双宝典_哲学宝典完全对齐返工_2026-05-25/15_reasoning_direct_compilation_20260601

- next_action: resolve visible blockers before content production
- flags: none
- risk_hits: 缺

### 选必三双宝典_哲学宝典完全对齐返工_2026-05-25/14_reasoning_baodian_rebuild_after_v87_20260601

- next_action: resolve visible blockers before content production
- flags: none
- risk_hits: pending

### 选必三双宝典_哲学宝典完全对齐返工_2026-05-25/13_reasoning_clean_redo_20260531

- next_action: resolve visible blockers before content production
- flags: none
- risk_hits: 缺

### 选必三双宝典_哲学宝典完全对齐返工_2026-05-25/12_reasoning_exercise_compilation_20260531

- next_action: resolve visible blockers before content production
- flags: none
- risk_hits: 未完成

### 选必三双宝典_哲学宝典完全对齐返工_2026-05-25/06_candidate_audit/final_delivery_ultimate_20260531

- next_action: create or align PROGRESS.md before executing
- flags: missing_progress; missing_governor; acceptance_without_coverage
- risk_hits: none

### 选必二重做_2026-04-30/opus48_dynamic_workflow_subjective_compilation_2026-05-29/06_governor

- next_action: resolve visible blockers before content production
- flags: missing_progress
- risk_hits: blocked; 缺; pending

### 选必二重做_2026-04-30/opus48_dynamic_workflow_subjective_compilation_2026-05-29/07_acceptance

- next_action: resolve visible blockers before content production
- flags: missing_progress; missing_governor; acceptance_without_coverage
- risk_hits: 待; 缺; pending

### 选必二重做_2026-04-30/opus48_dynamic_workflow_subjective_compilation_2026-05-29

- next_action: resolve visible blockers before content production
- flags: none
- risk_hits: 待; 缺; pending

### 选必三双宝典_哲学宝典完全对齐返工_2026-05-25/10_acceptance

- next_action: resolve visible blockers before content production
- flags: stale>7d; acceptance_without_coverage; possible_false_closure
- risk_hits: BLOCKED; blocked; real_call_pending; blocked_advisor; 待; 缺; +3 more

### 选必三双宝典_哲学宝典完全对齐返工_2026-05-25/06_governor_confucius

- next_action: resolve visible blockers before content production
- flags: stale>7d
- risk_hits: real_call_pending; 缺; 未完成; pending

### 选必三双宝典_哲学宝典完全对齐返工_2026-05-25/09_external_review

- next_action: resolve visible blockers before content production
- flags: stale>7d; possible_false_closure
- risk_hits: BLOCKED; blocked; real_call_pending; blocked_advisor; 待; 缺; +3 more

### claude_zero_run

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_governor; possible_false_closure
- risk_hits: blocked; 待; 缺; pending

### 选必三双宝典_哲学宝典完全对齐返工_2026-05-25/11_claudecode_thick_lane_packet

- next_action: resolve visible blockers before content production
- flags: stale>7d; acceptance_without_coverage
- risk_hits: blocked; real_call_pending; 待; 缺; 未完成; pending

### claude_zero_run/supervision/backups_20260526_041947

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor; acceptance_without_coverage
- risk_hits: 待

### claude_zero_run/governor

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor; acceptance_without_coverage; possible_false_closure
- risk_hits: pending

### 选必三双宝典_哲学对齐重做_2026-05-25

- next_action: resolve visible blockers before content production
- flags: stale>7d
- risk_hits: blocked; real_call_pending; blocked_advisor; 缺; pending

### 选必三双宝典_哲学对齐重做_2026-05-25/04_delivery/选必三双宝典_哲学对齐重做_最终交付包_20260525

- next_action: resolve visible blockers before content production
- flags: stale>7d
- risk_hits: blocked; real_call_pending; blocked_advisor; 缺; pending

### 选必三双宝典_哲学对齐重做_2026-05-25/06_governor_confucius

- next_action: resolve visible blockers before content production
- flags: stale>7d
- risk_hits: 缺; pending

### 选必三双宝典_哲学对齐重做_2026-05-25/04_delivery/选必三双宝典_哲学对齐重做_最终交付包_20260525/06_governor_confucius

- next_action: resolve visible blockers before content production
- flags: stale>7d
- risk_hits: 缺; pending

### 选必三双宝典_哲学对齐重做_2026-05-25/05_external_review/review_packets/v9_q2_all_wrong_options_review

- next_action: verify final report against live artifacts
- flags: stale>7d; acceptance_without_coverage
- risk_hits: none

### 选必三双宝典_哲学对齐重做_2026-05-25/04_delivery/选必三双宝典_哲学对齐重做_最终交付包_20260525/05_external_review/review_packets/v9_q2_all_wrong_options_review

- next_action: verify final report against live artifacts
- flags: stale>7d; acceptance_without_coverage
- risk_hits: none

### 选必三双宝典_哲学对齐重做_2026-05-25/05_external_review/review_packets/v8_p1_closure_review

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; acceptance_without_coverage
- risk_hits: 待; 缺; 未完成

### 选必三双宝典_哲学对齐重做_2026-05-25/04_delivery/选必三双宝典_哲学对齐重做_最终交付包_20260525/05_external_review/review_packets/v8_p1_closure_review

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; acceptance_without_coverage
- risk_hits: 待; 缺; 未完成

### 选必三双宝典_哲学对齐重做_2026-05-25/02_source_index

- next_action: resolve visible blockers before content production
- flags: stale>7d
- risk_hits: 缺; pending

### 选必三双宝典_哲学对齐重做_2026-05-25/04_delivery/选必三双宝典_哲学对齐重做_最终交付包_20260525/02_source_index

- next_action: resolve visible blockers before content production
- flags: stale>7d
- risk_hits: 缺; pending

### 选必三双宝典_哲学对齐重做_2026-05-25/05_external_review/review_packets/v7_gpt_full_pdf_review

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; acceptance_without_coverage
- risk_hits: BLOCKED; real_call_pending; 缺; 未完成; pending

### 选必三双宝典_哲学对齐重做_2026-05-25/04_delivery/选必三双宝典_哲学对齐重做_最终交付包_20260525/05_external_review/review_packets/v7_gpt_full_pdf_review

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; acceptance_without_coverage
- risk_hits: BLOCKED; real_call_pending; 缺; 未完成; pending

### 选必三双宝典_哲学对齐重做_2026-05-25/05_external_review/review_packets/v6_gpt_light_review

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; acceptance_without_coverage
- risk_hits: real_call_pending; 缺; 未完成; pending

### 选必三双宝典_哲学对齐重做_2026-05-25/04_delivery/选必三双宝典_哲学对齐重做_最终交付包_20260525/05_external_review/review_packets/v6_gpt_light_review

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; acceptance_without_coverage
- risk_hits: real_call_pending; 缺; 未完成; pending

### 选必三双宝典_哲学对齐重做_2026-05-25/05_external_review/review_packets/v6_pdf_fix_review

- next_action: resolve visible blockers before content production
- flags: stale>7d; acceptance_without_coverage
- risk_hits: BLOCKED; real_call_pending; 待; 缺; 未完成; pending

### 选必三双宝典_哲学对齐重做_2026-05-25/04_delivery/选必三双宝典_哲学对齐重做_最终交付包_20260525/05_external_review/review_packets/v6_pdf_fix_review

- next_action: resolve visible blockers before content production
- flags: stale>7d; acceptance_without_coverage
- risk_hits: BLOCKED; real_call_pending; 待; 缺; 未完成; pending

### 选必三双宝典_哲学对齐重做_2026-05-25/05_external_review/review_packets/v5_full_review

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; acceptance_without_coverage
- risk_hits: real_call_pending; 缺; 未完成; pending

### 选必三双宝典_哲学对齐重做_2026-05-25/04_delivery/选必三双宝典_哲学对齐重做_最终交付包_20260525/05_external_review/review_packets/v5_full_review

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; acceptance_without_coverage
- risk_hits: real_call_pending; 缺; 未完成; pending

### 选必二法律主观题框架_从题源生长/05_reasoner_packets/gpt_textonly_v4

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; acceptance_without_coverage
- risk_hits: real_call_pending; 缺; 未完成; pending

### 选必二法律主观题框架_从题源生长/05_reasoner_packets/gpt_textonly_v3

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor; acceptance_without_coverage
- risk_hits: real_call_pending; 缺; 未完成; pending

### 选必二法律主观题框架_从题源生长/05_reasoner_packets/gpt_textonly_v2

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor; acceptance_without_coverage
- risk_hits: real_call_pending; 未完成; pending

### 选必二法律主观题框架_从题源生长/v12_1_reference_cleanup_and_stage_integration

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor; acceptance_without_coverage; possible_false_closure
- risk_hits: 缺; pending

### 选必二法律主观题框架_从题源生长

- next_action: resolve visible blockers before content production
- flags: stale>7d; possible_false_closure
- risk_hits: BLOCKED; blocked; real_call_pending; TODO; 待; 缺; +3 more

### 选必二法律主观题框架_从题源生长/05_reasoner_packets/v12_24_backfill_gptpro_review_ascii_20260522/v11_1

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor; acceptance_without_coverage
- risk_hits: 待; 未完成; pending

### 选必二法律主观题框架_从题源生长/05_reasoner_packets/v12_24_backfill_gptpro_review_ascii_20260522/v12

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor; acceptance_without_coverage; possible_false_closure
- risk_hits: 待; 无法; pending

### 选必二法律主观题框架_从题源生长/05_reasoner_packets/v12_24_backfill_gptpro_review_20260522/v11_1_written_chain_patch

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor; acceptance_without_coverage
- risk_hits: 待; 未完成; pending

### 选必二法律主观题框架_从题源生长/v12_24_question_backfill

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor; acceptance_without_coverage; possible_false_closure
- risk_hits: 待; 无法; pending

### 选必二法律主观题框架_从题源生长/05_reasoner_packets/v12_24_backfill_gptpro_review_20260522/v12_24_question_backfill

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor; acceptance_without_coverage; possible_false_closure
- risk_hits: 待; 无法; pending

### 选必二法律主观题框架_从题源生长/v11_1_written_chain_patch

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor; acceptance_without_coverage
- risk_hits: 待; 未完成; pending

### 选必二法律主观题框架_从题源生长/v11_source_locked_rebuild

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor; acceptance_without_coverage
- risk_hits: 待; pending

### 选必二法律主观题框架_从题源生长/v11_source_locked_rebuild/07_packet_for_gpt_review_ascii_20260521

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor; acceptance_without_coverage
- risk_hits: 待; pending

### 选必二法律主观题框架_从题源生长/v11_source_locked_rebuild/07_packet_for_gpt_review_20260521

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor; acceptance_without_coverage
- risk_hits: 待; pending

### 选必二法律主观题框架_从题源生长/v10_exhaustive_framework_and_all_questions

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor; acceptance_without_coverage
- risk_hits: pending

### 选必二法律主观题框架_从题源生长/v9_feige_style_rebuild

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor; acceptance_without_coverage
- risk_hits: 待; pending

### 选必二法律主观题框架_从题源生长/v8_1_student_delivery_fix

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor; acceptance_without_coverage
- risk_hits: 缺; pending

### 选必二法律主观题框架_从题源生长/v8_student_usable_rebuild/09_packet_for_user_gpt_review_20260521

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor; acceptance_without_coverage
- risk_hits: 缺; pending

### 选必二法律主观题框架_从题源生长/v8_student_usable_rebuild

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor; acceptance_without_coverage
- risk_hits: 缺; pending

### 选必二法律主观题框架_从题源生长/v8_student_usable_rebuild/00_model_packet/files

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor
- risk_hits: pending

### 新题增补_哲学_选必一_2026-05-18/08_governor

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; acceptance_without_coverage
- risk_hits: blocked; real_call_pending; 缺; pending

### 新题增补_哲学_选必一_2026-05-18

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_governor
- risk_hits: real_call_pending; 缺; pending

### run_control/desktop_mock_sort_2026-05-18

- next_action: add governor check before claiming completion
- flags: stale>7d; missing_governor
- risk_hits: none

### 选必三逻辑与思维_四线从0重跑_2026-05-04/claude_cowork/phase13_framework_rebuild/input_packet

- next_action: create or align PROGRESS.md before executing
- flags: stale>7d; missing_progress; missing_governor
- risk_hits: none

### 选必三逻辑与思维_四线从0重跑_2026-05-04

- next_action: resolve visible blockers before content production
- flags: stale>7d; possible_false_closure
- risk_hits: BLOCKED; blocked; real_call_pending; blocked_advisor; 待; 缺; +3 more

### 选必二重做_2026-04-30/claudecode_full_rerun_2026-05-05

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; acceptance_without_coverage
- risk_hits: real_call_pending; 待; 缺; 无法; pending

### 选必二重做_2026-04-30/claudecode_lane_C_full_rerun_2026-05-05

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_governor; acceptance_without_coverage; possible_false_closure
- risk_hits: real_call_pending; web_visible_pro_adaptive_call_pending_user_waived; 待; 缺; 无法; pending

### 选必二重做_2026-04-30/claudecode_lane_C_full_rerun_2026-05-05/governor

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress
- risk_hits: 待; 无法

### 选必三逻辑与思维_四线从0重跑_2026-05-04/09_student_draft

- next_action: create or align PROGRESS.md before executing
- flags: stale>7d; missing_progress; missing_governor
- risk_hits: none

### 选必二重做_2026-04-30/claudecode_lane_B_full_rerun_2026-05-04

- next_action: resolve visible blockers before content production
- flags: stale>7d; acceptance_without_coverage
- risk_hits: real_call_pending; 待; 缺; 无法; pending

### 选必三逻辑与思维_四线从0重跑_2026-05-04/opus_writer/phase08_teaching_prototype

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_governor
- risk_hits: blocked; 未完成

### 选必一_当代国际政治与经济_四线终极全书_2026-05-03/10_teaching_rebuild_20260504/03_review

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress
- risk_hits: 缺

### 选必一_当代国际政治与经济_四线终极全书_2026-05-03

- next_action: resolve visible blockers before content production
- flags: stale>7d; possible_false_closure
- risk_hits: BLOCKED; blocked; real_call_pending; 待; 缺; pending

### 选必一_当代国际政治与经济_四线终极全书_2026-05-03/10_teaching_rebuild_20260504/05_acceptance

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor; acceptance_without_coverage
- risk_hits: 缺

### 选必二重做_2026-04-30/claudecode_full_rerun_2026-05-04/source_inventory

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor
- risk_hits: 待; pending

### 选必二重做_2026-04-30/claudecode_full_rerun_2026-05-04

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_governor
- risk_hits: real_call_pending; 待; 缺; 无法; pending

### 选必二重做_2026-04-30/strict_four_lane_closure_2026-05-04

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; acceptance_without_coverage
- risk_hits: TODO; 缺

### 选必二重做_2026-04-30

- next_action: resolve visible blockers before content production
- flags: stale>7d; acceptance_without_coverage; possible_false_closure
- risk_hits: BLOCKED; blocked; 待; 缺; 未完成; 无法; +1 more

### 选必三逻辑与思维_完全模仿哲学宝典返工_2026-05-04

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress; missing_governor; acceptance_without_coverage
- risk_hits: 缺

### 选必三逻辑与思维双线四线终极跑_2026-05-04

- next_action: resolve visible blockers before content production
- flags: stale>7d; possible_false_closure
- risk_hits: blocked; 待; 缺; 无法

### 选必一_当代国际政治与经济_四线终极全书_2026-05-03/codex_lane/agents/governor

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress
- risk_hits: BLOCKED; blocked; 待; 缺; 未完成; pending

### 选必二重做_2026-04-30/framework_bootstrap_2026-05-03

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_governor
- risk_hits: blocked; real_call_pending; blocked_advisor; 待; 缺; 未完成; +2 more

### 选必一_四线终极版_五题样例_2026-05-03

- next_action: refresh lane state and register next step
- flags: stale>7d
- risk_hits: none

### 选必一_当代国际政治与经济_从0重跑_GPT55内容监督_ClaudeCode完整复跑_2026-05-02

- next_action: resolve visible blockers before content production
- flags: stale>7d
- risk_hits: blocked; pending

### 选必一_当代国际政治与经济_双线总控_2026-05-02

- next_action: resolve visible blockers before content production
- flags: stale>7d; possible_false_closure
- risk_hits: blocked; 待; 缺; pending

### 选必一_当代国际政治与经济_双线总控_2026-05-02/audit

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress
- risk_hits: blocked

### 必修四从0重跑_ClaudeCode_2026-05-02

- next_action: resolve visible blockers before content production
- flags: stale>7d; possible_false_closure
- risk_hits: blocked; 缺

### reports

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_progress
- risk_hits: 待; 缺; 未完成

### 必修四框架重做_2026-04-29

- next_action: add governor check before claiming completion
- flags: stale>7d; missing_governor
- risk_hits: none

### codex_continuous/jobs/哲学必修四_三线闭环穷尽满分课

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_governor
- risk_hits: 待; 缺; 未完成

### codex_continuous/jobs/选必三_思维触发穷尽

- next_action: resolve visible blockers before content production
- flags: stale>7d; missing_governor
- risk_hits: 缺
