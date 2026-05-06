# GPT-5.5 Pro Phase07 Commander Review Prompt

你是本轮“飞哥政治庄园”四线工作流里的 GPT-5.5 Pro 阶段总指挥/内容风险审稿人。

请审查 Phase07：选必三《逻辑与思维》从0重跑的“locked Opus input packet 准备阶段”。本阶段不是学生稿，不是终稿，不是 Word/PDF。请只判断下一阶段是否可以进入 Claude Opus 4.7 教学文本 prototype，或者是否还需要补 Phase07 包。

## 当前运行背景

- 工作目录：`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`
- 范围：选必三《逻辑与思维》分两部分处理：
  - 思维部分：完全模仿此前“哲学宝典”的触发链工作流；每个思维/方法相当于哲学原理方法论，要穷尽题目并能转化为学生可迁移的触发链。
  - 推理部分：按题型分类（如三段论、假言推理、选言/联言、归纳/类比等），所有题归入对应题型下。
- 当前硬禁令：不得写学生稿、不得让 Opus 写教学正文、不得生成 Word/PDF、不得 final PASS、不得说终稿/宝典成品。
- GPT 和 Claude/Opus 只能做指挥/审稿/成文化建议，不是证据来源；任何新内容后续都必须回本地证据验证。

## Phase06 进入 Phase07 的依据

- GPT Phase06 verdict：`GO_TO_PHASE07_LOCKED_OPUS_INPUT_PACKET_PREP_NO_STUDENT_DRAFT`
- Phase06 patched 后可作为 evidence-lock/framework-fusion 内部底座。
- Phase07 任务：准备 locked Opus input packet；把 74 条证据行分成 include/hold；L3 不能一股脑喂 Opus；L0 必须全部排除；cross rows 必须双挂；生成边界规则和审计文件。

## Phase07 生成结果

核心输出：

- `05_coverage/phase07_locked_opus_input_packet.csv/md`
- `05_coverage/phase07_opus_input_thinking_entries.csv/md`
- `05_coverage/phase07_opus_input_reasoning_entries.csv/md`
- `05_coverage/phase07_opus_input_cross_entries.csv`
- `05_coverage/phase07_cross_mount_opus_policy.md`
- `05_coverage/phase07_L3_hold_list.csv`
- `05_coverage/phase07_L3_promote_or_hold_decision.md`
- `05_coverage/phase07_L0_excluded_from_opus_input.csv`
- `05_coverage/phase07_L0_exclusion_summary.md`
- `06_conflicts/phase07_hard_lock_audit.csv/md`
- `05_coverage/phase07_opus_input_boundary_rules_FINAL_FOR_PACKET.md`
- `05_coverage/phase07_Governor_locked_packet_gate.md`
- `05_coverage/phase07_Confucius_locked_packet_value_gate.md`
- `05_coverage/phase07_GPT_commander_review_packet.md`

计数：

- packet rows: 74
- packet permission counts: `include=4`, `include_as_packet_candidate=25`, `hold_answer_locator_risk=25`, `hold_reasoning_form_risk=20`
- L3 rows: 70；其中 25 include candidate，45 hold
- L0 rows: 288；全部 `exclude`
- thinking input rows: 18
- reasoning input rows: 16
- cross policy rows: 13

硬锁：

- Q-2024西城一模-11：保留正确 `B=①③`；退休旧错配 `B=①④` 不得作为正确 pairing 出现。
- Q-2025海淀二模-12：答案 D；render_008_page_04；补充答案表 page 9。
- Q-2025海淀二模-13：答案 C；render_008_page_04；补充答案表 page 9。
- Q-2026顺义一模-3：不得进入 reasoning input；当前仅作为 thinking hold / same-method 参考，未进入 reasoning input。
- 13 个 cross rows 保持双挂；禁止 single-mount。
- Opus permission 全部 `packet_only`，student permission 全部 `no`。

## Codex A 本地审计

- `codex_lane/phase07_local_audit/phase07_codexA_local_audit.md`
- verdict: `PASS_LOCAL_PHASE07_PACKET_AUDIT`
- checks: 11
- failures: 0
- 新增 C04：Phase07 Lane B P3 placeholder classes repaired。

本地 hard-lock audit：

- `06_conflicts/phase07_hard_lock_audit.md`
- verdict: `PASS_HARD_LOCK_AUDIT`

## ClaudeCode Lane B Phase07 审计

真实 ClaudeCode / Opus 4.7 max 审计，不是模拟：

- prompt: `08_review/claudecode_phase07_locked_packet_audit_opus47_max_prompt.md`
- debug: `logs/opus47_max/claudecode-opus47max-phase07-locked-packet-audit-debug.log`
- debug confirmed: `model=claude-opus-4-7`, `effectiveWindow=980000`
- stdout: 25 lines
- stderr: 0
- outputs under `claudecode_lane/opus47_phase07_locked_packet_audit/`

