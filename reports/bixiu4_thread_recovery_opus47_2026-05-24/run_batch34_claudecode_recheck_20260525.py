from __future__ import annotations

import importlib.util
import re
from pathlib import Path


BASE_PATH = Path(__file__).with_name("run_batch32_claudecode_recheck_20260525.py")
spec = importlib.util.spec_from_file_location("run_batch32", BASE_PATH)
r32 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(r32)

r32.PROMPT = r32.ROOT / "OPUS47_CLAUDECODE_BATCH34_2026_TONGZHOU_FINAL_RECHECK_PROMPT.md"
r32.RAW = r32.ROOT / "OPUS47_CLAUDECODE_BATCH34_2026_TONGZHOU_FINAL_RECHECK_RAW.json"
r32.STDERR = r32.ROOT / "OPUS47_CLAUDECODE_BATCH34_2026_TONGZHOU_FINAL_RECHECK_STDERR.log"
r32.DEBUG = r32.ROOT / "OPUS47_CLAUDECODE_BATCH34_2026_TONGZHOU_FINAL_RECHECK_DEBUG.log"
r32.EVIDENCE = r32.ROOT / "OPUS47_CLAUDECODE_BATCH34_2026_TONGZHOU_FINAL_RUNTIME_EVIDENCE.json"
r32.RESULT = r32.ROOT / "OPUS47_CLAUDECODE_BATCH34_2026_TONGZHOU_FINAL_RECHECK_RESULT.md"
r32.BATCH_REPORT = r32.ROOT / "COVERAGE_FUSION_BATCH34_2026_TONGZHOU_FINAL_CODEX_20260525.md"

PENDING_MARKER = "CLAUDECODE_BATCH34_TONGZHOU_FINAL_RECHECK"
OPUS_MARKER = "OPUS47_BATCH34_TONGZHOU_FINAL_RECHECK_001"


def replace_batch_report(content: str, final_status: str, evidence: dict, content_result: str, local_policy: str) -> str:
    content = re.sub(r"Status: `[^`]+`", f"Status: `{final_status}`", content, count=1)
    content = content.replace("ClaudeCode Opus 4.7 recheck is pending.", f"ClaudeCode Opus 4.7 recheck result is `{content_result}`.")
    content = content.replace("Render QA is pending because Batch34 modified the DOCX.", "Render QA passed after Batch34 DOCX modification.")
    content = content.replace("Render status: `RENDER_PASS_CONTENT_RECHECK_PENDING_MODEL_PENDING`", "Render status: `RENDER_PASS_CONTENT_RECHECK_PASS_MODEL_GATE_BLOCKED`")
    marker = "\n## ClaudeCode Recheck Result"
    if marker in content:
        content = content[: content.index(marker)]
    content += f"""

## ClaudeCode Recheck Result

- Result artifact: `OPUS47_CLAUDECODE_BATCH34_2026_TONGZHOU_FINAL_RECHECK_RESULT.md`.
- `content_result`: `{content_result}`.
- `local_policy_result`: `{local_policy}`.
- `batch34_status`: `{final_status}`.
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Observed models: `{', '.join(evidence['models_observed']) or 'none'}`.
- Debug model mentions: `{', '.join(evidence['debug_model_mentions']) or 'none'}`.
- Whole-project status remains non-final.
"""
    return content


