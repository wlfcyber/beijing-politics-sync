from __future__ import annotations

import csv
import json
import re
from collections import OrderedDict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "23_reasoning_baodian_full_rebuild_20260606"

BAODIAN = ROOT / "14_reasoning_baodian_rebuild_after_v87_20260601" / "delivery" / "选必三推理宝典_重做版_20260601.md"
COMPILATION = ROOT / "15_reasoning_direct_compilation_20260601" / "delivery" / "选必三推理题汇编_20260601.md"
SOURCE_BOOK = ROOT / "13_reasoning_clean_redo_20260531" / "选必三_逻辑与思维_推理习题汇编_干净重做版_20260531.md"

OUT_MD = RUN / "delivery" / "选必三逻辑与思维_推理宝典_按类型完整题源细则优秀答案版_20260606.md"
QA_CSV = RUN / "qa" / "REASONING_BAODIAN_V23_ENTRY_QA_20260606.csv"
SUMMARY_JSON = RUN / "qa" / "reasoning_baodian_v23_summary.json"


FIELD_RE = re.compile(r"^【([^】]+)】\s*(.*)$")
ENTRY_RE = re.compile(r"^#{3,4}\s+\d+\.\s+(.+)$")
MAJOR_RE = re.compile(r"^##\s+([一二三四五六七八九十]+、.+)$")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalize_entry_title(title: str) -> str:
    title = title.strip()
    title = re.sub(r"\s+", " ", title)
    return title


def clean_block(text: str) -> str:
    lines = [line.rstrip() for line in text.strip().splitlines()]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines).strip()


def normalize_major(major: str | None) -> str:
    if not major:
        return ""
    major = re.sub(r"^[一二三四五六七八九十]+、", "", major.strip())
    return re.sub(r"\s+", " ", major)


def entry_key(major: str | None, subtype: str | None, title: str) -> tuple[str, str, str]:
    return (normalize_major(major), (subtype or "").strip(), normalize_entry_title(title))


def parse_student_baodian(text: str) -> list[dict]:
    entries: list[dict] = []
    major = None
    subtype = None
    current = None
    current_field = None

    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("## ") and re.match(r"^##\s+[一二三四五六七八九十]+、", line):
            major = line[3:].strip()
            subtype = None
            current = None
            current_field = None
            continue
        if line.startswith("### ") and not ENTRY_RE.match(line):
            subtype = line[4:].strip()
            current = None
            current_field = None
            continue
        m_entry = ENTRY_RE.match(line)
        if m_entry:
            title = normalize_entry_title(m_entry.group(1))
            current = {
                "title": title,
                "major": major,
                "subtype": subtype,
                "fields": OrderedDict(),
            }
            entries.append(current)
            current_field = None
            continue
        if not current:
            continue
        m_field = FIELD_RE.match(line)
        if m_field:
            current_field = m_field.group(1).strip()
            current["fields"][current_field] = m_field.group(2).strip()
        elif current_field is not None:
            old = current["fields"].get(current_field, "")
            current["fields"][current_field] = clean_block((old + "\n" + line).strip())
    return entries


def parse_compilation(text: str) -> dict[str, dict]:
    entries = {}
    major = None
    subtype = None
    current = None
    current_field = None

    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("## ") and re.match(r"^##\s+[一二三四五六七八九十]+、", line):
            major = line[3:].strip()
            subtype = None
            current = None
            current_field = None
            continue
        if line.startswith("### ") and not ENTRY_RE.match(line):
            subtype = line[4:].strip()
            current = None
            current_field = None
            continue
        m_entry = ENTRY_RE.match(line)
        if m_entry:
            title = normalize_entry_title(m_entry.group(1))
            current = {"title": title, "major": major, "subtype": subtype, "fields": OrderedDict()}
            entries[entry_key(major, subtype, title)] = current
            current_field = None
            continue
        if not current:
            continue
        m_field = FIELD_RE.match(line)
        if m_field:
            current_field = m_field.group(1).strip()
            current["fields"][current_field] = m_field.group(2).strip()
        elif current_field is not None:
            old = current["fields"].get(current_field, "")
            current["fields"][current_field] = clean_block((old + "\n" + line).strip())
    return entries


