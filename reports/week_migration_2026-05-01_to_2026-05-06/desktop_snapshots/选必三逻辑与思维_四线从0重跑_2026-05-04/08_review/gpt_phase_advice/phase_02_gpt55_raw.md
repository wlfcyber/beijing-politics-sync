## 1. 阶段判断：CONDITIONAL GO

允许进入下一阶段：全量逐套逐题扫描与分类。
但只允许进入扫描、分类、挂载、差异复核阶段。严禁进入学生稿、Claude/Opus 成文化、Word/PDF、最终 PASS。

判断理由很明确：

1. Phase 02 已证明四线机制开始真实运转。Codex lane A 做了硬样本回源，ClaudeCode lane B 独立复核，随后做了 A/B 融合与冲突处理。
2. 五个硬样本覆盖了关键风险类型：思维主观题、辩证思维可选角度、创新思维、选择题完整选项、推理综合题。
3. HS02 的纠错说明流程有效，已经阻止了把可选角度池误写成三点必答。
4. 56 个优先原始源文件已批量抽取，且 missing=0、errors=0，说明下一阶段没有理由因格式复杂而停滞。
5. 但当前只完成五个硬样本，coverage 尚未全量到 suite/question 级。旧稿 locator 行仍在 top-level SOURCE_LEDGER.csv，PPTX 内嵌图片和图形批注尚未全部视觉读取，HS02 仍有 LOCKED_PENDING_VISUAL 状态。

因此结论是：

```text
CONDITIONAL GO for 全量逐套逐题扫描与分类
NO-GO for 学生稿
NO-GO for Claude/Opus 成文化
NO-GO for Word/PDF
NO-GO for PASS
```

进入下一阶段的边界条件：

```text
1. 所有题必须从 raw source 回源。
2. 旧稿只能定位，不能继承结论。
3. 所有题必须有 stable locator。
4. 推理题必须进入题型挂载矩阵。
5. 思维题必须进入材料信号链矩阵。
6. 无答案、无选项、无细则、视觉未核读的题必须进入 blocker。
7. HS02 不得进入学生稿，直到最终视觉确认完成。
```

---

# 2. 下一阶段必须产出的文件清单

建议将下一阶段命名为：

```text
Phase 03 full suite question scan and classification
```

必须产出以下文件。缺任一类，不能进入后续成文化阶段。

## 2.1 干净源文件总账

```text
phase03_raw_source_registry.csv
phase03_raw_source_registry.md
phase03_locator_only_removed_or_isolated.md
phase03_source_reading_methods.md
phase03_source_failures_and_fallbacks.md
```

硬要求：

```text
1. top-level SOURCE_LEDGER.csv 中旧稿 locator 行必须剥离。
2. raw source、locator only、旧稿 failure reference 必须分表。
3. 每个原始文件必须标明读取方法。
4. 每个 PDF 必须标明文本读取与命中页渲染状态。
5. 每个 PPTX 必须标明 slide 文本、内嵌图片、图形批注是否处理。
6. 每个 DOCX 必须标明正文、表格、图片题是否处理。
7. RTF 必须标明转换与读取状态。
```

## 2.2 套题级总账

```text
phase03_suite_registry.csv
phase03_suite_registry.md
phase03_suite_duplicate_map.csv
phase03_missing_expected_sources.md
phase03_2026_二模_missing_or_blocked.md
```

每个 suite 至少包含：

```text
suite_id
source_id
文件名
地区
年份
考试阶段
题目范围
是否含思维部分
是否含推理部分
题目页范围
答案页范围
评分细则页范围
讲评页范围
题量检测值
题量确认值
视觉风险等级
是否进入全量扫描
```

必须单独记录：

```text
1. 2026 二模在已扫 source roots 未发现。
2. 未发现不等于不存在。
3. 除非新文件出现，否则进入 missing/blocked。
```

## 2.3 逐题覆盖矩阵

```text
phase03_question_coverage_matrix.csv
phase03_question_coverage_matrix.xlsx
phase03_question_coverage_matrix.md
```

每题至少一行。字段必须包含：

```text
question_id
suite_id
source_id
stable_locator
原始题号
题型：选择题 / 主观题 / 图表题 / 漫画题 / 组合题 / 讲评题
部分归属：思维 / 推理 / 交叉 / 待判
是否完整题干
是否完整选项
是否有答案
是否有评分细则
是否有讲评
是否需要视觉核读
是否已视觉核读
知识节点
题型节点
材料信号
设问动作
答案落点状态
推理规则状态
blocked_status
blocked_reason
lane_A_classification
lane_B_classification
A_B_conflict_status
final_classification
```

