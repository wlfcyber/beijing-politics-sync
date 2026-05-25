from __future__ import annotations

import json
import re
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PROMPT = ROOT / "OPUS47_CLAUDECODE_BATCH23_2025_CHAOYANG_FINAL_RECHECK_PROMPT.md"
RAW = ROOT / "OPUS47_CLAUDECODE_BATCH23_2025_CHAOYANG_FINAL_RECHECK_STREAM_RAW_UTF8.jsonl"
STDERR = ROOT / "OPUS47_CLAUDECODE_BATCH23_2025_CHAOYANG_FINAL_RECHECK_STREAM_UTF8_STDERR.log"
DEBUG = ROOT / "OPUS47_CLAUDECODE_BATCH23_2025_CHAOYANG_FINAL_RECHECK_STREAM_UTF8_DEBUG.log"
EVIDENCE = ROOT / "OPUS47_CLAUDECODE_BATCH23_2025_CHAOYANG_FINAL_RUNTIME_EVIDENCE.json"
RESULT = ROOT / "OPUS47_CLAUDECODE_BATCH23_2025_CHAOYANG_FINAL_RECHECK_RESULT.md"
MODEL_LEDGER = ROOT / "MODEL_EVIDENCE_LEDGER.md"
GOVERNOR = ROOT / "GOVERNOR_RECOVERY_REPORT_20260524.md"
THREAD_STATUS = ROOT / "THREAD_RECOVERY_STATUS_20260524.md"
CONFUCIUS = ROOT / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"
BATCH_REPORT = ROOT / "COVERAGE_FUSION_BATCH23_2025_CHAOYANG_FINAL_CODEX_20260525.md"


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
        r"content_result`?\s*[:：]\s*`?([a-z_]+)",
        r"content result`?\s*[:：]\s*`?([a-z_]+)",
        r"\bcontent_result\b.*?\b(pass_with_notes|pass|fail|blocked)\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, lowered, re.DOTALL)
        if match:
            value = match.group(1)
            if value in {"pass", "pass_with_notes", "fail", "blocked"}:
                return value
    if "pass_with_notes" in lowered:
        return "pass_with_notes"
    if re.search(r"\bpass\b", lowered):
        return "pass"
    if "blocked" in lowered:
        return "blocked"
    if "fail" in lowered:
        return "fail"
    return "blocked"


def extract_final_text(raw_bytes: bytes) -> str:
    chunks = []
    for line in raw_bytes.decode("utf-8", errors="replace").splitlines():
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(obj, dict):
            continue
        if obj.get("type") == "assistant":
            msg = obj.get("message")
            if isinstance(msg, dict):
                for block in msg.get("content", []):
                    if isinstance(block, dict) and block.get("type") == "text":
                        chunks.append(block.get("text", ""))
        if obj.get("type") == "content_block_delta":
            delta = obj.get("delta")
            if isinstance(delta, dict) and isinstance(delta.get("text"), str):
                chunks.append(delta["text"])
    return "".join(chunks).strip()


