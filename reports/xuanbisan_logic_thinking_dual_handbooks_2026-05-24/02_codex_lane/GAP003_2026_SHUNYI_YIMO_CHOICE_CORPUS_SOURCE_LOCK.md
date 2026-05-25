# GAP003 Source Lock: 2026顺义一模 Q1-Q15 选择题语料

Status: `closed_choice_corpus_classified_pending_external_review`

This file closes GAP003 at the local source-evidence level only. It does not close GPT Pro, Claude V4/V5, Governor, Confucius, or final delivery gates.

## Source

- paper cache: `gpt_sources/8d19592ca0679f21_2026顺义一模.md:26-201`
- answer key cache: `gpt_sources/de758e5e79500dd0_2026顺义一模细则.md:20-50`
- raw paper: `C:\Users\Administrator\Desktop\2026各区模拟题\2026各区一模\2026顺义一模\试卷\2026顺义一模.pdf`
- raw rubric / answer source: `C:\Users\Administrator\Desktop\2026各区模拟题\2026各区一模\2026顺义一模\细则\2026顺义一模细则.pptx`

Formal objective answer key for Q1-Q15:

| question | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| answer | B | C | C | A | D | A | D | A | B | B | D | B | C | D | C |

## Q1-Q15 Module Classification

| question | answer | local decision | reason |
|---|---|---|---|
| Q1 | B | exclude | 中共领导和社会发展史，非选必三语料。 |
| Q2 | C | promote as `Q0031` reasoning choice-trap | D 项把“上世纪20年代末北京城南风土人情”和“北京题材”误判为外延交叉关系，可入概念外延关系陷阱。 |
| Q3 | C | promote as `Q0032` thinking choice-trap | 探月工程“先核心后细分、全链条自主可控”可训练分析与综合、整体性和动态性，错项集中在矛盾主要方面和适度原则硬套。 |
| Q4 | A | promote as `Q0033` reasoning choice-trap | `论持久战`对当前中长期问题提供启迪，锁定类比推理；错项含比喻定义、完全归纳和决定作用夸大。 |
| Q5 | D | promote as `Q0034` thinking choice-trap | “触摸历史温度、聆听无声之教”对应感觉、知觉、表象基础上认识本质和规律；可训练思维抽象边界。 |
| Q6 | A | promote as `Q0035` conflict row only | 正式答案键为 A，题面支持“基于既有认知框架和乔哈里视窗衍生模型”；但旧错肢库曾把 A 记为错误，本轮不入陷阱库，等待外审复核。 |
| Q7 | D | promote as `Q0036` thinking choice-trap | 第四象限对应个人情感体验、价值判断和价值选择、复杂人际沟通、协商谈判、矛盾调解，可入人机分工边界陷阱。 |
| Q8 | A | exclude | 民族政策与新时代治疆方略，非选必三。 |
| Q9 | B | exclude | 政务 App 规范化与政府治理，非选必三；只作跨模块边界。 |
| Q10 | B | exclude | AI 法律责任与民事主体资格，属选必二法律。 |
| Q11 | D | exclude | 未成年人人格权、侵权与诉讼代理，属选必二法律。 |
| Q12 | B | exclude | 基础研究与经济高质量发展，属经济与社会。 |
| Q13 | C | exclude | 社会救助与再分配，属经济与社会。 |
| Q14 | D | exclude | 数字贸易与全球价值链，属选必一国政经。 |
| Q15 | C | exclude | 金砖合作与全球治理，属选必一国政经。 |

## Local Decisions To Ledger

### Q0031 2026顺义一模 Q2

Evidence level: `B-choice-signal`

- correct answer: `C`
- usable trap: D 项“外延交叉关系”错误。
- reasoning form / concept focus: 概念外延关系。
- student rule: 先判断两个概念的大小范围和包含关系。具体剧目、具体历史风土和“北京题材”不是简单交叉关系。

### Q0032 2026顺义一模 Q3

Evidence level: `B-choice-signal`

- correct answer: `C` (`②③`)
- usable thinking signal: 分析与综合相结合，整体把握全链条难题，再突破细分技术。
- trap: ①把“关键核心技术制约”误写成抓矛盾主要方面；④把技术攻关硬套成“得中而处之”的适度原则。

### Q0033 2026顺义一模 Q4

Evidence level: `B-choice-signal`

- correct answer: `A`
- usable reasoning signal: 类比推理。由《论持久战》处理抗战中长期问题的思想，启发当前科技创新、乡村振兴等中长期问题。
- trap: C 把“思想灯塔”的比喻误说成定义方法；D 把总结全国抗战经验误说成完全归纳推理。

### Q0034 2026顺义一模 Q5

Evidence level: `B-choice-signal`

- correct answer: `D`
- usable thinking signal: 感觉、知觉、表象基础上认识事物本质和规律。
- trap: B 把“把众多信息引导到条理化逻辑思路中”误说成发散思维；本质上更接近聚合、整理和抽象。

### Q0035 2026顺义一模 Q6

Evidence level: `B-choice-signal`

- correct answer by formal key: `A`
- conflict note: old wrong-option library recorded A as wrong, while the official answer key records A as correct. The source paper says the model is based on Rumsfeld's known-unknown framework and Johari Window, then derived for AI-human cognitive boundaries. This supports the official-key reading of migration, but the conflict must be reviewed before any trap-library promotion.
- status: `source_locked_answer_conflict_pending_external_review`

### Q0036 2026顺义一模 Q7

Evidence level: `B-choice-signal`

- correct answer: `D`
- usable thinking signal: fourth quadrant is reserved for human emotional experience, value judgment and value choice, complex interpersonal communication, negotiation, mediation, and conflict resolution.
- trap: A/B/C map the quadrant fields too mechanically and mismatch AI/human advantage boundaries.

## Gate Decision

GAP003 can move from `open` to `closed_choice_corpus_classified_pending_external_review`: all Q1-Q15 items have been classified; Q2-Q7 produce local ledger rows; Q6 is deliberately held as a conflict row rather than a choice-trap entry.

This is still not release-ready. The additions must be included in the next GPT Pro packet and the next real Claude external-review packet.
