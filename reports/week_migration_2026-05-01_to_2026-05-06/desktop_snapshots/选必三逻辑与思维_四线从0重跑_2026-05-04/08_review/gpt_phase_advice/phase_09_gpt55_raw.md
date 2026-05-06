GO_TO_PHASE10_POLISH_OR_OUTLINE_NO_WORD_NO_FINAL

## verdict

Phase09 通过受控学生稿草案 gate，可以进入 Phase10 polish/outline。Phase10 仍然只能做结构梳理、表达打磨、标题体系、可读性优化、同类题索引样式统一、交叉题答案锚点补强，不能生成 Word/PDF，不能 final PASS，不能称终稿、最终稿、宝典成品。

裁决依据：Phase09 只从 29 个 Phase08 prototype rows 生成，draft/control rows 均为 29；模块为思维 13、推理 11、交叉 5；禁用学生正文内部词命中为 0；Q11 错配命中为 0；hard-excluded expansion failures 为 0；Codex A 为 `PASS_CODEXA_PHASE09_CONTROLLED_DRAFT`，Lane B 为 `PASS_PHASE09_STUDENT_DRAFT_AUDIT_WITH_WARNINGS` 且无 blocker，warning patch 后为 `PASS_CODEXA_PHASE09_AFTER_LANEB_PATCH`，Governor 与 Confucius 均为 pending GPT 的 pass。

---

## must-fix before Phase10 freeze

这些不是退回 Phase09 的 blocker，但必须在 Phase10 第一版冻结前处理。

### 1. `Q-2025顺义一模-7`

当前已改为大项不当扩大，并在 risk register 中保留源迹。Phase10 必须继续保留这一解释：

```text
选 A。
真实错误是大项不当扩大。
A 项错在把它说成小项不当扩大。
```

不得回流 Phase08 的小项不当扩大旧表达。Phase10 审计表必须继续保留 036 顺义参考答案来源线索。

### 2. `Q-2025丰台期末-7`

继续放在边界陷阱，不得移动进思维主链正例。

固定处理：

```text
主落点：哲学唯物论，从实际出发，从当下做起。
选必三超前思维：干扰项。
```

Phase10 若重排章节，只能放入边界陷阱或易错辨析，不得放入超前思维正例组。

### 3. `Q-2026顺义一模-19-2`

保持科学思维主讲，推理辅助。

固定处理：

```text
主讲线：科学思维三特征，客观性、预见性、可检验性。
辅助线：三段论 / 判断 / 推理骨架，只用于帮助理解证据支撑。
```

不得把它写成典型三段论题。

### 4. `Q-2024朝阳二模-19-1`、`Q-2024朝阳二模-19-2`

Phase09 已移除审稿味表达。Phase10 必须继续确保：

```text
无细则编号。
无文件编号。
无来源页码。
无审稿术语。
填空表达统一为第一空 / 第二空。
```

### 5. `Q-2024朝阳一模-20-1`、`Q-2024朝阳一模-20-2`、`Q-2026通州期末-19-2`

Phase10 必须保持充分条件与必要条件分开写。

固定规则：

```text
充分条件：肯定前件有效，否定后件有效。
必要条件：肯定后件有效，否定前件有效；仅肯定前件不能肯定后件。
```

不得用一个口诀混写。

### 6. `Q-2026丰台一模-18-2`

L4 hard sample 必须保留完整链条：

```text
甲：必要条件假言推理，肯定后件式，前提真实，正确。
乙：三段论，大项在前提中不周延却在结论中周延，大项不当扩大，错误。
```

不得简化成甲正确、乙错误。

### 7. `Q-2025海淀二模-20`

继续保持角度池写法：

```text
辩证思维角度池。
从角度池中选材料最顺的两个写深。
不能写成三点全必答。
不能写成 3 点固定赋分模板。
```

### 8. hard-excluded rows

以下题只能作为 index-only 或 absent，不能展开答案、选项、题型结论：

```text
Q-2024西城一模-11
Q-2025海淀二模-12
Q-2025海淀二模-13
Q-2026顺义一模-3
```

尤其 `Q-2024西城一模-11` 不得出现 `B=①④` 作为正确配对。

