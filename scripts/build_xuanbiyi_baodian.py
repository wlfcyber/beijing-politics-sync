from __future__ import annotations

import re
from collections import OrderedDict
from dataclasses import dataclass, asdict, replace
from pathlib import Path
import json


RUN = Path("reports") / "选必一_哲学宝典式重建_2026-05-16"
FUSION = RUN / "03_fusion"
OUT = RUN / "06_final_handbook"

BUCKETS = [
    "时代背景",
    "理论",
    "经济全球化",
    "政治多极化",
    "中国",
    "联合国",
    "附：总说句 / 兜底加分表达",
]

SKIP_HEADINGS = {
    "边界说明",
    "融合裁决备注",
    "同类项合并索引",
    "源包边界提示",
    "暂不入链来源",
}

BUCKET_BOUNDARY_NOTES = {
    "时代背景": [
        "本桶只负责解释中国主张、倡议或外交行动为什么有正当性和必要性。",
        "如果材料重点落在开放、市场、贸易、产业链、共享发展成果或全球经济治理，应转入“经济全球化”桶，不要只停留在宏观背景。",
        "如果题目已经要求分析国际关系结构本身，时代背景里的多极化表述只能作前提铺垫，主体落点应转入“政治多极化”桶。",
    ],
    "理论": [
        "本桶只负责解释合作、竞争、国家行动和外交立场背后的原理。",
        "如果材料重点落在中国方案、中国行动或中国贡献，应转入“中国”桶；如果重点落在联合国机制、宪章原则或共同议程，应转入“联合国”桶。",
        "“正确义利观”只有在细则明确列入国家利益角度、理论逻辑或合作基础可选表达时才放在本桶；设问重心是中国行动、中国担当、发展合作、共享机遇或发展中国家民生时归入“中国”桶。",
        "“独立自主和平外交政策”“和平共处五项原则”“独立自主的基本立场”属于中国外交政策链，统一归入“中国”桶；技术、产业链语境中的“独立自主、自力更生、自主可控”也归入“中国”桶，不放在理论桶。",
    ],
    "经济全球化": [
        "本桶负责写开放、市场、贸易、投资、产业链供应链、经济规则和共享发展成果等具体作用链。",
        "经济全球化可以作为时代背景出现，但当题目问具体经济合作机制、开放平台或全球经济治理时，应作为主答点展开。",
        "本桶同类项合并必须看细则表述是否接近、卷面是否可替代；不能把“开放型世界经济”“开放型经济”“全球经济治理和规则制定”“贸易自由化”等只因本质相关就压成一类。",
    ],
    "政治多极化": [
        "本桶名称用于导航归类，卷面表达优先使用本题细则术语和节点内表述积累。",
        "看到国际关系、国际秩序、共同利益、合作共赢、全球治理方向时，优先从本桶组织答案；不要只把标题“政治多极化”当作答案术语照抄。",
        "如果材料已经要求分析国际关系结构本身，时代背景的多极化表述只能作前提铺垫一句，主体落点必须使用本桶细则术语。",
    ],
    "中国": [
        "本桶侧重中国主张、中国方案、中国行动、中国外交和中国贡献。",
        "中国外交政策链包括独立自主和平外交政策、独立自主的基本立场、和平共处五项原则、维护世界和平促进共同发展的宗旨和目标。",
        "技术、产业链、安全发展语境中的独立自主、自力更生、自主可控、发展主动权，属于中国如何行动和提升能力，不归入理论桶。",
        "如果题目重心是国际秩序、全球治理原则或共同利益，不要把所有“有中国参与”的材料都归入本桶。",
    ],
    "联合国": [
        "本桶只负责联合国框架、宪章宗旨原则、以联合国为核心的国际体系和共同议程。",
        "如果材料重点落在国际秩序改革、国际关系民主化或全球治理方向，应转入“政治多极化”桶；如果重点落在开放、贸易、市场和发展成果共享，应转入“经济全球化”桶。",
    ],
    "附：总说句 / 兜底加分表达": [
        "本附录只用于答案收束、过渡或最后补充，不能替代核心答题点。",
        "没有材料支撑时不能单独作为主答案；能写具体角度时先写具体角度。",
    ],
}

CORE_BOUNDARY_NOTES = {
    ("政治多极化", "推动构建人类命运共同体"): "本节点侧重国际关系、国际秩序、共同利益、合作共赢和全球治理方向；同题若还写中国桶，应避免重复堆写同一句。",
    ("中国", "中国推动构建人类命运共同体"): "本节点侧重中国主张、中国方案、中国行动、中国外交和中国贡献；若材料重点是国际秩序和治理原则，应回到政治多极化桶。",
    ("理论", "正确义利观〔国家利益角度可选表述〕"): "只有细则明确把正确义利观列入国家利益角度、理论逻辑或合作基础可选表达时，才放在理论桶；中国行动、中国担当、发展合作、共享机遇或发展中国家民生统一归入中国桶。",
    ("经济全球化", "提升发展中国家的代表性和发言权，打破规则制定垄断"): "本节点只保留自贸区、数字经济规则、标准制定和经贸合作中的规则代表性；若设问主问国际秩序公正合理，应回到政治多极化。",
}


@dataclass
class Entry:
    batch: str
    bucket: str
    heading_path: list[str]
    term: str
    question: str
    rubric: str
    source: str
    trigger: str
    answer: str


def clean_text(s: str) -> str:
    s = s.strip()
    replacements = {
        "设问要求": "题目要求",
        "细则要求": "阅卷依据指出",
        "本题需要": "本题宜",
        "材料中": "材料里",
        "要落到": "应归结为",
        "采分点": "得分点",
        "Batch": "批次",
        "Codex": "本地裁决",
        "GPT": "外部审阅",
        "Claude": "外部审阅",
        "prompt": "指令",
        "证据层级": "证据说明",
        "rubric_angle_id": "角度编号",
        "formal_rubric": "正式细则",
        "blocked_prompt_only": "题面待补细则",
    }
    for a, b in replacements.items():
        s = s.replace(a, b)
    return s


