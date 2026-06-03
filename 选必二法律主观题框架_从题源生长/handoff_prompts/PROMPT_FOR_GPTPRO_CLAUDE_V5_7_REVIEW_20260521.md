# V5.7 选必二法律主观题满分训练宝典终审复核 Prompt

你现在扮演 GPT-5.5 Pro / Claude Opus 4.7 Adaptive Thinking 的终审复核者。

请读取本包全部文件，尤其是：

1. `01_student_handbook/选必二法律主观题满分训练宝典_v5_7_27核心38题保分索引小修版_20260521.md`
2. `02_non_core_index/non_core_guardrails_v5_6_20260521.csv`
3. `03_pressure_tests/v5_6_zero_baseline_student_pressure_test_20260521.md`
4. `03_pressure_tests/v5_7_student_patch_report_20260521.md`
5. `04_external_reviews/claude_opus_v5_2_review_20260521.md`
6. `04_external_reviews/gptpro_v5_4_review_20260521.md`
7. `05_evidence_baseline/merged_subjective_law_questions.csv`
8. `05_evidence_baseline/merged_material_atoms_subjective.csv`
9. `05_evidence_baseline/merged_ask_atoms_subjective.csv`
10. `05_evidence_baseline/merged_rubric_atoms_subjective.csv`

本轮只问一个核心问题：

**一个聪明但原本啥都不会的高三学生，学完 V5.7 后，面对选必二《法律与生活》陌生主观题，能不能快速启动，并在 27 道核心题接近评分细则满分，在其余 38 道非核心题至少不乱套、能保分、不会误升核心？**

## 必守规则

1. 不要把 65 题全部说成核心满分闭环。
2. 27 道核心题可以严格压测；38 道非核心题只能看“最低保分、边界、回源提醒”是否够学生使用。
3. reference_only、source-check、boundary、excluded 题不得被你升为核心满分题。
4. 不按教材目录评价框架；只评价学生能不能审题、翻译材料、生成答案句。
5. 重点检查 V5.7 是否像学生能用的宝典，而不是审计文件。
6. 如果发现答案污染、题干拼贴、评分草句、后台标签、元数据、空泛必修三话术、法考化过度分析，必须标 P0。
7. 如果学生只能背例题不能迁移、动作卡入口过宽、source-check 红线仍不清，必须标 P1。

## 请输出

### 1. 总裁定

PASS / CONDITIONAL_PASS / FAIL

### 2. 学生可用性判断

- 20 秒启动是否够用？
- 六张动作卡是否能让学生选入口？
- 27 道核心题逐题示范是否像考场答案？
- 38 道非核心保分索引是否能防止学生乱套？
- “这题先判断什么”是否足够具体？
- 是否还能看到后台证据语言或审计语言？

### 3. 抽题压力测试

请至少抽 12 道题：

- 6 道核心题；
- 3 道 source-check 或低频题；
- 2 道 boundary/open/reference 题；
- 1 道 excluded/转出本书题。

每题输出：

question_id:
题型:
V5.7 入口:
学生可能答案:
对照细则估分或保分判断:
丢分点:
是否由 V5.7 不足导致:
修补建议:

### 4. P0/P1/P2 修补清单

每条必须写：

file_or_section:
problem:
patch:
why:
severity:

### 5. 是否允许进入 Word/PDF 成稿

只能回答：

- YES
- YES_WITH_GUARDS
- NO

并说明条件。

### 6. 如果你来改，第一优先级改什么

只给最重要的 3 件事。
