from __future__ import annotations

import importlib.util
import re
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


INPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_第30轮海淀二模正细则修正版_带水印_20260603.docx")
OUTPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_第31轮正式细则漏项修正版_带水印_20260603.docx")
HELPER = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/37_claude_v6_residual_closure_20260602/round21_systematic_audit/apply_round29_user_omission_fix.py")

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def load_helper():
    spec = importlib.util.spec_from_file_location("round29_helper", HELPER)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


H = load_helper()
qn = H.qn
paragraph_text = H.paragraph_text
make_blank = H.make_blank
make_title = H.make_title
make_field = H.make_field
make_bullet = H.make_bullet


PROMPTS = {
    "2026朝阳二模Q20(2)": "结合材料，运用《当代国际政治与经济》知识，分析人类命运共同体理念为什么能维护世界和平与发展。（6分）",
    "2026西城期末Q20": "结合材料，运用《当代国际政治与经济》知识，阐释参与全球气候治理的中国实践。",
    "2026房山二模Q20": "2026年3月30日，世界数据组织（简称WDO）在北京成立，旨在“弥合数据鸿沟、释放数据价值、繁荣数字经济”。结合材料，运用《当代国际政治与经济》知识，分析世界数据组织完善全球数据治理，服务全球数字经济发展的智慧。",
    "2026通州一模Q19": "元首外交掌舵航向。结合材料，运用《当代国际政治与经济》知识，分析中国元首外交如何为世界注入稳定性与正能量。（8分）",
}


SAME_GROUPS = {
    "2026朝阳二模Q20(2)": [
        "· 理论：国家间共同利益是国家合作的基础",
        "· 政治多极化：在平等互利基础上开展合作，实现互利共赢；践行真正的多边主义；共商共建共享的全球治理观；推动全球治理体系变革完善，建立更加公正合理的国际政治经济新秩序",
        "· 中国：贡献中国智慧、中国方案、中国力量",
    ],
    "2026西城期末Q20": [
        "· 时代背景：和平与发展仍是时代主题",
        "· 理论：国家间共同利益是国家合作的基础",
        "· 政治多极化：共商共建共享的全球治理观；推动国际秩序和全球治理体系更加公正合理；践行真正的多边主义；推动构建人类命运共同体",
        "· 中国：贡献中国智慧、中国方案、中国力量；中国推进绿色低碳转型并参与全球气候治理；严格落实《巴黎协定》要求，每五年向联合国提交国家自主贡献目标，维护全球气候治理多边进程；中国是负责任大国并勇于担当；坚持正确义利观",
        "· 联合国：坚定维护以联合国为核心的国际体系和以国际法为基础的国际秩序",
    ],
    "2026房山二模Q20": [
        "· 理论：共同利益是合作的基础",
        "· 经济全球化：推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展；数据要素在全球范围内流动",
        "· 政治多极化：世界多极化是当今国际形势的突出特点；在平等互利基础上开展合作，实现互利共赢；共商共建共享的全球治理观；践行真正的多边主义",
        "· 中国：坚持正确义利观",
    ],
    "2026通州一模Q19": [
        "· 时代背景：和平与发展仍是时代主题",
        "· 理论：共同利益是合作的基础；维护国家利益是主权国家对外活动的出发点和落脚点",
        "· 经济全球化：推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展",
        "· 政治多极化：相互尊重、公平正义、合作共赢的新型国际关系；国际关系民主化与国际政治经济新秩序；共商共建共享的全球治理观；推动构建人类命运共同体",
        "· 中国：中国特色大国外交与人类命运共同体；坚持正确义利观",
        "· 联合国：遵循联合国宪章宗旨和原则",
    ],
}


