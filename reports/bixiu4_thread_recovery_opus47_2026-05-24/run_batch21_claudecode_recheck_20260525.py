from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PROMPT = ROOT / "OPUS47_CLAUDECODE_BATCH21_2025_DONGCHENG_FINAL_RECHECK_PROMPT.md"
RAW = ROOT / "OPUS47_CLAUDECODE_BATCH21_2025_DONGCHENG_FINAL_RECHECK_STREAM_RAW_UTF8.jsonl"
STDERR = ROOT / "OPUS47_CLAUDECODE_BATCH21_2025_DONGCHENG_FINAL_RECHECK_STREAM_UTF8_STDERR.log"
DEBUG = ROOT / "OPUS47_CLAUDECODE_BATCH21_2025_DONGCHENG_FINAL_RECHECK_STREAM_UTF8_DEBUG.log"
EVIDENCE = ROOT / "OPUS47_CLAUDECODE_BATCH21_2025_DONGCHENG_FINAL_RUNTIME_EVIDENCE.json"
RESULT = ROOT / "OPUS47_CLAUDECODE_BATCH21_2025_DONGCHENG_FINAL_RECHECK_RESULT.md"


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
    final_text = final_text.strip()
    result = evidence["content_result_detected"]
    local_policy = evidence["local_policy_result"]
    lines = [
        "# ClaudeCode Batch21 Recheck Result - 2025 Dongcheng Final",
        "",
        "Parsed from raw stream:",
        "",
        "- `OPUS47_CLAUDECODE_BATCH21_2025_DONGCHENG_FINAL_RECHECK_STREAM_RAW_UTF8.jsonl`",
        "- `OPUS47_CLAUDECODE_BATCH21_2025_DONGCHENG_FINAL_RUNTIME_EVIDENCE.json`",
        "",
        "## Result",
        "",
        f"- `content_result`: `{result}`",
        f"- `local_policy_result`: `{local_policy}`",
        "- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`",
        "- `required_fixes`: see ClaudeCode final response below; none recorded by parser if `content_result` is pass/pass_with_notes.",
        "",
        "## Evidence Checked",
        "",
        "- Matrix target: Batch21 should have `25` rows, covering Q1-Q21/subparts.",
        "- Body target: four governed DOCX entries for Q4, Q16, Q21 value judgment, and Q21 people.",
        "- Render target: `249/249` pages/images, labels `2315/2315`, visible suite mentions `4/4`, pages `20, 127, 216, 233`.",
        "- Ledger target: four governed records in both `docx_insert_ledger.csv` and `student_patch_entries.accepted.jsonl`.",
        "- Global scope target: remaining raw midterm/final source gap `14` suites.",
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
        final_text or "_No final text extracted from stream._",
        "",
    ]
    RESULT.write_text("\n".join(lines), encoding="utf-8", newline="\n")


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
        return_code = -1

    RAW.write_bytes(raw_bytes)
    STDERR.write_bytes(stderr_bytes)
    debug_text = DEBUG.read_text(encoding="utf-8", errors="replace") if DEBUG.exists() else ""
    evidence = parse_stream(raw_bytes, debug_text)
    evidence.update(
        {
            "command": " ".join(cmd) + " < " + PROMPT.name,
            "started_at": started,
            "finished_at": datetime.now().isoformat(timespec="seconds"),
            "return_code": return_code,
            "timed_out": timed_out,
            "prompt": PROMPT.name,
            "raw_artifact": RAW.name,
            "stderr_artifact": STDERR.name,
            "debug_artifact": DEBUG.name,
            "result_artifact": RESULT.name,
        }
    )
    EVIDENCE.write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    write_result(evidence, extract_final_text(raw_bytes))
    print(json.dumps(evidence, ensure_ascii=False, indent=2))
    return 1 if timed_out else 0


if __name__ == "__main__":
    sys.exit(main())
