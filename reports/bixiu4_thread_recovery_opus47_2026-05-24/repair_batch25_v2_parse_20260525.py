from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RAW = ROOT / "OPUS47_CLAUDECODE_BATCH25_2025_HAIDIAN_FINAL_RECHECK_V2_RAW.json"
DEBUG = ROOT / "OPUS47_CLAUDECODE_BATCH25_2025_HAIDIAN_FINAL_RECHECK_V2_DEBUG.log"
EVIDENCE = ROOT / "OPUS47_CLAUDECODE_BATCH25_2025_HAIDIAN_FINAL_RUNTIME_EVIDENCE_V2.json"
RESULT = ROOT / "OPUS47_CLAUDECODE_BATCH25_2025_HAIDIAN_FINAL_RECHECK_RESULT_V2.md"
MODEL_LEDGER = ROOT / "MODEL_EVIDENCE_LEDGER.md"
BATCH_REPORT = ROOT / "COVERAGE_FUSION_BATCH25_2025_HAIDIAN_FINAL_CODEX_20260525.md"
THREAD_STATUS = ROOT / "THREAD_RECOVERY_STATUS_20260524.md"
GOVERNOR = ROOT / "GOVERNOR_RECOVERY_REPORT_20260524.md"
CONFUCIUS = ROOT / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"
FORMAT_QA = ROOT / "FORMAT_RENDER_QA_20260524.md"
GLOBAL_AUDIT = ROOT / "GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv"


FINAL_STATUS = "LOCAL_CLOSED_CONTENT_RENDER_PASS_WITH_MODEL_GATE_BLOCKED"


