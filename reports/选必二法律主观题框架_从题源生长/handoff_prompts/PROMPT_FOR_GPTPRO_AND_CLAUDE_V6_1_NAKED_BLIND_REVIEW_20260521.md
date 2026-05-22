你现在参与“选必二《法律与生活》主观题框架从题源生长工程”的 V6.1 裸题盲测复核。

你的身份不是夸稿人，而是两个人叠加：

1. 一个聪明但原来不会法律主观题的高三学生；
2. 一个按评分细则狠扣分的阅卷老师。

请你读取附件：

- `选必二法律主观题满分训练宝典_v6_1_裸题盲测修补稿_20260521.md`
- `clean_questions_no_labels_v6_20260521_v2.md`
- `agent_student_answers_v6_naked_20260521_v2.md`
- `internal_grading_key_v6_20260521_v2.csv`
- `codex_grading_report_v6_naked_20260521_v2.md`
- `v5_9_attack_review_synthesis_20260521.md`

当前进度：

- 证据底座仍为 65 道主观题，formal / reference_only / missing = 61 / 4 / 0。
- 学生正文严格分为 27 道 strict core 满分训练区 + 38 道 non-core guard/index/reference/boundary 保分区。
- V5.9 已被用户否定并降级为攻击样稿。
- GPTPro 与 Claude Opus 对 V5.9 的攻击结论均为 `PASS_WITH_MAJOR_REWRITE`。
- Codex 已据此生成 V6，并做了一轮隐藏 question_id/category/core 标签的裸题盲测。
- 裸题盲测结论暂定为 `PASS_WITH_REAL_GUARDS_NOT_FINAL`。
- V6.1 只修裸题暴露的问题：CC0206 营商环境硬词、表格题真实列名、source-check/reference-only 前台红线。

你的任务：

一、先判总成色

请给出一个总判：

- PASS：聪明学生读完 V6.1，面对陌生法律主观题可以稳定启动，并在核心题上接近满分；
- CONDITIONAL_PASS：主干可用，但仍有若干会导致失分/误用的硬伤；
- FAIL：学生读完仍不会用，或框架会系统性误导。

二、逐题复核裸题 A-L

对每个样题给出：

- 是否能看出学生是从 V6.1 学会的，而不是靠题目标签；
- 按评分钥匙能否接近满分；
- 最可能扣分的词句；
- 是 V6.1 问题、题面包问题、source-card 问题，还是学生临场表达问题。

三、攻击 V6.1 学生稿

请找 P0 / P1 / P2：

- P0：会导致学生大面积写错、必修三化、法考化、误收 reference_only、或把 source-check 升核心的问题。
- P1：会导致一类题少踩关键分的问题。
- P2：表达不够顺、教学顺序可优化、但不致命的问题。

每个问题必须写：

- 问题位置或对应题型；
- 为什么会扣分或误导；
- 应该改成什么具体句子。

四、框架是否真的比 V5.9 进步

请比较：

- V6.1 的设问尾词诊断树是否足够学生启动？
- 九个战场是否仍然太散？
- 27 core 是否适合作为学习路径？
- 38 non-core 的 guard/index 是否能防误用？
- 三句保底答案是否会让学生误以为就是满分？

五、最后输出

请最后给出：

1. 总判：PASS / CONDITIONAL_PASS / FAIL。
2. 必须立刻修改的 5 条以内。
3. 可以暂缓的 5 条以内。
4. 是否允许进入 Word/PDF candidate。
5. 是否允许宣布“学生读完能答到满分”；如果不允许，请说明还差哪一关。

硬规则：

- 不要重新写一套漂亮框架。
- 不要把普通参考答案升成 formal 细则。
- 不要把 65 题全部说成核心满分闭环。
- 如果你认为 V6.1 仍然不够好，要直接说，不要客气。
