# Phase12 Next Repair Batch01

Status: `QUEUED_REVIEW_ONLY_NO_WORD_NO_FINAL`

Batch purpose: process the highest-value non-body rows before broad 362-row rescan.

- rows: 12
- priority counts: {'P1_REPAIR_HIGH_VALUE_INDEX_CLUSTER': 3, 'P4_RECHECK_SUBJECTIVE_REASONING_FORM': 4, 'P3_REPAIR_THINKING_OR_CROSS_SOURCE': 5}
- question type counts: {'选择题': 7, '主观题': 5}

## Rows

### 1. 2024 朝阳二模第7题 `Q-2024朝阳二模-7`

- priority: `P1_REPAIR_HIGH_VALUE_INDEX_CLUSTER`
- module/type: 交叉 / 选择题
- required action: 补 logical_form、题型归属、有效式/错误式、规则口令、易错陷阱；通过后转正文
- body target: 选择题正文条目：题干信号/正确项理由/错项陷阱/同类题
- source: 023_Desktop_2024模拟题_2024朝阳二模_细则_补充材料_细则.docx::Q7=D
- answer: answer_confirmed_D_from_023_rubric
- risk note: A小项不当周延/小项扩大（娱乐工具在前提中不周延，结论中周延）;B归纳推理结论确定性夸大;C必要条件假言推理误用

### 2. 2025 东城期末第18题第(2)问 `Q-2025东城期末-18-2`

- priority: `P1_REPAIR_HIGH_VALUE_INDEX_CLUSTER`
- module/type: 交叉 / 主观题
- required action: 补 logical_form、题型归属、有效式/错误式、规则口令、易错陷阱；通过后转正文
- body target: 主观题正文条目：材料触发点/设问/为什么能想到/答案落点
- source: paper:012@L199-203; rubric:012@L681-698(inline)
- answer: answer_confirmed_from_rubric_012_inline
- risk note: 只列思维无材料分析丢分;混淆联想/发散/聚合归属丢分

### 3. 2026 通州期末第9题 `Q-2026通州期末-9`

- priority: `P1_REPAIR_HIGH_VALUE_INDEX_CLUSTER`
- module/type: 思维 / 选择题
- required action: 回源确认题干/选项/答案来源；不得猜答案；通过后转正文或保留 blocked
- body target: 选择题正文条目：题干信号/正确项理由/错项陷阱/同类题
- source: 006试卷::Q9=D
- answer: answer_confirmed_D_from_006_paper
- risk note: A完善基本医疗保障体系夸大;B创新思维保障民生但"优先构建"过窄;C发散思维拓展应用场景"转化服务要素"表述错

### 4. 2024 朝阳期中第18题 `Q-2024朝阳期中-18`

- priority: `P4_RECHECK_SUBJECTIVE_REASONING_FORM`
- module/type: 推理 / 主观题
- required action: 补 logical_form、题型归属、有效式/错误式、规则口令、易错陷阱；通过后转正文
- body target: 主观题正文条目：材料触发点/设问/为什么能想到/答案落点
- source: paper:017@L224-232; rubric:018@L56-78
- answer: answer_confirmed_from_rubric_018
- risk note: 楚王=以一例归纳全体;晏子=橘枳类比环境致变(均或然但晏子辩证驳论)

### 5. 2025 丰台期末第18题第(1)问 `Q-2025丰台期末-18-1`

- priority: `P4_RECHECK_SUBJECTIVE_REASONING_FORM`
- module/type: 推理 / 主观题
- required action: 补 logical_form、题型归属、有效式/错误式、规则口令、易错陷阱；通过后转正文
- body target: 主观题正文条目：材料触发点/设问/为什么能想到/答案落点
- source: paper:040@L240-251; rubric:040@L569-571(inline)
- answer: answer_confirmed_from_rubric_040_inline
- risk note: 误判断类型(写充分而非必要)0分;漏保真条件丢分

### 6. 2025 顺义一模第17题第(1)问 `Q-2025顺义一模-17-1`

- priority: `P4_RECHECK_SUBJECTIVE_REASONING_FORM`
- module/type: 推理 / 主观题
- required action: 补 logical_form、题型归属、有效式/错误式、规则口令、易错陷阱；通过后转正文
- body target: 主观题正文条目：材料触发点/设问/为什么能想到/答案落点
- source: paper:033@L43-45(via excerpt); rubric:034@L24-29
- answer: answer_confirmed_from_rubric_034
- risk note: 误识别判断类型0分;误把相容当不相容选言扣分

