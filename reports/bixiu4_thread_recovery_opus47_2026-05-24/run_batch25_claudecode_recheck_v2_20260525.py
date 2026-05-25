from __future__ import annotations

import json
import re
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PROMPT = ROOT / "OPUS47_CLAUDECODE_BATCH25_2025_HAIDIAN_FINAL_RECHECK_PROMPT_V2.md"
RAW = ROOT / "OPUS47_CLAUDECODE_BATCH25_2025_HAIDIAN_FINAL_RECHECK_V2_RAW.json"
STDERR = ROOT / "OPUS47_CLAUDECODE_BATCH25_2025_HAIDIAN_FINAL_RECHECK_V2_STDERR.log"
DEBUG = ROOT / "OPUS47_CLAUDECODE_BATCH25_2025_HAIDIAN_FINAL_RECHECK_V2_DEBUG.log"
EVIDENCE = ROOT / "OPUS47_CLAUDECODE_BATCH25_2025_HAIDIAN_FINAL_RUNTIME_EVIDENCE_V2.json"
RESULT = ROOT / "OPUS47_CLAUDECODE_BATCH25_2025_HAIDIAN_FINAL_RECHECK_RESULT_V2.md"
MODEL_LEDGER = ROOT / "MODEL_EVIDENCE_LEDGER.md"
GOVERNOR = ROOT / "GOVERNOR_RECOVERY_REPORT_20260524.md"
THREAD_STATUS = ROOT / "THREAD_RECOVERY_STATUS_20260524.md"
CONFUCIUS = ROOT / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"
BATCH_REPORT = ROOT / "COVERAGE_FUSION_BATCH25_2025_HAIDIAN_FINAL_CODEX_20260525.md"
GLOBAL_AUDIT = ROOT / "GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv"


