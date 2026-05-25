# GAP006 2024海淀一模 Q6/Q7 Source Lock

Status: `local_source_locked_pending_external_review`

Scope: 2024 district backlog / 2024海淀一模 / 选择题 Q6-Q7

Evidence level: `A-formal answer-key lock`

Reason: current run matched the original 2024海淀一模 paper and official answer file. The formal细则 cache was checked but contains subjective-question scoring detail rather than independent Q6/Q7 objective explanations. These rows are official answer-key locks and still need GPT Pro / Claude re-review before release.

## Source Files

1. Original paper:
   - `C:\Users\Administrator\Desktop\2024各区模拟题\2024各区一模\2024海淀一模\试卷\高三政治：一模试题.pdf`
   - cache: `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\4bc0edec2a08a90e_高三政治_一模试题.md`
   - Q6 around `:98-105`; Q7 around `:108-114`.
2. Official answer:
   - `C:\Users\Administrator\Desktop\2024各区模拟题\2024各区一模\2024海淀一模\其他材料\一模政治-答案.docx`
   - cache: `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\98d1d762f302004f_一模政治-答案.md`
   - answer table around `:21-28`, locking `6=B, 7=C`.
3. Formal细则 cache checked:
   - `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\b692254ceb1b8174_2024海淀一模细则.md`
   - No independent Q6/Q7 objective explanation found in this cache.
4. Supporting classification cache:
   - `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\4b25cddd4dc2992d_2024届各区一模试题分类汇编选必3.md`
   - Q6-Q7 appear around `:108-148`.

## Q0081 = 2024海淀一模 Q6

Original prompt focus:

围棋实战中，从开盘布局、中盘拼杀，到收官阶段中的每一手棋的推敲、计算，通常都表现为各种形式的判断推理。判断哪些说法正确。

Options:

- ① 一步棋有多种走法，运用选言推理可以从中选择最优的解决方案。
- ② 断定不同走法与结果之间的必然联系，应运用必要条件假言判断。
- ③ 选点落子犹豫不决时，运用完全归纳推理方法才能取得最终胜利。
- ④ 一步棋与双方都有关联，采用逆向思维有助于作出正确判断推理。

Official answer key: `6 = B`, so ①④ are accepted.

Classification:

- `book_part`: reasoning, with thinking cross-registration for逆向思维.
- Correct lock: ①选言推理 for multiple possible moves; ④逆向思维 for looking from the opponent / outcome side.
- Trap boundary: ② overcommits to necessary-condition judgment; ③ overstates complete induction as a route to victory.

## Q0082 = 2024海淀一模 Q7

Original prompt focus:

“不是洋货买不起，而是国货更有性价比。”下列判断中，与上述句式判断类型一致的是。

Official answer key: `7 = C`

Classification:

- `book_part`: reasoning.
- Correct lock: “不是 P，而是 Q” functions as a联言判断: `非P 并且 Q`; option C also uses联言判断: 前提真实，并且推理形式有效。
- Trap boundary: A is充分必要条件判断; B is条件判断; D is必要条件 judgment with “除非”.

## Gate Impact

- Add Q0081-Q0082 to source coverage and queue.
- Add Q0081-Q0082 to reasoning-form ledger, choice-trap ledger, and reasoning handbook body.
- Add Q0081 as a cross-reference trigger in the thinking handbook body because the accepted answer includes逆向思维.
- Keep rows on hold: no GPT Pro review captured; Claude V39 not run; 2024 backlog still incomplete.
- Do not call final/pass.
