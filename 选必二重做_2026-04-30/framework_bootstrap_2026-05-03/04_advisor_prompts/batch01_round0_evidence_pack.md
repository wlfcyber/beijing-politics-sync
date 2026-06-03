# Batch 01 Trial 3 Round 0 Evidence Pack

## Phase

- batch_id: BATCH01_TRIAL3
- current_framework_version: V0_SCAFFOLD
- proposed_next_version: V1_CANDIDATE
- purpose: 用前三道主观题测试“主干高频 + 全量可归位 + 命题路径反推”的框架进化机制。

## Current Framework Summary

- 一核：以事实为根据、以法律为准绳，定分止争。
- 二线：权利保护与权利边界；法治规则与德治价值。
- 三问：判什么/怎么处理；凭什么；有什么意义。
- 四步：定主体关系 -> 找争点事实 -> 套法定要件 -> 落责任/效力/程序。
- 五域：合同消费者劳动；物权相邻继承家庭；人格权侵权；知识产权不正当竞争；纠纷解决生态公益与新业态。

## Batch Evidence Summary

| source_id | year | district | stage | q_no | type | evidence_level | legal_relation | dispute_focus | result_or_solution | proposition_goal | question_path | rubric_rewarded_action | current_framework_place | placement_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B01-Q1 | 2024 | 朝阳 | 二模 | 17 | subjective | formal_or_scoring_source | 平台企业与新就业形态劳动者 | 合作协议外观下是否构成事实劳动关系 | 仲裁支持经济补偿 | 用事实和要件识别劳动关系 | 事实 -> 要件 -> 裁决理由 -> 意义 | 三个从属性材料匹配 + 劳动关系归纳 + 意义分层 | 合同消费者劳动 / 劳动关系认定 | clear |
| B01-Q2 | 2024 | 海淀 | 一模 | 19 | subjective | reference_answer | 著作权人与未经许可使用者/竞争者 | 虚拟数字人视频使用是否侵权及不正当竞争 | 消除影响并赔偿损失 | 新技术场景下的权利保护和市场秩序 | 新现象 -> 权利保护 -> 市场秩序 | 著作权保护 + 未经许可使用 + 虚假宣传/不正当竞争 + 创新/秩序意义 | 知识产权不正当竞争 | reference_only_cannot_promote |
| B01-Q3 | 2024 | 海淀 | 二模 | 19 | subjective | formal_or_scoring_source | 遗赠扶养协议当事人与法定继承人 | 协议效力、扶养履行、遗产归属 | 确认协议有效并判遗产归居委会 | 继承/扶养制度中的公平正义和德治价值 | 具体争议 -> 裁判确认 -> 社会价值 | 法律确认 + 个案公平 + 养老司法理念 + 传统美德/核心价值观 | 物权相邻继承家庭 / 继承扶养 | clear |

## Frequency Snapshot

| candidate_node | hit_count | formal_scoring_count | representative_source_ids |
|---|---:|---:|---|
| 法律关系判断 | 3 | 2 | B01-Q1, B01-Q2, B01-Q3 |
| 事实 -> 要件匹配 | 3 | 2 | B01-Q1, B01-Q2, B01-Q3 |
| 责任/效力/程序/裁判结果落点 | 3 | 2 | B01-Q1, B01-Q2, B01-Q3 |
| 价值收束锚定具体领域 | 3 | 2 | B01-Q1, B01-Q2, B01-Q3 |
| 新技术知识产权/不正当竞争 | 1 | 0 | B01-Q2 |
| 继承扶养与德治价值 | 1 | 1 | B01-Q3 |
| 新就业形态劳动关系 | 1 | 1 | B01-Q1 |

## Hard Cases

| source_id | reason_hard_to_place | current_attempt | risk |
|---|---|---|---|
| B01-Q2 | reference_answer，不是 formal scoring source | 放入开放容器层 | 不能推动主干或作为评分细则证据 |

## Proposition Path Findings

| source_id | carrier_choice | question_path | legal_vs_value_balance | framework_implication |
|---|---|---|---|---|
| B01-Q1 | 平台经济典型案例 + 劳动关系资料包 | 事实 -> 要件 -> 裁决理由 -> 意义 | 法律推理与治理意义结合 | 强化“法律关系判断 + 要件匹配”主干 |
| B01-Q2 | 虚拟数字人 / AI 新技术案例 | 新现象 -> 权利保护 -> 市场秩序 | 规则和创新价值结合，但证据弱 | 作为新技术开放容器，待 formal 补强 |
| B01-Q3 | 遗赠扶养协议养老案例 | 具体争议 -> 裁判确认 -> 社会价值 | 法治价值较强但以具体法律关系为锚 | 强化“价值收束必须锚定具体法律关系” |

## Proposed Changes From Codex

| change_id | change_type | proposal | reason | evidence_needed |
|---|---|---|---|---|
| C1 | reorder | 五域降为题域容器，主干上升为“定关系 -> 找争点 -> 套要件 -> 落责任/效力/程序” | 三题均先考答题动作，不只是领域 | 需要更多 formal 主观题验证 |
| C2 | add_layer | 新增命题路径层 | 用户新增要求，且三题路径不同但可解释 | 每批都填 proposition_path |
| C3 | add_rule | 价值收束必须锚定具体法律关系 | B01-Q1 和 B01-Q3 均 formal 支撑 | 需更多意义类题验证 |
| C4 | open_container | AI/虚拟数字人/新技术知识产权暂为开放容器 | B01-Q2 证据弱但命题路径重要 | 寻找 formal 同类题 |

## Questions For GPT-5.5 Pro

1. 这三题是否足以说明主干应从“五域”改为“法律分析动作层”？
2. `价值收束必须锚定具体法律关系` 是否可以作为主干，还是应暂放开放容器？
3. B01-Q2 的新技术知识产权路径在 reference-only 情况下应如何保留而不污染主干？

## Questions For Claude Opus 4.7 Adaptive

1. 学生版是否应先教“定关系 -> 找争点 -> 套要件 -> 落结果”，再讲题域？
2. “命题路径层”怎样表达才不增加学生负担？
3. 意义类题如何避免学生背宏观空话？

## Forbidden

- 不发送本地绝对路径。
- 不发送大段原始试卷或大段细则全文。
- 不发送旧选必二结论。
- 不让模型决定本地证据事实。
