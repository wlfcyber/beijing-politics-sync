# GAP006 Source Lock: 2024东城一模 Q6-Q8

Status: `source_locked_pending_external_review`

This file advances GAP006 at the local source-evidence level only. It does not close the 2024 suite backlog, GPT Pro, Claude V4/V5/V35, Governor, Confucius, or final delivery gates.

## Source

- raw paper render: `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\renders\74cdfac9253763bf\page_003.png`
- official answer / marking-standard render: `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\renders\7b4eece2963205d8\page_001.png`
- Q6 formal analysis cache: `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\4b2073bcc9e26f62_2024东城一模细则.md:22-27`
- raw paper: `C:\Users\Administrator\Desktop\2024各区模拟题\2024各区一模\2024东城一模\试卷\北京市东城区2023-2024学年度第二学期高三综合练习（一）思想政治试卷(1).pdf`
- raw answer: `C:\Users\Administrator\Desktop\2024各区模拟题\2024各区一模\2024东城一模\其他材料\北京市东城区2023-2024学年度第二学期高三综合练习（一）思想政治答案(1).pdf`
- raw marking rule: `C:\Users\Administrator\Desktop\2024各区模拟题\2024各区一模\2024东城一模\细则\2024东城一模细则.pptx`

The official answer page locks Q6 = D, Q7 = A, Q8 = D. The raw paper render locks the option text. Q6 also has a PPT analysis cache; Q7/Q8 are answer-key locked without a detailed option rubric.

## Q0071 2024东城一模 Q6

Evidence level: `A-formal`

Question family: logic-rule comprehensive choice.

Correct answer: `D`

Local decision:

- A is not the correct analysis: the issue is closer to definition over-breadth, not simply 同语反复.
- B is not the correct analysis: "北京分为东城、西城、海淀等区" is an incomplete listing / decomposition context, not a strict division error as stated.
- C is not the correct analysis: the sentence has a concept-matching problem, not merely "含义不明确、不表达判断".
- D is correct: "选择" presupposes comparison; "不加比较作选择" contains a contradiction and violates the law of contradiction.

Promote as `Q0071` reasoning choice row and `CT0017` choice-trap row.

## Q0072 2024东城一模 Q7

Evidence level: `A-formal`

Question family: syllogism validity vs premise truth.

Correct answer: `A` = ①②.

Prompt:

> “所有鸟都是会飞的，鸵鸟是鸟，所以，鸵鸟是会飞的。”对此推理分析正确的是？

Local decision:

- ① is correct: the syllogism has a valid form.
- ② is correct: the major premise is false, so the conclusion is not true.
- ③ is wrong: a necessary deductive form does not guarantee a true conclusion unless the premises are true.
- ④ is wrong: the argument has three terms and does not commit a four-concepts error.

Promote as `Q0072` reasoning choice row and `CT0018` choice-trap row.

## Q0073 2024东城一模 Q8

Evidence level: `A-formal`

Question family: compound hypothetical / disjunctive reasoning chain.

Correct answer: `D`

Known conditions:

- 只有小徐选物理，小赵才选地理: `小赵选地理 -> 小徐选物理`.
- 或者小李选政治，或者小王选政治.
- 当且仅当小孙选政治，小李选政治.
- 如果小王选政治，那么小赵选地理.

Local decision:

`小徐未选物理` implies `小赵未选地理`; then by the contrapositive of `小王选政治 -> 小赵选地理`, `小王未选政治`; with "或者小李选政治，或者小王选政治", infer `小李选政治`. Therefore D is the necessary added information.

Promote as `Q0073` reasoning choice row and `CT0019` choice-trap row.

## Gate Decision

Add Q0071-Q0073 to the coverage matrix, source-packet queue, reasoning-form ledger, choice-trap ledger, and reasoning V2 body draft as `source_locked_pending_external_review`.

GAP006 remains open because the 2024 suite-by-suite backlog is not exhausted and these rows have not passed GPT Pro / Claude re-review.