NEW_ENTRIES = [
    {
        "key": "2026朝阳二模Q20(2)",
        "core": "践行真正的多边主义",
        "title": "2026朝阳二模Q20(2)人类命运共同体理念维护世界和平与发展",
        "trigger": "细则角度2写明“倡导合作共赢”，并把“坚持多边主义”列为可替代关键词；材料要求分析人类命运共同体理念为什么能维护世界和平与发展，指向超越零和博弈、通过多边合作解决全球性问题。",
        "why": "看到细则把“坚持多边主义”放在合作共赢角度中，就不能只写一般合作或中国方案。人类命运共同体理念维护和平与发展，关键在于反对单边和零和逻辑，依靠多边合作协调各国行动。",
        "answer": "人类命运共同体理念倡导多边合作，反对单边主义和零和博弈，有利于各国共同应对全球性问题，维护世界和平与发展。",
    },
    {
        "key": "2026朝阳二模Q20(2)",
        "core": "共商共建共享的全球治理观",
        "title": "2026朝阳二模Q20(2)人类命运共同体理念维护世界和平与发展",
        "trigger": "细则角度2明确将“共商共建共享”作为倡导合作共赢的可替代关键词，题目又围绕人类命运共同体理念维护世界和平与发展展开。",
        "why": "人类命运共同体理念不是单方治理方案，而是要求各国共同参与全球治理。细则中“共商共建共享”提示学生把合作共赢具体落实到全球治理方式上。",
        "answer": "人类命运共同体理念坚持共商共建共享，推动各国共同参与全球治理、共同建设治理机制、共享治理成果，从而减少冲突、促进共同发展。",
    },
    {
        "key": "2026朝阳二模Q20(2)",
        "core": "推动全球治理体系变革完善，建立更加公正合理的国际政治经济新秩序",
        "title": "2026朝阳二模Q20(2)人类命运共同体理念维护世界和平与发展",
        "trigger": "细则角度3写明“提供中国方案”，并把“国际新秩序/新型国际关系”列为可替代关键词；答案句强调推动构建更加公正合理的国际治理体系。",
        "why": "题目问理念为什么能维护和平与发展，不能只停在价值宣示。细则把中国方案同国际新秩序、新型国际关系相连，说明答题应落到全球治理体系和国际秩序更加公正合理。",
        "answer": "人类命运共同体理念为解决全球性问题提供中国方案，推动全球治理体系变革完善，促进国际秩序朝更加公正合理方向发展。",
    },
    {
        "key": "2026西城期末Q20",
        "core": "和平与发展仍是时代主题",
        "title": "2026西城期末Q20参与全球气候治理中的中国实践",
        "trigger": "正式细则角度2写明“国际背景：和平发展合作共赢是时代潮流/非传统安全威胁”，材料围绕全球气候治理这一跨国共同挑战展开。",
        "why": "气候治理不是单纯国内绿色发展题，而是和平与发展时代主题下的全球共同治理议题。细则把时代潮流列为得分角度，提示应先交代中国参与治理的国际背景。",
        "answer": "和平与发展仍是时代主题，气候变化等非传统安全威胁需要国际社会合作应对，中国参与全球气候治理顺应和平、发展、合作、共赢的时代潮流。",
    },
    {
        "key": "2026西城期末Q20",
        "core": "国家间共同利益是国家合作的基础",
        "title": "2026西城期末Q20参与全球气候治理中的中国实践",
        "trigger": "正式细则角度2将“共同利益”单列为1分，材料中全球气候治理、可持续发展、清洁世界都指向各国共同利益。",
        "why": "看到细则把共同利益单列，就不能只用大国担当或中国方案概括。气候变化影响所有国家，中国参与全球气候治理的合作基础正在于各国维护生态安全和可持续发展的共同利益。",
        "answer": "国家间共同利益是国家合作的基础。应对气候变化、促进全球可持续发展符合各国共同利益，中国参与全球气候治理有利于推动国际合作。",
    },
    {
        "key": "2026西城期末Q20",
        "core": "践行真正的多边主义",
        "title": "2026西城期末Q20参与全球气候治理中的中国实践",
        "trigger": "正式细则角度2在“中国理念”中列出“践行真正的多边主义”，参考答案也写中国维护全球气候治理多边进程。",
        "why": "气候治理需要多边机制和国际协作。材料中落实《巴黎协定》、向联合国提交国家自主贡献目标，正是中国维护多边进程、反对单边治理的具体表现。",
        "answer": "中国践行真正的多边主义，落实《巴黎协定》并维护全球气候治理多边进程，推动各国以多边合作共同应对气候变化。",
    },
    {
        "key": "2026西城期末Q20",
        "core": "推动构建人类命运共同体",
        "title": "2026西城期末Q20参与全球气候治理中的中国实践",
        "trigger": "正式细则角度2把“命运共同体”列入中国理念，参考答案也写维护联合国核心作用、促进全球可持续发展、推动构建人类命运共同体。",
        "why": "气候变化是典型的共同命运议题，任何国家都不能独善其身。中国参与全球气候治理，体现的是把本国绿色发展同人类共同未来相连接的命运共同体路径。",
        "answer": "中国参与全球气候治理，推动各国共同应对气候变化、促进全球可持续发展，有利于推动构建人类命运共同体。",
    },
    {
        "key": "2026西城期末Q20",
        "core": "坚持正确义利观",
        "title": "2026西城期末Q20参与全球气候治理中的中国实践",
        "trigger": "正式细则角度2在“中国理念”中明确列出“正确义利观”，材料强调中国承担气候治理责任并为发展中国家应对气候变化提供系统性方案。",
        "why": "气候治理中的中国实践既维护本国发展利益，也兼顾全球可持续发展和发展中国家合理关切。细则列出正确义利观，提示学生要把责任担当与利益兼顾联系起来。",
        "answer": "中国坚持正确义利观，在推进自身绿色低碳转型的同时承担国际责任、贡献治理方案，兼顾本国利益与全球共同利益。",
    },
    {
        "key": "2026西城期末Q20",
        "core": "坚定维护以联合国为核心的国际体系和以国际法为基础的国际秩序",
        "title": "2026西城期末Q20参与全球气候治理中的中国实践",
        "trigger": "正式细则角度3写明“维护联合国的核心作用/完善全球治理体系”，材料写中国向联合国提交国家自主贡献目标并落实《巴黎协定》。",
        "why": "全球气候治理离不开联合国框架和国际法规则。看到《巴黎协定》、联合国、国家自主贡献目标，应把中国实践提升到维护以联合国为核心的国际体系和国际法秩序上。",
        "answer": "中国落实《巴黎协定》、向联合国提交国家自主贡献目标，维护联合国在全球气候治理中的核心作用，坚定维护以联合国为核心的国际体系和以国际法为基础的国际秩序。",
    },
    {
        "key": "2026房山二模Q20",
        "core": "世界多极化是当今国际形势的突出特点",
        "title": "2026房山二模Q20世界数据组织完善全球数据治理",
        "trigger": "正式评标写明“世界数据组织顺应经济全球化和世界多极化的趋势”，并在给分点中列出“世界多极化1分”。",
        "why": "世界数据组织不是单一国家平台，而是推动各方参与数据治理、制定和互认标准的国际组织化实践。细则明确给“世界多极化”1分，应把它落在世界多极化趋势，而不是泛化为全球南方表达。",
        "answer": "世界数据组织顺应世界多极化趋势，推动各方平等参与全球数据治理规则制定和标准互认，服务全球数字经济发展。",
    },
    {
        "key": "2026房山二模Q20",
        "core": "在平等互利基础上开展合作，实现互利共赢",
        "title": "2026房山二模Q20世界数据组织完善全球数据治理",
        "trigger": "正式评标把“合作共赢”单列为1分，并写明“推动技术联合研发，促进数智技术创新，合作共赢、弥补数据鸿沟”。",
        "why": "题目问世界数据组织服务全球数字经济发展的智慧，材料中的技术联合研发和标准互认不是单向输出，而是各方在平等互利基础上的合作。细则单列合作共赢，必须作为独立迁移点保留。",
        "answer": "世界数据组织推动技术联合研发和标准互认，促进各方在平等互利基础上合作，实现互利共赢，弥合数据鸿沟。",
    },
    {
        "key": "2026房山二模Q20",
        "core": "践行真正的多边主义",
        "title": "2026房山二模Q20世界数据组织完善全球数据治理",
        "trigger": "正式评标把“共商共建共享/全球治理观/真正的多边主义”列为同一给分点，说明全球数据治理要依靠多方共同参与。",
        "why": "世界数据组织搭建平台、推动标准制定和互认，体现的不是单边治理，而是多边协同治理。细则把真正的多边主义列为可得分表达，提示学生可从多边主义角度迁移。",
        "answer": "世界数据组织践行真正的多边主义，搭建全球数据治理合作平台，推动各方共同制定、对接和互认数据治理标准。",
    },
    {
        "key": "2026通州一模Q19",
        "core": "维护国家利益是主权国家对外活动的出发点和落脚点",
        "title": "2026通州一模Q19中国元首外交为世界注入稳定性与正能量",
        "trigger": "正式评标可采点包括“兼顾他国合理关切”，材料要求分析中国元首外交如何为世界注入稳定性与正能量。",
        "why": "元首外交既维护我国发展和安全利益，也通过兼顾他国合理关切推动合作。看到细则中的“兼顾他国合理关切”，应迁移到国家利益与国际合作的关系，而不是只写一般外交贡献。",
        "answer": "维护国家利益是主权国家对外活动的出发点和落脚点。中国元首外交在维护我国国家利益的同时兼顾他国合理关切，为世界注入稳定性与正能量。",
    },
    {
        "key": "2026通州一模Q19",
        "core": "推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展",
        "title": "2026通州一模Q19中国元首外交为世界注入稳定性与正能量",
        "trigger": "正式评标可采点包括“多边贸易体制、经济全球化方向”，材料中的元首外交通过国际合作机制推动开放合作。",
        "why": "元首外交不是只有政治安全意义，也服务开放合作和世界经济稳定。细则明确给出多边贸易体制和经济全球化方向，说明应把经济全球化的正确方向纳入同题组。",
        "answer": "中国元首外交维护多边贸易体制，推动经济全球化朝更加开放、包容、普惠、平衡、共赢方向发展，为世界经济稳定注入正能量。",
    },
    {
        "key": "2026通州一模Q19",
        "core": "共商共建共享的全球治理观",
        "title": "2026通州一模Q19中国元首外交为世界注入稳定性与正能量",
        "trigger": "正式评标可采点包括“共商共建共享的全球治理观”，材料强调元首外交推动国际合作和全球治理。",
        "why": "中国元首外交通过会晤、倡议和合作机制推动各方共同参与治理。细则列出共商共建共享，提示要把外交行动上升为全球治理方式。",
        "answer": "中国元首外交坚持共商共建共享的全球治理观，推动各方共同参与全球治理体系改革和建设，增强国际合作的稳定性。",
    },
    {
        "key": "2026通州一模Q19",
        "core": "推动构建人类命运共同体",
        "title": "2026通州一模Q19中国元首外交为世界注入稳定性与正能量",
        "trigger": "正式评标可采点包括“人类命运共同体”，题目要求说明中国元首外交为世界注入稳定性与正能量。",
        "why": "元首外交的落点不是零散外事活动，而是通过合作应对共同挑战、维护共同发展。细则列出人类命运共同体，说明答案应指向中国外交的总体价值方向。",
        "answer": "中国元首外交推动构建人类命运共同体，推动各国在共同挑战中加强合作，为世界和平发展注入稳定性与正能量。",
    },
    {
        "key": "2026通州一模Q19",
        "core": "坚持正确义利观",
        "title": "2026通州一模Q19中国元首外交为世界注入稳定性与正能量",
        "trigger": "正式评标可采点包括“正确义利观”，材料强调中国元首外交为世界注入稳定性和正能量。",
        "why": "中国元首外交不仅追求自身发展利益，也关注世界和平发展和他国合理关切。细则列出正确义利观，提示应把中国外交的义利统一写出来。",
        "answer": "中国元首外交坚持正确义利观，兼顾本国利益和他国合理关切，以负责任行动推动共同发展和国际稳定。",
    },
]


