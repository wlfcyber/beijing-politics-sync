---
name: feige-politics-garden
description: "Use when the user says 飞哥政治庄园 or asks for Beijing Gaokao politics research and the book/module must be routed. Route 必修四 philosophy/culture work to feige-politics-garden-bixiu4, and 选择性必修一《当代国际政治与经济》 main-question rubric-term work to feige-politics-garden-xuanbiyi. Keep cache-first evidence, scoring-rubric guardrails, and document-rendering requirements."
---

# 飞哥政治庄园

This is the router entrypoint for the user's Beijing Gaokao politics research system. Do not run substantial research from this file directly; choose the correct branch skill first.

If the final artifact is `.docx`, also use the `documents` skill and render every DOCX before delivery.

## Route

Use `C:\Users\Administrator\.codex\skills\feige-politics-garden-bixiu4\SKILL.md` when the task is about:

- 必修四, 哲学, 文化, 哲学与文化.
- Material-to-knowledge trigger chains, principle/method framework placement, choice-question wrong-option patterns, or 必修四 cumulative artifacts.
- The existing long-running 飞哥政治庄园 workflow, governor review, cache-first corpus work, Word deliverables, GitHub sync, or cross-machine continuation for the 必修四 line.

Use `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbiyi\SKILL.md` when the task is about:

- 选择性必修一, 选必一, 当代国际政治与经济, 国政经.
- Main-question scoring rubrics, marking rules, 细则术语 accumulation, 完整设问, 细则位置, 材料触发, 答案句.
- Topics such as 国际竞争, 国际合作, 经济全球化, 世界多极化, 中国外交, 中国与联合国, 南南合作, 全球治理.

If the user asks for a mixed-book task, route each term to its real book/module. Do not force 必修二、选必二、选必三, or 必修四 terms into the 选必一 table.

## Shared Rules

- Use the reusable corpus cache before raw Office/PDF/PPT conversion: `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus`.
- Cache-first is not cache-only. Return to the original Word/PDF/PPT when cached text is missing, confusing, incomplete, or insufficient for evidence.
- Do not invent rubrics, answer keys, scoring rules, or source files.
- Do not treat ordinary reference answers as scoring rubrics unless the user explicitly confirms that file is usable.
- Preserve the user's framework over generic category systems. If a scoring term cannot fit cleanly, record the closest location and why.
- For long-running work, keep source ledgers, progress/control files, and governor decisions aligned before declaring completion.
