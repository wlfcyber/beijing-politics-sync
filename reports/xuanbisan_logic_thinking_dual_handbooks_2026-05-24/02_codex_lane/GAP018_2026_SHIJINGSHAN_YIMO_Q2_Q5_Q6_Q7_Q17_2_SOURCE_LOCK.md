# GAP018 2026石景山一模 Q2/Q5/Q6/Q7/Q17(2) Source Lock

Status: `source_locked_pending_external_review`

This file records a 2026石景山一模 source lock for four choice rows and one innovation-thinking main-question row. Q2 is kept as a `B-choice-signal` because it mixes辩证思维 wording with broader development/philosophy language. Q5-Q7 are reasoning choice rows locked from the original paper and formal answer table. Q17(2) is an A-formal innovation-thinking main-question row locked from the prompt and scoring rules. Q21 is only a broad comprehensive boundary and is not promoted.

## Evidence

- Paper prompt and embedded teacher answer: `preprocessed_corpus/gpt_sources/0d4a5cd29c2e6961_2026北京石景山高三一模政治_教师版.md:38-46,67-99,207-212,288-306`
- Formal answer table and scoring rules: `preprocessed_corpus/gpt_sources/78d97b669465d8a5_2026石景山一模细则.md:23-25,53-57,91-110`

## Q0103 2026石景山一模 Q2

- Official key: Q2 = D, namely ②④.
- Classification: thinking choice-signal, not a full main-question trigger chain.
- Trigger chain: 吉林长白山夏日山地旅游破圈、衡阳工业遗址蝶变文旅空间 -> 创造条件、克服困难、推动矛盾双方转化；从“一季养四季”到“四季皆旺季”、以新视角新方法开发资源价值 -> 发展观点。
- Boundary: ①的“部分功能之和大于整体功能”是系统优化误写；③的“促使客观见之于主观”方向错误。本题保留为选择题信号，不作为主观题模板。

## Q0104 2026石景山一模 Q5

- Official key: Q5 = D.
- Classification: reasoning choice row.
- Trigger chain: “有些属于非物质文化遗产组成部分的实物和场所，适用文物保护法”是特称肯定判断；可换质为“有些……不是不适用文物保护法”，但换质后成为特称否定判断，不能再换位，因此 D 项“无法进行换质位推理”成立。

## Q0105 2026石景山一模 Q6

- Official key: Q6 = D, namely ②④.
- Classification: reasoning choice row.
- Trigger chain: 具身智能属于具有身体且能像人一样感知、学习的人工智能；“只有能像人一样感知、学习，才能称之为具身智能”锁定必要条件关系。②可由定义推出，④“除非P，否则不能Q”等价于 Q -> P。①把所有有身体的人工智能都当成具身智能，③犯否定后件/逆否误读。

## Q0106 2026石景山一模 Q7

- Official key: Q7 = C.
- Classification: reasoning choice row.
- Trigger chain: 通过观茶芽、察茶汤、闻茶香等有限经验样本，识别茶的香气持久与烘焙工艺之间的内在关联，属于不完全归纳推理。A误挂必要条件假言判断，B误挂求同法，D把“见微知著”泛化为辩证思维整体妙悟。

## Q0107 2026石景山一模 Q17(2)

- Prompt: 结合材料二，运用创新思维的知识，为传承中医药文化提出两条建议。
- Formal rubric: 可从发散与聚合思维、超前思维等角度作答；一条正确建议 3 分，两条 6 分；其他角度符合题意可酌情给分。
- Classification: thinking main-question row, `A-formal`.
- Trigger chain: 中医药文化传播行动和活动产品供给 -> 发散思维多路径传播；进校园、进社区、进家庭 -> 聚合资源；健康中国和中医药预防保健服务体系 -> 超前思维前瞻布局；传统诊疗方法与现代智能技术结合 -> 联想思维。

## Boundary

- Q21 is a broad “综合运用所学” ecological-environment-code question. The scoring source allows制度优势、新发展理念、系统优化、科学立法、辩证思维等角度, but it is not an explicit《逻辑与思维》设问 and not an independent elective-3 row in this pass.

## Required Gates

- Add Q0103-Q0107 to coverage matrix and source queue.
- Add MT0048-MT0049, RF0062-RF0064, and CT0041-CT0044.
- Add thinking handbook V2 sections 55-56 and reasoning handbook V2 sections 44-46.
- Keep all five rows on hold pending GPT Pro V53 / Claude V51 and B-line rerun.
