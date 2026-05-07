# P2G012_RECHECK_ACCEPTANCE: NOT_FINAL

> 状态：NOT_FINAL（小规模 source_id 级 P2 复核子产物，非交付件）。
> Scope: 仅 P2G012，单一 source_id `012_Desktop_2025模拟题_2025各区期末_2025东城期末_试卷_试卷.pdf`。
> 不写 Word/PDF；不写 delivery/；不写 framework_first_fusion 终稿 patch 文件；输出仅在 `claudecode_lane/p2_recheck/`。

## 1. 输出件清单与计数

| 文件 | 路径（相对） | 期望 | 实际 |
|------|-------------|------|------|
| P2G012_RECHECK_DECISIONS.csv | claudecode_lane/p2_recheck/P2G012_RECHECK_DECISIONS.csv | 1 表头 + 4 数据行 | 1 表头 + 4 数据行 ✅ |
| P2G012_RECHECK_PATCHES.jsonl | claudecode_lane/p2_recheck/P2G012_RECHECK_PATCHES.jsonl | 4 行 JSON | 4 行 JSON ✅ |
| P2G012_SOURCE_EVIDENCE.md | claudecode_lane/p2_recheck/P2G012_SOURCE_EVIDENCE.md | 已写 | 已写 ✅ |
| P2G012_RECHECK_ACCEPTANCE.md | claudecode_lane/p2_recheck/P2G012_RECHECK_ACCEPTANCE.md | 当前文件 | 已写 ✅ |
| P2G012_PROGRESS.md | claudecode_lane/p2_recheck/P2G012_PROGRESS.md | 已写 | 已写 ✅ |

精确行数声明：
- decision rows = 4（exact）
- patch rows = 4（exact）
- 四行的 question_id：Q-2025东城期末-5 / Q-2025东城期末-13 / Q-2025东城期末-14 / Q-2025东城期末-15。
- 无任何其他 P2 行混入。

## 2. CSV header 校验

实际表头：
`priority,question_id,parent_question_id,source_batch,type,framework_node,evidence_level,decision,decision_reason,source_evidence,patch_needed,can_enter_fusion`

与任务规定完全一致 ✅。

## 3. Allowed-decisions 校验

| 行 | decision | 是否在允许集 |
|----|----------|-------------|
| Q-2025东城期末-5 | confirmed_with_patch | ✅ |
| Q-2025东城期末-13 | confirmed_with_patch | ✅ |
| Q-2025东城期末-14 | confirmed_with_patch | ✅ |
| Q-2025东城期末-15 | confirmed_with_patch | ✅ |

允许集：confirmed / confirmed_with_patch / downgrade_to_index / source_insufficient / wrong_framework / block_from_student_body。四行均落在 confirmed_with_patch，符合允许集。

## 4. 评分硬规则一致性

- **'Verify stem/options and answer key before confirming choice-trap rows'**：四行的 stem/options 已在 012_*paper.txt 行40-48/110-117/118-124/125-131 行级核验；answer key 在同一 paper.txt 行 318-346/490-509/510-542/543-564（教师版试卷嵌入的"参考答案"段）逐字核验为 5.C / 13.B / 14.D / 15.B；按规则可以 confirm ✅。
- **'Use the manifest evidence_level exactly unless the source genuinely proves the row is misclassified'**：四行均沿用 manifest 中的 evidence_level=B-choice-signal，未做任何上调下调（B-choice-signal 表示题面+选项+答案均在源中明示且 framework_node 由选项配对锁定，与源证据完全一致） ✅。
- **'Do not invent options, answers, rubrics, or source files'**：四行的 patched_answer_sentence 均直引 paper.txt 行号+"故选：C/B/D/B"原文，未捏造任何答案；source_evidence 仅引用 P2_SOURCE_TEXT_INDEX.csv 第8-10行已落地的三份文本（1 paper + 2 support），未引用未抽取的源文件 ✅。
- **'If answer evidence is unavailable, mark source_insufficient and can_enter_fusion=no'**：四行的答案证据均充分（paper.txt 行级可核验），故无需走 source_insufficient；四行 can_enter_fusion=yes ✅。

