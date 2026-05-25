from __future__ import annotations

import copy
import json
import shutil
import tempfile
import zipfile
from collections import Counter
from datetime import datetime
from pathlib import Path

from lxml import etree


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML_NS = "http://www.w3.org/XML/1998/namespace"
W = f"{{{W_NS}}}"
XML = f"{{{XML_NS}}}"
NS = {"w": W_NS}

RECOVERY = Path(__file__).resolve().parent
RUN = RECOVERY.parent / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
REPORT_JSON = RECOVERY / "STYLE_NORMALIZATION_AUDIT_20260525.json"
REPORT_MD = RECOVERY / "STYLE_NORMALIZATION_AUDIT_20260525.md"


def u(codes: list[int]) -> str:
    return "".join(chr(code) for code in codes)


LABELS = [
    u([0x3010, 0x6750, 0x6599, 0x89E6, 0x53D1, 0x70B9, 0x3011]),
    u([0x3010, 0x8BBE, 0x95EE, 0x3011]),
    u([0x3010, 0x4E3A, 0x4EC0, 0x4E48, 0x80FD, 0x60F3, 0x5230, 0x3011]),
    u([0x3010, 0x7B54, 0x6848, 0x843D, 0x70B9, 0x3011]),
]


def current_docx() -> Path:
    docs = [
        p
        for p in DELIVERY.glob("*.docx")
        if "_backup_" not in p.stem and not p.name.startswith("~$")
    ]
    if len(docs) != 1:
        raise RuntimeError(f"Expected one current DOCX, found {docs}")
    return docs[0]


def para_text(p: etree._Element) -> str:
    return "".join(t.text or "" for t in p.xpath(".//w:t", namespaces=NS))


def run_text(r: etree._Element) -> str:
    return "".join(t.text or "" for t in r.xpath(".//w:t", namespaces=NS))


def is_bold(r: etree._Element) -> bool:
    rpr = r.find("./w:rPr", namespaces=NS)
    if rpr is None:
        return False
    bold = rpr.find("./w:b", namespaces=NS)
    if bold is None:
        return False
    val = bold.get(W + "val")
    return val is None or val not in {"0", "false", "False"}


def run_color(r: etree._Element) -> str | None:
    rpr = r.find("./w:rPr", namespaces=NS)
    if rpr is None:
        return None
    color = rpr.find("./w:color", namespaces=NS)
    return color.get(W + "val") if color is not None else None


def paragraph_style(p: etree._Element) -> str | None:
    style = p.find("./w:pPr/w:pStyle", namespaces=NS)
    return style.get(W + "val") if style is not None else None


def spacing_after(p: etree._Element) -> str | None:
    spacing = p.find("./w:pPr/w:spacing", namespaces=NS)
    return spacing.get(W + "after") if spacing is not None else None


def ensure_spacing_after_80(p: etree._Element) -> None:
    ppr = p.find("./w:pPr", namespaces=NS)
    if ppr is None:
        ppr = etree.Element(W + "pPr", nsmap=p.nsmap)
        p.insert(0, ppr)
    spacing = ppr.find("./w:spacing", namespaces=NS)
    if spacing is None:
        spacing = etree.SubElement(ppr, W + "spacing")
    spacing.set(W + "after", "80")


def make_run(text: str, *, label: bool) -> etree._Element:
    r = etree.Element(W + "r")
    if label:
        rpr = etree.SubElement(r, W + "rPr")
        etree.SubElement(rpr, W + "b")
        color = etree.SubElement(rpr, W + "color")
        color.set(W + "val", "21574C")
    t = etree.SubElement(r, W + "t")
    if text.startswith(" ") or text.endswith(" "):
        t.set(XML + "space", "preserve")
    t.text = text
    return r