def collect_strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from collect_strings(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from collect_strings(item)


def detect_content_result(text: str) -> str:
    lowered = text.lower()
    patterns = [
        r"`content_result`\s*:\s*`?(pass_with_notes|pass|fail|blocked)`?",
        r"content_result\s*:\s*`?(pass_with_notes|pass|fail|blocked)`?",
        r"content result\s*:\s*`?(pass_with_notes|pass|fail|blocked)`?",
    ]
    for pattern in patterns:
        match = re.search(pattern, lowered)
        if match:
            return match.group(1)
    if "pass_with_notes" in lowered:
        return "pass_with_notes"
    if re.search(r"\bpass\b", lowered):
        return "pass"
    if "fail" in lowered:
        return "fail"
    return "blocked"


def parse_json_output(raw_text: str) -> tuple[str, dict]:
    result_text = ""
    result_obj = {}
    try:
        result_obj = json.loads(raw_text)
    except json.JSONDecodeError:
        return raw_text, result_obj
    if isinstance(result_obj, dict):
        for key in ["result", "message", "text", "content"]:
            value = result_obj.get(key)
            if isinstance(value, str):
                result_text = value
                break
        if not result_text:
            result_text = json.dumps(result_obj, ensure_ascii=False, indent=2)
    return result_text, result_obj if isinstance(result_obj, dict) else {}


def parse_evidence(raw_text: str, debug_text: str, result_obj: dict) -> dict:
    models = set()
    for s in collect_strings(result_obj):
        for model in re.findall(r"claude-[a-z0-9-]+", s.lower()):
            models.add(model)
    for model in re.findall(r"claude-[a-z0-9-]+", debug_text.lower()):
        models.add(model)
    if result_obj.get("model"):
        models.add(str(result_obj["model"]).lower())
    return {
        "models_observed": sorted(models),
        "debug_model_mentions": sorted(set(re.findall(r"claude-[a-z0-9-]+", debug_text.lower()))),
        "thinking_block_seen": bool(re.search(r"\bthinking(_delta)?\b|signature", raw_text.lower() + debug_text.lower())),
        "result_obj_summary": {
            key: result_obj.get(key)
            for key in ["type", "subtype", "duration_ms", "duration_api_ms", "is_error", "num_turns", "session_id", "total_cost_usd"]
            if key in result_obj
        },
        "model_gate": "BLOCKED_MODEL_CONFIRMATION_REQUIRED",
    }


def replace_batch_report(content: str, final_status: str, evidence: dict, content_result: str, local_policy: str) -> str:
    content = re.sub(r"Status: `[^`]+`", f"Status: `{final_status}`", content, count=1)
    content = content.replace("ClaudeCode Opus 4.7 recheck is pending.", f"ClaudeCode Opus 4.7 V2 recheck result is `{content_result}`.")
    content = content.replace("Render QA is pending because Batch25 modified the DOCX.", "Render QA passed after Batch25 DOCX modification.")
    marker = "\n## ClaudeCode Recheck Result"
    if marker in content:
        content = content[: content.index(marker)]
    content += f"""

## ClaudeCode Recheck Result

- V1 stream result: `blocked` because the stream stopped before a final conclusion; not counted as content pass evidence.
- V2 result artifact: `OPUS47_CLAUDECODE_BATCH25_2025_HAIDIAN_FINAL_RECHECK_RESULT_V2.md`.
- `content_result`: `{content_result}`.
- `local_policy_result`: `{local_policy}`.
- `batch25_status`: `{final_status}`.
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Observed models: `{', '.join(evidence['models_observed']) or 'none'}`.
- Debug model mentions: `{', '.join(evidence['debug_model_mentions']) or 'none'}`.
- Whole-project status remains non-final.
"""
    return content


def append_status(evidence: dict, content_result: str, local_policy: str) -> None:
    final_status = (
        "LOCAL_CLOSED_CONTENT_RENDER_PASS_WITH_MODEL_GATE_BLOCKED"
        if content_result in {"pass", "pass_with_notes"}
        else "LOCAL_RECHECK_FAILED_OR_BLOCKED"
    )
    appendix = f"""

## Batch25 ClaudeCode Opus 4.7 Recheck V2: 2025海淀期末
Updated: 2026-05-25

- V1 stream result: `blocked` because it stopped before a final conclusion; not counted as content pass evidence.
- Runtime command: `claude -p --model claude-opus-4-7 --effort max --tools Read,Grep --output-format json --verbose`.
- `content_result`: `{content_result}`.
- `local_policy_result`: `{local_policy}`.
- `batch25_status`: `{final_status}`.
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Observed models: `{', '.join(evidence['models_observed']) or 'none'}`.
- Debug model mentions: `{', '.join(evidence['debug_model_mentions']) or 'none'}`.
- Thinking block/signature seen: `{str(evidence['thinking_block_seen']).lower()}`.
- Sonnet/Haiku/model-unknown evidence is not counted as qualified ClaudeCode evidence.
- Result artifact: `OPUS47_CLAUDECODE_BATCH25_2025_HAIDIAN_FINAL_RECHECK_RESULT_V2.md`.
"""
    for path in [THREAD_STATUS, GOVERNOR, CONFUCIUS]:
        text = path.read_text(encoding="utf-8")
        text = text.replace("LOCAL_APPLIED_RENDER_PASS_MODEL_PENDING", final_status)
        text = text.replace("LOCAL_RECHECK_FAILED_OR_BLOCKED", final_status)
        marker = "\n## Batch25 ClaudeCode Opus 4.7 Recheck"
        if marker in text:
            text = text[: text.index(marker)]
        path.write_text(text + appendix, encoding="utf-8", newline="\n")

    ledger = MODEL_LEDGER.read_text(encoding="utf-8")
    pending_pattern = (
        r"\n## CLAUDECODE_BATCH25_HAIDIAN_FINAL_RECHECK\n\n"
        r"status: `(?:real_call_pending|superseded_by_real_call)`.*?(?=\n## |\Z)"
    )
    ledger = re.sub(
        pending_pattern,
        """

## CLAUDECODE_BATCH25_HAIDIAN_FINAL_RECHECK

status: `superseded_by_real_call`

- Superseded by `OPUS47_BATCH25_HAIDIAN_FINAL_RECHECK_001` and V2 completion `OPUS47_BATCH25_HAIDIAN_FINAL_RECHECK_002`.
- The earlier pending placeholder is not used as evidence.
""",
        ledger,
        flags=re.DOTALL,
    )
    marker = "\n## OPUS47_BATCH25_HAIDIAN_FINAL_RECHECK_002"
    if marker in ledger:
        ledger = ledger[: ledger.index(marker)]
    ledger += f"""

## OPUS47_BATCH25_HAIDIAN_FINAL_RECHECK_002

- Batch: `2025海淀期末`.
- Command: `claude -p --model claude-opus-4-7 --effort max --tools Read,Grep --output-format json --verbose`.
- Prompt: `OPUS47_CLAUDECODE_BATCH25_2025_HAIDIAN_FINAL_RECHECK_PROMPT_V2.md`.
- Raw JSON: `OPUS47_CLAUDECODE_BATCH25_2025_HAIDIAN_FINAL_RECHECK_V2_RAW.json`.
- Runtime evidence: `OPUS47_CLAUDECODE_BATCH25_2025_HAIDIAN_FINAL_RUNTIME_EVIDENCE_V2.json`.
- Result: `OPUS47_CLAUDECODE_BATCH25_2025_HAIDIAN_FINAL_RECHECK_RESULT_V2.md`.
- Observed models: `{', '.join(evidence['models_observed']) or 'none'}`.
- Debug model mentions: `{', '.join(evidence['debug_model_mentions']) or 'none'}`.
- Thinking block/signature seen: `{str(evidence['thinking_block_seen']).lower()}`.
- Content result: `{content_result}`.
- Local policy result: `{local_policy}`.
- Model gate: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Boundary: Sonnet/Haiku/model-unknown output is not counted as qualified evidence; auxiliary model usage, if any, remains non-qualifying.
"""
    MODEL_LEDGER.write_text(ledger, encoding="utf-8", newline="\n")

    report = BATCH_REPORT.read_text(encoding="utf-8")
    BATCH_REPORT.write_text(replace_batch_report(report, final_status, evidence, content_result, local_policy), encoding="utf-8", newline="\n")

    if GLOBAL_AUDIT.exists():
        text = GLOBAL_AUDIT.read_text(encoding="utf-8")
        text = text.replace(
            "Batch25 matrix/DOCX/render pass; ClaudeCode Opus 4.7 model-lane recheck pending.",
            f"Batch25 matrix/DOCX/render pass; ClaudeCode V2 content_result={content_result}; model gate remains BLOCKED_MODEL_CONFIRMATION_REQUIRED.",
        )
        GLOBAL_AUDIT.write_text(text, encoding="utf-8", newline="\n")


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
        completed = subprocess.run(
            cmd,
            cwd=ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=1200,
            check=False,
        )
        raw_bytes = completed.stdout or b""
        stderr_bytes = completed.stderr or b""
        return_code = completed.returncode
    except subprocess.TimeoutExpired as exc:
        timed_out = True
        raw_bytes = exc.stdout or b""
        stderr_bytes = exc.stderr or b""
        return_code = 124

    RAW.write_bytes(raw_bytes)
    STDERR.write_bytes(stderr_bytes)
    raw_text = raw_bytes.decode("utf-8", errors="replace")
    result_text, result_obj = parse_json_output(raw_text)
    debug_text = DEBUG.read_text(encoding="utf-8", errors="replace") if DEBUG.exists() else ""
    evidence = parse_evidence(raw_text, debug_text, result_obj)
    content_result = "blocked" if timed_out or return_code != 0 else detect_content_result(result_text)
    local_policy = "pass_with_model_gate_blocked" if content_result in {"pass", "pass_with_notes"} else content_result
    evidence.update(
        {
            "content_result_detected": content_result,
            "local_policy_result": local_policy,
            "started": started,
            "finished": datetime.now().isoformat(timespec="seconds"),
            "timed_out": timed_out,
            "return_code": return_code,
            "command": cmd[:-1] + ["<prompt_text>"],
            "raw_bytes": len(raw_bytes),
            "stderr_bytes": len(stderr_bytes),
        }
    )
    EVIDENCE.write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")

    RESULT.write_text(
        "\n".join(
            [
                "# ClaudeCode Batch25 Recheck Result V2 - 2025 Haidian Final",
                "",
                f"- `content_result`: `{content_result}`",
                f"- `local_policy_result`: `{local_policy}`",
                "- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`",
                f"- `return_code`: `{return_code}`",
                f"- `timed_out`: `{str(timed_out).lower()}`",
                f"- Observed models: `{', '.join(evidence['models_observed']) or 'none'}`",
                f"- Debug model mentions: `{', '.join(evidence['debug_model_mentions']) or 'none'}`",
                f"- Thinking block/signature seen: `{str(evidence['thinking_block_seen']).lower()}`",
                "",
                "## ClaudeCode Final Response",
                "",
                result_text.strip() or "_No final text extracted._",
                "",
            ]
        ),
        encoding="utf-8",
        newline="\n",
    )
    append_status(evidence, content_result, local_policy)
    print(json.dumps(evidence, ensure_ascii=False, indent=2))
    return 0 if not timed_out and return_code == 0 else return_code


if __name__ == "__main__":
    raise SystemExit(main())
