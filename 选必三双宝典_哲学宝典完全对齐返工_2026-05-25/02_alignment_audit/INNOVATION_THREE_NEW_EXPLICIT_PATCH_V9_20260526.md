# INNOVATION_THREE_NEW_EXPLICIT_PATCH_V9_20260526

- trigger: V8 fresh-context A4 answer could identify `联想/迁移`、`发散/聚合`、`逆向思维`, but did not explicitly write `思路新、方法新、结果新`.
- status: `PATCH_APPLIED`
- affected_file: `05_candidate_md/选必三_逻辑与思维_思维宝典_哲学完全对齐候选稿.md`

## Problem

V8 local fresh-context answer showed the innovation chapter was usable but not yet fully stable at the “三新总帽子 + 小方法下沉” level. The student simulation wrote the small methods correctly, but omitted explicit `思路新、方法新、结果新`. Since the goal is full philosophy-handbook alignment, this was treated as an actionable expression gap rather than waved through.

## Patch

In the `思路新、方法新、结果新` guide:

- added that innovation compound questions should first use `思路新、方法新、结果新` as the total hat;
- then require `发散`、`聚合`、`联想`、`迁移`、`逆向`、`超前` to be mapped to material actions.

In the `发散思维与聚合思维` guide:

- added that when the prompt asks `如何体现创新思维`, the answer should return to how divergent/convergent thinking produces `思路新`、`方法新` or `结果新`;
- revised the answer template so it explicitly says `体现思路新` and `形成可落实的新方法和新效果`.

## Verification

- Rebuilt DOCX/PDF.
- Thinking PDF page count changed from 34 to 35, confirming the guide patch entered the rendered artifact.
- V9 fresh-context answer A4 now ends with: `形成吸引年轻消费者的新思路、新方法和新结果`.

## Boundary

This is a targeted teaching-transfer patch. It does not change source evidence, question classification, or reasoning-book content.

