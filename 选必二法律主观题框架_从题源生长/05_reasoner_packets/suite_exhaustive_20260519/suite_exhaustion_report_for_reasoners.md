# Suite Exhaustion Report - 20260519

- generated_at: 2026-05-19T15:25:33+08:00
- source base: boundary_recovered_20260519, 56 rows
- new core recoveries: 10
- suite-exhaustive core corpus rows: 66
- evidence_level_counts: {"formal": 61, "reference_only": 5}
- suite_count: 63
- suite_status_counts: {"has_suite_exhaustive_core_rows": 57, "no_law_subjective_confirmed": 2, "midterm_mixed_law_reference_not_core": 1, "stage_mapping_conflict_mixed_review": 1, "stage_mapping_conflict": 1, "special_user_excluded_or_source_blocked": 1}

## Decision

The previous 56-row package is not sufficient for GPT Pro / Claude Opus framework generation. This run adds the clearly missed core law subjective questions and creates a suite-level exhaustion matrix. GPT/Claude framework input must use this suite-exhaustive package or a later package, not the 53/56-row packages.

## Newly Recovered Core Questions

- `RECOVER_2024_东城_一模_19`: 2024东城一模 Q19; formal; locator: paper F0011 rendered page_009; answer F0010 page_001; rubric F0009 slides 57-62
- `RECOVER_2024_东城_二模_19_1`: 2024东城二模 Q19(1); formal; locator: paper F0043 page_009; rubric F0037 lines 30-45
- `RECOVER_2024_东城_二模_19_2`: 2024东城二模 Q19(2); formal; locator: paper F0043 page_009; rubric F0038 lines 3-23
- `RECOVER_2025_丰台_二模_19_2`: 2025丰台二模 Q19(2); formal; locator: paper F0114/F0326 lines 256-327; rubric F0111 lines 3-25
- `RECOVER_2026_延庆_一模_18_1`: 2026延庆一模 Q18(1); formal; locator: paper F0368 lines 170-181; rubric F0369 lines 16-23
- `RECOVER_2026_房山_一模_17_1`: 2026房山一模 Q17(1); formal; locator: paper F0161 page_008; rubric F0371 lines 22-31
- `RECOVER_2026_西城_二模_18_1`: 2026西城二模 Q18(1); formal; locator: paper F0201 lines 120-129; rubric F0200 rendered page_006
- `RECOVER_2026_西城_二模_18_2`: 2026西城二模 Q18(2); formal; locator: paper F0201 lines 120-129; rubric F0200 rendered pages_007-008
- `RECOVER_2026_西城_二模_18_3`: 2026西城二模 Q18(3); formal; locator: paper F0201 lines 120-129; rubric F0200 rendered page_009
- `RECOVER_2026_门头沟_一模_18_1`: 2026门头沟一模 Q18(1); formal; locator: paper F0381 lines 273-290; rubric F0382 lines 30-36 and 87-96

## Boundary Or Blocked, Not Core

- `UNCERTAIN_2024_东城_二模_18_2_MIXED`: mixed_boundary_review_not_core; 设问为相关知识、建议书；评标明说涉及经济与社会、政治与法治、法律与生活等多个模块，法律点包括劳动关系认定、劳动者权益、全面履行劳动合同、职业培训权利义务。
- `UNCERTAIN_2025_海淀_期中_21_1_MIXED`: midterm_mixed_law_reference_not_core; 材料为婚姻法与民法典夫妻共同债务条文，设问为运用法治知识评析良法；有婚姻家庭法律素材，但答案收束在良法符合国情与社会发展需求，且仅见参考答案。
- `UNCERTAIN_2026_丰台_期末_18_MIXED`: mixed_boundary_review_not_core; 知识板块同时标注政治与法治、法律与生活；给分含检察权、政府履职、市场主体法定义务、未成年人合法权益、法治意识和核心价值观。
- `UNCERTAIN_2026_房山_一模_17_2_MIXED`: mixed_boundary_review_not_core; 设问为运用法治知识分析案例写入最高人民法院工作报告的意义，给分包含平衡民事权益与公共利益、全民法治观念、AI行业规范、公正司法、国家治理、社会主义核心价值观，混合必修三/法律价值。
- `BLOCKED_2026_石景山_期末_17_SOURCE_EXCLUDED`: special_user_excluded_or_source_blocked; 仅见答案及评分参考，缺原题题面；且选必二 hard-rule notebook 明确2026石景山期末 remains excluded unless user provides new usable scoring source。当前不能作为核心入库。
- `STAGE_CONFLICT_2026_石景山_期中`: stage_mapping_conflict; 这是清单分组误差，不是独立期中套卷；同一文件为石景山期末答案。

## Confirmed No-Law Suites

- 2024朝阳期中: 主观题为文化/哲学/逻辑/经济，未见选必二法律主观题。
- 2026朝阳期中: 主观题为当代国际、哲学、文化、辩证思维，未见法律主观题。

## Files

- `suite_exhaustion_matrix.csv`
- `merged_subjective_law_questions_suite_exhaustive.csv`
- `merged_material_atoms_subjective_suite_exhaustive.csv`
- `merged_ask_atoms_subjective_suite_exhaustive.csv`
- `merged_rubric_atoms_subjective_suite_exhaustive.csv`
- `boundary_mixed_or_blocked_cases.csv`
- `suite_exhaustive_counts.json`
