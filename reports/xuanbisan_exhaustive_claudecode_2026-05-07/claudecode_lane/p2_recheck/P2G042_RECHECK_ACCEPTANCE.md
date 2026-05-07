# P2G042_RECHECK_ACCEPTANCE: NOT_FINAL

> 状态：NOT_FINAL（小规模 source_id 级 P2 复核子产物，非交付件）。
> Scope: 仅 P2G042，单一 source_id `042_Desktop_2026模拟题_2026各区一模_2026丰台一模_试卷_试卷.pdf`。
> 不写 Word/PDF；不写 delivery/；不写 framework_first_fusion 终稿 patch 文件；输出仅在 `claudecode_lane/p2_recheck/`。

## 1. 输出件清单与计数

| 文件 | 路径 | 期望 | 实际 |
|------|------|------|------|
| P2G042_RECHECK_DECISIONS.csv | claudecode_lane/p2_recheck/P2G042_RECHECK_DECISIONS.csv | 1 表头 + 4 数据行 | 1 表头 + 4 数据行 ✅ |
| P2G042_RECHECK_PATCHES.jsonl | claudecode_lane/p2_recheck/P2G042_RECHECK_PATCHES.jsonl | 4 行 JSON | 4 行 JSON ✅ |
| P2G042_SOURCE_EVIDENCE.md | claudecode_lane/p2_recheck/P2G042_SOURCE_EVIDENCE.md | 已写 | 已写 ✅ |
| P2G042_RECHECK_ACCEPTANCE.md | claudecode_lane/p2_recheck/P2G042_RECHECK_ACCEPTANCE.md | 当前文件 | 已写 ✅ |
| P2G042_PROGRESS.md | claudecode_lane/p2_recheck/P2G042_PROGRESS.md | 已写 | 已写 ✅ |

精确行数声明：
- decision rows = 4（exact）
- patch rows = 4（exact）
- 四行的 question_id：Q-2026丰台一模-4 / Q-2026丰台一模-7 / Q-2026丰台一模-8 / Q-2026丰台一模-9。
- 无任何其他 P2 行混入。

## 2. CSV header 校验

实际表头（取自 P2G042_RECHECK_DECISIONS.csv 第 1 行）：
`priority,question_id,parent_question_id,source_batch,type,framework_node,evidence_level,decision,decision_reason,source_evidence,patch_needed,can_enter_fusion`

与任务规定完全一致 ✅。

## 3. Allowed-decisions 校验

| 行 | decision | 是否在允许集 |
|----|----------|-------------|
| Q-2026丰台一模-4 | source_insufficient | ✅ |
| Q-2026丰台一模-7 | source_insufficient | ✅ |
| Q-2026丰台一模-8 | source_insufficient | ✅ |
| Q-2026丰台一模-9 | source_insufficient | ✅ |

允许集：confirmed / confirmed_with_patch / downgrade_to_index / source_insufficient / wrong_framework / block_from_student_body。四行均落在 source_insufficient，符合允许集。

## 4. 评分硬规则一致性

- 'Verify stem/options and answer key before confirming choice-trap rows'：
  - 四行 stem 与四个选项**全部不可在 042 号源逐字核验**——042_*paper.txt 全文仅含 10 条 `===== PAGE n =====` 占位符（OCR 失败），唯一 support 文件 042_*support__2026丰台一模细则.pptx.txt 通篇仅覆盖 Q17-Q20 主观题阅卷细则；
  - answer key 四行**全部不可在 042 号源验证**；
  - 四行均**未 confirm/confirmed_with_patch**，全部按硬规则降为 source_insufficient ✅。
- 'Use the manifest evidence_level exactly unless the source genuinely proves the row is misclassified'：
  - 四行均沿用 manifest 中的 evidence_level=B-choice-signal，未做任何上调或下调；
  - source 缺失，未证伪也未证实 manifest 给出的 framework_node，未触发 wrong_framework 路径 ✅。
- 'Do not invent options, answers, rubrics, or source files'：
  - 四行的 patched_material_signal/patched_trigger_logic 均明确标注"基于 fusion P1 第 N 行已落体的识别正文，本轮源级未能在 042 号源内逐字核验"，未捏造任何题干、选项、答案、细则或源文件；
  - 四行的 patched_answer_sentence 均明确标注"源不足"，未输出确定性答案 ✅。
