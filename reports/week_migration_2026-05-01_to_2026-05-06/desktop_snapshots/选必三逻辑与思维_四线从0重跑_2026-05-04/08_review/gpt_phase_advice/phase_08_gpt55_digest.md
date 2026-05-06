# Phase 08 GPT-5.5 Pro Digest

- status: complete
- channel: ChatGPT web, visible Pro conversation `高考政治四线工作流`
- prompt_file: `08_review/gpt_phase_advice/phase_08_prompt_for_gpt55.md`
- raw_reply_capture: `08_review/gpt_phase_advice/phase_08_gpt55_raw.md`
- full_page_copy: `08_review/gpt_phase_advice/safari_page_copy_phase08.txt`
- verdict: `GO_TO_PHASE09_STUDENT_DRAFT_CONSTRUCTION_NO_WORD_NO_FINAL`

## Accepted Gate

GPT 认可 Phase08 在 Lane B warning patch 之后通过 review-only prototype gate，可以进入 Phase09 受控学生稿构建阶段。

Phase09 的输入边界必须保持很窄：只允许把 Phase08 已通过的 29 行 prototype 转成受控学生稿草案；不得扩展到 74 行全量证据池；不得纳入 45 个 hold rows；不得纳入 288 个 L0 rows。

## Must-Fix Before Phase09 First Draft Freeze

- `Q-2025丰台期末-7`：不能放入思维主链正文；必须作为 `boundary_trap` 或易错辨析，不得作为选必三思维方法正例。
- `Q-2025顺义一模-7`：正确选项与原因表达存在高风险，Phase09 前必须回 Phase08 freeze 与原答案依据核验；未核验前不得定稿化。
- `Q-2026顺义一模-19-2`：主讲位置放在科学思维；推理侧只能作题目框架或共采分辅助，不得写成典型三段论题。
- `Q-2024朝阳二模-19-1`、`Q-2024朝阳二模-19-2`：不得回流细则编号、文件编号、填空编号等审稿味表达。
- `Q-2024朝阳一模-20-1`、`Q-2024朝阳一模-20-2`、`Q-2026通州期末-19-2`：假言推理必须区分充分条件与必要条件有效式，不能混用口诀。
- `Q-2026丰台一模-18-2`：必须保留 L4 已锁动作链：甲为必要条件假言推理肯定后件式且前提真实，乙为三段论大项不当扩大。
- `Q-2025海淀二模-20`：必须保持角度池写法，不得写成三点全必答或 `3 点乘 2 分`。
- `Q-2024西城一模-11`、`Q-2025海淀二模-12`、`Q-2025海淀二模-13`、`Q-2026顺义一模-3`：不得作为 Phase09 正文题条目进入；只能按授权作为 hard-excluded 或同类题 ID 引用。

## Allowed Phase09 Outputs

- `09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md`
- `09_student_draft/phase09_student_draft_control_matrix.csv`
- `09_student_draft/phase09_question_id_backcheck.csv`
- `09_student_draft/phase09_opus_or_codex_change_log.csv`
- `09_student_draft/phase09_internal_terms_scan.md`
- `09_student_draft/phase09_QID_risk_register.md`
- `08_review/phase09_codexA_student_draft_verification.md`
- `claudecode_lane/opus47_phase09_student_draft_audit/phase09_laneB_student_draft_audit.md`
- `08_review/phase09_Governor_student_draft_boundary_gate.md`
- `08_review/phase09_Confucius_learning_value_gate.md`
- `08_review/phase09_GPT_commander_review_packet.md`

## Still Blocked

Word、PDF、final PASS、终稿、最终稿、宝典成品、74 行全量证据池直接写成学生稿、45 个 hold rows 入稿、288 个 L0 rows 入稿、hard-excluded rows 展开成正文、同类题 ID 自动扩成答案讲解、把 L3_candidate 写成完全锁定。

## Phase09 Hard Rules

- Phase09 只写 29 行受控学生稿草案，必须逐条保留 `question_id` 到内部对照表。
- 思维部分按 `材料信号 -> 可写思维/方法 -> 为什么能想到 -> 答题动作 -> 答案落点 -> 易错陷阱 -> 同类题` 转写。
- 推理部分按 `题型 -> 逻辑形式 -> 规则口诀 -> 有效式或错误式 -> 解题动作 -> 答案落点 -> 易错陷阱 -> 同类题` 转写。
- 交叉题保留主挂载与次挂载，不得单挂。
- 选择题必须显式写正确选项字母和组合，例如 `选 C，②③`。
- 主观题必须写考场可执行动作，每条至少有一条能直接搬到答题纸上的表达。
- 学生稿正文禁止内部词：`Phase07`、`Phase08`、`packet`、`source locator`、`lane`、`Governor`、`Confucius`、`L3`、`L4`、`B-choice-signal`、`LOCKED_FOR_FUSION`、文件路径、细则编号式残留。
- `Q-2024西城一模-11` 错配硬锁继续生效，任何 Phase09 文件若写成 `B=①④` 必须回滚。
- `Q-2025海淀二模-12`、`Q-2025海淀二模-13` 不得进入 Phase09 正文；如作同类题 ID 引用，只能保留 ID，不得写答案 D/C 或展开讲解。
- `Q-2026顺义一模-3` 不得进入推理正文；若作为思维同类题引用，只能在思维侧出现。
- Phase09 完成后必须先过 Codex A verification，再过 ClaudeCode Lane B audit，再过 Governor/Confucius，再提交 GPT review；在这些 gate 之前仍禁止 Word/PDF 和 final PASS。