硬要求：

```text
1. 不能只统计题目数量。
2. 不能只统计知识点数量。
3. 必须到每一道题。
4. 一题多问拆成子题，例如 Q21-1、Q21-2。
5. 一题多法必须有 primary 与 secondary 挂载。
```

## 2.4 思维部分材料信号链矩阵

```text
phase03_thinking_signal_chain_matrix.csv
phase03_thinking_signal_chain_matrix.md
```

字段必须包含：

```text
question_id
suite_id
stable_locator
思维知识节点
材料信号
可写思维或方法
答题动作
设问类型
为什么能想到
答案落点
来源例题
同类题
易错点
是否可入学生稿
```

验收口径：

```text
材料信号 -> 可写思维/方法 -> 答题动作 -> 来源例题
```

任何思维题缺少材料信号或答题动作，不能进入宝典正文。

## 2.5 推理部分题型挂载矩阵

```text
phase03_reasoning_typology_tree.md
phase03_reasoning_question_attachment_matrix.csv
phase03_reasoning_question_attachment_matrix.xlsx
phase03_reasoning_rule_slogans.md
phase03_reasoning_trap_matrix.md
phase03_reasoning_action_templates.md
```

字段必须包含：

```text
question_id
suite_id
stable_locator
原始题号
primary_reasoning_type
secondary_reasoning_type
logical_form
rule_slogan
valid_pattern
invalid_pattern_or_trap
same_type_question_ids
answer_key
explanation_status
blocked_status
```

硬要求：

```text
1. coverage matrix 中归为推理的题，必须全部出现在 attachment matrix。
2. attachment matrix 中的题，后续正文必须逐题出现。
3. 推理综合题不能只写综合，必须拆出具体规则。
4. HS05 这类题必须挂矛盾律、充分条件假言推理误用、三段论中项不周延。
5. HS01 Q19(1) 必须作为推理候选进入扫描，不得漏掉。
```

## 2.6 视觉补读队列

```text
phase03_visual_fallback_queue.csv
phase03_visual_fallback_results.md
phase03_pptx_embedded_image_review.md
phase03_pdf_render_review_log.md
phase03_docx_table_and_image_review.md
```

必须覆盖：

```text
1. PDF 命中页。
2. PPTX 内嵌学生答卷图片。
3. PPTX 图形批注。
4. DOCX 表格题。
5. 图片题、漫画题、图表题。
6. 文本层薄弱的原卷。
```

阻断规则：

```text
视觉未核读的边界题，不能进入 LOCKED。
视觉未核读但不影响分类的题，可以进入 PENDING_VISUAL。
视觉未核读且影响答案或题干完整性的题，必须 BLOCKED。
```

## 2.7 A/B 独立扫描与差异文件

```text
phase03_laneA_full_scan.csv
phase03_laneB_full_scan.csv
phase03_AB_question_diff.csv
phase03_AB_classification_diff.csv
phase03_AB_source_diff.csv
phase03_resolved_conflicts.md
phase03_unresolved_conflicts.md
phase03_blocked_questions.csv
```

冲突类型至少包括：

```text
1. A 有题，B 无题。
2. B 有题，A 无题。
3. A/B 题号不同。
4. A/B locator 不同。
5. A/B 部分归属不同。
6. A/B 知识节点不同。
7. A/B 推理题型不同。
8. A/B 答案不同。
9. A/B 对是否需要视觉核读判断不同。
10. A/B 对是否可入学生稿判断不同。
```

## 2.8 阶段审查包

```text
phase03_GPT_commander_review_packet.md
phase03_Governor_interim_gate.md
phase03_Confucius_interim_learning_value_check.md
```

GPT-5.5 Pro 阶段审查包必须包含：

```text
1. raw source registry 摘要。
2. suite registry 摘要。
3. 总题量。
4. 思维题量。
5. 推理题量。
6. 交叉题量。
7. blocked 题量与原因。
8. A/B 冲突数量与类型。
9. 视觉待核读题量。
10. HS02 当前状态。
11. 2026 二模 missing 状态。
12. 推理题型树覆盖情况。
13. 思维材料信号链覆盖情况。
```

---

# 3. 下一阶段扫描顺序：思维部分与推理部分如何并行分工

下一阶段不能按先思维、后推理的串行方式做。原因：一部分题会交叉，尤其是科学思维、逻辑规则、论证评价、假言推理、辩证思维与形式逻辑结合题。应采用“同源逐套扫描，双矩阵并行挂载”。

