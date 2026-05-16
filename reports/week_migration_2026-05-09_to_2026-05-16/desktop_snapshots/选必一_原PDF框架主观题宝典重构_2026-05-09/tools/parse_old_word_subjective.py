#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


RUN = Path("/Users/wanglifei/Desktop/北京高考政治/选必一_原PDF框架主观题宝典重构_2026-05-09")
TEXT_PATH = RUN / "02_old_doc_audit" / "old_doc_text_from_word.txt"
OLD_AUDIT = RUN / "02_old_doc_audit"
FILTER = RUN / "03_subjective_filter"


ELEMENTS = ["时代背景", "理论", "经济全球化", "政治多极化", "中国", "联合国"]


POLLUTION_TERMS = [
    "治理赤字",
    "全球性挑战",
    "逆全球化",
    "零和博弈",
    "百年未有之大变局",
    "制度型开放",
    "全球南方",
    "NDC",
    "气候治理框架",
    "30秒读题法",
    "六桶读题总图",
    "题型堆点模型",
    "按题训练闭环",
    "慎用与跨模块表达积累",
    "细则新增点接入总表",
    "题源索引",
    "核心点索引",
    "后台字段",
    "点位性质",
    "正式细则",
    "非正式细则",
    "卷面层级",
    "补丁题链",
    "见对应题号",
    "答案见本题正确项",
]


REMOVED_STRUCTURES = [
    "目录中的旧四部分结构",
    "0. 30 秒读题法",
    "第一部分：六桶读题总图",
    "第三部分：按题训练闭环",
    "第四部分：慎用与跨模块表达积累",
    "旧稿按核心知识点直接生成的小框架",
    "补丁题链",
    "后台字段/细则字段/卷面层级字段",
]


