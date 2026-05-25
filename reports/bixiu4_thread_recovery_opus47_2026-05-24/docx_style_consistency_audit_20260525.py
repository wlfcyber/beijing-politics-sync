from __future__ import annotations

import csv
import hashlib
import json
import re
import zipfile
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree as ET


RECOVERY = Path(__file__).resolve().parent
RUN = RECOVERY.parent / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
RENDER_DIR = RECOVERY / "word_render_qa_20260525_heading_style_fix"
OUT_JSON = RECOVERY / "DOCX_STYLE_CONSISTENCY_AUDIT_20260525.json"
OUT_MD = RECOVERY / "DOCX_STYLE_CONSISTENCY_AUDIT_20260525.md"

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
VOLATILE_ATTR_SUFFIXES = ("rsidR", "rsidRPr", "rsidRDefault", "rsidP", "paraId", "textId")
LABELS = [
    "【材料触发点】",
    "【设问】",
    "【为什么能想到】",
    "【答案落点】",
]
QUESTION_HEADING_RE = re.compile(r"^\s*\d+\.\s*20(?:24|25|26).+第.+题")


def current_docx_pdf() -> tuple[Path, Path]:
    docx_files = [
        p
        for p in DELIVERY.glob("*.docx")
        if not p.name.startswith("~$") and "_backup_" not in p.stem
    ]
    pdf_files = [
        p
        for p in DELIVERY.glob("*.pdf")
        if not p.name.startswith("~$") and "_backup_" not in p.stem
    ]
    if len(docx_files) != 1 or len(pdf_files) != 1:
        raise RuntimeError(f"Expected one current docx/pdf, got {docx_files} / {pdf_files}")
    return docx_files[0], pdf_files[0]


def strip_volatile(elem: ET.Element) -> ET.Element:
    clone = ET.fromstring(ET.tostring(elem, encoding="utf-8"))
    for node in clone.iter():
        for key in list(node.attrib):
            local = key.rsplit("}", 1)[-1]
            if local in VOLATILE_ATTR_SUFFIXES or local.startswith("rsid"):
                del node.attrib[key]
    return clone


def sig(elem: ET.Element | None) -> str:
    if elem is None:
        raw = b""
    else:
        raw = ET.tostring(strip_volatile(elem), encoding="utf-8")
    return hashlib.sha1(raw).hexdigest()[:12]


def style_id(p: ET.Element) -> str:
    ppr = p.find(f"{W}pPr")
    if ppr is None:
        return ""
    pstyle = ppr.find(f"{W}pStyle")
    if pstyle is None:
        return ""
    return pstyle.attrib.get(f"{W}val", "")


def paragraph_text(p: ET.Element) -> str:
    parts: list[str] = []
    for t in p.iter(f"{W}t"):
        parts.append(t.text or "")
    return "".join(parts)


def first_run_rpr_sig(p: ET.Element) -> str:
    run = p.find(f"{W}r")
    if run is None:
        return sig(None)
    return sig(run.find(f"{W}rPr"))


def first_run_text(p: ET.Element) -> str:
    run = p.find(f"{W}r")
    if run is None:
        return ""
    return "".join((t.text or "") for t in run.iter(f"{W}t"))


def read_document_paragraphs(docx: Path) -> list[dict[str, str]]:
    with zipfile.ZipFile(docx) as z:
        xml = z.read("word/document.xml")
    root = ET.fromstring(xml)
    out: list[dict[str, str]] = []
    for idx, p in enumerate(root.iter(f"{W}p")):
        text = paragraph_text(p).strip()
        if not text:
            continue
        ppr = p.find(f"{W}pPr")
        run = p.find(f"{W}r")
        out.append(
            {
                "index": str(idx),
                "text": text,
                "style_id": style_id(p),
                "ppr_sig": sig(ppr),
                "first_run_text": first_run_text(p),
                "first_run_rpr_sig": first_run_rpr_sig(p),
                "heading_rpr_sig": first_run_rpr_sig(p),
            }
        )
    return out


def normalize_heading(text: str) -> str:
    return re.sub(r"^\s*\d+\.\s*", "", text).strip()


def ledger_headings() -> set[str]:
    p = DELIVERY / "docx_insert_ledger.csv"
    with p.open("r", encoding="utf-8-sig", newline="") as f:
        return {
            normalize_heading(row["inserted_heading"].strip())
            for row in csv.DictReader(f)
            if row.get("inserted_heading")
        }


def label_for_text(text: str) -> str | None:
    for label in LABELS:
        if text.startswith(label):
            return label
    return None