Lane B required files all produced:

- `phase06_warning_patch_ack.csv`
- `phase06_warning_patch_ack.md`
- `phase07_laneB_locked_packet_audit.csv`
- `phase07_laneB_locked_packet_audit.md`
- `phase07_laneB_locked_packet_audit_findings.csv`
- `phase07_laneB_locked_packet_audit_blockers.md`
- `progress.md`

Lane B results:

- Phase06 warning patch ack: 8/8 `PATCH_VERIFIED`
- Phase07 verdict before Codex P3 patch: `PASS_PHASE07_WITH_WARNINGS`
- 16 audit lines: 14 PASS / 2 WARN / 0 FAIL / 0 BLOCK
- blocker file: `NO_PHASE07_BLOCKERS_DETECTED`

Lane B P0 checks all passed:

- packet row count = 74
- permission distribution exact
- all student_permission = `no`
- all opus_permission = `packet_only`
- L3 hold list contains all 70 L3 rows; not blindly included
- all 288 L0 excluded; zero L0 leak
- thinking/reasoning inputs restricted to include rows and carry critical fields
- Q-2026顺义一模-3 absent from reasoning input
- Q11/Q12/Q13 hard locks pass
- 13 cross rows; all `forbidden_single_mount=yes`
- boundary rules forbid Opus from adding/deleting/changing answers/status/single-mounting/generating student稿/Word/PDF
- Governor/Confucius/GPT gates do not authorize student稿 or Opus prose

Lane B P3 warnings before patch:

- W01：`Q-2026丰台一模-18-2` L4 reasoning `answer_action` was placeholder `answer_confirmed_PASS_TO_FUSION` instead of action-chain sentence.
- W02：10 thinking entries had `同类题=NO_SAME_METHOD_IN_PHASE06_INDEX` placeholder instead of real same-method IDs.

## Codex A Patch After Lane B P3

Patch file:

- `06_conflicts/phase07_laneB_warning_patch_resolution.md`

Patch was made in generator, not only one-off CSV:

- `02_extraction/phase07_build_locked_opus_packet.py`

Patch details:

- W01 fixed：`Q-2026丰台一模-18-2` Phase07 reasoning `answer_action` now says：先识别甲为必要条件假言推理的肯定后件式，并结合前提真实判定甲推理正确；再识别乙为三段论大项在前提中不周延却在结论中周延，属于大项不当扩大，判定乙推理错误。
- W01 extra cleanup：同题 packet `answer_locator` changed from `answer_confirmed_PASS_TO_FUSION` to `answer_confirmed_甲正确乙错误_from_043_slide35_36_rubric`。
- W02 fixed：Phase07 thinking input auto-populates missing `同类题` by `framework_node` across locked Phase06 thinking pool; added `risk_note` to document whether same-method chain came from Phase06 index or auto framework-node matching.

Post-patch checks:

- packet rows still 74
- permission counts still `4/25/25/20`
- thinking input rows still 18
- reasoning input rows still 16
- cross rows still 13
- L3 rows still 70
- L0 rows still 288
- `NO_SAME_METHOD_IN_PHASE06_INDEX` in Phase07 thinking input: 0
- `answer_confirmed_PASS_TO_FUSION` in Phase07 reasoning `answer_action`: 0
- `answer_confirmed_PASS_TO_FUSION` in Phase07 packet `answer_locator`: 0
- local audit remains `PASS_LOCAL_PHASE07_PACKET_AUDIT`
- hard-lock audit remains `PASS_HARD_LOCK_AUDIT`

## 请你给出阶段裁决

请返回一个明确 verdict，最好使用下面四选一之一：

1. `GO_TO_PHASE08_OPUS_TEACHING_PROTOTYPE_NO_FINAL`
2. `PATCH_PHASE07_BEFORE_OPUS_PROTOTYPE`
3. `HOLD_FOR_SOURCE_REPAIR`
4. `REQUEST_MORE_PACKET_INFO`

同时请给：

- 你是否认可 Phase07 已足够进入下一步 Opus 教学文本 prototype。
- 如果进入 Phase08，Opus prototype 的边界应该是什么：能写什么、不能写什么。
- GPT 认为下一阶段必须检查的 5-10 个风险点。
- 是否需要再次让 ClaudeCode Lane B 复核 P3 patch，还是可把补丁记录带入 Phase08 后由 Governor/Confucius/GPT 继续压测。
- 绝对不要授权 final student稿、Word/PDF、final PASS；最多只能授权“Opus prototype draft for review”。
