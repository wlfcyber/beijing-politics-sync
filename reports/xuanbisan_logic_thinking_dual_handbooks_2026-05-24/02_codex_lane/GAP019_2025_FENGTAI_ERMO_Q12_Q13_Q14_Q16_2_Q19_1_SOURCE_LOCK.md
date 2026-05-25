# GAP019 Source Lock: 2025丰台二模 Q12/Q13/Q14/Q16(2)/Q19(1)

Status: `source_locked_pending_external_review`

This file advances GAP019 at the local source-evidence level only. It does not close the 2025 suite scan, ClaudeCode B-line rerun, GPT Pro, Claude, Governor, Confucius, or final delivery gates.

## Sources

- Paper and embedded teacher answer: `preprocessed_corpus/gpt_sources/9f3b486088840b52_2025北京丰台高三二模政治_教师版.md`
  - Q12-Q14 prompt: `:177-198`
  - Q16(2) prompt: `:214-232`
  - Q19(1) prompt and material: `:271-347`
  - answer key and reference answer: `:368-412`
- Q16(2) marking rule: `preprocessed_corpus/gpt_sources/e3e9942211ec52f9_16._2.md:20-78`
- Q19(1) marking rule: `preprocessed_corpus/gpt_sources/0e0ec077bf920336_19._1.md:20-78`

## q0108-2025丰台二模-q12

Evidence level: `A-support`

Paper evidence:

- Q12 describes a technology-transfer model: a company may use a patent free for one year and pay later according to use, similar to "try before buying".
- Teacher answer key locks Q12 = C, i.e. ②③.

Local decision:

- Promote as `Q0108`, a thinking choice row.
- It trains逆向思维 and辩证思维动态性 as support-level choice evidence.
- Because no independent objective-question rubric explanation was recovered, keep it as `A-support`.

## q0109-2025丰台二模-q13

Evidence level: `A-support`

Paper evidence:

- Q13 asks students to judge claims about concepts, judgments, and reasoning.
- Teacher answer key locks Q13 = A.

Local decision:

- Promote as `Q0109`, a reasoning choice row.
- The stable positive point is关系判断中的非传递关系: 甲是乙的同学、乙是丙的同学, 不必然推出甲是丙的同学.
- Keep the other options as traps: incomplete division, particular-negative换位, and definition over-narrowness.
- Because no independent objective-question rubric explanation was recovered, keep it as `A-support`.

## q0110-2025丰台二模-q14

Evidence level: `A-support`

Paper evidence:

- Q14 uses Marx's movement from commodity to money, capital, surplus value, and capitalist contradictions.
- Teacher answer key locks Q14 = B, i.e. ①④.

Local decision:

- Promote as `Q0110`, a thinking choice row.
- It trains感性具体到思维抽象 and辩证思维方法.
- Because no independent objective-question rubric explanation was recovered, keep it as `A-support`.

## q0111-2025丰台二模-q162

Evidence level: `A-formal`

Prompt evidence:

- Q16(2) asks students to construct a syllogism with the conclusion "`大思政课`有利于培养时代新人".

Marking-rule evidence:

- The marking rule requires labels for大前提/小前提/结论, gives full credit for a correct syllogism structure, and identifies the structure as: all M are P; S is M; therefore S is P.
- It lists common zero-credit errors: four concepts, undistributed middle term, illicit minor, changing the conclusion, missing conclusion, and writing a sufficient conditional or conjunctive inference instead.

Local decision:

- Promote as `Q0111`, a formal reasoning main-question row on三段论构建.
- Add to reasoning handbook under same-form syllogism construction.

## q0112-2025丰台二模-q191

Evidence level: `A-formal`

Prompt evidence:

- Q19(1) asks whether the claim is correct: "只要给 AI 装上版权雷达, 提前扫描问题指令, 就能防止点击盗版资源网站", and requires《逻辑与思维》reasoning.

Marking-rule evidence:

- The marking rule requires: judgment that the view is partial/wrong; logic reason that版权雷达 is an important condition but not a sufficient condition; and a further explanation of how to prevent piracy by配套法律机制/技术检测/用户素养提升 and辩证思维.
- It explicitly flags common errors: treating the claim as an inference rather than a sufficient conditional judgment, confusing sufficient and necessary conditions, using conjunctive judgment from the material, and omitting the "what should be done" layer.

Local decision:

- Promote as `Q0112`, a dual `thinking+reasoning` main-question row.
- Register the reasoning side as充分条件假言判断真假辨析: "只要P就Q" is false if P is only important but not sufficient.
- Register the thinking side as辩证思维/综合治理 trigger: solving AI copyright piracy requires multiple coordinated measures, not a single technical device.

## Gate Decision

Add Q0108-Q0112 to the coverage matrix and source-packet queue.

Add Q0108/Q0110/Q0112 to `MAIN_THINKING_LEDGER.csv`; add Q0109/Q0111/Q0112 to `REASONING_FORM_LEDGER.csv`; add Q0108-Q0110 to `CHOICE_TRAP_LEDGER.csv`.

Keep Q0108-Q0112 on hold until GPT Pro V54, Claude V52, and B-line rerun are reconciled. Do not call final/pass.
