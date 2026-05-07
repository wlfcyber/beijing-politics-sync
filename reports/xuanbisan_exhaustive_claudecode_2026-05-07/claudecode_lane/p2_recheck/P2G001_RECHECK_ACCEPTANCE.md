# P2G001_RECHECK_ACCEPTANCE: NOT_FINAL

> 状态：NOT_FINAL（小规模 source_id 级 P2 复核子产物，非交付件）。
> Scope: 仅 P2G001，单一 source_id `001_Desktop_2026模拟题_2026各区一模_2026顺义一模_试卷_试卷.pdf`。
> 不写 Word/PDF；不写 delivery/；不写 framework_first_fusion 终稿 patch 文件；输出仅在 `claudecode_lane/p2_recheck/`。

## 1. 输出件清单与计数

| 文件 | 路径 | 期望 | 实际 |
|------|------|------|------|
| P2G001_RECHECK_DECISIONS.csv | claudecode_lane/p2_recheck/P2G001_RECHECK_DECISIONS.csv | 1 表头 + 4 数据行 | 1 表头 + 4 数据行 ✅ |
| P2G001_RECHECK_PATCHES.jsonl | claudecode_lane/p2_recheck/P2G001_RECHECK_PATCHES.jsonl | 4 行 JSON | 4 行 JSON ✅ |
| P2G001_SOURCE_EVIDENCE.md | claudecode_lane/p2_recheck/P2G001_SOURCE_EVIDENCE.md | 已写 | 已写 ✅ |
| P2G001_RECHECK_ACCEPTANCE.md | claudecode_lane/p2_recheck/P2G001_RECHECK_ACCEPTANCE.md | 当前文件 | 已写 ✅ |
| P2G001_PROGRESS.md | claudecode_lane/p2_recheck/P2G001_PROGRESS.md | 已写 | 已写 ✅ |

精确行数声明：
- decision rows = 4（exact）
- patch rows = 4（exact）
- 四行的 question_id：Q-2026顺义一模-3 / Q-2026顺义一模-4 / Q-2026顺义一模-5 / Q-2026顺义一模-6。
- 无任何其他 P2 行混入。

## 2. CSV header 校验

实际表头：
`priority,question_id,parent_question_id,source_batch,type,framework_node,evidence_level,decision,decision_reason,source_evidence,patch_needed,can_enter_fusion`

与任务规定完全一致 ✅。

## 3. Allowed-decisions 校验

| 行 | decision | 是否在允许集 |
|----|----------|-------------|
| Q-2026顺义一模-3 | confirmed_with_patch | ✅ |
| Q-2026顺义一模-4 | confirmed_with_patch | ✅ |
| Q-2026顺义一模-5 | confirmed_with_patch | ✅ |
| Q-2026顺义一模-6 | confirmed_with_patch | ✅ |

允许集：confirmed / confirmed_with_patch / downgrade_to_index / source_insufficient / wrong_framework / block_from_student_body。四行均落在 confirmed_with_patch，符合允许集。

## 4. 评分硬规则一致性

- 'Verify stem/options and answer key before confirming choice-trap rows'：四行的 stem/options 已经过 paper.txt 行级核验（Q3 行25-33 / Q4 行34-42 / Q5 行43-63 / Q6 行64-73）；answer key 由 support 2026顺义一模细则.pptx SLIDE1 答案表逐题锁定（3=C, 4=A, 5=D, 6=A）✅。
- 'Use the manifest evidence_level exactly unless the source genuinely proves the row is misclassified'：四行均沿用 manifest 中的 evidence_level=B-choice-signal，未做任何上调下调 ✅。
- 'Do not invent options, answers, rubrics, or source files'：四行的 patched_material_signal/patched_answer_sentence 均严格基于 paper.txt + support 答案表的字面证据，未捏造任何选项、答案或规则 ✅。
- 'If answer evidence is unavailable, mark source_insufficient and can_enter_fusion=no'：本批次 answer evidence 在 support SLIDE1 答案表内可用且与 manifest framework_node 完全吻合，所以四行 confirmed_with_patch + can_enter_fusion=yes ✅。

## 5. Source_id 范围校验

仅包含 source_id=`001_Desktop_2026模拟题_2026各区一模_2026顺义一模_试卷_试卷.pdf` 的 P2 行。
不涉及 003/006/012/017/035/040/042/044/046 等其他 P2 source_id。

manifest 第67-70行确认本 source_id 下 P2 行恰为：
- 第67行：P2,Q-2026顺义一模-3
- 第68行：P2,Q-2026顺义一模-4
- 第69行：P2,Q-2026顺义一模-5
- 第70行：P2,Q-2026顺义一模-6

四行全部纳入；无遗漏；无额外行 ✅。

## 6. 文件位置硬规则

所有输出仅在 `claudecode_lane/p2_recheck/` 目录之下。无 Word/PDF/delivery/最终交付物 ✅。

## 7. Manifest framework_node ↔ support answer 一致性快照

| 题号 | manifest framework_node | manifest 注明 | support SLIDE1 答案 | 是否吻合 |
|------|-------------------------|--------------|---------------------|----------|
| Q3 | 辩证思维-整体性与独立性的对立统一 | ②正解（→C=②③） | 3 C | ✅ |
| Q4 | 推理-类比推理 | A正解 | 4 A | ✅ |
| Q5 | 创新思维-形象思维以感性形象为基本单元 | D正解 | 5 D | ✅ |
| Q6 | 创新思维-迁移和想象 | A正解 | 6 A | ✅ |

四行 framework_node 与 support 答案完全吻合，无需 wrong_framework。

## 8. 后续动作（非本任务范围）

- 后续 fusion patch 应将 framework_first_fusion P1 第75-83 / 233-239 / 241-247 / 501-507 行四处 Codex 复核标记按 confirmed_with_patch 路径处理，并将'需 Codex 回源复核' 改为'P2回源已闭合'，把 P2 证据（'2026顺义一模.pdf::Q[3-6]+2026顺义一模细则.pptx::SLIDE1答案表'）追加到各条目的 P0/P2 证据行——不在本 P2G001 任务的输出范围内。
- 本任务不写 Word/PDF/delivery/最终交付物，待后续 fusion 终稿 patch 流程接力。

## 9. 终态声明

`P2G001_RECHECK_ACCEPTANCE: NOT_FINAL`

- exact row count 4 ✅
- patch count 4 ✅
- no Word/PDF/delivery ✅
- 输出全部在 claudecode_lane/p2_recheck/ ✅
- 四行 decision 均为 confirmed_with_patch（基于 support SLIDE1 答案表逐题锁定）✅
- 四行 evidence_level 维持 manifest 原值 B-choice-signal ✅
- 四行 framework_node 与 support 答案完全吻合，无需 wrong_framework / block_from_student_body / source_insufficient ✅
