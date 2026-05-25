from __future__ import annotations

import importlib.util
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BASE = ROOT / "run_batch32_claudecode_recheck_20260525.py"
spec = importlib.util.spec_from_file_location("run_batch32_helpers", BASE)
helpers = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(helpers)

PROMPT = ROOT / "OPUS47_CLAUDECODE_POST_REPAIR_IN_BODY_EVIDENCE_RECHECK_PROMPT_20260525.md"
RAW = ROOT / "OPUS47_CLAUDECODE_POST_REPAIR_IN_BODY_EVIDENCE_RECHECK_RAW.json"
STDERR = ROOT / "OPUS47_CLAUDECODE_POST_REPAIR_IN_BODY_EVIDENCE_RECHECK_STDERR.log"
DEBUG = ROOT / "OPUS47_CLAUDECODE_POST_REPAIR_IN_BODY_EVIDENCE_RECHECK_DEBUG.log"
EVIDENCE = ROOT / "OPUS47_CLAUDECODE_POST_REPAIR_IN_BODY_EVIDENCE_RUNTIME_EVIDENCE.json"
RESULT = ROOT / "OPUS47_CLAUDECODE_POST_REPAIR_IN_BODY_EVIDENCE_RECHECK_RESULT.md"
LEDGER = ROOT / "MODEL_EVIDENCE_LEDGER.md"


def append_model_ledger(evidence: dict, content_result: str, local_policy: str) -> None:
    ledger = LEDGER.read_text(encoding="utf-8") if LEDGER.exists() else "# MODEL_EVIDENCE_LEDGER\n"
    marker = "\n## OPUS47_POST_REPAIR_IN_BODY_EVIDENCE_RECHECK_20260525"
    if marker in ledger:
        ledger = ledger[: ledger.index(marker)]
    ledger += f"""

## OPUS47_POST_REPAIR_IN_BODY_EVIDENCE_RECHECK_20260525

- Purpose: post-repair review of current in-body evidence placement after Shijingshan Q16 removal and Xicheng Q20 formal pingbiao repair.
- Command: `claude -p --model claude-opus-4-7 --effort max --permission-mode auto --tools Read,Grep --output-format json --verbose --debug-file ... --no-session-persistence`.
- Prompt: `OPUS47_CLAUDECODE_POST_REPAIR_IN_BODY_EVIDENCE_RECHECK_PROMPT_20260525.md`.
- Raw JSON: `OPUS47_CLAUDECODE_POST_REPAIR_IN_BODY_EVIDENCE_RECHECK_RAW.json`.
- Runtime evidence: `OPUS47_CLAUDECODE_POST_REPAIR_IN_BODY_EVIDENCE_RUNTIME_EVIDENCE.json`.
- Result: `OPUS47_CLAUDECODE_POST_REPAIR_IN_BODY_EVIDENCE_RECHECK_RESULT.md`.
- Observed models: `{', '.join(evidence.get('models_observed', [])) or 'none'}`.
- Debug model mentions: `{', '.join(evidence.get('debug_model_mentions', [])) or 'none'}`.
- Thinking block/signature seen: `{str(evidence.get('thinking_block_seen', False)).lower()}`.
- Content result: `{content_result}`.
- Local policy result: `{local_policy}`.
- Model gate: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Boundary: Sonnet/Haiku/model-unknown output is not counted as qualified evidence; auxiliary model traces remain non-qualifying until independently confirmed acceptable.
"""
    LEDGER.write_text(ledger, encoding="utf-8", newline="\n")


def write_result(started: str, finished: str, return_code: int, timed_out: bool, result_text: str, evidence: dict, content_result: str, local_policy: str) -> None:
    RESULT.write_text(f"""# ClaudeCode Opus 4.7 Recheck Result - Post-Repair In-Body Evidence

status: `{local_policy}`

## Runtime Evidence

- Started: `{started}`.
- Finished: `{finished}`.
- Return code: `{return_code}`.
- Timed out: `{str(timed_out).lower()}`.
- Command: `claude -p --model claude-opus-4-7 --effort max --tools Read,Grep --output-format json --verbose`.
- Observed models: `{', '.join(evidence.get('models_observed', [])) or 'none'}`.
- Debug model mentions: `{', '.join(evidence.get('debug_model_mentions', [])) or 'none'}`.
- Thinking block/signature seen: `{str(evidence.get('thinking_block_seen', False)).lower()}`.
- Model gate: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

## ClaudeCode Verdict

{result_text}

## Local Policy Verdict

- `content_result`: `{content_result}`.
- `local_policy_result`: `{local_policy}`.
- Sonnet/Haiku/model-unknown evidence is not counted as qualified evidence.
- GPTPro web and Claude web/app external reviews remain `real_call_pending` unless separately captured.
- Whole-project status remains non-final.
""", encoding="utf-8", newline="\n")


