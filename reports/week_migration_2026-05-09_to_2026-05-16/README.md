# Week Migration 2026-05-09 to 2026-05-16

This package snapshots Beijing Gaokao politics artifacts created or modified from 2026-05-09 through 2026-05-16 across desktop and supervision threads.

Included:

- `desktop_snapshots/选必一_原PDF框架主观题宝典重构_2026-05-09`: source framework extraction, old-document audit, subjective-only filtering, Claude packets/drafts, V2/V3/V4 audit and final drafts, build scripts, final DOCX outputs, and render/text checks.
- `supervision_snapshots/选必二_LIVE_SUPERVISION_BOARD_2026-05-16.md`: latest visible ClaudeCode supervision board from the 选必二 lane.
- Existing repository-side 选必三 2026-05-07 delivery revision folders are committed in the same sync round under `reports/xuanbisan_exhaustive_claudecode_2026-05-07/`.

Included files in this weekly package: 142
Included size: about 4.8 MB

Excluded from Git in this package:

- `.DS_Store`
- Python bytecode caches
- PDF/OCR page images and render PNGs

Notes:

- The desktop project root is not the Git root; this package lives inside `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync`.
- Final DOCX deliverables are included because they are student-facing/results artifacts, not raw source corpora.
- Raw source PDFs, scans, and large visual caches remain outside normal Git per the project sync rule.
