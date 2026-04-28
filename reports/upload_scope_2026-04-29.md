# 2026-04-29 GitHub Upload Scope

This sync round preserves the portable project state produced during the 2026-04-28 to 2026-04-29 reruns.

## Included

- New untracked report trees already created inside this repository:
  `reports/culture_all_suites_rerun_2026-04-29/`,
  `reports/final_56_ocr_repaired_claudecode_2026-04-29/`,
  `reports/final_56_v8_decode_claudecode_2026-04-29/`,
  `reports/final_56_v8_decode_rebuilt_2026-04-29/`,
  `reports/full_55_independent_rerun_2026-04-29/`,
  `reports/full_all_suites_independent_rerun_2026-04-29/`,
  `reports/ocr_rerun_claudecode_2026-04-28/`,
  `reports/ocr_rerun_windows_2026-04-28/`.
- New workflow/code files:
  `scripts/build_culture_56_outputs.py`,
  `scripts/init_culture_56_run.py`,
  `cloudcode/s001_windows_package/`.
- Desktop culture deliverables mirrored into
  `artifacts/desktop_exports_2026-04-29/4.29文化线56套重跑结果/`,
  including the final Word files, merged Markdown/CSV outputs, audit report, process logs, and render QA PNG pages.

## Excluded

- User home private state such as `.claude`, `.codex`, browser profiles, shell/session snapshots, and local caches.
- Raw source binaries outside the project mirror boundary.
- System/application state unrelated to the Beijing politics workspace.

## Safety Notes

- This is a portable project-output sync, not a full-machine backup.
- A text-pattern secret scan should remain clean before staging/push.
- The sync target is the existing `wlfcyber/beijing-politics-sync` repository on `origin/main`.
