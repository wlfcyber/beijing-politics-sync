# GAP006 Source Lock: 2024顺义二模 Q3/Q5/Q6/Q7

Status: `source_locked_pending_external_review`

This file advances GAP006 at the local source-evidence level only. It does not close the 2024 backlog, GPT Pro, Claude, Governor, Confucius, or final delivery gates.

## Source

- original paper cache: `gpt_sources/33010f3bed39e275_20240318顺义思政二模试题_定.md`
- official reference-answer cache: `gpt_sources/f986728ea555a6ed_2024顺义思政二模细则.md`
- answer-key lines: `f986728ea555a6ed_2024顺义思政二模细则.md:20-25`
- source type: district paper text plus independent reference-answer key

## Q0086 2024顺义二模 Q3

Evidence level: `B-choice-signal`

Prompt evidence:

- paper lines 38-43 show Q3 on the “文旅局” wave after哈尔滨冰雪经济火爆.
- option ③ says文旅局打造各自文旅名片 is the government using矛盾分析法科学履职.
- option ④ says网友喊话家乡文旅局“抄作业”“亮家底” is逆向思维.
- answer key line 23 locks Q3 = C, meaning ②③ are accepted and ④ is rejected.

Local decision:

- Promote as Q0086, a thinking choice-signal row.
- Use it to train two boundaries:
  - accepted signal:具体分析地方文旅资源和发展问题 can be read as矛盾分析法 in this official key.
  - rejected trap: “抄作业/亮家底” is not enough to call逆向思维.

This is not a main subjective scoring chain and should not be treated as a formal rubric explanation beyond the official option key.

## Q0087 2024顺义二模 Q5

Evidence level: `B-choice-signal`

Prompt evidence:

- paper lines 50-54 show Q5 on short-video first-person micro perspectives and scattered narrative.
- option C says creators narrating from different angles and directions is聚合思维.
- answer key lines 23-24 lock Q5 = B, so option C is rejected.

Local decision:

- Promote as Q0087, a thinking trap row only.
- Use it to train the boundary: “不同角度、不同方向、散点式叙事” is closer to发散思维/opening perspectives, not聚合思维.
- Do not add it as a positive thinking-method main chain because the correct answer is not a logic-and-thinking option.

## Q0088 2024顺义二模 Q6

Evidence level: `A-formal`

Prompt evidence:

- paper lines 55-71 show the question asking which “观点和逻辑分析” is correct.
- option C quotes the刑法第二十条正当防卫 clause and says the judgment belongs to复合判断.
- answer key line 24 locks Q6 = C.
- The extracted paper text omits the visible leading `6.` before line 55, but the sequence between Q5 and Q7 and the official answer key identify this as Q6.

Local decision:

- Promote as Q0088, a reasoning choice row on compound judgment recognition and logic-rule comparison.
- It belongs in the reasoning handbook, not the thinking-method main chain.

## Q0089 2024顺义二模 Q7

Evidence level: `A-formal`

Prompt evidence:

- paper lines 72-76 show Q7 using the condition sentence “只有不断加深对于数字劳动的认识，把握数字劳动的基本特征，并以此为基础构建起相关法律法规，才能确保数字劳动受到监管和保护，保证我国数字经济稳定和快速发展”.
- option C says构建起相关法律法规 is a necessary condition for guaranteeing stable and rapid economic development.
- answer key line 24 locks Q7 = C.

Local decision:

- Promote as Q0089, a reasoning choice row on necessary-condition hypothetical judgment.
- It belongs in the reasoning handbook, not the thinking-method main chain.

## Gate Decision

Add Q0086-Q0089 to the coverage matrix and source-packet queue.

Add Q0086 to `MAIN_THINKING_LEDGER.csv` as a choice-signal row, and add Q0086-Q0089 to `CHOICE_TRAP_LEDGER.csv`.

Add Q0088-Q0089 to `REASONING_FORM_LEDGER.csv` and the reasoning body draft.

Keep all four rows `source_locked_pending_external_review` until real GPT Pro and Claude review are captured.
