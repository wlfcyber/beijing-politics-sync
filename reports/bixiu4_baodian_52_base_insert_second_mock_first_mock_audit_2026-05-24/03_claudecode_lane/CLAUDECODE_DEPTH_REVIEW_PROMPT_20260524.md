# ClaudeCode Depth Review Prompt 2026-05-24

You are ClaudeCode production lane B for 飞哥政治庄园-必修四哲学宝典.

Task: independently audit and thicken the current 2026-05-24 philosophy handbook patch. This is not a final reviewer-only role. You must work as a parallel production lane and produce row-level improvement proposals that Codex can verify and merge.

## Files To Read

- `04_fusion_audit/student_patch_entries.accepted.jsonl`
- `01_source_inventory/second_mock_candidate_entries.csv`
- `01_source_inventory/suite_source_bundles/*.md`
- `06_governor_confucius/CURRENT_ACCEPTANCE_STATUS_20260524.md`
- `05_delivery/docx_insert_ledger.csv`

## Hard Rules

- Do not invent rubrics, answer keys, scoring rules, or source files.
- Do not add a new principle just because the source says "等角度"; high-risk principles require explicit rubric/scoring-source support.
- Preserve the accepted 5.2 handbook structure. Do not rebuild the handbook. Treat this run as inserting and thickening deltas into the already accepted handbook.
- Student-facing text must follow: 材料触发点 -> 设问 -> 为什么能想到 -> 答案落点.
- The "为什么能想到" field must explain the actual reasoning from material signal to principle/method, not just restate the principle.
- The "答案落点" field must be a natural answer sentence or answer direction a student could write. Do not use audit/meta language like "答案要写出", "不能只罗列", "可从...角度作答", "评分细则要求".
- Keep source paths and audit evidence out of student-facing fields.
- If a row is not evidence-safe, mark it DELETE or NEED_EVIDENCE instead of polishing it.

## Required Output

Write two files:

1. `03_claudecode_lane/claudecode_depth_review_20260524.md`
   - Overall verdict.
   - Row-level table with: row_id, source_suite, question_no, framework_node, verdict (`KEEP`, `REWRITE`, `DELETE`, `NEED_EVIDENCE`), reason.
   - List of any suspicious or too-thin rows.
   - State whether the current 38-row patch can meet the original philosophy handbook quality after your proposed rewrites.

2. `03_claudecode_lane/claudecode_depth_rewrite_proposals_20260524.jsonl`
   - One JSON object per row that should be rewritten.
   - Required keys: `row_id`, `source_suite`, `question_no`, `framework_node`, `material_trigger`, `question_prompt`, `why_trigger`, `answer_landing`, `evidence_basis`, `verdict`.
   - Only include rows with verdict `REWRITE`, `DELETE`, or `NEED_EVIDENCE`.
   - For `REWRITE`, provide the full replacement student-facing fields.
   - For `DELETE` or `NEED_EVIDENCE`, explain why in `evidence_basis`.

Scope: audit all 38 accepted rows, with special attention to 2026二模 entries that look thinner than the original handbook.
