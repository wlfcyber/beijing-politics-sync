# DEVELOPMENT_PLAN

## P0 门禁与控制文件

- status: completed
- objective: 完成项目总管、技能、小本本和 run 控制文件，避免无账本处理资料。
- output: `00_control/*`

## P1 题源清单

- status: completed
- objective: 扫描本机可见 2024-2026 北京区卷、答案、细则、讲评等，生成源文件清单。
- output: `01_source_inventory/source_inventory.csv`

## P2 缓存优先与文本候选

- status: completed
- objective: 优先检查项目内可复用文本缓存；缺失或不可靠时回源抽取文本。
- output: `02_text_cache/cache_manifest.csv`, `03_question_index/question_candidates.csv`

## P3 三模块初分

- status: completed_with_blockers
- objective: 按题/小问初分 B2、B3、B4_CULTURE，并标出边界排除与待人工复核。
- output: `04_module_classification/module_classification_matrix.csv`

## P4 交叉核验

- status: completed_with_blockers
- objective: 检查重复题、缺源题、未分类题、2026 石景山期末排除、选择题/主观题分别统计。
- output: `05_reports/classification_readiness_report.md`

## P5 总管验收

- status: completed
- objective: 对控制账本、分类矩阵和报告一致性做 Governor 检查；未闭环不得写 TASK_COMPLETE。
- output: `00_control/GOVERNOR_CHECKLIST.md`, `00_control/FINAL_ACCEPTANCE_REPORT.md`

## P6 最终答案键闭合

- status: completed
- objective: 对最后 3 条答案键依赖的混合选择题回源查答案，按正确项拆出目标组件并关闭父题余项。
- output: `00_control/FINAL_ANSWER_KEY_CLOSURE_COVERAGE_MATRIX.csv`, `05_reports/final_answer_key_closure_report.md`

## P7 Fable5 源缓存交接

- status: superseded_by_p9_completion
- objective: 自查并补齐可供 Fable5 直接读取的源文件级 AI-readable 缓存，避免逐个 OCR PDF/PPTX；同时标清参考答案不得作细则。
- output: `06_fable5_source_cache/FABLE5_READ_ME_FIRST.md`, `06_fable5_source_cache/fable5_ai_readable_source_cache.jsonl`

## P8 期中/期末身份与 OCR 文化补丁

- status: completed
- objective: 修复 2026 海淀、2026 朝阳以及 2025 海淀期中/期末源层与矩阵层身份错位；对朝阳期末与海淀期末扫描源补 OCR，并继续按用户规则抽离题目和细则中的文化部分。
- output: `00_control/HAIDIAN_2026_IDENTITY_OCR_CULTURE_PATCHED_COVERAGE_MATRIX.csv`, `00_control/CHAOYANG_2026_IDENTITY_OCR_CULTURE_PATCHED_COVERAGE_MATRIX.csv`

## P9 Fable5 全源缓存闭合

- status: completed_with_ocr_exactness_boundary
- objective: 将 `source_inventory.csv` 的 194 个唯一 sha 全部对齐进 Fable5 AI-readable 源缓存；补齐缺登记源、OCR 占位源和硬规则排除源，确保 Fable5 不再逐个打开/OCR 原 PDF、DOC、PPTX。
- output: `06_fable5_source_cache/FABLE5_READ_ME_FIRST.md`, `06_fable5_source_cache/fable5_ai_readable_source_cache.jsonl`, `05_reports/fable5_missing_source_cache_completion_report.md`