def parse_stream(raw_bytes: bytes, debug_text: str) -> dict:
    text = raw_bytes.decode("utf-8", errors="replace")
    models = set()
    debug_models = set(re.findall(r"claude-[a-z0-9-]+", debug_text.lower()))
    json_lines = 0
    result_obj = None
    collected = []

    for line in text.splitlines():
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            collected.append(line)
            continue
        json_lines += 1
        for s in collect_strings(obj):
            collected.append(s)
            for model in re.findall(r"claude-[a-z0-9-]+", s.lower()):
                models.add(model)
        if isinstance(obj, dict):
            if obj.get("type") == "result":
                result_obj = obj
            model = obj.get("model")
            if isinstance(model, str):
                models.add(model.lower())
            msg = obj.get("message")
            if isinstance(msg, dict) and isinstance(msg.get("model"), str):
                models.add(msg["model"].lower())

    full_text = "\n".join(collected)
    thinking = bool(re.search(r"\bthinking(_delta)?\b|signature", text.lower()))
    content_result = detect_content_result(full_text)
    local_policy = "pass_with_model_gate_blocked" if content_result in {"pass", "pass_with_notes"} else content_result
    summary = None
    if isinstance(result_obj, dict):
        summary = {
            key: result_obj.get(key)
            for key in [
                "type",
                "subtype",
                "duration_ms",
                "duration_api_ms",
                "is_error",
                "num_turns",
                "session_id",
            ]
            if key in result_obj
        }
    return {
        "models_observed": sorted(models),
        "debug_model_mentions": sorted(debug_models),
        "thinking_block_seen": thinking,
        "stderr_bytes": STDERR.stat().st_size if STDERR.exists() else 0,
        "raw_bytes": len(raw_bytes),
        "json_lines": json_lines,
        "result_obj_summary": summary,
        "content_result_detected": content_result,
        "local_policy_result": local_policy,
        "model_gate": "BLOCKED_MODEL_CONFIRMATION_REQUIRED",
    }


