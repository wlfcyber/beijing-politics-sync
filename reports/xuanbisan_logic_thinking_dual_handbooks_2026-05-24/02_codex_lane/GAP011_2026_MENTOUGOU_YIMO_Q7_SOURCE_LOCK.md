# GAP011 2026门头沟一模 Q7 Source Lock

Status: `source_locked_pending_external_review`

This file records a 2026门头沟一模 supplemental source lock for Q7. It is an objective choice question with a reliable answer key, but no independent objective-question explanation has been recovered. Therefore it enters only as a `B-choice-signal` mixed-boundary row.

## Evidence

- Paper Q7: `preprocessed_corpus/gpt_sources/e84e6bbdd8988978_门头沟区高三政治一模试卷.md:117-124`
- Answer key: `preprocessed_corpus/gpt_sources/89313bd871502cf4_2026门头沟一模细则.md:20-52`

## Q0099 2026门头沟一模 Q7

- Paper prompt: 学农教育让学生走进田间整地做畦、移栽菜苗，在操作间炒菜、制作豆腐，从背诵诗句转向切身感受劳动艰辛，并同时掌握生活技能、理解劳动价值。
- Official key: Q7 = B, namely ①④.
- Promotion: `Q0099`, thinking choice-signal row.
- Evidence level: `B-choice-signal`; the answer key locks the option combination, but there is no independent objective-question explanation. It must train signal/trap boundaries, not a full主观题 trigger chain.
- Correct-option boundary: ① is a 必修四实践第一观点 signal and should not be absorbed into the elective-3 thinking-method main chain. ④ is the elective-3 signal:兼顾农业技能培养与劳动价值观塑造，体现辩证思维整体性.
- Wrong-option traps: ② misstates thinking as direct; thinking is间接性、概括性 and能动性. ③ overuses思维抽象到思维具体;从劳动实践提炼劳动价值 can be abstraction, but the option does not show returning from abstract规定 to a many-sided concrete whole, and the official key excludes it.

## Required Gates

- Add Q0099 to coverage matrix and source queue.
- Add MT0044 and CT0040.
- Add thinking handbook V2 section 51.
- Keep Q0099 on hold pending GPT Pro V49 / Claude V47 and B-line rerun.