def parse_source_book(text: str) -> dict[str, dict]:
    entries = {}
    current = None
    current_field = None
    in_fence = False
    major = None
    subtype = None

    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("# ") and not line.startswith("## "):
            major = line[2:].strip()
            subtype = None
            current = None
            current_field = None
            in_fence = False
            continue
        if line.startswith("## ") and not line.startswith("### "):
            subtype = line[3:].strip()
            current = None
            current_field = None
            in_fence = False
            continue
        m_entry = re.match(r"^###\s+\d+\.\s+(.+)$", line)
        if m_entry:
            title = normalize_entry_title(m_entry.group(1))
            current = {"title": title, "major": major, "subtype": subtype, "fields": OrderedDict()}
            entries[entry_key(major, subtype, title)] = current
            current_field = None
            in_fence = False
            continue
        if not current:
            continue
        m_field = FIELD_RE.match(line)
        if m_field and not in_fence:
            current_field = m_field.group(1).strip()
            current["fields"][current_field] = m_field.group(2).strip()
            continue
        if current_field is not None:
            if line.strip().startswith("```"):
                in_fence = not in_fence
            old = current["fields"].get(current_field, "")
            current["fields"][current_field] = clean_block((old + "\n" + line).strip())
    return entries


def strip_fence(block: str) -> str:
    block = clean_block(block)
    if block.startswith("```"):
        lines = block.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        block = "\n".join(lines)
    return clean_block(block)


def clean_original_question(block: str) -> str:
    lines = strip_fence(block).splitlines()
    cleaned = []
    for line in lines:
        if line.strip() == "参考答案":
            break
        cleaned.append(line)
    return clean_block("\n".join(cleaned))


def method_summary(major: str | None, subtype: str | None) -> list[str]:
    major = major or ""
    subtype = subtype or ""

    if "充分条件" in major:
        base = [
            "先把题干翻译成 `P -> Q`：P 是前件，Q 是后件。",
            "有效方向只有两条：肯定 P 推出 Q；否定 Q 推出否定 P。",
            "卷面先写推理类型，再写前件、后件和本题事实，最后判断成立或指出错误方向。",
        ]
        if "后件为真" in subtype:
            base.append("看到结果已经出现，只能说明 Q 真；不能倒推 P 必真，要警惕“把结果当唯一原因”。")
        elif "重要条件" in subtype or "前提未必真" in subtype:
            base.append("形式像 `P -> Q` 还不够，要审前提是否真实：重要条件、必要条件不能冒充充分条件。")
        elif "构造" in subtype:
            base.append("补判断时先看题干要推出什么结果，再补一个能直接保证该结果的材料条件。")
        return base

    if "必要条件" in major:
        base = [
            "先把题干翻译成 `只有 P 才 Q`，也就是没有 P 就没有 Q。",
            "有效方向是：Q 成立推出 P 成立；P 不成立推出 Q 不成立。",
            "卷面要说清 P 是不可缺少的条件，不能把“有 P”写成“必然有 Q”。",
        ]
        if "选言" in subtype or "相容" in subtype:
            base.append("遇到“或”要先判断相容还是不相容：相容选言允许两项同时成立，不能误排斥。")
        elif "除非" in subtype or "否则" in subtype:
            base.append("把“除非 P，否则不 Q”改写成“只有 P 才 Q”，再按必要条件方向判断。")
        elif "定义" in subtype or "结论边界" in subtype:
            base.append("必要条件只能说明少了不行，不能把范围、定义或可能性结论推满。")
        return base

    if "三段论" in major:
        base = [
            "先找结论：结论主项是小项，结论谓项是大项；两个前提中反复出现的是中项。",
            "再查三条硬规则：中项至少周延一次，大项小项在结论中周延则在前提中也要周延，不能偷换概念。",
            "卷面答案按“类型/错误名称 + 大项小项中项 + 哪个词被扩大或偷换 + 本题材料”写。",
        ]
        if "构造" in subtype or "补大前提" in subtype or "省略" in subtype:
            base.append("补前提时用中项搭桥，让小项经过中项连到大项，不能只补一个政治观点。")
        elif "换" in subtype or "周延" in subtype:
            base.append("换质位题先看主谓项是否周延，不能为了倒句子改变原判断含义。")
        return base

    if "归纳" in major:
        return [
            "先判断是不是从若干个别事实推出一般结论；如果样本未穷尽，通常是不完全归纳。",
            "因果题要看材料在比较什么：求同看共同因素，求异看唯一差异，求同求异并用要两层比较都成立。",
            "卷面要把材料中的样本、共同点/差异点、结论之间的关系写出来，不能只写方法名。",
        ]

    if "类比" in major:
        return [
            "先找两个对象，再找二者已经相似的属性，最后看题目是否由这些相似属性推出新的相似结论。",
            "类比推理是或然推理，答案不能写成必然成立；要强调提高可靠性需要相似属性多、相关度高、无本质差异。",
            "卷面要写清“把什么和什么类比、相似点在哪里、推出什么、为什么有启发价值”。",
        ]

    if "概念" in major:
        return [
            "先分清题目考概念内涵还是外延：内涵看定义、种差、属概念；外延看包含、交叉、全异。",
            "划分题检查同一标准、子项互斥、划分穷尽；定义题检查不能过宽、过窄、循环或否定定义。",
            "选择题不要被材料热词带走，先把概念关系画成范围关系，再判断选项是否偷换对象。",
        ]

    if "选言" in major or "联言" in major:
        return [
            "先识别判断结构：联言是“并且”，选言是“或者”，假言是条件关系。",
            "联言判断要求各支都真；不相容选言只能有一个真；相容选言允许多个真。",
            "卷面要写出每个支判断的真假或材料依据，再按规则推出结论，不能只报答案。"
        ]

    if "真假" in major or "逻辑规律" in major:
        return [
            "先把人物说法翻译成可判断的命题，再判断是否同一时间、同一方面、同一对象。",
            "矛盾律抓“不能同真”，排中律抓“不能同假”，同一律抓前后概念是否一致。",
            "卷面要把违反的规律名称、本题中冲突的两句话、为什么不能同时成立或同时否定写清楚。",
        ]

    return [
        "先确定推理类型，再把材料中的前提、结论和条件关系翻译清楚。",
        "答题时必须同时写规则和材料，只有方法名或只有材料都不够。",
        "最后用一句考生卷面答案收束，不写制作说明。"
    ]