# Mapping status:
# - PDF原框架术语: the term is directly in the extracted PDF framework.
# - 考题增补术语: real old-Word subjective answer material can be hung under a PDF framework but not used as a framework.
# - 候选新增角度: cannot safely be hung under a PDF framework without user confirmation.
MAPPING = {
    "和平与发展仍是时代主题": ("时代背景", "机遇", "和平与发展是时代的主题", "PDF原框架术语", ""),
    "全球性挑战、逆全球化、保护主义和治理赤字凸显": ("政治多极化", "单边", "反对单边主义和贸易保护主义", "考题增补术语", "旧核心包含治理赤字/全球性挑战，不作为时代背景原框架；仅将贸易保护主义、逆全球化材料挂靠到 PDF“单边”。"),
    "霸权主义、强权政治、单边主义、零和博弈": ("时代背景", "挑战", "霸权主义；强权政治", "PDF原框架术语", "零和博弈不作为 PDF 原框架，只保留 PDF 已有霸权主义/强权政治。"),
    "在动荡变化的时代为国际社会注入稳定性和确定性": ("中国", "责任", "承担大国责任；发挥建设性作用", "考题增补术语", "稳定性和确定性不改写为小框架，只作为中国责任类卷面表达。"),
    "国家间共同利益是国家合作的基础": ("理论", "共同利益", "共同利益是国家间合作的基础", "PDF原框架术语", ""),
    "当前国际竞争的实质是以经济和科技实力为基础的综合国力较量": ("中国", "一条历史线", "中国的综合国力增强；国际地位提升", "考题增补术语", "国际竞争实质不进入 PDF 小框架；只作为综合国力/国际地位题的增补表达。"),
    "维护国家利益并兼顾他国合理关切，坚持正确义利观": ("理论", "共同利益", "维护本国利益的同时兼顾他国合理关切", "PDF原框架术语", "正确义利观只作同层增补，不新设框架。"),
    "在平等互利基础上开展合作": ("理论", "共同利益", "共同利益是国家间合作的基础", "考题增补术语", "平等互利是合作基础的卷面化表达，不新设框架。"),
    "处理好中国发展和世界发展的关系": ("中国", "责任", "承担大国责任；发挥建设性作用", "考题增补术语", "作为中国责任与建设性作用下的增补表达。"),
    "处理好发展和安全的关系；统筹发展和安全": ("理论", "国家安全", "国家安全是最高国家利益", "考题增补术语", "发展和安全关系只挂国家安全，不新设理论框架。"),
    "处理好自力更生和对外开放的关系": ("经济全球化", "开", "推进我国高水平对外开放", "考题增补术语", "自力更生不作为 PDF 原框架，仅用于开放关系题。"),
    "核心技术自主可控；把握创新主动权": ("中国", "一条历史线", "中国的综合国力增强；国际地位提升", "考题增补术语", "核心技术不作为 PDF 原框架，仅作为综合国力/竞争力材料表达。"),
    "建设开放型世界经济，参与全球经济治理和规则制定": ("经济全球化", "开", "发展更高层次的开放型经济；推进我国高水平对外开放", "考题增补术语", "制度型开放、规则制定均须标注考题增补，挂在 PDF“开”。"),
    "推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展": ("经济全球化", "总", "推动经济全球化朝着更加开放、包容、普惠、平衡、共赢的方向发展", "PDF原框架术语", ""),
    "充分利用国内国际两个市场、两种资源，增强国内国际循环联动": ("经济全球化", "兼", "充分利用国内国际两个市场；充分利用国内国际两种资源", "PDF原框架术语", "国内国际循环联动作为考题增补表达，不改变“兼”框架。"),
    "推动贸易和投资自由化便利化": ("经济全球化", "贸资", "推动贸易投资自由化便利化", "PDF原框架术语", ""),
    "促进生产要素全球流动、资源优化配置、优势互补和国际分工合作": ("经济全球化", "环", "促进要素自由流动；优化资源配置", "PDF原框架术语", "优势互补/国际分工合作作增补表达。"),
    "维护产业链供应链安全稳定，形成多元稳定的国际经济格局和经贸关系": ("经济全球化", "环", "产业结构优化升级；促进要素自由流动", "考题增补术语", "产业链供应链稳定不新设框架，挂在经济环节。"),
    "中国新能源汽车发展促进资源优化配置和国际贸易，让经济全球化更有活力": ("经济全球化", "配", "优化资源配置", "PDF原框架术语", "国际贸易活力挂靠贸资/配，不新设框架。"),
    "提升贸易投资合作质量和水平": ("经济全球化", "贸资", "推动贸易投资自由化便利化", "考题增补术语", "质量和水平是题中表达，不新设框架。"),
    "共商共建共享的全球治理观": ("政治多极化", "完善全球治理", "倡导共商共建共享的全球治理观", "PDF原框架术语", ""),
    "推动国际关系民主化，坚持真正的多边主义，推动国际秩序朝公正合理方向发展": ("政治多极化", "民主", "推动国际关系民主化；坚持真正的多边主义", "PDF原框架术语", "公正合理国际秩序作为增补表达。"),
    "推动建设相互尊重、公平正义、合作共赢的新型国际关系": ("政治多极化", "新国关", "有利于构建相互尊重、公平正义、合作共赢的新型国际关系", "PDF原框架术语", ""),
    "世界多极化深入发展与平等有序的世界多极化": ("政治多极化", "多极化", "坚持平等有序的多极化", "PDF原框架术语", "世界多极化深入发展同时可触发时代背景机遇。"),
    "全球治理应坚持开放、合作、共享、共赢、包容和共商共建": ("政治多极化", "完善全球治理", "完善全球治理；倡导共商共建共享的全球治理观", "考题增补术语", "开放合作共享共赢包容只作全球治理增补表达。"),
    "坚持共同但有区别的责任，发达国家应承担更多责任": ("政治多极化", "完善全球治理", "完善全球治理", "考题增补术语", "气候治理原则不新设框架，挂全球治理。"),
    "推动构建人类命运共同体": ("政治多极化", "共体", "有利于构建人类命运共同体", "PDF原框架术语", ""),
    "国际发展合作、南南合作与“小而美”项目": ("中国", "责任", "承担大国责任；发挥建设性作用", "考题增补术语", "南南合作/小而美不作为 PDF 小框架，挂中国责任。"),
    "贡献中国智慧、中国方案、中国力量与全球倡议体系": ("中国", "智慧", "中国智慧；中国方案", "PDF原框架术语", "全球倡议体系只作为考题增补表达。"),
    "中国特色大国外交、独立自主和平外交政策与周边命运共同体": ("中国", "政策", "我国奉行独立自主的和平外交政策", "PDF原框架术语", "周边命运共同体只作增补表达。"),
    "坚持正确义利观，在发展合作中义利相兼、互利共赢": ("理论", "共同利益", "维护本国利益的同时兼顾他国合理关切", "考题增补术语", "PDF第7页旁注有义利观，但不作为六要素小框架。"),
    "中国作为负责任大国积极参与全球治理并推动全球南方现代化": ("中国", "责任", "承担大国责任；发挥建设性作用", "考题增补术语", "全球南方现代化不作为 PDF 小框架。"),
    "中国作为负责任大国积极参与全球气候治理": ("中国", "责任", "承担大国责任；发挥建设性作用", "考题增补术语", "NDC/气候治理只作责任增补。"),
    "中国平等开放、合作共享的全球治理理念": ("中国", "智慧", "中国智慧；中国方案", "考题增补术语", "理念表达挂中国智慧。"),
    "中非携手推进现代化": ("中国", "责任", "承担大国责任；发挥建设性作用", "考题增补术语", "中非现代化不作为 PDF 小框架。"),
    "坚定维护本国利益，坚持互利共赢、和平谈判并推动贸易自由便利": ("理论", "共同利益", "维护本国利益的同时兼顾他国合理关切", "考题增补术语", "同时可触发贸资，但不新设框架。"),
    "改善民生、促进就业和经济社会发展，提升当地民众获得感": ("经济全球化", "民", "民生福祉；增加就业岗位；提高居民收入", "PDF原框架术语", ""),
    "自觉履行国际义务，遵循国际法，承担国际责任": ("中国", "责任", "承担大国责任；发挥建设性作用", "考题增补术语", "国际义务不新设框架。"),
    "《联合国宪章》宗旨和原则": ("联合国", "联合国", "遵循联合国宪章宗旨原则", "PDF原框架术语", ""),
    "以联合国为核心的国际体系、联合国作用与中国的联合国身份": ("联合国", "联合国", "践行多边主义的最佳场所", "考题增补术语", "以联合国为核心等不作为新小框架。"),
    "在联合国和《巴黎协定》框架下维护多边气候治理机制，推动全球治理体系完善": ("联合国", "联合国", "践行多边主义的最佳场所；遵循联合国宪章宗旨原则", "考题增补术语", "巴黎协定/NDC语境只作联合国增补。"),
    "联合国对中国的对外开放和现代化事业作出了独特贡献，成为中国开展多边合作的主要舞台": ("联合国", "联合国", "践行多边主义的最佳场所", "考题增补术语", "联合国贡献不新设框架。"),
}


