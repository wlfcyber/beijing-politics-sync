# GitHub Upload Report - Bixiu4 Spark Nonfinal Archive

Timestamp: 2026-05-26 02:23 +08

Status: `NONFINAL_ARCHIVE_PUSH_PREPARED`

## Boundary

This upload is for viewing and preserving the current Bixiu4 Spark-generated version only.

It is not `STRICT_FINAL_ACCEPTED`, not a qualified `5.5 xhigh` result, and must not be used as final acceptance evidence for the user's original hard gate.

## Reason

The migrated Bixiu4 recovery sub-thread was stopped because recent active token ledgers showed:

- `limit_id`: `codex_bengalfox`
- `limit_name`: `GPT-5.3-Codex-Spark`
- `model_context_window`: `258400`

Required condition from user: `5.5 xhigh`.

## Stop Record

- Initial process group stopped:
  - `codex.exe` PID `23236`
  - `node_repl.exe` PID `37092`
- Rehydrated process group stopped after the session wrote again:
  - `codex.exe` PID `11888`
  - `node_repl.exe` PID `9448`

Authoritative stop marker:

- `reports/bixiu4_thread_recovery_opus47_2026-05-24/STOP_DO_NOT_CONTINUE_SPARK_LINE_20260526.md`

## Upload Scope

Archive commit prepared:

- `2a8e08ee750d28106b042448d16bba8b22ee213a`
- message: `Archive Bixiu4 Spark nonfinal run`

Selected scope:

- 994 files
- about 63.5 MB
- 547 Markdown files
- 215 Python repair/check scripts
- 125 JSON files
- 92 CSV matrices
- 9 TXT files
- 3 DOCX files
- 2 PDF files
- 1 ZIP review packet

Included important viewing artifacts:

- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/05_delivery/哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.docx`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/05_delivery/哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.pdf`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/08_external_review/feige_bixiu4_philosophy_external_review_packet_2026-05-24.zip`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/08_external_review/upload_packet/哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.docx`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/08_external_review/upload_packet/哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.pdf`

Upload manifest:

- `reports/night_supervisor_2026-05-23/upload_filelist_20260526_bixiu4_spark_nonfinal.txt`

## Exclusions

Excluded from the commit:

- raw `.codex/sessions/*.jsonl`
- rendered page image folders
- `word_render_qa_*` image bulk
- `every_page_visual_qa_*` image bulk
- `__pycache__` and `.pyc`
- backup DOCX/PDF files
- obvious scratch logs and bulky intermediate render output

## Secret Scan

Selected text scope scanned:

- text files scanned: 936
- result: `NO_SECRET_PATTERN_MATCHES`

Patterns included common OpenAI, GitHub, Slack, AWS, Google API key, bearer token, and long api_key/secret/password assignment forms.

## Current Quality Boundary

Local visible state at stop:

- P0 had been cleared.
- Batch20 completed; Batch21 appeared; Batch22 inspection had begun but was not accepted under the user model gate.
- Latest queue summary showed 442 queued thin candidates:
  - P1: 210
  - P2: 207
  - P3: 25
- Latest render QA visible:
  - PDF pages: 309
  - rendered PNG count: 309
  - DOCX/PDF label counts: 2891/2891
  - blank-like body pages: 0

Open gates:

- current-version GPTPro full-artifact review pending
- current-version Claude Opus full-artifact review pending
- model gate blocked because the active Codex line was Spark, not `5.5 xhigh`
- not strict final
