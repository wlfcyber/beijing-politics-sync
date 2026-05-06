# Phase12 Post-Patch Addendum: Q-2025顺义一模第7题

Status: `PATCH_APPLIED_BEFORE_EXTERNAL_GATES_NO_WORD_NO_FINAL`

## Problem

The post-MUST_FIX rebuilt reasoning index still inherited a stale fallback label for `Q-2025顺义一模-7`:

`三段论_小项不当扩大+四概念+中项不周延`

This conflicted with the body, which correctly states:

- Correct answer: A.
- True fallacy: 大项不当扩大.
- Trap: A 项把大项不当扩大误称为小项不当扩大.

## Patch Applied

Updated generation script:

- `02_extraction/phase12_rebuild_locked_indexes_after_must_fix.py`

Regenerated:

- `09_student_draft/phase12_reasoning_typology_index_REBUILT.md`
- `09_student_draft/phase12_reasoning_typology_index.md`
- `05_coverage/phase12_locked_index_mounts.csv`
- `08_review/phase12_reasoning_index_rebuild_audit.csv`
- `08_review/phase12_post_patch_index_audit.md`

## New Locked Mount

`Q-2025顺义一模-7` now mounts as:

- `三段论结构题`
- `三段论周延规则 / 大项不当扩大 / 谬误名称纠错`

Its source basis is:

- `真实错误=大项不当扩大`
- `小项不当扩大仅为A项错误命名陷阱`
- `A项误称小项不当扩大`

## New Forced Check

`Q-2025顺义一模-7, major_term_expansion_not_positive_small_term, PASS`

## Scans

- `Q-2025顺义一模-7` no longer has `phase06_logical_form_locked` in the rebuilt index or locked mount CSV.
- `Q-2024朝阳二模-7` has no same-line `中项不周延` reflow in the rebuilt index or locked mount CSV.
- Exact `B=①④` / `B＝①④` does not appear in the current review packet files.
- `NEEDS_TYPE_CONFIRMATION`, `NEEDS_METHOD_CONFIRMATION`, `REVIEW_ONLY`, and HTML qid anchors remain only in review-only materials; no final clean candidate has been created.

## Boundary

This patch allows moving to visible ClaudeCode / Opus external audits. It does not authorize Word, PDF, final PASS, `终稿`, `最终稿`, or `宝典成品`.
