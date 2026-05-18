# Adaptive Rules Ledger

Self-learning in this project means durable rule capture after a user correction, governor failure, or repeated workflow defect. It never changes evidence hierarchy by itself.

| Date | Trigger | New rule | Validation check | Affected files | Status |
| --- | --- | --- | --- | --- | --- |
| 2026-05-18 | Project governor bootstrap | All workers must pass Layer 1 report, Layer 2 skill/notebook, and Layer 3 run controls before touching project data. | latest report plus worker orders exist before execution | reports/master_governor/*, skills/*/SKILL.md | accepted |
| 2026-05-18 | Context may exceed 1MB | Files above threshold require deterministic context capsules; original remains evidence source. | context_compression_manifest.csv contains oversized files | reports/master_governor/context_capsules/* | accepted |
