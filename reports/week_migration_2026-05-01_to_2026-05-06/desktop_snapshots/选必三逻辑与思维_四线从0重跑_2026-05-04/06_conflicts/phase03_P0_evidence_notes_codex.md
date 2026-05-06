# Phase 03 P0 Evidence Notes — Codex A

Status: `LOCAL_EVIDENCE_NOT_STUDENT_FACING`.

## 2025西城二模 Q16(2) / Q16(3)

Local source check resolves the apparent classification conflict by splitting sub-questions:

- Paper `037...2025西城二模_试卷.pdf.txt` lines 186-191: Q16(2) asks whether seeing 雕鸮 and 红嘴蓝鹊 can determine 岩松鼠 activity, and asks to explain the reasoning process. This is 推理部分.
- Rubric `038...2025西城二模_细则.docx.txt` lines 18-19: Q16(2) is a 充分条件假言判断 issue; seeing the consequent true cannot determine the antecedent true. This is 推理部分 / 充分条件假言推理 trap.
- Paper `037...` lines 192-193: Q16(3) asks for solutions to villagers' demand to remove the water source pool. This is not the same reasoning sub-question.
- Rubric `038...` line 22: Q16(3) explicitly allows `运用创新思维，改变创造条件、建立新的具体联系，分析解决矛盾`.

Codex decision note: A/B conflict was caused by treating Q16 as one classification unit. Correct split is:

- `2025西城二模 Q16(2)` -> 推理部分 / 充分条件假言判断 / 后件真不能推出前件真.
- `2025西城二模 Q16(3)` -> 思维部分 / 创新思维 / 改变创造条件、建立新联系.

No student稿 promotion yet; use this as a matrix correction task.

## 2026朝阳期中 Q11-Q15 Choice Answer Pairing

Local paper source `003...2026朝阳期中_试卷.pdf.txt` contains both question text and an answer table.

Question locators:

- Q11: lines 130-136, 三段论补大前提.
- Q13: lines 148-158, 石榴籽比喻, 类比推理/感性具体/联想思维.
- Q14: lines 159-168, 天气谚语, 归纳/或然性.
- Q15: lines 169-175, 联言判断否定.

Answer table:

- lines 297-311 list Q1-Q15.
- lines 312-326 list answers in order: `A C C A B B D D C C A B D B D`.

Codex paired answers:

- Q11 -> A.
- Q13 -> D.
- Q14 -> B.
- Q15 -> D.

Evidence level: `B-choice-signal`, because this is paper answer table, not a formal scoring rubric. It is enough for choice-trap extraction if the original options are complete and no conflicting key is found.

No student稿 promotion yet; use this to clear `blocked_until_answer_or_rubric_pairing` for these choice rows after matrix patching.

## 2025海淀二模 Q12/Q13 Visual Check

Source:

- paper render: `02_extraction/priority_queue_sources/renders/008_Desktop_2025模拟题_2025各区二模_2025海淀二模_试卷_试卷.pdf/page_04.png`
- rubric/answer text checked: `009_...细则.docx.txt`, `010_...评标实录.docx.txt`, `011_...讲评0510.pdf.txt`

Q12 visual recovery:

- 原卷 page_04 清晰可见完整题干与四个选项。
- 题干关键词：`耐心资本`、`不以追求短期收益为首要目标`、`长期限展望`、`对风险有较高承受力`、`为投资项目/资本市场提供长期稳定资金支持`、`科技创新和产业创新`。
- 选项组合：
  - ① 相对短期资本而言，耐心资本作为新事物具有更强大的生命力
  - ② 耐心资本消除短期收益与长期收益的矛盾，推动发展新质生产力
  - ③ 培育耐心资本需要平衡好风险与收益的关系，增强其可持续性
  - ④ 壮大耐心资本需要运用超前思维，关注投资项目的长期发展
  - A ①② / B ①④ / C ②③ / D ③④
- Codex A classification note: 思维部分候选，明显涉及超前思维；不能按“推理部分”直接锁定。
- Current status: visual full options recovered; answer source not found in currently extracted 009/010/011 text, so `blocked_until_answer_pairing` before fusion/student use.

Q13 visual recovery:

- 原卷 page_04 清晰可见完整题干与四个选项。
- 题干关键词：`学习逻辑思维有助于提升我们的思维水平`、`运用到《当代国际政治与经济》的学习过程中`、`下列表述正确的是`。
- 四个选项：
  - A 现代国家分为君主立宪制国家、议会制国家、总统制国家
  - B 只要国家机关是由选举产生的，就能维护最广大人民的根本利益
  - C 单一制国家中央政府享有最高权力，法国是单一制国家，所以，法国中央政府享有最高权力
  - D 主权国家之间的关系要么是竞争，要么是合作，要么是冲突
- Codex A classification note: 推理/逻辑规则候选，至少涉及三段论或选言判断陷阱；仍需答案来源和 B 线复核。
- Current status: visual full options recovered; answer source not found in currently extracted 009/010/011 text, so `blocked_until_answer_pairing` before fusion/student use.

## 2025海淀期末 Q2 Boundary Check

Source:

