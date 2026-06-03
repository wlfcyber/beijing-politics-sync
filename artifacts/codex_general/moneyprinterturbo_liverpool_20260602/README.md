# MoneyPrinterTurbo Liverpool Workflow Snapshot

Snapshot date: 2026-06-03

Included:

- `planning/`: source candidates, event ledger, edit decisions, narration, and fact-check notes.
- `scripts/`: reusable render script.
- `work/audio/`: generated narration audio and metadata.
- `work/subtitles/`: subtitle files used for the rendered clips.
- `work/render/`: ffmpeg render logs.
- `exports/`: rendered MP4 outputs produced in this work lane.

Excluded intentionally:

- MoneyPrinterTurbo `config.toml` and `config.toml.before-deepseek`, because the live config contains provider API keys.
- `work/uv-cache`, `work/uv-python`, virtual environments, PID files, and dependency caches.
- Browser/session state and provider account material.

Operational note: the reusable workflow boundary is that real football-highlight/commentary videos must be grounded in real match footage or explicitly sourced clips; stock media is not a substitute for match footage.
