# Phase10 Same-Type Index Style Decision

- decision: `student_readable_titles_in_body_raw_qids_in_control_matrix`
- reason: 学生正文不再显示 raw QID；同类题索引改成“年份 + 区 + 阶段 + 题号/小问”的可读标题。
- traceability: `phase10_polish_control_matrix.csv` 保留 `question_id`、`same_type_ids` 与 `same_type_visible`。
- scope_lock: 同类题只作为索引，未进入 29 行的题不得展开答案或解析。
