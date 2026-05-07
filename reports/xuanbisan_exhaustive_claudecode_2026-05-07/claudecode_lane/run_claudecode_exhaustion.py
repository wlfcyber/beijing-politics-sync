# -*- coding: utf-8 -*-
from __future__ import annotations

import os
import subprocess
import time
from pathlib import Path


RUN_DIR = Path(r"C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07")
LANE_DIR = RUN_DIR / "claudecode_lane"
PROMPT_FILE = LANE_DIR / "CLAUDECODE_EXHAUSTION_PROMPT.md"

ADD_DIRS = [
    r"C:\Users\Administrator\.codex\skills",
    r"C:\Users\Administrator\Desktop\2024各区模拟题",
    r"C:\Users\Administrator\Desktop\2025各区模拟题",
    r"C:\Users\Administrator\Desktop\2026各区模拟题",
    r"C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus",
    r"C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible",
    str(RUN_DIR),
]


def main() -> int:
    os.chdir(RUN_DIR)
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")

    prompt = PROMPT_FILE.read_text(encoding="utf-8")
    cmd = [
        "claude",
        "-p",
        prompt,
        "--model",
        "opus",
        "--permission-mode",
        "auto",
        "--effort",
        "max",
        "--add-dir",
        *ADD_DIRS,
    ]

    (LANE_DIR / "claudecode_exhaustion_started_at.txt").write_text(
        time.strftime("%Y-%m-%d %H:%M:%S") + "\n", encoding="utf-8"
    )
    (LANE_DIR / "claudecode_exhaustion_model_config.txt").write_text(
        "model=opus\n"
        "model_alias_meaning=latest Opus exposed by Claude Code CLI\n"
        "effort=max\n"
        "adaptive_thinking_mapping=Claude Code CLI has no separate adaptive-thinking flag; max effort is the enforced thinking-depth setting.\n"
        "cli_version_checked=2.1.119 (Claude Code)\n",
        encoding="utf-8",
    )

    print("Launching real local ClaudeCode exhaustion pass", flush=True)
    print(f"RUN_DIR={RUN_DIR}", flush=True)
    print(f"PROMPT_FILE={PROMPT_FILE}", flush=True)
    print("MODEL=opus", flush=True)
    print("EFFORT=max", flush=True)
    print("ADD_DIRS:", flush=True)
    for add_dir in ADD_DIRS:
        print(f"- {add_dir} exists={Path(add_dir).exists()}", flush=True)

    proc = subprocess.run(cmd, cwd=str(RUN_DIR), text=True)
    (LANE_DIR / "claudecode_exhaustion_return_code.txt").write_text(
        str(proc.returncode) + "\n", encoding="ascii"
    )
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())

