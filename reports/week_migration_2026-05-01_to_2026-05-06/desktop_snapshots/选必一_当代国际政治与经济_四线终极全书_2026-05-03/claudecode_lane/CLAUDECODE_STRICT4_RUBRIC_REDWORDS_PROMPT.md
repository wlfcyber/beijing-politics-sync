# ClaudeCode Production Lane B - Strict Four-Lane Rubric Redword Regate

Run identity:
`/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03`

You are ClaudeCode production lane B for this exact run. Another thread may also be using GPT, Claude, ClaudeCode, Safari, or desktop apps. Do not mix outputs, logs, browser context, or prior-thread conclusions across threads.

## Read First

- `00_control/CROSS_THREAD_TOOL_GUARD.md`
- `MASTER_REQUIREMENTS.md`
- `task_plan.md`
- `progress.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden/SKILL.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-book-orchestrator/SKILL.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/SKILL.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/current-user-requirements.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi/references/xuanbiyi-term-protocol.md`

## Mission

Independently review the latest Codex A patch for all-question rubric red scoring words. The user found that `2026海淀一模 Q20` previously used broad framework accumulation words instead of the actual colored rubric. Codex A claims it has now repaired all 47 main questions by making each question's red `踩分词` come from per-question scoring evidence or exact screenshot override.

You must challenge that claim. Do not edit final Markdown/DOCX/PDF. Produce an independent lane-B review that Codex A can adjudicate.

## Inputs To Inspect

- Student Markdown: `09_delivery/选必一_当代国际政治与经济_完整学生讲义_最终闭环版_20260504.md`
- Final DOCX/PDF for artifact-level sanity:
  - `09_delivery/选必一_当代国际政治与经济_完整学生讲义_最终闭环版_20260504.docx`
  - `09_delivery/选必一_当代国际政治与经济_完整学生讲义_最终闭环版_20260504.pdf`
- Audit matrix: `08_review/role_reviews/all_question_rubric_point_repair_matrix_20260504.csv`
- Repair report: `08_review/role_reviews/rubric_point_global_repair_report_20260504.md`
- Teacher/source index: `09_delivery/选必一_教师核查索引_最终闭环版_20260504.csv`
- Source ledger: `SOURCE_LEDGER.csv`
- Fusion atom table: `fusion/all_scoring_atoms_combined_20260504.csv`

## Required Checks

1. Count check:
   - 47 main questions in the final student Markdown.
   - 47 `本题踩分点汇总`.
   - 197 rubric-point rows in the audit matrix.
   - Each audit-matrix question appears in the final student Markdown.

2. Reverse coverage check:
   - For every audit matrix row, confirm its `red_scoring_terms` appear inside the matching question section.
   - Flag any missing term or question.

3. Source-boundary challenge:
   - Flag rows where `evidence_level`, `source_boundary`, or `scoring_position` suggests ordinary reference answer, guarded source, level answer, or non-point-by-point scoring.
   - Do not automatically reject guarded rows. Explain how the student artifact should label them if they remain.

4. Regression hard samples:
   - `2026海淀一模 Q20`: verify it has three layers, and the first layer includes `扩大制度型开放`, `国内国际两个市场、两种资源`, `畅通双循环`, `新发展格局`, `竞争力`; the second includes `开放、包容、普惠、平衡、共赢`, `国际标准`, `标准共通`, `技术共享`; the third includes `参与全球经济治理和规则制定`, `全球治理体制`, `话语权`, `国际影响力`, `国际经济新秩序`.
   - `2025海淀期中 Q21(2)`: verify `变/不变` layers are not flattened.
   - `2026西城期末 Q20`: verify practice/why/effect layers are visible and boundary points are labeled.
   - `2026通州期末 Q20`: verify no Haidian image scoring-position pollution remains.

5. Student-facing cleanliness:
   - Final student Markdown must not contain paths, debug/audit/model chatter, `评标`, `参考答案`, `评分细则`, `P0_`, `source_`, or similar backend fields as student content.

## Output Files

Write only under `claudecode_lane/` and `06_conflicts/`.

Required files:

- `claudecode_lane/strict4_rubric_redwords_review_20260504.md`
- `claudecode_lane/strict4_rubric_redwords_matrix_20260504.csv`
- `06_conflicts/strict4_rubric_redwords_conflicts_20260504.md`

## Verdict Format

Use one of:

- `PASS_NO_BLOCKER`
- `PASS_WITH_GUARDS`
- `NEEDS_CODEX_FIX`
- `BLOCKED_SOURCE_GAP`

If you find problems, be concrete: give question, audit row or term, source reason, and proposed Codex A action. Do not claim final delivery pass; Codex A and Governor decide after local adjudication.
