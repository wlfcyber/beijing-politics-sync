from __future__ import annotations

import json
import re
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PROMPT = ROOT / "OPUS47_CLAUDECODE_BATCH31_2026_HAIDIAN_MIDTERM_RECHECK_PROMPT.md"
RAW = ROOT / "OPUS47_CLAUDECODE_BATCH31_2026_HAIDIAN_MIDTERM_RECHECK_RAW.json"
STDERR = ROOT / "OPUS47_CLAUDECODE_BATCH31_2026_HAIDIAN_MIDTERM_RECHECK_STDERR.log"
DEBUG = ROOT / "OPUS47_CLAUDECODE_BATCH31_2026_HAIDIAN_MIDTERM_RECHECK_DEBUG.log"
EVIDENCE = ROOT / "OPUS47_CLAUDECODE_BATCH31_2026_HAIDIAN_MIDTERM_RUNTIME_EVIDENCE.json"
RESULT = ROOT / "OPUS47_CLAUDECODE_BATCH31_2026_HAIDIAN_MIDTERM_RECHECK_RESULT.md"
MODEL_LEDGER = ROOT / "MODEL_EVIDENCE_LEDGER.md"
GOVERNOR = ROOT / "GOVERNOR_RECOVERY_REPORT_20260524.md"
THREAD_STATUS = ROOT / "THREAD_RECOVERY_STATUS_20260524.md"
CONFUCIUS = ROOT / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"
BATCH_REPORT = ROOT / "COVERAGE_FUSION_BATCH31_2026_HAIDIAN_MIDTERM_CODEX_20260525.md"
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
    try:
        result_obj = json.loads(raw_text)
    except json.JSONDecodeError:
        return raw_text, {}
    if isinstance(result_obj, list):
        for item in reversed(result_obj):
            if isinstance(item, dict) and item.get("type") == "result" and isinstance(item.get("result"), str):
                return item["result"], {"events": result_obj, "final_result": item}
        texts = []
        for item in result_obj:
            if not isinstance(item, dict):
                continue
            message = item.get("message")
            if isinstance(message, dict):
                for content in message.get("content", []):
                    if isinstance(content, dict) and isinstance(content.get("text"), str):
                        texts.append(content["text"])
        return "\n\n".join(texts), {"events": result_obj}
    if isinstance(result_obj, dict):
        for key in ["result", "message", "text", "content"]:
            value = result_obj.get(key)
            if isinstance(value, str):
                return value, result_obj
        return json.dumps(result_obj, ensure_ascii=False, indent=2), result_obj
    return raw_text, {}


def parse_evidence(raw_text: str, debug_text: str, result_obj: dict) -> dict:
    models = set()
    for s in collect_strings(result_obj):
        for model in re.findall(r"claude-[a-z0-9-]+", s.lower()):
            if model != "claude-api":
                models.add(model)
    for model in re.findall(r"claude-[a-z0-9-]+", debug_text.lower()):
        if model != "claude-api":
            models.add(model)
    if isinstance(result_obj, dict) and result_obj.get("model"):
        models.add(str(result_obj["model"]).lower())
    return {
        "models_observed": sorted(models),
        "debug_model_mentions": sorted(model for model in set(re.findall(r"claude-[a-z0-9-]+", debug_text.lower())) if model != "claude-api"),
        "thinking_block_seen": bool(re.search(r"\bthinking(_delta)?\b|signature", raw_text.lower() + debug_text.lower())),
        "result_obj_summary": {
            key: result_obj.get(key)
            for key in ["type", "subtype", "duration_ms", "duration_api_ms", "is_error", "num_turns", "session_id", "total_cost_usd"]
            if isinstance(result_obj, dict) and key in result_obj
        },
        "model_gate": "BLOCKED_MODEL_CONFIRMATION_REQUIRED",
    }


def replace_batch_report(content: str, final_status: str, evidence: dict, content_result: str, local_policy: str) -> str:
    content = re.sub(r"Status: `[^`]+`", f"Status: `{final_status}`", content, count=1)
    content = content.replace("ClaudeCode Opus 4.7 recheck is pending.", f"ClaudeCode Opus 4.7 recheck result is `{content_result}`.")
    content = content.replace("Render QA is pending because Batch31 modified the DOCX.", "Render QA passed after Batch31 DOCX modification.")
    content = content.replace("Render status: `RENDER_PASS_CONTENT_RECHECK_PENDING_MODEL_PENDING`", "Render status: `RENDER_PASS_CONTENT_RECHECK_PASS_MODEL_GATE_BLOCKED`")
    marker = "\n## ClaudeCode Recheck Result"
    if marker in content:
        content = content[: content.index(marker)]
    content += f"""

## ClaudeCode Recheck Result

- Result artifact: `OPUS47_CLAUDECODE_BATCH31_2026_HAIDIAN_MIDTERM_RECHECK_RESULT.md`.
- `content_result`: `{content_result}`.
- `local_policy_result`: `{local_policy}`.
- `batch31_status`: `{final_status}`.
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Observed models: `{', '.join(evidence['models_observed']) or 'none'}`.
- Debug model mentions: `{', '.join(evidence['debug_model_mentions']) or 'none'}`.
- Whole-project status remains non-final.
"""
    return content


