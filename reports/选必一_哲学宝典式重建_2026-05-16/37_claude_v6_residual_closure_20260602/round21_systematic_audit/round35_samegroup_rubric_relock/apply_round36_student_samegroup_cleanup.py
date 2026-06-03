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
INPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_同题组回源重锁_核心答题点红色强调_带水印_20260603.docx")
OUTPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_同题组细则再锁_学生版无工程痕迹_带水印_20260603.docx")
AUDIT_JSON = BASE_DIR / "round36_student_cleanup_audit.json"

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
ensure = R35.ensure
emphasize_core_headings = R35.emphasize_core_headings
is_entry_title = R35.is_entry_title
clean_key_title = R35.clean_key_title
is_heading = R35.is_heading


CHAOYANG_2025_Q21_LINES = [
    "· 答题层次：本题8分，按“中国的发展需要—区域的发展需要—世界的发展需要”三层组织；同一关键词不重复，语言要有层次、无知识错误",
    "· 从中国的发展需要角度看（3分）：必要性1分，可写周边国家众多、符合我国与周边国家地理环境和文化发展状况、国际形势出现深刻变化；重要性任意两点2分，可写实现发展繁荣的重要基础、提高开放型经济水平、维护国家安全、为国家发展创造良好外部环境、运筹外交全局、推动构建人类命运共同体",
    "· 从区域的发展需要角度看（3分）：共同的国家利益是国际合作基础，中国与周边国家有广泛共同利益，或写我国坚持独立自主的和平外交政策、维护世界和平、促进共同发展，任意一点1分；与周边国家开展贸易，促进经济融合和共同发展、促进区域经济一体化、促进区域贸易和投资自由化便利化，任意一点1分；创新区域合作机制、搭建合作平台，维护地区和平稳定或区域安全，推动构建周边国家命运共同体，任意一点1分",
    "· 从世界的发展需要角度看（2分）：携手周边国家推动建设以合作共赢为核心的新型国际关系、推动国际关系民主化、实现真正的多边主义、推动全球治理变革，任意一点1分；通过区域经济合作维护和推动全球自由贸易、多边贸易，或推动经济全球化朝开放、包容、普惠、平衡、共赢方向发展，任意一点1分",
    "· 答题提醒：同一个关键词不重复计分；整体语言要有层次、有问题意识，不能把知识点机械堆在一起",
]


STUDENT_SAFE_SAMEGROUP_OVERRIDES = {
    "2026丰台期末Q20": [
        "· 作答提示：本题围绕“五大工程如何扩大中拉利益汇合点”组织，要扣住团结、发展、文明、和平、民心五类工程，再说明它们如何扩大中拉共同利益",
        "· 工程对应：团结工程强调国际关系和制度基础；发展工程强调发展合作、产业链供应链和开放环境；文明工程强调文明交流互鉴；和平工程强调安全合作；民心工程强调民生项目和人员交流",
        "· 易错提醒：不要把四大全球倡议题或五年规划综合题的评分层次直接搬到本题；必须回到“五大工程—利益汇合点—中拉命运共同体”的题目主线",
    ],
    "2025朝阳二模Q21": CHAOYANG_2025_Q21_LINES,
    "2026丰台二模Q20": [
        "· 作答提示：围绕自由贸易试验区、自由贸易港建设的背景和作用组织，不把相关术语机械罗列成答案",
        "· 背景理由：符合经济全球化发展趋势，顺应和平、发展、合作、共赢的时代潮流",
        "· 中国开放理由：坚持对外开放基本国策，坚持引进来和走出去并重，推进高水平对外开放",
        "· 互利共赢理由：坚持互利共赢，推动跨境金融、离岸贸易、高端制造等新业态蓬勃发展，助力全球产业链供应链稳定畅通",
        "· 全球治理理由：坚持多边主义，推动经济全球化朝更加开放、包容、普惠、平衡、共赢方向发展，推动构建人类命运共同体",
    ],
    "2026丰台期末Q21": [
        "· 作答提示：本题按短评题组织，要围绕主题、观点、论证和逻辑展开，不把四个倡议机械罗列成答案",
        "· 可用主线：四大全球倡议为构建人类命运共同体凝聚合力",
        "· 可用角度：共商共建共享的全球治理观；相互尊重、公平正义、合作共赢的新型国际关系；践行真正的多边主义；中国推动构建人类命运共同体",
        "· 写作要求：围绕主题、观点明确、论证充分、逻辑清晰、学科术语规范",
    ],
    "2025朝阳一模Q20": [
        "· 作答提示：围绕产业链供应链新态势的应对方向组织，不只写开放合作",
        "· 态势判断：题面涉及断链风险、绿色认证、数字技术和国际规则竞争",
        "· 应对方向：多元化布局、区域化合作、绿色化转型、数字化加速",
        "· 总体落点：通过高水平对外开放、参与全球治理和畅通国内国际双循环，在全球产业变革中赢得主动",
    ],
    "2025海淀一模Q21(2)": [
        "· 作答提示：围绕外贸连上两个万亿级台阶的原因组织，避免偏离到政治多极化等无关方向",
        "· 开放政策：实施更加积极主动的开放战略，以政策促进贸易自由化便利化，通过综合保税区等形式降低贸易成本，畅通国际贸易",
        "· 贸易结构：发展绿色贸易、数字贸易，推动货物贸易优化升级，打造产品出口竞争新优势",
        "· 市场与合作：依托我国超大规模市场优势，为世界各国提供更加广阔的市场，促进国际合作，实现互利共赢",
        "· 易错提醒：不要误写政治多极化、独立自主和平外交政策、比较优势等偏题方向",
    ],
    "2025东城一模Q21": [
        "· 作答提示：本题是教育强国综合题，不作为《当代国际政治与经济》专门同题组展开",
        "· 迁移提醒：不能把“人才与国际竞争力”“综合国力和国际竞争力”单独扩成选必一固定同题组",
    ],
    "2026通州期末Q21": [
        "· 作答提示：本题是中国式现代化综合多模块题，不作为《当代国际政治与经济》专门同题组展开",
        "· 迁移提醒：不能因为出现“高水平对外开放”“独立自主、自力更生”就扩成选必一固定同题组",
    ],
    "2026门头沟一模Q21": [
        "· 评分结构：本题10分，选必一只保留材料三的国政经角度，不扩成全题同题组",
        "· 国政经角度：结合材料三，用《当代国际政治与经济》知识阐释中国为世界提供确定性，可写大国担当、互利共赢的开放战略、构建人类命运共同体等；材料逻辑是中国与世界经济深度联动、与全球各方共享机遇、对外投资和跨国企业在华投资",
        "· 迁移提醒：材料一主要对应中国特色社会主义、哲学或思维；材料二主要对应《经济与社会》，不要把两部分都扩成选必一同题组",
    ],
    "2024丰台一模Q21": [
        "· 作答提示：本题是开放等级题和多模块题，不作固定同题组展开",
        "· 选必一迁移：可把构建人类命运共同体、全人类共同价值等作为开放题中的选必一角度使用",
        "· 等级要求：需要从多个不同维度展开分析，综合运用两个模块知识，不能只罗列选必一术语",
    ],
}