def source_for_student(e: Entry) -> str:
    source = e.source.rstrip("。")
    joined = f"{e.rubric} {e.source}"
    prefix = ""
    if "未定位正式评分细则" in joined and "未定位正式评分细则" not in source:
        source += "，未定位正式评分细则"
    if "教师版参考答案" in joined:
        prefix = "教师版参考答案来源："
    elif "官方参考答案" in joined:
        prefix = "官方参考答案来源："
    elif "参考答案" in joined:
        prefix = "参考答案来源："
    if prefix and not source.startswith(prefix):
        source = prefix + source
    level = evidence_level_note(e)
    if level and level not in source:
        source += f"；{level}"
    return source


def evidence_level_note(e: Entry) -> str:
    joined = f"{e.rubric} {e.source}"
    if "未定位正式评分细则" in joined:
        return "来源等级C：未定位正式细则，只作迁移参考，不作为稳定采分点"
    formal_markers = [
        "评分细则",
        "评标",
        "阅卷细则",
        "阅卷总结",
        "讲评细则",
        "评分标准",
        "评分标准说明",
    ]
    has_formal = any(marker in joined for marker in formal_markers)
    if "教师版参考答案" in joined and not has_formal:
        return "来源等级C：未定位正式细则，只作迁移参考，不作为稳定采分点"
    if ("未定位正式评分细则" in joined or "普通参考答案" in joined) and not has_formal:
        return "来源等级C：未定位正式细则，只作迁移参考，不作为稳定采分点"
    if ("官方参考答案" in joined or "参考答案" in joined or "阅卷前答案" in joined) and not has_formal:
        return "来源等级B：官方参考答案或阅卷前答案，需与正式细则区分"
    return ""


def term_field_label(e: Entry) -> str:
    return "参考答案术语" if evidence_level_note(e) else "细则术语"


def term_use_note(term: str) -> str | None:
    if "等" not in term:
        return None
    return "细则术语中的“等”表示同类表述可以结合材料补充，卷面答案不要以“等”收尾。"


def display_core(bucket: str, core: str) -> str:
    if bucket == "附：总说句 / 兜底加分表达":
        return f"【兜底】{core}"
    return core


def display_heading_path(bucket: str, core: str, heading_path: list[str]) -> list[str]:
    if not heading_path:
        return []
    joined = " / ".join(heading_path)
    if bucket == "经济全球化" and joined in {
        "两个市场两种资源与开放型世界经济",
        "全球化与贸易保护主义 + 开放型世界经济",
    }:
        return [core]
    return heading_path


def parse_batch(path: Path) -> list[Entry]:
    batch = path.stem.replace("_FINAL_AFTER_GPT_AND_CLAUDE", "")
    lines = path.read_text(encoding="utf-8").splitlines()
    entries: list[Entry] = []
    bucket = ""
    heading_path: list[str] = []
    current: dict[str, str] | None = None

    def flush() -> None:
        nonlocal current
        if not current:
            return
        required = ["term", "question", "rubric", "source", "trigger", "answer"]
        if bucket and all(current.get(k, "").strip() for k in required):
            entries.append(
                Entry(
                    batch=batch,
                    bucket=bucket,
                    heading_path=heading_path[:],
                    term=clean_text(current["term"]),
                    question=clean_text(current["question"]),
                    rubric=clean_text(current["rubric"]),
                    source=clean_text(current["source"]),
                    trigger=clean_text(current["trigger"]),
                    answer=clean_text(current["answer"]),
                )
            )
        current = None

    for raw in lines:
        line = raw.rstrip()
        m2 = re.match(r"^##\s+(.+)$", line)
        if m2:
            flush()
            name = m2.group(1).strip()
            if name in BUCKETS:
                bucket = name
                heading_path = []
            elif name in SKIP_HEADINGS:
                bucket = ""
                heading_path = []
            else:
                bucket = ""
                heading_path = []
            continue
        m3 = re.match(r"^###\s+(.+)$", line)
        if m3 and bucket:
            flush()
            heading_path = [clean_text(m3.group(1).strip())]
            continue
        m4 = re.match(r"^####\s+(.+)$", line)
        if m4 and bucket:
            flush()
            if not heading_path:
                heading_path = [clean_text(m4.group(1).strip())]
            elif len(heading_path) == 1:
                heading_path = [heading_path[0], clean_text(m4.group(1).strip())]
            else:
                heading_path[-1] = clean_text(m4.group(1).strip())
            continue
        mt = re.match(r"^\*\*(?:术语|得分表达)：(.+)\*\*$", line)
        if mt and bucket:
            flush()
            current = {"term": clean_text(mt.group(1).strip())}
            continue
        if current is None:
            continue
        for key, label in [
            ("question", "完整设问"),
            ("rubric", "细则位置"),
            ("source", "来源"),
            ("trigger", "材料触发"),
            ("answer", "答案句"),
        ]:
            prefix = f"- {label}："
            if line.startswith(prefix):
                current[key] = clean_text(line[len(prefix) :])
                break

    flush()
    return entries


def norm_term(term: str) -> str:
    t = re.sub(r"[`，。；;、/\s（）()“”\"'：:]+", "", term)
    t = t.replace("推动构建", "构建")
    t = t.replace("人类命运共同体", "构建人类命运共同体")
    t = t.replace("世贸组织", "世界贸易组织")
    return t


