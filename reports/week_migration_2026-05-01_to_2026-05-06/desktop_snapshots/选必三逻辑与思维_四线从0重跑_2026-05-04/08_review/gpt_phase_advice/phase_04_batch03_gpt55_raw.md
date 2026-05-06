# verdict

```text
GO_TO_PHASE05_EVIDENCE_FUSION_ARCHIVE
```

Batch03 达到我上次要求的 A-only/L1 队列复核目标。可以进入 Phase05，任务限于：

```text
证据融合底稿
同类题归档
思维框架骨架
推理题型骨架
缺口反查
一致性审计
```

仍然禁止：

```text
学生稿
Claude/Opus 成文化
Word/PDF
final PASS
```

不能选择 `GO_TO_STUDENT_DRAFT_PREP`。理由：当前 74 行只是 evidence fusion pool，尚未完成思维链、推理 logical form、题型归档正文骨架、L3/L4 内部一致性校验，也没有 Governor/Confucius 内容门禁。

---

# 审查结论

## 1. Batch03 是否完成 112 个 A-only/L1 行

认可完成。

依据是：

```text
主观题 56/56 已处理
选择题 56/56 已处理
合计 112/112
主观题 CSV 结构验收通过
选择题 normalized CSV 结构验收通过
学生稿权限 112 行全部 no
```

合并结果也自洽：

```text
Batch02 后 L3 = 13
Batch03 新确认 = 23 + 34 = 57
Batch03 后 L3 = 70
70 = 13 + 57
```

所以 112 行 A-only 队列已完成 targeted verification。
注意：这是 A-only 队列复核完成，不等于全书最终覆盖 PASS。

## 2. 选择题 normalized CSV 是否可作为 merge source

可以接受，但必须保留审计约束。

本轮 normalized CSV 的性质是字段归位修复，且 Codex 保留 raw CSV、生成 normalization audit，并声明不改证据结论。这个处理可以作为机械合并输入。

但必须把以下文件列入 Phase05 审计附件：

```text
claudecode_lane/opus47_batch03_choice/phase04_batch03_B_choice_results_normalized.csv
claudecode_lane/opus47_batch03_choice/phase04_batch03_B_choice_results_normalization_audit.csv
```

同时必须新增一个计数差异说明：

```text
06_conflicts/phase04_batch03_choice_count_discrepancy_audit.md
```

写清：

```text
raw report 手工计数 = 31 confirmed / 25 scope_out
row-level normalized CSV = 34 confirmed / 22 scope_out
merge source = row-level normalized CSV
理由 = row-level question_id 可逐行回源，手工汇总不可覆盖逐行记录
是否改变证据结论 = no
```

如果 Phase05 后续发现 34 个 confirmed 中存在无 locator、无答案源、无完整选项的行，必须降级。

## 3. `2026东城期末 Q16` cleanup 是否合理

认可。

根据你提供的信息：

```text
原卷与细则均为一个 7 分单题
不是 16(1) 与 16(2) 两个选必三逻辑与思维子题
内容归属为哲学与文化
非本项目核心范围
```

处理方式合理：

```text
只保留一个 boundary closed row
不保留错误拆分
不进入 evidence fusion pool
不进入思维/推理主链
```

但 Phase05 必须把它列在：

```text
out_of_scope_boundary_decisions
```

原因是它曾进入队列，后续不能无痕消失。

## 4. `2025西城二模 Q16(2)` 是否应视为已保留

应视为已保留，不构成新缺口。

当前处理正确：

```text
Batch03 队列缺失不构成漏题
因为全局控制表中已由 Batch01 锁定为 L4_LOCKED_FOR_FUSION
无需重复补行
```

Phase05 需要做的只是防止重复：

```text
保持 Q-2025西城二模-16(2) 为 L4
不得在 Batch03 cleanup 中误降级
不得重复生成第二个 canonical id
```

---

# must-fix list

以下是进入 Phase05 后必须先修的审计项。它们不阻断进入 Phase05，但阻断 Phase05 通过。

## M1. 固化 Batch03 cleaned control base

必须冻结：

```text
05_coverage/phase04_control_base_status_after_batch03_cleaned.csv
```

并生成：

```text
05_coverage/phase04_batch03_cleaned_status_freeze.md
```

必须写明：

```text
total rows = 362
L4 = 4
L3 = 70
L0 = 288
L1 = 0
duplicate canonical id = 0
student-facing permission = no for all rows
```

