# V5.9 零基础学生抽样盲测阅卷报告

- time: 2026-05-21 05:08 CST
- student answer file: `10_framework_validation/v5_9_zero_baseline_student_blind_test_20260521/agent_student_answers_v5_9_20260521.md`
- grading key: `10_framework_validation/v5_9_zero_baseline_student_blind_test_20260521/grading_key_v5_9_20260521.csv`
- verdict: PASS_WITH_GUARDS

## 总结论

V5.9 通过这一轮 8 题抽样盲测。

最重要的结果不是“每题都写得漂亮”，而是学生稿终于能同时做到两件事：

1. 对 4 道核心题，学生能按 V5.9 训练路径写出接近满分的考场答案。
2. 对 4 道非核心题，学生没有误升核心，没有把 source-check、reference-only、boundary、low-frequency 当成闭合满分模板。

这说明 V5.9 的“27 核心满分训练 + 38 保分/边界/回源索引”口径在学生端基本可执行。

## 逐题结果

| 样本 | question_id | 类型 | 结果 | 说明 |
| --- | --- | --- | --- | --- |
| 1 | `CC0002_2024_丰台_一模_17` | strict_core | PASS 8/8 | 写出好意同乘、无故意或重大过失、未系安全带/垫付、合理减责和价值。 |
| 2 | `CC0025_2024_朝阳_二模_17` | strict_core | PASS 8/8 | 三个从属性和事实劳动关系判断清楚，意义没有空泛化。 |
| 3 | `CC0103_2025_丰台_一模_19` | strict_core | PASS 8/8 | 先保护技术秘密和惩罚性赔偿，再推创新、竞争秩序、司法范例。 |
| 4 | `CC0244_2026_东城_期末_18` | strict_core | PASS_WITH_SOURCEPACK_NOTE 8/8 | 学生答案覆盖第（1）问和第（2）问，但盲测题面包从 canonical question row 抽 ask_text 时漏了第（2）问，后续需修源卡/题面包。 |
| 5 | `CC0011_2024_丰台_二模_17` | low_frequency_container | PASS_GUARD | 学生明确只作低频保分卡，没有抬成高频核心。 |
| 6 | `CC0019_2024_朝阳_一模_19` | source_check_pending | PASS_GUARD | 学生识别设问缺失，只写诚信原则最低方向，没有伪装闭合。 |
| 7 | `CC0040_2024_海淀_一模_19` | reference_only_locked | PASS_GUARD | 学生识别 reference-only，只作练笔，不支撑核心框架。 |
| 8 | `RECOVER_2026_西城_二模_18_3` | boundary_open_container | PASS_GUARD | 学生识别综合边界，只写法律层最低表达，并提醒其他模块另开段。 |

## 发现的问题

### P2-1：非核心 CSV 需要同步 V5.9 文本

阅卷时发现后台 grading key 最初引用 `non_core_guardrails_v5_8_20260521.csv`，其中 `RECOVER_2026_西城_二模_18_3` 仍有旧式边界表达。已生成 V5.9 同步副本：

- `12_final_baodian/non_core_guardrails_v5_9_20260521.csv`

该副本同步了低频、source-check、reference-only、boundary 的视觉红线，并修正了综合边界题的最低句。

### P2-2：`CC0244` 题面包取源存在 ask_text 漏项

V5.9 核心 CSV 已包含 `CC0244` 第（1）问和第（2）问；学生也能写出两问。但是盲测题面包最初从 `merged_subjective_law_questions.csv` 取 `ask_text`，只带出第（1）问。

这不是学生稿失败，而是 source-card/盲测包生成口径不一致。后续应把 `CC0244` 的 canonical question row 或盲测题包生成逻辑修到与 V5.9 核心 CSV 一致。

## 裁定

- V5.9 学生稿：PASS_WITH_GUARDS。
- V5.9 Word/PDF candidate：可交付用户阅读。
- 仍禁止宣称：65 题全部核心满分闭环。
- 下一步若继续：优先修 `CC0244` 源卡 ask_text，再对 24 个 source-check 题逐题回源。
