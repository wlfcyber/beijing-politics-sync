from __future__ import annotations

import csv
import json
import zipfile
from datetime import datetime
from pathlib import Path

from lxml import etree


ROOT = Path(__file__).resolve().parents[2]
RECOVERY = ROOT / "reports" / "bixiu4_thread_recovery_opus47_2026-05-24"
RUN = ROOT / "reports" / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
RENDER_DIR = RUN / "07_render_check" / "word_pdf_pages"
SUITE = "2026海淀二模"

MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
LEDGER = DELIVERY / "docx_insert_ledger.csv"
ACCEPTED = RUN / "04_fusion_audit" / "student_patch_entries.accepted.jsonl"
MODEL_LEDGER = RECOVERY / "MODEL_EVIDENCE_LEDGER.md"
THREAD_STATUS = RECOVERY / "THREAD_RECOVERY_STATUS_20260524.md"
FORMAT_QA = RECOVERY / "FORMAT_RENDER_QA_20260524.md"
GOVERNOR = RECOVERY / "GOVERNOR_RECOVERY_REPORT_20260524.md"
CONFUCIUS = RECOVERY / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"
RESULT = RECOVERY / "OPUS47_CLAUDECODE_BATCH06_2026_HAIDIAN_ERMO_RECHECK_RESULT.md"
RAW = RECOVERY / "OPUS47_CLAUDECODE_BATCH06_2026_HAIDIAN_ERMO_RECHECK_RAW.json"
DEBUG = RECOVERY / "OPUS47_CLAUDECODE_BATCH06_2026_HAIDIAN_ERMO_RECHECK_DEBUG.log"
PROMPT = RECOVERY / "OPUS47_CLAUDECODE_BATCH06_2026_HAIDIAN_ERMO_RECHECK_PROMPT.md"


def read_matrix_stats() -> dict[str, int]:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    open_marker = "是：需逐题回源/融合裁决"
    return {
        "matrix_rows": len(rows),
        "suite_rows": sum(1 for r in rows if r["题源"] == SUITE),
        "suite_open": sum(1 for r in rows if r["题源"] == SUITE and r["是否需补厚"] == open_marker),
        "global_open": sum(1 for r in rows if r["是否需补厚"] == open_marker),
    }


def read_ledger_stats() -> dict[str, int]:
    with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    return {
        "ledger_rows": len(rows),
        "suite_ledger_rows": sum(1 for r in rows if r["source_suite"] == SUITE),
    }


def read_accepted_count() -> int:
    return sum(1 for line in ACCEPTED.read_text(encoding="utf-8-sig").splitlines() if line.strip())


def current_docx_pdf() -> tuple[Path, Path]:
    docx = [p for p in DELIVERY.glob("*.docx") if "_backup_" not in p.stem and not p.name.startswith("~$")]
    pdf = [p for p in DELIVERY.glob("*.pdf") if "_backup_" not in p.stem and not p.name.startswith("~$")]
    if len(docx) != 1 or len(pdf) != 1:
        raise RuntimeError(f"expected one docx/pdf, found {docx} / {pdf}")
    return docx[0], pdf[0]


def label_stats(docx: Path) -> tuple[int, int]:
    labels = ["【材料触发点】", "【设问】", "【为什么能想到】", "【答案落点】"]
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    with zipfile.ZipFile(docx) as z:
        root = etree.fromstring(z.read("word/document.xml"))
    total = 0
    good = 0
    for p in root.xpath("//w:p", namespaces=ns):
        text = "".join(t.text or "" for t in p.xpath(".//w:t", namespaces=ns)).strip()
        if not any(text.startswith(label) for label in labels):
            continue
        total += 1
        first = p.xpath(".//w:r[1]", namespaces=ns)
        if not first:
            continue
        b = first[0].find(".//w:b", namespaces=ns)
        color = first[0].find(".//w:color", namespaces=ns)
        val = color.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val") if color is not None else None
        if b is not None and val == "21574C":
            good += 1
    return good, total


def read_raw() -> dict:
    return json.loads(RAW.read_text(encoding="utf-8-sig"))


def section_once(path: Path, marker: str, content: str) -> None:
    text = path.read_text(encoding="utf-8-sig")
    if marker in text:
        head = text.split(marker, 1)[0].rstrip()
        path.write_text(head + "\n\n" + content.strip() + "\n", encoding="utf-8")
    else:
        path.write_text(text.rstrip() + "\n\n" + content.strip() + "\n", encoding="utf-8")