CHINA_STATE_NATURE_CORE = "\u65b0\u4e2d\u56fd\u5916\u4ea4\u59cb\u7ec8\u670d\u52a1\u4e8e\u6211\u56fd\u4eba\u6c11\u6c11\u4e3b\u4e13\u653f\u7684\u56fd\u5bb6\u6027\u8d28\uff1b\u575a\u6301\u515a\u5bf9\u5916\u4ea4\u7edf\u4e00\u96c6\u4e2d\u9886\u5bfc"
CHINA_SECURITY_CORE = "\u575a\u6301\u603b\u4f53\u56fd\u5bb6\u5b89\u5168\u89c2\uff0c\u7edf\u7b79\u53d1\u5c55\u4e0e\u5b89\u5168\uff0c\u4ee5\u65b0\u5b89\u5168\u683c\u5c40\u4fdd\u969c\u65b0\u53d1\u5c55\u683c\u5c40"
CHINA_PUBLIC_PRODUCT_CORE = "\u7406\u5ff5\u8574\u542b\u666e\u904d\u4ef7\u503c\uff0c\u80fd\u591f\u5f62\u6210\u5171\u8bc6\u3001\u4fc3\u6210\u5408\u4f5c\u548c\u53d1\u5c55\u3001\u5e94\u5bf9\u5168\u4eba\u7c7b\u5171\u540c\u95ee\u9898\u548c\u5171\u540c\u6311\u6218"
CHINA_TECH_LIVELIHOOD_CORE = "\u4fc3\u8fdb\u6280\u672f\u5171\u4eab\u548c\u6c11\u751f\u6539\u5584\uff1b\u4e3a\u5168\u7403\u53ef\u6301\u7eed\u53d1\u5c55\u8d21\u732e\u529b\u91cf"
CHINA_CLIMATE_CORE = "\u4e2d\u56fd\u63a8\u8fdb\u7eff\u8272\u4f4e\u78b3\u8f6c\u578b\u5e76\u53c2\u4e0e\u5168\u7403\u6c14\u5019\u6cbb\u7406"
CHINA_GDI_CORE = "\u5168\u7403\u53d1\u5c55\u5021\u8bae\uff1a\u4ee5\u53d1\u5c55\u4fc3\u7e41\u8363"
CHINA_GSI_CORE = "\u5168\u7403\u5b89\u5168\u5021\u8bae\uff1a\u4ee5\u5b89\u5168\u4fdd\u7a33\u5b9a"
CHINA_GCI_CORE = "\u5168\u7403\u6587\u660e\u5021\u8bae\uff1a\u4ee5\u6587\u660e\u589e\u4e92\u4fe1"


def _has_any(text: str, needles: list[str]) -> bool:
    return any(needle in text for needle in needles)


def manual_core_override(term: str) -> str | None:
    """Hard boundary corrections found in the six-bucket re-audit."""
    if _has_any(term, ["\u4eba\u6c11\u6c11\u4e3b\u4e13\u653f", "\u515a\u5bf9\u5916\u4ea4\u7edf\u4e00\u96c6\u4e2d\u9886\u5bfc"]):
        return CHINA_STATE_NATURE_CORE
    if _has_any(term, ["\u603b\u4f53\u56fd\u5bb6\u5b89\u5168\u89c2", "\u5904\u7406\u597d\u53d1\u5c55\u548c\u5b89\u5168\u7684\u5173\u7cfb", "\u7edf\u7b79\u53d1\u5c55\u548c\u5b89\u5168", "\u7ef4\u62a4\u56fd\u5bb6\u7ecf\u6d4e\u5b89\u5168\u3001\u79d1\u6280\u5b89\u5168"]):
        return CHINA_SECURITY_CORE
    if "\u7ecf\u6d4e\u5b89\u5168 / \u7edf\u7b79\u5b89\u5168\u4e0e\u53d1\u5c55 / \u591a\u5143\u7a33\u5b9a\u7684\u7ecf\u8d38\u5173\u7cfb" in term:
        return "\u7ecf\u6d4e\u5b89\u5168 / \u7edf\u7b79\u5b89\u5168\u4e0e\u53d1\u5c55 / \u591a\u5143\u7a33\u5b9a\u7684\u7ecf\u8d38\u5173\u7cfb"
    if "\u6211\u56fd\u7684\u672a\u6765\u4ea7\u4e1a\u6709\u975e\u5e38\u5e7f\u9614\u7684\u56fd\u9645\u5e02\u573a" in term:
        return "\u6211\u56fd\u7684\u672a\u6765\u4ea7\u4e1a\u6709\u975e\u5e38\u5e7f\u9614\u7684\u56fd\u9645\u5e02\u573a\uff0c\u4e3a\u672a\u6765\u4ea7\u4e1a\u201c\u8d70\u51fa\u53bb\u201d\u63d0\u4f9b\u4e86\u53ef\u80fd"
    if "\u7406\u5ff5\u8574\u542b\u666e\u904d\u4ef7\u503c" in term:
        return CHINA_PUBLIC_PRODUCT_CORE
    if _has_any(term, ["\u4ee5\u79d1\u6280\u52a9\u529b\u53d1\u5c55\u4e2d\u56fd\u5bb6\u53d1\u5c55", "\u63d0\u5347\u5176\u81ea\u4e3b\u53d1\u5c55\u80fd\u529b\uff1b\u4fc3\u8fdb\u6c11\u751f\u6539\u5584"]):
        return CHINA_TECH_LIVELIHOOD_CORE
    if _has_any(term, ["\u6211\u56fd\u7528\u884c\u52a8\u4e3a\u4e16\u754c\u6c14\u5019", "\u300a\u5df4\u9ece\u534f\u5b9a\u300b", "\u56fd\u5bb6\u81ea\u4e3b\u8d21\u732e\u76ee\u6807", "NDC"]):
        return CHINA_CLIMATE_CORE
    if "\u5168\u7403\u53d1\u5c55\u5021\u8bae" in term:
        return CHINA_GDI_CORE
    if "\u5168\u7403\u5b89\u5168\u5021\u8bae" in term:
        return CHINA_GSI_CORE
    if _has_any(term, ["\u5168\u7403\u6587\u660e\u5021\u8bae", "\u901a\u8fc7\u4ea4\u6d41\u4e92\u9274\u3001\u4f20\u627f\u548c\u521b\u65b0\uff0c\u4fc3\u8fdb\u6c11\u5fc3\u76f8\u901a"]):
        return CHINA_GCI_CORE
    return None


