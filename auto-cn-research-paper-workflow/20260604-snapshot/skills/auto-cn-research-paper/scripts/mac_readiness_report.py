#!/usr/bin/env python3
"""Write a Mac readiness report for the automated CN research-paper workflow."""

from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path


def command_path(command: str) -> str | None:
    extra = [
        str(Path.home() / ".bun/bin"),
        str(Path.home() / ".local/bin"),
        "/opt/homebrew/bin",
        "/usr/local/bin",
    ]
    search_path = os.pathsep.join(extra + [os.environ.get("PATH", "")])
    return shutil.which(command, path=search_path)


def run_version(command: list[str]) -> str:
    try:
        completed = subprocess.run(
            command,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=20,
        )
    except Exception as exc:  # pragma: no cover - defensive for local tool oddities.
        return f"error: {exc}"
    output = completed.stdout.strip().splitlines()
    return output[0] if output else f"exit_code={completed.returncode}"


def chrome_app_status() -> tuple[str, str]:
    candidates = [
        Path("/Applications/Google Chrome.app"),
        Path.home() / "Applications/Google Chrome.app",
    ]
    for path in candidates:
        if path.exists():
            return "present", str(path)
    return "missing", "Google Chrome.app not found in /Applications or ~/Applications"


def status_for_command(command: str, version_args: list[str] | None = None) -> tuple[str, str]:
    path = command_path(command)
    if not path:
        return "missing", "not found on PATH or common Mac tool paths"
    detail = path
    if version_args:
        detail = f"{path}; {run_version([path, *version_args])}"
    return "present", detail


def pro_cli_doctor() -> tuple[str, str, str, str]:
    path = command_path("pro-cli")
    if not path:
        return "no", "missing", "missing", "pro-cli not installed"
    try:
        completed = subprocess.run(
            [path, "doctor", "--json"],
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=60,
        )
        data = json.loads(completed.stdout).get("data", {})
    except Exception as exc:
        return "unknown", "unknown", "unknown", f"doctor error: {exc}"

    ready = "yes" if data.get("ready") else "no"
    auth_status = data.get("auth", {}).get("status", "unknown")
    browser_status = data.get("browserSession", {}).get("status", "unknown")
    next_step = data.get("next", {}).get("command") or data.get("transport", {}).get("status") or "unknown"
    return ready, str(auth_status), str(browser_status), str(next_step)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", help="Run directory or workspace to write mac_readiness_report.md into.")
    parser.add_argument("--out", help="Defaults to <run_dir>/mac_readiness_report.md")
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    run_dir.mkdir(parents=True, exist_ok=True)
    out = Path(args.out).expanduser().resolve() if args.out else run_dir / "mac_readiness_report.md"

    python_status = "present"
    python_detail = sys.executable
    bun_status, bun_detail = status_for_command("bun", ["--version"])
    claude_status, claude_detail = status_for_command("claude", ["--version"])
    pro_cli_status, pro_cli_detail = status_for_command("pro-cli", ["--version"])
    pro_cli_ready, pro_cli_auth_status, pro_cli_browser_status, pro_cli_next = pro_cli_doctor()
    chrome_status, chrome_detail = chrome_app_status()

    blockers: list[str] = []
    if platform.system() != "Darwin":
        blockers.append("not_running_on_macos")
    if claude_status != "present":
        blockers.append("claude_cli_missing")
    if bun_status != "present":
        blockers.append("bun_missing_for_pro_cli")
    if pro_cli_status != "present":
        blockers.append("pro_cli_missing")
    elif pro_cli_ready != "yes":
        if pro_cli_auth_status != "ok":
            blockers.append("pro_cli_auth_not_ready")
        if pro_cli_browser_status not in {"ready", "connected", "ok"}:
            blockers.append("pro_cli_browser_session_not_ready")
    if chrome_status != "present":
        blockers.append("chrome_app_missing")
    blockers.append("browser_hands_free_gate_requires_fresh_mac_validation")
    blockers.append("advisor_pass_gate_requires_real_claude_and_gpt_pass_records")

    lines = [
        "# Mac Readiness Report",
        "",
        "## Summary",
        "",
        f"- platform_system: {platform.system()}",
        f"- platform_release: {platform.release()}",
        f"- workspace: {run_dir}",
        f"- python3_status: {python_status}",
        f"- python3_detail: {python_detail}",
        f"- bun_status: {bun_status}",
        f"- bun_detail: {bun_detail}",
        f"- claude_status: {claude_status}",
        f"- claude_detail: {claude_detail}",
        f"- pro_cli_status: {pro_cli_status}",
        f"- pro_cli_detail: {pro_cli_detail}",
        f"- pro_cli_doctor_ready: {pro_cli_ready}",
        f"- pro_cli_auth_status: {pro_cli_auth_status}",
        f"- pro_cli_browser_session_status: {pro_cli_browser_status}",
        f"- pro_cli_next_command: {pro_cli_next}",
        f"- chrome_app_status: {chrome_status}",
        f"- chrome_app_detail: {chrome_detail}",
        f"- final_user_goal_blocked_by: {', '.join(blockers) if blockers else 'none'}",
        "",
        "## Mac Gate Rule",
        "",
        "Windows evidence cannot satisfy this Mac gate. Revalidate Chrome/browser control, RUC/CNKI session access, full-text/export flow, and both external advisor lanes on this Mac before claiming the final user goal.",
        "",
        "## Next Actions",
        "",
    ]

    if pro_cli_status != "present":
        if bun_status != "present":
            lines.append("- Install Bun first, then install or restore `pro-cli`; `pro-cli` is a Bun/TypeScript CLI.")
        lines.append("- Install or restore `pro-cli`, or use a separately recorded GPT Pro / GPT-5.5 Pro web-session lane with raw evidence.")
    elif pro_cli_ready != "yes":
        lines.append(f"- Complete `pro-cli` setup/auth without exposing secrets. Suggested next command: `{pro_cli_next}`.")
    if claude_status != "present":
        lines.append("- Restore the Claude CLI or use a visible Claude web-session lane with raw evidence.")
    if chrome_status != "present":
        lines.append("- Install or open Google Chrome on this Mac, then rerun the browser access gate.")
    lines.append("- Run `browser_gate_report.py` after a real Mac RUC/CNKI search and full-text/export attempt.")
    lines.append("- Use `external_review_orchestrator.py` only for non-final skill-building advice or prompt-pack preparation. Final paper approval must be recorded from visible ChatGPT/Claude web or app sessions.")

    out.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"platform_system={platform.system()}")
    print(f"python3_status={python_status}")
    print(f"bun_status={bun_status}")
    print(f"claude_status={claude_status}")
    print(f"pro_cli_status={pro_cli_status}")
    print(f"pro_cli_doctor_ready={pro_cli_ready}")
    print(f"pro_cli_auth_status={pro_cli_auth_status}")
    print(f"pro_cli_browser_session_status={pro_cli_browser_status}")
    print(f"chrome_app_status={chrome_status}")
    print(f"out={out}")
    return 0 if not blockers else 1


if __name__ == "__main__":
    raise SystemExit(main())
