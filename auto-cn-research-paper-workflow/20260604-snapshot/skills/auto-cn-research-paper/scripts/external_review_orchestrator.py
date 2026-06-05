#!/usr/bin/env python3
"""Build prompt packs and optionally run external advisor reviews."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


DEFAULT_REVIEW_FILES = [
    "06_论文初稿.md",
    "04_优秀论文范式提取.md",
    "05_论证骨架.md",
    "20_质量差距诊断与重写方案.md",
    "03_文献矩阵.md",
    "07_引用与证据审查.md",
    "09_完成度审计.md",
    "14_S008原刊与政策核验记录.md",
    "15_外部评审与迭代计划.md",
    "16_总闸口矩阵.md",
    "citation_page_suggestions.md",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def scrub(text: str) -> str:
    text = text.replace(r"C:\Users\Administrator\Documents\论文写作\\", r"<workspace>\\")
    text = text.replace(r"C:\Users\Administrator\Documents\论文写作", "<workspace>")
    text = text.replace(r"C:\Users\Administrator\\", r"<user-home>\\")
    text = text.replace(r"C:\Users\Administrator", "<user-home>")
    home = str(Path.home())
    text = text.replace(f"{home}/Documents/论文写作/", "<workspace>/")
    text = text.replace(f"{home}/Documents/论文写作", "<workspace>")
    text = text.replace(f"{home}/", "<user-home>/")
    text = text.replace(home, "<user-home>")
    return text


def command_env() -> dict[str, str]:
    env = os.environ.copy()
    home = Path.home()
    extra_paths = [
        str(home / ".bun/bin"),
        str(home / ".local/bin"),
        "/opt/homebrew/bin",
        "/usr/local/bin",
        str(Path(env.get("LOCALAPPDATA", "")) / "Microsoft/WinGet/Packages/Oven-sh.Bun_Microsoft.Winget.Source_8wekyb3d8bbwe/bun-windows-x64"),
        str(Path(env.get("USERPROFILE", "")) / ".bun/bin"),
    ]
    existing_path = env.get("Path", env.get("PATH", ""))
    path_value = os.pathsep.join([path for path in extra_paths if path] + [existing_path])
    env["Path"] = path_value
    env["PATH"] = path_value
    return env


def run(command: list[str], cwd: Path, timeout: int = 120) -> tuple[int, str]:
    env = command_env()
    executable = shutil.which(command[0], path=env.get("Path", env.get("PATH", "")))
    actual_command = [executable or command[0], *command[1:]]
    completed = subprocess.run(
        actual_command,
        cwd=str(cwd),
        env=env,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
    )
    return completed.returncode, completed.stdout.strip()


def build_prompt(run_dir: Path, lane: str, review_mode: str = "final-gate") -> str:
    sections = []
    for name in DEFAULT_REVIEW_FILES:
        path = run_dir / name
        content = scrub(read(path))
        if content:
            sections.append(f"## File: {name}\n\n```markdown\n{content}\n```")

    if review_mode == "quality-gap":
        task_lines = [
            "# Task",
            "The user says the current draft is far below strong papers. Do not be polite. Return a concise Chinese review with these exact sections:",
            "1. `overall_verdict`: whether the current paper should be patched or rewritten.",
            "2. `gap_against_strong_papers`: compare against strong Chinese humanities/social-science papers on problem consciousness, research object, material organization, theoretical frame, paragraph progression, citation use, and conclusion strength.",
            "3. `workflow_root_causes`: which Codex workflow steps produced the weak paper.",
            "4. `evaluation_of_new_plan`: judge whether `20_质量差距诊断与重写方案.md` and `05_论证骨架.md` are directionally correct and what remains weak.",
            "5. `rewrite_blueprint`: give an executable rewrite blueprint with title, section plan, and the argumentative job of each section.",
            "6. `workflow_reform`: mandatory process changes for future automatic research-paper runs.",
            "7. `non_negotiable_quality_gates`: text-quality gates that must pass before external final review or completion can be claimed.",
        ]
    else:
        task_lines = [
            "# Task",
            "Return a concise Chinese review with these exact sections:",
            "1. `verdict`: PASS, CONDITIONAL_PASS, or REVISE.",
            "2. `graduate_quality_judgment`: whether the draft is a strong graduate-level paper now.",
            "3. `must_fix_before_final`: concrete paper edits.",
            "4. `workflow_must_fix`: concrete workflow gaps before hands-free automation can be claimed.",
            "5. `final_goal_judgment`: whether the user's final goal is achieved.",
            "6. `adoption_notes_for_codex`: what Codex may adopt locally and what must be verified.",
        ]

    return "\n\n".join(
        [
            "# Role",
            f"You are an external {lane} advisor reviewing a Chinese graduate-level humanities/social-science paper and the automation workflow that produced it.",
            "",
            "# Core Rules",
            "- You are advisory, not the evidence source.",
            "- Do not invent authors, journal records, page numbers, DOI, CNKI records, policies, quotations, data, interviews, or source facts.",
            "- Treat S-008 as a public reprint unless the provided files prove a primary PDF/database/original-journal source.",
            "- CAPTCHA, slider, SSO, identity verification, and access controls must not be bypassed.",
            "- Judge both the paper quality and whether the user's final hands-free workflow target has been achieved.",
            "",
            *task_lines,
            "",
            "# Provided Evidence",
            *sections,
        ]
    )


def upsert_summary_line(text: str, key: str, value: str) -> str:
    line = f"- {key}: {value}"
    pattern = rf"^- {re.escape(key)}: .+$"
    if re.search(pattern, text, flags=re.MULTILINE):
        return re.sub(pattern, line, text, flags=re.MULTILINE)
    return text.rstrip() + "\n" + line + "\n"


def advisor_gate_passed(summary: dict[str, object]) -> bool:
    required = [summary.get("claude", {}), summary.get("gpt_pro", {})]
    for item in required:
        if not isinstance(item, dict):
            return False
        if item.get("status") != "pass":
            return False
        if item.get("channel") not in {"web_session", "app_session"}:
            return False
        if item.get("review_scope") != "full_draft":
            return False
        if item.get("real_submission") is not True:
            return False
        if not item.get("review_run_id"):
            return False
        if not item.get("recorded_at"):
            return False
        raw_record = str(item.get("raw_record", ""))
        if not raw_record or "omitted" in raw_record:
            return False
    return True


def write_external_review_status_from_summary(run_dir: Path, summary: dict[str, object], run_folder: Path) -> None:
    path = run_dir / "15_外部评审与迭代计划.md"
    text = read(path)
    if not text:
        return

    claude = summary.get("claude", {})
    gpt = summary.get("gpt_pro", {})
    if not isinstance(claude, dict):
        claude = {}
    if not isinstance(gpt, dict):
        gpt = {}

    text = upsert_summary_line(text, "external_review_passed", "yes" if advisor_gate_passed(summary) else "no")
    for prefix, item in [("claude_opus", claude), ("gpt_pro", gpt)]:
        if item.get("status"):
            text = upsert_summary_line(text, f"{prefix}_review_status", str(item.get("status")))
        if item.get("channel"):
            text = upsert_summary_line(text, f"{prefix}_review_channel", str(item.get("channel")))
        if "real_submission" in item:
            text = upsert_summary_line(
                text,
                f"{prefix}_real_submission",
                "true" if item.get("real_submission") is True else "false",
            )
        if item.get("review_scope"):
            text = upsert_summary_line(text, f"{prefix}_review_scope", str(item.get("review_scope")))
        if item.get("review_run_id"):
            text = upsert_summary_line(text, f"{prefix}_review_run_id", str(item.get("review_run_id")))
        if item.get("recorded_at"):
            text = upsert_summary_line(text, f"{prefix}_review_recorded_at", str(item.get("recorded_at")))
        if item.get("raw_record"):
            text = upsert_summary_line(text, f"{prefix}_raw_record", str(item.get("raw_record")))

    note = (
        "\n\n## 最新外部评审编排记录\n\n"
        f"- run_folder: `{run_folder}`\n"
        f"- claude_opus_review_status: {claude.get('status', 'unchanged')}\n"
        f"- claude_opus_review_channel: {claude.get('channel', 'unknown')}\n"
        f"- claude_opus_review_scope: {claude.get('review_scope', 'unknown')}\n"
        f"- claude_opus_real_submission: {claude.get('real_submission', False)}\n"
        f"- gpt_pro_review_status: {gpt.get('status', 'unchanged')}\n"
        f"- gpt_pro_review_channel: {gpt.get('channel', 'unknown')}\n"
        f"- gpt_pro_review_scope: {gpt.get('review_scope', 'unknown')}\n"
        f"- gpt_pro_real_submission: {gpt.get('real_submission', False)}\n"
    )
    if "## 最新外部评审编排记录" in text:
        text = re.sub(r"\n## 最新外部评审编排记录\n\n[\s\S]*$", lambda _match: note, text)
    else:
        text += note
    path.write_text(text, encoding="utf-8")


def write_external_review_status(run_dir: Path, claude_status: str | None, gpt_status: str | None, run_folder: Path) -> None:
    summary = {
        "claude": {"status": claude_status or "unchanged"},
        "gpt_pro": {"status": gpt_status or "unchanged"},
    }
    write_external_review_status_from_summary(run_dir, summary, run_folder)


def parse_advisor_status(raw: str) -> str:
    try:
        data = json.loads(raw)
        result = json.dumps(data, ensure_ascii=False)
    except json.JSONDecodeError:
        result = raw
    if "REVISE" in result:
        return "revise"
    if "CONDITIONAL_PASS" in result:
        return "conditional_pass"
    if re.search(r"`?PASS`?", result):
        return "pass"
    return "real_call_completed_unparsed"


def parse_claude_status(raw: str) -> str:
    return parse_advisor_status(raw)


def parse_gpt_status(raw: str) -> str:
    return parse_advisor_status(raw)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir")
    parser.add_argument("--out-root", default=".codex/advisor-runs")
    parser.add_argument("--run-claude", action="store_true")
    parser.add_argument("--run-gpt", action="store_true")
    parser.add_argument("--cdp", default="http://127.0.0.1:9222")
    parser.add_argument("--review-mode", choices=["final-gate", "quality-gap"], default="final-gate")
    parser.add_argument("--update-status", action="store_true")
    args = parser.parse_args()

    workspace = Path.cwd().resolve()
    run_dir = Path(args.run_dir).expanduser().resolve()
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    review_dir = (workspace / args.out_root / f"{stamp}-external-paper-review").resolve()
    review_dir.mkdir(parents=True, exist_ok=True)

    claude_prompt = build_prompt(run_dir, "Claude Opus", args.review_mode)
    gpt_prompt = build_prompt(run_dir, "GPT Pro / GPT-5.5 Pro", args.review_mode)
    (review_dir / "claude_prompt.md").write_text(claude_prompt, encoding="utf-8")
    (review_dir / "gpt_pro_prompt.md").write_text(gpt_prompt, encoding="utf-8")

    summary: dict[str, object] = {
        "run_dir": str(run_dir),
        "review_dir": str(review_dir),
        "review_mode": args.review_mode,
        "provenance_gate": {
            "web_session": "submitted in a user-visible web chat/session",
            "app_session": "submitted in a visible ChatGPT or Claude app session",
            "cli_or_api_real_call": "submitted through a local CLI/API/backend tool and saved locally; useful for skill-building advice but not final pass evidence",
            "preflight_only": "readiness check only; no advisor review was submitted",
        },
        "claude": {"requested": args.run_claude, "status": "not_requested"},
        "gpt_pro": {"requested": args.run_gpt, "status": "not_requested"},
    }

    claude_status: str | None = None
    if args.run_claude:
        if not shutil.which("claude"):
            summary["claude"] = {
                "requested": True,
                "status": "missing_cli",
                "channel": "preflight_only",
                "real_submission": False,
                "web_history_expected": False,
            }
            claude_status = "missing_cli"
        else:
            completed = subprocess.run(
                [
                    "claude",
                    "-p",
                    "--model",
                    "opus",
                    "--effort",
                    "max",
                    "--output-format",
                    "json",
                    "--no-session-persistence",
                ],
                cwd=str(workspace),
                input=claude_prompt,
                text=True,
                encoding="utf-8",
                errors="replace",
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=600,
            )
            (review_dir / "claude_raw.json").write_text(completed.stdout, encoding="utf-8")
            claude_status = parse_claude_status(completed.stdout) if completed.returncode == 0 else "call_failed"
            summary["claude"] = {
                "requested": True,
                "status": claude_status,
                "exit_code": completed.returncode,
                "channel": "cli_or_api_real_call",
                "tool": "claude CLI",
                "real_submission": completed.returncode == 0,
                "raw_record": str(review_dir / "claude_raw.json"),
                "web_history_expected": False,
            }

    gpt_status: str | None = None
    if args.run_gpt:
        if not shutil.which("pro-cli", path=command_env().get("Path", "")):
            summary["gpt_pro"] = {
                "requested": True,
                "status": "missing_pro_cli",
                "channel": "preflight_only",
                "real_submission": False,
                "web_history_expected": False,
            }
            gpt_status = "missing_pro_cli"
        else:
            code, doctor = run(["pro-cli", "doctor", "--cdp", args.cdp, "--json"], workspace, timeout=120)
            (review_dir / "gpt_pro_doctor.json").write_text(doctor, encoding="utf-8")
            ready = False
            try:
                doctor_data = json.loads(doctor).get("data", {})
                ready = bool(doctor_data.get("ready"))
                browser_status = doctor_data.get("browserSession", {}).get("status")
            except json.JSONDecodeError:
                ready = False
                browser_status = "unknown"
            if not ready:
                gpt_status = "pending_login_after_install" if browser_status == "logged_out" else "real_call_pending"
                summary["gpt_pro"] = {
                    "requested": True,
                    "status": gpt_status,
                    "browser_status": browser_status,
                    "doctor_exit_code": code,
                    "channel": "preflight_only",
                    "real_submission": False,
                    "raw_record": str(review_dir / "gpt_pro_doctor.json"),
                    "web_history_expected": False,
                }
            else:
                code, output = run(
                    [
                        "pro-cli",
                        "job",
                        "create",
                        f"@{review_dir / 'gpt_pro_prompt.md'}",
                        "--wait",
                        "--reasoning",
                        "extended",
                        "--json",
                    ],
                    workspace,
                    timeout=1200,
                )
                (review_dir / "gpt_pro_raw.json").write_text(output, encoding="utf-8")
                summary["gpt_pro"] = {
                    "requested": True,
                    "status": "real_call_completed" if code == 0 else "call_failed",
                    "exit_code": code,
                    "channel": "cli_or_api_real_call",
                    "tool": "pro-cli job",
                    "real_submission": code == 0,
                    "raw_record": str(review_dir / "gpt_pro_raw.json"),
                    "web_history_expected": "unknown_without_web_verification",
                }
                gpt_status = parse_gpt_status(output) if code == 0 else "call_failed"
                summary["gpt_pro"]["status"] = gpt_status

    (review_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    if args.update_status:
        write_external_review_status_from_summary(run_dir, summary, review_dir)

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if args.run_gpt and gpt_status not in {None, "real_call_completed"}:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
