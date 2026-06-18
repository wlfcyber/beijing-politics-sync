# 必修二三与必修四文化题源分类准备 TASK_BRIEF

- run_id: 必修二三与必修四文化_题源分类准备_20260617_1301
- created_at: 2026-06-17 13:01 +08:00
- workspace: /Users/wanglifei/Desktop/北京高考政治
- task_type: future-book-preparation / source-forward classification

## 用户目标

为后续制作三条宝典线提前整理题源：

1. 必修二《经济与社会》
2. 必修三《政治与法治》
3. 必修四《哲学与文化》中的文化部分

本 run 的目标不是生成学生版宝典，而是把现有三年北京区级模拟题、答案、细则、讲评材料等按试卷和题目先做可复用分类，形成后续宝典可直接接手的题源账本、逐题索引和模块分类矩阵。

## 核心交付物

- `01_source_inventory/source_inventory.csv`: 三年区卷与配套答案/细则/讲评源文件清单。
- `03_question_index/question_candidates.csv`: 从题源或缓存中抽出的逐题候选索引。
- `04_module_classification/module_classification_matrix.csv`: 必修二、必修三、必修四文化及边界排除分类矩阵。
- `05_reports/classification_readiness_report.md`: 后续三条宝典线接手报告。
- `00_control/SOURCE_LEDGER.csv` and `00_control/COVERAGE_MATRIX.csv`: 总管可读控制账本。

## 范围边界

Included modules:

- B2: 必修二《经济与社会》
- B3: 必修三《政治与法治》
- B4_CULTURE: 必修四《哲学与文化》文化部分

Excluded or boundary modules:

- B4_PHILOSOPHY: 必修四哲学部分，只作为边界排除，不进入文化准备包。
- B1: 必修一《中国特色社会主义》
- XB1: 选择性必修一《当代国际政治与经济》
- XB2: 选择性必修二《法律与生活》
- XB3: 选择性必修三《逻辑与思维》
- UNKNOWN_OR_MIXED: 无法仅凭当前题面/答案判断的混合或待回源题。

## 必守教训

v1 哲学宝典失败的根因之一是用条目数、厚度、模型摘要替代唯一题库覆盖。此 run 必须从题源清单向逐题矩阵推进：先确认源文件，再确认唯一题/小问，再确认模块去向。任何“全覆盖”结论都必须能从矩阵反查。

## 当前最小步骤

先建立控制文件与硬规则，再扫描源文件形成 `source_inventory.csv`，不得跳过账本直接写正文或下结论。
