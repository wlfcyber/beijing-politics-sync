import json
import re
from collections import defaultdict
from pathlib import Path


AUDIT = Path("/Users/wanglifei/Desktop/北京高考政治/哲学宝典5.2原地修订/audit")
ENTRIES = AUDIT / "docx_entries.json"
OUT = AUDIT / "自动硬伤扫描.md"


CULTURE_PREFIX = "六、文化传承"
QUESTION_CUES = ["结合材料", "运用", "从哲学", "谈谈", "说明", "分析", "阐释", "评价", "认识", "理解", "为什么", "如何", "看法", "启示", "意义", "理由"]
FUZZY_PROMPTS = [
    "相关材料",
    "有关观点",
    "综合运用哲学与文化知识阐释有关观点",
    "结合算力、人工智能和区域发展相关材料",
    "选择题：根据题干材料",
]
META_BAD = [
    "答案可以落在",
    "把材料事实同",
    "说明这一原理如何",
    "支撑题目要求",
    "答题时要围绕",
    "正确项链",
    "错肢",
    "参考示例",
    "9分标准",
    "评标",
    "细则",
    "参考答案",
]
GENERIC_WHY_START = re.compile(r"^(能想到这个原理，是因为材料中的“[^”]+”给出了直接信号|题目不是|材料不是|材料强调|材料把|看到|这类题|当材料|可从)")


def source_key(heading: str):
    h = re.sub(r"^\d+\.\s*", "", heading or "")
    h = re.sub(r"（(?:主观题|选择题)）$", "", h).strip()
    return h


def norm(text):
    return re.sub(r"\s+", "", text or "")


def main():
    entries = json.loads(ENTRIES.read_text(encoding="utf-8"))
    philosophy = [e for e in entries if not e.get("module", "").startswith(CULTURE_PREFIX)]
    culture = [e for e in entries if e.get("module", "").startswith(CULTURE_PREFIX)]

    by_source_node = defaultdict(list)
    by_source = defaultdict(list)
    for i, e in enumerate(philosophy):
        src = source_key(e["heading"])
        by_source_node[(src, e["module"], e["node"])].append((i, e))
        by_source[src].append((i, e))

    problems = []

    for key, vals in by_source_node.items():
        if len(vals) > 1:
            problems.append(("疑似重复/同题同节点多次出现", vals))

    for i in range(len(philosophy) - 1):
        a, b = philosophy[i], philosophy[i + 1]
        if source_key(a["heading"]) == source_key(b["heading"]):
            problems.append(("相邻同题重复", [(i, a), (i + 1, b)]))

    field_rows = []
    for i, e in enumerate(philosophy):
        f = e.get("fields", {})
        trigger = f.get("材料触发点", "")
        prompt = f.get("设问", "")
        why = f.get("为什么能想到", "")
        landing = f.get("答案落点", "")
        flags = []
        if not any(c in prompt for c in QUESTION_CUES):
            flags.append("设问缺少常见问法信号")
        if any(x in prompt for x in FUZZY_PROMPTS):
            flags.append("设问疑似模糊概括")
        if len(prompt) < 18:
            flags.append("设问过短")
        if norm(trigger) and norm(trigger) == norm(why):
            flags.append("为什么能想到整句重复材料触发点")
        if len(why) < 45:
            flags.append("为什么能想到过短")
        if GENERIC_WHY_START.search(why):
            flags.append("为什么能想到疑似模板化/泛泛触发")
        if len(landing) < 45:
            flags.append("答案落点过短")
        if any(x in landing for x in META_BAD):
            flags.append("答案落点含元话术或审计话术")
        if not any(x in landing for x in ["因为", "所以", "体现", "说明", "应", "需要", "能够", "有利于", "必须"]):
            flags.append("答案落点不像答案句")
        if flags:
            field_rows.append((i, e, flags))

    lines = [
        "# 自动硬伤扫描",
        "",
        f"- 当前 Word 条目总数：{len(entries)}",
        f"- 哲学/价值观条目：{len(philosophy)}",
        f"- 将删除文化线条目：{len(culture)}",
        "",
        "## 重复与相邻重复",
        "",
    ]
    for kind, vals in problems[:200]:
        lines.append(f"### {kind}")
        for i, e in vals:
            lines.append(f"- #{i+1} {e['module']} / {e['node']} / {e['heading']}")
        lines.append("")

    lines += ["## 字段质量风险", ""]
    for i, e, flags in field_rows:
        f = e.get("fields", {})
        lines.append(f"### #{i+1} {e['module']} / {e['node']} / {e['heading']}")
        lines.append(f"- 风险：{'；'.join(flags)}")
        lines.append(f"- 材料触发点：{f.get('材料触发点','')}")
        lines.append(f"- 设问：{f.get('设问','')}")
        lines.append(f"- 为什么能想到：{f.get('为什么能想到','')}")
        lines.append(f"- 答案落点：{f.get('答案落点','')}")
        lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"philosophy": len(philosophy), "culture": len(culture), "duplicate_groups": len(problems), "field_risk_entries": len(field_rows)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
