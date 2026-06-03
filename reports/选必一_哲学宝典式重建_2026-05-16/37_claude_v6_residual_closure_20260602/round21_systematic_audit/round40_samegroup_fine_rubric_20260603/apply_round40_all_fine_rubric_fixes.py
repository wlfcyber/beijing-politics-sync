#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import re
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


RUN_DIR = Path(__file__).resolve().parent
REPORT_DIR = RUN_DIR / "agent_reports"
ROUND35 = RUN_DIR.parent / "round35_samegroup_rubric_relock" / "apply_round35_samegroup_rubric_relock.py"

INPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_同题组细颗粒修正_延庆回归版_学生版_带水印_20260603.docx")
OUTPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_同题组细颗粒全量修正_核心答题点红色强化_学生版_带水印_20260603.docx")
AUDIT_JSON = RUN_DIR / "round40_all_fine_rubric_fixes.json"

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

FORBIDDEN = [
    "证据卡",
    "证据边界",
    "证据层级",
    "源卡",
    "回源",
    "细则复练",
    "待复核",
    "可锁定",
    "未锁定",
    "正式主链",
    "正文条目",
    "工程痕迹",
    "后台",
    "raw_cards",
    "BLOCKED",
    "backend",
    "audit",
    "source",
    "risk",
    "round",
    "参考答案",
    "正式细则",
    "细则",
    "评标",
    "评分",
    "证据",
]

TEXT_REPLACEMENTS = [
    ("评分结构", "答题层次"),
    ("评分层次", "得分层次"),
    ("评分边界", "易错边界"),
    ("评分标准", "得分标准"),
    ("正式材料", "原题材料"),
    ("评标参考角度", "原题答题角度"),
    ("按评标参考角度组织", "按原题答题角度组织"),
    ("参考答案式方向", "答案方向"),
    ("参考答案式文本", "答案方向"),
    ("未锁定", "未确认"),
    ("正式细则", "原题要求"),
    ("细则", "要求"),
    ("评标", "要求"),
    ("评分", "得分"),
    ("证据", "支撑"),
]


def load_round35():
    spec = importlib.util.spec_from_file_location("round35", ROUND35)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


R35 = load_round35()
qn = R35.qn
paragraph_text = R35.paragraph_text
make_bullet = R35.make_bullet
set_text = R35.set_text


def clean_student_text(text: str) -> str:
    cleaned = text.strip()
    for old, new in TEXT_REPLACEMENTS:
        cleaned = cleaned.replace(old, new)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def extract_key(text: str) -> str | None:
    compact = text.replace(" ", "")
    match = re.search(r"(20\d{2}.*?Q\d+(?:\(\d+\))?)", compact)
    if not match:
        return None
    return match.group(1)


def section_blocks(text: str) -> list[tuple[str, str]]:
    starts = list(re.finditer(r"^##\s+(.+)$", text, flags=re.M))
    blocks: list[tuple[str, str]] = []
    for i, start in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else len(text)
        blocks.append((start.group(1).strip(), text[start.end() : end]))
    return blocks


def parse_replacement(section: str) -> tuple[str, list[str]] | None:
    match = re.search(r"-\s*replacement_text:\s*(.*)", section)
    if not match:
        return None
    tail = section[match.start() :]
    tail = re.sub(r"^- replacement_text:\s*", "", tail, count=1).strip()
    tail = re.split(r"\n##\s+", tail, maxsplit=1)[0].strip()
    if not tail or tail.startswith("无"):
        return None
    if tail.startswith("```"):
        tail = re.sub(r"^```[a-zA-Z0-9_-]*\s*", "", tail)
        tail = re.sub(r"\s*```$", "", tail.strip())
    lines = [clean_student_text(line) for line in tail.splitlines() if clean_student_text(line)]
    lines = [line for line in lines if not line.startswith("```")]
    if not lines:
        return None
    marker = lines[0]
    body = [line for line in lines[1:] if line.startswith("·")]
    if not marker.startswith("【同题组】") or not body:
        return None
    marker = marker.replace("【同题组】（", "【同题组】 （")
    return marker, body


def load_report_overrides() -> dict[str, dict[str, object]]:
    overrides: dict[str, dict[str, object]] = {}
    report_summary: dict[str, dict[str, int]] = {}
    for report in sorted(REPORT_DIR.glob("round40_slice_*.md")):
        text = report.read_text(encoding="utf-8")
        report_summary[report.name] = {"FIX_FINE": 0, "OK_FINE": 0, "NO_FORMAL_RUBRIC": 0, "EXCLUDE": 0}
        for heading, section in section_blocks(text):
            key = extract_key(heading)
            verdict_match = re.search(r"-\s*verdict:\s*([A-Z_]+)", section)
            if verdict_match:
                verdict = verdict_match.group(1)
                report_summary[report.name][verdict] = report_summary[report.name].get(verdict, 0) + 1
            if not key or not verdict_match or verdict_match.group(1) != "FIX_FINE":
                continue
            parsed = parse_replacement(section)
            if not parsed:
                continue
            marker, lines = parsed
            overrides[key] = {"marker": marker, "lines": lines, "source_report": report.name}
    return overrides, report_summary


