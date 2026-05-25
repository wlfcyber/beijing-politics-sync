# GAP006 Source Lock: 2024朝阳二模 Q19(1)-Q19(2)

Status: `source_locked_pending_external_review`

This file advances GAP006 at the local source-evidence level only. It does not close the 2024 backlog, GPT Pro, Claude, Governor, Confucius, or final delivery gates.

## Source

- original paper cache: `gpt_sources/9223488a4b5e6f80_003202405朝阳高三二模政治试题.md:306-324`
- formal marking-rule cache: `gpt_sources/84218459671af8ac_2024朝阳二模细则.md:142-163`
- source type: original district paper text plus 2024朝阳二模主观题阅卷总结 / formal scoring detail

## Q0084 2024朝阳二模 Q19(1)

Evidence level: `A-formal`

Question:

> 生生之宇宙观体现了辩证思维的 ① 特征。人效法天地之德体现的推理类型是 ② 推理。（4分）

Material signal:

- `生生之宇宙观`: 宇宙处于生生不息的变化之中；“日新之谓盛德，生生之谓易”；宇宙永久的变易包含永远的革新。
- `法天地之人生观`: 人应该效法天地之德；天地生育万物不息、广阔博大，君子应学习天地之德，自强不息、厚德载物。

Formal rubric signal:

- Reference answer: `① 动态性 ② 类比`
- Variant for ①: `用变化发展的观点看问题` / `用矛盾运动的观点看问题` / `创新` can receive 1 point.
- Variant for ②: `类比推理，无变通`.

## Local Decision

Promote Q19(1) as `Q0084`, a cross-registered sample:

- thinking body: 辩证思维动态性
- reasoning body: 类比推理

This is not a full essay-style trigger chain, but it is a high-value bridge question because one blank trains thought-method recognition and the other trains reasoning-form recognition in the same material.

## Student-Usable Trigger Chain

- `生生不息、永久变易、日新、革新、成长和展开` -> the object is not static -> 辩证思维的动态性.
- `人效法天地之德` -> from the qualities of one object type, infer and model what another object should learn -> 类比推理.
- Do not replace `类比推理` with a broad phrase such as `联想` or `演绎`; the formal rubric says no variant for the second blank.

Answer sentence: 生生之宇宙观强调宇宙永远处在变化、更新和展开之中，体现辩证思维的动态性；人效法天地之德，是把天地之德类推到人的修身实践中，体现类比推理。

## Q0085 2024朝阳二模 Q19(2)

Evidence level: `A-formal`

Question:

> “夫大人者，与天地合其德，与日月合其明，与四时合其序。” 是哪种复合判断？该复合判断为真的条件是什么？（5分）

Formal rubric signal:

- Reference answer: `该判断是联言判断`.
- Scoring: writing `联言判断` gets 2 points; inaccurate expressions such as `充分/必要条件联言判断` do not receive the concept point.
- Truth condition: when and only when all conjuncts are true, the conjunctive judgment is true.
- Variant: if one conjunct is false, the conjunctive judgment is false; `全真才真，一假即假` can receive partial credit when wording is not fully standard.

## Local Decision

Promote Q19(2) as `Q0085` reasoning main-question row.

This is a clean conjunctive-judgment truth-condition sample. It belongs in the reasoning handbook under compound judgment recognition, and it should not be put into the thinking-method main chain.

## Student-Usable Trigger Chain

- The quoted sentence links three parallel clauses with the same subject structure: `与天地合其德` / `与日月合其明` / `与四时合其序`.
- The relationship is not `if...then...`, `only if`, or `either...or...`; it says several judgments are true together.
- Therefore it is a 联言判断.
- Truth口令: all conjuncts true -> whole judgment true; one conjunct false -> whole judgment false.

Answer sentence: 该复合判断是联言判断；只有组成它的各个联言支都是真的，这个联言判断才是真的，如果有一个联言支为假，整个联言判断就是假的。

## Gate Decision

Add Q0084 and Q0085 to the coverage matrix and source-packet queue.

Add Q0084 to both `MAIN_THINKING_LEDGER.csv` and `REASONING_FORM_LEDGER.csv`.

Add Q0085 to `REASONING_FORM_LEDGER.csv`.

Append both samples to the framework body drafts, but keep them `source_locked_pending_external_review` until real GPT Pro and Claude review are captured.
