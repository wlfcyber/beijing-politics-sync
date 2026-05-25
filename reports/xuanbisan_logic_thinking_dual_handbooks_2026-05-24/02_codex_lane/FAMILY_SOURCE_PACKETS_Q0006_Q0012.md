# Family Source Packets Q0006-Q0012

Status: `A_LINE_SOURCE_LOCKED_Q0006_Q0012`

Rule: 本文件服务两件事：推理宝典按同一推理形式聚合，思维宝典继续补“触发链”样本。这里仍然是 source packet，不是终稿。

## Q0006 2024朝阳一模 Q20(1)

- part: 推理宝典
- reasoning_form: 充分条件假言推理
- evidence_level: `A-formal`
- paper: `gpt_sources/25b655e73b7424e7_202404朝阳高三一模试题.md:231-238`
- rubric: `gpt_sources/d64506799887753e_2024朝阳一模细则.md:317-327`

### Trigger Chain

推理一是“如果 A 区域古代没有广泛生长竹子，就不可能有大量炭化竹节；已发现大量炭化竹节；所以 A 区域古代广泛生长竹子”。这是充分条件假言推理的否定后件式：如果 P 则 Q，非 Q，所以非 P。

## Q0007 2024朝阳一模 Q20(2)

- part: 推理宝典
- reasoning_form: 必要条件假言推理
- evidence_level: `A-formal`
- paper: `gpt_sources/25b655e73b7424e7_202404朝阳高三一模试题.md:239-241`
- rubric: `gpt_sources/d64506799887753e_2024朝阳一模细则.md:328-335`

### Trigger Chain

推理二要求补充不同于推理一的演绎推理。细则要求前提表达“A 区域古代气候温暖是 A 区域古代生长竹子的必要条件”，即“只有 A 区域古代气候温暖，A 区域古代才有可能生长竹子”；再接“A 区域古代广泛生长着竹子”，由肯定后件推出肯定前件。

## Q0008 2025西城二模 Q16(2)

- part: 推理宝典
- reasoning_form: 充分条件假言推理
- evidence_level: `A-formal`
- paper: `gpt_sources/06c08602a2f5c20b_2025北京西城高三二模政治_教师版.md:192-197`
- rubric: `gpt_sources/cfb0f19ef38aafd7_2025西城二模细则.md:52-53`
- answer: `gpt_sources/06c08602a2f5c20b_2025北京西城高三二模政治_教师版.md:303-305`

### Trigger Chain

条件②是“若发现岩松鼠活动痕迹，则一定能找到红嘴蓝鹊”。观察到红嘴蓝鹊只是肯定后件，不能确定前件真假，因此不能确定一定有岩松鼠活动。

## Q0009 2026通州期末 Q19(2)

- part: 推理宝典
- reasoning_form: 充分条件假言推理 + 必要条件假言推理
- evidence_level: `A-formal`
- paper: `gpt_sources/7f3083ea306ea1e9_2026北京通州高三_上_期末政治_教师版.md:226-233`
- rubric: `gpt_sources/44537714bd68a7c1_2026通州期末细则.md:147-161`
- answer: `gpt_sources/7f3083ea306ea1e9_2026北京通州高三_上_期末政治_教师版.md:309-313`

### Trigger Chain

推理①“如果阻碍加装电梯，就会侵犯相关业主合法权益；范某阻碍；所以侵权”是充分条件假言推理肯前肯后，结构有效。推理②“只有公示期间未收到异议，加装电梯才符合要求；公示期内未收到异议；所以符合要求”是必要条件假言推理肯前肯后，结构无效。

## Q0010 2026丰台一模 Q18(2)

- part: 推理宝典
- reasoning_form: 必要条件假言推理 + 三段论
- evidence_level: `A-formal`
- rubric: `gpt_sources/26649804f1de31f5_2026丰台一模细则.md:116-132`

### Trigger Chain

甲的推理属于必要条件假言推理，细则明确为肯定后件式，推理正确。乙的推理属于三段论推理，材料中“带动居民消费”作为大项在前提中不周延、在结论中周延，犯“大项不当扩大”。

## Q0011 2024海淀二模 Q17(1)

- part: 思维宝典
- framework_node: 科学思维总帽下三模块复合 -> 科学思维客观性 / 创新思维三新与发散聚合或超前 / 辩证思维整体性与分析综合
- evidence_level: `A-formal`
- paper: `gpt_sources/13d454fdd813a039_高三二模_政治试题_以PDF为准_1.md:141-158`
- rubric: `gpt_sources/227192d22e10241b_2024海淀二模细则.md:30-54`

### Trigger Chain

设问仍问“如何体现科学思维”，但正式细则把 7 分拆成三模块：全面、真实、准确了解居民时间利用情况 -> 科学思维客观性或预见性，2 分；调查思路新、方法新、范围对象内容更丰富、创造性解决问题 -> 创新思维三新，发散思维/聚合思维或超前思维，3 分；调查工作具有整体性、分阶段实施、任务明确 -> 辩证思维整体性、分析与综合或矛盾分析法，2 分。不得再把本题写成“科学思维单角度只答客观性/探索性/整体性”。

## Q0012 2025顺义一模 Q7

- part: 推理宝典选择题陷阱
- reasoning_form: 三段论谬误名称纠偏
- evidence_level: `A-formal`
- paper_and_answer: `gpt_sources/9dd43cae443f853c_2025北京顺义高三一模政治_教师版.md:88-115`
- explanation: `gpt_sources/9dd43cae443f853c_2025北京顺义高三一模政治_教师版.md:371-380`

### Trigger Chain

题目问“下列三段论的逻辑分析错误的是”。正确选 A，因为 A 选项中的推理实际犯“大项不当扩大”，不是“小项不当扩大”。B 是两个否定前提不能必然推出结论；C 是四概念；D 是中项不周延，三者分析正确。