def manual_bucket_override(term: str, core: str) -> str | None:
    if core in {
        CHINA_STATE_NATURE_CORE,
        CHINA_SECURITY_CORE,
        CHINA_PUBLIC_PRODUCT_CORE,
        CHINA_TECH_LIVELIHOOD_CORE,
        CHINA_CLIMATE_CORE,
        CHINA_GDI_CORE,
        CHINA_GSI_CORE,
        CHINA_GCI_CORE,
    }:
        return "\u4e2d\u56fd"
    if core in {
        "\u7ecf\u6d4e\u5b89\u5168 / \u7edf\u7b79\u5b89\u5168\u4e0e\u53d1\u5c55 / \u591a\u5143\u7a33\u5b9a\u7684\u7ecf\u8d38\u5173\u7cfb",
        "\u6211\u56fd\u7684\u672a\u6765\u4ea7\u4e1a\u6709\u975e\u5e38\u5e7f\u9614\u7684\u56fd\u9645\u5e02\u573a\uff0c\u4e3a\u672a\u6765\u4ea7\u4e1a\u201c\u8d70\u51fa\u53bb\u201d\u63d0\u4f9b\u4e86\u53ef\u80fd",
    }:
        return "\u7ecf\u6d4e\u5168\u7403\u5316"
    return None


