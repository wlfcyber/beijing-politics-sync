"""V8 decode-version student-MD residue stripper.

Reads the rendered `2026..._v8_decode版_学生版.md`, walks each entry, removes
audit/scoring/teacher-process residues line by line, drops the entire
`**细则边界**` subsection, and drops any entry that, after cleanup, lacks
either a complete prompt body or a concrete answer chain. Re-emits the
cleaned student-facing markdown and logs dropped-entry boundaries to
`audit/V8_DECODE_DROPPED_ENTRIES.json` so they can be cross-referenced from
the audit document and coverage matrix.

This script is deliberately deterministic so the quality gate is reproducible.
Run after 02_build_student_md.py and before 04_build_audit.py / 05_md_to_docx.py.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"C:/bp_sync_visible/reports/final_56_v8_decode_claudecode_2026-04-29")
STUDENT_MD = ROOT / "outputs" / "2026北京高考政治哲学宝典---三年模拟全触发全链条_v8_decode版_学生版.md"
DROPPED_JSON = ROOT / "audit" / "V8_DECODE_DROPPED_ENTRIES.json"

# A line containing any of these substrings is dropped entirely from a
# student-body section. Each token is anchored to teacher-audit/source-spill
# vocabulary that the independent controller flagged.
DROP_LINE_TOKENS: tuple[str, ...] = (
    "评分细则",
    "阅卷前",
    "阅卷中",
    "细则边界",
    "参考答案",
    "采分点",
    "应给分情况",
    "ADDIN",
    "MERGEFORMAT",
    "高三政治",
    "高三思想政治",
    "知识板块",
    "能力板块",
    "试题分析",
    "学生问题及建议",
    "复练试题",
    "教学启示",
    "学生表现",
    "学生作答",
    "本题标准和变通",
    "典型示例",
    "优秀作答",
    "优秀试卷",
    "书面作答问题",
    "应答与试题无关",
    "应答没有",
    "存在问题",
    "学生答题问题",
    "评卷分析",
    "通篇只从",
    "仅从一个模块作答",
    "同一知识点，不重复给分",
    "政治与法治",
    "法律与生活",
    "逻辑与思维",
    "可参照评分",
    "层次学生",
    "酌情给分",
    "评分视角",
    "总分值不超过",
    "实际阅卷细则",
    "阅卷反思",
    "阅卷感受",
    "审题不精准",
    "材料主旨把握不到位",
    "表达规范不够",
    "高三政治  参考答案",
    "评分点",
    "评分标准",
    "细则1",
    "细则2",
    "细则3",
    "细则：",
    "细则",  # any line with the bare token "细则" is teacher-process metadata
    "0—8分",
    "0-8分",
    "酌情给",
)

# When a line contains any of these markers, we truncate from that line to the
# end of the answer/prompt section (i.e. the rest belongs to teacher-process
# narrative or audit metadata).
TRUNCATE_AT_MARKERS: tuple[str, ...] = (
    "（一）本题标准和变通",
    "（二）学生表现",
    "（二）学生作答",
    "（三）教学启示",
    "（三）学生表现",
    "（一）试题分析",
    "二、典型示例",
    "三、典型示例",
    "四、学生问题及建议",
    "五、复练试题",
    "三、典型",
    "二、试题分析",
    "一、试题分析",
    "学生问题及建议",
    "复练试题",
    "教学启示",
    "本题标准和变通",
    "ADDIN CNKISM",
    "高三思想政治答案",
    "高三政治  参考答案",
    "评卷分析",
    "学生作答情况",
    "评分参考",
    "学生表现",
    "存在问题",
    "优秀试卷",
    "优秀作答",
    "典型示例",
)

# These lines should be replaced silently (often page artefacts that survive
# the universal noise stripper in 02_build_student_md.py).
DROP_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"^\s*\d{1,2}\s*[\.．]\s*[A-D]\s*$"),
    re.compile(r"^\s*[A-D][\.．]\s*$"),
    re.compile(r"^\s*PAGE\s*[A-Za-z\\\*\s]*$"),
    re.compile(r"^\s*第\s*\d+\s*页[共/]?\s*\d+\s*页\s*$"),
)

# A normalised placeholder we wrote when the answer chain was missing entirely.
PLACEHOLDER_MISSING_ANSWER = "（参考答案缺失：仅依据细则触发点提示，正式答题以细则为准。）"

# Regex helpers
ENTRY_HEADER_RE = re.compile(r"^####\s+(.*?)\s*$")
NODE_HEADER_RE = re.compile(r"^###\s+(\d+\.\d+)\s+(.*?)\s*$")
UNIT_HEADER_RE = re.compile(r"^##\s+(第[一二三四五六七八九十]+单元.*?)\s*$")
APPENDIX_HEADER_RE = re.compile(r"^##\s+附录")
BOLD_LABEL_RE = re.compile(r"^\*\*(完整设问|关键材料触发|为何触发该原理|答案落点|细则边界)\*\*\s*$")


def line_should_be_dropped(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    for tok in DROP_LINE_TOKENS:
        if tok in s:
            return True
    for pat in DROP_PATTERNS:
        if pat.match(line):
            return True
    return False


def truncate_at_audit_marker(lines: list[str]) -> list[str]:
    """Cut a section's body at the first audit/teacher-process marker."""
    out: list[str] = []
    for ln in lines:
        s = ln.strip()
        if any(m in s for m in TRUNCATE_AT_MARKERS):
            break
        out.append(ln)
    return out