---

## allowed next actions

Phase10 可以启动，建议阶段名：

```text
Phase10 polish and outline from controlled 29-row student draft
```

允许产出：

```text
09_student_draft/phase10_polished_outline_FROM_29.md
09_student_draft/phase10_polish_control_matrix.csv
09_student_draft/phase10_question_id_traceability_backcheck.csv
09_student_draft/phase10_same_type_index_style_decision.md
09_student_draft/phase10_cross_answer_anchor_patch.md
09_student_draft/phase10_internal_terms_scan.md
09_student_draft/phase10_QID_risk_register.md
08_review/phase10_codexA_polish_verification.md
claudecode_lane/opus47_phase10_polish_audit/phase10_laneB_polish_audit.md
08_review/phase10_Governor_boundary_gate.md
08_review/phase10_Confucius_learning_value_gate.md
08_review/phase10_GPT_commander_review_packet.md
```

Phase10 可以做：

```text
1. 调整章节标题和小标题。
2. 统一同类题索引呈现方式。
3. 统一选择题答案表达，例如选 C，②③。
4. 给交叉题补一行答案落点，提升卷面作答锚点。
5. 删除所有审稿味、流程味、文件味表达。
6. 优化语言可读性。
7. 保持 29 行不扩张。
8. 保持所有 question_id 在 control matrix 中可回查。
```

---

## still forbidden

继续禁止：

```text
Word
PDF
final PASS
终稿
最终稿
宝典成品
扩展到 74 evidence rows
加入 45 hold rows
加入 288 L0 rows
把 hard-excluded rows 展开成答案讲解
删除 question_id traceability
把同类题 ID 自动扩成完整解析
把 L3_candidate 写成完全锁定
改变答案
改变选项 pairing
改变题型归属
改变交叉题主辅线
```

不需要 `RUN_ADDITIONAL_LANEB_AUDIT`。Lane B 已完成 Phase09 审计，P0 全 pass，无 blocker；P1 warning 已由 Codex patch，Governor 和 Confucius 均给出 pending GPT 的 pass。下一次 Lane B 应审 Phase10 polish 是否越界，而不是重跑 Phase09。

不需要 `STOP_SOURCE_REPAIR_REQUIRED`。当前没有源证据 blocker，剩余风险是 polish 阶段表达、边界、索引和双挂载保真风险。

---

## next-phase hard rules

1. Phase10 仍然只处理 29 行。任何新增题必须回到 Phase07 packet 和本地证据链，不能由 polish 阶段直接加入。

2. 思维部分必须保留完整链条：

```text
材料信号 -> 可写思维/方法 -> 为什么能想到 -> 答题动作 -> 答案落点 -> 易错陷阱 -> 同类题
```

3. 推理部分必须保留完整链条：

```text
题型 -> 逻辑形式 -> 规则口诀 -> 有效式或错误式 -> 解题动作 -> 答案落点 -> 易错陷阱 -> 同类题
```

4. 交叉题必须继续双挂载。Phase10 可以让正文更简洁，但 control matrix 中必须保留主挂载、次挂载、同类题索引和对应题号。

5. 同类题索引只能作为索引。未进入 29 行的题不得因出现在同类题列表中被展开答案或解析。

6. 选择题答案必须统一为：

```text
选 X，组合项。
```

例如：

```text
选 C，②③。
选 D，③④。
```

7. 主观题必须保留至少一句可直接写到答题纸上的答案落点，不能只保留讲解口吻。

8. Phase10 必须决定可见标题策略：要么保留学生友好标题并用 control matrix 追踪 question_id，要么在标题中附简短 question_id。不能让审计回查再次依赖模糊匹配。

9. 内部词继续零容忍：

```text
Phase09
Phase10
packet
source locator
lane
Governor
Confucius
L3
L4
B-choice-signal
LOCKED_FOR_FUSION
文件路径
细则编号
```

这些可以出现在审计文件中，不能出现在学生正文中。

10. Phase10 完成后必须先过 Codex A verification，再过 ClaudeCode Lane B audit，再过 Governor/Confucius gate，再提交 GPT review。未通过这些 gate 前，Word/PDF 和 final PASS 继续阻断。
