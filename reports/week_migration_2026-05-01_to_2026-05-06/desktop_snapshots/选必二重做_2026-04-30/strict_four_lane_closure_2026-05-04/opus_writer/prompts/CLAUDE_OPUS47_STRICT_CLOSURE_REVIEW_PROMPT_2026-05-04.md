# 严格四线闭环复审：零基础强补版
你仍然是 Claude Opus 4.7 Adaptive，在同一个选必二《法律与生活》专用对话中工作。请只基于本次附上的两份“零基础强补版” Markdown，不要网页搜索，不要继承其他项目。

这次不是普通审稿，而是检查上一轮学会性压力测试暴露的问题是否已经被补齐。请模拟聪明但零基础的高三学生，看这两份新版文档后能否直接做陌生新题，并判断是否能稳定全对。

重点检查：
1. “争点三种锁定法”是否真的能让学生自己生成争点；
2. 高频要件卡是否堵住：竞业限制经济补偿、遗赠扶养书面形式、无过错责任免责减责、消费者欺诈/违约/知情权分线、民事公益诉讼 vs 行政公益诉讼；
3. 五域决策树是否解决消费者/合同/劳动混淆；
4. 主观题和选择题是否分开，选择题是否不会误用成主观题模板；
5. 是否过度法考化或增加负担；
6. 意义类模板是否避免价值空转；
7. 还需不需要 before Word delivery 的 must-fix。

请输出：
- final_verdict: PASS / CONDITIONAL PASS / FAIL
- can_do_unseen_subjective_questions: YES / ALMOST / NO
- can_stably_full_score: YES / ALMOST / NO
- must_fix_before_word_delivery
- should_fix_after_delivery
- reject_or_do_not_change
- exact_student_risk_cases
- final_advice_to_codex

注意：所有新法律事实都写“需本地题源核验”；不要把普通参考答案当细则。