def main() -> None:
    docx, pdf = current_docx_pdf()
    paragraphs = read_document_paragraphs(docx)
    inserted_set = ledger_headings()

    heading_positions: list[int] = [
        i for i, p in enumerate(paragraphs) if QUESTION_HEADING_RE.match(p["text"])
    ]
    entries: list[dict[str, object]] = []
    missing_labels: list[dict[str, object]] = []
    duplicate_label_blocks: list[dict[str, object]] = []
    label_stats: dict[str, Counter[str]] = {label: Counter() for label in LABELS}
    label_group_stats: dict[str, dict[str, Counter[str]]] = {
        "inserted": {label: Counter() for label in LABELS},
        "legacy": {label: Counter() for label in LABELS},
    }
    heading_stats: dict[str, Counter[str]] = {
        "all_ppr": Counter(),
        "all_rpr": Counter(),
        "inserted_ppr": Counter(),
        "inserted_rpr": Counter(),
        "legacy_ppr": Counter(),
        "legacy_rpr": Counter(),
    }

    heading_texts_norm: list[str] = []
    for pos_index, start in enumerate(heading_positions):
        end = heading_positions[pos_index + 1] if pos_index + 1 < len(heading_positions) else len(paragraphs)
        heading = paragraphs[start]
        norm = normalize_heading(heading["text"])
        heading_texts_norm.append(norm)
        group = "inserted" if norm in inserted_set else "legacy"
        body = paragraphs[start + 1 : end]
        found: dict[str, list[dict[str, str]]] = {label: [] for label in LABELS}
        for p in body[:12]:
            label = label_for_text(p["text"])
            if label:
                found[label].append(p)

        for label in LABELS:
            if not found[label]:
                missing_labels.append({"heading": heading["text"], "missing_label": label})
            elif len(found[label]) > 1:
                duplicate_label_blocks.append(
                    {"heading": heading["text"], "label": label, "count": len(found[label])}
                )
            else:
                p = found[label][0]
                label_stats[label].update([p["first_run_rpr_sig"]])
                label_group_stats[group][label].update([p["first_run_rpr_sig"]])

        heading_stats["all_ppr"].update([heading["ppr_sig"]])
        heading_stats["all_rpr"].update([heading["heading_rpr_sig"]])
        heading_stats[f"{group}_ppr"].update([heading["ppr_sig"]])
        heading_stats[f"{group}_rpr"].update([heading["heading_rpr_sig"]])
        entries.append(
            {
                "heading": heading["text"],
                "normalized_heading": norm,
                "group": group,
                "style_id": heading["style_id"],
                "ppr_sig": heading["ppr_sig"],
                "rpr_sig": heading["heading_rpr_sig"],
            }
        )

    missing_ledger_headings = sorted(inserted_set - set(heading_texts_norm))
    label_variant_counts = {label: len(counter) for label, counter in label_stats.items()}
    inserted_legacy_label_mismatch: list[dict[str, object]] = []
    for label in LABELS:
        inserted_sigs = set(label_group_stats["inserted"][label])
        legacy_sigs = set(label_group_stats["legacy"][label])
        if inserted_sigs and legacy_sigs and inserted_sigs != legacy_sigs:
            inserted_legacy_label_mismatch.append(
                {
                    "label": label,
                    "inserted_sigs": sorted(inserted_sigs),
                    "legacy_sigs": sorted(legacy_sigs),
                }
            )

    render_manifest_path = RENDER_DIR / "render_manifest.json"
    render_manifest = {}
    if render_manifest_path.exists():
        render_manifest = json.loads(render_manifest_path.read_text(encoding="utf-8-sig"))

    failures: list[str] = []
    if missing_labels:
        failures.append("missing_label_blocks")
    if duplicate_label_blocks:
        failures.append("duplicate_label_blocks")
    if any(count != 1 for count in label_variant_counts.values()):
        failures.append("label_first_run_style_variants")
    if inserted_legacy_label_mismatch:
        failures.append("inserted_legacy_label_style_mismatch")
    if len(heading_stats["all_ppr"]) != 1 or len(heading_stats["all_rpr"]) != 1:
        failures.append("heading_style_variants")
    if missing_ledger_headings:
        failures.append("ledger_heading_not_found_in_docx")
    if render_manifest:
        if render_manifest.get("pdf_pages") != render_manifest.get("rendered_png_count"):
            failures.append("rendered_page_count_mismatch")
        if render_manifest.get("blank_like_pages_excluding_cover_foreword"):
            failures.append("blank_like_body_pages")
        if render_manifest.get("docx_label_count") != render_manifest.get("pdf_label_count"):
            failures.append("docx_pdf_label_count_mismatch")

    status = "PASS" if not failures else "FAIL"
    result = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S +08"),
        "status": status,
        "failures": failures,
        "docx": str(docx),
        "pdf": str(pdf),
        "docx_bytes": docx.stat().st_size,
        "pdf_bytes": pdf.stat().st_size,
        "question_entry_count": len(entries),
        "inserted_entry_count": sum(1 for e in entries if e["group"] == "inserted"),
        "legacy_entry_count": sum(1 for e in entries if e["group"] == "legacy"),
        "unique_ledger_headings": len(inserted_set),
        "missing_ledger_heading_count": len(missing_ledger_headings),
        "missing_ledger_headings_sample": missing_ledger_headings[:30],
        "missing_label_count": len(missing_labels),
        "missing_label_sample": missing_labels[:30],
        "duplicate_label_count": len(duplicate_label_blocks),
        "duplicate_label_sample": duplicate_label_blocks[:30],
        "heading_ppr_variant_count": len(heading_stats["all_ppr"]),
        "heading_rpr_variant_count": len(heading_stats["all_rpr"]),
        "inserted_heading_ppr_variant_count": len(heading_stats["inserted_ppr"]),
        "legacy_heading_ppr_variant_count": len(heading_stats["legacy_ppr"]),
        "inserted_heading_rpr_variant_count": len(heading_stats["inserted_rpr"]),
        "legacy_heading_rpr_variant_count": len(heading_stats["legacy_rpr"]),
        "label_first_run_variant_counts": label_variant_counts,
        "inserted_legacy_label_mismatch": inserted_legacy_label_mismatch,
        "label_counts": {
            label: sum(label_stats[label].values()) for label in LABELS
        },
        "render_manifest": render_manifest,
    }
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    render_line = "not found"
    if render_manifest:
        render_line = (
            f"{render_manifest.get('rendered_png_count')}/{render_manifest.get('pdf_pages')} pages, "
            f"labels {render_manifest.get('docx_label_count')}/{render_manifest.get('pdf_label_count')}, "
            f"blank-like pages {len(render_manifest.get('blank_like_pages_excluding_cover_foreword') or [])}"
        )

    lines = [
        "# DOCX_STYLE_CONSISTENCY_AUDIT_20260525",
        "",
        f"Status: `{status}`",
        f"Updated: {result['timestamp']}",
        "",
        "## Scope",
        "",
        f"- DOCX bytes: `{result['docx_bytes']}`.",
        f"- PDF bytes: `{result['pdf_bytes']}`.",
        f"- Question entries audited: `{result['question_entry_count']}`.",
        f"- Entries matched to insertion ledger: `{result['inserted_entry_count']}`.",
        f"- Legacy or inherited entries: `{result['legacy_entry_count']}`.",
        f"- Unique ledger headings: `{result['unique_ledger_headings']}`.",
        "",
        "## Structural Style Checks",
        "",
        f"- Heading paragraph property variants: `{result['heading_ppr_variant_count']}`.",
        f"- Heading run property variants: `{result['heading_rpr_variant_count']}`.",
        f"- Inserted heading pPr/rPr variants: `{result['inserted_heading_ppr_variant_count']}`/`{result['inserted_heading_rpr_variant_count']}`.",
        f"- Legacy heading pPr/rPr variants: `{result['legacy_heading_ppr_variant_count']}`/`{result['legacy_heading_rpr_variant_count']}`.",
        f"- Missing label blocks: `{result['missing_label_count']}`.",
        f"- Duplicate label blocks: `{result['duplicate_label_count']}`.",
        f"- Ledger headings missing from current DOCX: `{result['missing_ledger_heading_count']}`.",
        "",
        "## Label Style Variants",
        "",
    ]
    for label, count in label_variant_counts.items():
        lines.append(f"- `{label}` first-run style variants: `{count}`; count: `{result['label_counts'][label]}`.")
    lines.extend(
        [
            "",
            "## Render Cross-Check",
            "",
            f"- Latest retained render: `{render_line}`.",
            "",
            "## Boundary",
            "",
            "- This audit proves structural heading/label style consistency inside the DOCX and checks it against the latest retained PDF render manifest.",
            "- It does not replace full every-page human visual review or the required GPTPro/Claude Opus external content-thickness review.",
        ]
    )
    if failures:
        lines.extend(["", "## Failures", ""])
        for item in failures:
            lines.append(f"- `{item}`")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