- paper text: `02_extraction/priority_queue_sources/text/015_Desktop_2025模拟题_2025各区期末_2025海淀期末_试卷_试卷.docx.txt`
- rubric/lecture text checked: `016_Desktop_2025模拟题_2025各区期末_2025海淀期末_细则_细则.pptx.txt`

Q2 text is complete in the paper extraction:

- 题干：申遗成功后，“大美中轴”观光巴士吸引游客；复刻百年前电车外观；线路涵盖中轴线 15 处文化遗产；车上可听京味解说、品北京烤鸭、看曲艺表演，沉浸式体验古都历史底蕴。
- 选项：
  - ① 观光巴士复刻百年前的电车外观是对旧事物积极部分的扬弃
  - ② 将北京烤鸭、曲艺表演搬上巴士是通过场景迁移获得的新思路
  - ③ 旅游项目设计关注乘客与环境的关系，把握辩证思维的整体性
  - ④ 人们可以立足观光巴士成功经验，开发更多沉浸式体验新形式
  - A ①② / B ①④ / C ②③ / D ③④

Codex A classification note:

- Q2 是思维部分候选，涉及创新思维的迁移、辩证思维整体性；同时和哲学/文化边界有交叉。
- 016 细则/讲评当前可读部分没有给出 Q2 选择题答案或逐项讲解；PPT 主要从 Q16/Q17 起讲。
- Current status: full stem/options recovered, but answer source not found; keep `blocked_until_answer_pairing_and_boundary_review`.

## 2024西城一模 Q11 Textbox Recovery

Source:

- paper docx XML: `/Users/wanglifei/Desktop/2024模拟题/西城一模/试卷/试卷.docx`
- answer/rubric texts: `025_...西城一模_细则.docx.txt`, `026_...2024.4高三统一测试思想政治答案.docx.txt`

Problem:

- The normal docx text extraction only produced `1 2 3 4`, because the four inference options are inside Word text boxes / drawing shapes.

Codex A XML textbox recovery:

- ① `“问天”是中国空间站的舱段，“梦天”是中国空间站的舱段，“天和”是中国空间站的舱段，所以，“问天”“梦天”“天和”都是中国空间站的舱段。`
- ② `“问天”是中国航天人走过的路，“梦天”是中国航天人走过的路，“天和”是中国航天人走过的路，所以，中国航天人走过的路，或是“问天”，或是“梦天”，或是“天和”。`
- ③ `“问天”是中国航天人走过的路，“梦天”是中国航天人走过的路，“天和”是中国航天人走过的路，所以，“问天”“梦天”“天和”连缀起中华民族求索太空的浩瀚征程。`
- ④ `“问天”“梦天”“天和”连缀起中华民族求索太空的浩瀚征程，中国空间站的三个舱段是“问天”“梦天”“天和”，所以，中国空间站的三个舱段连缀起中华民族求索太空的浩瀚征程。`
- answer key from both 025 and 026: `11．B`.

Codex A classification note:

- Q11 is a 推理选择题; answer B means ①/④ are correct.
- ① is an inductive/generalization style inference from enumerated cases to a class statement.
- ② reverses the direction of the class relation and creates an over-broad disjunctive conclusion.
- ③ moves from “is a route walked by astronauts” to “therefore links the journey”; the conclusion is not licensed by the premises alone.
- ④ substitutes the equivalent set “中国空间站的三个舱段” for “问天/梦天/天和” and preserves the predicate relation.
- Current status: full options + answer recovered by Codex A; still requires Lane B targeted verification before locked fusion.

## 2025西城二模 Q7 Answer/Options Check

Source:

- paper text: `037_Desktop_2025模拟题_2025各区二模_2025西城二模_试卷_试卷.pdf.txt`
- answer/rubric text: `038_Desktop_2025模拟题_2025各区二模_2025西城二模_细则_细则.docx.txt`

Paper text already contains full stem/options:

- 题干：花粉过敏；甲医生基于“只有接触过敏源，才会引发过敏”和病人未接触花粉，断定不属于花粉过敏；乙医生基于春天开花季出现症状、过季消失，断定由花粉过敏引起；丙医生基于一名中年女性确诊，推断另一名年纪相仿女性也应是花粉过敏。
- 选项：
  - ① 甲医生运用了演绎法，推理结构正确能确保这类推理得出正确结论
  - ② 乙医生正确运用了求异法，但其结论不具有必然性
  - ③ 与乙、丙相比，甲医生的推理方式在科学领域更有利于得出新结论
  - ④ 三名医生结论的可信度由高到低依次应该是甲、乙、丙
  - A ①② / B ①③ / C ②④ / D ③④
- Answer key in 038: `7．C`.

Codex A classification note:

- Q7 is 推理选择题; answer C means ②/④ correct.
- 甲：必要条件假言推理否定前件，形式无效，结论不能保证；所以①错。
- 乙：类比求异/求异法信号，有经验归纳性质，结论或然；②可成立。
- 丙：类比推理弱，可信度低；甲/乙/丙可信度排序需 B 线复核细化。
- Current status: full options + answer recovered by Codex A; still requires Lane B targeted verification before locked fusion.
