# GAP006 2024石景山一模 Q6/Q7 Source Lock

Status: `local_support_locked_pending_external_review`

Scope: 2024 district backlog / 2024石景山一模 / 选择题 Q6-Q7

Evidence level: `A-support`

Reason: current run found the original teacher-version paper with an embedded answer key, but no independent formal scoring rubric or district marking rule for Q6-Q7. These rows can be used as local training samples, but must not be promoted as A-formal rubric samples.

## Source Files

1. Teacher-version paper with answer key:
   - `C:\Users\Administrator\Desktop\2024各区模拟题\2024各区一模\2024石景山一模\试卷\2024北京石景山高三一模政治（教师版带答案）.docx`
   - cache: `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\f581620be44a4c2c_2024北京石景山高三一模政治_教师版带答案.md`
   - cache lines: Q6 around `:53-56`, Q7 around `:57-61`, answer key around `:188`.
2. Supporting classification cache:
   - `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\4b25cddd4dc2992d_2024届各区一模试题分类汇编选必3.md`
   - Q7 appears in the logic-rule section around `:72-77`.
   - Q6 appears in the thinking/reasoning section around `:283-286`.
3. Support lecture PPT was checked but does not provide a formal scoring rule for Q6/Q7:
   - `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\935b8ea1e01b3ba5_2024年石景山一模.md`

## Q0074 = 2024石景山一模 Q6

Original prompt:

海草床可以经光合作用产生大量氧气，被誉为“海洋之肺”。近年来，受人类活动影响，全球约三分之一的海草床已经消失，严重影响到海岸带生态安全。我国科研人员研究出了“海草培育移植法”，通过“优选种子——人工育苗——移植”的方法提高了移植过程的人工可控性和种子成活率。这种技术：

- ① 运用了联想思维，通过迁移搭建由此及彼的桥梁。
- ② 运用了类比推理，模仿地上植物移植的技术方法。
- ③ 运用了超前思维，用发展眼光构想事物发展趋势。
- ④ 运用了发散思维，以寻求解决问题的多样性答案。

Options:

- A. ①②
- B. ①③
- C. ②④
- D. ③④

Teacher answer key: `6 = A`

Classification:

- `book_part`: thinking, with reasoning cross-registration.
- Correct lock: ①联想思维迁移 + ②类比推理.
- Trap boundary: ③把生态修复技术误判为超前思维趋势预测；④把既定移植方案误判为发散思维多方案求解.

## Q0075 = 2024石景山一模 Q7

Original prompt:

概念的外延是指具有概念所反映的本质属性的事物的范围，人们经常用图来表示概念外延之间的关系。对此，下列说法正确的是：

- ① 图甲，可以用来描述财产权和物权的关系。
- ② 图乙，可以用来描述国体和政体的关系。
- ③ 图丙，如果 Q 是社会主要矛盾，S 是生产力，P 是生产关系。
- ④ 图丁，如果 Q 是领土，S 可以是领陆，P 可以是领空。

Options:

- A. ①③
- B. ①④
- C. ②③
- D. ②④

Teacher answer key: `7 = B`

Classification:

- `book_part`: reasoning.
- Correct lock: concept-extension relation choice; answer B means ① and ④ are accepted.
- Trap boundary: ② misreads 国体/政体 as a diagrammed extension relation; ③ misplaces social principal contradiction, productive forces, and production relations into the shown extension pattern.

## Gate Impact

- Add Q0074/Q0075 to source coverage, queue, reasoning-form ledger, choice-trap ledger, and reasoning/thinking body drafts.
- Keep both rows on hold: no GPT Pro review captured; Claude V35 not rerun; 2024 backlog still incomplete.
- Do not call final/pass.