### 7. 2026 东城期末第17题第(2)问 `Q-2026东城期末-17-2`

- priority: `P4_RECHECK_SUBJECTIVE_REASONING_FORM`
- module/type: 推理 / 主观题
- required action: 补 logical_form、题型归属、有效式/错误式、规则口令、易错陷阱；通过后转正文
- body target: 主观题正文条目：材料触发点/设问/为什么能想到/答案落点
- source: paper:044@L231-239; rubric:044@L352-353(inline)
- answer: answer_confirmed_from_rubric_044_inline
- risk note: 误识别判断/推理类型扣分;违反矛盾律辨析失误扣分

### 8. 2026 东城一模第6题 `Q-2026东城一模-6`

- priority: `P3_REPAIR_THINKING_OR_CROSS_SOURCE`
- module/type: 交叉 / 选择题
- required action: 回源确认题干/选项/答案来源；不得猜答案；通过后转正文或保留 blocked
- body target: 选择题正文条目：题干信号/正确项理由/错项陷阱/同类题
- source: 046_Desktop_2026模拟题_2026各区一模_2026东城一模_试卷_试卷.pdf::Page9参考答案表(题号6=D)
- answer: answer_confirmed_D_from_046_paper
- risk note: A辩证否定误用_联结非否定;B抽象思维误标_应为形象思维;C有些S是P不能必推有些S不是P

### 9. 2026 丰台一模第4题 `Q-2026丰台一模-4`

- priority: `P3_REPAIR_THINKING_OR_CROSS_SOURCE`
- module/type: 思维 / 选择题
- required action: 回源确认题干/选项/答案来源；不得猜答案；通过后转正文或保留 blocked
- body target: 选择题正文条目：题干信号/正确项理由/错项陷阱/同类题
- source: supplemental_source=2026北京丰台高三一模政治试题有答案_北京高考在线.txt; 答案表Q4=A; 题干见page2文字
- answer: answer_confirmed_A_from_supplemental_key
- risk note: ④陷阱：古人营建在现代"最速降线"理论发现之前，④倒置时序；③"全新重构"错

### 10. 2026 丰台一模第7题 `Q-2026丰台一模-7`

- priority: `P3_REPAIR_THINKING_OR_CROSS_SOURCE`
- module/type: 思维 / 选择题
- required action: 回源确认题干/选项/答案来源；不得猜答案；通过后转正文或保留 blocked
- body target: 选择题正文条目：题干信号/正确项理由/错项陷阱/同类题
- source: supplemental_source=2026北京丰台高三一模政治试题有答案_北京高考在线.txt; 答案表Q7=B; 题干见page2-3文字
- answer: answer_confirmed_B_from_supplemental_key
- risk note: ②"断定病症病因必然联系应运用充分条件假言推理"——错，必然联系是充要条件非单向充分条件；③"只有完全归纳才能确保结论无误"——临床不可能做完全归纳

### 11. 2026 朝阳期中第13题 `Q-2026朝阳期中-13`

- priority: `P3_REPAIR_THINKING_OR_CROSS_SOURCE`
- module/type: 交叉 / 选择题
- required action: 回源确认题干/选项/答案来源；不得猜答案；通过后转正文或保留 blocked
- body target: 选择题正文条目：题干信号/正确项理由/错项陷阱/同类题
- source: 003 lines 148-158; 003 lines 297-326
- answer: answer_confirmed_D_from_003 lines 148-158; 003 lines 297-326
- risk note: ②类比推理是推理部分（诱惑项非答案）；①哲学常识层面

### 12. 2026 顺义一模第6题 `Q-2026顺义一模-6`

- priority: `P3_REPAIR_THINKING_OR_CROSS_SOURCE`
- module/type: 思维 / 选择题
- required action: 回源确认题干/选项/答案来源；不得猜答案；通过后转正文或保留 blocked
- body target: 选择题正文条目：题干信号/正确项理由/错项陷阱/同类题
- source: 002细则.pptx答案表(Q6=A)
- answer: answer_confirmed_A_from_002_alt_extraction
- risk note: B界限不变绝对论错;C优势互补延伸认识边界过度;D具体操作路径错位

## Gate

No row in this batch is promoted by being queued. Promotion requires source repair/reasoning-form repair and a row-level review note.
