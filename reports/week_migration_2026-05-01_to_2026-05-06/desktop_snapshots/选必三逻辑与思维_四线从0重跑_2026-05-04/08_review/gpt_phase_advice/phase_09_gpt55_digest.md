# Phase09 GPT-5.5 Pro Digest

- raw_reply: `08_review/gpt_phase_advice/phase_09_gpt55_raw.md`
- prompt_file: `08_review/gpt_phase_advice/phase_09_prompt_for_gpt55.md`
- sanitized_prompt_file: `08_review/gpt_phase_advice/phase_09_prompt_for_gpt55_SANITIZED.md`
- sent_at: 2026-05-05 02:10 CST
- captured_at: 2026-05-05 02:17 CST

## Verdict

`GO_TO_PHASE10_POLISH_OR_OUTLINE_NO_WORD_NO_FINAL`

GPT 允许 Phase09 受控学生稿进入 Phase10 polish/outline，但只允许结构梳理、表达打磨、标题体系、可读性优化、同类题索引样式统一、交叉题答案锚点补强。继续禁止 Word、PDF、final PASS、终稿、最终稿、宝典成品。

## Accepted Basis

- Phase09 仅从 29 个 Phase08 prototype rows 生成。
- draft/control rows 均为 29。
- 模块计数为思维 13、推理 11、交叉 5。
- 学生正文内部词命中 0。
- Q11 错配命中 0。
- hard-excluded expansion failures 0。
- Codex A 为 `PASS_CODEXA_PHASE09_CONTROLLED_DRAFT`。
- Lane B 为 `PASS_PHASE09_STUDENT_DRAFT_AUDIT_WITH_WARNINGS` 且无 blocker。
- Lane B warning patch 后为 `PASS_CODEXA_PHASE09_AFTER_LANEB_PATCH`。
- Governor 与 Confucius 为 pending-GPT pass。

## Must Fix Before Phase10 Freeze

- `Q-2025顺义一模-7`：必须保留“大项不当扩大；A 错在说成小项不当扩大”，不得回流 Phase08 旧表达；审计表继续保留 036 顺义参考答案来源线索。
- `Q-2025丰台期末-7`：继续放边界陷阱或易错辨析，不得进入超前思维正例组。
- `Q-2026顺义一模-19-2`：保持科学思维三特征为主讲，推理骨架只作辅助，不得写成典型三段论题。
- `Q-2024朝阳二模-19-1/19-2`：继续无细则编号、文件编号、来源页码、审稿术语；填空表达统一为第一空/第二空。
- `Q-2024朝阳一模-20-1`、`Q-2024朝阳一模-20-2`、`Q-2026通州期末-19-2`：充分条件与必要条件分开写，不得混成一个口诀。
- `Q-2026丰台一模-18-2`：保留甲必要条件假言推理肯定后件式正确、乙三段论大项不当扩大错误的完整链条。
- `Q-2025海淀二模-20`：继续保持辩证思维角度池；不能写成三点全必答或三点固定赋分模板。
- hard-excluded rows `Q-2024西城一模-11`、`Q-2025海淀二模-12`、`Q-2025海淀二模-13`、`Q-2026顺义一模-3` 只能 index-only 或 absent，不能展开答案、选项、题型结论；尤其 `Q-2024西城一模-11` 不得出现 `B=①④` 正确配对。

## Phase10 Allowed Outputs

- `09_student_draft/phase10_polished_outline_FROM_29.md`
- `09_student_draft/phase10_polish_control_matrix.csv`
- `09_student_draft/phase10_question_id_traceability_backcheck.csv`
- `09_student_draft/phase10_same_type_index_style_decision.md`
- `09_student_draft/phase10_cross_answer_anchor_patch.md`
- `09_student_draft/phase10_internal_terms_scan.md`
- `09_student_draft/phase10_QID_risk_register.md`
- `08_review/phase10_codexA_polish_verification.md`
- `claudecode_lane/opus47_phase10_polish_audit/phase10_laneB_polish_audit.md`
- `08_review/phase10_Governor_boundary_gate.md`
- `08_review/phase10_Confucius_learning_value_gate.md`
- `08_review/phase10_GPT_commander_review_packet.md`

## Phase10 Hard Rules

- Still only 29 rows; no expansion to 74 evidence rows, 45 hold rows, or 288 L0 rows.
- Thinking chain: `材料信号 -> 可写思维/方法 -> 为什么能想到 -> 答题动作 -> 答案落点 -> 易错陷阱 -> 同类题`。
- Reasoning chain: `题型 -> 逻辑形式 -> 规则口诀 -> 有效式或错误式 -> 解题动作 -> 答案落点 -> 易错陷阱 -> 同类题`。
- Cross entries must keep dual mounting in control matrix and avoid changing 主/辅 line.
- Same-type indexes remain index-only; same-type IDs must not expand into extra answer explanations.
- Choice answer format: `选 X，组合项。`
- Subjective entries must preserve at least one direct answer-sheet sentence.
- Decide traceability style: readable headings plus control matrix trace, or headings with compact QID.
- Student body must not contain internal terms: `Phase09`, `Phase10`, `packet`, `source locator`, `lane`, `Governor`, `Confucius`, `L3`, `L4`, `B-choice-signal`, `LOCKED_FOR_FUSION`, `文件路径`, `细则编号`。
- After Phase10: Codex A verification -> ClaudeCode Lane B audit -> Governor/Confucius -> GPT review. Word/PDF/final PASS remain blocked until later gates.
