# GPT-5.5 Pro 严格四线闭环复审

项目：选必二《法律与生活》严格四线补齐。

你仍然在“法律与生活框架审议”这个选必二专用对话中工作。用户已确认当前模型可按 GPT-5.5 Pro 高置信度计入。请只基于本次附上的两份“零基础强补版” Markdown，不要网页搜索，不要继承其他项目。

这不是普通格式审稿。请模拟一个聪明但零基础的高三学生，判断这两份文档是否已经从“旧题检索式学习”升级为“能做陌生新题的可迁移框架”。

重点检查：

1. 是否已经补上“争点生成器”，学生遇到新材料能不能自己形成争点。
2. 高频要件卡是否足以堵住先前系统性丢分点：竞业限制经济补偿、遗赠扶养书面形式、无过错责任免责减责、消费者欺诈/违约/知情权分线、民事公益诉讼与行政公益诉讼区分。
3. 五域定位是否清楚，消费者、合同、劳动是否仍会混淆。
4. 主观题和选择题是否分开，选择题是否不会被误当主观题模板。
5. 新增要件卡是否过度法考化，是否会增加学生负担。
6. 意义类模板是否避免宏观法治口号化。
7. 文档是否还有会误导学生的地方。

请输出：

- final_verdict: PASS / CONDITIONAL PASS / FAIL
- can_do_unseen_subjective_questions: YES / ALMOST / NO
- can_stably_full_score: YES / ALMOST / NO
- must_fix_before_word_delivery
- should_fix_after_delivery
- reject_or_do_not_change
- exact_student_risk_cases
- final_advice_to_codex

注意：
- 你可以提出补丁，但所有新法律事实都写“需本地题源核验”。
- 不要把普通参考答案当细则。
- 不要泛泛夸，必须给可以执行的结论。