FORBIDDEN_REPLACEMENTS = [
    ("证据边界：", "作答提示："),
    ("细则边界：", "作答提示："),
    ("源卡为阅卷前参考答案，按“为什么开创周边工作新局面”的理由链组织，不再写成六桶并集", "按“为什么开创周边工作新局面”的理由链组织，不把相关术语机械罗列成答案"),
    ("源卡为参考答案结构，按原答案理由链组织，不再扩成六桶并集", "按题目理由链组织，不把相关术语机械罗列成答案"),
    ("源卡为参考答案与阅卷提示，按外贸连上两个万亿级台阶的原因组织", "围绕外贸连上两个万亿级台阶的原因组织"),
    ("源卡为旧核查表稳定抓手，按产业链供应链新态势的应对方向组织", "围绕产业链供应链新态势的应对方向组织"),
    ("本题为“四大全球倡议”短评题，正式细则层级偏弱，按短评题综合迁移标注，不作为逐点固定细则", "本题按短评题组织，围绕主题、观点、论证和逻辑展开"),
    ("正式细则层级偏弱", "按题目要求综合展开"),
    ("不作为逐点固定细则", "不要机械罗列"),
    ("源卡", ""),
    ("证据卡", ""),
    ("证据层级：", ""),
    ("证据层级", ""),
    ("回源", "核对"),
    ("细则复练", ""),
    ("正式细则含", "评分层次包含"),
    ("细则明确", "评分层次提示"),
    ("作答边界：", "作答提醒："),
    ("评分边界：", "评分提醒："),
    ("边界提示：", "易错提醒："),
    ("材料与逻辑边界：", "材料与逻辑提醒："),
    ("选必一迁移边界：", "选必一迁移提醒："),
    ("迁移边界：", "迁移提醒："),
    ("使用边界：", "使用提醒："),
    ("暂不展示正式同题组", "本题只保留本条答题点"),
    ("正式同题组", "同题组"),
    ("逐点评分细则/评标层次", "评分层次"),
    ("待补充同题正式评分层次后再生成同题组文本", "不要机械借用其他题型的评分结构"),
    ("按用户复核的六点正式细则组织", "按六点评分层次组织"),
    ("按六点评分层次组织", "按六点答题层次组织"),
    ("【同题组】 （按原题评分层次）", "【同题组】 （按原题答题层次）"),
    ("· 评分结构：", "· 答题层次："),
    ("评分层次包含", "答题层次包含"),
    ("评分层次提示", "答题层次提示"),
    ("评分提醒：", "答题提醒："),
    ("评分层次", "答题层次"),
    ("评分结构", "答题结构"),
    ("不能写成固定六桶全覆盖", "不能写成六要素罗列"),
    ("本题是教育强国综合题，不作为《当代国际政治与经济》专门同题组展开", "本题按教育强国综合题处理，不按《当代国际政治与经济》专门同题组展开"),
    ("本题是中国式现代化综合多模块题，不作为《当代国际政治与经济》专门同题组展开", "本题按中国式现代化综合多模块题处理，不按《当代国际政治与经济》专门同题组展开"),
    ("本题10分，选必一只保留材料三的国政经角度，不扩成全题同题组", "本题10分，选必一重点看材料三的国政经角度，不按全题综合题展开"),
    ("不作固定扩展", "不按固定题型展开"),
    ("不作固定同题组展开", "不按固定同题组展开"),
    ("可锁定", "可确认"),
    ("未锁定", "未确认"),
    ("待复核", "待确认"),
    ("正式主链", "正文"),
    ("正文条目", "正文"),
    ("工程痕迹", ""),
    ("后台", ""),
    ("raw_cards", ""),
    ("BLOCKED", ""),
    ("backend", ""),
    ("audit", ""),
    ("source", ""),
    ("risk", ""),
    ("round", ""),
    ("v7", ""),
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
    "v7",
]

