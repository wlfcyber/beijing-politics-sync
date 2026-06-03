# 旧预处理隔离说明

本轮 v2 不读取旧 `LEGAL_QUESTION_INDEX.csv`、`SUBJECTIVE_PREPROCESS.csv`、`CHOICE_PREPROCESS.csv` 作为证据输入。

隔离原因：

- 旧表曾把 `2024海淀一模第19题` 误标为 `reference_answer`，本地实际有正式细则层次表。
- 旧 `LEGAL_QUESTION_INDEX.csv` 中选择题的 `rubric_excerpt` 常串入同套主观题细则，不能作为逐题证据。
- 旧 `rubric_position=自动匹配第X题上下文` 只是粗截段，不足以证明题面和细则严格配对。
- 旧选择题错项句存在模板化推断，答案未锁定时不得生成实质错项判断。