## 5. Source_id 范围校验

仅包含 source_id=`012_Desktop_2025模拟题_2025各区期末_2025东城期末_试卷_试卷.pdf` 的 P2 行。
不涉及 001/003/006/017/035/040/042/044/046 等其他 P2 source_id。

manifest（fusion/framework_first_fusion/RECHECK_MANIFEST_ENRICHED.csv）grep '012_Desktop_2025模拟题_2025各区期末_2025东城期末' 共命中 8 行，其中 priority=P0 的 4 行（Q-2025东城期末-18-2 跨节点的重复参考行）已超出本次 P2 范围；priority=P2 的 4 行恰为本次范围：
- Q-2025东城期末-5（辩证思维>整体性+动态性+矛盾分析法）
- Q-2025东城期末-13（推理>演绎推理>三段论·中项不周延）
- Q-2025东城期末-14（推理>判断>性质判断·主谓项周延）
- Q-2025东城期末-15（推理>演绎推理>充分条件假言推理）

四行全部纳入；无遗漏；无额外行 ✅。

## 6. 文件位置硬规则

所有输出仅在 `claudecode_lane/p2_recheck/` 目录之下：

```
claudecode_lane/p2_recheck/P2G012_RECHECK_DECISIONS.csv
claudecode_lane/p2_recheck/P2G012_RECHECK_PATCHES.jsonl
claudecode_lane/p2_recheck/P2G012_SOURCE_EVIDENCE.md
claudecode_lane/p2_recheck/P2G012_RECHECK_ACCEPTANCE.md
claudecode_lane/p2_recheck/P2G012_PROGRESS.md
```

无 Word/PDF/delivery/最终交付物 ✅。

## 7. patch_needed 与 can_enter_fusion 字段一致性

| question_id | decision | patch_needed | can_enter_fusion | 一致性说明 |
|-------------|----------|--------------|------------------|------------|
| Q-2025东城期末-5 | confirmed_with_patch | yes | yes | confirmed_with_patch → patch_needed=yes（去除"需 Codex 回源复核"标记并锁定答案 C） + can_enter_fusion=yes（源充分，可入正文） |
| Q-2025东城期末-13 | confirmed_with_patch | yes | yes | 同上，锁定答案 B |
| Q-2025东城期末-14 | confirmed_with_patch | yes | yes | 同上，锁定答案 D |
| Q-2025东城期末-15 | confirmed_with_patch | yes | yes | 同上，锁定答案 B |

## 8. 后续动作（非本任务范围）

- **后续 fusion patch（独立任务）**：framework_first_fusion P1_PATCHED.md 第142/543/643/667 行四处需去除"（choice_trap；B-choice-signal；**需 Codex 回源复核**）"中的"需 Codex 回源复核"标记，正文锁定答案 C/B/D/B。该 patch 应由独立任务承接，不在 P2G012 这一小规模子任务输出范围内。
- **其他 P2 source_id 的子组复核**：001/003/006/035/040/042/044/046 等 P2 source_id 应由独立的 P2GXXX 子任务承接（P2G017 已闭合；本 P2G012 闭合后，剩余子组应继续切片处理）。

## 9. 终态声明

`P2G012_RECHECK_ACCEPTANCE: NOT_FINAL`

- exact row count 4 ✅
- patch count 4 ✅
- no Word/PDF/delivery ✅
- 输出全部在 claudecode_lane/p2_recheck/ ✅
- 四行 decision 均为 confirmed_with_patch（源充分、未捏造答案、维持 manifest evidence_level） ✅
- four answer keys（5.C / 13.B / 14.D / 15.B）均已通过 paper.txt 行级核验 ✅
- four framework_nodes 与 manifest 一致并由源逐项验证 ✅
