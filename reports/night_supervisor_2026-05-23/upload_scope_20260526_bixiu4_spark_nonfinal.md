# Upload Scope - Bixiu4 Spark Nonfinal Archive

Timestamp: 2026-05-26 02:13 +08

Status: `NONFINAL_ARCHIVE_SCOPE`

## Reason

The user stopped the migrated Bixiu4 recovery sub-thread because it was running under `GPT-5.3-Codex-Spark`, not the requested `5.5 xhigh`.

This upload is therefore an archive and handoff snapshot only. It is not a strict final delivery and must not be described as `STRICT_FINAL_ACCEPTED`.

## Included Scope

Selected files from:

- `reports/bixiu4_thread_recovery_opus47_2026-05-24/`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/`
- `reports/night_supervisor_2026-05-23/`

Included file classes:

- Markdown status, Governor, Confucius, model-ledger, audit, and patch reports.
- Coverage, placement, thickness, and evidence CSV/JSON matrices.
- Repair scripts used to generate auditable local changes.
- Current non-backup delivery DOCX/PDF.
- External-review packet zip already present under the Bixiu4 audit directory.
- Stop order and supervisor snapshot documenting the model mismatch.

Approximate selected upload size before staging: about `70-75 MB`, excluding the bulk render page images.

## Excluded Scope

Excluded intentionally:

- raw `.codex/sessions/*.jsonl` files;
- rendered page PNG/JPG bulk folders;
- `every_page_visual_qa_*` page/contact-sheet image bulk;
- `word_render_qa_*` page render folders except text manifests already selected by class where applicable;
- `__pycache__` and `.pyc`;
- backup DOCX/PDF/CSV/JSON/MD files where the current non-backup file exists;
- temporary logs and scratch files.

## Secret Scan

Sensitive-pattern scan must run before commit/push. The upload report may record `NO_SECRET_PATTERN_MATCHES` only if no high-risk token/key/password patterns are found in the selected text scope.
