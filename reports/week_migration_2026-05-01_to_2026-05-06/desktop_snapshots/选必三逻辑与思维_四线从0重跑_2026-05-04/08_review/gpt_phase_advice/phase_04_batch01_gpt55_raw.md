# GPT-5.5 Pro Phase04 Batch01 Reply

Capture method: Safari ChatGPT web conversation `https://chatgpt.com/c/69f868d7-1394-8399-b34e-d441489903fb`; full exact copy button was not available, so this file is reconstructed from visible page state plus AX dumps:

- `safari_ax_dump_phase04_batch01.tsv`
- `safari_ax_dump_phase04_batch01_pos2.tsv`
- `safari_ax_dump_phase04_batch01_pos3.tsv`
- `safari_ax_dump_phase04_batch01_pos4.tsv`
- `safari_ax_dump_phase04_batch01_pos5.tsv`
- `safari_ax_dump_phase04_batch01_pos6.tsv`

## 1. Batch01 裁决

Batch01 合格，可以进入 Batch02。

合格范围很窄：Batch01 只能算 targeted verification 第一批有效完成，不能算 Phase04 通过，不能算 full coverage 闭合，不能算学生稿证据锁定完成。

继续禁止：

```text
学生稿
Claude/Opus 成文化
Word/PDF
最终 PASS
```

Batch01 价值：

```text
1. 成功解除 2025海淀二模 Q20 的视觉 blocker。
2. 成功解除 2026丰台一模 Q18(2) 的视觉 blocker。
3. 发现并补入 2026朝阳期中 Q12。
4. 使 2025西城二模 Q16(2)、Q16(3) 进入 L4。
5. 让 A 线 matrix 去重拆分后的底座可继续使用。
```

Batch01 硬缺口：

```text
1. L1_A_ONLY_PENDING_B_TARGET 仍有 114 行。
2. L0_BLOCKED 高达 236 行，必须拆分 blocked 类型，不能作为黑箱。
3. 2026丰台一模 042 suite 仍有全套视觉清点风险。
4. 2025海淀二模 Q12/Q13 仍缺 answer source。
5. 2024西城一模 Q11 仍缺 B 线独立复核。
6. 2025海淀期末 Q2 scope 尚未裁定。
7. 2026朝阳期中 Q14/Q15 不能仅凭 B-choice-signal 自动升级。
```

结论：

```text
Batch01 PASS_AS_BATCH
Phase04 NO_PASS
Student稿 NO
```

## 2. Batch02 P0 顺序

### P0-0：先拆分 L0_BLOCKED 236 行

原因：`L0_BLOCKED = 236` 这个数字太粗。若里面混有 out-of-scope、重复删除、支撑材料行、真 blocker，后续 Governor 无法判断风险真实大小。

必须拆成：

```text
OUT_OF_SCOPE
SOURCE_UNREAD_BLOCKED
VISUAL_BLOCKED
ANSWER_SOURCE_MISSING
RUBRIC_SOURCE_MISSING
OPTIONS_MISSING
DUPLICATE_REMOVED
REFERENCE_SUPPORT_ROW
PENDING_SCOPE
TRUE_BLOCKER
```

### P0-1：2026朝阳期中 Q12 正式补入控制表，并补 B results CSV row

动作：

```text
1. 在 phase04_control_base_status_after_laneB_batch01.csv 中正式新增或修正 Q12 行。
2. 在 phase04_laneB_targeted_verification_results.csv 中补独立复核 row。
3. 写清 source_id、suite_id、stable_locator、完整题干选项、答案 B、scope=推理。
4. 更新 in-scope/cross count = 120 的机器可读记录。
```

原因：Q12 是从 Codex 待判中被 B 线纠出的漏判。控制表不先修，后面所有计数都会漂移。

### P0-2：2026丰台一模 042 renders 全套视觉题号/选必三选择题清点

动作：逐页清点 042 rendered pages，不能只看 Q18(2)。必须确认：

```text
Q1-Q15 是否有选必三思维/推理选择题
Q16-Q21 是否有选必三主观题或交叉题
每个选必三候选题的题干、选项、答案源状态、scope
```

产出：

```text
05_coverage/phase04_2026_fengtai_yimo_visual_suite_scan.csv
05_coverage/phase04_2026_fengtai_yimo_selected3_candidates.md
```

硬裁决：若整套没清完，`2026丰台一模` 的 suite-level blocker 不能解除。

### P0-3：2025海淀二模 Q12/Q13 视觉选项 + answer source 补找

