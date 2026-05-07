# -*- coding: utf-8 -*-
from __future__ import annotations

import os
import subprocess
from datetime import datetime
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[2]
TASK_DIR = RUN_DIR / "claudecode_lane" / "p1_recheck"
PROMPT = TASK_DIR / "CLAUDECODE_P1_RELATIVE_PROMPT.md"
STDOUT = TASK_DIR / "claudecode_p1_relative_stdout.log"
STDERR = TASK_DIR / "claudecode_p1_relative_stderr.log"
RET = TASK_DIR / "claudecode_p1_relative_return_code.txt"


def main() -> int:
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"
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
        str(RUN_DIR),
        str(Path.home() / ".codex" / "skills"),
    ]
    with STDOUT.open("w", encoding="utf-8", errors="replace") as out, STDERR.open(
        "w", encoding="utf-8", errors="replace"
    ) as err:
        out.write(f"started={datetime.now().isoformat(timespec='seconds')}\n")
        out.flush()
        code = subprocess.run(cmd, cwd=str(RUN_DIR), stdout=out, stderr=err, text=True, env=env).returncode
    RET.write_text(str(code), encoding="utf-8")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
