# GPT Pro V65 Upload Manifest

Status: `READY_FOR_USER_VISIBLE_GPTPRO_SUBMISSION`

## Clean Prompt Notice

The original paste prompt below may display with encoding damage in some viewers. Use the clean prompt instead:

- `05_gptpro_review/GPTPRO_V65_COPY_PASTE_PROMPT_CLEAN.md`

Result save instructions:

- `05_gptpro_review/GPTPRO_V65_RESULT_DROP_INSTRUCTIONS.md`

Both files are also included in the refreshed upload zip.

## V75 Upload Refresh

This upload set has been refreshed after the V73/V74 gate hardening. The zip now includes the current GPT Pro intake runbook, closure runbook, Claude V63 gate runbook, and current blocker/delivery status. This refresh does not mean GPT Pro review has happened.

Current zip: `05_gptpro_review/GPTPRO_V65_UPLOAD_SET.zip`

V77 one-screen user handoff: `05_gptpro_review/GPTPRO_V65_USER_HANDOFF_V77.md`

V78 post-GPT resume gate: `07_governor_confucius/POST_GPTPRO_RESUME_CHECK_V78.md`, `07_governor_confucius/resume_after_gptpro_v65.ps1`, and `07_governor_confucius/test_post_gptpro_resume_v78.ps1`

V80 traceability context: `07_governor_confucius/STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv`, `07_governor_confucius/STUDENT_ARTIFACT_TRACEABILITY_SUMMARY_V79.md`, and `07_governor_confucius/STUDENT_ARTIFACT_TRACEABILITY_ALIASES_V80.csv`

V81 local pre-submit audit: `05_gptpro_review/GPTPRO_V65_UPLOAD_PACKAGE_AUDIT_V81.md`

V82 result-drop guard: `05_gptpro_review/run_gptpro_v65_intake_check.ps1` and `05_gptpro_review/test_gptpro_v65_intake_placeholder_v82.ps1`

V83 GPT Pro triage quality gate: `05_gptpro_review/validate_gptpro_v65_triage_v83.ps1`, `05_gptpro_review/test_gptpro_v65_triage_quality_v83.ps1`, and `05_gptpro_review/GPTPRO_V65_TRIAGE_READY_CHECK_V83.md`

V84 Claude triage quality gate: `06_claude_review/validate_claude_v63_triage_v84.ps1`, `06_claude_review/test_claude_v63_triage_quality_v84.ps1`, and `06_claude_review/CLAUDE_V63_TRIAGE_READY_CHECK_V84.md`

V85 Chrome channel recheck: `05_gptpro_review/GPTPRO_V65_CHROME_EXTENSION_RECHECK_V85.md`

V86 coverage-gap audit: `01_source_inventory/COVERAGE_GAP_AUDIT_V86.md`

V87 suite-coverage audit: `01_source_inventory/SUITE_COVERAGE_AUDIT_V87.md`

V88 reasoning-body traceability delta: `07_governor_confucius/STUDENT_ARTIFACT_TRACEABILITY_DELTA_V88.md`

V81 audit tools: `05_gptpro_review/audit_gptpro_v65_upload_package_v81.ps1` and `05_gptpro_review/test_gptpro_v65_upload_package_audit_v81.ps1`

The upload-package audit now checks `blocker_v84_gate_check` so `B2026ERMO-016` must include the V84 Claude triage gate before the package is treated as synchronized.
It also checks `chrome_v85_recheck_check` so the latest browser-channel evidence is present before submission.
`blocker_v85_channel_check` verifies that `B2026ERMO-016` also names this V85 channel evidence.
`coverage_v86_audit_check` verifies that the latest coverage-gap audit is included in the package.
`suite_v87_audit_check` verifies that the latest suite-coverage audit is included in the package and records the 143-row matrix state.
`audit_tool_check` verifies that the audit script and its test are included in the package.

Use this file when the browser/profile/login blocker is fixed. Do not paste passwords, email addresses, or account identifiers into the review chat.

## Current Review Packet

- `10_packets/GPTPRO_REVIEW_PACKET_V65.md`

## Minimum Files To Upload Or Paste

Upload these first. They are the current student-facing review bases and gate files:

1. `10_packets/GPTPRO_REVIEW_PACKET_V65.md`
2. `08_delivery/选必三_逻辑与思维_思维宝典_框架重排送审版.md`
3. `08_delivery/选必三_逻辑与思维_推理宝典_题型重排送审版.md`
4. `07_governor_confucius/STUDENT_REVIEW_DRAFT_GOVERNOR_PRE_GPT_V65.md`
5. `07_governor_confucius/STUDENT_REVIEW_DRAFT_CONFUCIUS_PRE_GPT_V65.md`
6. `07_governor_confucius/OBJECTIVE_COMPLETION_AUDIT_PRE_EXTERNAL_V66.md`
7. `07_governor_confucius/EXTERNAL_REVIEW_CLOSURE_RUNBOOK_V74.md`
8. `05_gptpro_review/GPTPRO_V65_INTAKE_RUNBOOK.md`
9. `05_gptpro_review/GPTPRO_V65_RESULT_DROP_INSTRUCTIONS.md`
10. `07_governor_confucius/POST_GPTPRO_RESUME_CHECK_V78.md`
11. `07_governor_confucius/STUDENT_ARTIFACT_TRACEABILITY_SUMMARY_V79.md`
12. `07_governor_confucius/STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv`
13. `07_governor_confucius/STUDENT_ARTIFACT_TRACEABILITY_ALIASES_V80.csv`
14. `01_source_inventory/COVERAGE_GAP_AUDIT_V86.md`
15. `01_source_inventory/SUITE_COVERAGE_AUDIT_V87.md`
16. `07_governor_confucius/STUDENT_ARTIFACT_TRACEABILITY_DELTA_V88.md`

