# Batch04H ClaudeCode Conflict Resolution - 2026门头沟一模

time: 2026-05-03 23:14 CST
student_doc_touched: no
cross_thread_guard: active

## Inputs Read

- Codex A prelim:
  - `05_coverage/batch04H_mengtougou2026_candidate_questions.csv`
  - `codex_lane/agents/worker/worker_batch04H_mengtougou2026_triage.md`
  - `02_extraction/codex_extraction_logs/batch04H_mengtougou2026_manual_evidence_notes.md`
  - `fusion/scoring_atom_table_batch04H_mengtougou2026_prelim.csv`
  - `fusion/merge_register_batch04H_mengtougou2026_updates.md`
- ClaudeCode B:
  - `claudecode_lane/progress_batch04H.md`
  - `claudecode_lane/batch04H_mengtougou2026_matrix.csv`
  - `claudecode_lane/batch04H_mengtougou2026_entries.md`
  - `claudecode_lane/batch04H_missing_blockers.md`
  - `claudecode_lane/batch04H_conflicts_for_codex.md`
  - `04_suite_reports/claudecode_suite_reports/batch04H_mengtougou2026_suite_report.md`
- Codex A role gates:
  - `codex_lane/agents/patcher/patcher_review_batch04H_mengtougou2026.md`
  - `codex_lane/agents/governor/governor_gate_batch04H_mengtougou2026.md`
  - `codex_lane/agents/decision_maker/decision_batch04H_mengtougou2026.md`

## A/B Status

ClaudeCode B completed and exited. It reported no missing blockers for Q20 and independently confirmed:

- Q20 is P0 candidate-for-fusion.
- Q21 is boundary-only.
- Q16/Q17/Q18(1)/Q18(2)/Q19 are excluded by module.
- The two scoring caps are real: one-sided answers cap at 4; textbook-only answers cap at 5.

## Conflict Decisions

### C1 - Number of Q20 Atoms

ClaudeCode B produced 9 term atoms plus 1 logic skeleton. Codex A produced 5 candidate atoms plus logic handled as an answer-structure guard.

Ruling: keep Codex A's 5 candidate atoms for fusion, but absorb B's subpoint list as expression variants.

Reason: the P0 scoring source has `中国意义2分` and `世界意义2分`, each with four optional material subpoints and two required for full side score. Treating every subpoint as a separate main frequency would over-count one scoring block. Student-facing later should show them as optional material抓手 under the China-side and world-side paragraphs.

### C2 - 两种市场两种资源 Direction Tag

ClaudeCode B correctly flags an apparent cross-question conflict:

- 2025门头沟一模 Q19 world-meaning question: `充分利用两个市场两种资源` explicitly does not score.
- 2026门头沟一模 Q20 China-side meaning: `国内国际两种市场两种资源联动` explicitly scores.

Ruling: accept B's direction-tag fix. The term is positive only when the question asks for China-side economic meaning / open-economy advantage; it must not be moved into a world-meaning paragraph unless the rubric says so.

### C3 - 高水平开放新范例

ClaudeCode B asks whether `高水平开放新范例` should open a new core.

Ruling: no new core. Keep it as a high-information expression variant under `制度型开放 / 高水平对外开放`, with a `示范/范例` subcluster.

### C4 - 开放型世界经济

ClaudeCode B and Codex A agree that `开放型世界经济` must remain a full expression.

Ruling: preserve the full phrase. Do not collapse it into vague `经济全球化正确方向`.

### C5 - Q21 Boundary

ClaudeCode B and Codex A agree Q21 is boundary-only.

Ruling: Q21 may supply expression accumulation for `中国为世界提供确定性`、`互利共赢的开放战略`、`构建人类命运共同体`; it does not become a frequency atom or student required point in this batch.

## Final A/B Ruling Before Role Closure

Batch04H can move to Patcher/Governor A/B closure after the small fusion-note patch for the two-markets direction tag. Student draft, Word/PDF, FINAL_ACCEPTANCE, and coverage close remain blocked.
