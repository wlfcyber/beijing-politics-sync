#!/usr/bin/env python3
"""Regression tests for Chrome CDP browser probing."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
PROBE_SCRIPT = SKILL_DIR / "scripts" / "chrome_cdp_probe.py"
BROWSER_GATE_SCRIPT = SKILL_DIR / "scripts" / "browser_gate_report.py"


def run_script(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def write_targets(path: Path) -> None:
    targets = [
        {
            "type": "page",
            "title": "中国知网",
            "url": "https://libproxy.ruc.edu.cn/https/77726476706e69737468656265737421f5f652d2243e635930068cb8/kns.cnki.net/kns8/defaultresult/index",
        },
        {
            "type": "background_page",
            "title": "Extension",
            "url": "chrome-extension://example/background.html",
        },
    ]
    path.write_text(json.dumps(targets, ensure_ascii=False), encoding="utf-8")


def test_chrome_cdp_probe_records_authorized_page() -> None:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-cdp-probe-"))
    targets_json = run_dir / "targets.json"
    write_targets(targets_json)

    result = run_script([str(PROBE_SCRIPT), str(run_dir), "--targets-json", str(targets_json)])

    assert result.returncode == 0, result.stdout
    out = run_dir / "chrome_cdp_probe.md"
    assert out.exists(), result.stdout
    text = out.read_text(encoding="utf-8")
    assert f"- run_id: {run_dir.name}" in text
    assert "- generated_at:" in text
    assert "- browser_path_status: pass" in text
    assert "- authorized_page_status: pass" in text
    assert "- highest_capability_tier: claim_url" in text
    assert "libproxy.ruc.edu.cn" in text
    assert "中国知网" in text


def test_browser_gate_uses_probe_report_when_status_args_unknown() -> None:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-browser-gate-probe-"))
    targets_json = run_dir / "targets.json"
    write_targets(targets_json)
    probe = run_script([str(PROBE_SCRIPT), str(run_dir), "--targets-json", str(targets_json)])
    assert probe.returncode == 0, probe.stdout

    (run_dir / "02_检索日志.md").write_text(
        "实际检索记录\n检索页 URL: https://libproxy.ruc.edu.cn/kns.cnki.net\n详情页: 已打开\n",
        encoding="utf-8",
    )
    (run_dir / "03_文献矩阵.md").write_text(
        "| 编号 | 标题 | 状态 |\n| --- | --- | --- |\n| S-001 | 示例论文 | PDF_or_user_exported |\n",
        encoding="utf-8",
    )
    (run_dir / "source_inventory.md").write_text("source_count: 1\n", encoding="utf-8")

    result = run_script([str(BROWSER_GATE_SCRIPT), str(run_dir), "--user-verification-status", "pass"])

    assert result.returncode == 0, result.stdout
    text = (run_dir / "12_浏览器准入验收.md").read_text(encoding="utf-8")
    assert "- hands_free_ready: yes" in text
    assert "- browser_path_status: pass" in text
    assert "- current_url_status: pass" in text
    assert "Chrome CDP 探针" in text


def test_browser_gate_rejects_probe_from_other_run() -> None:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-browser-gate-current-"))
    other_run = Path(tempfile.mkdtemp(prefix="auto-cn-paper-browser-gate-other-"))
    targets_json = other_run / "targets.json"
    write_targets(targets_json)
    probe = run_script([str(PROBE_SCRIPT), str(other_run), "--targets-json", str(targets_json)])
    assert probe.returncode == 0, probe.stdout

    (run_dir / "02_检索日志.md").write_text(
        "实际检索记录\n检索页 URL: https://libproxy.ruc.edu.cn/kns.cnki.net\n详情页: 已打开\n",
        encoding="utf-8",
    )
    (run_dir / "03_文献矩阵.md").write_text(
        "| 编号 | 标题 | 状态 |\n| --- | --- | --- |\n| S-001 | 示例论文 | PDF_or_user_exported |\n",
        encoding="utf-8",
    )
    (run_dir / "source_inventory.md").write_text("source_count: 1\n", encoding="utf-8")

    result = run_script(
        [
            str(BROWSER_GATE_SCRIPT),
            str(run_dir),
            "--probe-report",
            str(other_run / "chrome_cdp_probe.md"),
            "--user-verification-status",
            "pass",
        ]
    )

    assert result.returncode == 1, result.stdout
    text = (run_dir / "12_浏览器准入验收.md").read_text(encoding="utf-8")
    assert "- probe_run_id_status: mismatch" in text
    assert "- current_url_status: unknown" in text
    assert "probe run_id mismatch" in text


def test_login_page_forces_waiting_user_not_authorized_pass() -> None:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-cdp-login-"))
    targets = [
        {
            "type": "page",
            "title": "登录 - 中国人民大学",
            "url": "https://v.ruc.edu.cn/account/login?redirect_uri=https%3A%2F%2Flibproxy.ruc.edu.cn%2FermsLogin%2FSSOLoginResult.do",
        },
        {
            "type": "page",
            "title": "电子资源平台",
            "url": "https://libproxy.ruc.edu.cn/ermsClient/eresourceInfo.do?rid=114",
        },
    ]
    targets_json = run_dir / "targets.json"
    targets_json.write_text(json.dumps(targets, ensure_ascii=False), encoding="utf-8")

    result = run_script([str(PROBE_SCRIPT), str(run_dir), "--targets-json", str(targets_json)])

    assert result.returncode == 1, result.stdout
    text = (run_dir / "chrome_cdp_probe.md").read_text(encoding="utf-8")
    assert "- authorized_page_status: waiting_user" in text
    assert "- user_action_status: waiting_user" in text
    assert "- selected_title: 登录 - 中国人民大学" in text

    gate = run_script([str(BROWSER_GATE_SCRIPT), str(run_dir)])
    assert gate.returncode == 1, gate.stdout
    gate_text = (run_dir / "12_浏览器准入验收.md").read_text(encoding="utf-8")
    assert "- current_url_status: waiting_user" in gate_text
    assert "- user_verification_status: waiting_user" in gate_text


def test_cnki_security_verify_forces_waiting_user() -> None:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-cdp-verify-"))
    targets = [
        {
            "type": "page",
            "title": "安全验证",
            "url": "https://example.libproxy.ruc.edu.cn/verify/home?captchaType=blockPuzzle&captchaId=abc",
        },
        {
            "type": "page",
            "title": "中国知网",
            "url": "https://example.libproxy.ruc.edu.cn/kns8s/search",
        },
    ]
    targets_json = run_dir / "targets.json"
    targets_json.write_text(json.dumps(targets, ensure_ascii=False), encoding="utf-8")

    result = run_script([str(PROBE_SCRIPT), str(run_dir), "--targets-json", str(targets_json)])

    assert result.returncode == 1, result.stdout
    text = (run_dir / "chrome_cdp_probe.md").read_text(encoding="utf-8")
    assert "- authorized_page_status: waiting_user" in text
    assert "- user_action_status: waiting_user" in text
    assert "- selected_title: 安全验证" in text


def main() -> int:
    tests = [
        test_chrome_cdp_probe_records_authorized_page,
        test_browser_gate_uses_probe_report_when_status_args_unknown,
        test_browser_gate_rejects_probe_from_other_run,
        test_login_page_forces_waiting_user_not_authorized_pass,
        test_cnki_security_verify_forces_waiting_user,
    ]
    for test in tests:
        try:
            test()
        except AssertionError as exc:
            print(f"FAIL {test.__name__}: {exc}")
            return 1
    print("PASS test_chrome_cdp_probe_records_authorized_page")
    print("PASS test_browser_gate_uses_probe_report_when_status_args_unknown")
    print("PASS test_browser_gate_rejects_probe_from_other_run")
    print("PASS test_login_page_forces_waiting_user_not_authorized_pass")
    print("PASS test_cnki_security_verify_forces_waiting_user")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