def clean_section_body(lines: list[str]) -> list[str]:
    """Apply truncate-at-marker, then drop forbidden lines, then collapse blanks."""
    lines = truncate_at_audit_marker(lines)
    cleaned: list[str] = []
    for ln in lines:
        if line_should_be_dropped(ln):
            continue
        cleaned.append(ln)
    # Collapse consecutive blank lines
    out: list[str] = []
    blank = False
    for ln in cleaned:
        if not ln.strip():
            if blank:
                continue
            blank = True
            out.append("")
        else:
            blank = False
            out.append(ln)
    while out and not out[-1].strip():
        out.pop()
    while out and not out[0].strip():
        out.pop(0)
    return out


def split_entry_sections(entry_lines: list[str]) -> tuple[str, dict[str, list[str]]]:
    """Return (heading, {section_label -> body_lines}) for one entry."""
    heading = entry_lines[0]
    body = entry_lines[1:]
    sections: dict[str, list[str]] = {}
    cur_label: str | None = None
    cur_body: list[str] = []
    for ln in body:
        m = BOLD_LABEL_RE.match(ln.strip())
        if m:
            if cur_label is not None:
                sections[cur_label] = cur_body
            cur_label = m.group(1)
            cur_body = []
        else:
            if cur_label is None:
                # Lines before the first labeled section — ignore
                continue
            cur_body.append(ln)
    if cur_label is not None:
        sections[cur_label] = cur_body
    return heading, sections


def render_entry(heading: str, sections: dict[str, list[str]]) -> list[str]:
    out: list[str] = [heading, ""]
    for label in ("完整设问", "关键材料触发", "为何触发该原理", "答案落点"):
        body = sections.get(label) or []
        body = [ln for ln in body if ln.strip()]
        if not body:
            continue
        out.append(f"**{label}**")
        out.append("")
        out.extend(body)
        out.append("")
    return out


def has_meaningful_answer(answer_lines: list[str]) -> bool:
    body = "\n".join(ln for ln in answer_lines if ln.strip()).strip()
    if not body:
        return False
    if PLACEHOLDER_MISSING_ANSWER in body:
        return False
    # Need at least 30 visible Chinese-or-letter characters of substance.
    visible = re.sub(r"\s+", "", body)
    return len(visible) >= 30


def has_meaningful_prompt(prompt_lines: list[str]) -> bool:
    body = "\n".join(ln for ln in prompt_lines if ln.strip()).strip()
    if not body:
        return False
    visible = re.sub(r"\s+", "", body)
    return len(visible) >= 30


def parse_md_into_blocks(md_text: str) -> list[dict]:
    """Walk the MD into a flat block list preserving order.

    Block kinds:
      - 'preamble': header lines before the first '## 第N单元'
      - 'unit_open'
      - 'node_open'
      - 'node_placeholder' (the parenthesised '本节点暂未...' line for a node)
      - 'entry'
      - 'separator'
      - 'appendix'  (one block; everything from '## 附录' to EOF)
    """
    lines = md_text.splitlines()
    blocks: list[dict] = []
    i = 0
    n = len(lines)

    # Preamble
    pre_end = n
    for j, ln in enumerate(lines):
        if UNIT_HEADER_RE.match(ln):
            pre_end = j
            break
    blocks.append({"kind": "preamble", "lines": lines[:pre_end]})

    # Find appendix start
    apx_start = n
    for j in range(pre_end, n):
        if APPENDIX_HEADER_RE.match(lines[j]):
            apx_start = j
            break

    # Body walk
    j = pre_end
    cur_entry: list[str] | None = None
    while j < apx_start:
        ln = lines[j]
        if UNIT_HEADER_RE.match(ln):
            if cur_entry is not None:
                blocks.append({"kind": "entry", "lines": cur_entry})
                cur_entry = None
            blocks.append({"kind": "unit_open", "lines": [ln]})
            j += 1
            continue
        if NODE_HEADER_RE.match(ln):
            if cur_entry is not None:
                blocks.append({"kind": "entry", "lines": cur_entry})
                cur_entry = None
            blocks.append({"kind": "node_open", "lines": [ln]})
            j += 1
            continue
        if ENTRY_HEADER_RE.match(ln):
            if cur_entry is not None:
                blocks.append({"kind": "entry", "lines": cur_entry})
            cur_entry = [ln]
            j += 1
            continue
        if ln.strip() == "---":
            if cur_entry is not None:
                blocks.append({"kind": "entry", "lines": cur_entry})
                cur_entry = None
            blocks.append({"kind": "separator", "lines": [ln]})
            j += 1
            continue
        if cur_entry is not None:
            cur_entry.append(ln)
        else:
            blocks.append({"kind": "node_body", "lines": [ln]})
        j += 1
    if cur_entry is not None:
        blocks.append({"kind": "entry", "lines": cur_entry})

    blocks.append({"kind": "appendix", "lines": lines[apx_start:]})
    return blocks