ENTRY_RE = re.compile(r"^\s*\d+\.\s+(20\d{2}.+?Q\d+(?:\(\d+\))?)（主观题）\s*$")
FIELD_RE = re.compile(r"^【([^】]+)】\s*(.*)$")


def source_parts(raw: str):
    year = raw[:4]
    middle = raw[4:]
    q_match = re.search(r"(Q\d+(?:\(\d+\))?)", raw)
    q = q_match.group(1) if q_match else ""
    region_exam = middle[: middle.find(q)] if q else middle
    return year, region_exam.strip(), q


def find_core_headings(lines):
    heads = {}
    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            continue
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        if j < len(lines) and lines[j].strip().startswith("一句话抓手"):
            heads[i] = s
    return heads


def parse_entries(lines):
    starts = [i for i, l in enumerate(lines) if l.strip() == "第二部分：按核心知识点触发宝典"]
    start = starts[-1]
    end = next((i for i, l in enumerate(lines[start + 1 :], start + 1) if l.strip() == "第三部分：按题训练闭环"), len(lines))
    core_heads = find_core_headings(lines)
    entries = []
    current_element = ""
    current_core = ""
    i = start
    while i < end:
        s = lines[i].strip()
        if s in ELEMENTS:
            current_element = s
        if i in core_heads:
            current_core = core_heads[i]
        m = ENTRY_RE.match(s)
        if m:
            source = m.group(1)
            fields = {}
            j = i + 1
            while j < end:
                nxt = lines[j].strip()
                if ENTRY_RE.match(nxt) or j in core_heads or nxt in ELEMENTS:
                    break
                fm = FIELD_RE.match(nxt)
                if fm:
                    fields[fm.group(1)] = fm.group(2).strip()
                j += 1
            year, region_exam, q = source_parts(source)
            element, frame, pdf_term, status, note = MAPPING.get(current_core, ("", "", "", "候选新增角度", "未找到安全映射。"))
            missing = [name for name in ["材料触发点", "设问", "为什么能想到", "踩分词", "答案落点"] if not fields.get(name)]
            skip_reasons = []
            if missing:
                skip_reasons.append("缺字段：" + "、".join(missing))
            if "见对应题号" in fields.get("设问", "") or "答案见本题正确项" in fields.get("答案落点", ""):
                skip_reasons.append("占位题链")
            if "（主观题）" not in s:
                skip_reasons.append("非主观题")
            if status == "候选新增角度":
                skip_reasons.append("无法安全挂靠到 PDF 小框架")
            entries.append({
                "旧稿记录ID": f"OLD-{len(entries)+1:04d}",
                "旧稿核心标题": current_core,
                "旧稿章节": current_element,
                "题源": source,
                "年份": year,
                "区县考试": region_exam,
                "题号": q,
                "是否主观题": "是",
                "PDF六要素": element,
                "PDF小框架": frame,
                "对应答题术语": pdf_term,
                "术语性质": status,
                "映射说明": note,
                "材料触发点": fields.get("材料触发点", ""),
                "设问": fields.get("设问", ""),
                "为什么能想到": fields.get("为什么能想到", ""),
                "踩分词": fields.get("踩分词", ""),
                "答案落点": fields.get("答案落点", ""),
                "筛选结论": "保留" if not skip_reasons else "排除",
                "排除原因": "；".join(skip_reasons),
            })
            i = j
            continue
        i += 1
    return entries