## 3.1 总体顺序

```text
第一步：清源
第二步：定 suite
第三步：逐套逐题切题
第四步：思维矩阵与推理矩阵并行挂载
第五步：A/B diff
第六步：冲突裁决
第七步：blocked list 锁定
第八步：提交 Phase 03 审查包
```

## 3.2 Codex lane A 分工

Codex lane A 做主生产线：

```text
1. 生成 canonical source_id。
2. 生成 suite_id。
3. 逐套切出全部 question_id。
4. 建立 phase03_question_coverage_matrix。
5. 对每题做初判：思维 / 推理 / 交叉 / 待判。
6. 对思维题填 thinking_signal_chain_matrix。
7. 对推理题填 reasoning_question_attachment_matrix。
8. 建立 visual_fallback_queue。
9. 标记 blocked questions。
10. 生成 laneA_full_scan。
```

Codex lane A 的重点是完整性：

```text
宁可多列待判题，不能漏题。
宁可把边界题列入交叉，不能提前单线归类。
宁可 BLOCKED，不能编答案。
```

## 3.3 ClaudeCode lane B 分工

ClaudeCode lane B 做独立生产和复核线：

```text
1. 不读取 lane A 分类结论。
2. 自行扫描 56 个 raw source。
3. 自行建立 suite/question inventory。
4. 自行标注思维、推理、交叉、待判。
5. 自行识别 PPTX 图片、表格、批注、视觉风险。
6. 自行提出 missing source、missing question、classification conflict。
7. 输出 laneB_full_scan。
```

ClaudeCode lane B 的重点是抓漏：

```text
1. 漏题。
2. 漏小问。
3. 漏选项。
4. 漏答案页。
5. 漏讲评页。
6. 漏 PPTX 图片题。
7. 漏交叉题。
8. 漏推理候选题。
9. 漏同题重复。
10. 漏边界冲突。
```

## 3.4 思维部分扫描规则

每一道思维题先进入以下判断链：

```text
1. 材料中出现什么信号。
2. 这个信号可调用哪一类思维或方法。
3. 设问要求学生做什么动作。
4. 答案应落在哪些句子或评分点。
5. 来源例题如何回指。
```

思维部分分类节点建议先设为：

```text
1. 科学思维特征。
2. 科学思维方法。
3. 辩证思维。
4. 分析与综合。
5. 质量互变。
6. 适度原则。
7. 简单肯定否定到辩证否定。
8. 创新思维。
9. 联想思维。
10. 发散思维与聚合思维。
11. 逆向思维。
12. 超前思维。
13. 综合或交叉。
14. 待判。
```

每题必须填：

```text
材料信号
可写思维/方法
答题动作
来源例题
```

例如 HS02 这种题，必须写成：

```text
材料信号：题干中存在动态过程、整体布局、阶段推进、问题解决、旧方案突破等信号。
可写角度池：分析与综合/系统优化/整体性，质量互变/动态性，辩证否定。
答题动作：从三个角度中选择材料最顺的两个写深。
来源例题：2025 海淀二模 Q20。
状态：LOCKED_PENDING_VISUAL，暂不入学生稿。
```

## 3.5 推理部分扫描规则

每一道推理候选题都必须先抽逻辑结构：

```text
材料语言 -> 逻辑形式 -> 推理规则 -> 有效式/无效式 -> 答案动作
```

推理部分分类节点建议先设为：

```text
1. 概念外延与定义。
2. 判断类型识别。
3. 性质判断。
4. 换质推理。
5. 换位推理。
6. 三段论。
7. 联言判断与联言推理。
8. 相容选言推理。
9. 不相容选言推理。
10. 充分条件假言推理。
11. 必要条件假言推理。
12. 充要条件假言推理。
13. 假言连锁推理。
14. 二难推理或复合推理。
15. 矛盾律。
16. 排中律。
17. 同一律。
18. 归纳推理。
19. 类比推理。
20. 求同法。
21. 求异法。
22. 共变法。
23. 剩余法。
24. 论证评价。
25. 逻辑错误辨析。
26. 综合推理。
27. 待判。
```

推理题不能只填知识节点。必须填：

```text
logical_form
rule_slogan
valid_pattern
trap
answer_action
same_type_question_ids
```

例如 HS05 不能只写形式逻辑综合，必须拆成：

```text
1. 矛盾律。
2. 充分条件假言推理误用。
3. 三段论中项不周延。
```

## 3.6 并行后的融合规则

