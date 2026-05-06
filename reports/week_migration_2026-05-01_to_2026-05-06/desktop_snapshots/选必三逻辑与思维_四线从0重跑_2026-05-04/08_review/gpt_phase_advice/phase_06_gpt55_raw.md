# verdict

```text
GO_TO_PHASE07_LOCKED_OPUS_INPUT_PACKET_PREP_NO_STUDENT_DRAFT
```

Phase06 可以通过，允许进入 Phase07 准备 `locked_opus_input_packet`。
继续禁止学生稿、Claude Opus 教学成文化正文、Word/PDF、final PASS。

依据：Phase06 evidence lock register 为 74 行，L4=4、L3=70；thinking fusion 为 36 行，reasoning fusion 为 51 行，cross mount lock 为 13 行，L0 retention register 为 288 行；Codex A 本地审计 16 项 0 failure；ClaudeCode Lane B Opus 4.7 max 审计为 `PASS_PHASE06_WITH_WARNINGS`，38 项中 30 PASS、8 WARN、0 FAIL、0 BLOCK；Lane B 明确确认 74 行、36 行、51 行、13 个双挂载、Q11、Q12/Q13、288 个 L0 排除、以及当前仍禁止学生稿/Opus prose/Word/PDF/final PASS。

---

# 1. patched Phase06 是否可接受

可以接受为：

```text
evidence-lock / framework-fusion acceptable
```

但只能接受到 Phase07 input-packet preparation，不接受为 student draft readiness。

理由：

```text
1. 74 行 evidence lock register 数量闭合。
2. L3/L4 分级仍保留。
3. 36 行 thinking fusion 与 51 行 reasoning fusion 均已建立。
4. 13 个交叉题双挂载已确认。
5. 288 个 L0 行被保留且排除出 Opus input。
6. Q-2024西城一模-11 保持 B=①③，无旧错配污染。
7. Q-2025海淀二模-12/13 保留答案与 locator。
8. Codex A 与 ClaudeCode B 均无 blocker。
```

Lane B warnings 被 Codex A patch 后，post-patch checks 显示：

```text
thinking placeholders = 0
reasoning single-letter rule_slogan = 0
reasoning duplicated answer_action = 0
letter-only evidence answer_locator = 0
Q-2026顺义一模-3 在 Phase06 reasoning index/fusion 中出现次数 = 0
Q-2024西城一模-11 retired wrong-pairing string 出现次数 = 0
Codex A audit 仍为 PASS_LOCAL_PHASE06_STRUCTURE_AUDIT
```

这些足以支持进入 Phase07。

---

# 2. Lane B warnings 是否还需要再审

不需要在进入 Phase07 前做完整 Lane B 重审。
但需要做一个窄范围 patch acknowledgment，作为 Phase07 的 P0 审计附件。

必须产出：

```text
claudecode_lane/opus47_phase07_locked_packet_audit/phase06_warning_patch_ack.csv
claudecode_lane/opus47_phase07_locked_packet_audit/phase06_warning_patch_ack.md
```

只复核 8 个 patch 点：

```text
F01 Q-2026朝阳期中-13 answer_action 已从 D 改为动作链。
F02 Q-2026丰台一模-4 method 已细化为 分析与综合；综合思维。
F03 Q-2026朝阳期中-11 rule_slogan 已改为三段论补大前提规则。
F04 Q-2026朝阳期中-13 rule_slogan 已改为类比/联想/感性具体边界。
F05 duplicate/generic answer_action 已清零。
F06 letter-only answer_locators 已清零。
F07 L0 group summary 已含 8 类，零计数类别显式保留。
F08 Phase05 patch freeze 已由 Lane B Phase06 audit 承认。
```

这不是阻断 Phase07 启动的条件，但阻断任何 Opus prototype 消费输入包。

---

# 3. 是否允许准备 locked_opus_input_packet

允许。

但 Phase07 的任务只能是准备输入包，不是让 Opus 写教学文本。
阶段名建议固定为：

```text
Phase07 locked Opus input packet preparation
```

Phase07 允许做：

```text
1. 从 74 行 evidence lock register 中筛选可进入 Opus 输入包的行。
2. 为每行生成 locked entry。
3. 保留 question_id、题型、答案、材料信号、logical_form、answer_action 等字段。
4. 建立 L3_hold 与 L4_ready 分区。
5. 排除 L0。
6. 排除缺关键字段的 L3。
7. 生成 Opus 禁止动作清单。
8. 生成 machine-checkable backcheck。
9. 交给 GPT/Governor/Confucius 再审。
```

Phase07 禁止做：

