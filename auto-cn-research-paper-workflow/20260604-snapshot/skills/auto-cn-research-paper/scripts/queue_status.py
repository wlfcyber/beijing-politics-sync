#!/usr/bin/env python3
"""Summarize a CNKI candidate download queue Markdown file."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


CAPTCHA_TERMS = ["拼图", "验证码", "滑块", "SSO", "身份确认", "安全验证"]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def parse_summary_value(text: str, key: str) -> str:
    match = re.search(rf"^- {re.escape(key)}:\s*(.+)$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else "unknown"


def parse_rows(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line in text.splitlines():
        if not line.startswith("| C-"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 6:
            continue
        if "->" in cells[0] or "无需继续下载" in cells[-1] or "已进入正式文献矩阵" in line:
            continue
        item = {
            "id": cells[0],
            "title": cells[1],
            "authors": cells[2],
            "source": cells[3],
            "status_or_position": cells[4],
            "next": cells[-1],
        }
        rows.append(item)
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("queue_file", help="Candidate queue Markdown file.")
    parser.add_argument("--verified-fulltext", type=int, default=0)
    parser.add_argument("--target-fulltext", type=int, default=8)
    parser.add_argument("--browser-gate", help="Defaults to sibling 12_浏览器准入验收.md when present.")
    args = parser.parse_args()

    queue_path = Path(args.queue_file).expanduser().resolve()
    text = read(queue_path)
    gate_path = Path(args.browser_gate).expanduser().resolve() if args.browser_gate else queue_path.parent / "12_浏览器准入验收.md"
    gate_text = read(gate_path)
    user_verification_status = parse_summary_value(gate_text, "user_verification_status")
    hands_free_ready = parse_summary_value(gate_text, "hands_free_ready")
    rows = parse_rows(text)
    waiting_user_scan = any(term in text for term in CAPTCHA_TERMS)
    waiting_user = user_verification_status == "waiting_user" if user_verification_status != "unknown" else waiting_user_scan
    remaining = max(args.target_fulltext - args.verified_fulltext, 0)
    next_items = rows[:remaining] if remaining else []

    print(f"queue_items={len(rows)}")
    print(f"waiting_user_verification={'yes' if waiting_user else 'no'}")
    print(f"browser_hands_free_ready={hands_free_ready}")
    print(f"verified_fulltext={args.verified_fulltext}")
    print(f"target_fulltext={args.target_fulltext}")
    print(f"remaining_fulltext={remaining}")
    for item in next_items:
        print(f"- {item['id']}: {item['title']} -> {item['next']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
