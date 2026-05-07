# P2G046_RECHECK_ACCEPTANCE: NOT_FINAL

> 状态：NOT_FINAL（小规模 source_id 级 P2 复核子产物，非交付件）。
> Scope: 仅 P2G046，单一 source_id `046_Desktop_2026模拟题_2026各区一模_2026东城一模_试卷_试卷.pdf`。
> 不写 Word/PDF；不写 delivery/；不写 framework_first_fusion 终稿 patch 文件；输出仅在 `claudecode_lane/p2_recheck/`。

## 1. 输出件清单与计数

| 文件 | 路径 | 期望 | 实际 |
|------|------|------|------|
| P2G046_RECHECK_DECISIONS.csv | claudecode_lane/p2_recheck/P2G046_RECHECK_DECISIONS.csv | 1 表头 + 3 数据行 | 1 表头 + 3 数据行 ✅ |
| P2G046_RECHECK_PATCHES.jsonl | claudecode_lane/p2_recheck/P2G046_RECHECK_PATCHES.jsonl | 3 行 JSON | 3 行 JSON ✅ |
| P2G046_SOURCE_EVIDENCE.md | claudecode_lane/p2_recheck/P2G046_SOURCE_EVIDENCE.md | 已写 | 已写 ✅ |
| P2G046_RECHECK_ACCEPTANCE.md | claudecode_lane/p2_recheck/P2G046_RECHECK_ACCEPTANCE.md | 当前文件 | 已写 ✅ |
| P2G046_PROGRESS.md | claudecode_lane/p2_recheck/P2G046_PROGRESS.md | 已写 | 已写 ✅ |

精确行数声明：
- decision rows = 3（exact）
- patch rows = 3（exact）
- 三行的 question_id：Q-2026东城一模-5 / Q-2026东城一模-6 / Q-2026东城一模-7。
- 无任何其他 P2 行混入。

## 2. CSV header 校验

实际表头：
`priority,question_id,parent_question_id,source_batch,type,framework_node,evidence_level,decision,decision_reason,source_evidence,patch_needed,can_enter_fusion`

与任务规定完全一致 ✅。

## 3. Allowed-decisions 校验

| 行 | decision | 是否在允许集 |
|----|----------|-------------|
| Q-2026东城一模-5 | confirmed_with_patch | ✅ |
| Q-2026东城一模-6 | confirmed_with_patch | ✅ |
| Q-2026东城一模-7 | confirmed_with_patch | ✅ |

允许集：confirmed / confirmed_with_patch / downgrade_to_index / source_insufficient / wrong_framework / block_from_student_body。三行均落在 confirmed_with_patch，符合允许集。

## 4. 评分硬规则一致性

- 'Verify stem/options and answer key before confirming choice-trap rows'：
  - 三行的 stem 与四个选项已在 046_*paper.txt 行46-52（Q5）/行53-60（Q6）/行61-73（Q7）逐字核验；
  - answer key 已在 046_*paper.txt 行265-268 答案表逐字核验：5=B / 6=D / 7=D；
  - Q7 还另有 26东城一模细则.pdf 第9页 + 18+选择7、13.pptx 第5-6 张幻灯片官方符号化推理双重佐证；
  - 全部满足'choice_trap 复核须先验 stem/options 与 answer key'硬规则后再 confirm ✅。
- 'Use the manifest evidence_level exactly unless the source genuinely proves the row is misclassified'：
  - 三行均沿用 manifest 中的 evidence_level=B-choice-signal，未做任何上调下调；
  - source 未证明任何一行被错误分级 ✅。
- 'Do not invent options, answers, rubrics, or source files'：
  - 三行的 patched_answer_sentence 全部以 paper.txt 答案表为准；Q7 额外引用 26东城一模细则.pdf 与 18+选择7、13.pptx 中实际存在的符号化材料；
  - 未捏造任何选项/答案/细则/源文件 ✅。
- 'If answer evidence is unavailable, mark source_insufficient and can_enter_fusion=no'：
  - 三行 answer evidence 均充分（paper.txt 答案表 + Q7 细则补强），全部 confirmed_with_patch + can_enter_fusion=yes，符合规则的反面（即 evidence 充分时不应误标 source_insufficient）✅。

## 5. Source_id 范围校验

仅包含 source_id=`046_Desktop_2026模拟题_2026各区一模_2026东城一模_试卷_试卷.pdf` 的 P2 行。
不涉及 001/003/006/012/017/035/040/042/044 等其他 P2 source_id。

manifest 中本 source_id 下 P2 行恰为：
- P2,Q-2026东城一模-5 (辩证思维>分析与综合)
- P2,Q-2026东城一模-6 (推理>演绎推理>换质位推理)
- P2,Q-2026东城一模-7 (推理>演绎推理>复合假言推理)

三行全部纳入；无遗漏；无额外行 ✅。

## 6. 文件位置硬规则

所有输出仅在 `claudecode_lane/p2_recheck/` 目录之下。
- 无 Word（.docx）输出 ✅
- 无 PDF 输出 ✅
- 无 `delivery/` 目录写入 ✅
- 无 framework_first_fusion 终稿 patch 写入 ✅
- 无 fusion/ 子目录写入 ✅

## 7. fusion P1 体覆盖确认

| 行 | fusion P1 行号 | 现状 | 本 patch 动作 |
|----|--------------|------|-------------|
| Q5 | 第93-101 行 | 已含完整识别+陷阱+卷面句但带'需 Codex 回源复核'前置标签 | 锁定答案 B（paper 答案表 5=B），后续 patch 应去除复核标签 |
| Q6 | 第698-708 行 | 已含完整识别+陷阱+卷面句但带'需 Codex 回源复核'前置标签 | 锁定答案 D（paper 答案表 6=D），后续 patch 应去除复核标签 |
| Q7 | 第688-696 行 | 已含完整符号化卷面句但带'需 Codex 回源复核'前置标签 | 锁定答案 D（paper 答案表 7=D + 细则 pdf + pptx 真值表三重证据），后续 patch 应去除复核标签 |

manifest 中 Q5/Q7 标 phase12_action=blocked_keep_out / phase12_category=answer_missing 在本轮源级复核中已被推翻——答案表与官方符号化推理证据齐备；Q6 标 phase12_action=covered_by_74_review_body 与 fusion P1 第698-708 行落体一致。

## 8. 后续动作（非本任务范围）

- 后续 fusion patch 应将 framework_first_fusion P1 第93/690/700 行三处'需 Codex 回源复核'前置标签按 confirmed_with_patch 路径处理（去除标签，保留正文）；
- Q5 与 Q7 应从 manifest 标记的 blocked_keep_out 状态转入正常学生体保留路径；Q6 维持 74-row review-only expanded body 现状或视后续需要并入学生体；
- 不在本 P2G046 任务的输出范围内。

## 9. 终态声明

`P2G046_RECHECK_ACCEPTANCE: NOT_FINAL`

- exact row count 3 ✅
- patch count 3 ✅
- no Word/PDF/delivery ✅
- 输出全部在 claudecode_lane/p2_recheck/ ✅
- 三行 decision 均为 confirmed_with_patch（基于 paper 答案表与细则 pdf/pptx 三重证据，未捏造答案）✅
- evidence_level 与 manifest 完全一致（B-choice-signal × 3）✅
- 仅 source_id=046 范围 ✅