def write_result(evidence: dict, final_text: str) -> None:
    result = evidence["content_result_detected"]
    local_policy = evidence["local_policy_result"]
    lines = [
        "# ClaudeCode Batch23 Recheck Result - 2025 Chaoyang Final",
        "",
        "Parsed from raw stream:",
        "",
        "- `OPUS47_CLAUDECODE_BATCH23_2025_CHAOYANG_FINAL_RECHECK_STREAM_RAW_UTF8.jsonl`",
        "- `OPUS47_CLAUDECODE_BATCH23_2025_CHAOYANG_FINAL_RUNTIME_EVIDENCE.json`",
        "",
        "## Result",
        "",
        f"- `content_result`: `{result}`",
        f"- `local_policy_result`: `{local_policy}`",
        "- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`",
        "- `required_fixes`: see ClaudeCode final response below.",
        "",
        "## Evidence Checked",
        "",
        "- Matrix target: Batch23 should have `41` rows, `21` body rows, `20` boundary rows.",
        "- Body target: `21` governed DOCX entries for Q2, Q9, Q16, and Q22.",
        "- Render target: `254/254` pages/images, labels `2375/2375`, visible suite headings `21/21`.",
        "- Ledger target: `21` governed records in both `docx_insert_ledger.csv` and `student_patch_entries.accepted.jsonl`.",
        "- Global scope target: remaining raw midterm/final source gap `12` suites.",
        "",
        "## Model Evidence Boundary",
        "",
        f"- Runtime observed models: `{', '.join(evidence['models_observed']) or 'none'}`.",
        "- Command lane used `--model claude-opus-4-7 --effort max`.",
        f"- Stream thinking block/signature seen: `{str(evidence['thinking_block_seen']).lower()}`.",
        f"- Debug model mentions: `{', '.join(evidence['debug_model_mentions']) or 'none'}`.",
        "- Sonnet/Haiku/model-unknown output is not counted as qualified evidence.",
        "- Machine-readable adaptive/max-effort proof is still insufficient, so the model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.",
        "",
        "## ClaudeCode Final Response",
        "",
        final_text.strip() or "_No final text extracted from stream._",
        "",
    ]
    RESULT.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def append_status(evidence: dict) -> None:
    content = evidence["content_result_detected"]
    local = evidence["local_policy_result"]
    append = f"""

## Batch23 ClaudeCode Opus 4.7 Recheck: 2025朝阳期末
Updated: 2026-05-25

- Runtime command: `claude -p --model claude-opus-4-7 --effort max --output-format stream-json --verbose`.
- `content_result`: `{content}`.
- `local_policy_result`: `{local}`.
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Observed models: `{', '.join(evidence['models_observed']) or 'none'}`.
- Thinking block/signature seen: `{str(evidence['thinking_block_seen']).lower()}`.
- Sonnet/Haiku/model-unknown evidence is not counted as qualified ClaudeCode evidence.
- Result artifact: `OPUS47_CLAUDECODE_BATCH23_2025_CHAOYANG_FINAL_RECHECK_RESULT.md`.
"""
    for path in [THREAD_STATUS, GOVERNOR, CONFUCIUS]:
        text = path.read_text(encoding="utf-8")
        marker = "\n## Batch23 ClaudeCode Opus 4.7 Recheck: 2025朝阳期末"
        if marker in text:
            text = text[: text.index(marker)]
        path.write_text(text + append, encoding="utf-8")

    ledger = MODEL_LEDGER.read_text(encoding="utf-8")
    marker = "\n## OPUS47_BATCH23_CHAOYANG_FINAL_RECHECK_001"
    if marker in ledger:
        ledger = ledger[: ledger.index(marker)]
    ledger += f"""

## OPUS47_BATCH23_CHAOYANG_FINAL_RECHECK_001

- Batch: `2025朝阳期末`.
- Command: `claude -p --model claude-opus-4-7 --effort max --output-format stream-json --verbose`.
- Raw stream: `OPUS47_CLAUDECODE_BATCH23_2025_CHAOYANG_FINAL_RECHECK_STREAM_RAW_UTF8.jsonl`.
- Runtime evidence: `OPUS47_CLAUDECODE_BATCH23_2025_CHAOYANG_FINAL_RUNTIME_EVIDENCE.json`.
- Result: `OPUS47_CLAUDECODE_BATCH23_2025_CHAOYANG_FINAL_RECHECK_RESULT.md`.
- Observed models: `{', '.join(evidence['models_observed']) or 'none'}`.
- Thinking block/signature seen: `{str(evidence['thinking_block_seen']).lower()}`.
- Content result: `{content}`.
- Local policy result: `{local}`.
- Model gate: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Boundary: Sonnet/Haiku/model-unknown output is not counted as qualified evidence; auxiliary model usage, if any, remains non-qualifying.
"""
    MODEL_LEDGER.write_text(ledger, encoding="utf-8")

    report = BATCH_REPORT.read_text(encoding="utf-8")
    if content in {"pass", "pass_with_notes"}:
        report = report.replace("Status: `LOCAL_APPLIED_RENDER_PASS_MODEL_PENDING`", "Status: `LOCAL_CLOSED_CONTENT_PASS_WITH_MODEL_GATE_BLOCKED`")
    marker = "\n## ClaudeCode Recheck Result"
    if marker in report:
        report = report[: report.index(marker)]
    report += f"""

## ClaudeCode Recheck Result

- `content_result`: `{content}`.
- `local_policy_result`: `{local}`.
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Result artifact: `OPUS47_CLAUDECODE_BATCH23_2025_CHAOYANG_FINAL_RECHECK_RESULT.md`.
"""
    BATCH_REPORT.write_text(report, encoding="utf-8")


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
        "--output-format",
        "stream-json",
        "--verbose",
        "--debug-file",
        str(DEBUG),
        "--no-session-persistence",
    ]
    started = datetime.now().isoformat(timespec="seconds")
    timed_out = False
    try:
        completed = subprocess.run(
            cmd,
            cwd=ROOT,
            input=prompt_text.encode("utf-8"),
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
    debug_text = DEBUG.read_text(encoding="utf-8", errors="replace") if DEBUG.exists() else ""
    evidence = parse_stream(raw_bytes, debug_text)
    evidence.update(
        {
            "started": started,
            "finished": datetime.now().isoformat(timespec="seconds"),
            "timed_out": timed_out,
            "return_code": return_code,
            "command": cmd,
        }
    )
    EVIDENCE.write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8")
    final_text = extract_final_text(raw_bytes)
    write_result(evidence, final_text)
    append_status(evidence)
    print(json.dumps(evidence, ensure_ascii=False, indent=2))
    return 0 if not timed_out else 124


if __name__ == "__main__":
    raise SystemExit(main())

