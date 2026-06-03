# V4 Classification Source-Clean Audit

## Bottom Line

- total questions: 65
- promotion counts: {'core_candidate': 53, 'low_frequency_container': 5, 'reference_only_container': 4, 'boundary_open_container': 3}
- node counts: {'先判后证': 10, '价值三层收束': 4, '责任成链': 12, '边界开放容器': 7, '程序证据救济': 8, '格子先行': 9, '创新竞争定性': 8, '新技术划边界': 7}
- rows with source-clean flags: 26

本轮把 `ask_text` 缺失、串入其他模块、answer_text 串题的行单独标记。标记不等于删除；它只表示学生成品可以用细则踩分点，但教师后台必须知道这些行需要回源补题面。

## Flagged Rows

- CC0019_2024_朝阳_一模_19 | derived_from_rubric_atom | keep_core | 原 ask_text 缺失，临时用首个细则原子定位。
- CC0077_2025_东城_一模_19 | derived_from_question_or_rubric | keep_core | 原 ask_text 缺失或污染，已从题干/细则邻近句反推。
- CC0084_2025_东城_二模_19 | derived_from_question_or_rubric | keep_core | 原 ask_text 缺失或污染，已从题干/细则邻近句反推。
- CC0092_2025_东城_期末_19_1 | derived_from_rubric_atom | keep_core | 原 ask_text 缺失，临时用首个细则原子定位。
- CC0131_2025_房山_一模_19 | derived_from_question_or_rubric | keep_core | 原 ask_text 缺失或污染，已从题干/细则邻近句反推。
- CC0157_2025_朝阳_期末_20 | derived_from_question_or_rubric | keep_core | 原 ask_text 缺失或污染，已从题干/细则邻近句反推。
- CC0180_2025_海淀_期末_20 | derived_from_question_or_rubric|answer_text_contains_other_questions | keep_core | 原 ask_text 缺失或污染，已从题干/细则邻近句反推。
- CC0181_2025_海淀_期末_21 | answer_text_contains_other_questions | keep_core | 创新竞争定性信号。
- CC0189_2025_石景山_一模_20 | derived_from_question_or_rubric | keep_core | 原 ask_text 缺失或污染，已从题干/细则邻近句反推。
- CC0195_2025_西城_一模_20 | derived_from_question_or_rubric | keep_core | 原 ask_text 缺失或污染，已从题干/细则邻近句反推。
- CC0213_2025_门头沟_一模_20 | derived_from_question_or_rubric | keep_core | 原 ask_text 缺失或污染，已从题干/细则邻近句反推。
- CC0214_2025_门头沟_一模_20_2 | derived_from_question_or_rubric | keep_core | 原 ask_text 缺失或污染，已从题干/细则邻近句反推。
- CC0245_2026_东城_期末_18_2 | derived_from_rubric_atom | keep_core | 原 ask_text 缺失，临时用首个细则原子定位。
- CC0251_2026_丰台_一模_20 | answer_text_contains_other_questions | keep_core | 原 ask 被等级表污染，核心是法院判决论述。
- CC0254_2026_丰台_二模_18 | answer_text_contains_other_questions | low_frequency_container | formal 但低频单例，进入全量容器。
- CC0276_2026_房山_二模_17 | derived_from_rubric_atom|boundary_open_container | boundary_open_container | 原 ask_text 缺失，临时用首个细则原子定位。
- CC0277_2026_房山_二模_18 | derived_from_question_or_rubric | keep_core | 原 ask_text 缺失或污染，已从题干/细则邻近句反推。
- CC0317_2026_海淀_期末_18 | derived_from_rubric_atom | keep_core | 原 ask_text 缺失，临时用首个细则原子定位。
- CC0318_2026_海淀_期末_18_2 | derived_from_rubric_atom | keep_core | 原 ask_text 缺失，临时用首个细则原子定位。
- CC0319_2026_海淀_期末_19 | derived_from_rubric_atom | keep_core | 原 ask_text 缺失，临时用首个细则原子定位。
- CC0325_2026_石景山_一模_18 | derived_from_question_or_rubric | keep_core | 原 ask_text 缺失或污染，已从题干/细则邻近句反推。
- CC0353_2026_西城_期末_17 | derived_from_rubric_atom | reference_only_container | 原 ask_text 缺失，临时用首个细则原子定位。
- CC0364_2026_通州_期末_19_1 | reconstructed_from_legal_rubric|ask_module_contamination | core_candidate | 原 ask_text 串入《逻辑与思维》小问。
- CC0305_2026_海淀_一模_18_3 | derived_from_rubric_atom | keep_core | 原 ask_text 缺失，临时用首个细则原子定位。
- CC0380_2026_顺义_二模_18_2 | derived_from_rubric_atom|ask_module_contamination|boundary_open_container | boundary_open_container | 原 ask_text 缺失，临时用首个细则原子定位。
- RECOVER_2026_西城_二模_18_3 | boundary_open_container | boundary_open_container | 综合/开放边界，保留法律点但不升核心。
