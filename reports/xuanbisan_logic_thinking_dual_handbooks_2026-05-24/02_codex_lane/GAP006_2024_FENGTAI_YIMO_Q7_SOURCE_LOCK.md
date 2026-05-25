# GAP006 2024丰台一模 Q7 Source Lock

Status: `local_support_locked_pending_external_review`

Scope: 2024 district backlog / 2024丰台一模 / 选择题 Q7

Evidence level: `A-support`

Reason: current run found a paper PDF that includes the original question and answer key, and rendered the relevant pages to resolve PDF text-order extraction. The formal 2024丰台一模细则 file was checked, but it does not provide an independent objective-question explanation for Q7. Therefore this row can enter local training as answer-key supported, but must not be overclaimed as an independently explained formal rubric sample.

## Source Files

1. Paper with answer key:
   - `C:\Users\Administrator\Desktop\2024各区模拟题\2024各区一模\2024丰台一模\试卷\2024北京丰台高三一模政治试题及答案.pdf`
   - cache: `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\5f5486bfc3baab2b_2024北京丰台高三一模政治试题及答案.md`
   - Q7 around `:80-92`; answer key around `:287-293`, locking `7=C`.
2. Local render check:
   - `09_logs/render_check_fengtai_2024_q7/fengtai2024_page_002_q7.png`
   - `09_logs/render_check_fengtai_2024_q7/fengtai2024_page_008_answer_key.png`
3. Supporting classification cache:
   - `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\4b25cddd4dc2992d_2024届各区一模试题分类汇编选必3.md`
   - Q7 appears around `:80-85`.
4. Formal rubric cache checked but no objective Q7 explanation was found:
   - `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\950d6b2d3cdda441_2024丰台一模细则.md`

## Q0080 = 2024丰台一模 Q7

Original prompt:

“法者，治之端也。”法是维持社会秩序、调整社会关系的一种社会规范。法是由国家制定或认可的社会规范。法是由国家强制力保证实施的具有普遍约束力的社会规范。

对上述文段的分析正确的是：

- A. 上述文段存在假言判断。
- B. 法律和社会规范是属种关系。
- C. “社会规范”在文中是不周延的。
- D. “法者，治之端也”是特称肯定判断。

Answer key: `7 = C`

Classification:

- `book_part`: reasoning.
- Correct lock: affirmative judgment predicate non-distribution.
- Trap boundary: A incorrectly sees hypothetical judgment; B loosely/reversely states the genus-species relation and shifts from “法” to “法律”; D mislabels the quoted judgment as a particular affirmative judgment.

## Gate Impact

- Add Q0080 to source coverage, queue, reasoning-form ledger, choice-trap ledger, and reasoning handbook body.
- Keep Q0080 on hold: no GPT Pro review captured; Claude V38 not run; no formal objective explanation recovered; 2024 backlog still incomplete.
- Do not call final/pass.
