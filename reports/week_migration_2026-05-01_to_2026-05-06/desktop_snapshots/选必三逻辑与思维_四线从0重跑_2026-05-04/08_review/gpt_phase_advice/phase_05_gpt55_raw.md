# verdict

```text
GO_TO_PHASE06_EVIDENCE_LOCK_AND_FRAMEWORK_FUSION_NO_STUDENT_DRAFT
```

Phase05 evidence archive 结构上可以通过。可以进入 Phase06，但 Phase06 只能做 evidence lock、框架融合、题型归档骨架加固、思维链骨架加固。继续禁止学生稿、Claude Opus 教学成文化、Word/PDF、final PASS。

我的裁决依据是：Phase05 已冻结 cleaned control base，362 行控制底座中 L4=4、L3=70、L0=288、L1=0；74 行 evidence pool 已全部进入 archive；thinking archive 为 36 行，reasoning archive 为 51 行，13 个交叉题双挂载；Codex A 本地硬审计 14 项 0 failure，ClaudeCode B Opus 4.7 max 审计 58 项中 56 pass、2 warn、0 fail、0 blocked；两个 P3 soft findings 已由 Codex A patch 并重新通过本地审计。

---

# Phase05 判断

## 1. Phase05 evidence archive 是否结构可接受

可以接受。

通过点：

```text
1. control base 已冻结：362 rows。
2. L1 已清空：0 rows。
3. evidence pool 74 rows 与 L4/L3 数量一致。
4. L4 4 行完整保留。
5. L3 70 行独立保留，没有偷升 L4。
6. L0 288 行保留，没有从审计视野消失。
7. thinking archive 覆盖 23 思维 + 13 交叉。
8. reasoning archive 覆盖 38 推理 + 13 交叉。
9. 13 个交叉题双挂载。
10. Q11 pairing lock 已修正为 B=①③。
11. Q12/Q13 answer locator 已保留。
12. student-facing permission 全部保持 no。
```

这说明 Phase05 已达到“证据归档与骨架入口”的最低结构标准。

## 2. 两个 P3 问题是否已足够 patch

可以视为足够 patch，允许进入 Phase06。

两个 P3：

```text
P3-1: Q-2026顺义一模-3 错入 reasoning same-type index。
P3-2: archive backcheck report 曾显示旧 Q11 FAIL。
```

patch 后状态：

```text
1. same-type index 已按 archive membership 生成。
2. thinking index 只取 思维 + 交叉。
3. reasoning index 只取 推理 + 交叉。
4. Q-2026顺义一模-3 已从 reasoning same-type index 移除。
5. backcheck report 已更新为 PASS_INTERNAL_ARCHIVE_BACKCHECK。
6. Q11 pairing lock 显示 PASS。
7. Codex A local audit rerun 仍为 PASS_LOCAL_HARD_AUDIT。
```

但 Phase06 启动时必须做一次 patch freeze：

```text
06_conflicts/phase05_patch_freeze_after_laneB_warnings.md
```

必须写清：

```text
patched files
before issue
after state
rerun audit result
whether ClaudeCode B warning remains open: no / pending_B_ack
```

若还没有 Lane B 对 patch 后文件的二次确认，可以不阻断 Phase06，但必须列为 Phase06 P1 audit item，不能留到学生稿阶段。

---

# Phase06 允许做什么

Phase06 建议命名为：

```text
Phase06 evidence lock and framework fusion
```

允许产出内部文件：

```text
1. evidence lock register
2. 思维框架融合表
3. 推理题型融合表
4. 交叉题双挂载锁定表
5. L3/L4 分级审计表
6. L0 blocker retention register
7. Opus input readiness checklist
8. Governor interim evidence-lock gate
9. Confucius interim learning-value gate
10. GPT commander review packet
```

Phase06 的目标不是写稿，而是把 74 行从“证据池”推进到“可交给成文化 lane 的锁定输入包候选”。

---

# Phase06 必须产出的文件

## P0. evidence lock register

```text
05_coverage/phase06_evidence_lock_register.csv
05_coverage/phase06_evidence_lock_register.md
```

每行至少包含：

```text
question_id
status: L4 / L3
module: 思维 / 推理 / 交叉
question_type
source_locator
answer_locator
rubric_or_commentary_locator
visual_locator
archive_destination
student_permission = no
lock_readiness
missing_fields
risk_note
```

硬规则：

```text
L4 可标 LOCKED_FOR_FRAMEWORK。
L3 只能标 CONFIRMED_FOR_ARCHIVE。
L3 不得自动标 LOCKED_FOR_STUDENT_TEXT。
```

## P0. 思维框架融合表

```text
05_coverage/phase06_thinking_framework_fusion.csv
05_coverage/phase06_thinking_framework_fusion.md
```

36 行必须全部处理，包括 13 个交叉题的思维侧。

每行必须填：

