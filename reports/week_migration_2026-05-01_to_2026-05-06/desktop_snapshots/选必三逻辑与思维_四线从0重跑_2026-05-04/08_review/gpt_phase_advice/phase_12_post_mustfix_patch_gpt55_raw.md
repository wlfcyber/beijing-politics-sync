# Phase12 Post-MUST_FIX Patch GPT-5.5 Pro User-Pasted Review

Captured: 2026-05-05 CST

Source: user pasted the GPT/external review directly into the current Codex thread.

## Verdict

`PATCH_REQUIRED_BEFORE_EXTERNAL_GATES_NO_WORD_NO_FINAL`

The review says the post-MUST_FIX packet closed most earlier hard issues, including:

- `2024海淀二模17(1)` source-locked as science-thinking only;
- sufficient/necessary conditional forced checks passed;
- `2025丰台期末7` and `2026通州期末9` removed from positive thinking-method nodes;
- manifest correctly marks no Word/PDF/final authorization.

## New Must-Fix

`Q-2025顺义一模-7` still had stale reasoning-index pollution from phase06:

`三段论_小项不当扩大+四概念+中项不周延`

The correct lock is:

- 三段论谬误判断纠错题
- true fallacy: 大项不当扩大
- trap: A 项把大项不当扩大误称为小项不当扩大
- mount: 三段论周延规则 / 大项不当扩大 / 谬误名称纠错

## Additional Clean-Build Boundaries

- `NEEDS_TYPE_CONFIRMATION` and `NEEDS_METHOD_CONFIRMATION` may remain in review-only indexes but cannot enter the student clean index.
- Review-only `Status`, HTML `question_id` comments, `phase12_decision`, `source_pool`, and audit anchors must be stripped before final student-clean build.
- Traceability must be preserved in a separate matrix.

## Merge Policy

After patching `Q-2025顺义一模-7`, the packet may move to visible ClaudeCode 77-row audit and Claude Opus 4.7 Adaptive teaching review. Word/PDF/final remain forbidden.
