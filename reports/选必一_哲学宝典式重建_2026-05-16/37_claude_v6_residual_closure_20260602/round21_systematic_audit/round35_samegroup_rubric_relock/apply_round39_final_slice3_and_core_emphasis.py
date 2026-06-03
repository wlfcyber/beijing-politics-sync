#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from lxml import etree


BASE_DIR = Path(__file__).resolve().parent
ROUND38 = BASE_DIR / "apply_round38_rubric_audit_fixes.py"

INPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_同题组全量细则复核首批修正版_学生版_带水印_20260603.docx")
OUTPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_同题组全量细则复核最终修正版_核心答题点红色强化_学生版_带水印_20260603.docx")
AUDIT_JSON = BASE_DIR / "round39_final_slice3_and_core_emphasis.json"

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def load_round38():
    spec = importlib.util.spec_from_file_location("round38", ROUND38)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


R38 = load_round38()
qn = R38.qn
paragraph_text = R38.paragraph_text


SLICE3_OVERRIDES: dict[str, dict[str, list[str] | str]] = {
    "2026海淀期中Q22(1)": {
        "marker": "【同题组】 （按原题答题层次）",
        "lines": [
            "· 答题层次：本题6分，按“必要性2分—重要性4分”组织，不能只堆知识点。",
            "· 必要性（2分）：全球治理倡议顺应和平与发展的时代潮流（1分）；符合各国共同利益、共同愿望，弘扬全人类共同价值，推动构建人类命运共同体（1分）。",
            "· 重要性（4分）：全球治理角度2分，写秉持共商共建共享全球治理观，推动建设更加公正合理的全球治理体系；联合国角度1分，写捍卫《联合国宪章》宗旨和原则；国际关系角度1分，写推进国际关系民主化、推动构建新型国际关系或国际政治经济新秩序。",
            "· 作答要求：每个重要性层次都要结合全球治理倡议的核心理念展开；只推知识、不回应材料，该层次最多2分；不按必要性和重要性的逻辑回应，单纯知识堆砌最多3分。",
        ],
    },
    "2025朝阳一模Q20": {
        "marker": "【同题组】 （按原题答题层次）",
        "lines": [
            "· 答题层次：本题8分，围绕全球产业链供应链新态势，从多元化布局、区域化合作、绿色化转型、数字化加速四个特点分别作答，最后进行总结；每个特点要写出“措施+效果”。",
            "· 多元化布局：鼓励和支持有实力的跨国公司在全球范围内分散投资，利用世界各地优势组织生产经营，顺应经济全球化趋势推进产业链多元化布局；效果可写促进产业链供应链多元化，维护多元稳定的国际经济格局和经贸关系，维护产业链供应链安全。",
            "· 区域化合作：可写深化区域经济合作，秉持亲诚惠容理念，加强与周边国家和地区经济合作，促进区域内投资和贸易自由化便利化，推动区域产业链供应链深度融合；也可写吸引更多外资和高端产业留在或落户中国；还可写坚持独立自主、自力更生，加强核心技术攻关，提升产业链自主可控能力，增强产业链供应链韧性和抗风险能力。",
            "· 绿色化转型：坚持绿色发展理念，加大绿色技术研发投入，完善绿色法律法规，对接国际规则与标准，制定环境政策；效果可写提升产业链绿色化水平，推进绿色低碳转型。",
            "· 数字化加速：推动产业数字化，促进数字技术与实体经济深度融合，推动互联网、大数据、人工智能与实体经济融合，加大数字技术研发投入；效果可写培育数字产品和服务新优势，提升产业链数字化水平和竞争新优势。",
            "· 总结提升：积极参与全球经济治理和规则制定，维护多边贸易体系；发展更高水平开放型经济，形成国内大循环为主体、国内国际双循环相互促进的新发展格局；推动构建开放型世界经济或人类命运共同体。",
        ],
    },
    "2024海淀期中Q16(2)": {
        "marker": "【同题组】 （按原题答题层次）",
        "lines": [
            "· 答题层次：本题选必一部分2分，主体是政府，围绕“路径+结果”作答。",
            "· 政府路径：企业和政府可利用国际组织赋予的权利，积极参与全球经济治理和规则制定。",
            "· 作答结果：为企业“出海”营造良好的国际环境。",
            "· 不采分边界：市场监管、营商环境、建立产权保护制度等不作为本题选必一得分点；党、人大立法等其他模块知识不作为本题选必一得分点。",
        ],
    },
}


EXTRA_TEXT_REPLACEMENTS = [
    ("不采分边界", "易错边界"),
    ("正式评标可采点", "原题答题角度"),
    ("按评标参考角度组织", "按原题答题角度组织"),
    ("评标参考角度", "原题答题角度"),
    ("正式评标", "原题要求"),
    ("评标", "答题要求"),
]

EXTRA_FORBIDDEN = ["评标"]


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


def force_core_answer_style(body: etree._Element) -> int:
    changed = 0
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
        changed += 1
    return changed


def audit_core_style(body: etree._Element) -> dict:
    total = 0
    red_bold_12 = 0
    failures = []
    for p in body.xpath(".//w:p", namespaces=NS):
        text = paragraph_text(p)
        if not text.startswith("核心答题点："):
            continue
        total += 1
        visible_runs = [r for r in p.xpath(".//w:r", namespaces=NS) if "".join(r.xpath(".//w:t/text()", namespaces=NS)).strip()]
        ok = True
        for r in visible_runs:
            colors = r.xpath("./w:rPr/w:color/@w:val", namespaces=NS)
            bold = r.xpath("./w:rPr/w:b", namespaces=NS)
            sizes = r.xpath("./w:rPr/w:sz/@w:val", namespaces=NS)
            if not colors or colors[0].upper() != "C00000" or not bold or not sizes or sizes[0] != "24":
                ok = False
                break
        if ok and visible_runs:
            red_bold_12 += 1
        else:
            failures.append(text[:120])
    return {"core_total": total, "core_red_bold_12": red_bold_12, "core_failures": failures[:10]}


def main() -> None:
    R38.INPUT = INPUT
    R38.OUTPUT = OUTPUT
    R38.AUDIT_JSON = AUDIT_JSON
    R38.SAMEGROUP_OVERRIDES.update(SLICE3_OVERRIDES)
    for old, new in EXTRA_TEXT_REPLACEMENTS:
        if (old, new) not in R38.TEXT_REPLACEMENTS:
            R38.TEXT_REPLACEMENTS.append((old, new))
    for token in EXTRA_FORBIDDEN:
        if token not in R38.FORBIDDEN_PATTERNS:
            R38.FORBIDDEN_PATTERNS.append(token)
    R38.emphasize_core_headings = force_core_answer_style

    R38.main()

    # Add a stricter core-style audit after the inherited script writes its report.
    import zipfile

    with zipfile.ZipFile(OUTPUT) as zf:
        root = etree.fromstring(zf.read("word/document.xml"))
    body = root.find(qn("w:body"))
    assert body is not None
    audit = json.loads(AUDIT_JSON.read_text(encoding="utf-8"))
    audit["strict_core_style"] = audit_core_style(body)
    AUDIT_JSON.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"strict_core_style": audit["strict_core_style"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