def write_controls(summary: dict) -> None:
    (RUN / "TASK_BRIEF.md").write_text(
        """# TASK_BRIEF

- run: `23_reasoning_baodian_full_rebuild_20260606`
- trigger: 用户要求推理部分不能只是简陋汇编，必须做成真正“推理宝典”。
- scope: 只处理选必三《逻辑与思维》推理部分。

## Contract

按推理类型分类，保留全部现有 83 条推理题放置点。每个条目必须包含：

- 完整题目材料信息；
- 细则要点；
- 考生应该写出来的优秀答案；
- 当前小类型的做题方法总结。

## Inputs

- `13_reasoning_clean_redo_20260531/选必三_逻辑与思维_推理习题汇编_干净重做版_20260531.md`
- `14_reasoning_baodian_rebuild_after_v87_20260601/delivery/选必三推理宝典_重做版_20260601.md`
- `15_reasoning_direct_compilation_20260601/delivery/选必三推理题汇编_20260601.md`

## Non-goals

- 不新增未回源题目。
- 不宣称 GPT Pro / Claude 真实外审 PASS。
- 本轮先交 Markdown 成稿，DOCX/PDF 后续生成并渲染验收。
""",
        encoding="utf-8",
    )

    (RUN / "DEVELOPMENT_PLAN.md").write_text(
        """# DEVELOPMENT_PLAN

1. 融合 V17/V88 学生化推理宝典、V89 推理题汇编、V87 回源题本。
2. 按推理类型和小题型保留全部 83 条题。
3. 每个小题型前补 `本类做题方法`。
4. 每个条目补齐 `题目材料信息`、`细则要点`、`为什么能想到`、`考生优秀答案`。
5. 跑结构 QA：83 条覆盖、字段缺失、方法段、后台污染、源路径泄露。
6. 后续再生成 DOCX/PDF 并做版式验收。
""",
        encoding="utf-8",
    )

    (RUN / "PROGRESS.md").write_text(
        f"""# PROGRESS

## 2026-06-06 推理宝典重构

- 已创建本 run。
- 已读取项目/选必三门禁文件，并使用既有 13/14/15 三条推理线作为输入。
- 已生成 Markdown 成稿：`delivery/{OUT_MD.name}`。
- 覆盖条目：{summary["entries"]}。
- 小题型方法段：{summary["method_sections"]}。
- 字段缺失条目：{summary["missing_required_entries"]}。
- 源路径/后台词命中：{summary["forbidden_hits"]}。

## 当前边界

- 本轮是推理宝典 Markdown 重构稿，尚未生成 DOCX/PDF。
- 不宣称 GPT Pro / Claude 真实外审 PASS。
""",
        encoding="utf-8",
    )

    verdict = "PASS_MARKDOWN_STRUCTURE" if summary["missing_required_entries"] == 0 and summary["forbidden_hits"] == 0 else "NEEDS_PATCH"
    (RUN / "GOVERNOR.md").write_text(
        f"""# GOVERNOR

## Verdict

verdict: `{verdict}`

## Checks

- 83 条推理题覆盖：{summary["entries"]}/83。
- 每条含题目材料信息、设问/选项、细则要点、为什么能想到、考生优秀答案：缺失 {summary["missing_required_entries"]} 条。
- 每个小题型前有做题方法：{summary["method_sections"]} 段。
- 未发现 `/Users`、`C:\\\\`、`OCR`、`source_extracted`、`A-formal`、`B-choice-signal` 等后台/路径字段：命中 {summary["forbidden_hits"]}。

## Boundary

- 接受范围只到 Markdown 结构重构和字段完整性。
- 尚未完成 Word/PDF 渲染验收。
- 尚未完成外部模型真实审查。
""",
        encoding="utf-8",
    )


