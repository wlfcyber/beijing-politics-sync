# 题干待核实 gate 闭环表

Date: 2026-05-24

本表处理 `student_patch_entries.blocked.jsonl` 中 `question_prompt_not_verified` 的 9 条。它们当时被挡出，是因为候选 JSON 仍写着“题干待回源确认”；后续最终 DOCX 已经含有正式设问和学生版条目，所以这些不再作为“未覆盖”缺口。

## 结论

- 2026丰台一模 Q16：4 条均已由最终 DOCX 覆盖。
- 2026房山一模 Q16(2)：4 条均已由最终 DOCX 覆盖。
- 2025门头沟一模 Q16：1 条已由最终 DOCX 覆盖。

## Governor Note

这些条目不应重新插入，否则会造成重复。它们应从 open evidence/prompt gate 中移出，状态记为 `resolved_by_final_docx`。
