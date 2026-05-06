#!/usr/bin/env python3
"""按飞哥框架节点聚合所有 audit/entries/*.jsonl，输出学生版 Markdown。

学生版字段顺序：材料触发点 → 设问 → 为什么能想到 → 答案落点。
排序：节点内主观题优先；同类按 海淀-西城-东城-朝阳-丰台-其他区；年份新→旧；阶段一模→二模→期末→期中。
学生版不出现：路径、line/file/slide id、OCR/debug、英文状态字段、审计/答案来源话术。
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/必修四从0重跑_ClaudeCode_2026-05-02")
ENTRIES_DIR = ROOT / "audit" / "entries"

# 飞哥框架（必修四哲学，不含文化）
FRAMEWORK = [
    ("唯物论", [
        "物质决定意识",
        "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一",
        "主观能动性 / 意识的能动作用",
        "尊重客观规律与发挥主观能动性相结合",
        "规律的客观性",
    ]),
    ("辩证法", [
        "联系的普遍性 / 联系的观点（总）",
        "联系的客观性",
        "根据固有联系建立新的具体联系",
        "联系的多样性",
        "整体与部分",
        "系统观念 / 系统优化",
        "发展的观点 / 发展的普遍性",
        "量变与质变 / 适度原则",
        "事物发展是前进性与曲折性的统一",
        "辩证否定 / 守正创新",
        "矛盾就是对立统一",
        "矛盾的普遍性",
        "矛盾的特殊性 / 具体问题具体分析",
        "矛盾的普遍性和特殊性",
        "两点论与重点论",
        "内因与外因",
    ]),
    ("认识论", [
        "实践与认识（总）",
        "实践是认识的基础",
        "认识对实践的反作用",
        "认识发展原理",
        "真理观",
    ]),
    ("历史唯物主义", [
        "社会存在与社会意识",
        "社会发展的两大基本规律和基本矛盾",
        "改革 / 改革的实质",
        "人民群众",
    ]),
    ("价值观 / 人生观", [
        "价值观的导向作用",
        "价值判断与价值选择",
        "实现人生价值",
    ]),
]

DISTRICT_ORDER = ["海淀", "西城", "东城", "朝阳", "丰台", "石景山", "房山", "通州", "昌平",
                  "顺义", "延庆", "门头沟", "怀柔", "平谷", "密云", "大兴"]
STAGE_ORDER = {"一模": 1, "二模": 2, "期末": 3, "期中": 4}

# 学生版禁止出现词清单（审计话术、状态字段、来源标识）
FORBIDDEN_TOKENS = [
    "yes", "pass", "filled", "correct_option_chain", "PASS_OBJECTIVE",
    "评标", "参考答案", "答案写", "答案/补充", "答案核",
    "可从……角度作答", "可从…角度作答", "可从某角度作答",
    "/Users/", "page_", "slide", "L24", "F04", "S015",
    "ocr", "OCR", "debug",
]

CIRCLED_OPTION_MARKS = "①②③④⑤⑥⑦⑧⑨⑩"


def normalize_quote_marks(text: str) -> str:
    """学生版统一使用中文双引号标出关键材料词句。"""
    if not text:
        return ""
    out: list[str] = []
    single_open = True
    double_open = True
    for ch in text:
        if ch in {"'", "‘", "’"}:
            out.append("“" if single_open else "”")
            single_open = not single_open
        elif ch == '"':
            out.append("“" if double_open else "”")
            double_open = not double_open
        else:
            out.append(ch)
    return "".join(out)


def format_choice_options(text: str) -> str:
    """把选择题 ①②③④ 选项拆成逐项换行，便于学生扫读。"""
    if not text:
        return ""
    matches = list(re.finditer(f"[{CIRCLED_OPTION_MARKS}]", text))
    if len(matches) < 2:
        return text

    prefix = text[:matches[0].start()].rstrip()
    options: list[str] = []
    for idx, match in enumerate(matches):
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        seg = text[match.start():end].strip()
        if idx + 1 < len(matches):
            seg = re.sub(r"[；;，,、\s]+$", "", seg) + "；"
        options.append(seg)

    return prefix + "\n" + "\n".join(options)


def normalize_node_path(p: str) -> tuple[str, str]:
    if not p:
        return "", ""
    parts = re.split(r"[\\/]+", p.strip(), maxsplit=1)
    if len(parts) == 2:
        return parts[0].strip(), parts[1].strip()
    return "", parts[0].strip()


def _strip(s: str) -> str:
    """归一化字符串用于比较：去掉空格、标点、停用词。"""
    s = re.sub(r"[\s（）()\[\]【】《》""''、，,。.!\?·…—\-\(\)/／·]+", "", s or "")
    for stop in ["的", "与", "和", "相", "及", "对", "与社会", "等"]:
        s = s.replace(stop, "")
    return s


# 节点别名/同义映射：左侧（输入归一化后）→ 右侧（飞哥框架节点）
NODE_ALIASES = {
    # 唯物论
    "物质决定意识意识对物质具有能动作用": "物质决定意识",
    "意识具有能动作用": "主观能动性 / 意识的能动作用",
    "意识反作用于物质": "主观能动性 / 意识的能动作用",
    "意识能动作用": "主观能动性 / 意识的能动作用",
    "主观能动性意识能动作用": "主观能动性 / 意识的能动作用",
    "主观能动性": "主观能动性 / 意识的能动作用",
    "一切从实际出发": "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一",
    "实事求是": "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一",
    "主观客观具体历史统一": "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一",
    "尊重客观规律发挥主观能动性结合": "尊重客观规律与发挥主观能动性相结合",
    "尊重客观规律发挥主观能动性": "尊重客观规律与发挥主观能动性相结合",
    "客观规律主观能动性": "尊重客观规律与发挥主观能动性相结合",
    "规律客观性": "规律的客观性",
    # 辩证法
    "联系普遍性": "联系的普遍性 / 联系的观点（总）",
    "联系观点": "联系的普遍性 / 联系的观点（总）",
    "联系普遍性观点": "联系的普遍性 / 联系的观点（总）",
    "联系观点总": "联系的普遍性 / 联系的观点（总）",
    "联系客观性": "联系的客观性",
    "根据固有联系建立新具体联系": "根据固有联系建立新的具体联系",
    "建立新具体联系": "根据固有联系建立新的具体联系",
    "固有联系建立新联系": "根据固有联系建立新的具体联系",
    "联系多样性": "联系的多样性",
    "整体部分": "整体与部分",
    "整体部分关系": "整体与部分",
    "系统观念": "系统观念 / 系统优化",
    "系统优化": "系统观念 / 系统优化",
    "系统观念系统优化": "系统观念 / 系统优化",
    "发展观点": "发展的观点 / 发展的普遍性",
    "发展观点普遍性": "发展的观点 / 发展的普遍性",
    "发展普遍性": "发展的观点 / 发展的普遍性",
    "量变质变": "量变与质变 / 适度原则",
    "量变质变适度原则": "量变与质变 / 适度原则",
    "适度原则": "量变与质变 / 适度原则",
    "前进性曲折性": "事物发展是前进性与曲折性的统一",
    "前进性曲折性统一": "事物发展是前进性与曲折性的统一",
    "事物发展前进性曲折性": "事物发展是前进性与曲折性的统一",
    "辩证否定": "辩证否定 / 守正创新",
    "辩证否定观": "辩证否定 / 守正创新",
    "守正创新": "辩证否定 / 守正创新",
    "辩证否定守正创新": "辩证否定 / 守正创新",
    "矛盾对立统一": "矛盾就是对立统一",
    "对立统一": "矛盾就是对立统一",
    "矛盾普遍性特殊性": "矛盾的普遍性和特殊性",
    "矛盾普遍性特殊性辩证关系": "矛盾的普遍性和特殊性",
    "矛盾普遍性": "矛盾的普遍性",
    "矛盾特殊性": "矛盾的特殊性 / 具体问题具体分析",
    "具体问题具体分析": "矛盾的特殊性 / 具体问题具体分析",
    "矛盾特殊性具体问题具体分析": "矛盾的特殊性 / 具体问题具体分析",
    "两点论重点论": "两点论与重点论",
    "重点论": "两点论与重点论",
    "两点论": "两点论与重点论",
    "主要矛盾": "两点论与重点论",
    "主次矛盾": "两点论与重点论",
    "矛盾主次方面": "两点论与重点论",
    "矛盾主要方面": "两点论与重点论",
    "主流支流": "两点论与重点论",
    "矛盾分析法": "矛盾就是对立统一",
    "矛盾分析方法": "矛盾就是对立统一",
    "内因外因": "内因与外因",
    "内外因": "内因与外因",
    # 认识论
    "实践认识总": "实践与认识（总）",
    "实践认识": "实践与认识（总）",
    "实践认识关系": "实践与认识（总）",
    "实践认识反作用关系": "实践与认识（总）",
    "实践认识基础": "实践是认识的基础",
    "实践基础": "实践是认识的基础",
    "认识实践反作用": "认识对实践的反作用",
    "认识反作用实践": "认识对实践的反作用",
    "认识发展": "认识发展原理",
    "认识发展原理": "认识发展原理",
    "真理": "真理观",
    "真理观": "真理观",
    # 历史唯物主义
    "社会存在社会意识": "社会存在与社会意识",
    "社会发展两大基本规律基本矛盾": "社会发展的两大基本规律和基本矛盾",
    "社会发展规律基本矛盾": "社会发展的两大基本规律和基本矛盾",
    "两大基本规律": "社会发展的两大基本规律和基本矛盾",
    "改革": "改革 / 改革的实质",
    "改革实质": "改革 / 改革的实质",
    "人民群众": "人民群众",
    # 价值观
    "价值观导向作用": "价值观的导向作用",
    "价值观导向": "价值观的导向作用",
    "价值判断价值选择": "价值判断与价值选择",
    "价值判断": "价值判断与价值选择",
    "价值选择": "价值判断与价值选择",
    "实现人生价值": "实现人生价值",
    "人生价值": "实现人生价值",
    "价值创造实现": "实现人生价值",
    "价值的创造实现": "实现人生价值",
    "在劳动奉献中创造价值": "实现人生价值",
    "群众路线": "人民群众",
    "群众观点": "人民群众",
    "矛盾观点": "矛盾就是对立统一",
    "矛盾观": "矛盾就是对立统一",
    "认识论实践认识辩证关系": "实践与认识（总）",
    "实践认识辩证关系": "实践与认识（总）",
    "实践真理": "真理观",
    "实践观点": "实践是认识的基础",
    "实践的观点": "实践是认识的基础",
    "认识反复性": "认识发展原理",
    "认识反复性无限性上升性": "认识发展原理",
    "认识具有反复性无限性上升性": "认识发展原理",
    "认识反复性无限性": "认识发展原理",
    "认识局限性": "认识发展原理",
    "认识发展": "认识发展原理",
    "经济基础上层建筑": "社会发展的两大基本规律和基本矛盾",
    "社会发展规律": "社会发展的两大基本规律和基本矛盾",
    "社会发展普遍规律": "社会发展的两大基本规律和基本矛盾",
    "社会基本矛盾": "社会发展的两大基本规律和基本矛盾",
    "社会基本规律": "社会发展的两大基本规律和基本矛盾",
    "经济基础上层建筑矛盾运动": "社会发展的两大基本规律和基本矛盾",
    "生产力生产关系": "社会发展的两大基本规律和基本矛盾",
    "生产力生产关系矛盾运动": "社会发展的两大基本规律和基本矛盾",
    "价值客观性": "价值判断与价值选择",
    "价值人需要": "价值判断与价值选择",
    "价值判断价值选择主体差异": "价值判断与价值选择",
    "马克思主义中国化时代化": "",
    "意识活动目的性": "主观能动性 / 意识的能动作用",
    "意识活动主动创造性": "主观能动性 / 意识的能动作用",
    "意识活动自觉选择性": "主观能动性 / 意识的能动作用",
    "真理认识反复性条件性": "真理观",
    "真理认识反复性": "真理观",
    "真理主客观条件": "真理观",
    "价值实现": "实现人生价值",
    "价值实现创造": "实现人生价值",
    "价值的实现创造": "实现人生价值",
    "人生价值实现": "实现人生价值",
    "在劳动中创造价值": "实现人生价值",
    "认识对实践指导作用": "认识对实践的反作用",
    "认识对实践的指导作用": "认识对实践的反作用",
    "认识实践指导作用": "认识对实践的反作用",
    "认识实践反作用": "认识对实践的反作用",
    "认识反作用": "认识对实践的反作用",
    "意识对物质能动作用": "主观能动性 / 意识的能动作用",
    "认识反作用实践": "认识对实践的反作用",
}


def _try_split_compound_node(node: str) -> list[str]:
    """节点名含 '/' 或 '、' 时拆分成多个候选，逐个尝试匹配。"""
    parts = re.split(r"[\\/／、,，]+", node)
    return [p.strip() for p in parts if p.strip()]


def match_framework_node(category: str, node: str) -> tuple[str, str] | None:
    """把条目的 (大类, 节点名) 对齐到飞哥框架。同义/别名匹配。"""
    cat = (category or "").strip()
    cat_alias = {
        "唯物论": "唯物论",
        "辩证唯物论": "唯物论",
        "辩证法": "辩证法",
        "唯物辩证法": "辩证法",
        "认识论": "认识论",
        "辩证唯物主义认识论": "认识论",
        "历史唯物主义": "历史唯物主义",
        "历唯": "历史唯物主义",
        "社会历史观": "历史唯物主义",
        "价值观": "价值观 / 人生观",
        "价值观 / 人生观": "价值观 / 人生观",
        "人生观": "价值观 / 人生观",
        "价值观/人生观": "价值观 / 人生观",
        "人生观/价值观": "价值观 / 人生观",
    }.get(cat, cat)

    # 1) 直接别名命中（先归一化再查表）
    norm = _strip(node)
    if norm in NODE_ALIASES:
        target_node = NODE_ALIASES[norm]
        if not target_node:
            return None
        for fw_cat, nodes in FRAMEWORK:
            if target_node in nodes:
                return fw_cat, target_node

    # 2) 大类内子串匹配（针对原节点完整字符串）
    for fw_cat, nodes in FRAMEWORK:
        if fw_cat != cat_alias:
            continue
        for fw_node in nodes:
            if _strip(node) and _strip(fw_node) and (
                _strip(node) in _strip(fw_node) or _strip(fw_node) in _strip(node)
            ):
                return fw_cat, fw_node
        # 大类匹配但节点未匹配 → 拆分复合节点继续找
        for sub in _try_split_compound_node(node):
            sub_norm = _strip(sub)
            if sub_norm in NODE_ALIASES:
                target = NODE_ALIASES[sub_norm]
                if target in nodes:
                    return fw_cat, target
            for fw_node in nodes:
                if sub_norm and _strip(fw_node) and (
                    sub_norm in _strip(fw_node) or _strip(fw_node) in sub_norm
                ):
                    return fw_cat, fw_node
        return fw_cat, ""

    # 3) 跨大类回退
    if norm:
        for fw_cat, nodes in FRAMEWORK:
            for fw_node in nodes:
                if _strip(fw_node) == norm or norm in _strip(fw_node) or _strip(fw_node) in norm:
                    return fw_cat, fw_node
    # 4) 拆分回退
    for sub in _try_split_compound_node(node):
        sub_norm = _strip(sub)
        if sub_norm in NODE_ALIASES:
            target = NODE_ALIASES[sub_norm]
            if not target:
                continue
            for fw_cat, nodes in FRAMEWORK:
                if target in nodes:
                    return fw_cat, target
        for fw_cat, nodes in FRAMEWORK:
            for fw_node in nodes:
                if sub_norm and _strip(fw_node) and (
                    sub_norm in _strip(fw_node) or _strip(fw_node) in sub_norm
                ):
                    return fw_cat, fw_node
    return None


def district_rank(d: str) -> int:
    try:
        return DISTRICT_ORDER.index(d)
    except ValueError:
        return 999


def stage_rank(s: str) -> int:
    return STAGE_ORDER.get(s, 99)


def load_all_entries() -> list[dict]:
    entries = []
    for jsonl_path in sorted(ENTRIES_DIR.glob("*.jsonl")):
        with open(jsonl_path, "r", encoding="utf-8") as f:
            for ln, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except Exception as e:
                    print(f"WARN: bad json {jsonl_path}:{ln}: {e}", file=sys.stderr)
                    continue
                obj["__file"] = jsonl_path.name
                entries.append(obj)
    return entries


def sanitize(text: str, field_name: str = "") -> str:
    if not text:
        return ""
    out = normalize_quote_marks(text)
    for tok in FORBIDDEN_TOKENS:
        if tok in out:
            # 不删除文中合理出现的"价值观"——这里只删除明显审计话术
            if tok in {"yes", "pass", "filled", "correct_option_chain", "PASS_OBJECTIVE",
                       "page_", "slide", "/Users/", "评标", "答案写", "答案/补充", "答案核",
                       "可从……角度作答", "可从…角度作答", "可从某角度作答"}:
                out = out.replace(tok, "").strip()
    if field_name == "设问":
        out = format_choice_options(out)
    return out.strip()


def render_question_label(e: dict) -> str:
    year = e.get("year", "")
    district = e.get("district", "")
    stage = e.get("stage", "")
    qno = e.get("question_no", "")
    sub = e.get("sub_part", "")
    parts = [f"{year}{district}{stage}", f"第{qno}题"]
    if sub:
        parts.append(f"第{sub}问")
    return " ".join(parts)


def main():
    entries = load_all_entries()
    print(f"# 共加载 {len(entries)} 条条目", file=sys.stderr)

    # 按节点分桶
    buckets: dict[tuple[str, str], list[dict]] = {}
    unmatched: list[dict] = []
    for e in entries:
        cat, node = normalize_node_path(e.get("target_node_path", ""))
        m = match_framework_node(cat, node)
        if not m or not m[1]:
            unmatched.append(e)
            continue
        buckets.setdefault(m, []).append(e)

    # 输出 Markdown
    lines: list[str] = []
    lines.append("# 2026 北京高考政治哲学宝典——三年模拟全触发全链条")
    lines.append("")
    lines.append("> 飞哥正志讲堂")
    lines.append("")
    lines.append("（前言留位，由飞哥本人填写）")
    lines.append("")
    lines.append("---")
    lines.append("")

    for fw_cat, nodes in FRAMEWORK:
        lines.append(f"## {fw_cat}")
        lines.append("")
        for fw_node in nodes:
            lines.append(f"### {fw_node}")
            lines.append("")
            ents = buckets.get((fw_cat, fw_node), [])
            if not ents:
                lines.append("*（本轮三年模拟未放入稳定案例。）*")
                lines.append("")
                continue
            # 排序：主观→客观；区县；年份新→旧；阶段一模→期中
            ents.sort(key=lambda e: (
                0 if e.get("question_type") == "subjective" or e.get("sort_priority") == "main_question" else 1,
                district_rank(e.get("district", "")),
                -int(e.get("year", 0) or 0),
                stage_rank(e.get("stage", "")),
                str(e.get("question_no", "")),
            ))
            for i, e in enumerate(ents, 1):
                label = render_question_label(e)
                lines.append(f"#### {label}")
                lines.append("")
                lines.append(f"**材料触发点**：{sanitize(e.get('材料触发点',''), '材料触发点')}")
                lines.append("")
                lines.append(f"**设问**：{sanitize(e.get('设问',''), '设问')}")
                lines.append("")
                lines.append(f"**为什么能想到**：{sanitize(e.get('为什么能想到',''), '为什么能想到')}")
                lines.append("")
                lines.append(f"**答案落点**：{sanitize(e.get('答案落点',''), '答案落点')}")
                lines.append("")
        lines.append("---")
        lines.append("")

    out_md = ROOT / "outputs" / "2026北京高考政治哲学宝典---三年模拟全触发全链条_学生版.md"
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(lines), encoding="utf-8")
    print(f"OK 学生版 Markdown -> {out_md}", file=sys.stderr)
    if unmatched:
        print(f"WARN 未匹配框架节点的条目 {len(unmatched)} 条：", file=sys.stderr)
        for e in unmatched[:20]:
            print(f"  - {e.get('entry_id')} target={e.get('target_node_path')}", file=sys.stderr)


if __name__ == "__main__":
    main()
