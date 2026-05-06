# Phase 11C Bad Word Four-Element Failure Audit

## Trigger

2026-05-05 CST, user reviewed the Word from:

`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_完全模仿哲学宝典返工_2026-05-04/04_delivery/选必三逻辑与思维_完全模仿哲学宝典_学生版_2026-05-04.docx`

User verdict: content quality is poor; the four elements under each question are insufficient and unclear.

## Local Audit Result

The user verdict is correct. This artifact may not be used as final or as a base for cosmetic polishing.

Quick counts from its paired Markdown:

| Check | Count | Verdict |
|---|---:|---|
| Total `【材料触发点】` entries | 181 | Not enough by itself |
| Generic fake prompt `本题要求结合材料说明其体现的思维方法...` | 101 | FAIL |
| Meta answer prefix `卷面要把材料中的具体动作写进方法里：` | 101 | FAIL |
| Student-answer entries that read like production instructions | 101+ | FAIL |
| Philosophy benchmark occurrences of the same generic prompt | 0 | Shows mismatch |
| Philosophy benchmark occurrences of the same meta answer prefix | 0 | Shows mismatch |

## Why It Fails

1. `设问` is often not the real question sentence. It is a placeholder. The philosophy benchmark uses the actual prompt.
2. `答案落点` often says what the writer should do, not what the student can write. A valid answer landing must be a direct answer sentence: thinking method + material fact + effect/conclusion.
3. Same-question multi-node mounting often repeats the same four elements, instead of rewriting the entry for that exact node and small method.
4. Complex questions are flattened into method lists such as `科学思维 + 辩证思维 + 创新思维`; this does not tell a weak student which material signal triggers which method.
5. Choice-question entries often repeat a generic instruction about circling material actions, instead of giving all options, correct answer logic, tempting wrong-option logic, and trap type.
6. The artifact reads like a compressed index dressed in philosophy format. It is not yet a philosophy-style teaching artifact.

## New Hard Gate

Every future 选必三 student entry must pass all of these:

- `材料触发点`: concrete material signal(s), not only a topic label.
- `设问`: actual question prompt. If unavailable, mark blocked and return to source.
- `为什么能想到`: material signal -> total hat -> small method -> why nearby methods are weaker or wrong when useful.
- `答案落点`: direct answer-sheet sentence(s), not instructions such as `先写`, `要写`, `卷面要`, or `本题要求`.
- Multi-node same-question entries must be node-specific. If one question appears under `科学思维`, `分析与综合`, and `发散聚合`, each entry must explain that node's trigger and answer landing separately.
- No Word/PDF/final until the whole draft passes this gate and external GPT/Claude review has concrete content corrections closed locally.

## Gold-Standard Mini Example

Bad artifact style for `2025东城期末 Q18(2)`:

> 答案落点：卷面要把材料中的具体动作写进方法里：看到造型元素跨界联结写联想，看到多需求统筹写发散与聚合，看到提前预判月面环境写超前。

Acceptable student-facing style:

`答案落点`: 登月服设计把“飞天”飘带、火箭升空尾焰和航天服造型联系起来，体现联想思维；又围绕月面出舱任务同时考虑行走、攀爬、驾车、科考、防护和防眩光等多种需要，并收束成服务登月任务的整体方案，体现发散思维与聚合思维。

This still requires source verification before merge, but it shows the required direction: no production instruction, no empty method list, and each method is tied to material action.

## Status

`HARD_FAIL_BAD_WORD_CONTENT_GATE`

The bad Word/Markdown is frozen as a failure sample only. The active four-line project must continue from the evidence-locked/current Phase11 materials, not from this Word as a deliverable base.
