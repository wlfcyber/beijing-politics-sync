# Supervisor Patch 03: P2G040 Q16 boundary repair

Time: 2026-05-07 17:42 +08:00

P2G040 structurally passed QA, but one row was semantically inconsistent:

- `Q-2025丰台期末-16`
- `辩证思维>质量互变（适度原则）`
- decision `block_from_student_body`
- can_enter_fusion `yes`

Because the row is philosophy/boundary material and the source note allows
fusion-only attach for quality-change content, the correct decision is
`downgrade_to_index` with `can_enter_fusion=yes`.

Supervisor action: repair the CSV/JSONL/evidence/acceptance wording and rerun
QA before merge.
