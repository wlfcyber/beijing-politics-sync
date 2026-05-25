# GPT Pro V65 Clean Copy-Paste Prompt

Status: `READY_FOR_USER_VISIBLE_GPTPRO_SUBMISSION`

Use this prompt in a real GPT Pro chat after uploading `05_gptpro_review/GPTPRO_V65_UPLOAD_SET.zip` or the files listed below. Do not paste passwords, email addresses, or account details.

## Upload Files

Minimum upload set:

1. `10_packets__GPTPRO_REVIEW_PACKET_V65.md`
2. `08_delivery__选必三_逻辑与思维_思维宝典_框架重排送审版.md`
3. `08_delivery__选必三_逻辑与思维_推理宝典_题型重排送审版.md`
4. `07_governor_confucius__STUDENT_REVIEW_DRAFT_GOVERNOR_PRE_GPT_V65.md`
5. `07_governor_confucius__STUDENT_REVIEW_DRAFT_CONFUCIUS_PRE_GPT_V65.md`
6. `07_governor_confucius__OBJECTIVE_COMPLETION_AUDIT_PRE_EXTERNAL_V66.md`
7. `07_governor_confucius__EXTERNAL_REVIEW_CLOSURE_RUNBOOK_V74.md`
8. `05_gptpro_review__GPTPRO_V65_INTAKE_RUNBOOK.md`
9. `05_gptpro_review__GPTPRO_V65_RESULT_DROP_INSTRUCTIONS.md`

Useful context if upload limits allow:

V75 additional context:

- `05_gptpro_review__EXTERNAL_REVIEW_STATUS.md`
- `06_claude_review__EXTERNAL_REVIEW_STATUS.md`
- `06_claude_review__CLAUDE_V63_RUNBOOK.md`

V75 upload refresh note: this zip includes the latest V73/V74 closure gates. GPT Pro should still treat the drafts as not final and should not give a final pass.

7. `03_claudecode_lane__suite_reports__2026二模_B线复跑.md`
8. `03_claudecode_lane__2026_ERMO_B_LINE_RERUN_RESULT.md`
9. `03_claudecode_lane__blockers_2026_ermo.csv`
10. `03_claudecode_lane__fusion_candidates_2026_ermo.csv`
11. `08_delivery__STUDENT_REVIEW_DRAFT_CLEANUP_NOTE.md`
12. `08_delivery__DELIVERY_STATUS.md`

V88 required context:

- `01_source_inventory__SUITE_COVERAGE_AUDIT_V87.md`
- `07_governor_confucius__STUDENT_ARTIFACT_TRACEABILITY_DELTA_V88.md`
- `07_governor_confucius__STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv`
- `07_governor_confucius__STUDENT_ARTIFACT_TRACEABILITY_SUMMARY_V79.md`
- `08_delivery__选必三_逻辑与思维_推理宝典_学生送审版.md`

V88 refresh note: the latest upload zip now includes the V87/V88 reasoning-body refresh. Traceability is `153` total rows, `153` matched, `0` unmatched, and `0` unparsed. GPT Pro must review `Q0141-Q0143` as part of the reasoning-body draft, not only as audit-ledger rows.

## Prompt To Paste

```text
你是本项目的真实 GPT Pro 内容总审。请严格审查我上传的 V65 外审包和两本选必三《逻辑与思维》送审稿。

项目背景：
- 这是北京高考政治选必三《逻辑与思维》双宝典项目。
- 当前文件只是送审稿，不是终稿，不允许给 final pass。
- 思维宝典目标：按框架和材料触发链组织，质量对齐此前必修四哲学宝典的“材料信号 -> 方法触发 -> 卷面答案句”标准。
- 推理宝典目标：按同一推理形式归组，不能按地区年份散排。
- Codex 与 ClaudeCode 已做本地双线生产；你现在负责真实 GPT Pro 外审，但你的意见还必须由 Codex 回源验证后才能入稿。

请重点审查：
1. 思维宝典框架重排稿是否真正保住“材料动作 -> 方法触发 -> 卷面答案句”，有没有概念表格化、空泛化、误挂或触发链断裂。
2. 推理宝典题型重排稿是否真正把同一推理形式的考题放到一起，章节归类是否安全。
3. 是否还有学生可见的审核话术、内部编号、证据等级、状态字段、路径、模型痕迹或会误导学生的表达。
4. 2026 二模 B 线复跑和本地补丁是否足以进入 Claude V63 复审，尤其关注 Q0136、Q0137/Q0138、Q0139、Q0140 的边界是否安全。
5. V87/V88 新补入推理正文的 Q0141、Q0142、Q0143 是否归类安全：
   - Q0141：2024 东城二模 Q17(2)，已分别挂到科学归纳/求异法与类比推理；但有 source-path/internal-header suite identity conflict，必须审。
   - Q0142：2025 东城二模 Q18(2)，充分条件假言推理评价，重点看“结构有效但前提真实性需审查”的教学表述是否安全。
   - Q0143：2025 西城期末 Q17(2)，三段论构造，重点看补大前提的归类与学生写法是否安全。
6. 哪些问题必须在 Claude V63 前先由 Codex 回源修补。

请按以下格式输出，不要省略小节：

Verdict:
- 只能选一个：not_final / ready_for_claude_review_after_gptpro / reject

P0 findings:
- 用表格列出：id / 位置或文件 / 问题 / 为什么会影响学生或评分 / 需要回源检查的证据 / 必须动作
- 如果没有，写 none

P1 findings:
- 用表格列出：id / 位置或文件 / 问题 / 风险 / 建议动作
- 如果没有，写 none

思维宝典结构判断：
- 判断框架重排是否适合零基础学生进入。
- 判断触发链是否足够，指出最薄弱的 3-5 类问题。

推理宝典结构判断：
- 判断同形聚合是否完成。
- 指出任何章节归类不安全、混合过度、同形题遗漏或需要交叉索引的问题。

必须在 Claude V63 前回源修补的清单：
- 列出具体题号、章节或文件位置。
- 每项标注 P0/P1/P2。

禁止声明：
- 明确列出当前仍不能说的结论，例如 final、终稿、已通过、可发布、Word/PDF 成品等。

Codex 回源验证要求：
- 列出哪些 GPT Pro 意见必须回到原题、评分细则、答案表、source-lock 或 ledger 后才能采纳。

请不要给 final pass。请不要把当前送审稿说成终稿。
```

## Save Result

After GPT Pro responds, save the full response exactly here:

- `05_gptpro_review/GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md`

Then resume Codex so it can fill `05_gptpro_review/GPTPRO_V65_TRIAGE_FILLED.md`, apply only source-verified patches, and then run Claude V63.