If GPT Pro can accept more context, also upload:

V75 additional context:

- `05_gptpro_review/EXTERNAL_REVIEW_STATUS.md`
- `06_claude_review/EXTERNAL_REVIEW_STATUS.md`
- `06_claude_review/CLAUDE_V63_RUNBOOK.md`
- `07_governor_confucius/resume_after_gptpro_v65.ps1`
- `07_governor_confucius/test_post_gptpro_resume_v78.ps1`
- `07_governor_confucius/build_student_traceability_v79.ps1`
- `07_governor_confucius/test_student_traceability_v79.ps1`
- `07_governor_confucius/STUDENT_ARTIFACT_TRACEABILITY_ALIASES_V80.csv`
- `05_gptpro_review/run_gptpro_v65_intake_check.ps1`
- `05_gptpro_review/test_gptpro_v65_intake_placeholder_v82.ps1`
- `05_gptpro_review/validate_gptpro_v65_triage_v83.ps1`
- `05_gptpro_review/test_gptpro_v65_triage_quality_v83.ps1`
- `05_gptpro_review/GPTPRO_V65_TRIAGE_READY_CHECK_V83.md`
- `05_gptpro_review/audit_gptpro_v65_upload_package_v81.ps1`
- `05_gptpro_review/test_gptpro_v65_upload_package_audit_v81.ps1`
- `06_claude_review/run_claude_external_review_v63.ps1`
- `06_claude_review/test_claude_v63_gate.ps1`
- `06_claude_review/validate_claude_v63_triage_v84.ps1`
- `06_claude_review/test_claude_v63_triage_quality_v84.ps1`
- `06_claude_review/CLAUDE_V63_TRIAGE_READY_CHECK_V84.md`
- `05_gptpro_review/GPTPRO_V65_CHROME_EXTENSION_RECHECK_V85.md`
- `01_source_inventory/COVERAGE_GAP_AUDIT_V86.md`
- `01_source_inventory/SUITE_COVERAGE_AUDIT_V87.md`
- `07_governor_confucius/STUDENT_ARTIFACT_TRACEABILITY_DELTA_V88.md`

7. `03_claudecode_lane/suite_reports/2026二模_B线复跑.md`
8. `03_claudecode_lane/2026_ERMO_B_LINE_RERUN_RESULT.md`
9. `03_claudecode_lane/blockers_2026_ermo.csv`
10. `03_claudecode_lane/fusion_candidates_2026_ermo.csv`
11. `08_delivery/STUDENT_REVIEW_DRAFT_CLEANUP_NOTE.md`
12. `08_delivery/DELIVERY_STATUS.md`

## Paste Prompt

```text
你是本项目的真实 GPT Pro 内容总审。请严格审查我上传的 V65 外审包和双宝典送审稿。

任务背景：
- 这是北京高考政治选必三《逻辑与思维》双宝典项目。
- 思维宝典要按框架和材料触发链进入，质量对齐此前哲学必修四宝典的“材料信号 -> 方法触发 -> 卷面答案句”标准。
- 推理宝典要按同一推理形式归组，不按地区年份散排。
- 当前文件只是送审稿，不是终稿。

请重点审查：
1. 思维宝典框架重排稿是否真正保住“材料动作 -> 方法触发 -> 卷面答案句”，有没有概念表格化、空泛化或误挂。
2. 推理宝典题型重排稿是否真正把同一推理形式的题放到一起，是否有章节归类不安全的问题。
3. 是否还有学生可见的审核话术、内部编号、证据等级、状态字段、路径、模型痕迹或会误导学生的表达。
4. 2026 二模 B 线复跑和本地补丁是否足以进入 Claude 复审，尤其 Q0136、Q0137/Q0138、Q0139、Q0140 的边界是否仍安全。
5. 哪些问题必须在 Claude V63 前先回源修补。

请输出：
- Verdict：not_final / ready_for_claude_review_after_gptpro / reject
- P0 findings
- P1 findings
- 对思维宝典结构的判断
- 对推理宝典结构的判断
- 必须回源修补的清单
- 禁止声称的内容

不要给 final pass。不要把当前稿说成终稿。
```

## Save Result

After GPT Pro responds, save the result exactly here:

- `05_gptpro_review/GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md`

Then resume Codex so it can run Claude V63 and source-verified patching.