```text
1. 不得让 Opus 改写正文。
2. 不得生成学生稿。
3. 不得写章节导语。
4. 不得写宝典成品。
5. 不得生成 Word/PDF。
6. 不得 final PASS。
```

---

# 4. Phase07 必须产出的文件

## P0. 锁定输入包总表

```text
05_coverage/phase07_locked_opus_input_packet.csv
05_coverage/phase07_locked_opus_input_packet.md
```

每行必须包含：

```text
question_id
suite_id
module: 思维 / 推理 / 交叉
status: L4 / L3
input_permission: include / hold / exclude
source_locator
answer_locator
rubric_or_commentary_locator
visual_locator
question_type
full_stem_status
full_options_status
student_permission = no
opus_permission = packet_only
risk_note
```

硬规则：

```text
1. L4 可以 include。
2. L3 只有关键字段全齐才可以 include_as_L3_packet_candidate。
3. 缺关键字段的 L3 必须 hold。
4. L0 必须 exclude。
5. 所有行 student_permission 继续为 no。
```

## P0. 思维输入包

```text
05_coverage/phase07_opus_input_thinking_entries.csv
05_coverage/phase07_opus_input_thinking_entries.md
```

每个 thinking entry 必须包含：

```text
question_id
材料信号
可写思维/方法
答题动作
答案落点
来源例题
同类题
易错陷阱
L3_or_L4_status
allowed_opus_task
forbidden_opus_changes
```

缺以下任一字段的 L3，不得进入 Opus 输入包：

```text
材料信号
可写思维/方法
答题动作
答案落点
来源例题
```

## P0. 推理输入包

```text
05_coverage/phase07_opus_input_reasoning_entries.csv
05_coverage/phase07_opus_input_reasoning_entries.md
```

每个 reasoning entry 必须包含：

```text
question_id
primary_reasoning_type
secondary_reasoning_type
logical_form
rule_slogan
valid_or_invalid_pattern
common_trap
answer_action
same_type_question_ids
L3_or_L4_status
allowed_opus_task
forbidden_opus_changes
```

缺以下任一字段的 L3，不得进入 Opus 输入包：

```text
logical_form
rule_slogan
valid_or_invalid_pattern
common_trap
answer_action
same_type_question_ids
```

## P0. 交叉题输入锁

```text
05_coverage/phase07_opus_input_cross_entries.csv
05_coverage/phase07_cross_mount_opus_policy.md
```

13 个交叉题必须逐行说明：

```text
question_id
thinking_entry_id
reasoning_entry_id
primary_mount
secondary_mount
whether_opus_should_duplicate_explanation
whether_opus_should_cross_reference
forbidden_single_mount = yes
```

Opus 未来可以减少重复表达，但不能删除任一挂载。

## P0. L3 hold list

```text
05_coverage/phase07_L3_hold_list.csv
05_coverage/phase07_L3_promote_or_hold_decision.md
```

必须将 70 个 L3 全部判为：

```text
include_as_packet_candidate
hold_missing_fields
hold_answer_locator_risk
hold_visual_risk
hold_scope_risk
hold_reasoning_form_risk
hold_thinking_signal_risk
```

这一步是 Phase07 的核心。不能把 70 个 L3 一次性全部喂给 Opus。

## P0. L0 exclusion list

```text
05_coverage/phase07_L0_excluded_from_opus_input.csv
05_coverage/phase07_L0_exclusion_summary.md
```

288 个 L0 必须全部出现，并保留原因：

```text
out_of_scope
boundary_closed
duplicate_removed
support_reference_row
answer_missing
visual_missing
scope_rejected
source_or_locator_issue
```

## P0. hard-lock audit

```text
06_conflicts/phase07_hard_lock_audit.md
06_conflicts/phase07_hard_lock_audit.csv
```

必须检查：

```text
Q-2024西城一模-11 = B=①③
Q-2024西城一模-11 不出现 B=①④
Q-2025海淀二模-12 = D + render_008_page_04 + supplemental answer table page 9
Q-2025海淀二模-13 = C + render_008_page_04 + supplemental answer table page 9
Q-2026顺义一模-3 不进入 reasoning input
13 个 cross rows 双挂载
288 个 L0 不进入 input
student_permission 全部 no
```

## P1. Opus boundary rules final

现有文件可以升级为：

```text
05_coverage/phase07_opus_input_boundary_rules_FINAL_FOR_PACKET.md
```

必须写明 Opus 禁止事项：

```text
1. 不得新增题。
2. 不得删题。
3. 不得改答案。
4. 不得改题型。
5. 不得改 L3/L4 状态。
6. 不得把 L3 写成 L4。
7. 不得把交叉题单挂。
8. 不得补写无 locator 的答案。
9. 不得引入旧稿结论。
10. 不得输出学生稿。
11. 不得生成 Word/PDF。
12. 不得出现 source locator、lane、Governor、Confucius 等内部词进入未来学生文本。
```