- 'If answer evidence is unavailable, mark source_insufficient and can_enter_fusion=no'：
  - 四行 answer evidence 均不可获得，全部标 source_insufficient + can_enter_fusion=no；
  - patch_needed=yes（保留卷面识别要素，待补充可靠答案后再回填），符合规则字面要求 ✅。

## 5. Source_id 范围校验

仅包含 source_id=`042_Desktop_2026模拟题_2026各区一模_2026丰台一模_试卷_试卷.pdf` 的 P2 行。
不涉及 001/003/006/012/017/035/040/044/046 等其他 P2 source_id。

manifest 中本 source_id 下 P2 行恰为四行（manifest 第 60-63 行）：
- P2,Q-2026丰台一模-4 (选必三导论-综合思维（②正解）)
- P2,Q-2026丰台一模-7 (推理-充分条件假言推理（B正解）)
- P2,Q-2026丰台一模-8 (推理-充分条件假言推理-否定后件式有效（②正解）)
- P2,Q-2026丰台一模-9 (判断-联言判断（D正解）)

四行全部纳入；无遗漏；无额外行 ✅。

## 6. 文件位置硬规则

所有输出仅在 `claudecode_lane/p2_recheck/` 目录之下。
- 无 Word（.docx）输出 ✅
- 无 PDF 输出 ✅
- 无 `delivery/` 目录写入 ✅
- 无 framework_first_fusion 终稿 patch 写入 ✅
- 无 fusion/ 子目录写入 ✅

## 7. fusion P1 体覆盖确认

| 行 | fusion P1 行号 | 现状 | 本轮源级复核动作 |
|----|--------------|------|----------------|
| Q4 | 第972-976 行 | 已含完整识别+陷阱+卷面句但带'需 Codex 回源复核'前置标签 | **未去除标签**——042 号源不含答案，无法去除；建议后续 fusion patch 维持复核标签或降级为 source_insufficient |
| Q7 | 第487-491 行 | 已含完整识别+陷阱+卷面句但带'需 Codex 回源复核'前置标签 | **未去除标签**——同上 |
| Q8 | 第479-483 行 | 已含完整符号化卷面句但带'需 Codex 回源复核'前置标签 | **未去除标签**——同上 |
| Q9 | 第856-860 行 | 已含完整识别+陷阱+卷面句但带'需 Codex 回源复核'前置标签 | **未去除标签**——同上 |

manifest 中四行 phase12_action=covered_by_74_review_body / phase12_category=already_in_74 在本轮源级复核中**未维持**——答案表证据缺失，按硬规则不应继续保留在 74-row review-only expanded body 中；建议后续 supervisor 综合裁定时把四行从 covered_by_74_review_body 重新落到 blocked_keep_out / answer_missing 状态，与本 source_insufficient 决策对齐。

## 8. 后续动作（非本任务范围）

- 补充 042 号源的可靠官方答案：丰台教研中心 2026 一模选择题答案表 / 教师版试卷扫描件二次 OCR / 讲评录音转写——任一到位即可重启 4 行 confirm 流程；
- 在补充到位前，fusion P1 第 479-483 / 487-491 / 856-860 / 972-976 行四节的'需 Codex 回源复核'标签应**保留**，或降级为'source_insufficient·暂不入学生正文'；
- manifest 状态建议从 covered_by_74_review_body 修正为 blocked_keep_out / answer_missing；
- 不在本 P2G042 任务的输出范围内。

## 9. 终态声明

`P2G042_RECHECK_ACCEPTANCE: NOT_FINAL`

- exact row count 4 ✅
- patch count 4 ✅
- no Word/PDF/delivery ✅
- 输出全部在 claudecode_lane/p2_recheck/ ✅
- 四行 decision 均为 source_insufficient（基于 042 paper.txt 仅含 10 条页头占位符 + support pptx 仅覆盖 Q17-Q20 主观题，stem/options/answer 全部不可逐字核验）✅
- evidence_level 与 manifest 完全一致（B-choice-signal × 4，未上调未下调）✅
- 仅 source_id=042 范围 ✅
- 未捏造任何题干、选项、答案、细则或源文件 ✅
- can_enter_fusion 四行均为 no（与 source_insufficient 决策对齐）✅
