# GAP005 Source Lock: 2025朝阳二模 Q17

Status: `source_locked_pending_external_review`

This file advances GAP005 at the local source-evidence level only. It does not close the 2025 suite backlog, GPT Pro, Claude V4/V5/V21, Governor, Confucius, or final delivery gates.

## Source

- paper and teacher-version cache: `gpt_sources/6009b3f19a33a729_2025北京朝阳高三二模政治_教师版.md:192-200,304-308`
- formal marking-rule cache: `gpt_sources/73c36c3077dced72_2025朝阳二模细则.md:71-79,86-107`
- raw paper: `C:\Users\Administrator\Desktop\2025各区模拟题\2025各区二模\2025朝阳二模\试卷\2025北京朝阳高三二模政治（教师版）.pdf`
- raw marking rule: `C:\Users\Administrator\Desktop\2025各区模拟题\2025各区二模\2025朝阳二模\细则\2025朝阳二模细则.docx`

The formal marking-rule docx cache is the evidence authority. The teacher-version cache is used for prompt, material, and answer alignment.

## Q0053 2025朝阳二模 Q17

Evidence level: `A-formal`

Question:

> 某校研究性学习小组探究影响北京地铁客运量的决定性因素。该组同学比较了不同线路客运量数据，分析 2024 年全年日均客运量位居前列的线路，发现这些线路沿线分布着很多著名景点。据此，该组同学得出结论：沿线景点数量是影响北京地铁客运量的决定性因素。分析材料，运用《逻辑与思维》知识，识别该组同学所运用的推理类型，谈谈如何更好发挥该推理类型的思维功能。

Formal rubric signal:

- 判断推理类型：指出该组同学运用的推理类型为不完全归纳推理，写归纳推理或不完全归纳推理均可给 1 分；推理类型写错，整题最多 2 分。
- 说明推理特点：该推理是或然推理。
- 指出推理局限：仅依据部分线路、客运量位居前列线路情况得出结论；从个别性知识为前提推出一般性结论；没有对前提中的每个对象情况都进行考察。
- 扩大考察范围：应考察更多认识对象，分析更多线路。
- 探究因果联系：探究客运量与景点数量、人口密度等因素的因果联系；求同法、求异法等可替代。
- 说明改进道理：提高前提与结论的相关程度，增强推理可靠性。

## Local Decision

Promote as `Q0053` reasoning main-question row.

This row should be grouped with归纳推理可靠程度, but it adds a cleaner “先判不完全归纳，再改进可靠性” exam template than the broader Q0047科学建议题.

## Student-Usable Trigger Chain

- material: only selected high-ridership subway lines are observed.
- inference: from some lines' features to a general conclusion about the decisive factor of subway ridership.
- type: 不完全归纳推理, because the premise does not examine every subway line.
- weakness: conclusion is probable, not necessary.
- improvement: examine more lines, test more factors such as景点数量 and人口密度, and use因果分析/求同法/求异法 to raise the connection between premises and conclusion.

Answer sentence: 该组同学运用的是不完全归纳推理。他们只根据部分客运量位居前列线路的沿线景点情况，推出沿线景点数量是影响地铁客运量的决定性因素，前提与结论之间具有或然联系。要更好发挥该推理的功能，应考察更多线路，深入探究客运量与景点数量、人口密度等因素的因果联系，提高前提与结论的相关程度，增强推理可靠性。

## Gate Decision

Add Q0053 to the coverage matrix, source-packet queue, reasoning-form ledger, and reasoning V2 body draft as `source_locked_pending_external_review`.

GAP005 remains open because the 2025 suite-by-suite backlog is not exhausted.
