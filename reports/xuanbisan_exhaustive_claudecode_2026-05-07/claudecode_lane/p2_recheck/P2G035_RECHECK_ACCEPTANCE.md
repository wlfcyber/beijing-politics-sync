# P2G035_RECHECK_ACCEPTANCE: NOT_FINAL

> 状态：NOT_FINAL（小规模 source_id 级 P2 复核子产物，非交付件）。
> Scope: 仅 P2G035，单一 source_id `035_GaokaoPolitics_2025各区模拟题_2025各区一模_2025顺义一模_2025北京顺义高三一模政治_教师版_.pdf`。
> 不写 Word/PDF；不写 delivery/；不写 framework_first_fusion 终稿 patch 文件；输出仅在 `claudecode_lane/p2_recheck/`。

## 1. 输出件清单与计数

| 文件 | 路径 | 期望 | 实际 |
|------|------|------|------|
| P2G035_RECHECK_DECISIONS.csv | claudecode_lane/p2_recheck/P2G035_RECHECK_DECISIONS.csv | 1 表头 + 3 数据行 | 1 表头 + 3 数据行 ✅ |
| P2G035_RECHECK_PATCHES.jsonl | claudecode_lane/p2_recheck/P2G035_RECHECK_PATCHES.jsonl | 3 行 JSON | 3 行 JSON ✅ |
| P2G035_SOURCE_EVIDENCE.md | claudecode_lane/p2_recheck/P2G035_SOURCE_EVIDENCE.md | 已写 | 已写 ✅ |
| P2G035_RECHECK_ACCEPTANCE.md | claudecode_lane/p2_recheck/P2G035_RECHECK_ACCEPTANCE.md | 当前文件 | 已写 ✅ |
| P2G035_PROGRESS.md | claudecode_lane/p2_recheck/P2G035_PROGRESS.md | 已写 | 已写 ✅ |

精确行数声明：
- decision rows = 3（exact）
- patch rows = 3（exact）
- 三行的 question_id：Q-2025顺义一模-5 / Q-2025顺义一模-6 / Q-2025顺义一模-7。
- 无任何其他 P2 行混入。

## 2. CSV header 校验

实际表头：
`priority,question_id,parent_question_id,source_batch,type,framework_node,evidence_level,decision,decision_reason,source_evidence,patch_needed,can_enter_fusion`

与任务规定完全一致 ✅。

## 3. Allowed-decisions 校验

| 行 | decision | 是否在允许集 |
|----|----------|-------------|
| Q-2025顺义一模-5 | confirmed_with_patch | ✅ |
| Q-2025顺义一模-6 | confirmed_with_patch | ✅ |
| Q-2025顺义一模-7 | confirmed_with_patch | ✅ |

允许集：confirmed / confirmed_with_patch / downgrade_to_index / source_insufficient / wrong_framework / block_from_student_body。三行均落在 confirmed_with_patch，符合允许集。

## 4. 评分硬规则一致性

- 'Verify stem/options and answer key before confirming choice-trap rows'：
  - 三行的 stem 与四个选项已在 035_*paper.txt 行49-53（Q5）/行54-67（Q6）/行68-93（Q7）逐字核验；
  - answer key 已在 035_*paper.txt 行265-266 paper 答案表 + 035_*support__2025顺义一模细则.docx.txt 行1-2 顺义区参考答案表两处分别核验：
    - Q5：paper '5 B' + support '5.B' → 双源一致锁定 B；
    - Q6：paper '6 A' + 教师版【详解】行319-332 ①②正确/③④错误的逐项推演 + manifest framework_node '①正解'（仅与 A=①② 一致）三方锁定 A；support 行1 '6.C' 为同源 .docx 单行答案抄写笔误（详见 P2G035_SOURCE_EVIDENCE.md 第3.3-3.5 节与第6节三方对照表）；
    - Q7：paper '7 A' + support '7.A' → 双源一致锁定 A；
  - 全部满足'choice_trap 复核须先验 stem/options 与 answer key'硬规则后再 confirm ✅。
- 'Use the manifest evidence_level exactly unless the source genuinely proves the row is misclassified; explain any exception'：
  - 三行均沿用 manifest 中的 evidence_level=B-choice-signal，未做任何上调下调；
  - source 未证明任何一行被错误分级；本批未触发 evidence_level 例外说明 ✅。
