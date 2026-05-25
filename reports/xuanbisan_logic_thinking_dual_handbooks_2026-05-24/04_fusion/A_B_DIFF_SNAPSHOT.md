# A/B Diff Snapshot

Status: `SNAPSHOT_NOT_FINAL`

## Counts

- Codex A coverage matrix: 26 source-locked rows.
- Codex A ledgers: 8 thinking rows, 24 reasoning rows, 6 choice-trap rows.
- ClaudeCode B coverage matrix: 20 rows.
- ClaudeCode B entries: 8 main-thinking JSONL rows, 20 reasoning JSONL rows, 4 choice-trap JSONL rows.
- ClaudeCode B production process: completed with return code `0`; B self-check still marks external review and blockers as not closed.

## Confirmed Cross-Line Agreements

- `Q0001 2026顺义一模 Q19(2)`: 科学思维三性，A/B both source-locked to `8d19592...` paper and `de758e...` rubric.
- `Q0002 2025海淀二模 Q20`: B located the formal rubric `fc56fdd...`; A rechecked and upgraded from `A-support` to `A-formal`.
- `Q0003 2026朝阳期中 Q21(2)`: 创新思维复合题，A/B both use `885e694...` rubric and teacher-version material.
- `Q0004 2026通州期末 Q11`: 思维抽象与思维具体选择题，A/B both classify as choice-trap for the thinking handbook.
- `Q0005 2026东城期末 Q17(2)`: A/B both split into 矛盾律、充分条件假言推理、三段论中项不周延 and keep it in the reasoning handbook.

## B-Line Additions Accepted After A Backcheck

- `Q0013 2026顺义一模 Q19(1)`: 三段论/演绎保真两条件.
- `Q0014 2026朝阳期中 Q20`: 辩证思维复合题.
- `Q0015 2026东城期末 Q6`: 三段论补大前提保真.
- `Q0016 2026东城期末 Q7`: 矛盾关系真假判断.
- `Q0017 2026通州期末 Q9`: 数字化治理 vs 创新思维/发散思维误挂边界.
- `Q0018 2026朝阳一模 Q17(1) 前半`: 不完全归纳推理识别.
- `Q0019 2026朝阳一模 Q17(1) 后半`: 联想思维迁移或想象设计.
- `Q0020 2026海淀期末 Q20(1)`: 充分条件假言推理肯定后件错误.
- `Q0021 2026海淀期末 Q20(2)`: 超前思维调查研究、矛盾分析、推理和想象.
- `Q0022 2026海淀一模 Q17(1)`: 划分标准不一与选言判断遗漏.
- `Q0023 2026海淀一模 Q17(2)`: 调研改进题，科学/逻辑/辩证/创新思维任选两个.
- `Q0024 2024朝阳一模 Q6`: 形式逻辑综合选择题.
- `Q0025 2024.11朝阳期中 Q18`: 楚王不完全归纳轻率概括与晏子类比推理.
- `Q0026 2026西城一模 Q19(3)`: 三段论四概念、反对关系、同一律偷换概念.

## B-Line Additions Still Rejected/Pending

- `2024朝阳二模 Q7`: A line has now re-sourced the original paper and answer key as `Q0029`; old B placeholder wording remains rejected, but the source-locked A entry can be reviewed.
- GPT Pro review is still `prepared_not_submitted`.
- Independent Claude review is still running on packet V0 and does not cover Q0018-Q0026 unless re-run with an updated packet.

## A-Line Resolved While B Still Has Placeholder

- `2025顺义一模 Q7`: B choice entry is still old-index placeholder with `待回源核验`; A has now source-locked teacher-version stem and explanation to `9dd43cae...` and classifies it as 三段论谬误名称纠偏: 大项不当扩大 vs 小项不当扩大.
- `2024朝阳二模 Q7`: B choice entry was old-index placeholder; A has now source-locked the paper options and reference answer D to `9223488a...` and `f7c4cc4a...`, classifying A as 三段论小项不当扩大.

## Fusion Rule Going Forward

- B-line rows with full source paths and no blocker can be imported only after A backcheck.
- B-line rows that say `旧索引`, `待回源`, or `blocker` stay out of final handbooks until re-sourced.
- A-line rows are source packets, not final prose; they still need handbook fusion and external review.

## External Review V0 Follow-up

- Independent Claude review V0 returned `EXTERNAL_REVIEW_DONE_NOT_PASS`.
- F1 Critical has been corrected: `Q0011 2024海淀二模 Q17(1)` is no longer treated as a 科学思维单角度题; it is now logged as 科学思维总帽下三模块复合, 科学2分+创新3分+辩证2分.
- F5 has been materially addressed: B-line high-confidence rows named by Claude V0 have been A-line source-locked as Q0018-Q0026.
- F11 has been addressed structurally: `PROMOTION_GATE.md`, `PROMOTION_LOG.md`, `PROMOTION_HOLD.md`, and `BLOCKER_RECONCILIATION.md` now control V1 promotion.
- Remaining V1 holds: choice options have been embedded for Q0004/Q0012/Q0015/Q0016/Q0017/Q0024, the reasoning draft now has a V1 formalization index, and the thinking draft now has a V1 four-block trigger index. Final classroom polishing and V1 real external review are still pending.

## External Review V1 Follow-up

- Independent Claude review V1 returned `EXTERNAL_REVIEW_DONE_NOT_PASS`.
- V1 confirmed real progress on Q0011 route correction, Q0018-Q0026 source-locking, choice-option embedding, and index-level four-block/formalization repair.
- V1 also found the promotion gate was only partly effective: Check 3/4 were index-level rather than body-level, Check 7 was not reflected in status names, and BLK reconciliation state names were ambiguous.
- Immediate patch completed after V1: Q0011 cross-references were added to 辩证思维 and 创新思维 chapters; Q0011 易错边界 was rewritten as a student writing-error list; `PROMOTION_LOG.md` now has gate 1-7 columns and no `promote_to_v1_candidate` state.
- Remaining post-V1 holds: body-level four-block/five-element rewrite, promotion quality rating, coverage-gap ledger, and real GPT Pro review. Q0023 answer sentence, Q0021 超前思维帽说明, and Q0026 甲主链 have been patched once after Claude V1, but still need later review.