def is_heading(p: etree._Element, text: str) -> bool:
    style = p.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
    return text.startswith("核心答题点：") or bool(style and style[0] in {"1", "2", "3", "4", "5"})


def is_entry_title(text: str) -> bool:
    return bool(re.match(r"^\d+\.\s*20\d{2}", text))


def clean_key_title(title: str) -> str | None:
    m = re.search(r"(20\d{2}.+?Q\d+(?:\(\d+\))?)", title.replace(" ", ""))
    return m.group(1) if m else None


def section_bounds(body: etree._Element, core: str) -> tuple[int, int]:
    children = list(body)
    start = None
    for i, child in enumerate(children):
        if paragraph_text(child) == f"核心答题点：{core}":
            start = i
            break
    if start is None:
        raise RuntimeError(f"core not found: {core}")
    end = len(children)
    for j in range(start + 1, len(children)):
        txt = paragraph_text(children[j])
        if is_heading(children[j], txt):
            end = j
            break
    return start, end


def section_has_key(body: etree._Element, start: int, end: int, key: str) -> bool:
    for p in list(body)[start:end]:
        if key in paragraph_text(p):
            return True
    return False


def next_number(body: etree._Element, start: int, end: int) -> int:
    nums = []
    for p in list(body)[start:end]:
        m = re.match(r"^(\d+)\.\s*20\d{2}", paragraph_text(p))
        if m:
            nums.append(int(m.group(1)))
    return (max(nums) + 1) if nums else 1


