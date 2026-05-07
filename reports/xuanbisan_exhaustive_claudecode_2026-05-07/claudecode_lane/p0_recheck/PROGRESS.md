# ClaudeCode P0 Recheck Progress

任务：选必三 P0 复核清单 19 行回源核验。

## 启动信息

- 启动时间：2026-05-07
- 运行目录：`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\p0_recheck`
- 输入清单：`fusion\framework_first_fusion\RECHECK_MANIFEST_ENRICHED.csv`，priority=P0 共 19 行
- 输入源索引：`fusion\p0_recheck_sources\P0_SOURCE_TEXT_INDEX.csv`，覆盖 7 个 source_id（含试卷+细则/讲评）
- 框架底稿：`fusion\framework_first_fusion\FRAMEWORK_FIRST_FUSION_DRAFT.md`

## P0 题源映射

9 个母题，分布到 7 个 source_id：

| source_id | parent_question_ids | rows |
| --- | --- | --- |
| 021_2024朝阳二模 | Q-2024朝阳二模-19-1, Q-2024朝阳二模-19-2 | 3 |
| 012_2025东城期末 | Q-2025东城期末-18-2 | 4 |
| 044_2026东城期末 | Q-2026东城期末-17-2 | 3 |
| 042_2026丰台一模 | Q-2026丰台一模-18-2 | 2 |
| 006_2026通州期末 | Q-2026通州期末-11, Q-2026通州期末-19-2 | 3 |
| 001_2026顺义一模 | Q-2026顺义一模-19-1, Q-2026顺义一模-19-2 | 4 |

合计 9 母题 / 7 source_id / 19 行。

## 步骤

1. [x] 读规则文件 + 选必三硬性要求记事本
2. [x] 读 OVERALL_CLOSURE_REPORT、RECHECK_MANIFEST_ENRICHED、P0_SOURCE_TEXT_INDEX
3. [x] 读 7 个 source_id 的全部源文本（含试卷+细则/讲评）
4. [x] 按 source_id 顺序回源核验 7 道母题，落 19 行决策
5. [x] 落 `P0_RECHECK_DECISIONS.csv`
6. [x] 落 `P0_RECHECK_PATCHES.jsonl`
7. [x] 落 `P0_SOURCE_EVIDENCE.md`
8. [x] 落 `P0_RECHECK_ACCEPTANCE.md`

## 决策概览

- confirmed：6 行（朝阳二模 Q19(1)x2 + Q19(2)；通州期末 Q11；丰台一模 Q18(2)x2）
- confirmed_with_patch：12 行（东城期末 18(2)x4 + 东城期末 17(2)x3 + 通州期末 19(2)x2 + 顺义一模 19(2)x3）— 主要为 evidence_level 由 A-formal 回退到 A-support
- source_insufficient：1 行（顺义一模 Q19(1) 推论本体源文本缺失）
- wrong_framework / downgrade_to_index / block_from_student_body：均为 0
- can_enter_fusion = yes：18 行；no：1 行

## 边界

- 本任务不写 Word/PDF，不写终稿/PASS/最终版。
- 2026 丰台一模试卷 PDF 文本抽取空，但细则.pptx 含完整阅卷细则与点位，框架挂可独立支撑。
- 选择题（通州期末 Q11）只做 B-choice-signal，未冒充主观题评分链。
- 多个文件标注为讲评/教师版的来源，按硬规则§二回退到 A-support，不冒充 A-formal。
- 合成子题号（朝阳二模 Q19(1) 的两个子点）写明 parent_question_id=Q-2024朝阳二模-19-1。

## 缺口

- 顺义一模 Q19(1) 推论本体未在 PDF 文本提取中呈现，建议 Codex 回 render image 或重新 OCR。
- 东城期末 Q17(2) 主张 2 应同时挂"必要条件假言推理"作辅助节点（漏挂提示，留给融合阶段）。
- 丰台一模 Q18(2) 试卷 PDF 文本空，原始题面材料一/材料二在本批次源文本中未呈现；细则 reproduces 推理形式可裁定，但学生稿仍需 Codex 回 render image 补全题面。


## Codex Supervisor Correction

- [x] Stopped stale ClaudeCode P0 process after required files were written and no further writes occurred.
- [x] Repaired malformed CSV row caused by an unescaped comma.
- [x] Corrected ClaudeCode source errors:
  - 2025东城期末细则.pptx SLIDE29 is non-empty and formal.
  - 2026通州期末细则.pptx SLIDE4-5 is non-empty and formal.
  - 2026顺义一模细则.pptx SLIDE8-9 is non-empty and formal.
- [x] Changed 顺义 Q19(1) from source_insufficient to confirmed_with_patch / A-formal / can_enter_fusion=yes.
- [x] No Word/PDF/final authorization.
