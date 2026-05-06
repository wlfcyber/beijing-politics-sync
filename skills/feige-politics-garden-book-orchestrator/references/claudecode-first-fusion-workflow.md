# ClaudeCode 厚内容矿优先 + Codex 融合审稿工作流

适用场景：飞哥政治庄园整本书、整模块、全量宝典、终极文档任务。尤其适用于用户说“按哲学宝典那次成功工作流”“两线/四线一起跑”“Codex 自己也要跑”“ClaudeCode 跑出来更充实”“最终要 Word/PDF 成品”的任务。

## 成功复盘结论

2026-05-02 必修四哲学宝典的成功，不是 Codex 单线生产成功，而是分工成功：

- Codex 早期补全版较干净、框架更稳，但内容偏瘦。
- ClaudeCode 从 0 重跑版内容更厚、题源覆盖更足、材料触发链更密，但需要清洗、去审计话术、统一框架、锁定硬样本和 Word 验收。
- 最终双终极融合版采用的是“ClaudeCode 厚内容 + Codex 框架/证据/格式/验收”的合体模式。

本工作流的第一原则：

> ClaudeCode 是重型内容矿，Codex 是总控、并行生产者、融合器、审稿人和验收闸。不要让 Codex 的薄候选稿冒充全量底稿，也不要把 ClaudeCode 降级成普通 reviewer。

2026-05-06 复盘确认：

> 实话实说，在必修四哲学宝典那次任务里，相同大方向指令下，ClaudeCode 跑出的内容确实比 Codex 厚，很多材料触发和答案落点也更充实。Codex 的不可替代价值是把这批厚内容按用户框架、证据边界、硬样本、学生版洁净度和 Word 交付标准收成终稿。因此后续选必三等整本书任务必须默认 `ClaudeCode thick body first, Codex fusion and acceptance second`。

## 角色定位

### Codex

Codex 必须同时做三件事：

1. 总控：维护 notebook、MASTER_REQUIREMENTS、SOURCE_LEDGER、COVERAGE_MATRIX、PROGRESS、DECISION_LOG、FINAL_ACCEPTANCE_REPORT。
2. 并行生产 A 线：自己读源、抽题、写条目、关套卷，留下 `codex_lane/` 证据。
3. 融合审稿：比较 Codex A 与 ClaudeCode B，裁决冲突，回源核验，清洗学生版，跑 Governor/Confucius/Word 验收。

Codex 不得只当“监工”。但在最终内容厚度上，Codex 也不得把自己的较薄稿当默认主稿。

### ClaudeCode

ClaudeCode 是生产 B 线，默认承担厚内容矿：

- 从原始材料和可复用 cache 出发，独立穷尽题源。
- 逐套/逐题形成 source-backed entries、coverage、suite reports、blockers。
- 最终内容组织必须服务用户框架，不按试卷流水账堆砌。
- 输出要充实：每个框架节点下面必须配真实模拟题，且每题有可迁移分析流程。

当用户要求“真实窗口工作”时，ClaudeCode 必须在可见窗口或用户指定环境中运行，CLI 只能作为临时辅助，不能替代正式生产线。

### Claude Opus 4.7 Adaptive

Claude Opus 是教学表达成品化 lane：

- 只在证据锁定后改写表达、结构、学生可读性。
- 重点改“怎么讲给学生”“怎么迁移到新题”“答案句怎么自然落地”。
- 不得新增未经本地证据验证的知识点、评分术语或答案结论。

### GPT-5.5 Pro

GPT-5.5 Pro 是总审稿/压力测试 lane：

- 查概念错误、漏题、框架错挂、学生迁移失败、题量不足、内容薄弱。
- 阶段性成果和最终候选稿都要给 GPT 审。
- GPT 的建议必须回到 Codex 本地证据核验后才能进入正文。

不得把 Codex 自写的“假 GPT 意见”当成 GPT-5.5 Pro。

### Governor 与 Confucius

Governor 负责拒绝假闭环；Confucius 负责从零基础学生视角读最终学生版，只看成品，不看审计文件，判断能不能学会。

## 标准产物顺序

### Phase 0：硬规则同步

先读并写入：

- 总 skill 与分支 skill。
- 用户小本本/硬性要求记事本。
- 本轮 MASTER_REQUIREMENTS。
- 旧线继承边界：哪些可作定位，哪些不可作证据。
- 用户框架：本书到底按什么框架组织。

新要求如果来自用户纠错，必须先写入 notebook，再继续生产。

### Phase 1：源材料与控制文件

建立本轮工作目录，至少包含：

