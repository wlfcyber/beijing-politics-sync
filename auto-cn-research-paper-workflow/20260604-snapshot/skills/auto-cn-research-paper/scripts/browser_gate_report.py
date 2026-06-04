#!/usr/bin/env python3
"""Write a browser-access gate report for an automated CN research-paper run."""

from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path


CAPTCHA_TERMS = ["拼图", "验证码", "滑块", "SSO", "身份确认", "安全验证"]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def count_verified_sources(matrix_text: str) -> int:
    return sum(
        1
        for line in matrix_text.splitlines()
        if line.startswith("| S-") and ("PDF_or_user_exported" in line or "full_text_read" in line)
    )


def status_line(status: str, evidence: str) -> str:
    return f"{status} | {evidence.strip() or '未记录'} |"


def parse_summary_value(text: str, key: str) -> str:
    match = re.search(rf"^- {re.escape(key)}:\s*(.+)$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else "unknown"


def normalize_status(value: str) -> str:
    value = value.strip().lower()
    allowed = {"pass", "fail", "unknown", "waiting_user", "blocked", "partial"}
    if value not in allowed:
        raise argparse.ArgumentTypeError(f"unsupported status: {value}")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir")
    parser.add_argument("--out", help="Defaults to <run_dir>/12_浏览器准入验收.md")
    parser.add_argument("--browser-path-status", type=normalize_status, default="unknown")
    parser.add_argument("--browser-path-note", default="")
    parser.add_argument("--user-verification-status", type=normalize_status, default="unknown")
    parser.add_argument("--user-verification-note", default="")
    parser.add_argument("--computer-use-status", type=normalize_status, default="unknown")
    parser.add_argument("--computer-use-note", default="")
    parser.add_argument("--current-url-status", type=normalize_status, default="unknown")
    parser.add_argument("--current-url-note", default="")
    parser.add_argument("--probe-report", help="Defaults to <run_dir>/chrome_cdp_probe.md when present.")
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    out_path = Path(args.out).expanduser().resolve() if args.out else run_dir / "12_浏览器准入验收.md"
    probe_path = Path(args.probe_report).expanduser().resolve() if args.probe_report else run_dir / "chrome_cdp_probe.md"

    search_text = read(run_dir / "02_检索日志.md")
    matrix_text = read(run_dir / "03_文献矩阵.md")
    inventory_text = read(run_dir / "source_inventory.md")
    queue_text = read(run_dir / "10_候选下载队列.md")
    audit_text = read(run_dir / "09_完成度审计.md")
    probe_text = read(probe_path)

    browser_path_status = args.browser_path_status
    current_url_status = args.current_url_status
    browser_path_note = args.browser_path_note
    current_url_note = args.current_url_note
    user_verification_status = args.user_verification_status
    probe_run_id_status = "not_present"
    probe_note = ""
    if probe_text:
        probe_run_id = parse_summary_value(probe_text, "run_id")
        if probe_run_id == run_dir.name:
            probe_run_id_status = "match"
        else:
            probe_run_id_status = "mismatch"
            probe_note = f"probe run_id mismatch: {probe_run_id} != {run_dir.name}"
        probe_browser_path = parse_summary_value(probe_text, "browser_path_status")
        probe_authorized_page = parse_summary_value(probe_text, "authorized_page_status")
        probe_user_action = parse_summary_value(probe_text, "user_action_status")
        probe_title = parse_summary_value(probe_text, "selected_title")
        probe_url = parse_summary_value(probe_text, "selected_url")
        probe_blocker = parse_summary_value(probe_text, "blocker")
        if probe_run_id_status == "match":
            probe_note = f"Chrome CDP 探针: {probe_title}; {probe_url}"
            if probe_blocker not in {"none", "unknown", ""}:
                probe_note = f"{probe_note}; blocker={probe_blocker}"
            if browser_path_status == "unknown" and probe_browser_path in {"pass", "fail"}:
                browser_path_status = probe_browser_path
                browser_path_note = probe_note
            if current_url_status == "unknown" and probe_authorized_page in {"pass", "fail", "waiting_user"}:
                current_url_status = probe_authorized_page
                current_url_note = probe_note
            if user_verification_status == "unknown" and probe_user_action == "waiting_user":
                user_verification_status = "waiting_user"
                args.user_verification_note = probe_note

    verified = count_verified_sources(matrix_text)
    ruc_route = "pass" if ("libproxy.ruc.edu.cn" in search_text or "人大图书馆" in search_text) else "fail"
    search_status = "pass" if re.search(r"主题=`|检索页 URL|实际检索记录", search_text) else "fail"
    detail_status = "pass" if "详情页" in search_text else "fail"
    fulltext_status = "pass" if verified else "blocked"
    ledger_status = "pass" if matrix_text and inventory_text else "fail"
    waiting_terms_present = any(term in queue_text or term in audit_text or term in search_text for term in CAPTCHA_TERMS)

    if user_verification_status == "unknown" and waiting_terms_present:
        user_verification_status = "waiting_user"

    checks = {
        "browser_path": browser_path_status,
        "current_url": current_url_status,
        "computer_use": args.computer_use_status,
        "user_verification": user_verification_status,
        "ruc_route": ruc_route,
        "search": search_status,
        "result_detail": detail_status,
        "full_text_or_export": fulltext_status,
        "ledger": ledger_status,
    }

    hands_free_ready = all(
        checks[key] == "pass"
        for key in [
            "browser_path",
            "current_url",
            "user_verification",
            "ruc_route",
            "search",
            "result_detail",
            "full_text_or_export",
            "ledger",
        ]
    )

    lines = [
        "# 浏览器准入验收",
        "",
        "## 结论",
        "",
        f"- run_id: {run_dir.name}",
        f"- generated_at: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        f"- hands_free_ready: {'yes' if hands_free_ready else 'no'}",
        f"- verified_fulltext: {verified}",
        f"- probe_run_id_status: {probe_run_id_status}",
        f"- browser_path_status: {browser_path_status}",
        f"- current_url_status: {current_url_status}",
        f"- computer_use_status: {args.computer_use_status}",
        f"- user_verification_status: {user_verification_status}",
        "",
        "## 检查项",
        "",
        "| 检查项 | 状态 | 证据 |",
        "| --- | --- | --- |",
        f"| 探针 run-id 绑定 | {status_line(probe_run_id_status, probe_note)}",
        f"| Chrome/浏览器控制路径 | {status_line(browser_path_status, browser_path_note)}",
        f"| 当前 URL 可确认 | {status_line(current_url_status, current_url_note)}",
        f"| Computer Use 备用路径 | {status_line(args.computer_use_status, args.computer_use_note)}",
        f"| 用户验证状态 | {status_line(user_verification_status, args.user_verification_note)}",
        f"| 人大图书馆代理路径 | {status_line(ruc_route, '检索日志含 libproxy.ruc.edu.cn 或 人大图书馆 记录')}",
        f"| 检索已执行 | {status_line(search_status, '检索日志含实际检索记录')}",
        f"| 详情页已打开 | {status_line(detail_status, '检索日志含详情页记录')}",
        f"| 全文/导出可读 | {status_line(fulltext_status, f'文献矩阵已核验全文 {verified} 篇')}",
        f"| 台账记录 | {status_line(ledger_status, '文献矩阵与 source_inventory.md 已存在')}",
        "",
        "## 判定规则",
        "",
        "只有浏览器路径、当前 URL、人大代理路径、检索、详情页、全文/导出、台账和当前用户验证状态全部为 `pass`，才可声称当前数据库自动化链路可用。",
        "出现验证码、拼图、滑块、SSO、身份确认、下载确认、权限提示或 URL 无法可靠确认时，不得继续自动点击下载。",
    ]

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"hands_free_ready={'yes' if hands_free_ready else 'no'}")
    print(f"probe_run_id_status={probe_run_id_status}")
    print(f"browser_path_status={browser_path_status}")
    print(f"current_url_status={current_url_status}")
    print(f"computer_use_status={args.computer_use_status}")
    print(f"user_verification_status={user_verification_status}")
    print(f"verified_fulltext={verified}")
    print(f"out={out_path}")
    return 0 if hands_free_ready else 1


if __name__ == "__main__":
    raise SystemExit(main())