def write_csv(path, rows, fieldnames):
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_pollution_report(text):
    counts = Counter({term: text.count(term) for term in POLLUTION_TERMS})
    lines = [
        "# 旧稿污染项审计",
        "",
        "定位：旧 Word 只能作为主观题题源池、材料触发点素材池、设问素材池、答案句素材池、术语候选池；不得抽取或新增 PDF 小框架。",
        "",
        "## 禁止作为正文原框架的旧稿内容",
        "",
    ]
    for term in POLLUTION_TERMS:
        lines.append(f"- {term}：旧稿出现 {counts[term]} 次；处理为污染项/候选素材，不作为 PDF 原框架小框架。")
    lines += [
        "",
        "## 处理规则",
        "",
        "- PDF 没有的小框架一律不进入正文主框架。",
        "- 若某词来自主观题答案或细则，最多以【考题增补术语】挂靠到 PDF 已有小框架，并保留题源。",
        "- 不能安全挂靠的，进入 `03_audit/candidate_new_angle_report.md`。",
    ]
    (OLD_AUDIT / "old_doc_pollution_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_removed_structure_report(text):
    lines = [
        "# 旧稿结构移除报告",
        "",
        "以下内容只用于审计，不进入最终正文结构：",
        "",
    ]
    for item in REMOVED_STRUCTURES:
        lines.append(f"- {item}")
    lines += [
        "",
        "正文目标结构已重置为：六要素 -> PDF 小框架 -> 答题术语 -> 主观题出处 -> 四段触发链。",
        "",
        "旧稿保留价值：题源、设问、材料触发点、踩分词、答案落点。",
    ]
    (OLD_AUDIT / "old_doc_removed_structure_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_filter_reports(entries):
    kept = [e for e in entries if e["筛选结论"] == "保留"]
    excluded = [e for e in entries if e["筛选结论"] != "保留"]
    objective_like = [e for e in entries if re.search(r"\b[ABCD][、.．]", e["设问"])]
    incomplete = excluded

    lines = [
        "# 客观题/选择题移除报告",
        "",
        f"- 旧稿第二部分解析记录：{len(entries)} 条。",
        f"- 检出 A/B/C/D 选择题样式：{len(objective_like)} 条。",
        f"- 进入主观题素材池的选择题数量：0。",
        f"- 进入主观题素材池的客观题数量：0。",
        "",
        "说明：本轮只解析 `（主观题）` 条目；旧稿目录、总图、按题闭环、补丁题链不进入主观题素材池。",
    ]
    (FILTER / "objective_question_removed_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    lines = [
        "# 不完整/不可挂靠题目报告",
        "",
        f"- 排除记录：{len(incomplete)} 条。",
        "",
    ]
    for e in incomplete:
        lines.append(f"- {e['旧稿记录ID']} {e['题源']}｜{e['旧稿核心标题']}｜{e['排除原因']}")
    (FILTER / "incomplete_question_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    return kept, excluded


def add_pdf_term_duplicates(entries):
    kept = [e for e in entries if e["筛选结论"] == "保留"]
    existing = {(e["题源"], e["PDF六要素"], e["PDF小框架"], e["对应答题术语"], e["旧稿核心标题"]) for e in kept}
    additions = []

    def maybe_add(e, element, frame, term, status, reason, tag):
        key = (e["题源"], element, frame, term, e["旧稿核心标题"])
        if key in existing:
            return
        existing.add(key)
        ne = dict(e)
        ne["旧稿记录ID"] = f"{e['旧稿记录ID']}-{tag}"
        ne["PDF六要素"] = element
        ne["PDF小框架"] = frame
        ne["对应答题术语"] = term
        ne["术语性质"] = status
        ne["映射说明"] = reason
        additions.append(ne)

    for e in kept:
        blob = "；".join([e["材料触发点"], e["设问"], e["为什么能想到"], e["踩分词"], e["答案落点"]])
        if "霸权主义" in blob or "强权政治" in blob:
            maybe_add(e, "时代背景", "挑战", "霸权主义；强权政治", "PDF原框架术语", "同题材料/踩分词出现霸权主义或强权政治，补挂 PDF“挑战”。", "PDFCHALLENGE")
        if "营商环境" in blob:
            maybe_add(e, "经济全球化", "营", "优化营商环境；国际化、市场化、法治化营商环境", "PDF原框架术语", "同题答案句出现营商环境，补挂 PDF“营”。", "PDFBUSINESS")
        if ("共建国家" in blob and ("经济增长" in blob or "经济复苏" in blob or "发展" in blob or "国际经济合作" in blob or "融入经济全球化" in blob)) or "推动成员国经济复苏" in blob:
            maybe_add(e, "经济全球化", "国", "推动成员国经济复苏；共建国家经济增长", "PDF原框架术语", "同题材料/答案出现共建国家经济增长或成员国经济复苏，补挂 PDF“国”。", "PDFCOUNTRY")
        if "习近平外交思想" in blob:
            maybe_add(e, "中国", "一条主线", "习近平外交思想为新时代中国特色大国外交提供了根本遵循和行动指南", "PDF原框架术语", "同题踩分词出现习近平外交思想，补挂 PDF“一条主线”。", "PDFXJP")

    return entries + additions


def main():
    OLD_AUDIT.mkdir(parents=True, exist_ok=True)
    FILTER.mkdir(parents=True, exist_ok=True)
    text = TEXT_PATH.read_text(encoding="utf-8")
    lines = text.splitlines()
    entries = parse_entries(lines)
    entries = add_pdf_term_duplicates(entries)
    fields = [
        "旧稿记录ID", "旧稿核心标题", "旧稿章节", "题源", "年份", "区县考试", "题号", "是否主观题",
        "PDF六要素", "PDF小框架", "对应答题术语", "术语性质", "映射说明",
        "材料触发点", "设问", "为什么能想到", "踩分词", "答案落点", "筛选结论", "排除原因",
    ]
    write_csv(OLD_AUDIT / "old_doc_candidate_material_pool.csv", entries, fields)
    kept, excluded = write_filter_reports(entries)
    write_csv(FILTER / "subjective_question_pool.csv", kept, fields)
    write_pollution_report(text)
    write_removed_structure_report(text)
    print(f"parsed={len(entries)} kept={len(kept)} excluded={len(excluded)}")
    print(OLD_AUDIT / "old_doc_pollution_report.md")
    print(FILTER / "subjective_question_pool.csv")


if __name__ == "__main__":
    main()