```text
question_id
材料信号
可写思维/方法
答题动作
来源例题
答案落点
易错陷阱
同类题
framework_node
status: L4 / L3
missing_fields
```

思维部分不能只写“科学思维、辩证思维、创新思维”这些标题。必须形成：

```text
材料信号 -> 可写思维/方法 -> 答题动作 -> 来源例题
```

## P0. 推理题型融合表

```text
05_coverage/phase06_reasoning_typology_fusion.csv
05_coverage/phase06_reasoning_typology_fusion.md
```

51 行必须全部处理，包括 13 个交叉题的推理侧。

每行必须填：

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
status: L4 / L3
missing_fields
```

推理部分不能只形成题型目录。每个题型必须能反查到全部题：

```text
题型 -> 规则口令 -> 常见陷阱 -> 同类真题 -> 解题动作
```

## P0. 交叉题双挂载锁定表

```text
05_coverage/phase06_cross_mount_lock.csv
```

13 行必须全部明确：

```text
question_id
thinking_component
reasoning_component
primary_mount
secondary_mount
why_double_mount
whether_student_text_should_duplicate_or_cross_reference
```

交叉题不得被一个“交叉题”标签吞掉。

## P0. 题型同类题总索引

```text
05_coverage/phase06_reasoning_same_type_index_LOCK_CANDIDATE.md
05_coverage/phase06_thinking_same_method_index_LOCK_CANDIDATE.md
```

必须能回答：

```text
某一推理题型下面有哪些题？
某一思维方法下面有哪些题？
每道题是否只出现一次，或因交叉题双挂载而合理出现两次？
```

## P1. L0 blocker retention register

```text
05_coverage/phase06_L0_blocker_retention_register.csv
05_coverage/phase06_L0_blocker_retention_summary.md
```

288 个 L0 必须保留，不得删。

至少分组：

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

Phase06 必须证明：L0 不会进入 Opus 输入包。

## P1. Governor 与 Confucius interim gate

```text
05_coverage/phase06_Governor_evidence_lock_gate.md
05_coverage/phase06_Confucius_framework_value_gate.md
```

Governor 重点：

```text
1. 74 行是否全部锁入 fusion。
2. L3/L4 是否分级。
3. Q11 是否无污染。
4. Q12/Q13 locator 是否存在。
5. 交叉题是否双挂载。
6. L0 是否保留。
7. 是否出现学生稿授权。
```

Confucius 重点：

```text
1. 思维题是否有材料信号。
2. 思维题是否有答题动作。
3. 推理题是否有 logical_form。
4. 推理题是否有规则口令。
5. 推理题是否有易错陷阱。
6. 题型归档是否可迁移。
```

## P1. Phase06 GPT commander review packet

```text
05_coverage/phase06_GPT_commander_review_packet.md
```

必须汇总：

```text
1. 74 行 evidence lock 状态。
2. 36 行 thinking fusion 状态。
3. 51 行 reasoning fusion 状态。
4. 13 行 cross mount 状态。
5. L3/L4 分级状态。
6. L0 retention 状态。
7. Q11 lock。
8. Q12/Q13 locator。
9. unresolved warnings。
10. 是否申请允许 Claude Opus 进入教学文本成文化。
```

---

# Claude Opus 何时可以允许进入

当前不允许。

Claude Opus teaching-text lane 只有在 Phase06 通过后，且同时满足以下条件，才可以有限介入：

```text
1. phase06_evidence_lock_register 完成。
2. 74 行全部有 archive destination。
3. 36 行 thinking fusion 无 missing critical fields。
4. 51 行 reasoning fusion 无 missing critical fields。
5. 13 行 cross rows 双挂载已锁。
6. L3/L4 状态未混淆。
7. Q11 pairing lock 通过。
8. Q12/Q13 answer locators 保留。
9. L0 rows 明确排除出 Opus input。
10. Governor evidence-lock gate 通过。
11. Confucius framework-value gate 通过。
12. GPT-5.5 Pro 明确放行 Opus input packet。
```

即使放行，Opus 也只能拿到：

```text
locked_opus_input_packet
```

不能直接读旧稿，不能读未清洗 source ledger，不能自行补题，不能自行改答案，不能合并题导致逐题覆盖消失。

Opus 首次允许任务也只能是：

```text
teaching-text prototype from locked entries
```

不是最终稿。

---

# 必须继续保留的 guardrails

## 1. L3 vs L4

```text
L4 = 已通过高强度证据锁，可用于 Phase06 framework lock。
L3 = A+B 确认进入 evidence archive，但仍需字段补全和内容一致性检查。
```

硬规则：

```text
1. L3 不得写成“锁定真题”。
2. L3 不得自动进入 Opus input。
3. L3 若缺 logical_form、材料信号、answer_action、locator，必须降级或 pending。
4. L4 不得因成文化被改答案、改题型、改设问。
5. Phase06 必须单独列 L3_promote_candidates 与 L3_hold_list。
```

## 2. B-choice-signal

```text
B-choice-signal = B 线基于选择题信号和答案来源确认可进 evidence archive。
```

硬规则：

```text
1. B-choice-signal 不等于最终学生稿许可。
2. B-choice-signal 不等于 L4。
3. B-choice-signal 题必须有 full options 与 answer locator。
4. B-choice-signal 题在推理部分仍要补 logical_form。
5. B-choice-signal 题在思维部分仍要补材料信号与答题动作。
```

## 3. 交叉题

```text
13 个交叉题必须双挂载。
```

硬规则：

```text
1. 不能只放在“交叉题”总表。
2. 每个交叉题必须有 thinking_component。
3. 每个交叉题必须有 reasoning_component。
4. 学生稿阶段若避免重复讲解，必须设置 cross-reference，但不能删掉任一挂载。
5. Phase06 要决定 primary_mount 与 secondary_mount。
```

## 4. Q11

`Q-2024西城一模-11` 硬锁：

```text
answer = B
pairing = B=①③
wrong retired pairing = B=①④
```

硬规则：

```text
1. Phase06 任何文件出现 Q11 B=①④，立即回滚。
2. B=①④ 只允许出现在非 Q11 行，例如 Q-2026丰台一模-7 的合法 pairing。
3. Q11 archive row 必须保留纠错记录。
4. Q11 进入推理题型时，必须使用完全归纳推理与正确选项 pairing。
```

## 5. Q12/Q13

`2025海淀二模 Q12/Q13` 硬锁：

```text
Q12 answer = D
Q13 answer = C
locator = render_008_page_04 + supplemental answer table page 9
```

硬规则：

```text
1. 不得只保留答案字母。
2. 不得删除 supplemental answer table locator。
3. 不得用逻辑推断替代 answer locator。
4. Phase06 archive 必须保留 full_options_locator 与 answer_key_locator。
```

## 6. L0 rows

```text
L0 = 288 rows retained
```

硬规则：

```text
1. L0 不得进 Opus input。
2. L0 不得在 Phase06 中消失。
3. L0 必须按 blocker reason 保留。
4. out_of_scope 与 true blocker 要区分。
5. duplicate_removed 与 support_reference_row 要区分。
6. Phase06 final packet 必须说明 L0 为什么不进入 74 行 evidence pool。
```

---

# still forbidden

继续阻断：

```text
学生稿
Claude Opus 教学成文化
Word/PDF
final PASS
任何学生可见章节
任何“终稿”“宝典成品”说法
任何把 L3 当 L4 的表述
任何把 archive skeleton 当正文
任何删除 L0 的操作
```

当前阶段最多允许说：

```text
Phase05 evidence archive structurally passed.
Phase06 evidence-lock/framework-fusion may begin.
```

不能说：

```text
内容已可交付学生。
```

---

# Phase06 分工建议

## Codex A

Codex A 继续做主控和生产：

```text
1. 生成 phase06_evidence_lock_register。
2. 生成 phase06_thinking_framework_fusion。
3. 生成 phase06_reasoning_typology_fusion。
4. 生成 phase06_cross_mount_lock。
5. 生成 phase06_L0_blocker_retention_register。
6. 生成 phase06_Governor_evidence_lock_gate。
7. 生成 phase06_Confucius_framework_value_gate。
8. 生成 phase06_GPT_commander_review_packet。
```

Codex A 不得写学生稿。

## ClaudeCode B

ClaudeCode B 做独立审查：

```text
1. 审查 Phase06 的 74 行是否全部保留。
2. 审查 36 thinking rows 是否全部有材料信号与答题动作。
3. 审查 51 reasoning rows 是否全部有 logical_form 与 trap。
4. 审查 13 cross rows 是否双挂载。
5. 审查 Q11、Q12、Q13 三个 hard lock。
6. 审查 L0 是否保留。
7. 输出 phase06_laneB_framework_fusion_audit.csv/md。
```

ClaudeCode B 不得成文化。

## Claude Opus

当前指令：

```text
NO_ACTION_FOR_TEACHING_TEXT
```

最多允许准备一个未来输入边界文件：

```text
phase06_opus_input_boundary_rules.md
```

内容只能写：

```text
1. Opus 只能改写 locked entries。
2. Opus 不能新增题。
3. Opus 不能删题。
4. Opus 不能改答案。
5. Opus 不能改 L3/L4 状态。
6. Opus 不能把交叉题单挂。
7. Opus 输出必须保留 question_id。
8. Opus 输出不得出现 source locator、lane、Governor、Confucius 等内部词。
```

---

# 最终阶段裁决

```text
GO_TO_PHASE06_EVIDENCE_LOCK_AND_FRAMEWORK_FUSION_NO_STUDENT_DRAFT
```

Phase05 archive 结构合格。两个 P3 soft findings 已足够 patch。可以进入 Phase06，但 Phase06 仍是证据锁定与框架融合阶段，不是学生稿阶段。