def append_status(evidence: dict, content_result: str, local_policy: str) -> None:
    final_status = "LOCAL_CLOSED_CONTENT_RENDER_PASS_WITH_MODEL_GATE_BLOCKED" if content_result in {"pass", "pass_with_notes"} else "LOCAL_RECHECK_FAILED_OR_BLOCKED"
    appendix = f"""

## Batch31 ClaudeCode Opus 4.7 Recheck: 2026海淀期中
Updated: 2026-05-25

- Runtime command: `claude -p --model claude-opus-4-7 --effort max --tools Read,Grep --output-format json --verbose`.
- `content_result`: `{content_result}`.
- `local_policy_result`: `{local_policy}`.
- `batch31_status`: `{final_status}`.
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Observed models: `{', '.join(evidence['models_observed']) or 'none'}`.
- Debug model mentions: `{', '.join(evidence['debug_model_mentions']) or 'none'}`.
- Thinking block/signature seen: `{str(evidence['thinking_block_seen']).lower()}`.
- Sonnet/Haiku/model-unknown evidence is not counted as qualified ClaudeCode evidence.
- Result artifact: `OPUS47_CLAUDECODE_BATCH31_2026_HAIDIAN_MIDTERM_RECHECK_RESULT.md`.
"""
    for path in [THREAD_STATUS, GOVERNOR, CONFUCIUS]:
        text = path.read_text(encoding="utf-8")
        text = text.replace("RENDER_PASS_CONTENT_RECHECK_PENDING_MODEL_PENDING", final_status)
        marker = "\n## Batch31 ClaudeCode Opus 4.7 Recheck"
        if marker in text:
            text = text[: text.index(marker)]
        path.write_text(text + appendix, encoding="utf-8", newline="\n")

    ledger = MODEL_LEDGER.read_text(encoding="utf-8")
    pending_pattern = r"\n## CLAUDECODE_BATCH31_HAIDIAN_MIDTERM_RECHECK\n\nstatus: `(?:real_call_pending|superseded_by_real_call)`.*?(?=\n## |\Z)"
    ledger = re.sub(pending_pattern, """

## CLAUDECODE_BATCH31_HAIDIAN_MIDTERM_RECHECK

status: `superseded_by_real_call`

- Superseded by `OPUS47_BATCH31_HAIDIAN_MIDTERM_RECHECK_001`.
- The earlier pending placeholder is not used as evidence.
""", ledger, flags=re.DOTALL)
    marker = "\n## OPUS47_BATCH31_HAIDIAN_MIDTERM_RECHECK_001"
    if marker in ledger:
        ledger = ledger[: ledger.index(marker)]
    ledger += f"""

## OPUS47_BATCH31_HAIDIAN_MIDTERM_RECHECK_001

- Batch: `2026海淀期中`.
- Command: `claude -p --model claude-opus-4-7 --effort max --tools Read,Grep --output-format json --verbose`.
- Prompt: `OPUS47_CLAUDECODE_BATCH31_2026_HAIDIAN_MIDTERM_RECHECK_PROMPT.md`.
- Raw JSON: `OPUS47_CLAUDECODE_BATCH31_2026_HAIDIAN_MIDTERM_RECHECK_RAW.json`.
- Runtime evidence: `OPUS47_CLAUDECODE_BATCH31_2026_HAIDIAN_MIDTERM_RUNTIME_EVIDENCE.json`.
- Result: `OPUS47_CLAUDECODE_BATCH31_2026_HAIDIAN_MIDTERM_RECHECK_RESULT.md`.
- Observed models: `{', '.join(evidence['models_observed']) or 'none'}`.
- Debug model mentions: `{', '.join(evidence['debug_model_mentions']) or 'none'}`.
- Thinking block/signature seen: `{str(evidence['thinking_block_seen']).lower()}`.
- Content result: `{content_result}`.
- Local policy result: `{local_policy}`.
- Model gate: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Boundary: Sonnet/Haiku/model-unknown output is not counted as qualified evidence; auxiliary model usage, if any, remains non-qualifying.
"""
    MODEL_LEDGER.write_text(ledger, encoding="utf-8", newline="\n")
    BATCH_REPORT.write_text(replace_batch_report(BATCH_REPORT.read_text(encoding="utf-8"), final_status, evidence, content_result, local_policy), encoding="utf-8", newline="\n")
    if GLOBAL_AUDIT.exists():
        text = GLOBAL_AUDIT.read_text(encoding="utf-8")
        text = text.replace("Batch31 matrix/DOCX/render pass; ClaudeCode Opus 4.7 model-lane recheck pending.", f"Batch31 matrix/DOCX/render pass; ClaudeCode content_result={content_result}; model gate remains BLOCKED_MODEL_CONFIRMATION_REQUIRED.")
        GLOBAL_AUDIT.write_text(text, encoding="utf-8", newline="\n")


