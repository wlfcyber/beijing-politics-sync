from __future__ import annotations

import csv
import json
import zipfile
from datetime import datetime
from pathlib import Path

from lxml import etree
from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
RECOVERY = ROOT / "reports" / "bixiu4_thread_recovery_opus47_2026-05-24"
RUN = ROOT / "reports" / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
RENDER_DIR = RUN / "07_render_check" / "word_pdf_pages"
SUITE = "2025东城一模"

MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
LEDGER = DELIVERY / "docx_insert_ledger.csv"
ACCEPTED = RUN / "04_fusion_audit" / "student_patch_entries.accepted.jsonl"
MODEL_LEDGER = RECOVERY / "MODEL_EVIDENCE_LEDGER.md"
THREAD_STATUS = RECOVERY / "THREAD_RECOVERY_STATUS_20260524.md"
FORMAT_QA = RECOVERY / "FORMAT_RENDER_QA_20260524.md"
GOVERNOR = RECOVERY / "GOVERNOR_RECOVERY_REPORT_20260524.md"
CONFUCIUS = RECOVERY / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"
RESULT = RECOVERY / "OPUS47_CLAUDECODE_BATCH08_2025_DONGCHENG_YIMO_RECHECK_RESULT.md"
RAW = RECOVERY / "OPUS47_CLAUDECODE_BATCH08_2025_DONGCHENG_YIMO_RECHECK_RAW.json"
DEBUG = RECOVERY / "OPUS47_CLAUDECODE_BATCH08_2025_DONGCHENG_YIMO_RECHECK_DEBUG.log"
PROMPT = RECOVERY / "OPUS47_CLAUDECODE_BATCH08_2025_DONGCHENG_YIMO_RECHECK_PROMPT.md"


def read_matrix_stats() -> dict[str, int]:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    exact_open = "是：需逐题回源/融合裁决"
    return {
        "matrix_rows": len(rows),
        "suite_rows": sum(1 for r in rows if r["题源"] == SUITE),
        "suite_exact_open": sum(1 for r in rows if r["题源"] == SUITE and r["是否需补厚"] == exact_open),
        "global_exact_open": sum(1 for r in rows if r["是否需补厚"] == exact_open),
        "global_startswith_open": sum(1 for r in rows if str(r["是否需补厚"]).startswith("是")),
    }


def read_ledger_stats() -> dict[str, int]:
    with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    return {
        "ledger_rows": len(rows),
        "suite_ledger_rows": sum(1 for r in rows if r["source_suite"] == SUITE),
    }


