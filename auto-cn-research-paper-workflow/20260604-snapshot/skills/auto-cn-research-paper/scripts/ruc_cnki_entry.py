#!/usr/bin/env python3
"""Record and optionally open the official RUC Library CNKI journal entry."""

from __future__ import annotations

import argparse
import json
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


RESOURCE = {
    "name": "中国知网-中国期刊全文数据库（网络版）",
    "rid": "114",
    "provider": "同方知网技术有限公司",
    "official_info_url": "https://libproxy.ruc.edu.cn/ermsClient/eresourceInfo.do?rid=114",
    "offcampus_url": "https://libproxy.ruc.edu.cn/entry.do?rid=114&uid=249",
    "campus_url": "http://kns.cnki.net/kns8",
    "source_note": "RUC Library electronic resource page for rid=114; off-campus access is routed through libproxy.ruc.edu.cn.",
}


def write_candidates(run_dir: Path) -> Path:
    out = run_dir / "ruc_cnki_entry_candidates.md"
    lines = [
        "# RUC CNKI Entry Candidates",
        "",
        "## Selected Resource",
        "",
        f"- name: {RESOURCE['name']}",
        f"- rid: {RESOURCE['rid']}",
        f"- provider: {RESOURCE['provider']}",
        f"- official_info_url: {RESOURCE['official_info_url']}",
        f"- offcampus_url: {RESOURCE['offcampus_url']}",
        f"- campus_url: {RESOURCE['campus_url']}",
        f"- source_note: {RESOURCE['source_note']}",
        "",
        "## Safety Rule",
        "",
        "This script may open the official RUC Library/CNKI entry in Chrome CDP. 用户必须自行完成登录、SSO、验证码、身份核验、权限确认或下载确认；脚本不得绕过这些步骤。",
    ]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def selected_url(mode: str) -> str:
    if mode == "campus":
        return RESOURCE["campus_url"]
    if mode == "info":
        return RESOURCE["official_info_url"]
    return RESOURCE["offcampus_url"]


def open_chrome_cdp(url: str, cdp_base: str, timeout: float) -> tuple[str, str]:
    endpoint = cdp_base.rstrip("/") + "/json/new?" + urllib.parse.quote(url, safe=":/?&=%")
    request = urllib.request.Request(endpoint, method="PUT")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = response.read().decode("utf-8", errors="replace")
    try:
        data = json.loads(body)
        target_url = str(data.get("url", "unknown"))
        target_id = str(data.get("id", "unknown"))
        return "opened", f"id={target_id}; url={target_url}"
    except json.JSONDecodeError:
        return "opened_unparsed", body[:500]


def write_open_report(
    run_dir: Path,
    mode: str,
    url: str,
    open_status: str,
    detail: str,
    cdp_base: str,
) -> Path:
    out = run_dir / "ruc_cnki_entry_open.md"
    lines = [
        "# RUC CNKI Entry Open",
        "",
        "## Summary",
        "",
        f"- generated_at: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        f"- selected_resource: {RESOURCE['name']}",
        f"- selected_rid: {RESOURCE['rid']}",
        f"- selected_mode: {mode}",
        f"- selected_url: {url}",
        f"- cdp_base: {cdp_base}",
        f"- open_status: {open_status}",
        f"- open_detail: {detail}",
        "",
        "## User Action Boundary",
        "",
        "用户必须自行完成登录、SSO、验证码、滑块、身份核验、权限确认或下载确认。脚本只打开官方入口并记录目标 URL，不读取账号凭据、cookie、local storage、表单内容或页面正文。",
    ]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir")
    parser.add_argument("--list", action="store_true", help="Write ruc_cnki_entry_candidates.md")
    parser.add_argument("--open", action="store_true", help="Open the selected RUC/CNKI entry in Chrome CDP.")
    parser.add_argument("--mode", choices=["offcampus", "campus", "info"], default="offcampus")
    parser.add_argument("--cdp-base", default="http://127.0.0.1:9222")
    parser.add_argument("--timeout", type=float, default=10)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    run_dir.mkdir(parents=True, exist_ok=True)
    candidates = write_candidates(run_dir)

    print(f"candidates={candidates}")
    if not args.open:
        return 0

    url = selected_url(args.mode)
    if args.dry_run:
        status, detail = "dry_run", "not opened"
    else:
        try:
            status, detail = open_chrome_cdp(url, args.cdp_base, args.timeout)
        except Exception as exc:
            status, detail = "failed", str(exc)
    out = write_open_report(run_dir, args.mode, url, status, detail, args.cdp_base)
    print(f"selected_url={url}")
    print(f"open_status={status}")
    print(f"out={out}")
    return 0 if status in {"dry_run", "opened", "opened_unparsed"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
