# 选必二框架自我进化协议

## 核心思想

框架不是一次性写出来的，而是在题源压力下不断进化出来的。每一次进化都必须同时经过：

- 本地题源和细则压力。
- 命题路径压力。
- GPT-5.5 Pro 的主干/全面压力。
- Claude Opus 4.7 Adaptive 的教学/迁移压力。
- Codex 的本地证据裁决。

## 命题路径反推

每道题进入框架前，必须先回答“这道题为什么会这样命制”。

### 反推字段

- `proposition_goal`：命题想培养哪种法治思维或能力。
- `carrier_choice`：为什么用案例、法条、法律现象或社会治理场景承载。
- `question_path`：设问路径是从总到分、从前到后、从事实到规范、从制度到价值，还是从具体争议到社会意义。
- `rubric_rewarded_action`：评分细则奖励的真正答题动作是什么。
- `legal_vs_value_balance`：本题更偏制度细节、法律推理、法治意义，还是三者结合。
- `framework_implication`：它强化主干、补开放容器，还是暴露框架缺口。

### 命题人图片带来的约束

- 选择题不能只归为“法治意义”，还要看制度自身内容、法定要件和细节边界。
- 主观题不能只做复杂法律职业分析，也不能只写宏观法治建设；必须看法律知识如何论证法治建设和社会经济发展。
- 框架不能只按教材目录，也不能只按案件类型；必须能解释命题从目标到载体、设问、细则的路径。
- 命题路径解释不清时，标记 `proposition_path_uncertain`，不得硬塞进已有框架。

## 两层框架结构

框架始终分为两层：

### 主干高频层

进入条件：

- 多题反复出现。
- 正式细则反复给分。
- 是学生遇到新题时必须先想到的答题动作。
- 能统摄多个具体题域。

### 开放容器层

进入条件：

- 低频但真实出现。
- 新题可暂时归位。
- 目前证据不足以升为主干。
- 有助于防止框架漏题。

开放容器层不是垃圾桶。每个容器都要写清：它容纳什么、边界是什么、何时升为主干。

## Framework Council 每轮流程

### Round 0：Evidence Pack

Codex 生成：

- 当前框架版本。
- 本批题目案例卡。
- 每题命题路径反推。
- 频次统计。
- 框架归位矩阵。
- 归位困难题。
- 新增/删除/改名候选。
- 证据风险：reference-only、unknown、uncertain、OCR 不稳、选择题未锁答案。

### Round 1：Independent Blueprints

真实调用 GPT-5.5 Pro：

- 提出主干排序。
- 找出覆盖漏洞。
- 判断哪些节点应升主干、降容器、合并或拆分。
- 给出版本升级条件。

真实调用 Claude Opus 4.7 Adaptive：

- 判断学生是否能学会。
- 找出过抽象、过密、不可迁移的节点。
- 提出课堂表达和答题动作重构。
- 判断哪些节点适合口诀化，哪些只能做开放容器。

### Round 2：Cross-Critique

将 GPT 原文交给 Claude：

- Claude 必须指出 GPT 方案的教学风险、学生误用风险、过度抽象风险。

将 Claude 原文交给 GPT：

- GPT 必须指出 Claude 方案的覆盖风险、证据风险、主干弱化风险。

### Round 3：Convergence Brief

Codex 汇总：

- 双方一致建议。
- 双方冲突建议。
- 双方都没看到但本地证据显示的问题。
- 每条建议需要核验的题源/细则证据。

### Round 4：Local Evidence Decision

Codex 裁决字段：

- `accepted`
- `partially_accepted`
- `rejected_no_evidence`
- `rejected_student_risk`
- `deferred_more_batches`
- `candidate_pending_real_call`

### Round 5：Version Update

每个版本必须同步更新：

- `FRAMEWORK_V*.md`
- `FRAMEWORK_CHANGELOG.md`
- `FRAMEWORK_COVERAGE_MATRIX.csv`
- `FRAMEWORK_GAP_LIST.md`
- `MODEL_ADVICE_LOG.md`

## 版本升级硬门槛

只有当修改满足至少一条，才允许升级：

- 提高主干高频清晰度。
- 提高全题覆盖率。
- 消除硬塞归位。
- 降低学生误用风险。
- 修正证据边界。
- 能让新题更自然归位。

## 禁止事项

- 禁止 Codex 单独改框架后声称 GPT/Claude 已参与。
- 禁止把 GPT/Claude 的一致意见当作证据。
- 禁止为了全面把所有低频点堆成并列主干。
- 禁止为了主干简洁把归不进去的题硬塞。
- 禁止未完成真实调用时把版本标为 accepted。
