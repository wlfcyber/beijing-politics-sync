# Phase12 77-Row External Review Packet Manifest

Status: `USER_UPLOAD_READY_NO_FINAL_AUTHORIZATION`

本包用于提交给 GPT-5.5 Pro、可见 ClaudeCode 或 Claude Opus 4.7 Adaptive 做内容审查。不得据此生成 Word/PDF/final。

## 当前状态

- review-only 正文：77 条。
- 主观题：27 条。
- 选择题：50 条。
- 排序：主观题在前，选择题在后；每类内部按海淀、西城、东城、朝阳、丰台、其他区；年份 2026 > 2025 > 2024。
- 选择题选项可见性：50 道选择题已修复，24 道显示完整 ①②③④ 单位，26 道显示 A/B/C/D 选项，修复队列 0。
- 元数据预清洗：已删除重复 question_id 注释 74 个、重复“选择题”大标题 1 个；保留每题一个审稿锚点，不改知识内容。
- 最终 clean build 前置审计：本地结构可继续外审，但 GPT-5.5 Pro、可见 ClaudeCode、Opus 4.7 Adaptive 三个外部硬门仍未捕获。
- 仍然禁止：Word、PDF、final、终稿、宝典成品、TASK_COMPLETE。

## 建议提交方式

把压缩包 `phase12_77row_external_review_packet_2026-05-05.zip` 上传给外部模型，并复制对应 prompt：

- GPT-5.5 Pro：`phase_12_77body_prompt_for_gpt55_USER_SUBMIT.md`
- 可见 ClaudeCode：`claudecode_phase12_visible_77body_audit_prompt.md`
- Claude Opus 4.7 Adaptive：`phase_12_77body_prompt_for_claude_opus47_adaptive.md`

## 包内文件

- `09_student_draft/phase12_expanded_body_FROM_362_REVIEW_ONLY.md`
- `09_student_draft/phase12_expanded_body_FROM_362_control_matrix.csv`
- `09_student_draft/phase12_thinking_method_index.md`
- `09_student_draft/phase12_reasoning_typology_index.md`
- `09_student_draft/phase12_sort_key_matrix.csv`
- `05_coverage/phase12_362_control_base_rescan_summary.md`
- `08_review/phase12_quantity_and_coverage_gate.md`
- `08_review/phase12_choice_option_visibility_audit.md`
- `08_review/phase12_choice_full_option_repair_log.md`
- `08_review/phase12_preclean_metadata_cleanup_report.md`
- `08_review/phase12_preclean_metadata_cleanup_actions.csv`
- `08_review/phase12_final_clean_build_readiness_audit.md`
- `08_review/phase12_final_clean_build_readiness_matrix.csv`
- `08_review/phase12_codexA_local_review_gate.md`
- `governor_confucius/phase12_governor_gate.md`
- `governor_confucius/phase12_confucius_learning_gate.md`
- `08_review/gpt_phase_advice/phase_12_77body_prompt_for_gpt55_USER_SUBMIT.md`
- `08_review/claudecode_phase12_visible_77body_audit_prompt.md`
- `08_review/opus_writer/phase_12_77body_prompt_for_claude_opus47_adaptive.md`