## P1. Governor / Confucius / GPT Phase07 gates

```text
05_coverage/phase07_Governor_locked_packet_gate.md
05_coverage/phase07_Confucius_locked_packet_value_gate.md
05_coverage/phase07_GPT_commander_review_packet.md
```

Governor 检查：

```text
packet 行数
include / hold / exclude 数量
L3/L4 分级
L0 排除
hard locks
cross 双挂载
student_permission=no
Opus 权限=packet_only
```

Confucius 检查：

```text
思维条目是否可形成材料触发链
推理条目是否可形成解题动作链
同类题是否可迁移
是否存在空泛题型总结风险
是否存在只给答案字母风险
是否存在没有考场动作的题
```

GPT packet 必须申请下一步是否允许：

```text
Opus teaching-text prototype from locked packet
```

不能申请 final student稿。

---

# 5. 哪些 L3 必须排除出 Opus input

原则：L3 不因 L3 身份自动排除，但 L3 需要逐行过字段门槛。以下 L3 必须排除或 hold，不得进入 Opus input。

## 5.1 缺 source 或 answer locator 的 L3

排除：

```text
source_locator missing
answer_locator missing
visual_locator required but missing
rubric/commentary required but missing
```

## 5.2 选择题证据仍停留在 B-choice-signal 的 L3

如果只有：

```text
answer = A/B/C/D
```

但没有：

```text
完整题干
完整选项
answer_locator
source_locator
```

必须 hold。

B-choice-signal 可以保留为 evidence archive 状态，不能直接成为 Opus 输入许可。

## 5.3 推理字段不完整的 L3

hold：

```text
logical_form 缺失
rule_slogan 缺失
valid_or_invalid_pattern 缺失
trap 缺失
answer_action 缺失
same_type_question_ids 缺失
```

特别是 rule_slogan 不能只写答案字母，answer_action 不能是“选 X”。

## 5.4 思维字段不完整的 L3

hold：

```text
材料信号 缺失
可写思维/方法 缺失
答题动作 缺失
答案落点 缺失
来源例题 缺失
```

特别是 method 不能写“待细化”，answer_action 不能是泛句。

## 5.5 交叉挂载不完整的 L3

hold：

```text
thinking_component 缺失
reasoning_component 缺失
primary_mount 缺失
secondary_mount 缺失
cross_reference policy 缺失
```

## 5.6 hard-lock 风险行

以下行若任何字段缺失或污染，必须 hold：

```text
Q-2024西城一模-11
Q-2025海淀二模-12
Q-2025海淀二模-13
Q-2026顺义一模-3
```

Q11 任何地方出现 `B=①④` 作为 Q11 正确配对，整包回滚。

---

# 6. 下一阶段分工

## Codex A

Codex A 执行 Phase07 主控：

```text
1. 生成 locked_opus_input_packet。
2. 生成 thinking / reasoning / cross 三类 input entries。
3. 生成 L3 hold list。
4. 生成 L0 exclusion list。
5. 生成 hard-lock audit。
6. 生成 Opus boundary rules FINAL。
7. 生成 Governor / Confucius / GPT Phase07 gates。
```

Codex A 不得写学生稿。

## ClaudeCode B

ClaudeCode B 做 Phase07 input-packet 独立审计：

```text
1. 审计 packet 是否只含 include 行。
2. 审计所有 include 行是否字段齐全。
3. 审计 L3 hold 是否合理。
4. 审计 L0 是否全部排除。
5. 审计 Q11、Q12、Q13、Q-2026顺义一模-3。
6. 审计 13 个 cross rows。
7. 审计 Opus boundary rules 是否足够硬。
8. 输出 phase07_laneB_locked_packet_audit.csv/md。
```

ClaudeCode B 不得写教学文本。

## Claude Opus

当前仍然：

```text
NO_TEACHING_TEXT_ACTION
```

可以在 Phase07 结束后，若 GPT/Governor/Confucius 全部通过，才讨论：

```text
Claude Opus teaching-text prototype from locked packet
```

不是最终稿。

---

# still forbidden

继续禁止：

```text
学生稿
Claude Opus 教学正文
Word/PDF
final PASS
终稿说法
宝典成品说法
L3 当 L4
B-choice-signal 直接入稿
L0 删除
交叉题单挂
Q11 错配回流
Q12/Q13 locator 丢失
```

---

# final line

```text
GO_TO_PHASE07_LOCKED_OPUS_INPUT_PACKET_PREP_NO_STUDENT_DRAFT
```
