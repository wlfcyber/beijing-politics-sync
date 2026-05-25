# GAP005 Source Lock: 2025东城一模 Q18(1)

Status: `source_locked_pending_external_review`

This file advances GAP005 at the local source-evidence level only. It does not close the 2025 suite backlog, GPT Pro, Claude V4/V5/V19, Governor, Confucius, or final delivery gates.

## Source

- paper and teacher-version cache: `gpt_sources/46c444a91d491a4f_2025北京东城高三一模政治_教师版.md:183-189,305-308`
- formal marking-rule PDF cache: `gpt_sources/c254bbee61da4abd_2025东城一模细则.md:81-97`
- raw paper: `C:\Users\Administrator\Desktop\2025各区模拟题\2025各区一模\2025东城一模\试卷\2025北京东城高三一模政治（教师版）.pdf`
- raw marking rule: `C:\Users\Administrator\Desktop\2025各区模拟题\2025各区一模\2025东城一模\细则\2025东城一模细则.pdf`

The formal marking-rule PDF cache is the evidence authority. The teacher-version cache is used for prompt, material, and answer alignment.

## Q0051 2025东城一模 Q18(1)

Evidence level: `A-formal`

Question:

> 结合材料一，说明“两重”实施是如何体现辩证思维的。

Formal rubric signal:

- 第一层：知识 1 分 + 材料分析 1 分。“两重”在实施中坚持辩证思维的整体性、动态性以及实践的观点；既强化“硬投资”，又要搞好“软建设”；既解决当前问题，又着眼长远目标。
- 变通：整体性可替换为联系的观点、全面的观点、坚持系统优化、综合的观点、立足整体；动态性可替换为发展的观点、量变质变。
- 第二层：知识 1 分 + 材料分析 1 分。抓主要矛盾，聚焦新质生产力发展等核心领域，加快推进重大战略实施和重点领域安全能力建设。
- 变通：抓主要矛盾可替换为坚持两点论重点论相统一。只写“运用矛盾分析法”且材料分析准确，只得本层次 1 分。
- 学生问题：只答“辩证思维的特点”细节知识，或只答矛盾观点，或选用“创新思维”知识。

## Local Decision

Promote as `Q0051` thinking main-question row.

This is a clean辩证思维 trigger sample. It has two scoring layers: the first trains整体性/动态性/实践观点 from paired material actions, and the second trains抓主要矛盾 from“聚焦核心领域”.

## Student-Usable Trigger Chain

- `硬投资 + 软建设` -> not a single measure, but multiple linked elements coordinated together -> 辩证思维整体性/联系全面/系统优化.
- `解决当前问题 + 着眼长远目标` -> development process and practical problem-solving over time -> 动态性/发展观点/实践观点.
- `聚焦新质生产力等核心领域` -> identify the key field that drives the overall task -> 抓主要矛盾 / 两点论与重点论统一.

Answer sentence: “两重”实施既强化硬投资又搞好软建设，体现辩证思维的整体性；既解决当前问题又着眼长远目标，体现动态性和实践观点；聚焦新质生产力等核心领域推进重大战略和重点领域安全能力建设，体现抓主要矛盾、坚持两点论与重点论统一。

## Gate Decision

Add Q0051 to the coverage matrix, source-packet queue, main-thinking ledger, and thinking V2 body draft as `source_locked_pending_external_review`.

GAP005 remains open because the 2025 suite-by-suite backlog is not exhausted.
