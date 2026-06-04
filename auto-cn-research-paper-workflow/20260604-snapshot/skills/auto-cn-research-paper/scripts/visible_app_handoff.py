#!/usr/bin/env python3
"""Prepare a manual visible-app advisor handoff without recording submission."""

from __future__ import annotations

import argparse
import subprocess
from datetime import datetime, timezone
from pathlib import Path


LANES = {
    "claude_opus": "Claude Opus / Opus 4.8 Max",
    "gpt_pro": "GPT Pro / GPT-5.5 Pro",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def stamp() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace(":", "-").replace(".", "-")


def copy_to_clipboard(text: str) -> str:
    try:
        completed = subprocess.run(
            ["pbcopy"],
            input=text,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return f"failed: {exc}"
    if completed.returncode != 0:
        detail = completed.stdout.strip() or f"exit_code={completed.returncode}"
        return f"failed: {detail}"
    return "copied"


def open_app(app_name: str) -> str:
    try:
        completed = subprocess.run(
            ["open", "-a", app_name],
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=15,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return f"failed: {exc}"
    if completed.returncode != 0:
        detail = completed.stdout.strip() or f"exit_code={completed.returncode}"
        return f"failed: {detail}"
    return "opened"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir")
    parser.add_argument("--lane", choices=sorted(LANES), required=True)
    parser.add_argument("--target-app", default="Claude")
    parser.add_argument("--pack", default="27_网页外审精简包.md")
    parser.add_argument("--no-copy", action="store_true", help="Write prompt files but do not use pbcopy.")
    parser.add_argument("--open-app", action="store_true", help="Open the target app without clicking, pasting, or submitting.")
    parser.add_argument("--note", default="")
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    pack_path = Path(args.pack).expanduser()
    if not pack_path.is_absolute():
        pack_path = run_dir / pack_path
    if not pack_path.exists():
        raise SystemExit(f"missing review pack: {pack_path}")

    visible_dir = run_dir / "visible_reviews"
    pending_dir = visible_dir / "pending"
    pending_dir.mkdir(parents=True, exist_ok=True)

    recorded_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    current_stamp = stamp()
    prompt_path = pending_dir / f"{current_stamp}_{args.lane}_app_handoff_prompt.md"
    record_path = visible_dir / f"{current_stamp}_{args.lane}_app_handoff_pending.md"

    prompt = (
        f"请作为真实可见 {LANES[args.lane]} App 复评通道，严格审阅下面这份最新网页外审精简包。"
        "请只按包内“请返回”字段输出，尤其不要在 final_anchor_ready=no 时给 PASS。\n\n"
        + read(pack_path)
    )
    prompt_path.write_text(prompt, encoding="utf-8")

    clipboard_status = "skipped"
    if not args.no_copy:
        clipboard_status = copy_to_clipboard(prompt)

    app_status = "not_requested"
    if args.open_app:
        app_status = open_app(args.target_app)

    record_lines = [
        "# Visible App Manual Handoff Pending",
        "",
        f"- recorded_at: {recorded_at}",
        f"- lane: {args.lane}",
        f"- lane_label: {LANES[args.lane]}",
        "- channel: app_session",
        "- status: manual_submission_pending",
        "- real_submission: false",
        "- visible_review_not_submitted: true",
        f"- target_app: {args.target_app}",
        f"- source_pack: {pack_path}",
        f"- prompt_file: {prompt_path}",
        f"- clipboard_copy_status: {clipboard_status}",
        f"- open_app_status: {app_status}",
    ]
    if args.note:
        record_lines.append(f"- note: {args.note}")
    record_lines.extend(
        [
            "",
            "## Next Required Human-Visible Step",
            "",
            "Paste the prompt into the visible app chat, send it, then save the visible response with `visible_review_record.py`.",
            "This file is not a review record and must not satisfy the final external-review gate.",
            "",
        ]
    )
    record_path.write_text("\n".join(record_lines), encoding="utf-8")

    print("status=manual_submission_pending")
    print("real_submission=false")
    print(f"clipboard_copy_status={clipboard_status}")
    print(f"open_app_status={app_status}")
    print(f"prompt_file={prompt_path}")
    print(f"out={record_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