def blocked(started: str, return_code: int, timed_out: bool, stderr_text: str, raw_text: str) -> int:
    finished = datetime.now().isoformat(timespec="seconds")
    evidence = {
        "models_observed": [],
        "debug_model_mentions": [],
        "thinking_block_seen": False,
        "started": started,
        "finished": finished,
        "return_code": return_code,
        "timed_out": timed_out,
        "model_gate": "BLOCKED_MODEL_CONFIRMATION_REQUIRED",
    }
    EVIDENCE.write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    excerpt = (stderr_text or raw_text)[:1600]
    write_result(started, finished, return_code, timed_out, excerpt or "No qualified ClaudeCode output was produced.", evidence, "blocked", "blocked")
    append_model_ledger(evidence, "blocked", "blocked")
    return 1


def main() -> int:
    prompt_text = PROMPT.read_text(encoding="utf-8")
    cmd = [
        "claude",
        "-p",
        "--model",
        "claude-opus-4-7",
        "--effort",
        "max",
        "--permission-mode",
        "auto",
        "--tools",
        "Read,Grep",
        "--output-format",
        "json",
        "--verbose",
        "--debug-file",
        str(DEBUG),
        "--no-session-persistence",
        prompt_text,
    ]
    started = datetime.now().isoformat(timespec="seconds")
    timed_out = False
    try:
        completed = subprocess.run(cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=1200, check=False)
        raw_text = (completed.stdout or b"").decode("utf-8", errors="replace")
        stderr_text = (completed.stderr or b"").decode("utf-8", errors="replace")
        return_code = completed.returncode
    except subprocess.TimeoutExpired as exc:
        timed_out = True
        raw_text = (exc.stdout or b"").decode("utf-8", errors="replace")
        stderr_text = (exc.stderr or b"").decode("utf-8", errors="replace")
        return_code = 124
    except FileNotFoundError as exc:
        RAW.write_text("", encoding="utf-8")
        STDERR.write_text(str(exc), encoding="utf-8")
        DEBUG.write_text("", encoding="utf-8")
        return blocked(started, 127, False, str(exc), "")

    finished = datetime.now().isoformat(timespec="seconds")
    RAW.write_text(raw_text, encoding="utf-8", newline="\n")
    STDERR.write_text(stderr_text, encoding="utf-8", newline="\n")
    if timed_out or return_code != 0 or not raw_text.strip():
        return blocked(started, return_code, timed_out, stderr_text, raw_text)

    debug_text = DEBUG.read_text(encoding="utf-8", errors="replace") if DEBUG.exists() else ""
    result_text, result_obj = helpers.parse_json_output(raw_text)
    evidence = helpers.parse_evidence(raw_text, debug_text, result_obj)
    evidence.update({
        "started": started,
        "finished": finished,
        "return_code": return_code,
        "timed_out": timed_out,
        "command": "claude -p --model claude-opus-4-7 --effort max --permission-mode auto --tools Read,Grep --output-format json --verbose --debug-file ... --no-session-persistence",
    })
    EVIDENCE.write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    content_result = helpers.detect_content_result(result_text)
    local_policy = "pass_with_model_gate_blocked" if content_result in {"pass", "pass_with_notes"} else "blocked_or_failed"
    write_result(started, finished, return_code, timed_out, result_text, evidence, content_result, local_policy)
    append_model_ledger(evidence, content_result, local_policy)
    print(json.dumps({"content_result": content_result, "local_policy": local_policy, "evidence": evidence}, ensure_ascii=False, indent=2))
    return 0 if content_result in {"pass", "pass_with_notes"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
