# ROUND 01 prompt for Claude Opus 4.7 Adaptive

你现在不是审稿人，也不是润色者。你的任务是基于处理后的北京选必二《法律与生活》主观题题源，独立生长一套适合学生启动、迁移和课堂讲解的框架候选。

## 必读输入

请按顺序读：

1. `00_READ_ME_FIRST.md`
2. `01_FRAMEWORK_GROWTH_GATE.md`
3. `evidence_pack/batch_01_priority_district_core_cards.md`
4. `evidence_pack/batch_02_remaining_core_cards.md`
5. `evidence_pack/batch_03_boundary_reference_and_next_backfill_cards.md`
6. `evidence_pack/true_coverage_matrix_v12_1.csv`

## 任务

1. 从 Batch 01 找学生最容易抓住的入口，不要先堆法律知识目录。
2. 用 Batch 02 检查学生能不能迁移：如果不能，说明框架节点哪里过抽象。
3. 用 Batch 03 判断开放容器和边界题怎样提醒学生，但不能支撑核心。
4. 对每个框架节点写清楚：
   - 学生看到什么材料信号会想到它
   - 设问让学生完成什么动作
   - 该节点最短可迁移语言
   - 常见误判
   - 课堂讲解顺序
5. 明确哪些题不适合进入主干，只适合做边界提醒。

## 输出格式

请输出以下部分：

1. `VERDICT`: 是否可以形成框架候选，不能写最终 PASS。
2. `STUDENT_FIRST_FRAMEWORK`: 学生第一眼能启动的框架，不超过 8 个主节点。
3. `TEACHING_SEQUENCE`: 课堂讲解顺序，先主干后容器。
4. `TRANSFER_LANGUAGE`: 每个节点的考场迁移句。
5. `BOUNDARY_AND_OPEN_CONTAINER`: 低频、参考、候选题如何处理。
6. `OVER_ABSTRACTION_RISKS`: 哪些节点太空、太法考化或太像审计表。
7. `EVIDENCE_GAPS`: 哪些题仍需要回源或不能纳入核心。
8. `REVISION_RULES`: 后续批次如何推动框架自我进化。

不要写完整宝典，不要生成 DOCX，不要宣布闭合。

