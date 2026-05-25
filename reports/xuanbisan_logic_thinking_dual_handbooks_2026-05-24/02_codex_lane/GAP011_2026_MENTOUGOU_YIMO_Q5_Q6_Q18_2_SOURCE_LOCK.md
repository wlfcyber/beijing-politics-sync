# GAP011 2026门头沟一模 Q5/Q6/Q18(2) Source Lock

Status: `source_locked_pending_external_review`

This file records a 2026门头沟一模 supplemental source lock. Q5 and Q6 are objective questions; Q18(2) is a formal main-question rubric under 《逻辑与思维》.

## Evidence

- Paper Q5-Q6: `preprocessed_corpus/gpt_sources/e84e6bbdd8988978_门头沟区高三政治一模试卷.md:96-113`
- Paper Q18(2): `preprocessed_corpus/gpt_sources/e84e6bbdd8988978_门头沟区高三政治一模试卷.md:274-280`
- Answer key: `preprocessed_corpus/gpt_sources/89313bd871502cf4_2026门头沟一模细则.md:20-52`
- Q18(2) rubric: `preprocessed_corpus/gpt_sources/89313bd871502cf4_2026门头沟一模细则.md:121-126`

## Q0095 2026门头沟一模 Q5

- Paper prompt: 北京鲜批市场公交专线 creatively sets the stop in the second-floor trading area, solving the last-mile procurement problem and creating a distinctive "bus upstairs" experience.
- Official key: Q5 = C, namely ②③.
- Promotion: `Q0095`, thinking choice-signal row.
- Evidence level: `B-choice-signal`; the answer key locks the option combination, but there is no independent objective-question explanation. It should train signal/trap boundaries, not a full主观题 trigger chain.
- Thinking signal: ② 对传统公交模式进行扬弃; ③ 打破思维定势、反向思考.
- Boundary: ① overstates system optimization as the target in this prompt; ④ misuses联想 and contradiction-transformation language.

## Q0096 2026门头沟一模 Q6

- Paper prompt: EAST is called an "artificial sun"; the question asks which judgment or reasoning statements are correct.
- Official key: Q6 = A, namely ①③.
- Promotion: `Q0096`, reasoning choice row.
- Evidence level: `A-formal` for local source lock, because the original paper and formal answer table match. Still pending real external review.
- Reasoning form: 类比推理 plus换位/换质 reasoning.
- Boundary: ② misstates the concept-extension relation; ④ illicitly converts the universal affirmative relation from "tokamak device" to "EAST device."

## Q0097 2026门头沟一模 Q18(2)

- Paper prompt: use 《逻辑与思维》 to explain the scientific thinking methods used by the court in solving an environmental dispute.
- Formal rubric: 辩证思维 3分, 创新思维 3分, overall logic 1分.
- Promotion: `Q0097`, thinking main-question row.
- Evidence level: `A-formal`.
- Trigger chain: environmental risks + long-term ecological/public/industrial goals -> 辩证思维; first settlement agreement insufficient + technical demonstration + multi-party negotiation + closed-loop mediation scheme -> 创新思维 with发散/聚合 and method innovation.

## Required Gates

- Add Q0095-Q0097 to coverage matrix and source queue.
- Add MT0041-MT0042, RF0061, and CT0038-CT0039.
- Add thinking handbook V2 sections 48-49 and reasoning handbook V2 section 43.
- Keep all rows on hold pending GPT Pro V47 / Claude V45 and B-line rerun.
