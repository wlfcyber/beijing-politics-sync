# 选必二《法律与生活》主观题宝典 V6.8 最终学生可用性审查

你现在是“选必二《法律与生活》主观题框架从题源生长工程”的最终学生可用性审查者。

你不要默认认可这份文档。你要同时扮演两个角色：

1. 一个聪明但几乎不会选必二法律主观题的高三学生。
2. 一个非常苛刻、只按材料和细则给分的阅卷人。

你的任务不是夸文档，也不是只审证据安全，而是判断：

> 学生读完 `选必二法律主观题满分训练宝典_v6_8_学生使用版_20260521.md` 后，看到陌生主观题，是否能快速启动、把材料翻译成法律语言、写出接近评分细则的满分答案？

## 当前工程状态

- 已入库主观题：65 题。
- 证据等级：61 formal / 4 reference-only / 0 missing。
- 学生训练边界：27 道严格核心题做满分训练；38 道题只能作为保分索引、边界题、待回源题或低频题，不得被说成全部满分闭环。
- V6.8 是当前最好学生使用版候选，不是最终封版。
- 本机 DOCX 全页视觉 QA 尚未完成：缺 `soffice`，Word AppleScript PDF 导出超时；只能承认结构 QA + 首屏缩略图 QA。

## 你必须阅读的文件

1. `PACKET_README.md`
2. `选必二法律主观题满分训练宝典_v6_8_学生使用版_20260521.md`
3. `v6_2_gptpro_claude_naked_review_comparison_20260521.md`
4. `V6_4_REGRESSION_VERDICT_20260521.md`
5. `grading_report_CEGH_v6_4_regression_20260521.md`
6. `V6_5_MINI_REGRESSION_VERDICT_20260521.md`
7. `DOCX_QA_V6_8_STUDENT_20260521.md`

## 审查方式

请按“裸题考试迁移”来审，不按“文件看起来是否完整”来审。

你要抽查至少 6 类场景：

1. 合同/侵权混合维权题。
2. 表格责任判断题。
3. 知识产权或 AI 作品题。
4. 程序路径/证据/起诉或调解仲裁题。
5. 企业合规或社会治理中容易写成必修三空话的题。
6. 38 道非核心索引题中至少 2 道，检查文档有没有误导学生把它们当核心模板。

每类场景都要回答：

- 学生读到题后第一步会不会知道从哪里进？
- 文档有没有逼学生先做最小必要判断？
- 文档有没有告诉学生哪些材料事实必须写进答案？
- 文档有没有把材料翻译成法律语言的动作？
- 文档有没有给出能贴近细则的句式，而不是空泛价值话？
- 文档有没有避免法考化过度分析？
- 文档有没有避免必修三化？
- 哪一句/哪一节仍然会误导学生？

## 输出格式

请严格输出以下部分：

### 1. 总 verdict

只能选一个：

- `PASS`
- `CONDITIONAL_PASS`
- `FAIL`

并说明：

- 是否可以交给学生使用。
- 是否可以生成 Word/PDF 最终封版。
- 是否可以声称“学生读完能稳定满分”。
- 是否仍必须保留“27 核心 + 38 保分索引”边界。

### 2. P0/P1/P2 问题清单

每条问题使用：

- issue_id:
- priority: P0 / P1 / P2
- location:
- problem:
- why_student_loses_points:
- concrete_rewrite_instruction:
- whether_blocks_final: yes / no

P0 = 会让学生系统性失分或跑偏，必须重写。
P1 = 会明显降低满分率，必须修补。
P2 = 表达、排版或局部清晰度问题，不阻塞候选使用。

### 3. 零基础学生模拟

请用 3 道你从文档中抽到的典型题或场景，模拟学生读完文档后的答题过程。

每题输出：

- scene:
- likely_entry:
- minimum_judgment:
- material_to_law_translation:
- likely_answer_sentence:
- grader_score_estimate:
- lost_points:
- document_fix_needed:

### 4. 必须保留的优点

只列真正帮助学生拿分的设计，不要泛泛夸。

### 5. 必须改掉的弱点

请直接、尖锐、可执行。

### 6. 下一版修订方案

如果 verdict 不是无条件 PASS，请给出下一版 V6.8 的修改方案：

- must_change_sections:
- exact_new_rules_or_sentences:
- examples_to_add_or_rewrite:
- tests_to_rerun:

## 硬规则

1. 不得把 reference-only 或 source-check 题升格为核心。
2. 不得说 65 题全部已经满分闭环。
3. 不得只给抽象建议，必须给可执行改写指令。
4. 如果你认为文档仍是一坨屎，请直接说 `FAIL`，不要客气。
5. 如果可以给学生用但还不能封最终 PDF，请说 `CONDITIONAL_PASS`。
