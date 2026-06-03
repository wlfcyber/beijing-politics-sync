# Web Claude Opus 4.7 Adaptive Thinking Prompt - Batch01 Trial3

请在 Claude 网页端新建一个独立对话，确认当前模式为 `Claude Opus 4.7` 且启用 `Adaptive Thinking` 后使用本 prompt。

项目：选必二《法律与生活》框架实验。

禁止继承其他项目上下文；禁止把其他正在运行的项目、对话、线程、文件结论带入本任务。

你是真实的 Claude Opus 4.7 Adaptive Thinking，本轮任务不是写最终答案，而是参加飞哥政治庄园选必二《法律与生活》框架制定委员会。请从学生可学性、迁移性、过抽象风险、框架压缩、命题路径表达角度审查。你不是证据权威；你的建议必须等待 Codex 回到本地题面和评分细则裁决。

## 任务目标

基于下面的 Batch01 前三道主观题证据包，研究选必二框架如何同时满足：

1. 主干高频：最高频、最常进入评分细则、最能迁移的法律思维和答题动作必须突出。
2. 全面可归位：所有旧题、新题、新细则都应有自然位置；归不进去要暴露框架缺口。
3. 命题路径：从命题目标、载体选择、设问路径、细则奖励动作反推框架，而不是只按教材目录分类。
4. 学生可学性：学生第一层记忆不能过载，必须能迁移到未见过的新案例。
5. 证据边界：reference answer 不能升格为 formal scoring source。

## 请输出

```markdown
# Claude Opus 4.7 Adaptive Thinking Web Framework Council Report

## 0. Mode Confirmation
请写明：本报告基于用户可见的 Claude Opus 4.7 Adaptive Thinking 网页端新对话生成。

## 1. Learnability Diagnosis

## 2. Student-Usable Trunk

## 3. Teacher Backend Framework

## 4. Proposition Path For Students

## 5. Open Containers And Knowledge Anchors

## 6. Risks Of Abstraction Or Misuse

| node | risk | fix |
|---|---|---|

## 7. Proposed Student-Facing Structure

## 8. Evidence/Placement/Proposition-Path Risks

## 9. Version Upgrade Criteria

## 10. Questions For GPT-5.5 Pro
```

不要编造具体试卷事实；没有证据就写“需本地核验”。

## Evidence Pack

### Current Framework V0

- 一核：以事实为根据、以法律为准绳，定分止争。
- 二线：权利保护与权利边界；法治规则与德治价值。
- 三问：判什么/怎么处理；凭什么；有什么意义。
- 四步：定主体关系 -> 找争点事实 -> 套法定要件 -> 落责任/效力/程序。
- 五域：合同消费者劳动；物权相邻继承家庭；人格权侵权；知识产权不正当竞争；纠纷解决生态公益与新业态。

### Batch Evidence Summary

| source_id | year | district | stage | q_no | type | evidence_level | legal_relation | dispute_focus | result_or_solution | proposition_goal | question_path | rubric_rewarded_action | current_framework_place | placement_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B01-Q1 | 2024 | 朝阳 | 二模 | 17 | subjective | formal_or_scoring_source | 平台企业与新就业形态劳动者 | 合作协议外观下是否构成事实劳动关系 | 仲裁支持经济补偿 | 用事实和要件识别劳动关系 | 事实 -> 要件 -> 裁决理由 -> 意义 | 三个从属性材料匹配 + 劳动关系归纳 + 意义分层 | 合同消费者劳动 / 劳动关系认定 | clear |
| B01-Q2 | 2024 | 海淀 | 一模 | 19 | subjective | reference_answer | 著作权人与未经许可使用者/竞争者 | 虚拟数字人视频使用是否侵权及不正当竞争 | 消除影响并赔偿损失 | 新技术场景下的权利保护和市场秩序 | 新现象 -> 权利保护 -> 市场秩序 | 著作权保护 + 未经许可使用 + 虚假宣传/不正当竞争 + 创新/秩序意义 | 知识产权不正当竞争 | reference_only_cannot_promote |
| B01-Q3 | 2024 | 海淀 | 二模 | 19 | subjective | formal_or_scoring_source | 遗赠扶养协议当事人与法定继承人 | 协议效力、扶养履行、遗产归属 | 确认协议有效并判遗产归居委会 | 继承/扶养制度中的公平正义和德治价值 | 具体争议 -> 裁判确认 -> 社会价值 | 法律确认 + 个案公平 + 养老司法理念 + 传统美德/核心价值观 | 物权相邻继承家庭 / 继承扶养 | clear |

### Frequency Snapshot

| candidate_node | hit_count | formal_scoring_count | representative_source_ids |
|---|---:|---:|---|
| 法律关系判断 | 3 | 2 | B01-Q1, B01-Q2, B01-Q3 |
| 事实 -> 要件匹配 | 3 | 2 | B01-Q1, B01-Q2, B01-Q3 |
| 责任/效力/程序/裁判结果落点 | 3 | 2 | B01-Q1, B01-Q2, B01-Q3 |
| 价值收束锚定具体领域 | 3 | 2 | B01-Q1, B01-Q2, B01-Q3 |
| 新技术知识产权/不正当竞争 | 1 | 0 | B01-Q2 |
| 继承扶养与德治价值 | 1 | 1 | B01-Q3 |
| 新就业形态劳动关系 | 1 | 1 | B01-Q1 |

### Hard Cases

| source_id | reason_hard_to_place | current_attempt | risk |
|---|---|---|---|
| B01-Q2 | reference_answer，不是 formal scoring source | 放入开放容器层 | 不能推动主干或作为评分细则证据 |

### Proposition Path Findings

| source_id | carrier_choice | question_path | legal_vs_value_balance | framework_implication |
|---|---|---|---|---|
| B01-Q1 | 平台经济典型案例 + 劳动关系资料包 | 事实 -> 要件 -> 裁决理由 -> 意义 | 法律推理与治理意义结合 | 强化“法律关系判断 + 要件匹配”主干 |
| B01-Q2 | 虚拟数字人 / AI 新技术案例 | 新现象 -> 权利保护 -> 市场秩序 | 规则和创新价值结合，但证据弱 | 作为新技术开放容器，待 formal 补强 |
| B01-Q3 | 遗赠扶养协议养老案例 | 具体争议 -> 裁判确认 -> 社会价值 | 法治价值较强但以具体法律关系为锚 | 强化“价值收束必须锚定具体法律关系” |

### Current Codex Candidate

Codex 只提出候选，不要求你照单全收：

- 教师后台：命题目标 -> 载体选择 -> 设问路径 -> 细则奖励动作。
- 学生看题：载体 -> 问点 -> 收束。
- 答题四步：定关系 -> 抓争议 -> 对规则/条件 -> 落处理。
- 价值一规：问意义时，先说本案法律关系和处理结果，再上升到制度、秩序、价值。
- 五域：不作唯一主干，但保留为覆盖索引和知识抓手。

请重点压力测试：这个候选框架是否过抽象、是否仍然太像法考、是否会让学生在考场上多套一层、是否需要保留五域作为知识抓手、是否应该把命题路径做成教师后台而不是学生背诵内容。
