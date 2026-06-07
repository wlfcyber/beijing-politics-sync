# Claude Code Cowork Review Prompt

You are the external Claude Code cowork reviewer for a Beijing Gaokao politics handbook. Do not edit files. Review only.

## Local Files To Inspect

- `delivery/选必三逻辑与思维_推理宝典_终极版_20260606.md`
- `delivery/选必三逻辑与思维_推理宝典_终极版_20260606.docx`
- `delivery/选必三逻辑与思维_推理宝典_终极版_20260606.pdf`
- `qa/QA_GATES_V24_20260606.json`
- `qa/QA_REPORT_V24_20260606.md`
- `qa/DEFECT_LEDGER_V24_20260606.csv`
- `FINAL_ACCEPTANCE_REPORT.md`
- `GOVERNOR.md`
- `PROGRESS.md`

## Context

The target product is a student-facing 推理宝典 for 选择性必修三《逻辑与思维》推理部分. It must be simple, efficient, comprehensive, accurate, and grouped by reasoning type. Every included question must keep its source anchor; no hidden deletion or fake source repair is allowed.

Current local QA says:

- 83 entries.
- 8 major reasoning classes.
- 62 subtype sections.
- 6 required fields appear 83 times each: 这道题考什么 / 题目材料 / 设问 / 怎么想到的 / 满分作答示范 / 采分点对照.
- G1-G10 local gates pass.
- Answer-vs-rubric and answer-vs-thinking copy gates pass.
- Banned template openings such as “本题应围绕” and “本题考查” are 0.
- Defect ledger intentionally keeps 2 unresolved source-material items: 2026海淀期末20(1), 2026朝阳二模19(1). Do not demand invention of missing original source material.

## Review Job

Audit the final handbook as a strict external reviewer. Focus on:

1. Coverage and organization: 83 questions present, no obvious duplicated/omitted entries, final body is grouped by reasoning type rather than paper order.
2. Reasoning accuracy: the type label, method summary, “怎么想到的”, full-mark answer, and scoring points are internally consistent for each sampled or inspected question.
3. Full-mark answer layer: must be a candidate answer, not a meta explanation, not a copy of “怎么想到的”, and not a copy of “采分点对照”.
4. Student usability: simple, direct, no AI/template/backend wording, no engineering trace, no empty filler.
5. Source-defect handling: the two unresolved items should be clearly neutral in the student body and recorded in the defect ledger; no fake reconstruction.
6. Fatal issues: source mismatch, wrong reasoning type, missing source anchor, empty field, backend/OCR/page-header residue, broken punctuation, or answer that would not score.

## Output Format

Return Markdown with exactly these sections:

1. `VERDICT`: one of `ACCEPT`, `REVISE`, or `BLOCK`.
2. `Critical Findings`: numbered list. Include entry anchor and exact problem. Use `None` if no critical findings.
3. `Patch Suggestions`: concrete wording or structural changes, each with local verification required.
4. `Sampled Evidence`: list the entries/pages you inspected and what passed or failed.
5. `External Boundary`: state that your review is advisory and local source/rubric evidence remains authoritative.

Do not invent original exam evidence or scoring-rule facts. If a correction depends on the original paper or rubric, mark it as “needs local source verification”.
