#!/usr/bin/env python3
"""Probe Chrome CDP tabs without reading credentials or page storage."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


AUTHORIZED_URL_MARKERS = [
    "libproxy.ruc.edu.cn",
    "cnki.net",
    "oversea.cnki.net",
    "kns.cnki.net",
    "navi.cnki.net",
]

USER_ACTION_MARKERS = [
    "v.ruc.edu.cn/account/login",
    "oauth2/authorize",
    "verify/home",
    "captchatype",
    "blockpuzzle",
    "sso",
    "login",
    "登录",
    "安全验证",
    "验证码",
    "滑块",
    "身份",
]


def load_targets_from_json(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("targets JSON must be a list")
    return [item for item in data if isinstance(item, dict)]


def fetch_targets(cdp_base: str, timeout: float) -> list[dict[str, Any]]:
    url = cdp_base.rstrip("/") + "/json/list"
    with urllib.request.urlopen(url, timeout=timeout) as response:
        data = json.loads(response.read().decode("utf-8", errors="replace"))
    if not isinstance(data, list):
        raise ValueError("Chrome CDP /json/list did not return a list")
    return [item for item in data if isinstance(item, dict)]


def clean(value: Any) -> str:
    text = str(value or "").replace("\n", " ").replace("\r", " ").strip()
    return text[:500]


def is_page_target(target: dict[str, Any]) -> bool:
    return clean(target.get("type")) == "page" and clean(target.get("url")).startswith(("http://", "https://"))


def is_authorized_candidate(target: dict[str, Any]) -> bool:
    url = clean(target.get("url")).lower()
    title = clean(target.get("title")).lower()
    haystack = f"{url} {title}"
    return any(marker in haystack for marker in AUTHORIZED_URL_MARKERS)


def is_user_action_target(target: dict[str, Any]) -> bool:
    url = clean(target.get("url")).lower()
    title = clean(target.get("title")).lower()
    haystack = f"{url} {title}"
    return any(marker.lower() in haystack for marker in USER_ACTION_MARKERS)


def choose_target(
    page_targets: list[dict[str, Any]],
    authorized_targets: list[dict[str, Any]],
    user_action_targets: list[dict[str, Any]],
) -> dict[str, Any] | None:
    if user_action_targets:
        return user_action_targets[0]
    if authorized_targets:
        return authorized_targets[0]
    if page_targets:
        return page_targets[0]
    return None


def target_row(target: dict[str, Any]) -> str:
    target_type = clean(target.get("type")) or "unknown"
    title = clean(target.get("title")) or "untitled"
    url = clean(target.get("url")) or "unknown"
    authorized = "yes" if is_authorized_candidate(target) else "no"
    user_action = "yes" if is_user_action_target(target) else "no"
    return f"| {target_type} | {title} | {url} | {authorized} | {user_action} |"


def write_report(
    run_dir: Path,
    out: Path,
    cdp_base: str,
    targets: list[dict[str, Any]],
    error: str = "",
) -> tuple[bool, str, str]:
    page_targets = [target for target in targets if is_page_target(target)]
    authorized_targets = [target for target in page_targets if is_authorized_candidate(target)]
    user_action_targets = [target for target in page_targets if is_user_action_target(target)]
    selected = choose_target(page_targets, authorized_targets, user_action_targets)

    browser_path_status = "pass" if page_targets else "fail"
    user_action_status = "waiting_user" if user_action_targets else "pass"
    if user_action_targets:
        authorized_page_status = "waiting_user"
    else:
        authorized_page_status = "pass" if authorized_targets else "fail"
    highest_capability_tier = "claim_url" if page_targets else ("tab_list" if targets else "none")
    blocker = "none"
    if error:
        blocker = error
    elif user_action_targets:
        blocker = "user action required: login/SSO/CAPTCHA/identity page is visible"
    elif not page_targets:
        blocker = "no inspectable http(s) page target found"
    elif not authorized_targets:
        blocker = "no RUC/CNKI authorized candidate page found"

    selected_title = clean(selected.get("title")) if selected else "unknown"
    selected_url = clean(selected.get("url")) if selected else "unknown"

    lines = [
        "# Chrome CDP Probe",
        "",
        "## Summary",
        "",
        f"- run_id: {run_dir.name}",
        f"- generated_at: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        f"- cdp_base: {cdp_base}",
        f"- browser_path_status: {browser_path_status}",
        f"- authorized_page_status: {authorized_page_status}",
        f"- user_action_status: {user_action_status}",
        f"- matching_target_count: {len(authorized_targets)}",
        f"- highest_capability_tier: {highest_capability_tier}",
        f"- selected_title: {selected_title}",
        f"- selected_url: {selected_url}",
        f"- blocker: {blocker}",
        "",
        "## Safety",
        "",
        "This probe records Chrome tab titles and URLs only. It does not read cookies, passwords, local storage, page text, forms, or downloaded files.",
        "",
        "## Targets",
        "",
        "| type | title | url | authorized_candidate | user_action_required |",
        "| --- | --- | --- | --- | --- |",
    ]
    lines.extend(target_row(target) for target in targets)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return browser_path_status == "pass" and authorized_page_status == "pass", browser_path_status, authorized_page_status


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", help="Run directory or workspace to write chrome_cdp_probe.md into.")
    parser.add_argument("--out", help="Defaults to <run_dir>/chrome_cdp_probe.md")
    parser.add_argument("--cdp-base", default="http://127.0.0.1:9222")
    parser.add_argument("--targets-json", help="Use a saved /json/list payload instead of live Chrome; for tests or preserved evidence.")
    parser.add_argument("--timeout", type=float, default=10)
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    run_dir.mkdir(parents=True, exist_ok=True)
    out = Path(args.out).expanduser().resolve() if args.out else run_dir / "chrome_cdp_probe.md"

    error = ""
    try:
        targets = load_targets_from_json(Path(args.targets_json).expanduser().resolve()) if args.targets_json else fetch_targets(args.cdp_base, args.timeout)
    except (OSError, urllib.error.URLError, json.JSONDecodeError, ValueError) as exc:
        targets = []
        error = f"cdp probe error: {exc}"

    passed, browser_path_status, authorized_page_status = write_report(run_dir, out, args.cdp_base, targets, error=error)
    print(f"browser_path_status={browser_path_status}")
    print(f"authorized_page_status={authorized_page_status}")
    print(f"out={out}")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
