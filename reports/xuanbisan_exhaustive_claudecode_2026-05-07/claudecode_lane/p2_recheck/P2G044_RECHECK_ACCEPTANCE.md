# P2G044_RECHECK_ACCEPTANCE: NOT_FINAL

> 状态：NOT_FINAL（小规模 source_id 级 P2 复核子产物，非交付件）。
> Scope: 仅 P2G044，单一 source_id `044_Desktop_2026模拟题_2026各区期末和期中_2026东城期末_试卷_试卷.pdf`。
> 不写 Word/PDF；不写 delivery/；不写 framework_first_fusion 终稿 patch 文件；输出仅在 `claudecode_lane/p2_recheck/`。

## 1. 输出件清单与计数

| 文件 | 路径 | 期望 | 实际 |
|------|------|------|------|
| P2G044_RECHECK_DECISIONS.csv | claudecode_lane/p2_recheck/P2G044_RECHECK_DECISIONS.csv | 1 表头 + 2 数据行 | 1 表头 + 2 数据行 ✅ |
| P2G044_RECHECK_PATCHES.jsonl | claudecode_lane/p2_recheck/P2G044_RECHECK_PATCHES.jsonl | 2 行 JSON | 2 行 JSON ✅ |
| P2G044_SOURCE_EVIDENCE.md | claudecode_lane/p2_recheck/P2G044_SOURCE_EVIDENCE.md | 已写 | 已写 ✅ |
| P2G044_RECHECK_ACCEPTANCE.md | claudecode_lane/p2_recheck/P2G044_RECHECK_ACCEPTANCE.md | 当前文件 | 已写 ✅ |
| P2G044_PROGRESS.md | claudecode_lane/p2_recheck/P2G044_PROGRESS.md | 已写 | 已写 ✅ |

精确行数声明：
- decision rows = 2（exact）
- patch rows = 2（exact）
- 两行的 question_id：Q-2026东城期末-6 / Q-2026东城期末-7。
- 无任何其他 P2 行混入。

## 2. CSV header 校验

实际表头：
`priority,question_id,parent_question_id,source_batch,type,framework_node,evidence_level,decision,decision_reason,source_evidence,patch_needed,can_enter_fusion`

与任务规定完全一致 ✅。

## 3. Allowed-decisions 校验

| 行 | decision | 是否在允许集 |
|----|----------|-------------|
| Q-2026东城期末-6 | confirmed_with_patch | ✅ |
| Q-2026东城期末-7 | confirmed_with_patch | ✅ |

允许集：confirmed / confirmed_with_patch / downgrade_to_index / source_insufficient / wrong_framework / block_from_student_body。两行均落在 confirmed_with_patch，符合允许集。

## 4. 评分硬规则一致性

- 'Verify stem/options and answer key before confirming choice-trap rows'：
  - 两行的 stem 与四个选项已在 044_*paper.txt 行52-62（Q6）/行63-73（Q7）逐字核验；
  - answer key 已在 044_*paper.txt 行251-252 答案表逐字核验：6=B / 7=A；
  - Q6 还另有 044_*support__2026东城期末细则.pptx Slide 78 三段论结构图 + Slide 82 文字版排错双重佐证；
  - Q7 还另有 044_*support__2026东城期末细则.pptx Slide 2 矛盾关系图 + Slide 3 文字版排错双重佐证；
  - 全部满足'choice_trap 复核须先验 stem/options 与 answer key'硬规则后再 confirm ✅。
- 'Use the manifest evidence_level exactly unless the source genuinely proves the row is misclassified'：
  - 两行均沿用 manifest 中的 evidence_level=B-choice-signal，未做任何上调下调；
  - source 未证明任何一行被错误分级 ✅。
- 'Do not invent options, answers, rubrics, or source files'：
  - 两行的 patched_answer_sentence 全部以 paper.txt 答案表为唯一答案锁定源；细则 pptx 提供官方排错佐证；
  - 未捏造任何选项/答案/细则/源文件 ✅。
- 'If answer evidence is unavailable, mark source_insufficient and can_enter_fusion=no'：
  - 两行 answer evidence 均充分（paper.txt 答案表 + 细则 pptx Slide 78/82 与 Slide 2/3 双重佐证），全部 confirmed_with_patch + can_enter_fusion=yes，符合规则的反面（即 evidence 充分时不应误标 source_insufficient）✅。

## 5. Source_id 范围校验

仅包含 source_id=`044_Desktop_2026模拟题_2026各区期末和期中_2026东城期末_试卷_试卷.pdf` 的 P2 行。
不涉及 001/003/006/012/017/035/040/042/046 等其他 P2 source_id。

manifest 中本 source_id 下 P2 行恰为：
- P2,Q-2026东城期末-6 (推理>演绎推理>三段论保真+必要条件假言判断)
- P2,Q-2026东城期末-7 (推理>逻辑思维基本要求>矛盾律 + 演绎推理>充分条件假言推理)

两行全部纳入；无遗漏；无额外行 ✅。

注：本 source_id 下 manifest 还存在 3 行 P0（Q-2026东城期末-17-2 跨三个 framework_node），均为 main_thinking 主观题，已在 P0 复核闭合，不属于本 P2 任务范围。

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
| Q6 | 第653-663 行 | 已含完整识别+陷阱+卷面句但带'需 Codex 回源复核'前置标签 | 锁定答案 B（paper 答案表 6=B + 细则 pptx Slide 78 三段论结构图 + Slide 82 文字版排错），后续 fusion patch 应去除复核标签 |
| Q7 | 第735-745 行 | 已含完整识别+陷阱+卷面句但带'需 Codex 回源复核'前置标签 | 锁定答案 A（paper 答案表 7=A + 细则 pptx Slide 2 矛盾关系图 + Slide 3 文字版排错），后续 fusion patch 应去除复核标签 |

manifest 中两行均标 phase12_action=covered_by_74_review_body / phase12_category=already_in_74，与 fusion P1 第653-663 / 第735-745 行落体一致——本轮源级复核仅为已落体内容补充答案锁定证据，未改写已有识别正文。

## 8. 后续动作（非本任务范围）

- 后续 fusion patch 应将 framework_first_fusion P1 第655 行（Q6）与第737 行（Q7）两处'需 Codex 回源复核'前置标签按 confirmed_with_patch 路径处理（去除标签，保留正文）；
- 两题已在 74-row review-only expanded body 中（manifest phase12_action=covered_by_74_review_body），维持现状或视后续需要并入正常学生体；
- 不在本 P2G044 任务的输出范围内。

## 9. 终态声明

`P2G044_RECHECK_ACCEPTANCE: NOT_FINAL`

- exact row count 2 ✅
- patch count 2 ✅
- no Word/PDF/delivery ✅
- 输出全部在 claudecode_lane/p2_recheck/ ✅
- 两行 decision 均为 confirmed_with_patch（基于 paper 答案表 + 细则 pptx 三重证据，未捏造答案）✅
- evidence_level 与 manifest 完全一致（B-choice-signal × 2）✅
- 仅 source_id=044 范围 ✅