def classify_core(bucket: str, term: str) -> str:
    t = term
    override = manual_core_override(t)
    if override:
        return override
    if bucket == "时代背景":
        if any(x in t for x in ["国际局势", "变乱交织", "外部环境", "风险挑战", "贸易保护主义", "逆全球化", "霸权主义", "强权政治", "单边主义"]):
            return "百年变局与外部风险挑战"
        if any(x in t for x in ["和平与发展", "和平、发展", "时代主题", "历史潮流"]):
            return "和平与发展仍是时代主题"
        if "经济全球化" in t and "政治多极化" in t:
            return "政治多极化、经济全球化深入发展"
    if bucket == "理论":
        if "共同利益" in t:
            return "国家间共同利益是国家合作的基础"
        if "和平共处五项原则" in t or "和平外交" in t or "对外关系基本准则" in t:
            return "中国坚持独立自主和平外交与和平共处五项原则"
        if "独立自主" in t or "自力更生" in t or "自主可控" in t or "发展主动权" in t:
            return "坚持独立自主、自力更生，增强发展主动权"
        if "国家利益" in t or "主权、安全" in t or "主权安全" in t:
            return "维护国家利益是主权国家对外活动的出发点和落脚点"
        if "国际竞争" in t or "综合国力" in t or "科技实力" in t or "创新驱动" in t:
            return "国际竞争的实质是综合国力较量"
        if "新型国际关系" in t:
            return "相互尊重、公平正义、合作共赢的新型国际关系"
        if "与发展中国家共享发展新机遇" in t or "惠民生增福祉" in t:
            return "与发展中国家共享发展新机遇，惠民生增福祉，实现互利共赢"
        if "发展合作中共享机遇" in t or ("正确义利观" in t and ("互利共赢" in t or "共商共建共享" in t)):
            return "坚持正确义利观，在发展合作中共享机遇"
        if "合作共赢；实现合作共赢；推动各国合作共赢" in t:
            return "合作共赢；实现合作共赢；推动各国合作共赢"
        if "在平等互利基础上开展合作" in t:
            return "在平等互利基础上开展合作；互利共赢"
        if "合作共赢" in t or "互利共赢" in t:
            return "合作共赢、互利共赢、共享发展成果"
        if "正确义利观" in t:
            return "坚持正确义利观"
    if bucket == "经济全球化":
        if "全球化 / 贸易保护主义" in t and "开放型世界经济" in t:
            return "全球化 / 贸易保护主义；开放型世界经济 / 世界经济共同繁荣 / 互利共赢 / 开放合作 / 共享成果"
        if "推动普惠包容的经济全球化 / 建设开放型世界经济 / 促进贸易自由化" in t:
            return "推动普惠包容的经济全球化 / 建设开放型世界经济 / 促进贸易自由化"
        if "以科学技术的发展推动建设创新型、开放型世界经济" in t or "创新型、开放型世界经济" in t:
            return "以科学技术的发展推动建设创新型、开放型世界经济"
        if "企业" in t and "出海" in t and ("全球经济治理" in t or "规则制定" in t):
            return "参与全球经济治理和规则制定，为企业出海营造国际环境"
        if "提升发展中国家的代表性" in t or "规则制定中的垄断" in t or "打破发达国家" in t:
            return "提升发展中国家的代表性和发言权，打破规则制定垄断"
        if (
            "国际高标准经贸规则" in t
            or "国际标准" in t
            or "相关贸易规则制定" in t
            or "规则话语权" in t
            or "国际技术标准" in t
        ):
            return "对接国际高标准经贸规则，参与国际标准和相关贸易规则制定，提升规则话语权"
        if "坚持多边贸易" in t or "全球经济治理体系改革" in t:
            return "坚持多边贸易、多边主义与全球经济治理体系改革"
        if "全球经济治理" in t and ("多边贸易体系" in t or "多边贸易体制" in t or "开放型世界经济" in t):
            return "积极参与全球经济治理和规则制定，维护多边贸易体系"
        if "全球经济治理" in t or "规则制定" in t:
            return "积极参与全球经济治理和规则制定"
        if "世界贸易组织" in t or "世贸组织" in t or "多边贸易体制" in t or "多边贸易体系" in t:
            return "维护以世界贸易组织为核心的多边贸易体制"
        if "两个市场" in t or "两种资源" in t or "资源配置" in t or "生产要素" in t:
            return "利用两个市场两种资源优化全球资源配置"
        if "发展更高层次开放型经济" in t or "建设高层次开放型经济" in t or "提高开放型经济水平" in t or "开放型经济水平" in t:
            return "提高开放型经济水平 / 建设高层次开放型经济"
        if "处理好自力更生和对外开放的关系" in t:
            return "处理好自力更生和对外开放的关系，参与经济全球化和国际分工"
        if "推动建设开放型世界经济" in t and "深化国际分工" in t:
            return "推动建设开放型世界经济；深化国际分工与合作"
        if "包容性增长" in t or "超大规模市场红利" in t or "广大而充满创新活力的市场" in t:
            return "中国市场红利与全球经济包容性增长"
        if (
            "推进普惠包容的经济全球化" in t
            or "让不同国家都能参与并享有" in t
            or "更加开放、包容的全球经济格局" in t
            or "开放、包容的全球经济格局" in t
            or "开放包容的全球经济格局" in t
            or "经济全球化方向：普惠、平衡、共赢" in t
        ):
            return "推进普惠包容的经济全球化，推动构建更加开放、包容的全球经济格局"
        if (
            "开放、包容、普惠、平衡、共赢" in t
            or "普惠、平衡、共赢" in t
            or "开放包容普惠" in t
            or "普惠包容" in t
            or t in {"推动经济全球化发展"}
        ):
            return "推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展"
        if "经济全球化趋势" in t or "顺应经济全球化趋势" in t or "融入经济全球化" in t or "更深层次迈进" in t:
            return "顺应经济全球化趋势，主动融入并推动深化"
        if "数字平台" in t or "数字科技" in t or "数字经济" in t or "数字贸易" in t or "电子商务" in t:
            return "数字贸易与数字经济跨境流通"
        if "高水平对外开放" in t or "制度型开放" in t or "市场准入" in t or "营商环境" in t or "外商投资" in t or "一线放开" in t or "国际职业资格" in t or "数据出境负面清单" in t:
            return "中国扩大高水平对外开放与制度型开放"
        if "推动建设开放型世界经济" in t or "推动构建开放型世界经济" in t or "建设开放型世界经济" in t:
            return "推动建设开放型世界经济"
        if (
            "贸易和投资自由化便利化" in t
            or "自由化便利化" in t
            or "贸易投资便利" in t
            or "贸易投资便利化" in t
            or "制度性交易成本" in t
            or "贸易效率" in t
            or "贸易壁垒" in t
            or "经贸合作" in t
            or "贸易合作" in t
        ):
            return "推进贸易和投资自由化便利化"
        if "一带一路" in t:
            return "高质量共建“一带一路”与共享发展机遇"
        if "产业链" in t or "供应链" in t:
            return "维护全球产业链供应链稳定畅通"
        if "比较优势" in t or "国际竞争新优势" in t:
            return "发挥比较优势并打造国际竞争新优势"
    if bucket == "政治多极化":
        if (
            "全球经济治理" in t
            or "国际标准" in t
            or "相关贸易规则制定" in t
            or "规则话语权" in t
        ):
            return "对接国际高标准经贸规则，参与国际标准和相关贸易规则制定，提升规则话语权"
        if "人类命运共同体" in t:
            return "推动构建人类命运共同体"
        if "新型国际关系" in t:
            return "相互尊重、公平正义、合作共赢的新型国际关系"
        if "共商共建共享" in t or "全球治理观" in t or "平等开放、合作共享" in t:
            return "共商共建共享的全球治理观"
        if "国际关系民主化" in t or "平等参与决策" in t:
            return "推动国际关系民主化"
        if "国际新秩序" in t or "国际秩序" in t or "全球治理体系" in t or "公正合理" in t or "完善全球治理" in t or "全球治理变革" in t:
            return "推动国际秩序和全球治理体系更加公正合理"
        if "多边主义" in t:
            return "践行真正的多边主义"
        if "多极化" in t or "全球南方" in t or "发展中国家" in t:
            return "世界多极化与全球南方联合自强"
        if "霸权主义" in t or "强权政治" in t or "单边主义" in t:
            return "反对单边主义、霸权主义和强权政治"
    if bucket == "中国":
        if "正确义利观" in t:
            return "坚持正确义利观"
        if "中国智慧" in t or "中国方案" in t or "中国力量" in t:
            return "贡献中国智慧、中国方案、中国力量"
        if "大国担当" in t or "负责任大国" in t or "建设性作用" in t:
            return "中国是负责任大国并勇于担当"
        if "公共产品" in t:
            return "中国提供国际公共产品"
        if "人类命运共同体" in t:
            return "中国推动构建人类命运共同体"
        if "习近平外交思想" in t or "中国特色大国外交主动作为" in t or "外交为民" in t or "中国式现代化" in t:
            return "习近平外交思想指导中国特色大国外交（外交为民、服务中国式现代化）"
        if "话语权" in t or "国际影响力" in t or "国际地位" in t or "综合国力" in t or "强大韧性" in t or "世界经济中的地位" in t:
            return "中国综合国力、国际地位和话语权提升"
        if "南南合作" in t or "全球南方" in t:
            return "南南合作与全球南方共同发展"
        if "和平共处五项原则" in t or "和平外交" in t or "对外关系基本准则" in t:
            return "中国坚持独立自主和平外交与和平共处五项原则"
        if "独立自主" in t or "自力更生" in t or "自主可控" in t or "发展主动权" in t or "核心技术攻关" in t:
            return "坚持独立自主、自力更生，增强发展主动权"
        if "改善发展中国家民生" in t or "改善民生" in t or "促进就业" in t or "公共卫生" in t:
            return "改善发展中国家民生并助力持续发展"
        if "教育文化交流" in t or "民心相通" in t or "文明互鉴" in t or "传播中华文化" in t:
            return "民心相通与文明互鉴"
        if "绿色低碳" in t or "气候变化" in t or "气候治理" in t or "碳交易" in t or "减缓和适应" in t:
            return "中国推进绿色低碳转型并参与全球气候治理"
        if "主权、安全" in t or "国家利益" in t:
            return "中国坚定维护国家主权、安全、发展利益"
    if bucket == "联合国":
        if "联合国宪章" in t:
            return "维护《联合国宪章》宗旨和原则"
        if "联合国宗旨和原则" in t:
            return "维护《联合国宪章》宗旨和原则"
        if "联合国" in t and ("核心" in t or "国际体系" in t or "多边" in t):
            return "维护以联合国为核心的国际体系"
        if "2030" in t or "可持续发展" in t or "消除贫困" in t or "教育普及" in t or "卫生健康" in t:
            return "落实联合国2030年可持续发展议程"
    return term


