#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import re
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


BASE_DIR = Path(__file__).resolve().parent
ROUND35 = BASE_DIR / "apply_round35_samegroup_rubric_relock.py"
INPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_同题组细则再锁_核心答题点红色强化_学生版_带水印_20260603.docx")
OUTPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_同题组全量细则复核首批修正版_学生版_带水印_20260603.docx")
AUDIT_JSON = BASE_DIR / "round38_rubric_audit_fixes.json"

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


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
emphasize_core_headings = R35.emphasize_core_headings
is_entry_title = R35.is_entry_title
clean_key_title = R35.clean_key_title
is_heading = R35.is_heading


SAMEGROUP_OVERRIDES: dict[str, dict[str, list[str] | str]] = {
    "2024丰台一模Q20": {
        "marker": "【同题组】 （按原题得分方式）",
        "lines": [
            "· 答题层次：本题7分，按“知识+材料”的论述质量给分；只写纯知识或只描述材料，属于低档。",
            "· 分档方式：围绕下列四个方面展开，任选三方面且论述到位可达6-7分，任选二方面为4-5分，任选一方面为2-3分；没有论述或论述严重偏差为0-1分。",
            "· 四个方面：建立和完善基础设施，推动产品、服务和生产要素在全球流动；加快供应链金融创新，缓解供应链发展中的资金短缺；打造国际经济合作交流平台，推进贸易投资自由化便利化；运用先进技术降低成本、提高效率，畅通全球产业链供应链，增强经济全球化活力，推动各国合作共赢。",
        ],
    },
    "2026西城一模Q20(2)": {
        "marker": "【同题组】 （按原题答题层次）",
        "lines": [
            "· 答题层次：本题8分，按标准规则2分、产业链供应链3分、综合意义2分、联系材料1分组织。",
            "· 标准规则（2分）：降低制度性交易成本/提高贸易效率（1分）；促进贸易投资便利化自由化、优化营商环境、破除贸易壁垒（1分）。",
            "· 产业链供应链（3分）：维护经济安全、统筹安全与发展、形成多元稳定经贸关系（1分）；发挥比较优势、优势互补、深度加入国际分工（1分）；促进产业协同、产业结构优化升级，带动就业、收入和税收（1分）。",
            "· 综合意义（2分）：对区域，推动地区经济转型升级、增强竞争力，或提升发展中国家的代表性和发言权、打破发达国家规则制定中的垄断主导（1分）；对世界，坚持合作共赢、开放包容和共同利益，维护多边贸易和多边主义，推动全球经济治理体系改革（1分）。",
            "· 联系材料（1分）：结合中国—东盟自贸区3.0版的具体安排作说明。",
        ],
    },
    "2024朝阳一模Q21": {
        "marker": "【同题组】 （按原题答题层次）",
        "lines": [
            "· 答题层次：本题9分，按4+5结构组织；先用4分概括我国当前经济形势，再用5分回答如何在变局中开新局。",
            "· 分析我国当前经济形势（4分）：经济总量持续增长、经济增速保持稳健；我国经济进入以新发展理念引领的高质量发展阶段；外部环境日趋严峻、风险挑战增多；我国经济保持强大韧性和良好势头，在世界经济中的地位和贡献稳步提升。",
            "· 政治多极化维度：面对外部风险挑战，要维护我国主权、安全和发展利益，在谋求本国发展中促进各国共同发展，坚持合作共赢，推动建设新型国际关系，推动构建人类命运共同体，为我国发展营造良好外部环境。",
            "· 经济全球化维度：依托我国超大规模市场优势，增强国内国际两个市场两种资源联动效应，深度参与全球产业分工和合作，推进高水平对外开放，构建国内国际双循环相互促进的新发展格局，同时坚持独立自主、自力更生，把发展主动权牢牢掌握在自己手中。",
            "· 得分提醒：开新局部分要从政治多极化、经济全球化两个维度展开；只写一个维度，最高不超过3分。",
        ],
    },
    "2026顺义一模Q20": {
        "marker": "【同题组】 （按原题答题层次）",
        "lines": [
            "· 答题层次：本题7分，按“共同利益必答 + 国际政治3分 + 国际经济3分”组织。",
            "· 必答基础：国家间共同利益是国家合作的基础，科技小院回应全球南方农业发展、人才培养、绿色发展和可持续发展的共同需求。",
            "· 国际政治：和平与发展是时代主题；构建人类命运共同体是习近平外交思想的核心理念；可结合独立自主的和平外交政策、外交政策宗旨、正确义利观、新型国际关系、合作共赢、互利共赢、共享发展成果说明南南合作为什么能成为典范。",
            "· 国际经济：科技小院输出农业技术、提升生产率、降低成本、培养本土人才、激发内生发展动力，体现经济全球化朝普惠、平衡、共赢方向发展，让更多全球南方国家共享发展成果。",
        ],
    },
    "2026房山二模Q20": {
        "marker": "【同题组】 （按原题答题层次）",
        "lines": [
            "· 答题层次：本题8分，围绕世界数据组织完善全球数据治理、服务全球数字经济发展的中国智慧展开。",
            "· 治理方向：普惠包容的经济全球化、平等有序的世界多极化，共同利益/共同发展，合作共赢/互利共赢。",
            "· 治理方式：坚持共商共建共享的全球治理观、践行真正的多边主义，推动数据要素在全球范围内流动。",
            "· 材料落点：结合世界数据组织弥合数据鸿沟、释放数据价值、繁荣数字经济，说明中国智慧如何服务全球数字经济发展。",
        ],
    },
    "2026丰台期末Q21": {
        "marker": "【同题组】 （按原题答题层次）",
        "lines": [
            "· 答题层次：本题8分，短评题，围绕“四大全球倡议为构建人类命运共同体凝聚磅礴合力”展开。",
            "· 核心问题：不是简单罗列四个倡议，而是说明四大全球倡议如何推动构建人类命运共同体。",
            "· 整体主线：四大全球倡议顺应和平与发展的时代主题，回应全球性问题和治理赤字，为世界提供公共产品，为构建人类命运共同体凝聚合力。",
            "· 论证角度：可从四大全球倡议的本质、当前世界形势的必要性、四大全球倡议的作用三个角度展开；可使用多边主义、共商共建共享、相互尊重、公平正义、合作共赢的新型国际关系等知识。",
            "· 高分写法：围绕四大全球倡议整体展开三层论证；也可以分别写全球发展、全球安全、全球文明、全球治理倡议，但要有总说，不能只摘抄材料。",
        ],
    },
    "2026丰台期末Q20": {
        "marker": "【同题组】 （同主题练习提醒）",
        "lines": [
            "· 本题适合作为同主题训练，不按固定得分层次展开。",
            "· 练习主线：围绕“五大工程如何扩大中拉利益汇合点”组织，扣住团结、发展、文明、和平、民心五类工程。",
            "· 可写方向：说明五大工程如何扩大中拉共同利益、促进互利共赢，并推动中拉命运共同体建设。",
        ],
    },
    "2026丰台一模Q19": {
        "marker": "【同题组】 （同主题练习提醒）",
        "lines": [
            "· 本题适合作为同主题训练，不按固定得分层次展开。",
            "· 可写方向：围绕全球治理、中国担当、人类命运共同体、多边主义、正确义利观等组织答案。",
            "· 易错提醒：不要把其他题目的逐点层次直接套到本题。",
        ],
    },
    "2026海淀一模Q20": {
        "marker": "【同题组】 （同主题练习提醒）",
        "lines": [
            "· 本题适合作为同主题训练，不按固定得分层次展开。",
            "· 可写方向：围绕制度型开放、两个市场两种资源、国际标准贡献、全球治理规则制定等组织。",
            "· 易错提醒：写中国标准走出国门时，要同时说明国内开放基础和国际治理意义。",
        ],
    },
    "2024石景山一模Q19(2)": {
        "marker": "【同题组】 （同主题练习提醒）",
        "lines": [
            "· 本题适合作为同主题训练，不按固定得分层次展开。",
            "· 可写方向：顺应经济全球化趋势，利用比较优势优化资源配置，降低生产贸易成本，打造国际竞争新优势，并通过技术交流与资源共享实现合作共赢。",
        ],
    },
    "2026丰台二模Q20": {
        "marker": "【同题组】 （同主题练习提醒）",
        "lines": [
            "· 本题适合作为同主题训练，不按固定得分层次展开。",
            "· 可写方向：自由贸易试验区、自由贸易港建设符合经济全球化和开放合作趋势，有利于推进高水平对外开放、稳定全球产业链供应链、推动经济全球化朝更加开放包容普惠平衡共赢方向发展。",
            "· 易错提醒：不要把参考性答案当成固定得分层次照搬。",
        ],
    },
    "2025海淀一模Q21(2)": {
        "marker": "【同题组】 （同主题练习提醒）",
        "lines": [
            "· 本题适合作为同主题训练，不按固定得分层次展开。",
            "· 可写方向：围绕我国外贸连上两个万亿级台阶的原因组织，可写开放战略、贸易自由化便利化、绿色贸易和数字贸易、超大规模市场优势、国际合作和互利共赢。",
            "· 易错提醒：不要偏离到政治多极化、独立自主和平外交政策等无关方向。",
        ],
    },
    "2025东城一模Q21": {
        "marker": "【同题组】 （综合题提醒）",
        "lines": [
            "· 本题按教育强国综合题处理，不按《当代国际政治与经济》固定同题组展开。",
            "· 迁移提醒：不能把“人才与国际竞争力”“综合国力和国际竞争力”单独扩成选必一固定同题组。",
        ],
    },
    "2026通州期末Q21": {
        "marker": "【同题组】 （综合题提醒）",
        "lines": [
            "· 本题按中国式现代化综合多模块题处理，不按《当代国际政治与经济》固定同题组展开。",
            "· 迁移提醒：不能因为出现“高水平对外开放”“独立自主、自力更生”就扩成选必一固定同题组。",
        ],
    },
}


