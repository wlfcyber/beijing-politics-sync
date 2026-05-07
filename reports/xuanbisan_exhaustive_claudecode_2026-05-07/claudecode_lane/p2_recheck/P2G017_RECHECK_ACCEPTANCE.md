# P2G017_RECHECK_ACCEPTANCE: NOT_FINAL

> 状态：NOT_FINAL（小规模 source_id 级 P2 复核子产物，非交付件）。
> Scope: 仅 P2G017，单一 source_id `017_Desktop_2024模拟题_2024朝阳期中_试卷_试卷.pdf`。
> 不写 Word/PDF；不写 delivery/；不写 framework_first_fusion 终稿 patch 文件；输出仅在 `claudecode_lane/p2_recheck/`。

## 1. 输出件清单与计数

| 文件 | 路径 | 期望 | 实际 |
|------|------|------|------|
| P2G017_RECHECK_DECISIONS.csv | claudecode_lane/p2_recheck/P2G017_RECHECK_DECISIONS.csv | 1 表头 + 3 数据行 | 1 表头 + 3 数据行 ✅ |
| P2G017_RECHECK_PATCHES.jsonl | claudecode_lane/p2_recheck/P2G017_RECHECK_PATCHES.jsonl | 3 行 JSON | 3 行 JSON ✅ |
| P2G017_SOURCE_EVIDENCE.md | claudecode_lane/p2_recheck/P2G017_SOURCE_EVIDENCE.md | 已写 | 已写 ✅ |
| P2G017_RECHECK_ACCEPTANCE.md | claudecode_lane/p2_recheck/P2G017_RECHECK_ACCEPTANCE.md | 当前文件 | 已写 ✅ |
| P2G017_PROGRESS.md | claudecode_lane/p2_recheck/P2G017_PROGRESS.md | 已写 | 已写 ✅ |

精确行数声明：
- decision rows = 3（exact）
- patch rows = 3（exact）
- 三行的 question_id：Q-2024朝阳期中-7 / Q-2024朝阳期中-8 / Q-2024朝阳期中-10。
- 无任何其他 P2 行混入。

## 2. CSV header 校验

实际表头：
`priority,question_id,parent_question_id,source_batch,type,framework_node,evidence_level,decision,decision_reason,source_evidence,patch_needed,can_enter_fusion`

与任务规定完全一致 ✅。

## 3. Allowed-decisions 校验

| 行 | decision | 是否在允许集 |
|----|----------|-------------|
| Q-2024朝阳期中-7 | source_insufficient | ✅ |
| Q-2024朝阳期中-8 | source_insufficient | ✅ |
| Q-2024朝阳期中-10 | source_insufficient | ✅ |

允许集：confirmed / confirmed_with_patch / downgrade_to_index / source_insufficient / wrong_framework / block_from_student_body。三行均落在 source_insufficient，符合允许集。

## 4. 评分硬规则一致性

- 'Verify stem/options and answer key before confirming choice-trap rows'：三行的 stem/options 已经过 paper.txt 行级核验；answer key 在 017 源所有 support 文件内不存在；按规则不能 confirm，全部走 source_insufficient ✅。
- 'Use the manifest evidence_level exactly unless the source genuinely proves the row is misclassified'：三行均沿用 manifest 中的 evidence_level=B-choice-signal，未做任何上调下调 ✅。
- 'Do not invent options, answers, rubrics, or source files'：三行的 patched_answer_sentence 均明文'源不足，不输出确定性答案'，未捏造任何答案 ✅。
- 'If answer evidence is unavailable, mark source_insufficient and can_enter_fusion=no'：三行 decision=source_insufficient + can_enter_fusion=no ✅。

## 5. Source_id 范围校验

仅包含 source_id=`017_Desktop_2024模拟题_2024朝阳期中_试卷_试卷.pdf` 的 P2 行。
不涉及 001/003/006/012/035/040/042/044/046 等其他 P2 source_id。

manifest 第32-34行确认本 source_id 下 P2 行恰为：
- 第32行：P2,Q-2024朝阳期中-10
- 第33行：P2,Q-2024朝阳期中-7
- 第34行：P2,Q-2024朝阳期中-8

三行全部纳入；无遗漏；无额外行 ✅。

## 6. 文件位置硬规则

所有输出仅在 `claudecode_lane/p2_recheck/` 目录之下。无 Word/PDF/delivery/最终交付物 ✅。

## 7. 后续动作（非本任务范围）

- 后续 fusion patch 应将 framework_first_fusion P1 第527/751/806 行三处 Codex 复核标记按 source_insufficient 路径处理（保留卷面识别要素，但不输出确定性答案）。
- 若获得朝阳教研中心或官方教师版2024.11期中政治答案表，应由独立 patch 走 confirmed_with_patch 路径回填——不在本 P2G017 任务的输出范围内。

## 8. 终态声明

`P2G017_RECHECK_ACCEPTANCE: NOT_FINAL`

- exact row count 3 ✅
- patch count 3 ✅
- no Word/PDF/delivery ✅
- 输出全部在 claudecode_lane/p2_recheck/ ✅
- 三行 decision 均为 source_insufficient（未捏造答案） ✅
