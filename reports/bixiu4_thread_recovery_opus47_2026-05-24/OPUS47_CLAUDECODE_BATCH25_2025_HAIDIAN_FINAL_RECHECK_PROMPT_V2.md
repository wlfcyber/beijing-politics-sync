# Opus 4.7 ClaudeCode Recheck V2 - Batch25 2025 Haidian Final

You are the ClaudeCode production lane for 必修四政治庄园 recovery. This is a constrained recheck after the previous stream stopped before a final conclusion.

Hard rules:
- Do not use Sonnet, Haiku, or model-unknown output as qualified evidence.
- Do not claim final whole-project acceptance.
- Do not treat ordinary reference answers as scoring rubrics.
- Objective-choice evidence is objective-only unless scoring/detail source supports a subjective principle.
- GPTPro web and external Claude Opus full artifact review remain `real_call_pending`.
- If model/max-effort/adaptive proof is not machine-confirmable, keep `model_gate: BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

Tool boundary:
- Use only Read/Grep if needed.
- Do not use Bash, PowerShell, Write, Edit, TodoWrite, or web tools.
- Do not modify files.

Files to inspect if needed:
- `BATCH25_2025_HAIDIAN_FINAL_SOURCE_TRANSCRIPTION_20260525.md`
- `COVERAGE_FUSION_BATCH25_2025_HAIDIAN_FINAL_CODEX_20260525.md`
- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`
- `word_render_qa_20260525_batch25_word/render_manifest.json`
- `FORMAT_RENDER_QA_20260524.md`
- `GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv`
- `MODEL_EVIDENCE_LEDGER.md`

Local deterministic evidence already gathered by Codex:
- Batch: `2025海淀期末`.
- Matrix rows: `46`.
- Matrix body rows: `28`.
- Matrix boundary rows: `18`.
- Matrix `NEED_EVIDENCE` rows for this suite: `0`.
- Body question set: `Q4,Q5,Q6,Q7,Q16,Q17(2),Q22`.
- Ledger records in `docx_insert_ledger.csv`: `28`.
- Accepted JSONL records in `student_patch_entries.accepted.jsonl`: `28`.
- Render manifest: `pages=257`, `rendered_png=257`.
- Render blank pages: `[2]`; blank pages excluding cover/foreword: `[]`.
- DOCX/PDF label count: `2407/2407`.
- DOCX suite mentions: `28`.
- Word-layout visible suite headings: `28`.
- Raw PDF exact suite text mentions: `0` because Word text extraction splits/encodes Chinese in this export; visual/Word-layout heading scan is the counted render check.
- Global audit row status for `2025海淀期末`: `covered_by_batch25_recovery_matrix`.
- Global remaining missing midterm/final raw source suites: `10`.

Placement points to verify:
- Q4/Q5/Q6/Q7 objective entries are allowed only as objective-choice exemplars.
- Q16 uses PPT scoring/detail support for 联系、矛盾、发展/辩证否定、人民立场、规律与能动性.
- Q17(1) and Q18 are 选必三 boundaries; Q17(2) has 必修四 philosophy support.
- Q19-Q21 are 法律与生活 boundaries.
- Q22 comprehensive essay can support 必修四 philosophy points: 量变质变、人民主体、主观能动性、价值观; non-philosophy points remain boundary.

Required final output:

Return a short Markdown result containing these exact fields:

- `content_result`: one of `pass`, `pass_with_notes`, `fail`, `blocked`
- `local_policy_result`: one of `pass_with_model_gate_blocked`, `fail`, `blocked`
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`
- `checked_counts`: matrix/body/boundary/ledger/accepted/render/global_missing
- `required_fixes`: empty list if none, otherwise concrete fixes
- `non_final_boundary`: one sentence confirming this is not whole-project final acceptance

If you cannot complete the recheck with Read/Grep only, output `content_result: blocked` and state the concrete blocker.