def normalize_label_paragraph(p: etree._Element, label: str, text: str) -> None:
    rest = text[len(label) :]
    for child in list(p):
        if child.tag == W + "r":
            p.remove(child)
    p.append(make_run(label, label=True))
    if rest:
        p.append(make_run(rest, label=False))
    ensure_spacing_after_80(p)


def label_failures(paragraphs: list[etree._Element]) -> tuple[dict[str, dict[str, object]], int]:
    stats: dict[str, dict[str, object]] = {
        label: {"count": 0, "fail": 0, "examples": []} for label in LABELS
    }
    total_fail = 0
    for idx, p in enumerate(paragraphs):
        text = para_text(p)
        label = next((candidate for candidate in LABELS if text.startswith(candidate)), None)
        if label is None:
            continue
        stats[label]["count"] = int(stats[label]["count"]) + 1
        issues: list[str] = []
        runs = p.findall("./w:r", namespaces=NS)
        if not runs:
            issues.append("no_runs")
        else:
            if run_text(runs[0]) != label:
                issues.append("first_run_not_label")
            if not is_bold(runs[0]):
                issues.append("label_not_bold")
            if run_color(runs[0]) != "21574C":
                issues.append("label_color_not_21574C")
            for r in runs[1:]:
                text_part = run_text(r)
                if text_part.strip() and is_bold(r):
                    issues.append("body_run_bold")
                    break
                if text_part.strip() and run_color(r) == "21574C":
                    issues.append("body_run_green")
                    break
        if spacing_after(p) != "80":
            issues.append("spacing_after_not_80")
        if issues:
            stats[label]["fail"] = int(stats[label]["fail"]) + 1
            total_fail += 1
            examples = stats[label]["examples"]
            if isinstance(examples, list) and len(examples) < 6:
                examples.append({"paragraph_index": idx, "issues": issues, "text": text[:120]})
    return stats, total_fail


def heading_style_hashes(paragraphs: list[etree._Element]) -> dict[str, object]:
    ppr_counts: Counter[str] = Counter()
    rpr_counts: Counter[str] = Counter()
    style5_count = 0
    for p in paragraphs:
        if paragraph_style(p) != "5":
            continue
        style5_count += 1
        ppr = p.find("./w:pPr", namespaces=NS)
        rprs = [r.find("./w:rPr", namespaces=NS) for r in p.findall("./w:r", namespaces=NS)]
        ppr_xml = etree.tostring(ppr) if ppr is not None else b""
        rpr_xml = b"|".join(etree.tostring(rpr) if rpr is not None else b"" for rpr in rprs)
        ppr_counts[str(hash(ppr_xml))] += 1
        rpr_counts[str(hash(rpr_xml))] += 1
    return {
        "style_5_count": style5_count,
        "ppr_variant_count": len(ppr_counts),
        "rpr_variant_count": len(rpr_counts),
        "ppr_variants": ppr_counts.most_common(),
        "rpr_variants": rpr_counts.most_common(),
    }


def normalize_heading_paragraphs(paragraphs: list[etree._Element]) -> int:
    canonical_ppr = None
    canonical_rpr = None
    for p in paragraphs:
        if paragraph_style(p) != "5":
            continue
        ppr = p.find("./w:pPr", namespaces=NS)
        first_run = p.find("./w:r", namespaces=NS)
        rpr = first_run.find("./w:rPr", namespaces=NS) if first_run is not None else None
        if ppr is not None and rpr is not None:
            canonical_ppr = copy.deepcopy(ppr)
            canonical_rpr = copy.deepcopy(rpr)
            break
    if canonical_ppr is None:
        raise RuntimeError("No canonical heading paragraph style found")

    changed = 0
    for p in paragraphs:
        if paragraph_style(p) != "5":
            continue
        old_ppr = p.find("./w:pPr", namespaces=NS)
        if old_ppr is not None:
            p.remove(old_ppr)
        p.insert(0, copy.deepcopy(canonical_ppr))
        if canonical_rpr is not None:
            for r in p.findall("./w:r", namespaces=NS):
                if not run_text(r).strip():
                    continue
                old_rpr = r.find("./w:rPr", namespaces=NS)
                if old_rpr is not None:
                    r.remove(old_rpr)
                r.insert(0, copy.deepcopy(canonical_rpr))
        changed += 1
    return changed


