# GPT-5.5 Pro Phase 04 Batch02 Raw Reply

- channel: ChatGPT web
- conversation: 高考政治四线工作流
- visible model: 进阶专业
- capture_method: Computer Use visual capture. Programmatic copy was unreliable because Safari copied the prompt/selection rather than the assistant reply, so this file records the visible GPT reply content that Codex confirmed on screen.
- prompt_file: `08_review/gpt_phase_advice/phase_04_batch02_prompt_for_gpt55.md`

## Visible Raw Excerpt

```text
verdict

GO_TO_BATCH03_AONLY_QUEUE

Batch02 可以作为 targeted visual/scope repair 通过。
但这只允许进入剩余 A-only / L1 队列分批复核。仍然禁止学生稿、Claude/Opus 成文化、Word/PDF、最终 PASS。

当前 17 个 L3/L4 可以进入 internal evidence archive skeleton，但是只能作为核对工具，不能优先于 A-only 112 行复核，也不能写成学生稿雏形。
```

## Must-Fix / Blocking Items Captured From Visible Reply

1. Accept `phase04_batch02_laneB_results_normalized.csv` only as a mechanical merge input, provided that an audit file exists for the column repair.
2. Keep the `2025海淀二模 Q12/Q13` answer-source locator explicit. If the answer-source location is missing later, those rows must return to L3 / no fusion lock.
3. Write the `2024西城一模 Q11` correction into the conflict record. Correct pairing is `B=①③`; if a later file still shows `B=①④`, treat it as contamination and roll back.
4. Freeze the Batch02 post-merge control counts in a dedicated status file before Batch03.
5. Do not let any archive skeleton become student-facing prose.

## Visible Notes Captured From Lower Reply

```text
当前最大质量风险是：17 个 L3/L4 看起来已经能支撑一个小型推理/思维归档，于是团队转去写稿，剩下 112 个 A-only 被边缘化。这个路径会复发上一版失败。

下一阶段主线必须是：
先清 A-only 112
再扩 L3/L4 evidence pool
再用 archive skeleton 反查漏题
最后才考虑成文化

短裁决：
GO_TO_BATCH03_AONLY_QUEUE
```

## Non-Pass Statement

GPT did not authorize Phase04 final promotion, student draft, Claude/Opus teaching rewrite, Word/PDF, or final PASS.