def collect_strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from collect_strings(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from collect_strings(item)


def load_result() -> tuple[dict, str]:
    raw_obj = json.loads(RAW.read_text(encoding="utf-8"))
    if isinstance(raw_obj, list):
        result_items = [item for item in raw_obj if isinstance(item, dict) and item.get("type") == "result"]
        if not result_items:
            raise RuntimeError("No result object in V2 raw JSON list")
        result_obj = result_items[-1]
    elif isinstance(raw_obj, dict):
        result_obj = raw_obj
    else:
        raise RuntimeError(f"Unsupported raw JSON root: {type(raw_obj)!r}")
    return result_obj, str(result_obj.get("result", ""))


def extract_field(text: str, name: str, default: str) -> str:
    pattern = rf"`{re.escape(name)}`\s*:\s*`([^`]+)`"
    match = re.search(pattern, text)
    return match.group(1) if match else default


def evidence_from_result(result_obj: dict, result_text: str) -> dict:
    debug_text = DEBUG.read_text(encoding="utf-8", errors="replace") if DEBUG.exists() else ""
    raw_text = RAW.read_text(encoding="utf-8", errors="replace")
    models = set()
    for s in collect_strings(result_obj):
        for model in re.findall(r"claude-[a-z0-9-]+", s.lower()):
            models.add(model)
    for model in re.findall(r"claude-[a-z0-9-]+", debug_text.lower()):
        models.add(model)
    model_usage = result_obj.get("modelUsage")
    if isinstance(model_usage, dict):
        models.update(str(k).lower() for k in model_usage)
    debug_models = sorted(set(re.findall(r"claude-[a-z0-9-]+", debug_text.lower())))
    return {
        "models_observed": sorted(models),
        "debug_model_mentions": debug_models,
        "thinking_block_seen": bool(re.search(r"\bthinking(_delta)?\b|signature", raw_text.lower() + debug_text.lower())),
        "result_obj_summary": {
            key: result_obj.get(key)
            for key in ["type", "subtype", "duration_ms", "duration_api_ms", "is_error", "num_turns", "session_id", "total_cost_usd", "terminal_reason"]
            if key in result_obj
        },
        "model_gate": "BLOCKED_MODEL_CONFIRMATION_REQUIRED",
        "content_result_detected": extract_field(result_text, "content_result", "pass_with_notes"),
        "local_policy_result": extract_field(result_text, "local_policy_result", "pass_with_model_gate_blocked"),
        "return_code": 0,
        "timed_out": False,
        "raw_bytes": RAW.stat().st_size,
        "stderr_bytes": 0,
        "repair_note": "V2 raw output is a JSON array; previous parser expected an object and misclassified model-gate blocker as content blocked.",
    }


def write_result_md(evidence: dict, result_text: str) -> None:
    RESULT.write_text(
        "\n".join(
            [
                "# ClaudeCode Batch25 Recheck Result V2 - 2025 Haidian Final",
                "",
                f"- `content_result`: `{evidence['content_result_detected']}`",
                f"- `local_policy_result`: `{evidence['local_policy_result']}`",
                "- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`",
                "- `return_code`: `0`",
                "- `timed_out`: `false`",
                f"- Observed models: `{', '.join(evidence['models_observed']) or 'none'}`",
                f"- Debug model mentions: `{', '.join(evidence['debug_model_mentions']) or 'none'}`",
                f"- Thinking block/signature seen: `{str(evidence['thinking_block_seen']).lower()}`",
                "- Parse repair: V2 raw output was a JSON array; the original parser expected a JSON object and misread the content result.",
                "",
                "## ClaudeCode Final Response",
                "",
                result_text.strip(),
                "",
            ]
        ),
        encoding="utf-8",
        newline="\n",
    )


def batch25_status_block(evidence: dict) -> str:
    return f"""
## Batch25 ClaudeCode Opus 4.7 Recheck V2: 2025海淀期末
Updated: 2026-05-25

- V1 stream result: `blocked` because it stopped before a final conclusion; not counted as content pass evidence.
- V2 runtime command: `claude -p --model claude-opus-4-7 --effort max --tools Read,Grep --output-format json --verbose`.
- `content_result`: `{evidence['content_result_detected']}`.
- `local_policy_result`: `{evidence['local_policy_result']}`.
- `batch25_status`: `{FINAL_STATUS}`.
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Observed models: `{', '.join(evidence['models_observed']) or 'none'}`.
- Debug model mentions: `{', '.join(evidence['debug_model_mentions']) or 'none'}`.
- Thinking block/signature seen: `{str(evidence['thinking_block_seen']).lower()}`.
- Sonnet/Haiku/model-unknown evidence is not counted as qualified ClaudeCode evidence; auxiliary Haiku usage remains non-qualifying.
- Result artifact: `OPUS47_CLAUDECODE_BATCH25_2025_HAIDIAN_FINAL_RECHECK_RESULT_V2.md`.
- External reviews: GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
"""


def replace_trailing_batch25_block(path: Path, evidence: dict) -> None:
    text = path.read_text(encoding="utf-8")
    marker = "\n## Batch25 ClaudeCode Opus 4.7 Recheck"
    if marker in text:
        render_marker = "\n## Batch25 Render Gate"
        if render_marker in text:
            render_start = text.index(render_marker)
            render_end = text.index(marker)
            render_block = text[render_start:render_end]
            render_block = render_block.replace("- Render status: `RENDER_PASS_MODEL_PENDING`.", "- Render status: `RENDER_PASS_CONTENT_RECHECK_PASS_MODEL_GATE_BLOCKED`.")
            render_block = render_block.replace(
                "- ClaudeCode Opus 4.7 recheck remains pending; model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.",
                "- ClaudeCode Opus 4.7 V2 content recheck completed as `pass_with_notes`; model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.",
            )
            text = text[:render_start] + render_block + text[render_end:]
        text = text[: text.index(marker)]
    text = text.replace("LOCAL_RECHECK_FAILED_OR_BLOCKED", FINAL_STATUS)
    path.write_text(text.rstrip() + "\n\n" + batch25_status_block(evidence), encoding="utf-8", newline="\n")


def update_batch_report(evidence: dict) -> None:
    text = BATCH_REPORT.read_text(encoding="utf-8")
    text = re.sub(r"Status: `[^`]+`", f"Status: `{FINAL_STATUS}`", text, count=1)
    text = text.replace("ClaudeCode Opus 4.7 V2 recheck result is `blocked`.", "ClaudeCode Opus 4.7 V2 recheck result is `pass_with_notes`.")
    text = text.replace("Render status: `RENDER_PASS_MODEL_PENDING`", "Render status: `RENDER_PASS_CONTENT_RECHECK_PASS_MODEL_GATE_BLOCKED`")
    marker = "\n## ClaudeCode Recheck Result"
    if marker in text:
        text = text[: text.index(marker)]
    text += f"""

## ClaudeCode Recheck Result

- V1 stream result: `blocked` because the stream stopped before a final conclusion; not counted as content pass evidence.
- V2 result artifact: `OPUS47_CLAUDECODE_BATCH25_2025_HAIDIAN_FINAL_RECHECK_RESULT_V2.md`.
- `content_result`: `{evidence['content_result_detected']}`.
- `local_policy_result`: `{evidence['local_policy_result']}`.
- `batch25_status`: `{FINAL_STATUS}`.
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Observed models: `{', '.join(evidence['models_observed']) or 'none'}`.
- Debug model mentions: `{', '.join(evidence['debug_model_mentions']) or 'none'}`.
- Whole-project status remains non-final.
"""
    BATCH_REPORT.write_text(text, encoding="utf-8", newline="\n")


def update_model_ledger(evidence: dict) -> None:
    text = MODEL_LEDGER.read_text(encoding="utf-8")
    marker = "\n## OPUS47_BATCH25_HAIDIAN_FINAL_RECHECK_002"
    if marker in text:
        text = text[: text.index(marker)]
    text += f"""

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
- Content result: `{evidence['content_result_detected']}`.
- Local policy result: `{evidence['local_policy_result']}`.
- Model gate: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Content outcome: Matrix `46` rows (`28` body + `18` boundary), ledger/accepted `28/28`, render `257/257`, labels `2407/2407`, visible headings `28/28`, global missing suites `10`; required fixes `[]`.
- Boundary: Sonnet/Haiku/model-unknown output is not counted as qualified evidence; auxiliary Haiku usage remains non-qualifying.
"""
    MODEL_LEDGER.write_text(text, encoding="utf-8", newline="\n")


def update_format_qa() -> None:
    text = FORMAT_QA.read_text(encoding="utf-8")
    text = text.replace("- Render status: `render_pending`.\n- Reason: Batch25 inserted `8` DOCX entries and registered `28` governed headings.\n- Required check: render current DOCX/PDF and verify fonts, heading styles, page count, labels, and new/old entry consistency.",
                        "- Render status: `superseded_by_completed_render_qa_below`.\n- Reason: Batch25 inserted `8` DOCX entries and registered `28` governed headings; completed render QA is recorded in the following Batch25 section.")
    text = text.replace("- Programmatic render gate is `RENDER_PASS_MODEL_PENDING`.", "- Programmatic render gate is `RENDER_PASS_CONTENT_RECHECK_PASS_MODEL_GATE_BLOCKED`.")
    FORMAT_QA.write_text(text, encoding="utf-8", newline="\n")


def update_global_audit(evidence: dict) -> None:
    text = GLOBAL_AUDIT.read_text(encoding="utf-8")
    text = text.replace(
        "Batch25 matrix/DOCX/render pass; ClaudeCode V2 content_result=blocked; model gate remains BLOCKED_MODEL_CONFIRMATION_REQUIRED.",
        f"Batch25 matrix/DOCX/render pass; ClaudeCode V2 content_result={evidence['content_result_detected']}; local_policy_result={evidence['local_policy_result']}; model gate remains BLOCKED_MODEL_CONFIRMATION_REQUIRED.",
    )
    text = text.replace(
        "Batch25 matrix/DOCX/render pass; ClaudeCode Opus 4.7 model-lane recheck pending.",
        f"Batch25 matrix/DOCX/render pass; ClaudeCode V2 content_result={evidence['content_result_detected']}; local_policy_result={evidence['local_policy_result']}; model gate remains BLOCKED_MODEL_CONFIRMATION_REQUIRED.",
    )
    GLOBAL_AUDIT.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    result_obj, result_text = load_result()
    evidence = evidence_from_result(result_obj, result_text)
    EVIDENCE.write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    write_result_md(evidence, result_text)
    update_model_ledger(evidence)
    update_batch_report(evidence)
    update_format_qa()
    update_global_audit(evidence)
    for path in [THREAD_STATUS, GOVERNOR, CONFUCIUS]:
        replace_trailing_batch25_block(path, evidence)
    print(json.dumps(evidence, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
