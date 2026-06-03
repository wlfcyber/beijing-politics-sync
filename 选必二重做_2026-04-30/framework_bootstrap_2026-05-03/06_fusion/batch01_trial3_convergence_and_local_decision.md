# Batch 01 Trial 3 融合与本地裁决

日期：2026-05-03

## 真实调用与隔离记录

本批次遵守用户新增的会话隔离要求：不复用其他项目正在运行的 GPT、Claude、ClaudeCode 对话或工作目录。

| lane | 状态 | 输出 |
|---|---|---|
| GPT-5.5 independent blueprint | cli_provisional_advice_only_web_visible_pro_pending | `05_advisor_reports/gpt55/batch01_trial3_gpt55_framework_council.md` |
| Claude Opus independent blueprint | cli_provisional_advice_only_adaptive_thinking_pending | `05_advisor_reports/claude_opus/batch01_trial3_claude_opus_framework_council.md` |
| GPT-5.5 critique of Claude | cli_provisional_advice_only_web_visible_pro_pending | `05_advisor_reports/gpt55/batch01_trial3_gpt55_cross_critique_of_claude.md` |
| Claude Opus critique of GPT | cli_provisional_advice_only_adaptive_thinking_pending | `05_advisor_reports/claude_opus/batch01_trial3_claude_cross_critique_of_gpt.md` |
| ClaudeCode B production lane | not_run_this_trial | 用户提醒 ClaudeCode 正在跑其他项目；本批先不触碰该线程，后续若启用必须新开专用会话/目录 |

说明：本批 GPT 不是通过 ChatGPT 网页版对话完成，而是通过本机 `codex exec -m gpt-5.5` 调用 OpenAI `gpt-5.5` 模型；Claude 也不是通过用户可见的 Claude 网页端 Adaptive Thinking 模式完成，而是通过 `claude -p --model opus` CLI 完成。因此二者都只能算 `cli_provisional_advice`。用户正式要求的 `GPT-5.5 Pro` 与 `Claude Opus 4.7 Adaptive Thinking` gate 仍为 `web_visible_pro_adaptive_call_pending`。

## 本批证据边界

- 样本数：3 道主观题。
- formal_or_scoring_source：2 道。
- reference_answer：1 道，不能推动主干升级。
- 题型边界：尚未覆盖选择题、纯程序题、纯效力题、纯比较题、纯意义题。

## 四份报告的一致点

1. `V0_SCAFFOLD` 可以作为起点，但不能定稿。
2. “五域”不应作为唯一主干。前三题真正反复出现的是答题动作：判法律关系、抓关键争议事实、对应规则/条件、落到结果。
3. `B01-Q2` 只能进入开放观察容器，不能用 reference answer 推动正式框架。
4. 价值表达必须锚定具体法律关系，不能脱离案件写必修三式宏观法治空话。
5. 必须新增命题路径层，追问命题目标、载体选择、设问路径、细则奖励动作。
6. 当前只能建立 `V1_CANDIDATE_TRIAL3`，不能发布正式 V1。

## 主要分歧

| issue | GPT 倾向 | Claude 倾向 | Codex 本地裁决 |
|---|---|---|---|
| 五域位置 | 降为开放容器 | 保留为知识抓手 B 轴 | 修改后接受：学生背诵主干不以五域为先，但教师覆盖矩阵和复习索引保留五域 B 轴 |
| 四步措辞 | 定关系 -> 找争点 -> 套要件 -> 落结果 | 去法考化，避免“套要件”过专业 | 接受 Claude 修正：学生版改为“定关系 -> 抓争议 -> 对规则/条件 -> 落处理” |
| 价值层 | 可作第五个主干规则 | 只在意义类题条件触发 | 修改后接受：写成“价值一规”，不是默认第五步；设问有意义/认识/价值时启用 |
| 三问 | 可合并进结果落点 | 学生层删掉 | 折中：学生不背“三问”，教师后台保留为验收检查：判什么、凭什么、有什么意义 |
| 命题路径层 | 教师框架层完整保留 | 学生侧压成载体-问点-收束 | 双视图接受：教师后台四段，学生看题三段 |