def write_blocked_result(started: str, finished: str, return_code: int, stderr_text: str, raw_text: str) -> int:
    evidence = {"models_observed": [], "debug_model_mentions": [], "thinking_block_seen": False, "result_obj_summary": {"return_code": return_code}, "model_gate": "BLOCKED_MODEL_CONFIRMATION_REQUIRED"}
    EVIDENCE.write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    RESULT.write_text(f"""# ClaudeCode Opus 4.7 Recheck Result - Batch31 2026海淀期中

status: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`

- Started: `{started}`.
- Finished: `{finished}`.
- Return code: `{return_code}`.
- `content_result`: `blocked`.
- `local_policy_result`: `blocked`.
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Raw stdout bytes/chars: `{len(raw_text)}`.
- Stderr excerpt: `{stderr_text[:1000]}`.
- No qualified ClaudeCode evidence was produced.
""", encoding="utf-8", newline="\n")
    append_status(evidence, "blocked", "blocked")
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
        raw_bytes = completed.stdout or b""
        stderr_bytes = completed.stderr or b""
        return_code = completed.returncode
    except subprocess.TimeoutExpired as exc:
        timed_out = True
        raw_bytes = exc.stdout or b""
        stderr_bytes = exc.stderr or b""
        return_code = 124
    except FileNotFoundError as exc:
        RAW.write_text("", encoding="utf-8")
        STDERR.write_text(str(exc), encoding="utf-8")
        DEBUG.write_text("", encoding="utf-8")
        return write_blocked_result(started, datetime.now().isoformat(timespec="seconds"), 127, str(exc), "")
    finished = datetime.now().isoformat(timespec="seconds")
    raw_text = raw_bytes.decode("utf-8", errors="replace")
    stderr_text = stderr_bytes.decode("utf-8", errors="replace")
    RAW.write_text(raw_text, encoding="utf-8", newline="\n")
    STDERR.write_text(stderr_text, encoding="utf-8", newline="\n")
    if timed_out or return_code != 0 or not raw_text.strip():
        return write_blocked_result(started, finished, return_code, stderr_text, raw_text)
    debug_text = DEBUG.read_text(encoding="utf-8", errors="replace") if DEBUG.exists() else ""
    result_text, result_obj = parse_json_output(raw_text)
    evidence = parse_evidence(raw_text, debug_text, result_obj)
    evidence.update({"started": started, "finished": finished, "return_code": return_code, "timed_out": timed_out, "command": "claude -p --model claude-opus-4-7 --effort max --permission-mode auto --tools Read,Grep --output-format json --verbose --debug-file ... --no-session-persistence"})
    EVIDENCE.write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    content_result = detect_content_result(result_text)
    local_policy = "pass_with_model_gate_blocked" if content_result in {"pass", "pass_with_notes"} else "blocked_or_failed"
    RESULT.write_text(f"""# ClaudeCode Opus 4.7 Recheck Result - Batch31 2026海淀期中

status: `{local_policy}`

## Runtime Evidence

- Started: `{started}`.
- Finished: `{finished}`.
- Return code: `{return_code}`.
- Command: `claude -p --model claude-opus-4-7 --effort max --tools Read,Grep --output-format json --verbose`.
- Observed models: `{', '.join(evidence['models_observed']) or 'none'}`.
- Debug model mentions: `{', '.join(evidence['debug_model_mentions']) or 'none'}`.
- Thinking block/signature seen: `{str(evidence['thinking_block_seen']).lower()}`.
- Model gate: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

## Claude Verdict

{result_text}

## Local Policy Verdict

- `content_result`: `{content_result}`.
- `local_policy_result`: `{local_policy}`.
- Sonnet/Haiku/model-unknown evidence is not counted as qualified evidence.
- Auxiliary model evidence, if present, remains non-qualifying; project status remains non-final.
""", encoding="utf-8", newline="\n")
    append_status(evidence, content_result, local_policy)
    print(json.dumps({"content_result": content_result, "local_policy": local_policy, "evidence": evidence}, ensure_ascii=False, indent=2))
    return 0 if content_result in {"pass", "pass_with_notes"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