def target_bucket(bucket: str, term: str, core: str, e: Entry | None = None) -> str:
    override = manual_bucket_override(term, core)
    if override:
        return override
    if core == "相互尊重、公平正义、合作共赢的新型国际关系":
        return "政治多极化"
    if core == "对接国际高标准经贸规则，参与国际标准和相关贸易规则制定，提升规则话语权":
        return "经济全球化"
    if core in {
        "与发展中国家共享发展新机遇，惠民生增福祉，实现互利共赢",
        "坚持正确义利观，在发展合作中共享机遇",
        "中国坚持独立自主和平外交与和平共处五项原则",
        "坚持独立自主、自力更生，增强发展主动权",
    }:
        return "中国"
    if core == "坚持正确义利观" and bucket == "理论":
        joined = f"{e.rubric if e else ''} {e.source if e else ''}"
        if "国家利益角度" in joined or "理论逻辑" in joined:
            return "理论"
        return "中国"
    if core == "合作共赢；实现合作共赢；推动各国合作共赢":
        return "经济全球化"
    if core == "在平等互利基础上开展合作；互利共赢":
        return "政治多极化"
    return bucket


def normalize_core_for_bucket(bucket: str, core: str) -> str:
    if bucket == "理论" and core == "坚持正确义利观":
        return "正确义利观〔国家利益角度可选表述〕"
    return core


def split_mixed_entries(entries: list[Entry]) -> list[Entry]:
    out: list[Entry] = []
    for e in entries:
        if (
            e.bucket == "理论"
            and e.term == "正确的义利观；正确义利观"
            and "2026延庆一模Q19(2)" in e.rubric
            and "2025顺义一模Q20" in e.rubric
        ):
            out.append(
                replace(
                    e,
                    question="结合材料二，运用《当代国际政治与经济》知识，说明中国“推动重塑全球能源治理格局”的理论逻辑和价值意蕴。",
                    rubric="2026延庆一模Q19(2)，评分细则“国家利益角度：共同利益是国家间合作的基础/维护国家利益是主权国家对外活动的出发点/正确的义利观”。",
                    source="2026延庆一模Q19(2)",
                    trigger="延庆一模的绿色能源合作不是单向输出利益，而是在帮助共建国家能源转型中兼顾共同发展和全球治理责任。",
                    answer="中国坚持正确义利观，依托绿色基建和新能源产业优势帮助共建国家能源转型，在共同发展中推动全球能源治理格局优化。",
                )
            )
            out.append(
                replace(
                    e,
                    question="结合材料，运用《当代国际政治与经济》知识，说明“小而美”项目为何成为中国开展国际发展合作的亮点和名片。",
                    rubric="2025顺义一模Q20，评分细则“项目对我国的意义或折射我国的理念”中“正确义利观”，任意一点1分，不超过2分。",
                    source="2025顺义一模Q20",
                    trigger="顺义一模的“小而美”项目直接服务共建国家民生，体现中国在国际发展合作中兼顾道义、共同发展和自身责任。",
                    answer="中国通过“小而美”项目帮助共建国家改善民生、促进发展，体现正确义利观和负责任大国形象。",
                )
            )
            continue
        out.append(e)
    return out


def analysis_flow(bucket: str, core: str) -> list[str]:
    if bucket == "时代背景":
        return [
            "材料怎么看：先看题目是否在追问中国主张、合作倡议或外交行动为什么具有正当性和必要性。",
            "该写哪个术语：外部环境、时代主题、世界变局、逆全球化和治理赤字优先放入时代背景。",
            "为什么触发：这类点不是单纯背背景，而是用背景解释中国行动为什么顺势、应势、解题。",
            "答案句怎么落：时代判断 + 材料里的中国行动或国际问题 + 对和平、发展、治理或合作的作用。",
        ]
    if bucket == "理论":
        return [
            "材料怎么看：先看题目是否在问合作为什么成立、竞争为什么激烈、国家为什么这样行动。",
            "该写哪个术语：凡是解释国际关系背后原因的，优先找国家利益、共同利益、综合国力、国际竞争实质等解释性原理；“共同利益是合作的基础”可解释合作为什么成立，独立自主和平外交政策、和平共处五项原则和发展主动权类表述转入中国桶；含新型国际关系、国际秩序、全球治理方向的合作共赢转入政治多极化，含贸易、市场、产业链供应链、资源流动、开放平台的合作共赢转入经济全球化，含中国担当、共享机遇、发展中国家民生的合作共赢转入中国桶。",
            "为什么触发：理论点负责回答“为什么”，不能只把材料事实改写成口号。",
            "答案句怎么落：理论术语 + 材料里的利益/竞争/合作事实 + 因果结论。",
        ]
    if bucket == "经济全球化":
        return [
            "材料怎么看：先看贸易、投资、市场、产业链供应链、规则、平台、资源流动和开放合作。",
            "该写哪个术语：国际经济循环、资源配置、开放型世界经济、贸易投资自由化便利化等放在本桶。",
            "为什么触发：经济全球化点要说明中国如何通过开放合作改善世界经济运行。",
            "答案句怎么落：全球化机制 + 材料里的开放或合作事实 + 对互利共赢、共同繁荣或稳定供应链的作用。",
        ]
    if bucket == "政治多极化":
        return [
            "材料怎么看：先看国际秩序、全球治理、发展中国家话语权、多边主义、国际关系民主化。",
            "该写哪个术语：凡是回答国际秩序应往哪里走、全球治理怎样改进的，放入政治多极化。",
            "为什么触发：政治多极化点强调秩序方向和治理原则，不要写成一般外交态度。",
            "答案句怎么落：治理/秩序术语 + 材料里的倡议或机制 + 对公正合理国际秩序的作用。",
        ]
    if bucket == "中国":
        return [
            "材料怎么看：先看中国身份、地位、责任、方案、外交宗旨、政策行动和中国式现代化。",
            "该写哪个术语：中国自身如何行动、贡献什么、承担什么责任，放入中国桶。",
            "为什么触发：本桶不是泛写爱国表态，而是把中国的地位、政策和责任同材料任务相连。",
            "答案句怎么落：中国定位/政策术语 + 材料里的中国行动 + 对世界或国家发展的作用。",
        ]
    if bucket == "联合国":
        return [
            "材料怎么看：先看联合国、安理会、联合国宪章、2030议程、多边合作场域。",
            "该写哪个术语：涉及联合国地位、宪章宗旨原则、以联合国为核心的国际体系，放入本桶。",
            "为什么触发：联合国点要说明中国行动为什么合乎多边规则、国际体系或共同议程。",
            "答案句怎么落：联合国术语 + 材料里的中国参与或议程事实 + 对多边合作和全球治理的作用。",
        ]
    return [
        "材料怎么看：先确认该表达是否只是兜底总说，不能替代正式逐点赋分。",
        "该写哪个术语：只在四角度未满分或卷面需要总起时使用。",
        "为什么触发：它负责总领方向，不单独代替具体角度。",
        "答案句怎么落：总判断 + 后续分角度展开。",
    ]