OLD_BUCKET_RESIDUES = [
    "· 时代背景：",
    "· 理论：",
    "· 经济全球化：",
    "· 政治多极化：",
    "· 中国：",
    "· 联合国：",
]


def clean_student_text(text: str) -> str:
    cleaned = text
    for old, new in FORBIDDEN_REPLACEMENTS:
        cleaned = cleaned.replace(old, new)
    cleaned = re.sub(r"\s{2,}", " ", cleaned)
    cleaned = cleaned.replace("·  ", "· ")
    return cleaned.strip()


def replace_student_samegroups(body: etree._Element) -> dict:
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

        if current_key in STUDENT_SAFE_SAMEGROUP_OVERRIDES and txt.startswith("【同题组】"):
            set_text(p, "【同题组】  （按原题评分层次）")
            j = i + 1
            removed = 0
            while j < len(body):
                t = paragraph_text(body[j])
                if not t.startswith("· "):
                    break
                body.remove(body[j])
                removed += 1
            lines = STUDENT_SAFE_SAMEGROUP_OVERRIDES[current_key]
            for offset, line in enumerate(lines, start=1):
                body.insert(i + offset, make_bullet(line))
            replaced += 1
            details.append({"key": current_key, "removed_lines": removed, "inserted_lines": len(lines)})
            i += len(lines)
        i += 1
    return {"student_safe_samegroups_replaced": replaced, "details": details}


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


def remove_old_bucket_residue_paragraphs(body: etree._Element) -> int:
    removed = 0
    for p in list(body.xpath(".//w:p", namespaces=NS)):
        txt = paragraph_text(p)
        if any(txt.startswith(prefix) for prefix in OLD_BUCKET_RESIDUES):
            parent = p.getparent()
            if parent is not None:
                parent.remove(p)
                removed += 1
    return removed


def audit_body(body: etree._Element) -> dict:
    paras = [paragraph_text(p) for p in body.xpath(".//w:p", namespaces=NS)]
    all_text = "\n".join(paras)
    forbidden = {pat: all_text.count(pat) for pat in FORBIDDEN_PATTERNS if all_text.count(pat)}
    old_bucket = {pat: all_text.count(pat) for pat in OLD_BUCKET_RESIDUES if all_text.count(pat)}
    core_total = 0
    core_red = 0
    for p in body.xpath(".//w:p", namespaces=NS):
        if not paragraph_text(p).startswith("核心答题点："):
            continue
        core_total += 1
        run_colors = p.xpath(".//w:rPr/w:color/@w:val", namespaces=NS)
        run_bolds = p.xpath(".//w:rPr/w:b", namespaces=NS)
        if run_colors and all(c.upper() == "C00000" for c in run_colors) and run_bolds:
            core_red += 1
    chaoyang_blocks = []
    for i, t in enumerate(paras):
        if "2025朝阳二模Q21" in t:
            chaoyang_blocks.append(paras[i : i + 10])
    return {
        "forbidden": forbidden,
        "old_bucket_residue": old_bucket,
        "core_headings_total": core_total,
        "core_headings_deep_red_bold": core_red,
        "chaoyang_2025_q21_blocks": chaoyang_blocks[:6],
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

        report = replace_student_samegroups(body)
        report["student_text_paragraphs_cleaned"] = clean_all_paragraphs(body)
        report["old_bucket_residue_paragraphs_removed"] = remove_old_bucket_residue_paragraphs(body)
        report["core_headings_deep_red"] = emphasize_core_headings(body)
        audit = audit_body(body)
        report["audit"] = audit

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