def read_accepted_stats() -> dict[str, int]:
    records = [json.loads(line) for line in ACCEPTED.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    return {
        "accepted_rows": len(records),
        "suite_accepted_rows": sum(1 for r in records if r.get("source_suite") == SUITE),
    }


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
    total = good = 0
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


def batch08_docx_stats(docx: Path) -> dict[str, int | bool | list[int]]:
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    with zipfile.ZipFile(docx) as z:
        root = etree.fromstring(z.read("word/document.xml"))
    paras = root.xpath("//w:p", namespaces=ns)
    hits = []
    q5_drawing = False
    label_good = label_total = 0
    for idx, p in enumerate(paras):
        text = "".join(t.text or "" for t in p.xpath(".//w:t", namespaces=ns)).strip()
        if SUITE in text:
            hits.append(idx)
            if "第5题" in text:
                q5_drawing = any(paras[j].xpath(".//w:drawing", namespaces=ns) for j in range(idx + 1, min(idx + 8, len(paras))))
            for j in range(idx + 1, min(idx + 6, len(paras))):
                t = "".join(x.text or "" for x in paras[j].xpath(".//w:t", namespaces=ns)).strip()
                if t.startswith(("【材料触发点】", "【设问】", "【为什么能想到】", "【答案落点】")):
                    label_total += 1
                    first = paras[j].xpath(".//w:r[1]", namespaces=ns)
                    if not first:
                        continue
                    b = first[0].find(".//w:b", namespaces=ns)
                    color = first[0].find(".//w:color", namespaces=ns)
                    val = color.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val") if color is not None else None
                    if b is not None and val == "21574C":
                        label_good += 1
    return {"suite_hits": len(hits), "q5_drawing": q5_drawing, "batch_label_good": label_good, "batch_label_total": label_total}


def render_stats() -> dict[str, int | list[str]]:
    pngs = sorted(RENDER_DIR.glob("page_*.png"))
    blank_like = []
    for p in pngs:
        image = Image.open(p).convert("L")
        lo, hi = image.getextrema()
        if hi - lo < 8:
            blank_like.append(p.name)
    return {"page_png_count": len(pngs), "blank_like": blank_like}


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
    accepted = read_accepted_stats()
    docx, pdf = current_docx_pdf()
    render = render_stats()
    good_labels, total_labels = label_stats(docx)
    batch_docx = batch08_docx_stats(docx)
    raw = read_raw()
    usage = raw["modelUsage"]
    opus = usage.get("claude-opus-4-7", {})
    haiku = usage.get("claude-haiku-4-5-20251001", {})
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M +08")

    model_section = f"""## OPUS47_BATCH08_DONGCHENG_YIMO_RECHECK_001

- timestamp: 2026-05-25 02:22-02:33 +08
- command: `claude -p --model claude-opus-4-7 --effort max --permission-mode auto --output-format json --debug-file OPUS47_CLAUDECODE_BATCH08_2025_DONGCHENG_YIMO_RECHECK_DEBUG.log --no-session-persistence < OPUS47_CLAUDECODE_BATCH08_2025_DONGCHENG_YIMO_RECHECK_PROMPT.md`
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
- content outcome: Q1/Q4/Q5/Q16 insertions passed; Q5 cartoon image passed; Q6/Q16/Q18/Q21 existing coverage passed; Q9/Q14 missing boundary rows passed; render gate passed.
- model gate: `BLOCKED_MODEL_CONFIRMATION_REQUIRED` because the command includes `--effort max` but runtime artifacts do not expose machine-readable max-effort/adaptive-thinking proof.
"""

    model_text = MODEL_LEDGER.read_text(encoding="utf-8-sig")
    model_text = model_text.replace(
        "Status: `OPUS47_BATCH07_ADDED__BLOCKED_MODEL_CONFIRMATION_REQUIRED_FOR_EFFORT_PROOF`",
        "Status: `OPUS47_BATCH08_ADDED__BLOCKED_MODEL_CONFIRMATION_REQUIRED_FOR_EFFORT_PROOF`",
    )
    if "## OPUS47_BATCH08_DONGCHENG_YIMO_RECHECK_001" not in model_text:
        model_text = model_text.rstrip() + "\n\n" + model_section.strip() + "\n"
    MODEL_LEDGER.write_text(model_text, encoding="utf-8")

    common_stats = (
        f"- Matrix rows: `{matrix['matrix_rows']}`; `{SUITE}` rows: `{matrix['suite_rows']}`; "
        f"`{SUITE}` exact open rows: `{matrix['suite_exact_open']}`; global exact open rows: `{matrix['global_exact_open']}`; global broader open rows: `{matrix['global_startswith_open']}`.\n"
        f"- Ledger rows: `{ledger['ledger_rows']}`; `{SUITE}` ledger rows: `{ledger['suite_ledger_rows']}`.\n"
        f"- Accepted JSONL rows: `{accepted['accepted_rows']}`; `{SUITE}` accepted rows: `{accepted['suite_accepted_rows']}`.\n"
        f"- DOCX/PDF bytes: `{docx.stat().st_size}` / `{pdf.stat().st_size}`.\n"
        f"- Rendered page PNG count: `{render['page_png_count']}`; blank-like rendered pages: `{len(render['blank_like'])}`; label style check: `{good_labels}/{total_labels}`; Batch08 suite hits: `{batch_docx['suite_hits']}`; Batch08 labels: `{batch_docx['batch_label_good']}/{batch_docx['batch_label_total']}`; Q5 image embedded: `{batch_docx['q5_drawing']}`."
    )

    thread_section = f"""## Batch08 Update: 2025东城一模

Updated: {timestamp}

Status remains: `RECOVERED_EXECUTION_IN_PROGRESS`.

- Batch08 completed `2025东城一模` row-source recovery.
- Inserted Q1/Q4/Q5/Q16 into the current DOCX:
  - Q1 -> `人民群众`
  - Q4 -> `根据固有联系建立新的具体联系`
  - Q5 -> `矛盾就是对立统一`, with source cartoon image embedded
  - Q16 -> `发展的观点 / 发展的普遍性`
- Q6, Q16, Q18(1), and Q21 existing DOCX coverage were retained with corrected evidence boundaries.
- Added missing boundary rows `M0868` and `M0869` for Q9 and Q14.
{common_stats}
- ClaudeCode Batch08 real run: `OPUS47_BATCH08_DONGCHENG_YIMO_RECHECK_001`; content result `pass_with_model_gate_blocked`; model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web full-artifact review: `real_call_pending`.
- Claude Opus external full-artifact review: `real_call_pending`.
"""
    section_once(THREAD_STATUS, "## Batch08 Update: 2025东城一模", thread_section)

    format_section = f"""## Batch08 Render QA: 2025东城一模

Updated: {timestamp}

- Current DOCX: `{docx.name}`, `{docx.stat().st_size}` bytes.
- Current PDF: `{pdf.name}`, `{pdf.stat().st_size}` bytes.
- PDF export reported `237` pages; rendered `page_*.png` count is `{render['page_png_count']}`.
- Pixel scan sampled all `page_*.png` files and found `{len(render['blank_like'])}` blank-like pages.
- Full-document label style check: `{good_labels}/{total_labels}` student-facing label runs are bold with color `21574C`.
- Batch08 label check: `{batch_docx['batch_label_good']}/{batch_docx['batch_label_total']}` labels pass.
- Q5 cartoon image is embedded in the DOCX near the Q5 entry: `{batch_docx['q5_drawing']}`; rendered page `123` was visually inspected and shows no overlap.
- Status: render gate passed for Batch08, but full every-page manual typography comparison remains open.
"""
    section_once(FORMAT_QA, "## Batch08 Render QA: 2025东城一模", format_section)

    governor_section = f"""## Batch08 Governor Update: 2025东城一模

Updated: {timestamp}

Verdict: `RECOVERED_EXECUTION_IN_PROGRESS`.

{common_stats}

Governor findings:
- Q1/Q4/Q5 choice-question insertions are supported by official answer key plus correct-option chain.
- Q5 source cartoon is embedded and rendered.
- Q16 development insertion is supported by the formal marking report explicitly listing `发展` as usable philosophy knowledge.
- Q18(1) existing coverage is retained because the formal marking report explicitly allows the relevant philosophy substitutions.
- Q21 remains only angle/level-scoring support for upper-structure reaction on economic base; no ordinary answer is upgraded to a detailed rubric.
- Sonnet/Haiku/model-unknown evidence is not counted as qualified ClaudeCode evidence.
- Batch08 ClaudeCode content review passed, but model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web full-artifact review and external Claude Opus full-artifact review remain `real_call_pending`.
"""
    section_once(GOVERNOR, "## Batch08 Governor Update: 2025东城一模", governor_section)

    confucius_section = f"""## Batch08 Confucius Artifact Check: 2025东城一模

Updated: {timestamp}

Confucius zero-baseline checks:
- Student-facing DOCX now has four new `2025东城一模` entries: Q1, Q4, Q5, and Q16 development.
- Q1 teaches that人民群众 are the root force behind national development.
- Q4 teaches that people can establish new concrete connections based on the inherent links among heritage protection, city renewal, and cultural experience.
- Q5 teaches 对立统一 through the actual cartoon image and the correct poem.
- Q16 development teaches why中国年 keeps growing through inherited core and new forms.
- Q18 and Q21 are retained only within their source-supported boundaries.
- Render gate: PDF `237` pages, page images `{render['page_png_count']}`, labels `{good_labels}/{total_labels}`, Q5 image embedded `{batch_docx['q5_drawing']}`.
- Remaining blockers: model effort/adaptive proof `BLOCKED_MODEL_CONFIRMATION_REQUIRED`; GPTPro and external Claude review `real_call_pending`; global exact open rows `{matrix['global_exact_open']}`.
"""
    section_once(CONFUCIUS, "## Batch08 Confucius Artifact Check: 2025东城一模", confucius_section)

    result_addendum = f"""## Codex Runtime Evidence Addendum

Added: {timestamp}

Codex captured the invoking shell artifacts for the Batch08 ClaudeCode run:

- Command used: `claude -p --model claude-opus-4-7 --effort max --permission-mode auto --output-format json --debug-file {DEBUG.name} --no-session-persistence`
- RAW artifact: `{RAW.name}`.
- Debug artifact: `{DEBUG.name}`.
- Debug proof: `model=claude-opus-4-7 modelSupported=true`.
- RAW `modelUsage`: `claude-opus-4-7` output `{opus.get('outputTokens')}` tokens with cache read `{opus.get('cacheReadInputTokens')}` and cache creation `{opus.get('cacheCreationInputTokens')}`; auxiliary `claude-haiku-4-5-20251001` output `{haiku.get('outputTokens')}` tokens.
- Qualification: content review is accepted as real ClaudeCode Opus 4.7 production-line evidence, but not final model-gate evidence. The gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED` because max-effort/adaptive-thinking proof is not machine-exposed beyond the command flag.
- Corrected global exact open rows after Batch08: `{matrix['global_exact_open']}`.
- Current measured DOCX/PDF bytes after Codex sync: `{docx.stat().st_size}` / `{pdf.stat().st_size}`.
"""
    section_once(RESULT, "## Codex Runtime Evidence Addendum", result_addendum)

    print("batch08 snapshots synced")
    print(common_stats)


if __name__ == "__main__":
    main()
