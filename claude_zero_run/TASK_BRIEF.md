# Claude Zero Run Task Brief

- run_id: claude_zero_run
- created_at: 2026-05-26 03:00 Asia/Shanghai
- workspace: /Users/wanglifei/Desktop/北京高考政治
- executor: ClaudeCode independent lane
- supervisor: Codex

## Objective

从 0 重跑选必二《法律与生活》主观题框架生长工程，产出一份“前面框架穷尽，后面全核心锁源题穷尽”的飞哥课堂版框架。

## User-Specified Output Root

All new artifacts for this run must be written under:

`/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/`

## Hard Boundary

- 只研究主观题。
- 旧 v8/v9/v10/v11/v12 只能作反面检查和风格对照，不得继承题链、分类或结论。
- 旧框架只用于学习表达风格，不作为选必二证据来源。
- 不扩大到旧 65/70 口径。
- 不纳入 pending 三题，除非本轮重新找到原题、设问、材料和正式给分口径。
- OPEN_OR_REFERENCE 只能放参考容器，不能支撑核心框架。
- 不写 DOCX、PDF、TASK_COMPLETE、FINAL_PASS。

## Required Final Artifacts

- `00_飞哥旧框架风格DNA.md`
- `01_source_manifest.csv`
- `01_processing_log.md`
- `01_failed_files.csv`
- `02_candidate_subjective_law_questions.csv`
- `02_uncertain_or_boundary_cases.md`
- `source_lock_cards/{question_id}.md`
- `03_source_lock_index.csv`
- `04_corpus_status_report.md`
- `04_core_questions.csv`
- `04_reference_questions.csv`
- `04_pending_or_excluded.csv`
- `05_framework_exhaustion_map.csv`
- `05_framework_exhaustion_map.md`
- `06_上篇_选必二法律主观题穷尽框架_飞哥版.md`
- `07_下篇_全题题链_飞哥版.md`
- `07_下篇_全题题链_飞哥版.csv`
- `08_开放容器与待补题.md`
- `09_框架_题目_覆盖矩阵.csv`
- `10_QA_acceptance.md`

## Acceptance Label

The only allowed QA labels are:

- `CLAUDE_ZERO_CONDITIONAL_PASS`
- `FAIL`