def entry_paragraphs(number: int, data: dict[str, str]) -> list[etree._Element]:
    key = data["key"]
    return [
        make_blank(),
        make_blank(),
        make_title(f"{number}. {data['title']}"),
        make_field("【材料触发点】", data["trigger"]),
        make_field("【设问】", PROMPTS[key]),
        make_field("【为什么能想到】", data["why"]),
        make_field("【答案落点】", data["answer"]),
        make_field("【同题组】", ""),
        *[make_bullet(x) for x in SAME_GROUPS[key]],
    ]


def remove_entry_for_key_under_core(body: etree._Element, key: str, core: str) -> int:
    start, end = section_bounds(body, core)
    children = list(body)
    removed = 0
    i = start + 1
    while i < end and i < len(body):
        txt = paragraph_text(body[i])
        if is_entry_title(txt) and key in txt:
            j = i + 1
            while j < len(body):
                t = paragraph_text(body[j])
                if is_entry_title(t) or is_heading(body[j], t):
                    break
                j += 1
            for _ in range(j - i):
                body.remove(body[i])
            removed += 1
            end -= (j - i)
            continue
        i += 1
    return removed


def insert_missing_entries(body: etree._Element) -> int:
    inserted = 0
    for data in NEW_ENTRIES:
        key = data["key"]
        core = data["core"]
        start, end = section_bounds(body, core)
        if section_has_key(body, start, end, key):
            continue
        n = next_number(body, start, end)
        for p in reversed(entry_paragraphs(n, data)):
            body.insert(end, p)
        inserted += 1
    return inserted


