# -*- coding: utf-8 -*-
from __future__ import annotations

import subprocess
from datetime import datetime
from pathlib import Path


BATCH_DIR = Path(r"C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch02a_chaoyang_yimo_2024")
PROMPT = BATCH_DIR / "CLAUDECODE_BATCH02A_PROMPT.md"
STDOUT = BATCH_DIR / "claudecode_batch02a_stdout.log"
STDERR = BATCH_DIR / "claudecode_batch02a_stderr.log"

ADD_DIRS = [
    r"C:\Users\Administrator\.codex\skills",
    r"C:\Users\Administrator\Desktop\2024各区模拟题",
    r"C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus",
    r"C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible",
    r"C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07",
]


def main() -> int:
    BATCH_DIR.mkdir(parents=True, exist_ok=True)
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