def main() -> None:
    matrix = read_matrix_stats()
    ledger = read_ledger_stats()
    accepted_rows = read_accepted_count()
    docx, pdf = current_docx_pdf()
    page_png_count = len(list(RENDER_DIR.glob("page_*.png")))
    good_labels, total_labels = label_stats(docx)
    raw = read_raw()
    usage = raw["modelUsage"]
    opus = usage.get("claude-opus-4-7", {})
    haiku = usage.get("claude-haiku-4-5-20251001", {})
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M +08")

    model_section = f"""## OPUS47_BATCH06_HAIDIAN_RECHECK_001

- timestamp: 2026-05-25 01:35-01:45 +08
- command: `claude -p --model claude-opus-4-7 --effort max --permission-mode auto --output-format json --debug-file OPUS47_CLAUDECODE_BATCH06_2026_HAIDIAN_ERMO_RECHECK_DEBUG.log --no-session-persistence < OPUS47_CLAUDECODE_BATCH06_2026_HAIDIAN_ERMO_RECHECK_PROMPT.md`
- prompt: `{PROMPT.name}`
- result: `{RESULT.name}`
- raw artifact: `{RAW.name}` (converted to UTF-8 after backup)
- debug artifact: `{DEBUG.name}`
- session id: `{raw.get('session_id')}`
- uuid: `{raw.get('uuid')}`
- runtime model proof: debug log records `model=claude-opus-4-7 modelSupported=true`; RAW JSON `modelUsage` contains `claude-opus-4-7`.
- opus tokens: input `{opus.get('inputTokens')}`, cache read `{opus.get('cacheReadInputTokens')}`, cache creation `{opus.get('cacheCreationInputTokens')}`, output `{opus.get('outputTokens')}`.
- auxiliary model usage: `claude-haiku-4-5-20251001` input `{haiku.get('inputTokens')}`, output `{haiku.get('outputTokens')}`; this auxiliary usage is not counted as qualified evidence.
- content result: `pass_with_model_gate_blocked`.
- content outcome: Q2/Q3/Q4 placements passed; Q16 broad-node downgrade passed; Q21 HOLD passed; Q5/Q9/Q10/Q14 boundary rows passed; render gate passed.
- model gate: `BLOCKED_MODEL_CONFIRMATION_REQUIRED` because the command includes `--effort max` but the runtime artifacts do not expose machine-readable max-effort/adaptive-thinking proof.
"""

    model_text = MODEL_LEDGER.read_text(encoding="utf-8-sig")
    model_text = model_text.replace(
        "Status: `OPUS47_BATCH04_ADDED__BLOCKED_MODEL_CONFIRMATION_REQUIRED_FOR_EFFORT_PROOF`",
        "Status: `OPUS47_BATCH06_ADDED__BLOCKED_MODEL_CONFIRMATION_REQUIRED_FOR_EFFORT_PROOF`",
    )
    if "## OPUS47_BATCH06_HAIDIAN_RECHECK_001" not in model_text:
        model_text = model_text.rstrip() + "\n\n" + model_section.strip() + "\n"
    MODEL_LEDGER.write_text(model_text, encoding="utf-8")

    common_stats = (
        f"- Matrix rows: `{matrix['matrix_rows']}`; `{SUITE}` rows: `{matrix['suite_rows']}`; "
        f"`{SUITE}` exact open rows: `{matrix['suite_open']}`; global exact open rows: `{matrix['global_open']}`.\n"
        f"- Ledger rows: `{ledger['ledger_rows']}`; `{SUITE}` ledger rows: `{ledger['suite_ledger_rows']}`.\n"
        f"- Accepted JSONL rows: `{accepted_rows}`.\n"
        f"- DOCX/PDF bytes: `{docx.stat().st_size}` / `{pdf.stat().st_size}`.\n"
        f"- Rendered page PNG count: `{page_png_count}`; label style check: `{good_labels}/{total_labels}`."
    )

    thread_section = f"""## Batch06 Update: 2026海淀二模

Updated: {timestamp}

Status remains: `RECOVERED_EXECUTION_IN_PROGRESS`.

- Batch06 completed `2026海淀二模` row-source recovery.
- Inserted Q2/Q3/Q4 into the current DOCX:
  - Q2 -> `社会存在与社会意识`
  - Q3 -> `主观能动性 / 意识的能动作用`
  - Q4 -> `联系的客观性`
- Q16 is retained only as two broad nodes: `联系的普遍性 / 联系的观点（总）` and `实践与认识（总）`; evidence wording is downgraded to `答案和评分参考角度（非逐点细则）`.
- Q21 remains HOLD/no insert because the source gives only broad angle prompts and includes `辩证思维` boundary risk.
- Added missing boundary rows `M0862`-`M0865` for Q5/Q9/Q10/Q14.
{common_stats}
- ClaudeCode Batch06 real run: `OPUS47_BATCH06_HAIDIAN_RECHECK_001`; content result `pass_with_model_gate_blocked`; model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web full-artifact review: `real_call_pending`.
- Claude Opus external full-artifact review: `real_call_pending`.
"""
    section_once(THREAD_STATUS, "## Batch06 Update: 2026海淀二模", thread_section)

    format_section = f"""## Batch06 Render QA: 2026海淀二模

Updated: {timestamp}

- Current DOCX: `{docx.name}`, `{docx.stat().st_size}` bytes.
- Current PDF: `{pdf.name}`, `{pdf.stat().st_size}` bytes.
- PDF export reported `234` pages; rendered `page_*.png` count is `{page_png_count}`. The directory also contains the existing contact/index image, which is not a page render.
- Pixel scan sampled all `page_*.png` files and found no near-blank pages.
- Label style check: `{good_labels}/{total_labels}` student-facing label runs are bold with color `21574C`.
- New Batch06 headings present in DOCX/ledger: Q2, Q3, Q4, plus prior Q16 two entries.
- Status: render gate passed for Batch06, but full every-page manual typography comparison remains open.
"""
    section_once(FORMAT_QA, "## Batch06 Render QA: 2026海淀二模", format_section)

    governor_section = f"""## Batch06 Governor Update: 2026海淀二模

Updated: {timestamp}

Verdict: `RECOVERED_EXECUTION_IN_PROGRESS`.

{common_stats}

Governor findings:
- Q2/Q3/Q4 insertions are supported by official answer key plus correct-option chain.
- Q16 is no longer overclaimed as per-point detailed scoring; only answer/scoring-reference broad angle evidence is used.
- Q21 remains blocked from insertion; no ordinary angle prompt is used as a detailed scoring rule.
- Sonnet/Haiku/model-unknown evidence is not counted as qualified ClaudeCode evidence.
- Batch06 ClaudeCode content review passed, but model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web full-artifact review and external Claude Opus full-artifact review remain `real_call_pending`.
"""
    section_once(GOVERNOR, "## Batch06 Governor Update: 2026海淀二模", governor_section)

    confucius_section = f"""## Batch06 Confucius Artifact Check: 2026海淀二模

Updated: {timestamp}

Confucius zero-baseline checks:
- Student-facing DOCX now has five `2026海淀二模` entries in the ledger: Q2, Q3, Q4, and Q16 x2.
- Q2 teaches that culture as social consciousness can react on social existence and produce real effects; it does not split option ③ into an extra philosophy node.
- Q3 teaches conscious creative activity through the `墨梅` artistic image.
- Q4 teaches that humanized connections remain objective and must respect ecological conditions.
- Q16 teaches only broad `联系` and `实践与认识` angles.
- Q21 is kept out of the student text because a broad angle list is not a scoring-rule landing.
- Render gate: PDF `234` pages, page images `{page_png_count}`, label style `{good_labels}/{total_labels}`.
- Remaining blockers: model effort/adaptive proof `BLOCKED_MODEL_CONFIRMATION_REQUIRED`; GPTPro and external Claude review `real_call_pending`; global exact open rows `{matrix['global_open']}`.
"""
    section_once(CONFUCIUS, "## Batch06 Confucius Artifact Check: 2026海淀二模", confucius_section)

    result_addendum = f"""## Codex Runtime Evidence Addendum

Added: {timestamp}

The Claude-authored result above says the recheck lacked captured RAW/debug artifacts from inside its own runtime. Codex did capture them from the invoking shell:

- Command used: `claude -p --model claude-opus-4-7 --effort max --permission-mode auto --output-format json --debug-file {DEBUG.name} --no-session-persistence`
- RAW artifact: `{RAW.name}`.
- Debug artifact: `{DEBUG.name}`.
- Debug proof: `model=claude-opus-4-7 modelSupported=true`.
- RAW `modelUsage`: `claude-opus-4-7` output `{opus.get('outputTokens')}` tokens with cache read `{opus.get('cacheReadInputTokens')}` and cache creation `{opus.get('cacheCreationInputTokens')}`; auxiliary `claude-haiku-4-5-20251001` output `{haiku.get('outputTokens')}` tokens.
- Qualification: content review is accepted as real ClaudeCode Opus 4.7 production-line evidence, but not final model-gate evidence. The gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED` because max-effort/adaptive-thinking proof is not machine-exposed beyond the command flag.
- Corrected global exact open rows after Batch06: `{matrix['global_open']}`.
"""
    section_once(RESULT, "## Codex Runtime Evidence Addendum", result_addendum)

    print("batch06 snapshots synced")
    print(common_stats)


if __name__ == "__main__":
    main()