如果还有 L1，则 Batch03 未闭合。你给出的 cleaned table 显示 L1 已清空，这一点要写入 freeze。

## M2. 选择题 34/22 与 report 31/25 的差异审计

必须新增：

```text
06_conflicts/phase04_batch03_choice_count_discrepancy_audit.md
```

要求逐项列出是哪 3 行造成差异。不能只写“以 normalized 为准”。

最低字段：

```text
question_id
raw_report_status
normalized_row_status
cause_of_difference
source_locator
answer_locator
final_merge_status
```

## M3. 2024西城一模 Q11 pairing 污染锁

必须生成或更新：

```text
06_conflicts/phase04_2024_xicheng_yimo_Q11_pairing_lock.md
```

固定：

```text
correct answer = B
correct pairing = B=①③
A=①②
B=①③
C=②④
D=③④
Codex A prior wrong pairing = B=①④
wrong pairing must not propagate
```

任何 Phase05 文件出现 `B=①④`，直接回滚该文件。

## M4. 2025海淀二模 Q12/Q13 答案源 locator 保留

必须在 Phase05 evidence archive 中保留 answer locator。不能只保留答案字母。

最低字段：

```text
question_id
full_options_locator
answer_key_locator
answer
LaneB_confirmation
fusion_status
```

若找不到可核查答案 locator，必须降级：

```text
L3 -> L0_ANSWER_SOURCE_MISSING
```

## M5. L3 与 L4 分级不得混用

当前 74 行中：

```text
L4 = 4
L3 = 70
```

Phase05 archive 必须保留分级。L3 不得写成“锁定题”。建议命名：

```text
L4_LOCKED_FOR_FUSION
L3_CONFIRMED_FOR_EVIDENCE_ARCHIVE
```

L3 仍需经过内容字段补全，尤其是：

```text
思维题：材料信号、答题动作、来源例题
推理题：logical_form、rule_slogan、trap、answer_action、same_type_question_ids
```

## M6. 288 个 L0 需要按原因保留

L0 不能变成垃圾桶。Phase05 必须携带：

```text
phase04_blocked_type_split.csv/md
```

并在 archive skeleton 中显示：

```text
out_of_scope
duplicate_removed
boundary_closed
answer_missing
visual_missing
scope_rejected
support_reference_row
```

---

# allowed next actions

## A. 进入 Phase05 evidence fusion archive

Phase05 可以启动，建议正式命名：

```text
Phase05 evidence fusion archive and typology skeleton
```

核心输入：

```text
05_coverage/phase04_control_base_status_after_batch03_cleaned.csv
06_conflicts/phase04_batch03_codexA_laneB_reconciliation.md
06_conflicts/phase04_batch03_queue_meta_cleanup_decisions.md
claudecode_lane/opus47_batch03_choice/phase04_batch03_B_choice_results_normalized.csv
claudecode_lane/opus47_batch03_subjective/phase04_batch03_A_subjective_results.csv
```

## B. 建 74 行 evidence pool 总表

产出：

```text
05_coverage/phase05_evidence_pool_74.csv
05_coverage/phase05_evidence_pool_74.md
```

字段至少包含：

```text
question_id
suite_id
source_locator
question_type
module: 思维 / 推理 / 交叉
status: L3 / L4
answer_locator
rubric_locator
visual_locator
full_stem_status
full_options_status
student_permission
risk_note
```

## C. 建思维部分 evidence archive

产出：

```text
05_coverage/phase05_thinking_signal_archive.csv
05_coverage/phase05_thinking_signal_archive.md
```

每一行必须填：

```text
question_id
材料信号
可写思维/方法
答题动作
答案落点
来源例题
同类题
易错陷阱
status
missing_fields
```

思维部分 23 行与交叉题中涉及思维的部分都要挂入，不得只挂主观题。

## D. 建推理部分 typology archive

产出：

```text
05_coverage/phase05_reasoning_typology_archive.csv
05_coverage/phase05_reasoning_typology_archive.md
05_coverage/phase05_reasoning_same_type_index.md
```

每一行必须填：

```text
question_id
primary_reasoning_type
secondary_reasoning_type
logical_form
rule_slogan
valid_or_invalid_pattern
trap
answer_action
same_type_question_ids
status
missing_fields
```

推理部分 38 行与交叉题中涉及推理的部分都要挂入。

## E. 建交叉题拆分表

产出：

```text
05_coverage/phase05_cross_question_split_matrix.csv
```

交叉题 13 行必须拆清：

