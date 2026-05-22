# v8.1 STEP 00 硬 QA 扫描

结论：当前 v8 不能直接交付。扫描命中大量学生正文禁用词，必须进入 v8.1 修复。

## 一、扫描范围
- `01_student_exam_framework_v8.md`
- `02_full_baodian_v8.md`
- `06_gold_standard_question_runs.md`
- `07_full_score_sentence_bank_v8.md`
- `08_question_by_question_runs_v8.md`
- `08_question_by_question_runs_v8.csv`
- `09_teacher_evidence_framework_v8.md`

## 二、命中统计

| severity | count |
|---|---:|
| P0 | 1479 |
| P1 | 159 |
| allowed_teacher_evidence | 16 |

## 三、判定

- QA 状态：FAIL。
- 原因：学生正文/逐题运行正文仍包含评分说明、证据编号、页码、设问缺失、细则摘抄或禁止词风险。
- 执行门槛：必须先修复金样板同步、设问缺失、优先 10 题、句库和教师证据框架，才能生成 v8.1 宝典。

## 四、P0 前 80 条样例

| file | line | pattern | action | excerpt |
|---|---:|---|---|---|
| `02_full_baodian_v8.md` | 5 | R_ | rewrite_or_move_to_teacher_evidence | 语料口径：boundary-patched 53 道主观题；37 PASS，11 PASS_RECOVERED，5 OPEN_OR_REFERENCE。   |
| `02_full_baodian_v8.md` | 6 | R_ | rewrite_or_move_to_teacher_evidence | 使用原则：学生先学动作，教师再看证据；OPEN_OR_REFERENCE 只作参考运行，不支撑核心节点。 |
| `02_full_baodian_v8.md` | 15 | 第.*页 | rewrite_or_move_to_teacher_evidence | 2. 再背第四章学生版一页框架。 |
| `02_full_baodian_v8.md` | 72 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0137_2025_昌平_二模_20_02、R_CC0137_2025_昌平_二模_20_03、R_CC0137_2025_昌平_二模_20_05。   |
| `02_full_baodian_v8.md` | 77 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0137_2025_昌平_二模_20_04、R_CC0137_2025_昌平_二模_20_07。   |
| `02_full_baodian_v8.md` | 82 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0137_2025_昌平_二模_20_08 至 R_CC0137_2025_昌平_二模_20_12。   |
| `02_full_baodian_v8.md` | 91 | M_ | rewrite_or_move_to_teacher_evidence | 对应材料：M_CC0137_2025_昌平_二模_20_15、M_CC0137_2025_昌平_二模_20_17。   |
| `02_full_baodian_v8.md` | 92 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0137_2025_昌平_二模_20_02、R_CC0137_2025_昌平_二模_20_03、R_CC0137_2025_昌平_二模_20_05。   |
| `02_full_baodian_v8.md` | 97 | M_ | rewrite_or_move_to_teacher_evidence | 对应材料：M_CC0137_2025_昌平_二模_20_16。   |
| `02_full_baodian_v8.md` | 98 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0137_2025_昌平_二模_20_04、R_CC0137_2025_昌平_二模_20_07。   |
| `02_full_baodian_v8.md` | 103 | M_ | rewrite_or_move_to_teacher_evidence | 对应材料：M_CC0137_2025_昌平_二模_20_20 至 M_CC0137_2025_昌平_二模_20_24。   |
| `02_full_baodian_v8.md` | 104 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0137_2025_昌平_二模_20_08 至 R_CC0137_2025_昌平_二模_20_12。   |
| `02_full_baodian_v8.md` | 155 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0238_2026_东城_二模_19_M17_01。   |
| `02_full_baodian_v8.md` | 160 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0238_2026_东城_二模_19_M17_02、R_CC0238_2026_东城_二模_19_M17_03。   |
| `02_full_baodian_v8.md` | 165 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0238_2026_东城_二模_19_M17_04、R_CC0238_2026_东城_二模_19_M17_05。   |
| `02_full_baodian_v8.md` | 174 | M_ | rewrite_or_move_to_teacher_evidence | 对应材料：M_CC0238_2026_东城_二模_19_05。   |
| `02_full_baodian_v8.md` | 175 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0238_2026_东城_二模_19_M17_01。   |
| `02_full_baodian_v8.md` | 180 | M_ | rewrite_or_move_to_teacher_evidence | 对应材料：M_CC0238_2026_东城_二模_19_07、M_CC0238_2026_东城_二模_19_08。   |
| `02_full_baodian_v8.md` | 181 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0238_2026_东城_二模_19_M17_02、R_CC0238_2026_东城_二模_19_M17_03。   |
| `02_full_baodian_v8.md` | 186 | M_ | rewrite_or_move_to_teacher_evidence | 对应材料：M_CC0238_2026_东城_二模_19_06。   |
| `02_full_baodian_v8.md` | 187 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0238_2026_东城_二模_19_M17_04、R_CC0238_2026_东城_二模_19_M17_05。   |
| `02_full_baodian_v8.md` | 237 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0305_2026_海淀_一模_18_3_P02。   |
| `02_full_baodian_v8.md` | 242 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0305_2026_海淀_一模_18_3_P02。   |
| `02_full_baodian_v8.md` | 247 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0305_2026_海淀_一模_18_3_P03。   |
| `02_full_baodian_v8.md` | 257 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0305_2026_海淀_一模_18_3_P01。   |
| `02_full_baodian_v8.md` | 262 | M_ | rewrite_or_move_to_teacher_evidence | 对应材料：M_CC0305_2026_海淀_一模_18_3_P01、M_CC0305_2026_海淀_一模_18_3_P02。   |
| `02_full_baodian_v8.md` | 263 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0305_2026_海淀_一模_18_3_P02。   |
| `02_full_baodian_v8.md` | 268 | M_ | rewrite_or_move_to_teacher_evidence | 对应材料：M_CC0305_2026_海淀_一模_18_3_P03。   |
| `02_full_baodian_v8.md` | 269 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0305_2026_海淀_一模_18_3_P03。   |
| `02_full_baodian_v8.md` | 319 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0054_2024_石景山_一模_17_M17_01。   |
| `02_full_baodian_v8.md` | 324 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0054_2024_石景山_一模_17_M17_02、R_CC0054_2024_石景山_一模_17_M17_03。   |
| `02_full_baodian_v8.md` | 329 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0054_2024_石景山_一模_17_M17_04 至 R_CC0054_2024_石景山_一模_17_M17_06。   |
| `02_full_baodian_v8.md` | 338 | M_ | rewrite_or_move_to_teacher_evidence | 对应材料：M_CC0054_2024_石景山_一模_17_02、M_CC0054_2024_石景山_一模_17_03。   |
| `02_full_baodian_v8.md` | 339 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0054_2024_石景山_一模_17_M17_01。   |
| `02_full_baodian_v8.md` | 344 | M_ | rewrite_or_move_to_teacher_evidence | 对应材料：M_CC0054_2024_石景山_一模_17_04。   |
| `02_full_baodian_v8.md` | 345 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0054_2024_石景山_一模_17_M17_02、R_CC0054_2024_石景山_一模_17_M17_03。   |
| `02_full_baodian_v8.md` | 350 | M_ | rewrite_or_move_to_teacher_evidence | 对应材料：M_CC0054_2024_石景山_一模_17_05 至 M_CC0054_2024_石景山_一模_17_09。   |
| `02_full_baodian_v8.md` | 351 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0054_2024_石景山_一模_17_M17_04 至 R_CC0054_2024_石景山_一模_17_M17_06。   |
| `02_full_baodian_v8.md` | 401 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0103_2025_丰台_一模_19_01 中企业层面。   |
| `02_full_baodian_v8.md` | 406 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0103_2025_丰台_一模_19_01 中科技创新意义。   |
| `02_full_baodian_v8.md` | 411 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0103_2025_丰台_一模_19_01 中司法领域价值。   |
| `02_full_baodian_v8.md` | 420 | M_ | rewrite_or_move_to_teacher_evidence | 对应材料：M_CC0103_2025_丰台_一模_19_02、M_CC0103_2025_丰台_一模_19_03。   |
| `02_full_baodian_v8.md` | 421 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0103_2025_丰台_一模_19_01。   |
| `02_full_baodian_v8.md` | 426 | M_ | rewrite_or_move_to_teacher_evidence | 对应材料：M_CC0103_2025_丰台_一模_19_03。   |
| `02_full_baodian_v8.md` | 427 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0103_2025_丰台_一模_19_01。   |
| `02_full_baodian_v8.md` | 432 | M_ | rewrite_or_move_to_teacher_evidence | 对应材料：M_CC0103_2025_丰台_一模_19_04。   |
| `02_full_baodian_v8.md` | 433 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0103_2025_丰台_一模_19_01。   |
| `02_full_baodian_v8.md` | 483 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0025_2024_朝阳_二模_17_02、R_CC0025_2024_朝阳_二模_17_09、R_CC0025_2024_朝阳_二模_17_10。   |
| `02_full_baodian_v8.md` | 488 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0025_2024_朝阳_二模_17_03、R_CC0025_2024_朝阳_二模_17_11、R_CC0025_2024_朝阳_二模_17_12。   |
| `02_full_baodian_v8.md` | 493 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0025_2024_朝阳_二模_17_04、R_CC0025_2024_朝阳_二模_17_13、R_CC0025_2024_朝阳_二模_17_14。   |
| `02_full_baodian_v8.md` | 502 | M_ | rewrite_or_move_to_teacher_evidence | 对应材料：M_CC0025_2024_朝阳_二模_17_09 至 M_CC0025_2024_朝阳_二模_17_11。   |
| `02_full_baodian_v8.md` | 503 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0025_2024_朝阳_二模_17_02、R_CC0025_2024_朝阳_二模_17_09、R_CC0025_2024_朝阳_二模_17_10。   |
| `02_full_baodian_v8.md` | 508 | M_ | rewrite_or_move_to_teacher_evidence | 对应材料：M_CC0025_2024_朝阳_二模_17_08、M_CC0025_2024_朝阳_二模_17_10。   |
| `02_full_baodian_v8.md` | 509 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0025_2024_朝阳_二模_17_03、R_CC0025_2024_朝阳_二模_17_11、R_CC0025_2024_朝阳_二模_17_12。   |
| `02_full_baodian_v8.md` | 514 | M_ | rewrite_or_move_to_teacher_evidence | 对应材料：M_CC0025_2024_朝阳_二模_17_06、M_CC0025_2024_朝阳_二模_17_07、M_CC0025_2024_朝阳_二模_17_13、M_CC0025_2024_朝阳_二模_17_14。   |
| `02_full_baodian_v8.md` | 515 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0025_2024_朝阳_二模_17_04、R_CC0025_2024_朝阳_二模_17_13、R_CC0025_2024_朝阳_二模_17_14。   |
| `02_full_baodian_v8.md` | 565 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0125_2025_延庆_一模_19_M17_02。   |
| `02_full_baodian_v8.md` | 570 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0125_2025_延庆_一模_19_M17_03。   |
| `02_full_baodian_v8.md` | 575 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0125_2025_延庆_一模_19_M17_04、R_CC0125_2025_延庆_一模_19_M17_05。   |
| `02_full_baodian_v8.md` | 585 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0125_2025_延庆_一模_19_M17_01。   |
| `02_full_baodian_v8.md` | 590 | M_ | rewrite_or_move_to_teacher_evidence | 对应材料：M_CC0125_2025_延庆_一模_19_02 至 M_CC0125_2025_延庆_一模_19_06。   |
| `02_full_baodian_v8.md` | 591 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0125_2025_延庆_一模_19_M17_03、R_CC0125_2025_延庆_一模_19_M17_04。   |
| `02_full_baodian_v8.md` | 596 | M_ | rewrite_or_move_to_teacher_evidence | 对应材料：M_CC0125_2025_延庆_一模_19_04、M_CC0125_2025_延庆_一模_19_06。   |
| `02_full_baodian_v8.md` | 597 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0125_2025_延庆_一模_19_M17_05。   |
| `02_full_baodian_v8.md` | 647 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0002_2024_丰台_一模_17_M17_01、R_CC0002_2024_丰台_一模_17_M17_03。   |
| `02_full_baodian_v8.md` | 652 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0002_2024_丰台_一模_17_M17_02、R_CC0002_2024_丰台_一模_17_M17_03。   |
| `02_full_baodian_v8.md` | 657 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则点：R_CC0002_2024_丰台_一模_17_M17_04 至 R_CC0002_2024_丰台_一模_17_M17_06。   |
| `02_full_baodian_v8.md` | 666 | M_ | rewrite_or_move_to_teacher_evidence | 对应材料：M_CC0002_2024_丰台_一模_17_01。   |
| `02_full_baodian_v8.md` | 667 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0002_2024_丰台_一模_17_M17_01。   |
| `02_full_baodian_v8.md` | 672 | M_ | rewrite_or_move_to_teacher_evidence | 对应材料：M_CC0002_2024_丰台_一模_17_02 至 M_CC0002_2024_丰台_一模_17_08。   |
| `02_full_baodian_v8.md` | 673 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0002_2024_丰台_一模_17_M17_02、R_CC0002_2024_丰台_一模_17_M17_03。   |
| `02_full_baodian_v8.md` | 679 | R_ | rewrite_or_move_to_teacher_evidence | 对应细则：R_CC0002_2024_丰台_一模_17_M17_04 至 R_CC0002_2024_丰台_一模_17_M17_06。   |
| `02_full_baodian_v8.md` | 701 | 第.*页 | rewrite_or_move_to_teacher_evidence | # 第四章：学生版一页框架 |
| `02_full_baodian_v8.md` | 901 | gold_sample_all_material_atoms | rewrite_or_move_to_teacher_evidence | - source_material_atom_ids: gold_sample_all_material_atoms |
| `02_full_baodian_v8.md` | 902 | gold_sample_all_rubric_atoms | rewrite_or_move_to_teacher_evidence | - source_rubric_atom_ids: gold_sample_all_rubric_atoms |
| `02_full_baodian_v8.md` | 914 | R_ | rewrite_or_move_to_teacher_evidence | - open_or_reference_limit: OPEN_OR_REFERENCE 只可练分诊，不支撑节点 |
| `02_full_baodian_v8.md` | 920 | M_ | rewrite_or_move_to_teacher_evidence | - source_material_atom_ids: M_CC0305_2026_海淀_一模_18_3_P01｜M_CC0305_2026_海淀_一模_18_3_P02｜M_CC0305_2026_海淀_一模_18_3_P03 |
| `02_full_baodian_v8.md` | 921 | R_ | rewrite_or_move_to_teacher_evidence | - source_rubric_atom_ids: R_CC0305_2026_海淀_一模_18_3_P01｜R_CC0305_2026_海淀_一模_18_3_P02｜R_CC0305_2026_海淀_一模_18_3_P03 |
| `02_full_baodian_v8.md` | 933 | R_ | rewrite_or_move_to_teacher_evidence | - open_or_reference_limit: 不使用 OPEN_OR_REFERENCE 表态题作核心代表 |
| `02_full_baodian_v8.md` | 939 | M_ | rewrite_or_move_to_teacher_evidence | - source_material_atom_ids: M_CC0137_2025_昌平_二模_20_15｜M_CC0137_2025_昌平_二模_20_16｜M_CC0137_2025_昌平_二模_20_20｜M_CC0137_2025_昌平_二模_20_21｜M_CC0137_2025_昌平_二模_20_22｜M_CC0137_2025_昌平_二模_20_24 |