def append_status(evidence: dict, content_result: str, local_policy: str) -> None:
    final_status = "LOCAL_CLOSED_CONTENT_RENDER_PASS_WITH_MODEL_GATE_BLOCKED" if content_result in {"pass", "pass_with_notes"} else "LOCAL_RECHECK_FAILED_OR_BLOCKED"
    appendix = f"""

## Batch34 ClaudeCode Opus 4.7 Recheck: 2026通州期末
Updated: 2026-05-25

- Runtime command: `claude -p --model claude-opus-4-7 --effort max --tools Read,Grep --output-format json --verbose`.
- `content_result`: `{content_result}`.
- `local_policy_result`: `{local_policy}`.
- `batch34_status`: `{final_status}`.
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Observed models: `{', '.join(evidence['models_observed']) or 'none'}`.
- Debug model mentions: `{', '.join(evidence['debug_model_mentions']) or 'none'}`.
- Thinking block/signature seen: `{str(evidence['thinking_block_seen']).lower()}`.
- Sonnet/Haiku/model-unknown evidence is not counted as qualified ClaudeCode evidence.
- Result artifact: `OPUS47_CLAUDECODE_BATCH34_2026_TONGZHOU_FINAL_RECHECK_RESULT.md`.
"""
    for path in [r32.THREAD_STATUS, r32.GOVERNOR, r32.CONFUCIUS]:
        text = path.read_text(encoding="utf-8")
        text = text.replace("RENDER_PASS_CONTENT_RECHECK_PENDING_MODEL_PENDING", final_status)
        marker = "\n## Batch34 ClaudeCode Opus 4.7 Recheck"
        if marker in text:
            text = text[: text.index(marker)]
        path.write_text(text + appendix, encoding="utf-8", newline="\n")

    ledger = r32.MODEL_LEDGER.read_text(encoding="utf-8")
    pending_pattern = rf"\n## {PENDING_MARKER}\n\nstatus: `(?:real_call_pending|superseded_by_real_call)`.*?(?=\n## |\Z)"
    ledger = re.sub(pending_pattern, f"""

## {PENDING_MARKER}

status: `superseded_by_real_call`

- Superseded by `{OPUS_MARKER}`.
- The earlier pending placeholder is not used as evidence.
""", ledger, flags=re.DOTALL)
    marker = f"\n## {OPUS_MARKER}"
    if marker in ledger:
        ledger = ledger[: ledger.index(marker)]
    ledger += f"""

## {OPUS_MARKER}

- Batch: `2026通州期末`.
- Command: `claude -p --model claude-opus-4-7 --effort max --tools Read,Grep --output-format json --verbose`.
- Prompt: `OPUS47_CLAUDECODE_BATCH34_2026_TONGZHOU_FINAL_RECHECK_PROMPT.md`.
- Raw JSON: `OPUS47_CLAUDECODE_BATCH34_2026_TONGZHOU_FINAL_RECHECK_RAW.json`.
- Runtime evidence: `OPUS47_CLAUDECODE_BATCH34_2026_TONGZHOU_FINAL_RUNTIME_EVIDENCE.json`.
- Result: `OPUS47_CLAUDECODE_BATCH34_2026_TONGZHOU_FINAL_RECHECK_RESULT.md`.
- Observed models: `{', '.join(evidence['models_observed']) or 'none'}`.
- Debug model mentions: `{', '.join(evidence['debug_model_mentions']) or 'none'}`.
- Thinking block/signature seen: `{str(evidence['thinking_block_seen']).lower()}`.
- Content result: `{content_result}`.
- Local policy result: `{local_policy}`.
- Model gate: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Boundary: Sonnet/Haiku/model-unknown output is not counted as qualified evidence; auxiliary model usage, if any, remains non-qualifying.
"""
    r32.MODEL_LEDGER.write_text(ledger, encoding="utf-8", newline="\n")
    r32.BATCH_REPORT.write_text(replace_batch_report(r32.BATCH_REPORT.read_text(encoding="utf-8"), final_status, evidence, content_result, local_policy), encoding="utf-8", newline="\n")
    if r32.GLOBAL_AUDIT.exists():
        text = r32.GLOBAL_AUDIT.read_text(encoding="utf-8")
        text = text.replace("Batch34 matrix/DOCX/render pass; ClaudeCode Opus 4.7 model-lane recheck pending.", f"Batch34 matrix/DOCX/render pass; ClaudeCode content_result={content_result}; model gate remains BLOCKED_MODEL_CONFIRMATION_REQUIRED.")
        r32.GLOBAL_AUDIT.write_text(text, encoding="utf-8", newline="\n")


def write_blocked_result(started: str, finished: str, return_code: int, stderr_text: str, raw_text: str) -> int:
    evidence = {"models_observed": [], "debug_model_mentions": [], "thinking_block_seen": False, "result_obj_summary": {"return_code": return_code}, "model_gate": "BLOCKED_MODEL_CONFIRMATION_REQUIRED"}
    r32.EVIDENCE.write_text(r32.json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    r32.RESULT.write_text(f"""# ClaudeCode Opus 4.7 Recheck Result - Batch34 2026通州期末

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


r32.replace_batch_report = replace_batch_report
r32.append_status = append_status
r32.write_blocked_result = write_blocked_result


def main() -> int:
    code = r32.main()
    if r32.RESULT.exists():
        text = r32.RESULT.read_text(encoding="utf-8")
        text = text.replace(
            "# ClaudeCode Opus 4.7 Recheck Result - Batch32 2026海淀期末",
            "# ClaudeCode Opus 4.7 Recheck Result - Batch34 2026通州期末",
            1,
        )
        r32.RESULT.write_text(text, encoding="utf-8", newline="\n")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
