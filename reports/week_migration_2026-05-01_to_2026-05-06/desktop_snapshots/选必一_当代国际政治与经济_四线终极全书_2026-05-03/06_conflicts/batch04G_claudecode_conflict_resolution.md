# Batch04G ClaudeCode Conflict Resolution

time: 2026-05-03 23:04 CST
student_doc_touched: no

## Inputs

- Codex A:
  - `05_coverage/batch04G_mengtougou_candidate_questions.csv`
  - `codex_lane/agents/worker/worker_batch04G_mengtougou_triage.md`
  - `02_extraction/codex_extraction_logs/batch04G_mengtougou_manual_evidence_notes.md`
  - `fusion/scoring_atom_table_batch04G_mengtougou_prelim.csv`
  - `fusion/merge_register_batch04G_mengtougou_updates.md`
  - `codex_lane/agents/patcher/patcher_review_batch04G_mengtougou.md`
  - `codex_lane/agents/governor/governor_gate_batch04G_mengtougou.md`
- ClaudeCode B:
  - `claudecode_lane/progress_batch04G.md`
  - `claudecode_lane/batch04G_mengtougou_matrix.csv`
  - `claudecode_lane/batch04G_mengtougou_entries.md`
  - `claudecode_lane/batch04G_missing_blockers.md`
  - `claudecode_lane/batch04G_conflicts_for_codex.md`
  - `04_suite_reports/claudecode_suite_reports/batch04G_mengtougou_suite_report.md`

## Evidence Conflict

No hard evidence conflict.

Both lanes agree:

- Q19 is the only in-scope Xuanbiyi subjective question in `2025门头沟一模`.
- P0 scoring authority is `细则.doc`.
- `试卷.pdf` only supports prompt/material/reference answer.
- Q16/Q17/Q18/Q20/Q21 are excluded or no_xuanbiyi by module boundary.
- Q19 has four 2-point angles with 1+1 internal structure.

## Merge Decisions

### MERGE-MTG-01

Decision: accept B recommendation.

`推动经济全球化朝着更加开放、包容、普惠、平衡、共赢的方向发展` is not a new core. It merges with the existing economic-globalization correct-direction core.

Batch04G adds the scenario:

`中国市场成为世界市场 -> 释放超大规模市场红利 -> 与各国共享发展机遇 -> 推动经济全球化正确方向`

Boundary: `充分利用两个市场两种资源` explicitly does not score here.

### MERGE-MTG-02

Decision: accept B recommendation.

`推动构建人类命运共同体` remains an existing China/HMC core. Batch04G adds the scenario:

`提供国际公共产品 / 贡献中国智慧中国方案 -> 维护世界和平、促进共同发展 -> 推动构建人类命运共同体`

Do not split MTG03 into multiple frequency atoms; it is one 1+1 scoring angle.

### MERGE-MTG-03

Decision: accept B recommendation.

`推动国际秩序/全球治理体系向着更加公正合理方向发展` merges with Batch04F FT04's fairer global-governance direction family.

Batch04G adds `国际秩序` wording to the expression pool; Batch04F wording used `全球治理体制`.

### MERGE-MTG-04

Decision: partial merge with existing global-initiative/civilization-value expression; preserve as a visible scoring subpoint in MTG04.

Search found existing related atom:

- `ATOM-DC04`: `全球文明倡议；以文明增互信；文明交流互鉴；相互理解与信任；平等包容的文明观；全人类共同价值`

Batch04G's `倡导文明平等互鉴，弘扬全人类共同价值` is same expression family, but this question makes it a distinct 1-point subpoint inside the value-system angle. Therefore:

- Do not create a new isolated core.
- Do preserve it visibly in MTG04.
- Do not let `国际秩序更加公正合理` swallow the civilization-value subpoint.

## Boundary Decisions

The following warnings must be inherited downstream:

- `充分利用两个市场两种资源` does not score in MTG01.
- Only China-side significance does not score.
- `国家关系民主化`、`世界多极化`、`多边主义` bare phrases do not score in MTG04.

## Gate Status

Codex A local Patcher: `PASS`.
Codex A local Governor: `PASS`.
ClaudeCode B: complete, no source blockers, no evidence conflicts.

Allowed next step: mark Batch04G Q19 as `candidate_with_fixes` after narrow recheck/sync. Student draft, Word/PDF, final, FINAL_ACCEPTANCE, and coverage close remain blocked.
