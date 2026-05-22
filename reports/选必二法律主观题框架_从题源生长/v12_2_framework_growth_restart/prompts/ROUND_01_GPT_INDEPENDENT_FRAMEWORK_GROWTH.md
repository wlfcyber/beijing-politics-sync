# ROUND 01 prompt for GPT-5.5 Pro

你现在不是审稿人，也不是润色者。你的任务是基于处理后的北京选必二《法律与生活》主观题题源，独立生长一套学生可用、证据可追踪的框架候选。

## 必读输入

请按顺序读：

1. `00_READ_ME_FIRST.md`
2. `01_FRAMEWORK_GROWTH_GATE.md`
3. `evidence_pack/batch_01_priority_district_core_cards.md`
4. `evidence_pack/batch_02_remaining_core_cards.md`
5. `evidence_pack/batch_03_boundary_reference_and_next_backfill_cards.md`
6. `evidence_pack/true_coverage_matrix_v12_1.csv`

## 任务

1. 从 Batch 01 独立提炼高频主干。不要套现成法律目录，也不要只列法条知识点。
2. 用 Batch 02 压测主干：哪些能覆盖，哪些需要开放容器，哪些暴露框架缺口。
3. 用 Batch 03 只做边界观察：5 道参考题和 6 道候选题不能直接支撑核心。
4. 对每个框架节点写清楚：
   - 题源触发信号
   - 设问动作
   - 材料事实如何翻译成法律判断
   - 评分口径奖励什么
   - 学生第一步怎么启动
   - 不能误判成什么
5. 给出版本变更标准：什么新题出现时需要新增节点，什么情况只放开放容器。

## 输出格式

请输出以下部分：

1. `VERDICT`: 是否可以形成框架候选，不能写最终 PASS。
2. `HIGH_FREQUENCY_TRUNK`: 3-8 个主干节点，每个节点必须列支撑题号。
3. `OPEN_CONTAINERS`: 低频/边界/参考容器，不得混入核心主干。
4. `QUESTION_MAKER_PATHS`: 命题人路径类型，说明题为什么这样设问。
5. `STUDENT_STARTERS`: 学生考场第一步判断语。
6. `COVERAGE_AND_GAPS`: 哪些题覆盖强、哪些题需要回源、哪些不能支撑。
7. `CHANGE_CRITERIA`: 后续批次如何修改框架。
8. `RED_LINES`: 禁止法考化、必修三化、泛法治口号化、参考题撑核心。

不要写完整宝典，不要生成 DOCX，不要宣布闭合。