A/B 融合时必须按以下顺序裁决：

```text
1. 先裁题目是否存在。
2. 再裁题干和选项是否完整。
3. 再裁答案来源。
4. 再裁部分归属。
5. 再裁知识节点。
6. 再裁推理类型。
7. 最后裁是否可入学生稿。
```

不能先讨论表达好坏。当前阶段不允许写最终表达。

---

# 4. 现在最大的内容风险

最大风险是：全量扫描阶段把“题目存在性覆盖”误当成“宝典可写性覆盖”。

具体表现会是：

```text
1. coverage matrix 有题号，但没有材料信号。
2. 推理题挂了题型，但没有 logical_form。
3. 主观题有知识点，但没有答案落点。
4. 选择题有答案，但没有完整四选项。
5. PPTX 图片题被标为 extracted，却没有视觉核读。
6. A/B 都抽到了同一题，却同时继承了同一个误判。
7. 旧稿 locator 行混在 raw source registry 中，后续污染证据池。
```

这比漏几个文件更危险。因为 Phase 02 已经证明文件读取问题暂时可控，真正的失败点会转移到内容层：

```text
抽到了，不等于读懂了。
分类了，不等于可入宝典。
有题型，不等于有解题动作。
有答案，不等于有评分落点。
```

当前最容易复发的旧失败是推理部分。它会很自然地退化为：

```text
题型讲解 + 少数例题 + 泛化陷阱
```

必须强制改为：

```text
题型节点下挂全部题目，逐题写规则、陷阱、同类题、动作。
```

第二大风险是 HS02 式主观题。它提示本轮不能机械追求唯一标准答案。北京政治讲评与评标中可能存在：

```text
角度池
替代给分
优先角度
材料最顺角度
评分弹性
```

所以主观题要区分：

```text
必写点
可选角度池
高价值替代角度
不建议写角度
材料最顺路径
```

---

# 5. 是否同意 HS02 融合结论

同意，但状态必须保持为：

```text
LOCKED_PENDING_VISUAL
```

我同意的部分：

```text
1. 不能写成三点全部必答。
2. 不能写成 3点×2分。
3. 可以写成三个可选角度池。
4. 应优先选择材料最顺的两个角度写深。
5. 辩证否定可以作为高价值补充或替代角度。
6. 最终学生稿中应提示：不要把所有辩证思维知识机械堆上去。
```

需要微调的地方：

```text
原融合表达：三个可选角度池，优先选材料最顺的两条写深；辩证否定是高价值补充/替代角度。

建议改为：三个可选角度池中，至少锁定两个与材料贴合度最高的角度展开；辩证否定经评标实录确认可作为有效替代或补充角度，但最终学生稿应标注其适用触发信号，避免学生见到改革、创新、突破就机械套辩证否定。
```

HS02 后续进入学生稿前，还必须补齐四件事：

```text
1. 原卷视觉最终确认：题干、设问、材料无误。
2. 主细则表格截图或定位记录确认。
3. 讲评 PDF 中选择 2 个角度、每角度 1+2 赋分的定位确认。
4. 评标实录中辩证否定有效、辩证思维特征角度可替代给分的定位确认。
```

HS02 的宝典写法应采用：

```text
题目定位：2025 海淀二模 Q20。
考查方向：辩证思维。
材料信号：整体推进、动态变化、阶段安排、问题解决、突破旧做法。
可选角度池：
  角度一：分析与综合 / 系统优化 / 整体性。
  角度二：质量互变 / 动态性。
  角度三：辩证否定。
考场策略：选材料最顺的两个角度写深。
易错陷阱：把三个角度全部当必答，或只背术语不扣材料。
当前状态：LOCKED_PENDING_VISUAL，暂不入学生稿。
```

---

# 6. 推理部分宝典结构硬要求

推理部分必须以“题型树 + 全题挂载 + 逐题动作”为唯一合法结构。任何只讲题型、不挂全部题的稿件，直接判失败。

## 6.1 推理部分总结构

必须生成四层结构：

```text
第一层：题型树
第二层：每个题型的规则与口令
第三层：该题型下全部真题归档
第四层：每道题的解题动作
```

禁止结构：

```text
1. 先讲归纳推理，再随便举几题。
2. 先讲类比推理，再配几个例子。
3. 三段论只写规则，不挂全部题。
4. 假言推理只写有效式和无效式，不逐题回到材料。
5. 综合题只写综合推理，不拆具体规则。
```

## 6.2 每个题型章必须包含

每个题型节点固定写成：

