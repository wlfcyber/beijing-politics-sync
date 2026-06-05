#!/usr/bin/env python3
"""Record visible web/app GPT or Claude external review evidence."""

from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path


LANES = {
    "claude_opus": "Claude Opus / Opus 4.8 Max",
    "gpt_pro": "GPT Pro / GPT-5.5 Pro",
}
VISIBLE_CHANNELS = {"web_session", "app_session"}
STATUSES = {"pass", "conditional_pass", "revise", "pending"}
REVIEW_SCOPES = {
    "full_draft",
    "revision_delta",
    "citation_page_spotcheck",
    "preflight_or_handoff",
    "unspecified",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def upsert_summary_line(text: str, key: str, value: str) -> str:
    line = f"- {key}: {value}"
    pattern = rf"^- {re.escape(key)}: .+$"
    if re.search(pattern, text, flags=re.MULTILINE):
        return re.sub(pattern, line, text, flags=re.MULTILINE)
    return text.rstrip() + "\n" + line + "\n"


def parse_summary_value(text: str, key: str) -> str:
    match = re.search(rf"^- {re.escape(key)}:\s*(.+)$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else "unknown"


def parse_boolish(text: str, key: str) -> bool:
    return parse_summary_value(text, key).lower() in {"true", "yes", "1"}


def lane_ready(text: str, lane: str) -> bool:
    return (
        parse_summary_value(text, f"{lane}_review_status") == "pass"
        and parse_summary_value(text, f"{lane}_review_channel") in VISIBLE_CHANNELS
        and parse_boolish(text, f"{lane}_real_submission")
        and parse_summary_value(text, f"{lane}_review_scope") == "full_draft"
        and parse_summary_value(text, f"{lane}_review_run_id") != "unknown"
        and parse_summary_value(text, f"{lane}_review_recorded_at") != "unknown"
        and parse_summary_value(text, f"{lane}_raw_record") not in {"unknown", "", "omitted"}
    )


def external_ready(text: str) -> bool:
    return lane_ready(text, "claude_opus") and lane_ready(text, "gpt_pro")


def append_record_note(
    text: str,
    lane: str,
    status: str,
    channel: str,
    review_scope: str,
    raw_record: str,
    review_url: str,
    note: str,
) -> str:
    lines = [
        "",
        "## 可见外部评审记录",
        "",
        f"- recorded_at: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        f"- lane: {lane}",
        f"- lane_label: {LANES[lane]}",
        f"- status: {status}",
        f"- channel: {channel}",
        f"- review_scope: {review_scope}",
        f"- raw_record: {raw_record}",
    ]
    if review_url:
        lines.append(f"- review_url: {review_url}")
    if note:
        lines.append(f"- note: {note}")
    lines.append("")
    return text.rstrip() + "\n" + "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir")
    parser.add_argument("--lane", choices=sorted(LANES), required=True)
    parser.add_argument("--status", choices=sorted(STATUSES), required=True)
    parser.add_argument("--channel", choices=sorted(VISIBLE_CHANNELS), required=True)
    parser.add_argument(
        "--review-scope",
        choices=sorted(REVIEW_SCOPES),
        default="unspecified",
        help="Use full_draft only when the visible model reviewed the full paper package.",
    )
    parser.add_argument("--raw-record", required=True, help="Path to pasted review transcript, screenshot note, or exported visible-session evidence.")
    parser.add_argument("--review-url", default="", help="Optional visible web/app conversation URL or share link.")
    parser.add_argument("--note", default="")
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    status_path = run_dir / "15_外部评审与迭代计划.md"
    raw_record = Path(args.raw_record).expanduser()
    raw_record_resolved = raw_record.resolve()

    if not status_path.exists():
        raise SystemExit(f"missing external review status file: {status_path}")
    if not raw_record_resolved.exists():
        raise SystemExit(f"raw record path does not exist: {raw_record_resolved}")

    text = read(status_path)
    prefix = args.lane
    recorded_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    text = upsert_summary_line(text, f"{prefix}_review_status", args.status)
    text = upsert_summary_line(text, f"{prefix}_review_channel", args.channel)
    text = upsert_summary_line(text, f"{prefix}_real_submission", "true")
    text = upsert_summary_line(text, f"{prefix}_review_scope", args.review_scope)
    text = upsert_summary_line(text, f"{prefix}_review_run_id", run_dir.name)
    text = upsert_summary_line(text, f"{prefix}_review_recorded_at", recorded_at)
    text = upsert_summary_line(text, f"{prefix}_raw_record", str(raw_record_resolved))
    text = append_record_note(
        text,
        lane=args.lane,
        status=args.status,
        channel=args.channel,
        review_scope=args.review_scope,
        raw_record=str(raw_record_resolved),
        review_url=args.review_url,
        note=args.note,
    )
    text = upsert_summary_line(text, "external_review_passed", "yes" if external_ready(text) else "no")
    status_path.write_text(text, encoding="utf-8")

    print(f"lane={args.lane}")
    print(f"lane_status={args.status}")
    print(f"channel={args.channel}")
    print(f"review_scope={args.review_scope}")
    print(f"external_review_passed={'yes' if external_ready(text) else 'no'}")
    print(f"out={status_path}")
    return 0 if external_ready(text) else 1


if __name__ == "__main__":
    raise SystemExit(main())
