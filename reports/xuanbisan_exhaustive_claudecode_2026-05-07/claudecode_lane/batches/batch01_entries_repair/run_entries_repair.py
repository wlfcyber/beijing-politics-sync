# -*- coding: utf-8 -*-
from __future__ import annotations

import subprocess
from datetime import datetime
from pathlib import Path


REPAIR_DIR = Path(r"C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch01_entries_repair")
PROMPT = REPAIR_DIR / "CLAUDECODE_BATCH01_ENTRIES_REPAIR_PROMPT.md"
STDOUT = REPAIR_DIR / "entries_repair_stdout.log"
STDERR = REPAIR_DIR / "entries_repair_stderr.log"

ADD_DIRS = [
    r"C:\Users\Administrator\.codex\skills",
    r"C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07",
]


def main() -> int:
    REPAIR_DIR.mkdir(parents=True, exist_ok=True)
    cmd = [
        "claude",
        "-p",
        PROMPT.read_text(encoding="utf-8"),
        "--model",
        "opus",
        "--permission-mode",
        "auto",
        "--effort",
        "max",
        "--add-dir",
        *ADD_DIRS,
    ]
    with STDOUT.open("w", encoding="utf-8", errors="replace") as out, STDERR.open("w", encoding="utf-8", errors="replace") as err:
        out.write(f"started={datetime.now().isoformat(timespec='seconds')}\n")
        out.flush()
        return subprocess.run(cmd, stdout=out, stderr=err, text=True).returncode


if __name__ == "__main__":
    raise SystemExit(main())
