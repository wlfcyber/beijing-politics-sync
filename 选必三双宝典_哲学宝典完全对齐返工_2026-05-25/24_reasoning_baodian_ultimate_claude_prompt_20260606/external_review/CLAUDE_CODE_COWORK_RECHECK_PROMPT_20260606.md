# Claude Code Cowork Recheck Prompt

You are rechecking a patched Beijing Gaokao politics 推理宝典 after your prior `REVISE` review.

Do not edit files. Review only.

## Files To Inspect

- `delivery/选必三逻辑与思维_推理宝典_终极版_20260606.md`
- `qa/QA_GATES_V24_20260606.json`
- `qa/QA_REPORT_V24_20260606.md`
- `external_review/CLAUDE_CODE_COWORK_REVIEW_RESULT_20260606.md`

## Prior Critical Findings To Verify

1. `2024.11朝阳期中 第18题` under `五、类比推理` previously had a wrong `满分作答示范` about 楚王轻率概括. Verify it now directly answers 晏子类比推理 and remains student-copyable.
2. `2024朝阳一模 第20题第（1）问` previously omitted the type name `充分条件假言推理` from `满分作答示范`. Verify it now includes the type and still reads as a full answer.
3. A new local G11 checks that full-mark answers include reasoning type terms when the question explicitly asks for 推理类型. Verify this gate passed and inspect any listed violations if present.

## Output Format

Return Markdown:

1. `VERDICT`: `ACCEPT`, `REVISE`, or `BLOCK`.
2. `Prior Findings Status`: for each prior finding, `closed` or `still open`, with evidence.
3. `New Critical Findings`: list only blockers that would prevent delivery. Use `None` if none.
4. `Boundary`: state that this is advisory and local source/rubric evidence remains authoritative.