- 'Do not invent options, answers, rubrics, or source files'：
  - 三行的 patched_answer_sentence 全部以 035_*paper.txt 答案表 + 教师版【详解】为权威源；Q5/Q7 另引 035_*support 顺义区参考答案表作双源对照；
  - 未捏造任何选项/答案/细则/源文件；Q6 的 support 笔误识别基于教师版【详解】 + paper 答案表 + manifest framework_node 三方对照与同源 .docx 在其余14题答案上的完全一致性，并未替换或修改 source 原文，仅在 source_evidence 字段如实记录 ✅。
- 'If answer evidence is unavailable, mark source_insufficient and can_enter_fusion=no'：
  - 三行 answer evidence 均充分（paper 答案表 + 教师版【详解】 + Q5/Q7 双源 support 答案表对照），全部 confirmed_with_patch + can_enter_fusion=yes，符合规则的反面（即 evidence 充分时不应误标 source_insufficient）✅。

## 5. Source_id 范围校验

仅包含 source_id=`035_GaokaoPolitics_2025各区模拟题_2025各区一模_2025顺义一模_2025北京顺义高三一模政治_教师版_.pdf` 的 P2 行。
不涉及 001/003/006/012/017/040/042/044/046 等其他 P2 source_id。

manifest 中本 source_id 下 P2 行恰为：
- P2,Q-2025顺义一模-5（判断-联言判断的矛盾命题（B正解））
- P2,Q-2025顺义一模-6（判断-性质判断主项识别（①正解））
- P2,Q-2025顺义一模-7（推理-三段论-大项不当扩大（A正解，硬样本：硬规则§十九））

三行全部纳入；无遗漏；无额外行 ✅。

（manifest 中本 source_id 下另有 3 条 P1 行 Q-2025顺义一模-17-1 三个 framework_node 变体，但优先级为 P1 不在本任务范围；本批严格只取 priority=P2 的 3 行。）

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
| Q5 | 第848-852 行（## 判断 / ### 判断-联言判断的矛盾命题（B正解）） | 已含完整识别+陷阱+卷面句但带'需 Codex 回源复核'前置标签 | 锁定答案 B（paper 答案表 + support 顺义区参考答案双源一致 + 教师版【详解】德摩根推演），后续 patch 应去除复核标签 |
| Q6 | 第840-844 行（## 判断 / ### 判断-性质判断主项识别（①正解）） | 已含完整识别+陷阱+卷面句但带'需 Codex 回源复核'前置标签 | 锁定答案 A（paper 答案表 + 教师版【详解】 + manifest framework_node 三方一致；support 行1 '6.C' 为同源 .docx 单行抄写笔误），后续 patch 应去除复核标签并在卷面句末尾保留 'support 行1 6.C 为同源 .docx 单行抄写笔误' 的简短源端注 |
| Q7 | 第471-475 行（## 推理 / ### 推理-三段论-大项不当扩大（A正解，硬样本：硬规则§十九）） | 已含完整识别+陷阱+卷面句但带'需 Codex 回源复核'前置标签 | 锁定答案 A（paper 答案表 + support 顺义区参考答案双源一致 + 教师版【详解】大项不当扩大推演），后续 patch 应去除复核标签并在硬规则§十九对应章节标注本题为该规则的核心硬样本 |

## 8. 后续动作（非本任务范围）

- 后续 fusion patch 应将 framework_first_fusion P1 第471/840/848 行三处'需 Codex 回源复核'前置标签按 confirmed_with_patch 路径处理（去除标签，保留正文，并按各题需要补 support 笔误简短源端注 / 硬规则§十九硬样本标注）；
- 三行均可从 needs_codex_recheck=yes 状态转入正常学生体保留路径（can_enter_fusion=yes）；
- 不在本 P2G035 任务的输出范围内。

## 9. 终态声明

`P2G035_RECHECK_ACCEPTANCE: NOT_FINAL`

- exact row count 3 ✅
- patch count 3 ✅
- no Word/PDF/delivery ✅
- 输出全部在 claudecode_lane/p2_recheck/ ✅
- 三行 decision 均为 confirmed_with_patch（基于 paper 答案表 + 教师版【详解】 + Q5/Q7 双源 support 答案表对照 + Q6 的 support 笔误三方对照识别，未捏造答案）✅
- evidence_level 与 manifest 完全一致（B-choice-signal × 3）✅
- 仅 source_id=035 范围 ✅
