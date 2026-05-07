# -*- coding: utf-8 -*-
from __future__ import annotations

import subprocess
from datetime import datetime
from pathlib import Path


REPAIR_DIR = Path(r"C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches\batch02_output_repair")
PROMPT = REPAIR_DIR / "CLAUDECODE_BATCH02_OUTPUT_REPAIR_PROMPT.md"
STDOUT = REPAIR_DIR / "claudecode_batch02_output_repair_stdout.log"
STDERR = REPAIR_DIR / "claudecode_batch02_output_repair_stderr.log"
RET = REPAIR_DIR / "claudecode_batch02_output_repair_return_code.txt"

ADD_DIRS = [
    r"C:\Users\Administrator\.codex\skills",
    r"C:\Users\Administrator\Desktop\2024各区模拟题",
    r"C:\Users\Administrator\Desktop\2025各区模拟题",
    r"C:\Users\Administrator\Desktop\2026各区模拟题",
    r"C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus",
    r"C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible",
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
        code = subprocess.run(cmd, stdout=out, stderr=err, text=True).returncode
    RET.write_text(str(code), encoding="utf-8")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
