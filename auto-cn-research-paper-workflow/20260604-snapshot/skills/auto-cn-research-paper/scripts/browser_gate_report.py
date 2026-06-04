#!/usr/bin/env python3
"""Write a browser-access gate report for an automated CN research-paper run."""

from __future__ import annotations

import argparse
import re
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
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    out_path = Path(args.out).expanduser().resolve() if args.out else run_dir / "12_浏览器准入验收.md"

    search_text = read(run_dir / "02_检索日志.md")
    matrix_text = read(run_dir / "03_文献矩阵.md")
    inventory_text = read(run_dir / "source_inventory.md")
    queue_text = read(run_dir / "10_候选下载队列.md")
    audit_text = read(run_dir / "09_完成度审计.md")

    verified = count_verified_sources(matrix_text)
    ruc_route = "pass" if ("libproxy.ruc.edu.cn" in search_text or "人大图书馆" in search_text) else "fail"
    search_status = "pass" if re.search(r"主题=`|检索页 URL|实际检索记录", search_text) else "fail"
    detail_status = "pass" if "详情页" in search_text else "fail"
    fulltext_status = "pass" if verified else "blocked"
    ledger_status = "pass" if matrix_text and inventory_text else "fail"
    waiting_terms_present = any(term in queue_text or term in audit_text or term in search_text for term in CAPTCHA_TERMS)

    user_verification_status = args.user_verification_status
    if user_verification_status == "unknown" and waiting_terms_present:
        user_verification_status = "waiting_user"

    checks = {
        "browser_path": args.browser_path_status,
        "current_url": args.current_url_status,
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
        f"- hands_free_ready: {'yes' if hands_free_ready else 'no'}",
        f"- verified_fulltext: {verified}",
        f"- browser_path_status: {args.browser_path_status}",
        f"- current_url_status: {args.current_url_status}",
        f"- computer_use_status: {args.computer_use_status}",
        f"- user_verification_status: {user_verification_status}",
        "",
        "## 检查项",
        "",
        "| 检查项 | 状态 | 证据 |",
        "| --- | --- | --- |",
        f"| Chrome/浏览器控制路径 | {status_line(args.browser_path_status, args.browser_path_note)}",
        f"| 当前 URL 可确认 | {status_line(args.current_url_status, args.current_url_note)}",
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
    print(f"browser_path_status={args.browser_path_status}")
    print(f"current_url_status={args.current_url_status}")
    print(f"computer_use_status={args.computer_use_status}")
    print(f"user_verification_status={user_verification_status}")
    print(f"verified_fulltext={verified}")
    print(f"out={out_path}")
    return 0 if hands_free_ready else 1


if __name__ == "__main__":
    raise SystemExit(main())
