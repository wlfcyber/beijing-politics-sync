# 全量试卷独立重跑任务书

创建时间：2026-04-29
工作目录：`C:\bp_sync_visible\reports\full_all_suites_independent_rerun_2026-04-29`
套卷数：56。正式题源清单 56 条；其中 55 条来自 suite bundle，`2024门头沟一模` 来自分类汇编线索 + 补源答案 PDF。

## 目标

按严格证据口径重新跑 2024-2026 北京区卷全量题源，重建：

- 必修四哲学材料-知识触发链
- 必修四文化材料-知识触发链
- 选择题错肢/正确项触发
- 题源覆盖与缺口清单

## 本轮不是

- 不是直接宣布旧三大文件 PASS。
- 不是把旧 artifact 合并进新结果。
- 不是只修几个已知错误。

## 优先级

主观题 > 选择题；海淀 > 西城 > 东城 > 朝阳 > 丰台 > 其他区。

## 验收门槛

- `COVERAGE_MATRIX.csv` 56 套都不是 pending。
- 每个 `included` 条目都有证据摘录和来源路径。
- 所有 `reference-only/source-missing/ocr-needed/module-boundary-excluded` 都有原因。
- governor 明确列出 PASS/REJECT/NEED_EVIDENCE。
