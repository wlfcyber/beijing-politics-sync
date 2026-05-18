# Adaptive Rules Ledger

Self-learning in this project means durable rule capture after a user correction, governor failure, or repeated workflow defect. It never changes evidence hierarchy by itself.

| Date | Trigger | New rule | Validation check | Affected files | Status |
| --- | --- | --- | --- | --- | --- |
| 2026-05-18 | Project governor bootstrap | All workers must pass Layer 1 report, Layer 2 skill/notebook, and Layer 3 run controls before touching project data. | latest report plus worker orders exist before execution | reports/master_governor/*, skills/*/SKILL.md | accepted |
| 2026-05-18 | Context may exceed 1MB | Files above threshold require deterministic context capsules; original remains evidence source. | context_compression_manifest.csv contains oversized files | reports/master_governor/context_capsules/* | accepted |
| 2026-05-18 | Xuanbiyi rebuild exposed workflow defects | Future xuanbier/xuanbisan production must use source packets, evidence ledgers, real model capture, ClaudeCode model hard lock, anti-merge checks, final-claim audits, and GitHub verification before delivery claims. | `CROSS_BOOK_WORKFLOW_V3_FOR_XUANBIER_XUANBISAN.md` is loaded by both book skills and verified in final audits | reports/master_governor/CROSS_BOOK_WORKFLOW_V3_FOR_XUANBIER_XUANBISAN.md, skills/feige-politics-garden-xuanbier/SKILL.md, skills/feige-politics-garden-xuanbisan/SKILL.md | accepted |