TEXT_REPLACEMENTS = [
    ("参考答案按", "可按"),
    ("参考答案也写维护联合国核心作用、促进全球可持续发展、推动构建人类命运共同体", "题目也指向维护联合国核心作用、促进全球可持续发展、推动构建人类命运共同体"),
    ("参考答案也写中国维护全球气候治理多边进程", "题目也指向中国维护全球气候治理多边进程"),
    ("正式细则角度2把“命运共同体”列入中国理念，题目也指向维护联合国核心作用、促进全球可持续发展、推动构建人类命运共同体。", "题目围绕中国参与全球气候治理的理念与行动展开，“命运共同体”提示应把中国实践放到促进全球可持续发展和推动构建人类命运共同体中理解。"),
    ("正式细则角度2在“中国理念”中列出“践行真正的多边主义”，题目也指向中国维护全球气候治理多边进程。", "题目围绕中国参与全球气候治理的理念与行动展开，“践行真正的多边主义”提示应把中国实践放到维护全球气候治理多边进程中理解。"),
    ("按原题三层评分细则组织", "按原题三层得分层次组织"),
    ("按细则三项组织", "按三项答题要求组织"),
    ("加细则补充", "加答题要求补充"),
    ("评分细则", "得分层次"),
    ("正式细则", "答题要求"),
    ("细则", "答题要求"),
    ("评分", "得分"),
    ("事实证据", "事实支撑"),
    ("核心证据", "关键支撑"),
    ("材料证据", "材料支撑"),
    ("实践证据", "实践支撑"),
    ("证据", "支撑"),
]