MANUAL_OVERRIDES: dict[str, dict[str, object]] = {
    "2024海淀二模Q18(1)": {
        "marker": "【同题组】 （按原题答题层次）",
        "lines": [
            "· 答题层次：本题8分，时政述评等级题；原题没有把共同利益单列为固定得分层。",
            "· 可用角度：可从时代主题、世界多极化、人类命运共同体、国际组织等角度作答。",
            "· 定档要求：观点明确；知识运用准确；论述合乎逻辑、条理清晰。高档要紧扣所选议题综合展开；低档多为观点不明、罗列知识、知识错误、重复题干或无效作答。",
            "· 迁移提醒：共同利益可以作为解释合作必要性的迁移语言，但不能替代原题明确列出的角度，也不能冒充单独固定分值。",
        ],
        "source_report": "manual_user_correction",
    },
    "2026海淀期中Q22(1)": {
        "marker": "【同题组】 （按原题答题层次）",
        "lines": [
            "· 答题层次：本题6分，按答案链训练，不展示固定分值层次。",
            "· 时代基础：全球治理倡议顺应和平与发展的时代潮流，符合世界各国人民共同愿望。",
            "· 核心理念：奉行主权平等、遵守国际法治、践行多边主义、倡导以人为本、注重行动导向。",
            "· 治理方向：坚定捍卫《联合国宪章》宗旨和原则，秉持共商共建共享全球治理观，直面全球治理突出问题，推动建设更加公正合理的全球治理体系。",
            "· 易错提醒：不要把未锁定的“必要性2分—重要性4分”当成固定层次；作答要围绕“为什么能获得广泛认同”。",
        ],
        "source_report": "manual_no_formal_rubric_safety",
    },
}

NO_FORMAL_LIGHT_TOUCH: dict[str, dict[str, object]] = {
    "2025海淀期中Q16(2)": {
        "marker": "【同题组】 （按原题答题层次）",
        "lines": [
            "· 答题层次：按答案链训练，不展示固定分值层次；围绕企业经营、政府支持与资源、贸易摩擦与规则三条建议链组织。",
            "· 企业经营层：客观看待“出海”的机遇与挑战，制定正确经营战略；重视海外市场考察研究，在充分了解市场信息基础上提高自主创新能力、形成竞争优势。",
            "· 政府支持与资源层：通过税收优惠等政策鼓励、支持企业积极参与经济全球化，充分利用国际国内两种资源、两个市场，打造稳定供应链、降低生产成本。",
            "· 贸易摩擦与规则层：面对国际贸易摩擦，政府和企业共同携手，充分利用国际组织赋予的权利，积极参与全球经济治理和规则制定，为企业“出海”营造良好的国际环境。",
        ],
        "source_report": "manual_no_formal_rubric_safety",
    },
    "2025海淀期中Q21(2)": {
        "marker": "【同题组】 （按原题答题层次）",
        "lines": [
            "· 答题层次：按答案链训练，不展示固定分值层次；围绕新中国外交的“变”与“不变”展开。",
            "· 变的方面：新中国外交的时代背景不断变化，政治多极化、经济全球化深入发展，和平与发展成为时代主题；中国的综合国力不断增强，国际地位不断提升，承担越来越多的国际责任；外交指导思想与时俱进，习近平外交思想为新时代中国特色大国外交提供根本遵循和行动指南。",
            "· 不变的方面：新中国外交始终服务于我国人民民主专政的国家性质；坚持独立自主的基本立场；贯彻维护世界和平、促进共同发展的宗旨；以维护我国的主权、安全和发展利益、促进世界和平与发展为基本目标；坚持以和平共处五项原则作为我国对外关系的基本准则。",
        ],
        "source_report": "manual_no_formal_rubric_safety",
    },
}


def is_entry_title(text: str) -> bool:
    return bool(re.match(r"^\d+\.\s*20\d{2}", text))


def clean_key_title(text: str) -> str | None:
    return extract_key(text)


def is_heading(text: str, p: etree._Element) -> bool:
    style = p.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
    return text.startswith("核心答题点：") or bool(style and style[0] in {"1", "2", "3", "4", "5"})


def replace_samegroups(body: etree._Element, overrides: dict[str, dict[str, object]]) -> dict:
    replaced = 0
    current_key: str | None = None
    details: list[dict] = []
    i = 0
    while i < len(body):
        elem = body[i]
        text = paragraph_text(elem) if elem.tag == qn("w:p") else ""
        if is_entry_title(text):
            current_key = clean_key_title(text)
        elif is_heading(text, elem):
            current_key = None

        if current_key in overrides and text.startswith("【同题组】"):
            override = overrides[current_key]
            marker = str(override["marker"])
            lines = [clean_student_text(str(line)) for line in override["lines"]]  # type: ignore[index]
            set_text(elem, marker)
            j = i + 1
            removed = 0
            while j < len(body):
                t = paragraph_text(body[j])
                if not t.startswith("·"):
                    break
                body.remove(body[j])
                removed += 1
            for offset, line in enumerate(lines, start=1):
                body.insert(i + offset, make_bullet(line))
            replaced += 1
            details.append(
                {
                    "key": current_key,
                    "removed": removed,
                    "inserted": len(lines),
                    "source_report": override.get("source_report", ""),
                }
            )
            i += len(lines)
        i += 1
    return {"samegroups_replaced": replaced, "details": details}


