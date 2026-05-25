# GAP005 Source Lock: 2025房山一模 Q16(2)-Q16(3)

Status: `source_locked_pending_external_review`

This file advances GAP005 at the local source-evidence level only. It does not close the 2025 suite backlog, GPT Pro, Claude V4/V5/V11, Governor, Confucius, or final delivery gates.

## Source

- paper and teacher-version cache: `gpt_sources/3227fd51f2020c04_2025北京房山高三一模政治_教师版.md:156-176`
- formal marking-rule cache: `gpt_sources/17cdecfbd774ee79_2025房山一模细则.md:46-68`
- raw paper: `C:\Users\Administrator\Desktop\2025各区模拟题\2025各区一模\2025房山一模\试卷\2025北京房山高三一模政治（教师版）.pdf`
- raw marking rule: `C:\Users\Administrator\Desktop\2025各区模拟题\2025各区一模\2025房山一模\细则\2025房山一模细则.pdf`

The teacher-version answer states that the original paper did not contain an answer for Q16(2)-Q16(3), so the formal marking-rule cache is the evidence authority for scoring. The teacher-version cache is used here for the prompt and material context.

## Q0042 2025房山一模 Q16(2)

Evidence level: `A-formal`

Question:

> 请以“博物馆是保护和传承人类文明的重要殿堂”为结论，编写一个合乎规则的三段论。

Formal rubric signal:

- 前提为真，推理结构正确，符合三段论基本规则：4分。
- 只写出正确前提、没写结论：3分。
- 其他错误不得分。

Local decision: promote as `Q0042` reasoning main-question row.

Student-usable reasoning chain:

- conclusion term: 大项 = 保护和传承人类文明的重要殿堂；小项 = 博物馆。
- usable middle term: 具有教育功能的场所，或承载人类历史文化遗产并通过展示研究推动文明延续的场所。
- valid structure: `M are P; S are M; therefore S are P`.
- answer sentence: 具有教育功能的场所是保护和传承人类文明的重要殿堂；博物馆是具有教育功能的场所；所以，博物馆是保护和传承人类文明的重要殿堂。

## Q0043 2025房山一模 Q16(3)

Evidence level: `A-formal`

Question:

> 结合材料，运用创新思维知识，就“如何让琉璃河遗址‘热’起来”提两条建议。

Formal rubric signal:

- 任一个思维 + 合理建议：2分。
- 创新思维的三个特征角度提合理建议：2分；两点4分。
- 知识和建议结合不够严谨，最高3分；建议与知识不匹配或只解释知识，2分；只有建议没有知识，1分。

Local decision: promote as `Q0043` thinking main-question row.

Student-usable trigger chain:

- material action: 琉璃河遗址有青铜罍铭文、两重城垣、三千年建城史等考古资源，但要从静态遗址转成可体验、可传播、能吸引年轻人的公共文化场景。
- trigger logic:
  - `多方案打开` -> 发散思维。
  - `借用沉浸式研学/角色扮演` -> 借用方法和联想思维。
  - `静态青铜器转成AI动态视频` -> 逆向思维、转换性思考。
  - `内容新、方法新、效果新` -> 创新思维三新。
- answer sentence: 让琉璃河遗址“热”起来，可以用发散思维设计沉浸式研学、角色扮演和互动解谜等多样体验，也可以运用逆向思维把静态文物转化为 AI 动态视频等新表达，扩大年轻群体关注。

## Gate Decision

Add Q0042 to the coverage matrix, source-packet queue, reasoning-form ledger, and reasoning V2 body draft as `source_locked_pending_external_review`.

Add Q0043 to the coverage matrix, source-packet queue, main-thinking ledger, and thinking V2 body draft as `source_locked_pending_external_review`.

GAP005 remains open because the 2025 suite-by-suite backlog is not exhausted.