FORBIDDEN_PATTERNS = [
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
    "评分",
    "证据",
    "按原题评分层次",
    "评分结构",
    "六桶全覆盖",
]


def clean_student_text(text: str) -> str:
    cleaned = text
    for old, new in TEXT_REPLACEMENTS:
        cleaned = cleaned.replace(old, new)
    cleaned = re.sub(r"\s{2,}", " ", cleaned).strip()
    return cleaned


def replace_samegroups(body: etree._Element) -> dict:
    replaced = 0
    details: list[dict] = []
    current_key: str | None = None
    i = 0
    while i < len(body):
        p = body[i]
        txt = paragraph_text(p) if p.tag == qn("w:p") else ""
        if is_entry_title(txt):
            current_key = clean_key_title(txt)
        elif is_heading(txt, p):
            current_key = None

        if current_key in SAMEGROUP_OVERRIDES and txt.startswith("【同题组】"):
            override = SAMEGROUP_OVERRIDES[current_key]
            set_text(p, str(override["marker"]))
            j = i + 1
            removed = 0
            while j < len(body):
                t = paragraph_text(body[j])
                if not t.startswith("· "):
                    break
                body.remove(body[j])
                removed += 1
            lines = list(override["lines"])  # type: ignore[arg-type]
            for offset, line in enumerate(lines, start=1):
                body.insert(i + offset, make_bullet(line))
            replaced += 1
            details.append({"key": current_key, "removed_lines": removed, "inserted_lines": len(lines), "marker": override["marker"]})
            i += len(lines)
        i += 1
    return {"samegroups_replaced": replaced, "details": details}