def compact_trigger(text: str, limit: int = 42) -> str:
    text = re.sub(r"\s+", "", text)
    text = text.replace("设问评价", "题目评价")
    text = text.replace("设问", "题目")
    if len(text) <= limit:
        return text
    return text[:limit].rstrip("，；、") + "..."


def make_why(bucket: str, core: str, e: Entry) -> str:
    trigger = compact_trigger(e.trigger)
    if bucket == "时代背景":
        target = "为什么有正当性、必要性或时代依据"
    elif bucket == "理论":
        target = "合作、竞争或国家行动背后的原因"
    elif bucket == "经济全球化":
        target = "贸易、投资、市场、产业链、规则或开放合作的作用"
    elif bucket == "政治多极化":
        target = "国际秩序、全球治理、共同利益或多边合作方向"
    elif bucket == "中国":
        target = "中国主张、中国行动、中国责任或中国贡献"
    elif bucket == "联合国":
        target = "联合国框架、宪章原则或共同议程"
    else:
        return f"看到材料里需要总起或收束，而具体角度还未写满时，才使用“{display_core(bucket, core)}”；它不能替代正式核心答题点。"
    return f"看到材料里出现“{trigger}”，且题目追问{target}，就把材料事实接到“{display_core(bucket, core)}”。"


def build() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    entries: list[Entry] = []
    for path in sorted(FUSION.glob("BATCH_*FINAL_AFTER_GPT_AND_CLAUDE.md")):
        entries.extend(parse_batch(path))
    entries = split_mixed_entries(entries)

    (OUT / "xuanbiyi_baodian_entries.json").write_text(
        json.dumps([asdict(e) for e in entries], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    grouped: OrderedDict[str, OrderedDict[str, list[Entry]]] = OrderedDict()
    variants: OrderedDict[tuple[str, str], OrderedDict[str, None]] = OrderedDict()
    for b in BUCKETS:
        grouped[b] = OrderedDict()
    for e in entries:
        core = classify_core(e.bucket, e.term)
        bucket = target_bucket(e.bucket, e.term, core, e)
        core = normalize_core_for_bucket(bucket, core)
        e.bucket = bucket
        grouped.setdefault(bucket, OrderedDict()).setdefault(core, []).append(e)
        variants.setdefault((bucket, core), OrderedDict()).setdefault(e.term, None)

    lines: list[str] = []
    lines.append("# 选择性必修一《当代国际政治与经济》主观题术语宝典")
    lines.append("")
    lines.append("**飞哥正志讲堂**")
    lines.append("")
    lines.append("## 前言")
    lines.append("")
    lines.append("这份稿子不按试卷流水账展开，而是按选必一主观题的六个答题框架组织：时代背景、理论、经济全球化、政治多极化、中国、联合国。学生使用时先找框架节点，再看材料怎样触发该节点，最后把答案句写成“术语 + 材料事实 + 因果/作用/结论”。")
    lines.append("")
    lines.append("## 使用方法")
    lines.append("")
    lines.append("先看一级框架，再找核心答题点。每个核心答题点后面的“出现N次”表示当前已定稿区卷材料里被挂载的题例数量；同一核心下的不同表述作为表述积累保留，不再拆成多个孤立术语。")
    lines.append("")
    lines.append("“出现N次”仅表示本宝典收录样本中的命中次数，用于判断复习优先级，不等同于考试预测，也不代表该点在所有设问中都可直接套用。高出现次数表示该节点在本宝典样本中复用度高，不代表它优先于材料语义；材料不触发就不写。每条题例固定保留七字段：术语（细则术语/参考答案术语）、材料触发点、设问、为什么能想到、答案落点、细则位置、来源。来源等级B/C只作迁移参考，不等同于正式稳定采分点。")
    lines.append("")
    lines.append("## 目录")
    lines.append("")
    for b in BUCKETS:
        if grouped.get(b):
            lines.append(f"- {b}（{sum(len(v) for v in grouped[b].values())}条题例）")
    lines.append("")

    for bucket in BUCKETS:
        cores = grouped.get(bucket)
        if not cores:
            continue
        lines.append(f"# {bucket}")
        lines.append("")
        lines.append("【本桶固定分析流程】")
        for flow in analysis_flow(bucket, bucket):
            lines.append(f"- {flow}")
        lines.append("- 考场动作：先判断材料属于本桶哪种关系，再把细则术语放入卷面句，后接本题材料事实，最后写出对合作、发展、治理、国家利益或中国贡献的作用。")
        if bucket in BUCKET_BOUNDARY_NOTES:
            lines.append("")
            lines.append("【归桶边界】")
            for note in BUCKET_BOUNDARY_NOTES[bucket]:
                lines.append(f"- {note}")
        lines.append("")
        for core, items in cores.items():
            if not items:
                continue
            var_list = list(variants[(bucket, core)].keys())
            core_title = display_core(bucket, core)
            lines.append(f"## 核心答题点：{core_title}（出现{len(items)}次）")
            lines.append("")
            lines.append("【表述积累】")
            for v in var_list:
                lines.append(f"- {v}")
            lines.append("")
            lines.append(f"【本节点真题】共 {len(items)} 条。")
            if (bucket, core) in CORE_BOUNDARY_NOTES:
                lines.append("")
                lines.append(f"【本节点边界】{CORE_BOUNDARY_NOTES[(bucket, core)]}")
            lines.append("")
            for idx, e in enumerate(items, 1):
                title = e.source.rstrip("。")
                lines.append(f"### {idx}. {title}")
                heading_path = display_heading_path(bucket, core, e.heading_path)
                if heading_path:
                    lines.append("")
                    lines.append(f"【本节点归类】{' / '.join(heading_path)}")
                lines.append("")
                lines.append(f"【{term_field_label(e)}】{e.term}")
                note = term_use_note(e.term)
                if note:
                    lines.append("")
                    lines.append(f"【卷面使用】{note}")
                lines.append("")
                lines.append(f"【材料触发点】{e.trigger}")
                lines.append("")
                lines.append(f"【设问】{e.question}")
                lines.append("")
                lines.append(f"【为什么能想到】{make_why(bucket, core, e)}")
                lines.append("")
                lines.append(f"【答案落点】{e.answer}")
                lines.append("")
                lines.append(f"【细则位置】{e.rubric}")
                lines.append("")
                lines.append(f"【来源】{source_for_student(e)}")
                lines.append("")
    out_md = OUT / "选必一_当代国际政治与经济_主观题术语宝典_学生版.md"
    out_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    nav: list[str] = []
    nav.append("# 选必一《当代国际政治与经济》主观题术语宝典：考前导航版")
    nav.append("")
    nav.append("这份导航版只保留框架、核心答题点、出现次数、最常用表述和迁移提醒；完整题例见学生厚版。导航节点与厚版同名，复习时可直接搜索同名“核心答题点”。")
    nav.append("")
    nav.append("“出现N次”仅表示本宝典收录样本中的命中次数，用于判断复习优先级，不等同于考试预测，也不代表该点在所有设问中都可直接套用。高出现次数不代表优先于材料语义；材料不触发就不写。")
    nav.append("")
    nav.append("导航版只提示节点，不替代厚版中的来源等级判断；厚版标为参考答案术语、来源等级B/C的内容，只作迁移参考，不按稳定正式细则背诵。")
    nav.append("")
    for bucket in BUCKETS:
        cores = grouped.get(bucket)
        if not cores:
            continue
        nav.append(f"## {bucket}")
        nav.append("")
        if bucket in BUCKET_BOUNDARY_NOTES:
            for note in BUCKET_BOUNDARY_NOTES[bucket]:
                nav.append(f"- {note}")
            nav.append("")
        nav.append("| 核心答题点 | 出现 | 表述积累首句 | 厚版定位 | 迁移提醒 |")
        nav.append("|---|---:|---|---|---|")
        for core, items in cores.items():
            first_variant = next(iter(variants[(bucket, core)].keys()), core)
            if bucket in {"时代背景", "理论"}:
                hook = "遇到原因、前提、深层逻辑，先判断它是不是背景或理论支撑。"
            elif bucket == "经济全球化":
                hook = "遇到贸易、投资、市场、供应链、规则和开放合作，优先从全球化机制写。"
            elif bucket == "政治多极化":
                hook = "遇到秩序、治理、话语权、多边主义，优先从政治多极化和全球治理写。"
            elif bucket == "中国":
                hook = "遇到中国行动、中国方案、中国责任，先写中国定位和政策作用。"
            elif bucket == "联合国":
                hook = "遇到联合国、宪章、2030议程和多边场域，先写联合国框架。"
            else:
                hook = "只作总起兜底，不替代具体角度。"
            core_title = display_core(bucket, core)
            if (bucket, core) in CORE_BOUNDARY_NOTES:
                hook = f"{CORE_BOUNDARY_NOTES[(bucket, core)]} {hook}"
            locator = "同名二级标题"
            nav.append(f"| {core_title} | {len(items)} | {first_variant} | {locator} | {hook} |")
        nav.append("")
    (OUT / "选必一_当代国际政治与经济_主观题术语宝典_考前导航版.md").write_text(
        "\n".join(nav).rstrip() + "\n", encoding="utf-8"
    )

    audit = []
    audit.append("# 选必一主观题术语宝典学生版构建审计")
    audit.append("")
    audit.append(f"- 输入批次终稿：{len(list(FUSION.glob('BATCH_*FINAL_AFTER_GPT_AND_CLAUDE.md')))}")
    audit.append(f"- 输出题例：{len(entries)}")
    audit.append(f"- 输出核心节点：{sum(len(v) for v in grouped.values())}")
    audit.append("- 七字段数量：术语（细则术语/参考答案术语）、材料触发点、设问、为什么能想到、答案落点、细则位置、来源均随每条题例输出")
    for b in BUCKETS:
        count = sum(len(v) for v in grouped.get(b, {}).values())
        core_count = len(grouped.get(b, {}))
        audit.append(f"- {b}：{core_count}个核心节点，{count}条题例")
    (OUT / "选必一_主观题术语宝典_学生版_构建审计.md").write_text(
        "\n".join(audit) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    build()