- `00_control/MASTER_REQUIREMENTS.md`
- `00_control/PROGRESS.md`
- `00_control/DECISION_LOG.md`
- `00_control/SOURCE_LEDGER.csv`
- `00_control/COVERAGE_MATRIX.csv`
- `codex_lane/`
- `claudecode_lane/`
- `fusion/`
- `gpt55_review/`
- `opus_writer/`
- `governor_confucius/`
- `outputs/`

源材料处理原则：

- cache-first，但不是 cache-only。
- PDF、Word、PPT、图片、扫描件、漫画、表格都要调工具处理。
- 题干/选项/图片/表格缺失时，回原件渲染、截图、OCR、视觉读取，不得猜。

### Phase 2：两条生产线并跑

Codex A 和 ClaudeCode B 都要产出条目，但侧重点不同：

- Codex A：证据边界更严，框架与审计更稳。
- ClaudeCode B：内容挖掘更厚，题源覆盖更宽，材料触发链更充实。

每条条目至少包含：

- 题目来源
- 材料信号/题干信号
- 可写原理/方法/题型
- 为什么能想到
- 答题动作
- 答案落点
- 易错陷阱
- 同类题

选择题还必须包含完整选项、正确项理由、错项陷阱。

### Phase 3：ClaudeCode 厚内容矿验收

进入融合前，ClaudeCode B 不能只交“代表题”或“摘要”。必须有独立验收：

- 条目数量是否接近源题池规模。
- evidence rows 是否全部裁决为 body/index/blocked。
- 每个框架节点下面是否有模拟题。
- 每个题型下面是否挂全部同类题，而非只放代表例。
- blocked 是否有具体证据原因。
- 学生正文是否已去掉审计话术。

若 ClaudeCode 输出明显比 Codex 更充实，融合时默认优先吸收 ClaudeCode 的内容厚度，但必须由 Codex 回源核验和规范化。

### Phase 4：融合规则

融合时不按“谁先写的”决定，而按以下顺序裁决：

1. 证据等级更高者优先。
2. 用户框架位置更准确者优先。
3. 学生可迁移解释更完整者优先。
4. 同题冲突必须回源，不得平均折中。
5. ClaudeCode 更充实且证据合格时，优先吸收或替换 Codex 薄条目。
6. Codex 更干净但偏薄时，不得用“格式好”压掉 ClaudeCode 的有效内容。
7. 重复题可以合并，但不能把不同触发点压没。

融合报告必须统计：

- Codex 原有条目数
- ClaudeCode 原有条目数
- ClaudeCode 独有导入数
- ClaudeCode 替换 Codex 数
- Codex 覆盖保留数
- ClaudeCode rejected 数及原因
- 最终正文条目数
- 四字段缺失数
- 学生禁词命中数

## 最终正文组织规则

最终学生版必须按用户框架组织，不按试卷流水账组织。

### 必修四哲学

按哲学原理/方法论节点组织：

- 每个原理/方法论下面挂真实模拟题。
- 每题固定 `材料触发点 -> 设问 -> 为什么能想到 -> 答案落点`。
- 选择题显示完整选项和错项陷阱。

### 选必三思维部分

按“思维类型 -> 思维特点/子方法 -> 对应模拟题”组织。

选必三不得重复后续失败路径：不能让 Codex 先产出一个按大题/地区/时间展开的小候选稿，再试图通过格式和索引补成宝典。正确路径是 ClaudeCode 先按框架节点跑厚内容矿，Codex 同步跑自己的证据线，然后以 ClaudeCode 的内容密度为主要吸收对象做融合。

例如：

- 科学思维
  - 客观性
  - 预见性
  - 可检验性
- 创新思维
  - 三新
  - 发散思维
  - 聚合思维
  - 逆向思维
  - 联想思维
  - 超前思维
- 辩证思维
  - 整体性
  - 动态性
  - 分析与综合
  - 质量互变
  - 适度原则

每个子节点下面必须有模拟题和固定分析流程：

- 材料怎么看
- 该写哪个思维方法
- 为什么触发
- 答案句怎么落
- 易错项怎么避

### 选必三推理部分

按推理题型树组织，并在每个题型下面挂全部对应题：

- 概念与定义
- 概念外延关系
- 判断类型识别
- 联言判断与联言推理
- 相容/不相容选言推理
- 充分/必要/充要条件假言推理
- 三段论结构题与谬误题
- 逻辑三律
- 归纳推理
- 类比推理
- 论证评价与逻辑错误

每道推理题必须写清：

- 题型归属
- 逻辑形式
- 规则口令
- 有效式或错误式
- 解题动作
- 答案落点
- 易错陷阱
- 同类题

## 题量与覆盖闸口

不得用小候选稿冒充全量稿。

硬闸：

