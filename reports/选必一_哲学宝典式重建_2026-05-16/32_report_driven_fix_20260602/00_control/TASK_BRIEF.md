# TASK_BRIEF

## Task

严格按照 Claude 三维审核报告提出的问题，修订选必一《当代国际政治与经济》6.1 最终版。

## User Request

“严格按照这个报告，针对里面提出的问题，去完善改正。”

## Report

- `/Users/wanglifei/Library/Application Support/Claude/local-agent-mode-sessions/2c0a1a14-78ce-4ddc-8f72-9d4f74dbff6e/703c2d6a-ade6-4ee8-94a4-92b2abb47bf1/local_ea19f1a6-c672-4010-9aa6-235ad1631aa4/outputs/选必一宝典_三维审核报告_20260601.md`

## Target Source

- Report object: `/Users/wanglifei/Desktop/选必一6.1最终版_带水印.docx`
- Do not overwrite source. Output a revised copy.

## Required Fix Classes

1. Fix 3 explicit accuracy problems:
   - 2026朝阳期中Q17「科教兴国战略与人才强国战略」挂点/落点错位。
   - 海淀Q21「坚持正确义利观」答案落点缺“正确义利观”。
   - 2026丰台二模Q20 删除臆造“单一窗口”。
2. Rewrite “为什么能想到” entries that merely duplicate “材料触发点”, prioritizing错位阐释。
3. Supplement 16 omitted 2024–2026 选必一主观题, using original papers/rubrics when available.

## Boundaries

- Claude report is a defect list, not a scoring source.
- Added scoring entries must still follow 选必一 source hierarchy: formal rubric/marking rule first.
- Preserve user's 6-bucket / second-level framework and student-facing format.
- Preserve watermark unless a regenerated copy requires re-applying it.
