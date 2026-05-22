# 04 GPT / Claude 框架生长记录

## 真实模型调用链

| 轮次 | GPT | Claude | Codex 处理 | 结论 |
|---|---|---|---|---|
| Round 01 | `model_outputs/gpt_round01_independent_framework.md` | `model_outputs/claude_round01_independent_framework.md` | `codex_adjudication/CODEX_ROUND01_ROUND02_ADJUDICATION.md` | 形成候选框架，待源检查 |
| Round 02 | `cross_critiques/gpt_critiques_claude_round01.md` | `cross_critiques/claude_critiques_gpt_round01.md` | 覆盖度与冲突裁决 | 六入口候选可覆盖 42/42 |
| Source Check | 无新模型 | 无新模型 | `codex_source_checks/pending_source_check_20260522.md` | 边界题保留/排除，分布不变 |
| Round 03 | `model_outputs/gpt_round03_source_check_review.md` | `model_outputs/claude_round03_source_check_review_key_capture.md` | `codex_adjudication/CODEX_ROUND03_SOURCE_CHECK_ADJUDICATION.md` | 双模型接受源检查候选，无结构变化 |

## GPT Round 03 结论

GPT 在 ChatGPT web clean conversation 中完成 Round 03。记录文件写明：可见模式为 `进阶专业`，准确 `GPT-5.5 Pro` 标签未独立可见，因此保留 model-label caution。其具体 verdict 为：

`accept_source_checked_candidate_no_structural_change`

GPT 接受的关键点：

- 六入口不作结构变化。
- E1=9, E2=8, E3=3, E4=7, E5=11, E6=4 的分布不变。
- CC0137、CC0289、CC0223、CC0364、CC0051、CC0195 的源检查边界接受。
- CC0162、CC0040、CC0353、CC0380 保持 reference/open，不晋升。
- 仍不能把源检查候选直接叫 final PASS。

## Claude Round 03 结论

Claude web 可见模型为 `Opus 4.7 Adaptive`，Round 03 key capture 的 verdict 为：

`accept_source_checked_candidate_no_structural_change`

Claude 接受的关键点：

- 源检查属于边界收紧，不是框架重构。
- 42/42 locked core 仍被六入口覆盖。
- 不需要第七入口。
- E1、E2、E4、E5、E6 需要写入学生误判边界；E3 标注低频。

## Codex 本地裁决

本地源证据优先于模型共识。GPT/Claude 的一致意见只用于确认：在 Codex 源检查已经闭合的前提下，六入口结构可以作为 v12.2 框架 baseline。最终文档生产仍是独立 gate。