- 题量必须与 source pool / evidence pool / control base 相匹配。
- 如果 evidence pool 有 74 行，29 条正文不能叫终稿。
- 如果用户判断源卷约 60 套、预期 90-120 题，候选稿必须解释差距；不能直接 Word。
- index-only 不是 body 覆盖；每一条都要有 body/index/blocked 决策。

进入 Word 前必须有：

- coverage matrix 完整。
- blocked 明细完整。
- index false positives 清零。
- 选择题完整选项可见。
- 主观题教学链完整。
- 学生正文内部审计标记清零。
- GPT/ClaudeCode/Claude Opus/Governor/Confucius 所需 gates 完成或明确用户豁免。

## 外部模型交互规则

Codex 可以准备上传包和 prompt，但不能让用户自己找路径。默认应：

- 自己打包。
- 自己打开/上传到 GPT 或 Claude 可见窗口，除非用户要求手动代传。
- 不点击不确定的 Stop/Send 按钮。
- 若外部模型停止、限额、账号异常，要记录 `real_call_pending`，但继续可安全推进的本地工作。

每次外部审查必须保存：

- 原文 raw
- digest
- accepted/rejected/deferred advice log
- 本地证据核验结果
- patch queue
- post-patch audit

## ClaudeCode 长 prompt 骨架

给 ClaudeCode 的 prompt 必须包含：

```text
你是飞哥政治庄园本轮整本书生产 B 线，不是 reviewer。

重要复盘结论：
- 在 2026-05-02 必修四哲学宝典成功案例中，ClaudeCode 跑出的内容比 Codex 更厚、更充实，最终成品大量吸收了 ClaudeCode 内容。
- 本轮也必须把你作为厚内容矿生产线，而不是审稿人。Codex 会并行跑 A 线并负责融合、证据裁决、清洗和 Word 验收，但不得用薄 Codex 稿替代你的厚内容矿。

本轮目标：
- 从 0 或从用户授权的源材料开始，生成可并入最终宝典的厚内容矿。
- 最终正文必须按用户框架组织，不按试卷流水账堆砌。
- 每个框架节点下面必须配真实模拟题；每题必须有材料信号、为什么触发、答案落点、易错陷阱、同类题。

硬规则：
- 读取总 skill、分支 skill、用户小本本、MASTER_REQUIREMENTS。
- 不继承旧结论，旧文件只能按本轮规则用于定位或对比。
- PDF、Word、PPT、图片、扫描件、漫画、表格都要调工具处理，不能因一个工具失败放弃。
- 不猜答案，不把普通参考答案升级为评分细则。
- blocked 要写清 source/answer/visual/reasoning blocker。
- 学生正文不能出现审计语言、路径、line id、file id、OCR/debug、评标、参考答案等。

输出：
- SOURCE_LEDGER.csv
- COVERAGE_MATRIX.csv
- entries.jsonl 或 entries/*.md
- suite_reports/
- blockers.csv
- framework_node_matrix.csv
- thick_body_REVIEW_ONLY.md
- fusion_candidates.csv

验收：
- 条目数与 source pool/evidence pool 匹配。
- 每个用户框架节点都有题目挂载或 blocked 说明。
- 选择题显示完整选项、正确项、错项陷阱。
- 主观题有材料触发点、设问、为什么能想到、答案落点。
- 推理题有逻辑形式、规则口令、有效/错误式和同类题。
```

## 常见失败模式

发现以下任一情况，必须停下返修，不得进入 Word：

- Codex 产出薄稿后直接叫“终稿”。
- ClaudeCode 只做 reviewer，没有独立厚内容矿。
- 正文按试卷/题号流水账组织，而不是按用户框架组织。
- “同类题索引”代替正文覆盖。
- 选择题缺选项或只写答案字母。
- 推理题只写知识点，不写逻辑形式。
- 思维题只写“创新思维/科学思维”总称，不拆到三性、三新、子方法。
- review-only 元数据、question_id、phase 字段进入学生稿。
- Word/PDF 在内容闸口前生成。
- GPT/Claude 外部模型没有真实审查，却在报告里写 PASS。

## 最终交付

最终交付必须包括：

- 学生清洁 Markdown。
- 经过 Word 打开/保存/渲染验收的 `.docx`。
- 可行时导出的 PDF 或截图审计附件。
- traceability matrix。
- fusion report。
- final acceptance report。

最终报告必须明说：

- 哪些内容来自 Codex。
- 哪些内容来自 ClaudeCode。
- 哪些被 Claude Opus 改写表达。
- GPT 提了哪些 must-fix，如何处理。
- Governor/Confucius 是否通过。
- 哪些题被 blocked，为什么。

一句话闭环标准：

> 最终作品必须像哲学宝典双终极融合版一样：ClaudeCode 提供足够厚的内容血肉，Codex 把证据、框架、学生化、外审和 Word 成品全部收住。
