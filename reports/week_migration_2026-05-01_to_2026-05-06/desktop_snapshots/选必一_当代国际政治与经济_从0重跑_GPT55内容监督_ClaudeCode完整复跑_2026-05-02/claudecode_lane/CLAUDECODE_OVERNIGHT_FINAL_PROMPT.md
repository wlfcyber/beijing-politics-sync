# ClaudeCode Overnight Final Prompt

You are ClaudeCode running the independent production lane for 选必一《当代国际政治与经济》主观题 from-zero rerun.

Run folder:

`/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_从0重跑_GPT55内容监督_ClaudeCode完整复跑_2026-05-02`

Your write scope:

- `claudecode_lane/`
- `claudecode_lane/claudecode_suite_reports_phase02/`
- Do not edit `codex_lane/`, `03_entries/`, `04_suite_reports/codex_suite_reports/`, old run folders, or old final artifacts.

The user authorized Claude to direct ClaudeCode overnight, but Codex remains local evidence judge and final artifact owner. Your job is to finish a complete independent candidate version and comparison report. Do not stop after Phase 02.

## Read First

Read these compact files only:

1. `MASTER_REQUIREMENTS.md`
2. `task_plan.md`
3. `00_control/GOVERNOR_GATES.md`
4. `08_review/claude_commander/claude_overnight_commander.md`
5. `06_conflicts/conflict_register.md`
6. `03_entries/suite_question_matrix.csv`
7. `03_entries/xuanbiyi_subjective_index.csv`
8. `04_suite_reports/codex_suite_reports/2026西城期末.md`
9. `04_suite_reports/codex_suite_reports/2025海淀期中.md`
10. `04_suite_reports/codex_suite_reports/2024东城一模.md`
11. `04_suite_reports/codex_suite_reports/2025海淀期末.md`
12. Your own `claudecode_lane/claudecode_entries_phase02.jsonl`
13. Your own `claudecode_lane/claudecode_conflicts_suspected.md`
14. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/current-user-requirements.md`
15. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/xuanbiyi-term-protocol.md`

Do not read `.claude` project memory for this task. It is stale on 2026西城期末 Q20 because Codex later found a missing-paper supplement and visually read the scanned scoring PDF.

## Updated Codex Facts You Must Reconcile

These facts are current as of 2026-05-03 after your Phase 02 stopped:

- 2026西城期末 Q20 is no longer a hard blocker for Codex. Desktop primary `试卷/` is empty, but `/Users/wanglifei/GaokaoPolitics/2026各区模拟题/2026各区期末和期中/2026西城期末/2026北京西城高三（上）期末政治（教师版）.pdf` provides the full prompt on page 8. Primary `细则.pdf` pages 4-5 were visually read and contain the Q20 scoring structure. You must update your blocker and comparison files accordingly. If you cannot independently verify images, write `needs_codex_visual_ack` but do not keep the old “unconfirmed question text” blocker as final.
- 2025海淀期中 Q16(2)/Q21(2) is P0 for Codex because `细则.docx` contains embedded scoring images: `02_extraction/codex_extraction_logs/2025海淀期中/docx_media/image2.png` and `image8.png`. Acknowledge this conflict. If you cannot OCR the images yourself, mark `codex_visual_evidence_acknowledged`, not `reference_answer_only`.
- 2025海淀期末 Q22 remains a source anomaly watch item: `细则.pptx` slides 61-62 align to Q22 and list 选必一 terms, but the deck header is odd. Treat as P2 or `source_checked_with_header_anomaly`.
- 2024东城一模 Q16/Q20 is source checked by Codex from `细则.pptx` slides 26 and 64 plus rendered paper pages. Treat as included, with boundary caution on `推进高水平对外开放`.
- Student-facing draft must not contain local paths, source ids, status words, audit terms, model chatter, `采分点`, `要落到`, `设问要求`, `细则要求`, `本题需要`, `材料中`, or `v7`.

## Required Work

1. Update `claudecode_lane/claudecode_blockers_phase02.md` with a top addendum: which prior blockers are resolved by Codex and which remain real.
2. Update `claudecode_lane/claudecode_conflicts_suspected.md` with a top addendum:
   - 2026西城期末 Q20 old blocker is superseded by Codex missing-paper supplement and visual scoring read.
   - 2025海淀期中 P1 classification is superseded by Codex embedded-image evidence unless you can disprove it.
   - Any remaining differences on 2025海淀期末 and 2024东城一模 are evidence-level caution, not exclusion.
3. Produce `claudecode_lane/claudecode_student_draft_phase03.md` in six buckets:
   - 时代背景
   - 理论
   - 经济全球化
   - 政治多极化
   - 中国
   - 联合国
4. Draft entries must use the xuanbiyi unit format:

```markdown
**术语：<rubric original phrase(s)>**（出现N次）

- 完整设问：<full question prompt>
- 细则位置：<suite + question + scoring point + score/evidence level>
- 来源：<year district exam + question>
- 材料触发：<why this question/material relation triggers this term>
- 答案句：<candidate answer-sheet sentence>
```

5. Include all closed P0 entries from your Phase 02 and Codex-confirmed hard samples. Include P2 entries only with evidence caution inside `细则位置`. Include 2026西城 Q20 as Codex visually checked if you cannot independently verify images.
6. Continue a high-priority Phase 3 sweep if time remains before final draft:
   - 2026朝阳一模 Q20
   - 2026顺义一模 Q20
   - 2025海淀二模 Q21
   - 2026海淀一模 Q20
   - 2025朝阳一模 scoring summaries
   - 2025丰台二模 分题细则
   - 2024朝阳期中 评标
   - 2024西城一模 阅卷细则调整
   Use only short structured extraction snippets. Never load large PDFs or PPTX files as a single payload.
7. Produce `claudecode_lane/claudecode_phase03_completion_report.md` with:
   - Processed suite count.
   - Entries by evidence level.
   - Remaining blockers.
   - Differences from Codex.
   - Whether the draft is ready for Codex fusion.
   - Any G11 trigger objects produced.

## Runtime Rules

- No `--max-budget-usd` cap.
- Avoid the previous 413: never read huge logs or binaries into context.
- If you hit a missing source or OCR barrier, write it to blockers and continue other suites.
- Do not ask for confirmation unless a source-boundary issue would make the artifact factually unsafe.
- Keep working until the candidate draft and completion report exist.