def clean_all_paragraphs(body: etree._Element) -> int:
    changed = 0
    for p in body.xpath(".//w:p", namespaces=NS):
        txt = paragraph_text(p)
        if not txt:
            continue
        cleaned = clean_student_text(txt)
        if cleaned != txt:
            set_text(p, cleaned)
            changed += 1
    return changed


def audit_body(body: etree._Element) -> dict:
    paras = [paragraph_text(p) for p in body.xpath(".//w:p", namespaces=NS)]
    full = "\n".join(paras)
    forbidden = {x: full.count(x) for x in FORBIDDEN_PATTERNS if full.count(x)}
    core_total = 0
    core_red = 0
    for p in body.xpath(".//w:p", namespaces=NS):
        if not paragraph_text(p).startswith("核心答题点："):
            continue
        core_total += 1
        run_colors = p.xpath(".//w:rPr/w:color/@w:val", namespaces=NS)
        run_bolds = p.xpath(".//w:rPr/w:b", namespaces=NS)
        run_sizes = p.xpath(".//w:rPr/w:sz/@w:val", namespaces=NS)
        if run_colors and all(c.upper() == "C00000" for c in run_colors) and run_bolds and run_sizes:
            core_red += 1
    return {
        "forbidden_counts": forbidden,
        "core_headings_total": core_total,
        "core_headings_red_bold": core_red,
        "marker_counts": {
            "同主题练习提醒": full.count("【同题组】 （同主题练习提醒）"),
            "综合题提醒": full.count("【同题组】 （综合题提醒）"),
        },
    }


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        with ZipFile(INPUT) as zin:
            zin.extractall(tmp)
        doc_xml = tmp / "word" / "document.xml"
        root = etree.fromstring(doc_xml.read_bytes())
        body = root.find(qn("w:body"))
        assert body is not None

        report = replace_samegroups(body)
        report["paragraphs_cleaned"] = clean_all_paragraphs(body)
        report["core_headings_emphasized"] = emphasize_core_headings(body)
        report["audit"] = audit_body(body)

        doc_xml.write_bytes(etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True))
        if OUTPUT.exists():
            OUTPUT.unlink()
        with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as zout:
            for path in sorted(tmp.rglob("*")):
                if path.is_file():
                    zout.write(path, path.relative_to(tmp).as_posix())

    AUDIT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    print(f"wrote={OUTPUT}")
    print(f"audit={AUDIT_JSON}")


if __name__ == "__main__":
    main()
