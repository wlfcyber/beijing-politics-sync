# Claude Opus 4.7 By-Question Review Digest

Source: same Claude web conversation, model selector shown as `Opus 4.7 Adaptive`.

Raw response: `08_review/claude_by_question_review_response_20260503.md`

Compatibility copy: `opus_writer/web_external/claude_by_question_review_response_20260503.md`

Boundary: Claude is a teaching-text and transfer advisor only. It did not decide local evidence truth.

## Verdict

Claude judged the draft as clearly improved and usable for internal preview after fixes, but not ready for external student final.

## Accepted Tasks

| issue_id | Claude issue | Codex local decision |
|---|---|---|
| CL-BQ-001 | Q17 answer card drops the phrase `国内国际两个市场、两种资源`. | ACCEPT. Local Q17 scoring supports this expression; patch answer-card wording. |
| CL-BQ-002 | Q16(2) uses an `如果材料进一步呈现` conditional inside the answer card. | ACCEPT. Move condition to caution; answer card should use subject-split wording. |
| CL-BQ-003 | 朝阳一模 Q20 fourth paragraph looks like a mandatory sweep-up paragraph. | ACCEPT AS STRUCTURE FIX. Mark it as optional sweep-up / compressible回扣, unless final evidence fusion later requires it as a separate paragraph. |
| CL-BQ-004 | 通州 Q20 phrase `中国提出全球治理公共产品` is unnatural. | ACCEPT. Patch to `中国把全球治理倡议作为重要国际公共产品贡献给世界`. |
| CL-BQ-005 | 海淀二模 Q21 is logically 2+2, but current answer card reads as four independent points. | ACCEPT. Add explicit one-side/other-side connectors. |
| CL-BQ-006 | 西城 Q20 answer card over-stacks six concepts in one sentence. | ACCEPT. Patch to fewer concepts in the answer card and move the rest to expression accumulation. |
| CL-BQ-007 | 海淀期末 Q22 and 东城 Q16 need a front-loaded use condition and `可用片段` label. | ACCEPT. Patch both into拓展迁移. |
| CL-BQ-008 | Bridge row `贡献中国智慧、中国方案、中国力量` needs scenario-specific wording. | ACCEPT. Patch use reminder. |

## P1 / Later Tasks

- Standardize every `材料抓手` into `看到材料原词 -> 想到核心点 -> 慎用条件`.
- Split `慎用提醒` into `使用条件` and `易错提醒`.
- Consider adding explicit主干点/可选点/慎用点 for each main question.

## Local Rule

No Claude wording can add a new scoring point by itself. All changes accepted here are either local-evidence supported or structure/wording improvements that do not create a new claim.