def main() -> None:
    student = parse_student_baodian(read_text(BAODIAN))
    compilation = parse_compilation(read_text(COMPILATION))
    source = parse_source_book(read_text(SOURCE_BOOK))

    lines: list[str] = []
    qa_rows: list[dict] = []
    method_sections = 0
    missing_required_entries = 0
    current_major = None
    current_subtype = None
    entry_no_by_subtype: dict[tuple[str, str], int] = {}

    lines.extend(
        [
            "# 2026北京高考政治选必三《逻辑与思维》推理宝典",
            "",
            "按推理类型分类·完整题源材料·细则要点·考生优秀答案版",
            "",
            "飞哥正志讲堂",
            "",
            "## 本版说明",
            "",
            "本版不是题目汇编。它以 83 条已回源推理题为底座，把旧学生化推理宝典的“为什么能想到/答案落点”和回源题本的完整题目材料、当前汇编的细则要点合并。每一类推理先给做题方法，再放同类题。",
            "",
        ]
    )

    for entry in student:
        major = entry["major"]
        subtype = entry["subtype"]
        title = entry["title"]
        if major != current_major:
            current_major = major
            current_subtype = None
            lines.extend(["", f"## {major}", ""])
        if subtype != current_subtype:
            current_subtype = subtype
            method_sections += 1
            lines.extend([f"### {subtype}", "", "【本类做题方法】"])
            for item in method_summary(major, subtype):
                lines.append(f"- {item}")
            lines.append("")

        key = (major or "", subtype or "")
        entry_no_by_subtype[key] = entry_no_by_subtype.get(key, 0) + 1
        n = entry_no_by_subtype[key]
        fields = entry["fields"]
        lookup = entry_key(major, subtype, title)
        comp_fields = compilation.get(lookup, {}).get("fields", {})
        source_fields = source.get(lookup, {}).get("fields", {})

        original = clean_original_question(source_fields.get("原题", ""))
        if not original:
            original = comp_fields.get("题干/材料摘要", fields.get("材料触发点", ""))
        question = comp_fields.get("设问/选项", fields.get("设问", ""))
        rubric = comp_fields.get("答案/细则要点", fields.get("答案落点", ""))
        trigger = fields.get("材料触发点", comp_fields.get("题干/材料摘要", ""))
        why = fields.get("为什么能想到", "")
        answer = fields.get("答案落点", rubric)

        missing = []
        for label, value in [
            ("题目材料信息", original),
            ("设问/选项", question),
            ("细则要点", rubric),
            ("为什么能想到", why),
            ("考生优秀答案", answer),
        ]:
            if not clean_block(value):
                missing.append(label)
        if missing:
            missing_required_entries += 1

        lines.extend(
            [
                f"#### {n}. {title}",
                "",
                "【题目材料信息】",
                "",
                "```text",
                original,
                "```",
                "",
                f"【材料触发点】 {trigger}",
                "",
                f"【设问/选项】 {question}",
                "",
                f"【细则要点】 {rubric}",
                "",
                f"【为什么能想到】 {why}",
                "",
                f"【考生优秀答案】 {answer}",
                "",
            ]
        )

        qa_rows.append(
            {
                "title": title,
                "major": major or "",
                "subtype": subtype or "",
                "has_original": bool(clean_block(original)),
                "has_question": bool(clean_block(question)),
                "has_rubric": bool(clean_block(rubric)),
                "has_why": bool(clean_block(why)),
                "has_answer": bool(clean_block(answer)),
                "missing": ";".join(missing),
            }
        )

    OUT_MD.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")

    forbidden_patterns = ["/Users/", "C:\\", "source_extracted", "OCR", "A-formal", "B-choice-signal", "correct_option_chain"]
    out_text = OUT_MD.read_text(encoding="utf-8")
    forbidden_hits = sum(out_text.count(p) for p in forbidden_patterns)

    with QA_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["title", "major", "subtype", "has_original", "has_question", "has_rubric", "has_why", "has_answer", "missing"],
        )
        writer.writeheader()
        writer.writerows(qa_rows)

    summary = {
        "entries": len(student),
        "source_original_matched": sum(1 for r in qa_rows if r["has_original"]),
        "method_sections": method_sections,
        "missing_required_entries": missing_required_entries,
        "forbidden_hits": forbidden_hits,
        "output": str(OUT_MD.relative_to(ROOT.parent)),
        "qa_csv": str(QA_CSV.relative_to(ROOT.parent)),
    }
    SUMMARY_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    write_controls(summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
