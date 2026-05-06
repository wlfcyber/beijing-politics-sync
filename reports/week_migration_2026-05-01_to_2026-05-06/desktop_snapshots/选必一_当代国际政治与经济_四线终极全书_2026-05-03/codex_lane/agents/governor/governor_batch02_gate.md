# Codex A Governor Gate - Worker Batch 02

- Role: Governor / 条目级门禁
- Scope: 2026朝阳一模 Q20、2026顺义一模 Q20、2025海淀二模 Q21、2025海淀期末 Q22
- Inputs read: `MASTER_REQUIREMENTS.md`; `feige-politics-garden-xuanbiyi` current requirements and term protocol; `codex_lane/agents/worker/worker_batch02_entries.md`; `codex_lane/agents/worker/worker_batch02_source_notes.csv`; `SOURCE_LEDGER.csv`; `COVERAGE_MATRIX.csv`; `fusion/merge_register_batch01.md`; `08_review/gpt_phase_fallback_log.md`
- Conclusion: `PASS_WITH_FIXES`

## Gate Decision

Batch02 worker entries may enter `fusion atoms / merge register` update, but only as evidence-labeled fusion candidates. They must not be treated as student final content or as coverage closure.

`section_batch_draft_for_external_review` is conditionally allowed after the fixes below are applied in the draft layer: it must be marked as draft / external review material, preserve teacher-audit evidence labels outside the student-facing prose, and must not imply Claude Opus review is complete.

## Required Fixes Before Fusion / Draft

1. In fusion atoms, normalize the internal heading `术语原词` to the required `术语` field or an equivalent atom field. The worker draft has 22 entries and all entries include `完整设问 / 细则位置 / 来源 / 材料触发 / 答案句 / 证据状态`, but the required student-facing unit must not keep a divergent field name.
2. In `SOURCE_LEDGER.csv`, the Batch02 海淀 rows still have potentially misleading `source_type=P0_candidate_scoring` while `evidence_level` is conservative. Fusion must use `evidence_level` as the controlling field:
   - 2025海淀期末 Q22: keep `P2_teaching_lecture_with_q22_rubric`; do not count as P0.
   - 2025海淀二模 Q21: keep `P1_structured_scoring_answer + P0_marking_record_support`; do not convert to pure P0 formal scoring.
3. Clean material-trigger wording before any section draft: `要求先说明` and `材料二先写` are close to the current protocol's forbidden backstage style. They do not contaminate the answer sentences, but external-review draft prose should rewrite them as question-driven trigger logic.
4. Do not use 2025海淀期末 Q22 as a mandatory or frequency-closed core. It is a P2 teacher-training PPT with optional 选必一 knowledge, and the ordinary paper/reference answer remains support only.
5. For 2026顺义一模 Q20, `经济全球化方向：普惠、平衡、共赢（典范）` must merge under the full higher-information core `推动经济全球化朝着更加开放、包容、普惠、平衡、共赢的方向发展`, supplied in 2026朝阳一模 Q20. The shortened 顺义 wording may only be a variant / 表述积累.
6. For 2026朝阳一模 Q20, `坚持共商共建共享` is recorded in an开放合作 / 发展潜力语境. Do not silently merge it into `共商共建共享的全球治理观` unless a later source explicitly marks that governance-view function.

## Special Checks

| Check | Result | Governor Note |
|---|---|---|
| 普通参考答案冒充细则 | PASS | Source notes explicitly use paper/reference material only for题面、触发、答案句事实；2025海淀期末 paragraph222 is marked not scoring. |
| P2 海淀期末 | PASS_WITH_GUARD | Worker correctly keeps P2 and says not P0; ledger `source_type` wording remains a downstream risk, so fusion must not count it as P0. |
| 2025海淀二模 Q21 P1+P0支撑 | PASS_WITH_GUARD | Worker repeatedly labels `P1 scoring-structured answer with P0 marking-record support；不标为纯 P0 正式细则`; this label must survive fusion. |
| 经济全球化开放、包容、普惠、平衡、共赢完整性 | PASS_WITH_FIXES | 2026朝阳一模 Q20 has the full five-direction phrase; 2026顺义一模 Q20 has only `普惠、平衡、共赢` and must be merged as variant, not promoted as shortened core. |
| 未捕获 Claude | PASS_WITH_GUARD | `gpt_phase_fallback_log.md` says Claude Opus teaching-text advice remains uncaptured. Local fusion work may continue, but student final / Word / PDF remain blocked. |
| 学生稿禁入词 | PASS_WITH_FIXES | 答案句未发现 `采分点 / 要落到 / 细则要求 / 证据层级 / v7 / 材料中` 等后台话；材料触发中两处“先说明/先写”须在外审草稿前改写。 |
| Coverage 闭合 | BLOCKED | `COVERAGE_MATRIX.csv` still shows Batch02 `not_promoted / pending_batch02_gate`; this gate only允许进入融合候选，不允许 coverage closed。 |

## Allowed Next Actions

- Generate / update Batch02 fusion atoms.
- Update Batch02 merge-register decisions with evidence labels preserved.
- Prepare `section_batch_draft_for_external_review` only after the required wording and evidence-label fixes above.

## Still Forbidden

- Do not generate student final Markdown / Word / PDF.
- Do not mark coverage closed or write final acceptance.
- Do not promote P2 海淀期末 Q22 into P0, mandatory point, or closed frequency.
- Do not promote 2025海淀二模 Q21 into pure P0 formal scoring.
- Do not use ordinary reference answers as `细则位置`.
- Do not claim Claude Opus teaching-text review has been captured.
- Do not merge shortened or loose wording into high-level cores without preserving source-specific variants and non-merge guards.
