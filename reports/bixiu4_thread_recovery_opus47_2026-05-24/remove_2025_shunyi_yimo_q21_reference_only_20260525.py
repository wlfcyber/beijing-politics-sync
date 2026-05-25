from __future__ import annotations

import csv
import json
import shutil
import tempfile
import zipfile
from datetime import datetime
from pathlib import Path

from lxml import etree


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
W = f"{{{W_NS}}}"
NS = {"w": W_NS}

RECOVERY = Path(__file__).resolve().parent
RUN = RECOVERY.parent / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
REPORT_JSON = RECOVERY / "SHUNYI_2025_YIMO_Q21_REFERENCE_ONLY_REMOVAL_20260525.json"
REPORT_MD = RECOVERY / "SHUNYI_2025_YIMO_Q21_REFERENCE_ONLY_REMOVAL_20260525.md"

SUITE = "2025顺义一模"
Q21_HEADING = "2025顺义一模 第21题"
SOURCE_BUNDLE = "preprocessed_corpus\\gpt_suite_bundles\\2025各区模拟题__2025各区一模__2025顺义一模.md"


def para_text(p) -> str:
    return "".join(t.text or "" for t in p.xpath(".//w:t", namespaces=NS))


def p_style(p) -> str:
    node = p.find("./w:pPr/w:pStyle", namespaces=NS)
    return node.get(W + "val") if node is not None else ""


def is_section_or_entry(p) -> bool:
    return p_style(p) in {"Heading1", "Heading2", "Heading3", "1", "2", "3", "4", "5"}


def current_docx() -> Path:
    docs = [p for p in DELIVERY.glob("*.docx") if "_backup_" not in p.stem and not p.name.startswith("~$")]
    if len(docs) != 1:
        raise RuntimeError(f"Expected one current DOCX, found {docs}")
    return docs[0]


def remove_q21(ts: str) -> dict[str, object]:
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_2025_shunyi_yimo_q21_reference_removal_{ts}.docx")
    shutil.copy2(docx, backup)
    removed_blocks = []
    with tempfile.TemporaryDirectory() as td:
        temp = Path(td)
        with zipfile.ZipFile(docx) as zin:
            zin.extractall(temp)
        xml_path = temp / "word" / "document.xml"
        tree = etree.parse(str(xml_path))
        body = tree.getroot().find("w:body", namespaces=NS)
        if body is None:
            raise RuntimeError("missing body")
        children = list(body)
        remove_indexes: set[int] = set()
        i = 0
        while i < len(children):
            child = children[i]
            if child.tag == W + "p" and Q21_HEADING in para_text(child):
                start = i
                j = i + 1
                while j < len(children):
                    nxt = children[j]
                    if nxt.tag == W + "p" and is_section_or_entry(nxt) and para_text(nxt).strip():
                        break
                    j += 1
                removed_blocks.append({"heading": para_text(child).strip(), "paragraphs_removed": j - start})
                remove_indexes.update(range(start, j))
                i = j
            else:
                i += 1
        for idx in sorted(remove_indexes, reverse=True):
            body.remove(children[idx])
        tree.write(str(xml_path), encoding="utf-8", xml_declaration=True, standalone=True)
        with zipfile.ZipFile(docx, "w", zipfile.ZIP_DEFLATED) as zout:
            for path in temp.rglob("*"):
                if path.is_file():
                    zout.write(path, path.relative_to(temp).as_posix())
    return {"docx": str(docx), "docx_backup": str(backup), "removed_blocks": removed_blocks}


def update_matrix(ts: str) -> dict[str, object]:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_2025_shunyi_yimo_q21_reference_removal_{ts}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)
    for row in rows:
        if row.get("matrix_row_id") == "M0522":
            row.update({
                "题号": "Q21",
                "题型或模块判断": "主观题：教师版参考答案链条，缺正式评分细则",
                "是否进宝典": "否：旧正文参考链已移除，不能以普通参考答案替代细则",
                "宝典节点": "-",
                "细则支持原理": "教师版答案写明“原卷无答案，此答案仅供参考”；无正式评分细则支撑整体与部分/价值判断落点。",
                "证据等级": "教师版参考答案+题面显性链条（非正式评分细则；已移除正文）",
                "是否误放": "否：旧参考链已修复移除",
                "是否需补厚": "否",
                "当前处理": "REMOVED_REFERENCE_ONLY_BODY_ENTRY",
                "备注": "硬规则：普通参考答案不能冒充细则；因此移除当前DOCX中Q21两处旧条目，仅保留矩阵边界记录。",
                "source_artifact": f"{SOURCE_BUNDLE}:371-378; {SOURCE_BUNDLE}:731-748",
            })
            break
    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return {"matrix_backup": str(backup), "updated_row": "M0522"}


def write_report(ts: str, removal: dict[str, object], matrix: dict[str, object]) -> None:
    payload = {"timestamp": ts, "docx": removal, "matrix": matrix}
    REPORT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    REPORT_MD.write_text(
        "\n".join([
            "# SHUNYI_2025_YIMO_Q21_REFERENCE_ONLY_REMOVAL_20260525",
            "",
            "Status: `SHUNYI_2025_YIMO_Q21_REFERENCE_ONLY_BODY_ENTRY_REMOVED_RENDER_PENDING`",
            "",
            f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')} +08",
            "",
            "## Decision",
            "",
            "- Removed two current-DOCX entries for 2025 Shunyi Yimo Q21.",
            "- Reason: the teacher-version answer explicitly says the original paper has no answer and this answer is for reference only; no formal scoring rules support the philosophy placements.",
            "- This enforces the hard rule that ordinary reference answers cannot masquerade as scoring rules.",
            "- Matrix row `M0522` is now marked `REMOVED_REFERENCE_ONLY_BODY_ENTRY`.",
            "- Render QA must be rerun after this DOCX change.",
            "",
            "## Outputs",
            "",
            f"- DOCX backup: `{removal['docx_backup']}`.",
            f"- Matrix backup: `{matrix['matrix_backup']}`.",
            f"- Removed blocks: `{json.dumps(removal['removed_blocks'], ensure_ascii=False)}`.",
            "",
            "## Boundary",
            "",
            "No external model evidence was added. GPTPro and full Claude Opus 4.7 DOCX/PDF artifact reviews remain `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.",
            "",
        ]),
        encoding="utf-8",
    )


def main() -> None:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    removal = remove_q21(ts)
    matrix = update_matrix(ts)
    write_report(ts, removal, matrix)
    print(json.dumps({"docx": removal, "matrix": matrix}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