def replace_samegroups(body: etree._Element) -> int:
    replaced = 0
    i = 0
    current_key = None
    while i < len(body):
        p = body[i]
        txt = paragraph_text(p) if p.tag == qn("w:p") else ""
        if is_entry_title(txt):
            current_key = clean_key_title(txt)
        elif is_heading(p, txt):
            current_key = None
        if current_key in SAME_GROUPS and txt.startswith("【同题组】"):
            j = i + 1
            while j < len(body):
                t = paragraph_text(body[j])
                if not t.startswith("· "):
                    break
                body.remove(body[j])
            for offset, line in enumerate(SAME_GROUPS[current_key], start=1):
                body.insert(i + offset, make_bullet(line))
            replaced += 1
            i += len(SAME_GROUPS[current_key])
        i += 1
    return replaced


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        with ZipFile(INPUT) as zin:
            zin.extractall(tmp)
        doc_xml = tmp / "word" / "document.xml"
        root = etree.fromstring(doc_xml.read_bytes())
        body = root.find(qn("w:body"))
        assert body is not None

        removed = remove_entry_for_key_under_core(body, "2026房山二模Q20", "世界多极化与全球南方联合自强")
        inserted = insert_missing_entries(body)
        replaced = replace_samegroups(body)

        doc_xml.write_bytes(etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True))
        if OUTPUT.exists():
            OUTPUT.unlink()
        with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as zout:
            for path in sorted(tmp.rglob("*")):
                if path.is_file():
                    zout.write(path, path.relative_to(tmp).as_posix())

    print(f"wrote={OUTPUT}")
    print(f"removed={removed}")
    print(f"inserted={inserted}")
    print(f"replaced_samegroups={replaced}")


if __name__ == "__main__":
    main()