def ensure(parent: etree._Element, tag: str, *, first: bool = False) -> etree._Element:
    found = parent.find(qn(tag))
    if found is not None:
        return found
    child = etree.Element(qn(tag))
    if first:
        parent.insert(0, child)
    else:
        parent.append(child)
    return child


def emphasize_core_headings(body: etree._Element) -> int:
    count = 0
    for p in body.xpath(".//w:p", namespaces=NS):
        text = paragraph_text(p)
        if not text.startswith("核心答题点："):
            continue
        ppr = ensure(p, "w:pPr", first=True)
        p_rpr = ensure(ppr, "w:rPr")
        ensure(p_rpr, "w:b").set(qn("w:val"), "1")
        ensure(p_rpr, "w:color").set(qn("w:val"), "C00000")
        ensure(p_rpr, "w:sz").set(qn("w:val"), "24")
        for run in p.xpath(".//w:r", namespaces=NS):
            rpr = ensure(run, "w:rPr", first=True)
            ensure(rpr, "w:b").set(qn("w:val"), "1")
            ensure(rpr, "w:color").set(qn("w:val"), "C00000")
            ensure(rpr, "w:sz").set(qn("w:val"), "24")
        count += 1
    return count


def clean_all_paragraphs(body: etree._Element) -> int:
    changed = 0
    for p in body.xpath(".//w:p", namespaces=NS):
        old = paragraph_text(p)
        new = clean_student_text(old)
        if old and new != old:
            set_text(p, new)
            changed += 1
    return changed


def audit(body: etree._Element, overrides: dict[str, dict[str, object]]) -> dict:
    paras = [paragraph_text(p) for p in body.xpath(".//w:p", namespaces=NS)]
    full = "\n".join(paras)
    core_total = 0
    core_ok = 0
    core_failures: list[str] = []
    for p in body.xpath(".//w:p", namespaces=NS):
        text = paragraph_text(p)
        if not text.startswith("核心答题点："):
            continue
        core_total += 1
        runs = [r for r in p.xpath(".//w:r", namespaces=NS) if "".join(r.xpath(".//w:t/text()", namespaces=NS)).strip()]
        ok = bool(runs)
        for r in runs:
            colors = r.xpath("./w:rPr/w:color/@w:val", namespaces=NS)
            sizes = r.xpath("./w:rPr/w:sz/@w:val", namespaces=NS)
            bolds = r.xpath("./w:rPr/w:b", namespaces=NS)
            if not colors or colors[0].upper() != "C00000" or not bolds or not sizes or sizes[0] != "24":
                ok = False
                break
        if ok:
            core_ok += 1
        else:
            core_failures.append(text[:120])
    return {
        "forbidden_counts": {token: full.count(token) for token in FORBIDDEN if full.count(token)},
        "core_headings_total": core_total,
        "core_headings_red_bold_12": core_ok,
        "core_failures": core_failures[:10],
        "override_key_count": len(overrides),
        "haidian_2024_2mo_has_old_reason_layer": "原因层：共同利益或国家利益是国家合作的基础" in full,
        "yanqing_replacement_count": full.count("国家利益、国际关系、多边主义等角度可替代"),
    }


def main() -> None:
    report_overrides, report_summary = load_report_overrides()
    overrides = dict(report_overrides)
    overrides.update(MANUAL_OVERRIDES)
    overrides.update(NO_FORMAL_LIGHT_TOUCH)

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        with ZipFile(INPUT) as zin:
            zin.extractall(tmp)
        doc_xml = tmp / "word" / "document.xml"
        root = etree.fromstring(doc_xml.read_bytes())
        body = root.find(qn("w:body"))
        assert body is not None

        replacement_report = replace_samegroups(body, overrides)
        cleaned = clean_all_paragraphs(body)
        core_count = emphasize_core_headings(body)
        audit_report = audit(body, overrides)

        doc_xml.write_bytes(etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True))
        if OUTPUT.exists():
            OUTPUT.unlink()
        with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as zout:
            for path in sorted(tmp.rglob("*")):
                if path.is_file():
                    zout.write(path, path.relative_to(tmp).as_posix())

    payload = {
        "input": str(INPUT),
        "output": str(OUTPUT),
        "report_summary": report_summary,
        "parsed_fix_overrides": len(report_overrides),
        "manual_override_keys": sorted(MANUAL_OVERRIDES),
        "no_formal_light_touch_keys": sorted(NO_FORMAL_LIGHT_TOUCH),
        "replacement_report": replacement_report,
        "paragraphs_cleaned": cleaned,
        "core_headings_emphasized": core_count,
        "audit": audit_report,
    }
    AUDIT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    print(f"wrote={OUTPUT}")
    print(f"audit={AUDIT_JSON}")


if __name__ == "__main__":
    main()
