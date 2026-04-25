# 主观题证据严格审计

## 审计结论

- 审计对象：`COVERAGE_MATRIX.csv` 中 45 条 main 主观题 + 1 条 lecture-scoring 主观题，共 46 条。
- 审计结果：46 条均已锚定到 rubric、marking-report、lecture-scoring、OCR-reviewed rubric scan 或 old-doc converted scoring text。
- 普通 reference-answer 没有作为主观题细则硬口径使用。
- 2025朝阳期末21、2026朝阳期末19 因 OCR 字距导致脚本初筛未命中，已用 `rg` 人工复核到原文中的评分/阅卷细则，并在审计 CSV 中标记为人工确认。

## 本次纠偏

- 主框架标题和正文已从“答题点”改为“术语包与细则硬口径”。
- 每个条目现在区分：`术语包/方向`、`细则硬口径`、`证据状态`。
- 没有写出细则硬口径的条目，均明确标注“仅作为术语包/方向，不是细则硬口径”。
- 乱码的术语速查表已重写，并在开头说明：速查表不是评分细则，只负责读出方向后的术语启动。

## 文件

- 审计 CSV：`MAIN_EVIDENCE_STRICT_AUDIT.csv`
- 主框架新文件：`C:\Users\Administrator\Desktop\飞哥的政治庄园\artifacts\选必一材料-触发-术语包与细则硬口径总框架.md`
- 术语速查：`C:\Users\Administrator\Desktop\飞哥的政治庄园\artifacts\选必一材料触发术语堆叠速查.md`