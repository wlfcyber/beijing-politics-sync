# Week Migration 2026-05-01 to 2026-05-06

This package snapshots Beijing Gaokao politics artifacts created or modified from 2026-05-01 through 2026-05-06 across desktop threads.

Included: control files, student/output documents, Markdown/CSV/JSON ledgers, scripts, external model prompts/reviews, final and candidate DOCX/PDF files, and lightweight image assets needed by student artifacts.

Excluded from normal Git: raw source PDFs, OCR/text/render caches, screenshot/render folders, process logs/locks, Python bytecode, external model stream/runtime traces, and files over 25 MB. See `excluded_manifest.csv` for exact paths and reasons.

Account/secret-like strings found in migratable text files were redacted. See `redaction_manifest.csv` for affected paths.

Included files: 2945
Included size MB: 278.4
Excluded files: 1449
Excluded size MB: 881.2
Redacted files: 4

## Included Top-Level Sources
- `08_review`: 1 files, 0.0 MB
- `reports`: 2 files, 0.0 MB
- `tools`: 1 files, 0.0 MB
- `哲学宝典5.2原地修订`: 43 files, 7.2 MB
- `必修四从0重跑_ClaudeCode_2026-05-02`: 189 files, 3.4 MB
- `必修四学生可读融合版_2026-05-02`: 16 files, 3.2 MB
- `必修四最终整合_2026-05-02`: 14 files, 1.5 MB
- `必修四框架重做_2026-04-29`: 1 files, 0.0 MB
- `必修四终极融合版_2026-05-02`: 118 files, 58.2 MB
- `选必一_四线终极版_五题样例_2026-05-03`: 33 files, 0.2 MB
- `选必一_当代国际政治与经济_从0重跑_GPT55内容监督_ClaudeCode完整复跑_2026-05-02`: 159 files, 2.1 MB
- `选必一_当代国际政治与经济_从0重跑_GPT55内容监督_ClaudeCode完整复跫_2026-05-02`: 1 files, 0.0 MB
- `选必一_当代国际政治与经济_双线总控_2026-05-02`: 171 files, 1.7 MB
- `选必一_当代国际政治与经济_四线终极全书_2026-05-03`: 533 files, 11.3 MB
- `选必三逻辑与思维_四线从0重跑_2026-05-04`: 926 files, 55.6 MB
- `选必三逻辑与思维_完全模仿哲学宝典返工_2026-05-04`: 12 files, 6.2 MB
- `选必三逻辑与思维双线四线终极跑_2026-05-04`: 129 files, 22.2 MB
- `选必二重做_2026-04-30`: 595 files, 105.6 MB
- `飞哥政治庄园总skill_终局沉淀_2026-05-02.md`: 1 files, 0.0 MB

## Migration Notes

- The desktop project root is not the Git root; this package lives inside the Git sync repository.
- Large/raw source migration should use Git LFS, release assets, or a separate cloud archive if required.
- This snapshot intentionally preserves review-only/candidate labels where the original workflow had not authorized final output.
