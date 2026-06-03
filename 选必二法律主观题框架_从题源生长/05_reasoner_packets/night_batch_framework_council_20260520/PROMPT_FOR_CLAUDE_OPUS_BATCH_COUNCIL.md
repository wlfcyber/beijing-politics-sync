# 选必二《法律与生活》主观题框架夜间分批 council prompt

你是本工程的外部框架审议者。请不要一次性凭直觉做总框架，而要读取本包文件：

- `INITIAL_CONCEPTION_CONTEXT_FROM_BIXIU4_FEED_RUBRIC.md`
- `batch_classification_65.csv`
- `BATCH_SUMMARY.md`
- 各批次 CSV

任务：

1. 先逐批分析每一批题真正训练的学生动作。
2. 每批只输出：材料触发信号、学生第一判断、细则奖励的表达、满分句生成方式、最常见错法。
3. 再判断哪些动作能合并成高频主干，哪些只能进入全量容器。
4. 必须保留 evidence 边界：formal 可支撑核心；reference_only 只参考；boundary/open 不能升核心；low-frequency singleton 不得制造稳定套路。
5. 输出一个学生能 20 秒启动的框架，同时给教师后台证据边界。
6. 不要按教材目录写，不要法考化，不要必修三化。

输出格式：

一、每批观察
- batch_id
- batch_action
- material_trigger
- first_judgment
- rewarded_sentence
- wrong_path
- can_support_core: yes/no/partial
- reason

二、建议主干
- trunk_id
- student_name
- action
- supported_batches
- supported_question_ids
- full_score_sentence
- boundary_warning

三、全量容器
- container_type
- question_ids
- how_to_answer_without_overclaim

四、你认为最强的一页学生版

五、你认为必须压测的题

注意：不要写最终宝典，只输出框架审议结果。