```text
question_id
thinking_component
reasoning_component
primary_archive_destination
secondary_archive_destination
是否双挂载
```

交叉题不能只放在一个“交叉”文件里。

## F. 做反查校验

产出：

```text
06_conflicts/phase05_archive_backcheck_report.md
```

校验：

```text
74 evidence rows 是否全部进入 archive
23 thinking rows 是否全部进入 thinking archive
38 reasoning rows 是否全部进入 reasoning archive
13 cross rows 是否双挂载或说明单挂载理由
L4 4 行是否全部保留
Q11 是否保持 B=①③
Q12/Q13 是否保留 answer locator
Q16 cleanup 是否没有误删 L4 Q16(2)
所有 student_permission 是否仍为 no
```

---

# still forbidden actions

继续禁止：

```text
学生稿
Claude/Opus 成文化
Word/PDF
final PASS
把 L3 题写成已锁定标准例题
把 archive skeleton 写成学生可读正文
把 B-choice-signal 当成最终入稿证据
删除 288 个 L0 的阻断记录
隐藏 2026东城期末 Q16 的 cleanup 决策
把 2024西城一模 Q11 写回 B=①④
用无 locator 的答案进入 archive
```

尤其禁止现在进入 `GO_TO_STUDENT_DRAFT_PREP`。
理由：

```text
1. Phase05 archive 还没建。
2. 74 行还没完成同类题归档。
3. 推理题 logical_form 尚未逐题验收。
4. 思维题材料信号链尚未逐题验收。
5. 交叉题双挂载尚未完成。
6. Governor/Confucius 尚未对内容骨架做门禁。
```

---

# 下一批分工建议

## Codex A 下一步

Codex A 做 Phase05 主控生产。

必须产出：

```text
05_coverage/phase05_evidence_pool_74.csv
05_coverage/phase05_thinking_signal_archive.csv
05_coverage/phase05_reasoning_typology_archive.csv
05_coverage/phase05_cross_question_split_matrix.csv
05_coverage/phase05_reasoning_same_type_index.md
06_conflicts/phase05_archive_backcheck_report.md
06_conflicts/phase04_batch03_choice_count_discrepancy_audit.md
06_conflicts/phase04_2024_xicheng_yimo_Q11_pairing_lock.md
```

Codex A 的工作重点：

```text
1. 把 74 行全部挂入 archive。
2. 对推理题逐题补 logical_form。
3. 对思维题逐题补材料信号和答题动作。
4. 对交叉题做双挂载。
5. 保留 L3/L4 状态，不得偷升。
6. 做 archive backcheck。
```

## ClaudeCode Lane B 下一步

ClaudeCode B 不需要再扫 112 行。它要做 Phase05 独立抽查与压力复核。

建议任务：

```text
1. 独立复核 74 行 evidence pool 是否全部有 locator。
2. 独立检查 Q11 pairing lock。
3. 独立检查 Q12/Q13 answer locator。
4. 抽查 reasoning archive 中全部 L4 与至少 30% L3 推理题。
5. 抽查 thinking archive 中全部 L4 与至少 30% L3 思维题。
6. 专门检查 13 个交叉题是否漏双挂载。
7. 输出 phase05_laneB_archive_audit.csv/md。
```

ClaudeCode B 不能做：

```text
学生化表达
章节润色
合并同类题正文
替 Codex 补写无 locator 答案
```

## Claude/Opus 下一步

Claude/Opus 仍不进场成文化。

当前给 Claude/Opus 的动作应为：

```text
NO_ACTION_FOR_STUDENT_TEXT
```

如果确实要提前准备，只允许做一个内部格式规范检查，不接触题目内容：

```text
phase05_opus_style_constraints_draft.md
```

内容只能包括：

```text
学生稿未来禁止出现的内部词
未来条目模板
未来语言风格约束
不得新增题
不得改答案
不得合并题
不得删除 L3/L4 状态
```

Claude/Opus 不得读取 74 行后改写为正文。Phase05 结束、GPT/Governor/Confucius 对 archive 通过后，才允许讨论是否进入 student draft prep。

---

# 最终裁决

```text
GO_TO_PHASE05_EVIDENCE_FUSION_ARCHIVE
```

Batch03 已完成 A-only 队列复核，cleaned control base 可以进入 evidence fusion archive。
Phase05 的任务是把 74 行做成可审计的思维链与推理题型归档骨架。
学生稿、Claude/Opus 成文化、Word/PDF、最终 PASS 继续全部阻断。
