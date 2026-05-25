# Promotion Gate

Status: `ACTIVE_FOR_V1_AND_LATER`

This gate is stricter than V0 review drafts. A row may enter a V1 review draft, external-review packet, or final handbook only if all applicable checks pass.

## Gate Checks

1. Source packet: current run has an A-line source packet with evidence level `A-formal` or an explicitly justified non-formal evidence level.
2. Blocker reconciliation: any related B-line blocker is closed or explicitly converted to a promotion hold in `BLOCKER_RECONCILIATION.md`.
3. Thinking template: thinking rows must include material action, why the method is triggered, exam-answer sentence, and mistakes/boundaries.
4. Reasoning template: reasoning rows must include reasoning form, checkable logical structure, validity/fallacy point, and same-family comparison.
5. Choice-question text: choice rows must include the original A/B/C/D option text and a per-option explanation.
6. A/B provenance: rows first surfaced by B line require Codex A backcheck before promotion.
7. External-review status: GPT Pro and Claude review results must be captured as real external outputs, not simulated by Codex or ClaudeCode production.
8. Status-name honesty: when external review is absent or returned `NOT_PASS`, promotion status names must not imply `candidate`, `passed`, `approved`, `final`, `ready`, or `complete`.
9. Quality rating: `PROMOTION_QUALITY_CHECK.md` must rate the row as `pass` before it can leave hold; `partial` or `fail` rows remain blocked even if their table fields are non-empty.

## Enforcement

- Rows that fail a check stay in `PROMOTION_HOLD.md`.
- Review drafts may contain provisional teaching prose, but no row can be promoted while `PROMOTION_LOG.md` records a failed source, blocker, template, option, provenance, or external-review check.
- A source-locked row is not automatically a handbook row.
- After Claude V1 returned `NOT_PASS`, no row is allowed to use `promote_to_v1_candidate`; use `hold_pending_next_external_review` or a narrower non-passing state instead.
- `PROMOTION_QUALITY_CHECK.md` is authoritative for body-quality gating; non-empty fields do not imply quality pass.
