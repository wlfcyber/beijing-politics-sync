# ClaudeCode Batch23 Recheck Result - 2025 Chaoyang Final

Parsed from raw stream:

- `OPUS47_CLAUDECODE_BATCH23_2025_CHAOYANG_FINAL_RECHECK_STREAM_RAW_UTF8.jsonl`
- `OPUS47_CLAUDECODE_BATCH23_2025_CHAOYANG_FINAL_RUNTIME_EVIDENCE.json`

## Result

- `content_result`: `pass`
- `local_policy_result`: `pass_with_model_gate_blocked`
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`
- `required_fixes`: see ClaudeCode final response below.

## Evidence Checked

- Matrix target: Batch23 should have `41` rows, `21` body rows, `20` boundary rows.
- Body target: `21` governed DOCX entries for Q2, Q9, Q16, and Q22.
- Render target: `254/254` pages/images, labels `2375/2375`, visible suite headings `21/21`.
- Ledger target: `21` governed records in both `docx_insert_ledger.csv` and `student_patch_entries.accepted.jsonl`.
- Global scope target: remaining raw midterm/final source gap `12` suites.

## Model Evidence Boundary

- Runtime observed models: `claude-api, claude-opus-4-7`.
- Command lane used `--model claude-opus-4-7 --effort max`.
- Stream thinking block/signature seen: `true`.
- Debug model mentions: `claude-haiku-4-5-20251001, claude-opus-4-7`.
- Sonnet/Haiku/model-unknown output is not counted as qualified evidence.
- Machine-readable adaptive/max-effort proof is still insufficient, so the model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

## ClaudeCode Final Response

I'll start by inspecting the working directory and the files mentioned in the task.Let me first verify the model gate context — I'm running on Opus 4.7 per the environment header, but adaptive/max-effort proof is a runtime claim I cannot independently verify. I'll note that explicitly. Now let me read the key Batch23 artifacts.Now let me check the matrix CSV for Batch23 rows and the boundary check.Counts match the claim (Matrix=41, Ledger=21, JSONL=21). Now let me verify body/boundary split in the matrix and check the specific node placements.Matrix body/boundary breakdown is correct (21+20=41), Q16/Q22 node coverage matches spec, Q7 stays in logic boundary. Now let me check the render manifest and ledger.Render counts and node mapping match. Let me check ledger contents and accepted JSONL contents for Batch23.Ledger entries match (21 rows, all Q2/Q9/Q16/Q22 nodes correct). Let me verify the PPT scoring source supports Q16 and Q22 placements.Now let me verify the teacher answer key matches and check the boundary check sections in detail.All Batch23 evidence verified. Teacher answer key `C D B C D A A B A D A C B D A` (line 299) matches spec exactly. Q16 PPT rubric (lines 131–137) and Q22 PPT rubric (lines 329–344) support all claimed philosophy nodes. Now I'll write the result file and return the summary.Recheck complete. Result file written to `OPUS47_CLAUDECODE_BATCH23_2025_CHAOYANG_FINAL_RECHECK_RESULT.md`.

# ClaudeCode Opus 4.7 Recheck Result – Batch23 2025朝阳期末

- `content_result`: **pass**
- `local_policy_result`: **pass_with_model_gate_blocked**
- `model_gate`: **BLOCKED_MODEL_CONFIRMATION_REQUIRED** — runtime header shows `claude-opus-4-7`, but max-effort/adaptive-thinking config cannot be independently proven from inside the session.
- `sonnet_haiku_used`: **no**

## matrix_check
- 41 rows for `2025朝阳期末`: 21 body (Q2, Q9, Q16×10, Q22×9 — all `KEEP_IN_BODY` / `KEEP_IN_BODY_OBJECTIVE_ONLY`) + 20 boundary (`MODULE_BOUNDARY_EXCLUDED_*` / `PHILOSOPHY_BODY_BOUNDARY_EXCLUDED_*`).
- Q2 and Q9 evidence labeled `教师版客观题答案+正确项解析；非主观评分细则` — objective answer-key only, not upgraded to rubric.
- Q16 and Q22 nodes match spec exactly; each cites PPT scoring lines (Q16: 131–137; Q22: 329–344). Teacher answer key `C D B C D A A B A D A C B D A` matches.
- Q7 stays in 选必三 logic/思维 boundary; Q16 culture and Q22 总说 stay in `PHILOSOPHY_BODY_BOUNDARY_EXCLUDED_*`.

## docx_check
- DOCX governed headings = **21**, ledger rows = **21**, accepted JSONL records = **21** — all aligned. Q2/Q9/Q16/Q22 node mapping verified line-by-line.

## render_check
- PDF/PNG pages **254/254**; labels **2375/2375**; word suite headings **21/21**; raw PDF text mentions **0** (expected — text layer not used); blank-like only `page_002.png` (known foreword).

## global_scope_check
- 64 raw suites → 52 covered → **12** midterm/final suites still outside the first/second mock audit scope.

## required_fixes
- None for Batch23 local scope. All counts, placements, citations, and boundary tags are internally consistent.

## remaining_project_blockers
- Model gate blocked (Opus 4.7 adaptive/max-effort proof not derivable).
- GPTPro web and external Claude Opus full-artifact review: `real_call_pending`.
- 12 raw midterm/final suites outside coverage; whole-project status remains non-final — no `STRICT_FINAL_ACCEPTED` claim.
