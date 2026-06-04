#!/usr/bin/env python3
"""Regression tests for external review status persistence."""

from __future__ import annotations

import importlib.util
import tempfile
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "external_review_orchestrator.py"
spec = importlib.util.spec_from_file_location("external_review_orchestrator", SCRIPT)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def make_run_dir() -> Path:
    root = Path(tempfile.mkdtemp(prefix="auto-cn-paper-status-test-"))
    (root / "15_外部评审与迭代计划.md").write_text(
        "\n".join(
            [
                "# 外部评审与迭代计划",
                "",
                "- external_review_passed: no",
                "- claude_opus_review_status: pending",
                "- gpt_pro_review_status: pending",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return root


def test_update_status_records_real_submission_metadata() -> None:
    run_dir = make_run_dir()
    summary = {
        "claude": {
            "status": "pass",
            "channel": "web_session",
            "real_submission": True,
            "raw_record": ".codex/advisor-runs/claude_raw.json",
        },
        "gpt_pro": {
            "status": "pass",
            "channel": "cli_or_api_real_call",
            "real_submission": True,
            "raw_record": ".codex/advisor-runs/gpt_raw.json",
        },
    }

    module.write_external_review_status_from_summary(run_dir, summary, run_dir / ".codex/advisor-runs/latest")

    text = (run_dir / "15_外部评审与迭代计划.md").read_text(encoding="utf-8")
    assert "- external_review_passed: no" in text
    assert "- claude_opus_review_status: pass" in text
    assert "- claude_opus_review_channel: web_session" in text
    assert "- claude_opus_real_submission: true" in text
    assert "- claude_opus_raw_record: .codex/advisor-runs/claude_raw.json" in text
    assert "- gpt_pro_review_status: pass" in text
    assert "- gpt_pro_review_channel: cli_or_api_real_call" in text
    assert "- gpt_pro_real_submission: true" in text
    assert "- gpt_pro_raw_record: .codex/advisor-runs/gpt_raw.json" in text


def main() -> int:
    try:
        test_update_status_records_real_submission_metadata()
    except AssertionError as exc:
        print(f"FAIL test_update_status_records_real_submission_metadata: {exc}")
        return 1
    except AttributeError as exc:
        print(f"FAIL test_update_status_records_real_submission_metadata: {exc}")
        return 1
    print("PASS test_update_status_records_real_submission_metadata")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
