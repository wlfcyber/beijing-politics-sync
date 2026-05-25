# GAP005 Source Lock: 2025西城一模 Q17

Status: `source_locked_pending_external_review`

This file advances GAP005 and GAP009 at the local source-evidence level only. It does not close the 2025 suite backlog, GPT Pro, Claude V4/V5/V14, Governor, Confucius, or final delivery gates.

## Source

- paper and teacher-version cache: `gpt_sources/2542f29bb04e2ae0_2025北京西城高三一模政治_教师版.md:225-232,340-342`
- formal marking-rule cache: `gpt_sources/af675a5d751f41db_2025西城一模细则.md:73-78`
- raw paper: `C:\Users\Administrator\Desktop\2025各区模拟题\2025各区一模\2025西城一模\试卷\2025北京西城高三一模政治（教师版）.pdf`
- raw marking rule: `C:\Users\Administrator\Desktop\2025各区模拟题\2025各区一模\2025西城一模\细则\2025西城一模细则.docx`

The formal marking-rule docx is the evidence authority. The teacher-version cache is used for the prompt, material, and answer alignment.

## Q0046 2025西城一模 Q17

Evidence level: `A-formal`

Question:

> 结合材料，说明“温榆生态心”建设中蕴含的科学思维。

Formal rubric signal:

- 角度1：追求认识的客观性。科学思维要从实际出发、努力把握和遵循客观规律；“生态心”建设从当地客观自然条件出发，遵循自然规律，实现人与自然和谐统一。
- 角度2：辩证思维。科学思维要运用辩证思维方法，用联系的、变化发展的、全面的观点思考问题，分析生态心建设的各个要素，整体规划，营造良好生态环境，促进生态建设。
- 角度3：创新思维。科学思维要能创新性解决问题；创新思维的“新”意味着思路新、方法新、结果新，或逆向思维；生态心没有常见的服务设施，甚至全面封闭，营造独特的生态系统和荒野景观。
- 评阅细则要求从以上三个维度回答。

## Local Decision

Promote as `Q0046` thinking main-question row.

This is a formal composite thinking sample. The prompt uses scientific thinking, while the marking rule requires客观性、辩证思维、创新思维 three scoring dimensions. It advances GAP009 alongside Q0011 and Q0041.

## Student-Usable Trigger Chain

- material action: 温榆生态心根据清河、温榆河交汇处水流、鱼、昆虫、水鸟等客观条件，取消常规游乐设施、园径和路灯，营建河心岛、深潭浅滩，部分粮田留给鸟兽，并封闭核心区让自然演替主导生态恢复。
- trigger logic:
  - `从当地自然条件出发` -> 科学思维追求认识的客观性。
  - `水流、鱼虫鸟兽、粮田、核心区封闭等多要素整体规划` -> 辩证思维的联系、发展、全面观点。
  - `不按一般公园建设逻辑，反向减少人工设施，让自然演替主导` -> 创新思维的思路新、方法新、结果新，也带有逆向思维。
- answer sentence: 温榆生态心从当地水系、生物和荒野条件出发，遵循自然规律，整体规划河心岛、深潭浅滩、粮田和封闭核心区，并用不同于普通公园的建设思路让自然演替主导生态恢复，体现科学思维的客观性、辩证思维和创新思维。

## Gate Decision

Add Q0046 to the coverage matrix, source-packet queue, main-thinking ledger, and thinking V2 body draft as `source_locked_pending_external_review`.

GAP005 remains open because the 2025 suite-by-suite backlog is not exhausted. GAP009 remains open but further advanced because Q0046 adds another formal scientific-prompt composite sample.