## 本地接受项

### Accepted

- 主干动作链作为下一批测试主线：`定关系 -> 抓争议 -> 对规则/条件 -> 落处理`。
- 命题路径作为每题必填字段：`命题目标 -> 载体选择 -> 设问路径 -> 细则奖励动作`。
- `B01-Q2` 标为 `reference_only_high_authenticity_container`，只能作开放观察题。
- 删除独立的空泛法治/德治价值主干节点。
- 所有模型建议进入日志后，必须回到题面和细则裁决。

### Partially Accepted

- 五域不作为学生第一背诵主干，但保留为知识抓手和覆盖矩阵。
- 价值收束不作为默认第五步，改为条件触发规则：设问问“意义、认识、社会价值、启示”时启用。
- 三问不进入学生背诵层，但保留为教师后台验收规则。

### Deferred

- `载体 -> 问点 -> 收束` 是否能覆盖选择题和小题。
- 四步动作链是否能覆盖纯程序题、纯效力题、纯比较题。
- 新技术知识产权是否从开放观察容器升为正式高频专题。
- “意义类题必须先点法律关系”是否适用于纯意义题。

### Rejected For Now

- 直接宣布 V1 正式定稿。
- 把 reference answer 当成 scoring source。
- 把五域完全删出可见框架。
- 把“锚价值”固定为所有题默认第五步。

## V1 Candidate Trial3

### 教师后台层

1. 命题路径：命题目标 -> 载体选择 -> 设问路径 -> 细则奖励动作。
2. 答题动作：定关系 -> 抓争议 -> 对规则/条件 -> 落处理。
3. 条件价值：先点本案法律关系和处理结果，再上升到制度、秩序、价值。
4. 覆盖索引：合同消费者劳动 / 物权相邻继承家庭 / 人格权侵权 / 知识产权不正当竞争 / 纠纷解决生态公益新业态。
5. 后台验收：判什么 / 凭什么 / 有什么意义。

### 学生试用层

看题三段：

- 载体：题给了什么法律生活场景。
- 问点：题到底问成立、有效、侵权、谁担责、怎么处理，还是意义。
- 收束：最后要落到处理结果，还是落到社会价值。

答题四步：

1. 定关系：这是谁和谁，是什么法律关系。
2. 抓争议：材料里真正争的是什么事实或权利义务。
3. 对规则/条件：把材料事实对应教材法律规则。
4. 落处理：支持谁、为什么、怎么处理。

价值一规：

- 问意义、认识、社会价值时，先说本案是什么法律关系、判了什么，再说公平、秩序、诚信、法治、德治或治理意义。
- 不许跳过法律关系直接喊价值口号。

## 前三题归位

| id | 题目 | 证据 | 归位 |
|---|---|---|---|
| B01-Q1 | 2024 朝阳二模 17 | formal_or_scoring_source | 平台劳动关系；定关系、抓争议、对从属性条件、落仲裁结果、分析法律/道德/经济意义 |
| B01-Q2 | 2024 海淀一模 19 | reference_answer | 新技术知识产权与不正当竞争；开放观察容器，不能推动主干 |
| B01-Q3 | 2024 海淀二模 19 | formal_or_scoring_source | 遗赠扶养与继承；定关系、抓协议效力和履行争议、对制度规则、落判决结果、分析社会价值 |

## 下批验证任务

下一批至少补 5-6 道 `formal_or_scoring_source` 主观题，优先寻找：

- 程序/纠纷解决题：仲裁、诉讼、调解、司法确认。
- 效力题：合同有效、无效、可撤销、效力待定。
- 消费者或格式条款题。
- 人格权/侵权题。
- 知识产权/不正当竞争 formal 题。
- 纯意义或社会价值题。

升级门槛：

- 主干节点至少需要 3 道 formal 支撑，且跨 2 个以上题域。
- 命题路径 `载体 -> 问点 -> 收束` 累计 10 题以上可还原后，才可进入公开稳定层。
- 开放容器升主干，必须有 formal 同向重复，reference answer 不够。
