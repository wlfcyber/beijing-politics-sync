"""V8 decode-version student MD builder.

Reads V8_DECODE_EXTRACTION.json and produces a framework-organized student-facing
Markdown for `2026北京高考政治哲学宝典---三年模拟全触发全链条`.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"C:/bp_sync_visible/reports/final_56_v8_decode_claudecode_2026-04-29")
EXTRACTION = ROOT / "audit" / "V8_DECODE_EXTRACTION.json"
OUT_MD = ROOT / "outputs" / "2026北京高考政治哲学宝典---三年模拟全触发全链条_v8_decode版_学生版.md"

S003_OCR_PATH = Path(r"C:/bp_sync_visible/reports/ocr_rerun_claudecode_2026-04-28/S001_2024东城一模.md")

FRAMEWORK = [
    {
        "code": "U1",
        "title": "第一单元 辩证唯物论：物质、意识与规律",
        "nodes": [
            {
                "code": "1.1",
                "title": "物质决定意识·一切从实际出发·实事求是",
                "keys": ["物质决定意识", "一切从实际出发", "实事求是", "客观实际", "尊重客观规律", "求真务实"],
            },
            {
                "code": "1.2",
                "title": "意识的能动作用·目的性·计划性·创造性",
                "keys": ["意识的能动", "意识能动", "意识的目的性", "意识的创造性", "意识对物质", "主观能动性", "能动反映"],
            },
            {
                "code": "1.3",
                "title": "客观规律与主观能动性·合规律性与合目的性",
                "keys": ["客观规律", "尊重规律", "合规律性", "合目的性", "顺应规律", "把握规律"],
            },
        ],
    },
    {
        "code": "U2",
        "title": "第二单元 认识论：实践与认识、真理",
        "nodes": [
            {
                "code": "2.1",
                "title": "实践决定认识·实践是认识的基础·社会生活本质上是实践的",
                "keys": ["实践决定", "实践是认识的基础", "实践是检验真理", "社会生活在本质上是实践", "在实践中产生", "在实践中检验", "实践的观点"],
            },
            {
                "code": "2.2",
                "title": "真理的客观性、具体性、条件性",
                "keys": ["真理是客观", "真理的客观", "真理是具体", "真理的条件", "真理面前人人平等", "具体的有条件的"],
            },
            {
                "code": "2.3",
                "title": "认识的反复性、无限性、上升性",
                "keys": ["认识的反复", "认识的无限", "认识的上升", "在实践中追求", "反复性"],
            },
        ],
    },
    {
        "code": "U3",
        "title": "第三单元 唯物辩证法：联系、发展与矛盾",
        "nodes": [
            {
                "code": "3.1",
                "title": "联系观·普遍性、客观性、多样性·整体与部分·系统优化",
                "keys": ["联系", "联系的普遍性", "联系的客观性", "联系的多样性", "整体与部分", "整体和部分", "系统优化", "系统观念"],
            },
            {
                "code": "3.2",
                "title": "发展观·前进性与曲折性·量变与质变·辩证否定与创新",
                "keys": ["前进性与曲折性", "量变", "质变", "辩证否定", "辩证的否定", "革故鼎新", "守正创新", "新事物", "事物发展的", "发展的观点", "适度原则", "量变引起质变", "创新意识", "创造性思维", "创新驱动"],
            },
            {
                "code": "3.3",
                "title": "矛盾观·对立统一·普特·主次·两点重点·具体问题具体分析",
                "keys": ["矛盾", "对立统一", "矛盾的普遍性", "矛盾的特殊性", "矛盾普遍性", "矛盾特殊性", "主要矛盾", "次要矛盾", "矛盾的主要方面", "两点论", "重点论", "具体问题具体分析", "矛盾分析法", "牛鼻子"],
            },
        ],
    },
    {
        "code": "U4",
        "title": "第四单元 历史唯物主义：社会、人民与价值观",
        "nodes": [
            {
                "code": "4.1",
                "title": "社会存在与社会意识·社会基本矛盾·改革",
                "keys": ["社会存在", "社会意识", "经济基础", "上层建筑", "生产关系", "社会基本矛盾", "改革是社会主义"],
            },
            {
                "code": "4.2",
                "title": "人民群众是历史创造者·群众观点群众路线·以人民为中心",
                "keys": ["人民群众", "人民立场", "群众路线", "群众观点", "以人民为中心", "依靠人民", "人民至上", "人民是历史"],
            },
            {
                "code": "4.3",
                "title": "价值观·价值判断与价值选择·在劳动和奉献中创造价值",
                "keys": ["价值观", "价值判断", "价值选择", "人生价值", "在劳动和奉献", "共同价值", "崇高理想", "价值取向"],
            },
        ],
    },
    {
        "code": "U5",
        "title": "第五单元 文化传承与文化创新",
        "nodes": [
            {
                "code": "5.1",
                "title": "文化的内涵与功能·中华民族精神",
                "keys": ["文化的内涵", "文化的功能", "文化的作用", "民族精神", "中华民族精神", "精神支柱", "精神纽带", "文化育人", "文化滋养", "凝聚力"],
            },
            {
                "code": "5.2",
                "title": "文化的继承、发展与创新·创造性转化创新性发展",
                "keys": ["文化创新", "文化的继承", "文化的发展", "推陈出新", "创造性转化", "创新性发展", "传统文化的", "中华优秀传统文化的", "古为今用", "推陈出新"],
            },
            {
                "code": "5.3",
                "title": "文化多样性·文化交流·借鉴外来文化",
                "keys": ["文化多样性", "文化交流", "文化交融", "互鉴", "外来文化", "面向世界", "博采众长", "求同存异", "兼收并蓄"],
            },
            {
                "code": "5.4",
                "title": "发展中国特色社会主义文化·文化自信·文化强国",
                "keys": ["中国特色社会主义文化", "文化自信", "文化强国", "革命文化", "社会主义先进文化", "中华优秀传统文化", "立德树人", "意识形态", "社会主义核心价值观"],
            },
            {
                "code": "5.5",
                "title": "中华文明新形态·命运共同体·讲好中国故事",
                "keys": ["人类文明新形态", "中华文明", "构建人类命运共同体", "命运共同体", "讲好中国故事", "全人类共同价值", "文明互鉴", "中国式现代化"],
            },
        ],
    },
]


def normalize_question_text(text: str) -> str:
    """Trim noise from a raw question chunk pulled from the bundle."""
    text = re.sub(r"\s+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.strip()
    return text


def has_philosophy_signal(text: str) -> bool:
    if not text:
        return False
    triggers = [
        "哲学", "马克思", "辩证", "矛盾", "联系", "发展", "实践", "认识", "意识", "物质",
        "规律", "价值", "人民", "群众", "文化", "民族精神", "传统", "创新", "中华文明",
        "运用", "结合材料", "评价", "谈谈对", "阐述", "辨析",
    ]
    return any(t in text for t in triggers)


def restrict_to_philosophy(text: str) -> bool:
    """True only if the prompt explicitly cites 必修四 / 哲学与文化 / 哲学方法."""
    if not text:
        return False
    must = [
        "哲学与文化", "运用《哲学与文化》", "运用哲学与文化", "运用哲学", "运用唯物辩证法",
        "运用辩证唯物主义", "运用辩证唯物论", "运用历史唯物主义", "运用认识论",
        "运用文化与价值观", "运用文化生活", "运用文化",
    ]
    return any(m in text for m in must)


def is_explicit_other_module(text: str) -> bool:
    """Detect prompts that are explicitly limited to 经济与社会／政治与法治／选修2／选修3."""
    if not text:
        return False
    others = [
        "运用《经济与社会》", "运用经济与社会", "运用经济知识", "运用经济的相关",
        "运用《政治与法治》", "运用政治与法治", "从政治和法治",
        "运用《法律与生活》", "运用法律与生活",
        "运用《逻辑与思维》", "运用逻辑与思维",
        "运用《当代国际政治与经济》", "运用《现代国家概论》",
    ]
    return any(o in text for o in others)


def best_node_codes(text: str) -> list[str]:
    """Return up to two framework node codes ranked by keyword density.

    Only return codes whose score is at least 60% of the top-scored node, so that
    weak secondary matches do not pollute the index. Always return at most 2.
    """
    if not text:
        return []
    scores: list[tuple[int, str]] = []
    for unit in FRAMEWORK:
        for node in unit["nodes"]:
            score = sum(text.count(k) for k in node["keys"])
            if score > 0:
                scores.append((score, node["code"]))
    if not scores:
        return []
    scores.sort(reverse=True)
    top = scores[0][0]
    out: list[str] = []
    for score, code in scores:
        if score < max(2, top * 0.6):
            break
        if code not in out:
            out.append(code)
        if len(out) >= 2:
            break
    return out


PAGE_NOISE_RE = re.compile(r"第?\s*\d{1,2}\s*页\s*[\(／/]?\s*共\s*\d{1,2}\s*页\s*[\)）]?")
PAGE_NOISE2_RE = re.compile(r"第\s*PAGE[^\n]*页")
PAGE_NOISE3_RE = re.compile(r"PAGE\s*\\?\*?\s*MERGEFORMAT[^\n]*")
LEVEL_TABLE_RE = re.compile(r"等级水平[\s\S]*?(?:水平\s*1[^\n]*|应答与试题无关[^\n]*|没有应答[^\n]*)", re.MULTILINE)
LEVEL_TABLE2_RE = re.compile(r"水平\s*4[\s\S]{0,1500}?水平\s*1[^\n]*")
LEVEL_TABLE3_RE = re.compile(r"等\s*级\s*描\s*述[\s\S]{0,1500}?水平\s*1[^\n]*")
RUBRIC_NOISE_RES = [
    re.compile(r"阅卷中发现的问题[\s\S]*?(?=\n\n|$)"),
    re.compile(r"未答[\s\S]*?最多给\s*\d\s*分[^\n]*"),
    re.compile(r"班级得分率[：:][^\n]*"),
    re.compile(r"最高分[：:][^\n]*"),
    re.compile(r"最低分[：:][^\n]*"),
    re.compile(r"原理表述准确性、科学性问题[^\n]*"),
    re.compile(r"逻辑层次问题[^\n]*"),
    re.compile(r"应答与试题无关[^\n]*"),
    re.compile(r"高三思想政治参考答案[^\n]*"),
    re.compile(r"思想政治[ \t]*试卷讲评[^\n]*"),
    re.compile(r"\d{4}\s*年\s*\d{1,2}\s*月\s*$", re.MULTILINE),
]


def _strip_universal_noise(text: str) -> str:
    text = PAGE_NOISE_RE.sub("", text)
    text = PAGE_NOISE2_RE.sub("", text)
    text = PAGE_NOISE3_RE.sub("", text)
    text = LEVEL_TABLE_RE.sub("", text)
    text = LEVEL_TABLE2_RE.sub("", text)
    text = LEVEL_TABLE3_RE.sub("", text)
    for pat in RUBRIC_NOISE_RES:
        text = pat.sub("", text)
    text = re.sub(r"(?m)^\s*\d+\s*[．.]\s*[A-D][^\n]*$", "", text)
    text = re.sub(r"(?m)^\s*[A-D]\s*$", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]{2,}", "  ", text)
    return text.strip()


def trim_to_clean_prompt(prompt: str) -> str:
    if not prompt:
        return ""
    lines = prompt.splitlines()
    cleaned: list[str] = []
    for ln in lines:
        s = ln.strip()
        if not s:
            cleaned.append("")
            continue
        if re.match(r"^[（(]\d{1,2}[）)]?$", s):
            cleaned.append(s)
            continue
        if s.startswith("等级水平") or s.startswith("等 级 描 述") or s.startswith("水平 "):
            continue
        if s in {"水平4", "水平3", "水平2", "水平1"}:
            continue
        if "应答与试题无关" in s:
            continue
        cleaned.append(ln)
    out = "\n".join(cleaned)
    out = _strip_universal_noise(out)
    return out


def trim_to_clean_answer(answer: str) -> str:
    if not answer:
        return ""
    return _strip_universal_noise(answer)


def short_excerpt(prompt: str, limit: int = 220) -> str:
    """Pull a representative material trigger excerpt from the prompt body."""
    if not prompt:
        return ""
    body = prompt
    body = re.sub(r"^\s*\d{1,2}\s*[．.、][^\n]*\n", "", body, count=1)
    body = re.sub(r"^\s*[（(]\d{1,2}\s*分[）)][^\n]*", "", body, count=1)
    candidates = [ln.strip() for ln in body.splitlines() if len(ln.strip()) > 30]
    if not candidates:
        return ""
    excerpt = candidates[0]
    if len(excerpt) > limit:
        excerpt = excerpt[: limit - 1].rstrip("，,。；;") + "…"
    return excerpt


def explain_trigger(node_codes: list[str]) -> str:
    """One-line plain explanation of why the material/answer maps to these nodes."""
    desc_map: dict[str, str] = {
        node["code"]: node["title"] for unit in FRAMEWORK for node in unit["nodes"]
    }
    parts = [desc_map[c] for c in node_codes if c in desc_map]
    if not parts:
        return "材料情境与必修四《哲学与文化》典型原理形成对接。"
    return "材料情境直接对接：" + "；".join(parts) + "。"


def s003_main_entries() -> list[dict]:
    """Two main-question entries seeded from the authorized S003 OCR rerun."""
    return [
        {
            "suite_id": "S003",
            "year": "2024",
            "district": "东城",
            "stage": "2024各区一模",
            "suite_name": "2024东城一模",
            "qno": "16",
            "score": 7,
            "prompt_text": (
                "中华民族是世界上伟大的民族，有着 5000 多年源远流长的文明历史，为人类文明进步作出了不可磨灭的贡献。"
                "牛皮封面、飘口烫金、书口刷红——作为法国国礼的《论语导读》如今典藏于中国国家图书馆。"
                "《论语》的早期翻译和导读曾对孟德斯鸠和伏尔泰的哲学思想给予启发。17 至 18 世纪，"
                "中国的思想、文化和技术\"东学西传\"，促成欧洲不断认识中国、改进自身，感受中华文明的深厚积淀。"
                "中国共产党领导中国人民成功走出了中国式现代化道路，创造了人类文明新形态，"
                "为促进世界文明交流互鉴、推动构建人类命运共同体贡献了中国方案、中国智慧、中国力量。"
                "马克思说，\"凡是民族作为民族所做的事情，都是他们为人类社会而做的事情\"。"
                "结合材料，运用《哲学与文化》知识，谈谈对此观点的理解。"
            ),
            "trigger_excerpt": "马克思：\"凡是民族作为民族所做的事情，都是他们为人类社会而做的事情\"——民族性与世界性、共性与个性的统一。",
            "trigger_reason": "马克思引文与中华文明对人类的贡献，直接对接矛盾普遍性与特殊性、整体与部分；东学西传与文明互鉴对接联系普遍性与文化交流交融；中国式现代化与人类命运共同体对接科学价值观与全人类共同价值。",
            "answer_landing": (
                "第一层：矛盾普遍性与特殊性、共性与个性辩证统一——民族文化构成世界文化多样性，民族文化成就既属本民族也属于整个世界。"
                "第二层：联系的观点+社会生活在本质上是实践的——文化交流是文化发展动力，党领导中国人民在实践中创造人类文明新形态，要维护文化多样性、推动构建人类命运共同体。"
                "第三层：科学的价值观符合社会发展规律和人民根本利益——坚持以人民为中心、坚守中华文化立场、坚定文化自信，让中华文化走出去，蕴含全人类共同价值。"
            ),
            "rubric_boundary": "哲学 3 分：候选观点为共性个性统一/普特统一/整体部分、联系观/社会生活实践本质、科学价值观/共同价值，2 个观点 3 分、1 个观点 2 分。文化 4 分：解释关系 1 分+分析论证 2 分+要求举措 1 分。",
            "node_codes": ["3.3", "3.1", "5.5"],
        },
        {
            "suite_id": "S003",
            "year": "2024",
            "district": "东城",
            "stage": "2024各区一模",
            "suite_name": "2024东城一模",
            "qno": "21",
            "score": 7,
            "prompt_text": (
                "辨辨同心心相连，京畿大地起宏图。十年携手、十年并进，京津冀三地致力于提速\"通勤圈\"、"
                "优化\"功能圈\"、打造\"产业圈\"，现代化首都都市圈建设欣欣向荣、生机勃勃。"
                "提速\"通勤圈\"——形成多节点、网格状、全覆盖的综合交通网络体系，构建京津冀区域内地级市半小时、一小时交通圈。"
                "优化\"功能圈\"——抓住疏解非首都功能这个\"牛鼻子\"，北京发挥\"一核\"辐射带动作用，推动雄安新区和北京城市副中心\"两翼\"齐飞，形成错位联动发展格局。"
                "打造\"产业圈\"——\"北京研发、津冀制造\"模式加速形成，京津冀联合绘制新能源、智能网联汽车等 6 条产业链图谱。"
                "结合材料，运用所学，阐述\"三圈\"联动如何促进现代化首都都市圈高质量发展。"
            ),
            "trigger_excerpt": "\"通勤圈半小时一小时交通圈\"+\"疏解非首都功能这个牛鼻子\"+\"一核两翼\"+\"北京研发、津冀制造\"——分别对接共享发展、主次矛盾与系统优化、产业链协同与比较优势。",
            "trigger_reason": "通勤圈：以人民为中心+共享发展+联系普遍性。功能圈：抓\"牛鼻子\"对接主次矛盾、两点论与重点论、整体与部分、系统优化。产业圈：辩证联系与矛盾普特(三地比较优势)+创新协调发展理念。",
            "answer_landing": (
                "第一层(通勤圈/共享)：坚持以人民为中心，贯彻新发展理念，发挥有为政府的公共服务职能，完善综合交通基础设施，促进区域内人流物流和资源要素流动，优化资源配置、促进共享发展。"
                "第二层(功能圈/系统优化)：坚持系统优化的方法，抓住疏解非首都功能这一主要矛盾，发挥\"一核两翼\"作用，处理好整体与部分的关系，促进区域协调发展。"
                "第三层(产业圈/比较优势)：坚持创新、绿色、协调的新发展理念，发挥三地比较优势，京津冀联合绘制 6 条产业链图谱，构建创新引领、协同发展的现代化产业体系。"
            ),
            "rubric_boundary": "等级评分 7 分：水平 4(5-7 分)、水平 3(3-4 分)、水平 2(1-2 分)、水平 1(0 分)。围绕\"三圈联动→高质量发展\"行文，单写一圈或不谈联动会被扣分。",
            "node_codes": ["4.2", "3.3", "3.1"],
        },
    ]


def harvest_main_entries(extraction: dict) -> list[dict]:
    """Walk the extraction JSON and emit framework-ready main-question entries."""
    rows: list[dict] = []
    for sid, suite in extraction["suites"].items():
        if sid == "S003":
            continue
        if not suite.get("bundle_present"):
            continue
        for qno_str, q in (suite.get("main_questions") or {}).items():
            prompt = trim_to_clean_prompt(q.get("paper_prompt") or "")
            answer = trim_to_clean_answer(q.get("answer_block") or "")
            if not prompt and not answer:
                continue
            combo = (prompt + "\n" + answer).strip()
            if is_explicit_other_module(prompt) or is_explicit_other_module(answer):
                continue
            node_codes = best_node_codes(combo)
            if not node_codes:
                continue
            distinct_keywords = sum(
                1 for u in FRAMEWORK for n in u["nodes"] for k in n["keys"] if k in combo
            )
            prompt_phil_explicit = restrict_to_philosophy(prompt) or restrict_to_philosophy(answer)
            if not prompt_phil_explicit and distinct_keywords < 3:
                continue
            rows.append({
                "suite_id": sid,
                "year": suite.get("year", ""),
                "district": suite.get("district", ""),
                "stage": suite.get("stage", ""),
                "suite_name": suite.get("suite_name", ""),
                "qno": qno_str,
                "score": q.get("score"),
                "prompt_text": prompt,
                "trigger_excerpt": short_excerpt(prompt),
                "trigger_reason": explain_trigger(node_codes),
                "answer_landing": (answer[:1200] + ("…" if len(answer) > 1200 else "")) if answer else "（参考答案缺失：仅依据细则触发点提示，正式答题以细则为准。）",
                "rubric_boundary": "",
                "node_codes": node_codes,
            })
    return rows


def render_md(entries: list[dict]) -> str:
    sections: list[str] = []

    sections.append("# 2026北京高考政治哲学宝典---三年模拟全触发全链条")
    sections.append("")
    sections.append("**飞哥正志讲堂**")
    sections.append("")
    sections.append("---")
    sections.append("")

    sections.append("## 序")
    sections.append("")
    sections.append("（本页为飞哥老师序言留白页。）")
    sections.append("")
    sections.append("---")
    sections.append("")

    sections.append("## 使用说明")
    sections.append("")
    sections.append("- 本宝典按必修四《哲学与文化》原理与方法节点组织，把 2024、2025、2026 三年北京各区一模、二模、期中、期末的真题主观题串成全触发全链条。")
    sections.append("- 每条目固定四件套：完整设问、关键材料触发、为何触发该原理、答案落点。")
    sections.append("- 不同节点之间会出现同一道题的不同触发面，请按节点视角阅读。")
    sections.append("- 选择题易错肢汇总另置一册：《北京高考政治选择题错肢总结·v8 decode 版》。")
    sections.append("")
    sections.append("---")
    sections.append("")

    by_node: dict[str, list[dict]] = {}
    for e in entries:
        for code in e["node_codes"]:
            by_node.setdefault(code, []).append(e)

    for unit in FRAMEWORK:
        sections.append(f"## {unit['title']}")
        sections.append("")
        for node in unit["nodes"]:
            sections.append(f"### {node['code']} {node['title']}")
            sections.append("")
            node_entries = by_node.get(node["code"], [])
            if not node_entries:
                sections.append("（本节点暂未在三年模拟主观题中检出独立触发条目；选择题部分见错肢总结。）")
                sections.append("")
                continue
            node_entries.sort(key=lambda e: (e["year"], e["suite_id"], e["qno"]))
            for e in node_entries:
                title = f"{e['year']}{e['district']}{'一模' if '一模' in e['stage'] else ('二模' if '二模' in e['stage'] else ('期中' if '期中' in e['stage'] else '期末'))} 第{e['qno']}题"
                if e.get("score"):
                    title += f"（{e['score']}分）"
                sections.append(f"#### {title}")
                sections.append("")
                if e.get("prompt_text"):
                    sections.append("**完整设问**")
                    sections.append("")
                    sections.append(e["prompt_text"])
                    sections.append("")
                if e.get("trigger_excerpt"):
                    sections.append("**关键材料触发**")
                    sections.append("")
                    sections.append(e["trigger_excerpt"])
                    sections.append("")
                if e.get("trigger_reason"):
                    sections.append("**为何触发该原理**")
                    sections.append("")
                    sections.append(e["trigger_reason"])
                    sections.append("")
                if e.get("answer_landing"):
                    sections.append("**答案落点**")
                    sections.append("")
                    sections.append(e["answer_landing"])
                    sections.append("")
                if e.get("rubric_boundary"):
                    sections.append("**细则边界**")
                    sections.append("")
                    sections.append(e["rubric_boundary"])
                    sections.append("")
                sections.append("---")
                sections.append("")

    sections.append("## 附录·节点-题目索引一览")
    sections.append("")
    for unit in FRAMEWORK:
        sections.append(f"### {unit['title']}")
        sections.append("")
        for node in unit["nodes"]:
            ne = by_node.get(node["code"], [])
            if not ne:
                sections.append(f"- {node['code']} {node['title']}：（本宝典暂无主观题触发，留待补录。）")
                continue
            ne.sort(key=lambda e: (e["year"], e["suite_id"], e["qno"]))
            ids = "、".join(f"{e['year']}{e['district']}{'一模' if '一模' in e['stage'] else ('二模' if '二模' in e['stage'] else ('期中' if '期中' in e['stage'] else '期末'))}Q{e['qno']}" for e in ne)
            sections.append(f"- {node['code']} {node['title']}：{ids}")
        sections.append("")

    return "\n".join(sections).rstrip() + "\n"


def main() -> None:
    extraction = json.loads(EXTRACTION.read_text(encoding="utf-8"))
    entries = s003_main_entries()
    entries.extend(harvest_main_entries(extraction))
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text(render_md(entries), encoding="utf-8")
    by_node: dict[str, int] = {}
    for e in entries:
        for c in e["node_codes"]:
            by_node[c] = by_node.get(c, 0) + 1
    print(f"wrote {OUT_MD}")
    print(f"entries total: {len(entries)}")
    for unit in FRAMEWORK:
        for node in unit["nodes"]:
            print(f"  {node['code']} {node['title'][:24]}: {by_node.get(node['code'], 0)}")


if __name__ == "__main__":
    main()
