# ClaudeCode Visible Audit Prompt: Phase12 Post-MUST_FIX Patch

你现在审的是选必三《逻辑与思维》Phase12 77 条 post-MUST_FIX review-only 稿。

必须在真实可见 ClaudeCode 窗口工作，不得使用旧 29-row Word，不得生成 Word/PDF/final，不得把本稿称为终稿。

## 背景

- 工作目录：`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`
- 29 条候选稿已被用户否决为题量过少，只能叫 controlled packet。
- 已扩到 77 条：主观题 27，选择题 50。
- GPT 外审 verdict=`MUST_FIX_CONTENT` 已由 Codex 本地补丁。
- 现在你只做可见窗口审稿，不要越权生成终稿。

## 必读文件

1. `08_review/phase12_external_patch_resolution.md`
2. `08_review/phase12_q2024_haidian_ermo_17_1_source_recheck.md`
3. `08_review/phase12_post_patch_addendum_Q2025_shunyi_yimo_7.md`
4. `09_student_draft/phase12_expanded_body_FROM_362_REVIEW_ONLY.md`
5. `09_student_draft/phase12_expanded_body_FROM_362_control_matrix.csv`
6. `09_student_draft/phase12_reasoning_typology_index_REBUILT.md`
7. `09_student_draft/phase12_thinking_method_index_REBUILT.md`
8. `08_review/phase12_post_patch_index_audit.md`
9. `08_review/phase12_post_patch_quantity_and_coverage_gate.md`
10. `05_coverage/phase12_locked_index_mounts.csv`

## 强制审查点

1. `2024 海淀二模17(1)` 是否确实按 `SCIENCE_ONLY_SOURCE_SUPPORTED` 写，未回流三模块并列设问。
2. 推理索引是否已清除充分条件/必要条件交叉污染。
3. 思维索引是否已清除边界陷阱正例化。
4. `2024 朝阳二模7` 是否锁定小项扩大，不得写成中项不周延。
5. `2025 顺义一模7` 是否锁定真实错误为大项不当扩大，`小项不当扩大` 只能作为 A 项误称陷阱。
6. 77 条正文是否仍有内容性漏答、答案不充分、推理形式不清、题型归类错误。
7. 选择题是否保留完整选项、正确项理由、错项陷阱。
8. 哪些 `NEEDS_*` 辅助挂载必须在 final clean build 前转成学生可读的非正例标签。

## 输出目录

写入：`claudecode_lane/phase12_visible_post_mustfix_patch_audit/`

至少生成：

- `phase12_visible_post_mustfix_status.md`
- `phase12_visible_post_mustfix_audit_matrix.csv`
- `phase12_visible_post_mustfix_audit_report.md`
- `phase12_visible_post_mustfix_patch_queue.csv`

## 输出 verdict

只能从以下选择：

- `VISIBLE_AUDIT_PASS_NO_FINAL`
- `MUST_FIX_CONTENT_AGAIN`
- `HOLD_SOURCE_REPAIR`
- `HOLD_INDEX_REPAIR`

无论 verdict 是什么，都不要授权 Word/PDF/final。