动作：

```text
1. 保留 Codex A 从 008 page_04.png 视觉恢复的完整四选项。
2. 让 Lane B 独立复核 Q12/Q13 题干与四选项。
3. 继续在 009/010/011 及所有同 suite 支撑源中找答案。
4. 若找不到答案源，保持 blocked。
```

硬裁决：

```text
完整选项不能替代答案源。
无 answer source 不得进入 L3 或 L4。
不得用题目逻辑推答案。
```

### P0-4：2024西城一模 Q11 B 线复核 Codex XML textbox recovery

Word XML 可以作为 A 线 recovery，但不能替代 Lane B 独立复核。

B 线可使用：

```text
1. 独立读取 DOCX XML textbox。
2. 用 LibreOffice 或 Word 渲染后视觉确认。
3. 用截图确认文本框选项。
```

最低入 fusion 条件：

```text
1. 四个选项完整。
2. 答案 B 来源明确。
3. 答案 B 与 Q11 题号配对明确。
4. A/B 均确认。
5. stable_locator 写入 control base。
```

在 B 线复核完成前，Q11 状态保持：

```text
PENDING_B_RECHECK
NO_FUSION_LOCK
NO_STUDENT_DRAFT
```

### P0-5：2025海淀期末 Q2 scope decision

裁决方向：可入思维部分证据池，但必须标注边界交叉/诱惑项。

理由：

```text
答案 C = ②③。
② 场景迁移/联想思维，是选必三思维。
③ 辩证思维整体性，是选必三思维。
① 扬弃具有哲学诱惑项性质，但不是答案。
④ 经验推广不构成明确思维方法。
```

建议状态：

```text
section_scope = 思维
scope_status = cross 或 in_scope_with_boundary_note
verification_level = B-choice-signal
fusion_level = L3 only after B row can_enter_fusion=yes
student稿_permission = no
```

### P1-1：2026朝阳期中 Q14/Q15 是否从 B-choice-signal 升为 L3

当前不能自动升。

升级条件：

```text
1. full stem = yes
2. full options = yes
3. answer source paired = yes
4. Lane B row can_enter_fusion 修正为 yes
5. Codex A 与 Lane B 对答案 B/D 无冲突
6. scope 分类明确
```

满足后可升：

```text
L3_A_PLUS_B_TARGET_CONFIRMED
```

未满足则保持 pending。

### P1-2：其余 A-only 114/116 行分批

先统一数字来源。当前正式表是 114 行，若其他文件出现 116，必须写明差异来源。

分批规则：

```text
Batch02 Tranche A: 全部 A-only 推理题、交叉题、形式逻辑题。
Batch02 Tranche B: 全部视觉风险题，包括 scan、PPTX 图片、Word textbox、图形批注。
Batch02 Tranche C: 全部选择题 answer pairing 不稳的题。
```

## 3. 2024西城一模 Q11

Word XML 不能替代 Lane B 独立复核。它可以替代普通文本抽取失败，但必须由 B 线或独立渲染/截图机制确认文本框内容。

## 4. 2025海淀二模 Q12/Q13

有完整选项但无答案源时必须 blocked。不得用题目逻辑推答案。

## 5. 2025海淀期末 Q2

可入思维部分证据池，但要写边界说明。正确项本身是选必三思维；哲学扬弃是错误诱惑项，不能因此把整题排除。

## 6. Batch02 后能否开始推理题型归档正文骨架

可以开始“内部归档骨架”，但仍非学生稿，且必须只挂载 L3/L4 或明确标注 pending 的题。禁止学生化讲解、章节导语、把 L1 当已归档例题、隐藏 A-only 推理候选、把综合题粗暴放入综合推理后停止拆解、让 Claude/Opus 接手润色。

## 7. Batch02 必须产出的文件

```text
phase04_blocked_type_split.csv
phase04_2026_chaoyang_q12_formal_patch.csv
phase04_2026_fengtai_yimo_visual_suite_scan.csv
phase04_2026_fengtai_yimo_selected3_candidates.md
phase04_2025_haidian_ermo_Q12_Q13_answer_search.md
phase04_2025_haidian_ermo_Q12_Q13_status.csv
phase04_2024_xicheng_yimo_Q11_B_recheck.csv
phase04_2025_haidian_qimo_Q2_scope_decision.md
phase04_Aonly_batch02_queue.csv
```

## 8. 短 verdict

```text
GO_TO_BATCH02_VISUAL_AND_SCOPE_REPAIR
```
