# -*- coding: utf-8 -*-
from __future__ import annotations

import subprocess
from datetime import datetime
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[2]
TASK_DIR = RUN_DIR / "claudecode_lane" / "p1_recheck"
PROMPT = TASK_DIR / "CLAUDECODE_P1_RECHECK_PROMPT.md"
STDOUT = TASK_DIR / "claudecode_p1_recheck_stdout.log"
STDERR = TASK_DIR / "claudecode_p1_recheck_stderr.log"
RET = TASK_DIR / "claudecode_p1_recheck_return_code.txt"

ADD_DIRS = [
    str(Path(r"C:\Users\Administrator\.codex\skills")),
    str(Path(r"C:\Users\Administrator\Desktop\2024各区模拟题")),
    str(Path(r"C:\Users\Administrator\Desktop\2025各区模拟题")),
    str(Path(r"C:\Users\Administrator\Desktop\2026各区模拟题")),
    str(RUN_DIR),
]


def main() -> int:
    TASK_DIR.mkdir(parents=True, exist_ok=True)
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
        code = subprocess.run(cmd, stdout=out, stderr=err, text=True).returncode
    RET.write_text(str(code), encoding="utf-8")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
