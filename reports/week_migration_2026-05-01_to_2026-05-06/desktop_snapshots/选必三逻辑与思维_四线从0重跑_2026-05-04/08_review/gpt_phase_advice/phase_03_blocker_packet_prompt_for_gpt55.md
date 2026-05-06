你是 GPT-5.5 Pro，作为飞哥政治庄园四线工作流里的“总指挥/内容压力测试官”。请你审阅本轮 Phase 03 的阻塞/差异包，给出下一步裁决。

## 背景

任务：从0重跑北京高考政治 选必三《逻辑与思维》，分成两个最终部分：

1. 思维部分：完全模仿已成功的哲学宝典做法。每个“思维/方法”像哲学原理方法论一样处理，形成“材料信号 -> 可写思维/方法 -> 答题动作 -> 来源例题”的学生可迁移体系。
2. 推理部分：按题型分类，把所有对应真题放在同类题型下面，例如三段论、充分/必要条件假言推理、联言/选言推理、归纳/类比、逻辑三律等；每类都要有规则口令、易错陷阱、解题动作、同类题归档。

用户明确批评过：上一版没有穷尽每一道题，内容质量远不如哲学宝典，属于偷懒。因此本轮必须严格四线：Codex A 自己跑、ClaudeCode B 独立跑、GPT-5.5 Pro 阶段指挥和内容审查、Claude/Opus 只在证据锁定后负责成品化表达。

当前日期：2026-05-04。
本轮目录：`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`

## 最高限制

- 这是 Phase 03 blocker/diff review，不是 PASS 包。
- 请不要批准学生稿、Claude/Opus 成文化、Word/PDF、最终 PASS。
- 你的建议必须回到本地证据矩阵和源文件，不要凭空新增事实。

## Phase 02 你此前给出的方向

你此前给出 `CONDITIONAL GO`，允许进入 full suite question scan and classification，要求：

- 每一道题必须能回到 source locator；
- 每一道题必须落到思维链矩阵、推理挂载矩阵，或 blocked list；
- HS02 等视觉题必须锁定到视觉确认后才能入稿；
- 推理部分需要 logical_form、rule_slogan、valid/invalid pattern/trap、answer_action、same_type_question_ids；
- 继续禁止学生稿、Opus 成文化、Word/PDF、最终 PASS。

## Phase 03 已完成工作

### Codex Lane A

- 正式 Phase03 初始矩阵：528 行 question/sub-question rows。
- thinking rows: 73。
- reasoning rows: 166。
- blocked rows: 42。
- visual blocker rows: 4。
- 视觉恢复种子：2025海淀二模 Q20、2026丰台一模 Q18(2)。
- 发现 A 线有噪声：重复行、answer/rubric/reference text 混入 question matrix。

### ClaudeCode Lane B

- Phase03 独立全量扫描已完成，但实际更像 candidate scan：
  - source registry 56 sources；
  - suite registry 17 suites；
  - question/candidate rows 约 53/59；
  - thinking 10；
  - reasoning 27；
  - visual blockers 11；
  - missing/conflicts 5 类。
- Lane B 明确承认 14 unread sources、4 pending suites，不能算 every-question coverage。

### A/B Diff 结论

Verdict: `NO_PASS_CONTINUE_EXTRACTION`

Counts:

- Lane A question/subquestion rows: 528
- Lane A in-scope/cross keys: 122
- Lane B question/candidate rows: 59
- Common A/B keys: 46
- A-only in-scope/cross keys: 76
- B-only candidate keys: 7

Critical findings:

1. P1: Lane B is not literal every-question coverage; it is useful candidate scan only.
2. P1: Lane B initially missed 2026丰台一模 Q18(2).
3. P1: HS02 / 2025海淀二模 Q20 originally still needed Lane B visual confirmation.
4. P2: Lane B unread sources remain.
5. P2: Lane A has noisy duplicates and reference text mixed into question rows.
6. P2: 2026二模 materials are not found in current source boundary; record missing, do not claim nonexistence.

### Focused ClaudeCode Patch 完成

为修正两个 P1，已让 ClaudeCode 做窄补丁，禁止学生稿。

Patch result:

1. 2026丰台一模 Q18(2)
   - 原卷 042 render page_07 视觉确认：Q18(2) 是“分别分析以上推理的类型，判断是否正确，并说明理由。（6分）”。
   - 043 细则 SLIDE 35 明确：知识板块“逻辑与思维”。
   - 甲：必要条件假言推理，肯定后件式，前提真实，正确。
   - 乙：三段论推理，“带动居民消费”作为大项在前提中不周延、结论中周延，犯“大项不当扩大”，错误。
   - 结论：`PASS_TO_FUSION / A-formal / VISUAL_CONFIRMED_LANE_B`。

2. 2025海淀二模 Q20 / HS02
   - 原卷 008 render page_07 视觉确认：Q20 设问“结合材料，运用辩证思维知识，谈谈如何更好地坚持共享发展理念推进共同富裕。”
   - 009/010/011 三源一致：角度池，从 3 个角度中选 2；分析与综合/整体性、质量互变/动态性、辩证否定；矛盾分析法最多 2 分。
   - 明确不是三点全必答。
   - 结论：`PASS_TO_FUSION / A-formal / VISUAL_CONFIRMED_LANE_B`，HS02 Lane B visual lock 解除。

### Codex Lane A 去重拆分完成

脚本：`02_extraction/phase03_dedup_split_laneA_matrix.py`

结果：

- Input rows: 528
- Canonical paper/question rows: 358
- Support/reference rows split out: 46
- Duplicate/removed rows logged: 170
- Duplicate suite/question keys in input: 118
- Canonical in-scope or cross candidates: 119
- Canonical locked rows after focused patch context: A matrix本身仍需后续写回状态；补丁文件已确认两个锁定点可进入 fusion。

Meaning:

- 原卷题目矩阵和细则/讲评/参考支撑矩阵已经拆开；
- 这一步不等于学生稿晋级，只是后续融合底座变干净；
- 仍有 2026二模 missing、Lane B not every-question、A-only/B-only conflict、choice answer pairing、视觉/OCR全页题号恢复等任务。

## 需要你裁决的问题

请你用非常严格的总指挥口吻回答：

1. 当前是否可以从 Phase03 进入 Phase04“补缺式证据融合/同类题归档”？还是必须继续 Phase03 full every-question coverage？
2. 对 Lane B 不可能短时间变成 528 行 every-question matrix 的情况，你建议怎么做才不算偷懒？例如是否以 Codex A canonical 358 行作为 every-question control base，再让 ClaudeCode B 对 A-only 高风险/高价值题做 targeted independent verification？
3. 你认为下一步最优先的 5 个任务是什么？请按 P0/P1/P2 排序。
4. 对思维部分和推理部分分别给出“不许进学生稿”的硬门槛。
5. 你认为 2026丰台一模 Q18(2) 和 2025海淀二模 Q20 现在是否可以进入 fusion evidence pool？请只回答是否可以进 evidence fusion，不要批准学生稿。
6. 请给出一个短的 verdict，格式必须是：
   - `GO_TO_PHASE04_TARGETED_FUSION`
   - `STAY_IN_PHASE03_FULL_COVERAGE`
   - `GO_BUT_WITH_BLOCKERS`

请记住：本轮目标是最终达到哲学宝典级质量，不是快速糊一份。
