# GAP006 2024西城一模 Q11/Q12/Q13 Source Lock

Status: `local_source_locked_pending_external_review`

Scope: 2024 district backlog / 2024西城一模 / 选择题 Q11-Q13

Evidence level: `A-formal answer-key lock`

Reason: current run matched the original 2024西城一模 paper, the official answer/scoring-reference file, the formal rubric cache answer table, and a local render check for the Q11 layout. These are formal answer-key locks for choice-question training. They still need GPT Pro / Claude re-review before any release claim.

## Source Files

1. Original paper:
   - `C:\Users\Administrator\Desktop\2024各区模拟题\2024各区一模\2024西城一模\试卷\2024.4高三统一测试思想政治试卷.docx`
   - cache: `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\2aa2ee045f75ecd8_2024.4高三统一测试思想政治试卷.md`
   - Q11 around `:105-143`; Q12-Q13 around `:145-156`.
2. Official answer and scoring reference:
   - `C:\Users\Administrator\Desktop\2024各区模拟题\2024各区一模\2024西城一模\其他材料\2024.4高三统一测试思想政治答案.docx`
   - cache: `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\91e28443e7a1bb0e_2024.4高三统一测试思想政治答案.md`
   - answer table around `:20-25`, locking `11=B, 12=C, 13=B`.
3. Formal rubric cache:
   - `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\f7bcf000f212cc69_2024西城一模细则.md`
   - answer table around `:20-25`.
4. Local render check for the Q11 layout:
   - `09_logs/render_check_west_2024_q11/west2024_page_005_q11.png`
   - `09_logs/render_check_west_2024_q11/west2024_page_006_q12_q13.png`

## Q0076 = 2024西城一模 Q11

Prompt focus:

“问天”“梦天”“天和”不仅是中国空间站的三个舱段，也是中国航天人走过的路，它们连缀起中华民族求索太空的浩瀚征程。据此，以下推理正确的是。

Original layout checked from render:

- ① 从“问天/梦天/天和分别是中国空间站的舱段”推出“问天、梦天、天和都是中国空间站的舱段”。
- ② 从“问天/梦天/天和分别是中国航天人走过的路”推出“中国航天人走过的路，或是问天，或是梦天，或是天和”。
- ③ 由“问天、梦天、天和连缀起中华民族求索太空的浩瀚征程”和“中国空间站的三个舱段是问天、梦天、天和”，推出“中国空间站的三个舱段连缀起中华民族求索太空的浩瀚征程”。
- ④ 从“问天/梦天/天和分别是中国航天人走过的路”推出“问天、梦天、天和连缀起中华民族求索太空的浩瀚征程”。

Official answer key: `11 = B`, so ①③ are accepted.

Classification:

- `book_part`: reasoning.
- Correct lock: bounded enumeration / collective judgment plus same-object substitution.
- Trap boundary: ② overgeneralizes three named examples into an exhaustive disjunction; ④ adds a whole-relation predicate not guaranteed by the separate premises.

## Q0077 = 2024西城一模 Q12

Prompt focus:

黑格尔说，人们总以为肯定和否定具有绝对的区别，其实两者是相同的。我们甚至可以称肯定为否定，也可以称否定为肯定。譬如说一条往东的路同时也是一条往西的路。对此理解正确的是。

Official answer key: `12 = C`

Classification:

- `book_part`: thinking.
- Correct lock: 肯定与否定互为条件，且只存在于它们的联系中。
- Trap boundary: not denying all boundaries, not splitting肯定/否定 into unrelated objects, and not refusing both attitudes.

## Q0078 = 2024西城一模 Q13

Prompt focus:

朱光潜以“火”字为起点，说明不同人或同一人在不同时境中的联想线索会变化，从而得出联想的散漫飘忽。

Official answer key: `13 = B`

Classification:

- `book_part`: thinking.
- Correct lock: 联想具有非逻辑制约的畅想性。
- Trap boundary: do not confuse联想 with思维抽象、判断串联, or或然推理.

## Gate Impact

- Add Q0076-Q0078 to source coverage and queue.
- Add Q0076 to the reasoning-form ledger and reasoning handbook body.
- Add Q0076-Q0078 to the choice-trap ledger.
- Add Q0077-Q0078 to the thinking handbook body.
- Keep rows on hold: no GPT Pro review captured; Claude V37 not run; 2024 backlog still incomplete.
- Do not call final/pass.