def filter_node_body_line(line: str) -> bool:
    """Keep node-body line iff it does NOT contain audit/forbidden tokens."""
    s = line.strip()
    if not s:
        return True
    return not line_should_be_dropped(line)


def main() -> None:
    md_text = STUDENT_MD.read_text(encoding="utf-8")
    blocks = parse_md_into_blocks(md_text)

    dropped: list[dict] = []
    kept_entries_per_node: dict[str, int] = {}

    # Work on the body block list (everything except 'appendix' block at the end)
    appendix_block = next(b for b in blocks if b["kind"] == "appendix")
    body_blocks = [b for b in blocks if b["kind"] != "appendix"]

    cur_unit_title: str | None = None
    cur_node_code: str | None = None
    cur_node_title: str | None = None

    new_blocks: list[dict] = []
    for b in body_blocks:
        if b["kind"] == "unit_open":
            cur_unit_title = b["lines"][0]
            new_blocks.append(b)
            continue
        if b["kind"] == "node_open":
            m = NODE_HEADER_RE.match(b["lines"][0])
            if m:
                cur_node_code = m.group(1)
                cur_node_title = m.group(2)
            new_blocks.append(b)
            continue
        if b["kind"] == "entry":
            heading, sections = split_entry_sections(b["lines"])
            # Drop 细则边界 entirely
            sections.pop("细则边界", None)
            for label in ("完整设问", "关键材料触发", "为何触发该原理", "答案落点"):
                if label in sections:
                    sections[label] = clean_section_body(sections[label])
            prompt_ok = has_meaningful_prompt(sections.get("完整设问") or [])
            answer_ok = has_meaningful_answer(sections.get("答案落点") or [])
            entry_title = heading.replace("####", "").strip()
            if not (prompt_ok and answer_ok):
                dropped.append({
                    "node_code": cur_node_code or "",
                    "node_title": cur_node_title or "",
                    "entry_title": entry_title,
                    "reason": (
                        ("missing/short complete prompt; " if not prompt_ok else "")
                        + ("missing/placeholder answer chain" if not answer_ok else "")
                    ).strip(" ;"),
                })
                continue
            kept_entries_per_node[cur_node_code or ""] = (
                kept_entries_per_node.get(cur_node_code or "", 0) + 1
            )
            new_lines = render_entry(heading, sections)
            new_blocks.append({"kind": "entry", "lines": new_lines})
            new_blocks.append({"kind": "separator", "lines": ["---"]})
            continue
        if b["kind"] == "separator":
            # Skip; we re-emit our own separator after each kept entry
            continue
        if b["kind"] == "node_body":
            # Filter forbidden tokens from node-body lines (placeholders etc.)
            body_lines = [ln for ln in b["lines"] if filter_node_body_line(ln)]
            new_blocks.append({"kind": "node_body", "lines": body_lines})
            continue
        new_blocks.append(b)

    # For each node, if no entry survives, ensure the placeholder appears.
    # We do a second pass: scan node groups and inject placeholders where missing.
    out_blocks: list[dict] = []
    i = 0
    while i < len(new_blocks):
        b = new_blocks[i]
        out_blocks.append(b)
        if b["kind"] == "node_open":
            # Look ahead until next node_open / unit_open / appendix to count entries
            j = i + 1
            entry_count = 0
            saw_placeholder = False
            while j < len(new_blocks):
                nb = new_blocks[j]
                if nb["kind"] in ("node_open", "unit_open"):
                    break
                if nb["kind"] == "entry":
                    entry_count += 1
                if nb["kind"] == "node_body":
                    txt = "\n".join(nb["lines"])
                    if "本节点暂未在三年模拟主观题中检出独立触发条目" in txt:
                        saw_placeholder = True
                j += 1
            if entry_count == 0 and not saw_placeholder:
                out_blocks.append({"kind": "node_body", "lines": [""]})
                out_blocks.append({"kind": "node_body", "lines": ["（本节点暂未在三年模拟主观题中检出独立触发条目；选择题部分见错肢总结。）"]})
                out_blocks.append({"kind": "node_body", "lines": [""]})
        i += 1

    # Rebuild appendix with the kept entries' suite-name index.
    # Preserve appendix preamble structure: '## 附录·节点-题目索引一览' + per-unit
    # listings. We harvest kept entry titles and group by node.
    kept_titles_per_node: dict[str, list[str]] = {}
    cur_node_code = None
    for b in out_blocks:
        if b["kind"] == "node_open":
            m = NODE_HEADER_RE.match(b["lines"][0])
            if m:
                cur_node_code = m.group(1)
        elif b["kind"] == "entry" and cur_node_code:
            heading_text = b["lines"][0].replace("####", "").strip()
            kept_titles_per_node.setdefault(cur_node_code, []).append(heading_text)

    # Rebuild appendix block: keep its first heading line, then re-emit listings
    # using kept_titles_per_node, preserving the original unit ordering.
    appendix_lines = appendix_block["lines"]
    new_appendix: list[str] = []
    new_appendix.append("## 附录·节点-题目索引一览")
    new_appendix.append("")
    # Walk units & nodes from out_blocks order
    unit_order: list[tuple[str, list[tuple[str, str]]]] = []
    cur_unit: tuple[str, list[tuple[str, str]]] | None = None
    for b in out_blocks:
        if b["kind"] == "unit_open":
            if cur_unit is not None:
                unit_order.append(cur_unit)
            cur_unit = (b["lines"][0].replace("##", "").strip(), [])
        elif b["kind"] == "node_open" and cur_unit is not None:
            m = NODE_HEADER_RE.match(b["lines"][0])
            if m:
                cur_unit[1].append((m.group(1), m.group(2)))
    if cur_unit is not None:
        unit_order.append(cur_unit)

    for unit_title, nodes in unit_order:
        new_appendix.append(f"### {unit_title}")
        new_appendix.append("")
        for code, title in nodes:
            titles = kept_titles_per_node.get(code, [])
            if not titles:
                new_appendix.append(f"- {code} {title}：（本宝典暂无主观题触发，留待补录。）")
                continue
            ids = "、".join(t.split("第")[0] + ("Q" + (t.split("第")[1].split("题")[0] if "第" in t and "题" in t else "")) for t in titles)
            new_appendix.append(f"- {code} {title}：{ids}")
        new_appendix.append("")

    # Stitch the entire MD back together
    out_lines: list[str] = []
    for b in out_blocks:
        if b["kind"] == "preamble":
            out_lines.extend(b["lines"])
            continue
        if b["kind"] == "unit_open":
            out_lines.append(b["lines"][0])
            out_lines.append("")
            continue
        if b["kind"] == "node_open":
            out_lines.append(b["lines"][0])
            out_lines.append("")
            continue
        if b["kind"] == "node_body":
            out_lines.extend(b["lines"])
            continue
        if b["kind"] == "entry":
            out_lines.extend(b["lines"])
            continue
        if b["kind"] == "separator":
            if out_lines and out_lines[-1].strip() != "":
                out_lines.append("")
            out_lines.append("---")
            out_lines.append("")
            continue
    out_lines.extend(new_appendix)

    # Collapse 3+ blank lines to 2
    final_text = re.sub(r"\n{3,}", "\n\n", "\n".join(out_lines)).rstrip() + "\n"
    STUDENT_MD.write_text(final_text, encoding="utf-8")

    DROPPED_JSON.parent.mkdir(parents=True, exist_ok=True)
    DROPPED_JSON.write_text(json.dumps({
        "dropped_entries": dropped,
        "kept_entries_per_node": kept_entries_per_node,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"wrote {STUDENT_MD}; chars={len(final_text)}")
    print(f"dropped entries: {len(dropped)}")
    for d in dropped:
        print(f"  - {d['node_code']} {d['entry_title']}: {d['reason']}")
    print(f"kept entries per node:")
    for code, n in sorted(kept_entries_per_node.items()):
        print(f"  {code}: {n}")


if __name__ == "__main__":
    main()