```text
题型名称
考查规则
规则口令
常见陷阱
本题型全部题目清单
逐题归档
同类题迁移动作
```

其中“本题型全部题目清单”必须列出真实 question_id。不能用示例题代替全部题。

格式：

```text
本题型全部题目清单：
Q-R-001
Q-R-007
Q-R-014
Q-R-022
```

后续正文中必须逐题出现：

```text
Q-R-001
Q-R-007
Q-R-014
Q-R-022
```

缺一题，推理部分不通过。

## 6.3 每道推理题必须包含

逐题模板必须固定：

```text
题目定位：
suite_id：
question_id：
stable_locator：

题型归属：
primary_reasoning_type：
secondary_reasoning_type：
是否一题多法：

材料信号：
题干中哪个词、哪句话、哪个结构触发该规则。

逻辑形式：
把材料语言转成 P、Q、S、M、P 等逻辑结构。

规则口令：
一句话记住本题规则。

有效式或无效式：
本题使用哪条有效推理式，或错在哪里。

解题动作：
Step 1：抽取对象、条件、结论。
Step 2：转成逻辑形式。
Step 3：套规则判断有效或无效。
Step 4：回到选项或设问。
Step 5：形成答案句。

答案落点：
选择题写正确项和排除理由。
主观题写可得分表达。

易错陷阱：
本题最容易误判的地方。

同类题：
列出同一题型下其他 question_id。
```

## 6.4 推理部分必须建立硬校验

必须执行四个一致性校验：

```text
校验一：coverage matrix 中所有 section_scope=推理 的题，必须出现在 reasoning attachment matrix。
校验二：reasoning attachment matrix 中所有题，必须出现在推理宝典正文。
校验三：每个题型章的全部题目清单，必须等于 attachment matrix 中该题型题目集合。
校验四：正文每一道推理题，必须有 logical_form、rule_slogan、trap、answer_action。
```

任一不一致，不能进入 Claude/Opus。

## 6.5 推理综合题处理规则

综合题不能成为垃圾桶。每道综合题必须拆解：

```text
综合题名称：形式逻辑综合
涉及规则：
  规则一：矛盾律
  规则二：充分条件假言推理
  规则三：三段论
每个规则对应的材料信号：
每个规则对应的错误类型：
每个规则对应的答案动作：
```

HS05 的最低合格写法：

```text
HS05：2026 东城期末 Q17(2)
归属：推理部分
primary_type：形式逻辑综合
secondary_types：矛盾律；充分条件假言推理误用；三段论中项不周延
规则口令：
  矛盾律：同一时间、同一方面，不能既肯定又否定。
  充分条件：肯前可肯后，否后可否前；肯后、否前都无效。
  三段论：中项至少周延一次。
解题动作：
  先找互相冲突的判断。
  再把条件句写成 P -> Q。
  再检查是否肯后或否前。
  最后检查三段论中项是否周延。
```

## 6.6 推理题型树只能由真实题源反推

可以先用教材逻辑搭预设树，但最终正文题型树必须由真实题源修正。

执行要求：

```text
1. 先建 provisional_reasoning_typology_tree。
2. 全量扫描后生成 observed_reasoning_typology_tree。
3. 没有真实题的节点不得在宝典正文中长篇展开。
4. 有真实题但预设树没有的节点，必须新增。
5. 交叉题必须双挂载。
6. 待判题必须列入 unresolved，不得消失。
```

## 6.7 推理部分最终进入成文化前的最低门槛

```text
1. 推理题总数明确。
2. 每道推理题有 stable locator。
3. 每道推理题有题型归属。
4. 每道推理题有 logical_form。
5. 每道推理题有 rule_slogan。
6. 每道推理题有 trap。
7. 每道推理题有 answer_action。
8. 每道推理题有 same_type_question_ids。
9. 选择题有完整选项与答案。
10. 主观题有设问与评分落点。
```

达不到以上标准，Claude/Opus 不能介入。

---

# 最后裁决

```text
CONDITIONAL GO
```

允许执行：

```text
全量逐套逐题扫描
全量分类
思维材料信号链矩阵
推理题型挂载矩阵
A/B 独立 diff
视觉 fallback 队列
blocked questions 锁定
Phase 03 commander review packet
```

继续禁止：

```text
学生稿
Claude/Opus 成文化
Word/PDF
最终 PASS
```

Phase 03 的核心验收句只有一句：

```text
每一道题都必须能从 source locator 回到原题，并且能在思维链矩阵或推理挂载矩阵中找到自己的位置。
```
