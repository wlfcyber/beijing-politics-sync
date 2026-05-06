# Batch04F ClaudeCode Conflict Resolution

time: 2026-05-03 22:31 CST
student_doc_touched: no

## Inputs

- Codex A prelim files:
  - `fusion/scoring_atom_table_batch04F_fengtai_prelim.csv`
  - `fusion/merge_register_batch04F_fengtai_updates.md`
- ClaudeCode B files:
  - `claudecode_lane/progress_batch04F.md`
  - `claudecode_lane/batch04F_fengtai_matrix.csv`
  - `claudecode_lane/batch04F_fengtai_entries.md`
  - `claudecode_lane/batch04F_conflicts_for_codex.md`
  - `04_suite_reports/claudecode_suite_reports/batch04F_fengtai_suite_report.md`

## Evidence Conflict

No evidence conflict.

Both lanes agree:

- Q20 has P0 formal marking evidence from `20题.docx`.
- Q20 paper prompt is confirmed by `试卷.pdf`.
- Q18 is《经济与社会》and excluded.
- Q19(2) is《法律与生活》and excluded.
- Q21 is comprehensive/level-scored and not promoted as Xuanbiyi frequency.

## Merge / Bucket Decisions

### FT01

Decision: accept B recommendation.

FT01 is not a new core. It merges with the existing China identity / global-governance role family and adds the scenario variant:

`最大发展中国家身份 -> 参与全球治理 -> 推动全球南方现代化`

### FT02

Decision: accept B recommendation and patch Codex A prelim.

Codex A initially put FT02 in the `联合国` bucket, but B correctly noted this is a broader China-role point:

`中国积极参与国际组织 -> 全球治理体系的重要参与者、贡献者和改革者`

It is now bucketed as `中国`.

Reason: prior merge rules already warn that `国际组织` is not automatically `联合国`; the dedicated UN permanent-member point is FT03.

### FT03

Decision: accept B recommendation.

FT03 remains in the `联合国` bucket and preserves the full scoring chain:

`联合国常任理事国 + 《联合国宪章》宗旨原则 + 践行多边主义 + 维护多边体制的权威性和有效性`

### FT04

Decision: accept B recommendation and patch Codex A prelim.

Codex A initially put FT04 in the `中国` bucket. It is now placed in `政治多极化`, with a China/HMC cross-reference.

Reason: the scoring function of this angle is the global governance direction:

`平等、开放、合作、共享 -> 全球治理体制向更加公正合理方向发展`

`推动构建人类命运共同体` must remain visible, but it should not swallow the international-order / governance-direction function.

## Next Gate

Send Batch04F patched prelim to Patcher and Governor. Student draft, Word/PDF, final, and coverage close remain blocked.

## Patcher Fix Notes

Patcher returned `PASS_WITH_FIXES` and required two narrow downstream guards:

1. `2025丰台二模 Q21` must be carried as `boundary_only/exhaustion-only`; do not inherit ClaudeCode B's simpler `no_xuanbiyi` wording if that makes the boundary row disappear from exhaustion accounting.
2. FT04 must use `共商共建共享的全球治理观` if naming the global-governance view. Do not inherit ClaudeCode B's raw `共建共商共享` word order.

Codex A applied both guards in the merge register and prelim fusion boundary note. Student docs remain untouched.