def write_docx(path: Path, infos: list[zipfile.ZipInfo], data: dict[str, bytes]) -> None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp_path = Path(tmp.name)
    with zipfile.ZipFile(tmp_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zout:
        for info in infos:
            zi = zipfile.ZipInfo(info.filename, date_time=info.date_time)
            zi.comment = info.comment
            zi.extra = info.extra
            zi.internal_attr = info.internal_attr
            zi.external_attr = info.external_attr
            zi.create_system = info.create_system
            zi.compress_type = zipfile.ZIP_DEFLATED
            zout.writestr(zi, data[info.filename])
    shutil.move(str(tmp_path), path)


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_global_style_normalization_{timestamp}.docx")
    shutil.copy2(docx, backup)

    with zipfile.ZipFile(docx, "r") as zin:
        infos = zin.infolist()
        data = {info.filename: zin.read(info.filename) for info in infos}

    parser = etree.XMLParser(remove_blank_text=False, resolve_entities=False)
    root = etree.fromstring(data["word/document.xml"], parser=parser)
    paragraphs = root.xpath(".//w:body/w:p", namespaces=NS)
    before_label_stats, before_label_failures = label_failures(paragraphs)
    before_heading_stats = heading_style_hashes(paragraphs)

    normalized_labels = 0
    for p in paragraphs:
        text = para_text(p)
        label = next((candidate for candidate in LABELS if text.startswith(candidate)), None)
        if label is None:
            continue
        normalize_label_paragraph(p, label, text)
        normalized_labels += 1
    normalized_headings = normalize_heading_paragraphs(paragraphs)

    after_label_stats, after_label_failures = label_failures(paragraphs)
    after_heading_stats = heading_style_hashes(paragraphs)

    data["word/document.xml"] = etree.tostring(
        root,
        encoding="UTF-8",
        xml_declaration=True,
        standalone=True,
    )
    write_docx(docx, infos, data)

    report = {
        "timestamp": timestamp,
        "docx": str(docx),
        "backup": str(backup),
        "normalized_label_paragraphs": normalized_labels,
        "normalized_heading_paragraphs": normalized_headings,
        "before_label_failures": before_label_failures,
        "after_label_failures": after_label_failures,
        "before_label_stats": before_label_stats,
        "after_label_stats": after_label_stats,
        "before_heading_stats": before_heading_stats,
        "after_heading_stats": after_heading_stats,
    }
    REPORT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    REPORT_MD.write_text(
        "\n".join(
            [
                "# STYLE_NORMALIZATION_AUDIT_20260525",
                "",
                "Status: `DOCX_STYLE_NORMALIZED_RENDER_PENDING`",
                "",
                f"- Timestamp: `{timestamp}`.",
                f"- DOCX: `{docx}`.",
                f"- Backup: `{backup}`.",
                f"- Label paragraphs normalized: `{normalized_labels}`.",
                f"- Label failures before/after: `{before_label_failures}/{after_label_failures}`.",
                f"- Heading paragraphs normalized: `{normalized_headings}`.",
                (
                    "- Heading pPr variants before/after: "
                    f"`{before_heading_stats['ppr_variant_count']}/{after_heading_stats['ppr_variant_count']}`."
                ),
                (
                    "- Heading rPr variants before/after: "
                    f"`{before_heading_stats['rpr_variant_count']}/{after_heading_stats['rpr_variant_count']}`."
                ),
                "",
                "Boundary: this is a structural DOCX style normalization only. It does not change source judgments, matrix placement, or model-review gates.",
            ]
        )
        + "\n",
        encoding="utf-8",
        newline="\n",
    )

    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
