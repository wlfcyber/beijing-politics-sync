from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync")
RUN = ROOT / "reports/选必一_哲学宝典式重建_2026-05-16"
SOURCE = (
    RUN
    / "15_final_delivery_after_recrawl_20260525"
    / "选必一_当代国际政治与经济_主观题术语宝典_学生版_FINAL_精简开头_含速记版_20260525.md"
)
OUT_DIR = RUN / "17_clean_student_opus47_review_20260526"
CLEAN_MD = OUT_DIR / "选必一_当代国际政治与经济_主观题术语宝典_学生版_FINAL_纯净送审稿_20260526.md"
PACKET_DIR = OUT_DIR / "opus47_review_packets"

BUCKETS = ["时代背景", "理论", "经济全球化", "政治多极化", "中国", "联合国"]
REMOVE_TOC = {
    "- 附：总说句 / 兜底加分表达",
    "- 附：模块边界 / 跨书提示",
}
MARKERS = [
    "提醒",
    "提示",
    "边界",
    "使用方法",
    "审计",
    "审核",
    "GPT",
    "Claude",
    "Opus",
    "Codex",
    "debug",
    "TODO",
    "/Users/",
    "reports/",
    "SHA",
    "本模块审题步骤",
    "易错边界",
    "易错提醒",
    "跨模块提醒",
    "边界提示",
    "可迁移提醒",
    "模块边界 / 跨书提示",
    "总说句 / 兜底加分表达",
]


@dataclass
class Packet:
    title: str
    filename: str
    content: str


def squeeze_blanks(text: str) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def join_single_line_answer_fields(text: str) -> str:
    return re.sub(r"(?m)^【卷面句】\n([^#【\n].+)$", r"【卷面句】\1", text)


def drop_non_core_appendices(text: str) -> str:
    speed_old = "# 附：六大要素术语极简速记版"
    speed_new = "# 六大要素术语极简速记版"
    start_candidates = [
        text.find("# 附：总说句 / 兜底加分表达"),
        text.find("# 附：模块边界 / 跨书提示"),
    ]
    starts = [pos for pos in start_candidates if pos != -1]
    speed_pos = text.find(speed_old)
    if speed_pos == -1:
        speed_pos = text.find(speed_new)
    if starts and speed_pos != -1:
        keep_until = min(starts)
        text = text[:keep_until].rstrip() + "\n\n" + text[speed_pos:].lstrip()
    text = text.replace(speed_old, speed_new)
    return text


def clean_toc(lines: list[str]) -> list[str]:
    cleaned: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped in REMOVE_TOC:
            continue
        if stripped == "- 附：六大要素术语极简速记版":
            cleaned.append("- 六大要素术语极简速记版")
        else:
            cleaned.append(line)
    return cleaned


def remove_bucket_prefaces(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("# ") and line[2:].strip() in BUCKETS:
            bucket = line[2:].strip()
            out.append(line)
            out.append("")
            j = i + 1
            next_top = len(lines)
            k = j
            while k < len(lines):
                if lines[k].startswith("# ") and lines[k][2:].strip() != bucket:
                    next_top = k
                    break
                k += 1
            first_core = None
            for k in range(j, next_top):
                if lines[k].startswith("## 核心答题点"):
                    first_core = k
                    break
            if first_core is not None:
                i = first_core
                continue
        out.append(line)
        i += 1
    return "\n".join(out)


def remove_labeled_reminders(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    block_labels = (
        "【本模块审题步骤】",
        "【易错边界】",
        "【二级定位表】",
        "【快速判断】",
        "【开放发展题组辨析】",
    )
    one_line_labels = (
        "【易错提醒】",
        "【跨模块提醒】",
        "【边界】",
        "【可迁移提醒】",
    )
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if any(stripped.startswith(label) for label in one_line_labels):
            i += 1
            continue
        if any(stripped.startswith(label) for label in block_labels):
            i += 1
            while i < len(lines):
                nxt = lines[i].strip()
                if not nxt:
                    i += 1
                    break
                if nxt.startswith("#") or nxt.startswith("【"):
                    break
                i += 1
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def remove_visible_prompt_words(text: str) -> str:
    appendix_reference_patterns = [
        r"；?中国特色大国外交主动作为，是顺应世界发展大势、服务国家发展大局的必然选择（附：总说句 / 兜底加分表达桶）",
        r"；?模块边界（必修二）优惠政策吸引高新技术企业入驻；降低企业税费成本；助力企业科技创新（附：模块边界 / 跨书(?:提示|指向)桶）",
    ]
    for pattern in appendix_reference_patterns:
        text = re.sub(pattern, "", text)
    replacements = [
        ("，迁移提醒", ""),
        ("（迁移提醒）", ""),
        ("迁移提醒", ""),
        ("时代背景/经济全球化边界", "时代背景与经济全球化交叉处"),
        ("选必一边界内", "选必一范围内"),
        ("### 1. 2024丰台一模Q20，", "### 1. 2024丰台一模Q20"),
        (
            '【卷面句】中拉双方在"团结工程"中坚定在国际和地区事务中发出共同声音。',
            '【卷面句】中拉双方在"团结工程"中坚定维护以联合国为核心的国际体系和以国际法为基础的国际秩序，在国际和地区事务中发出共同声音。',
        ),
        ("作答提示", "作答要求"),
        ("设问提示", "设问指向"),
        ("题目提示", "题目指向"),
        ("材料提示", "材料指向"),
        ("提示用", "指向使用"),
        ("提示", "指向"),
        ("提醒", "标注"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def clean_markdown(raw: str) -> str:
    text = drop_non_core_appendices(raw)
    lines = clean_toc(text.splitlines())
    text = "\n".join(lines)
    text = remove_bucket_prefaces(text)
    text = remove_labeled_reminders(text)
    text = remove_visible_prompt_words(text)
    text = join_single_line_answer_fields(text)
    return squeeze_blanks(text)


def split_top_sections(md: str) -> dict[str, str]:
    matches = list(re.finditer(r"(?m)^# (.+)$", md))
    sections: dict[str, str] = {}
    for idx, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(md)
        sections[title] = md[start:end].strip() + "\n"
    return sections


def split_by_core_blocks(section_title: str, section_text: str, max_chars: int = 42000) -> list[str]:
    lines = section_text.splitlines()
    if len(section_text) <= max_chars or not any(line.startswith("## 核心答题点") for line in lines):
        return [section_text]
    heading = lines[0]
    blocks: list[str] = []
    current: list[str] = []
    for line in lines[1:]:
        if line.startswith("## 核心答题点") and current:
            blocks.append("\n".join(current).strip())
            current = [line]
        else:
            current.append(line)
    if current:
        blocks.append("\n".join(current).strip())

    chunks: list[str] = []
    buf: list[str] = []
    size = len(heading) + 2
    for block in blocks:
        block_size = len(block) + 2
        if buf and size + block_size > max_chars:
            chunks.append(heading + "\n\n" + "\n\n".join(buf).strip() + "\n")
            buf = [block]
            size = len(heading) + 2 + block_size
        else:
            buf.append(block)
            size += block_size
    if buf:
        chunks.append(heading + "\n\n" + "\n\n".join(buf).strip() + "\n")
    return chunks


def packet_header(title: str) -> str:
    return f"""# Claude Opus 4.7 审核包：{title}

## 审核任务

请只审核本块，不重写全书。目标是判断这份“纯净学生版送审稿”是否已经去掉学生不需要看的提醒、边界、后台审核、路径、模型名、技术痕迹，同时保留选必一主观题宝典的有效内容。

## 必查项

1. 是否仍残留“提醒 / 提示 / 边界 / 审核 / 审计 / GPT / Claude / Opus / Codex / 本地文件路径 / SHA / TODO / debug”等学生版污染。
2. 是否仍有多余前言、使用说明、模块审题步骤、易错包装、跨书附录、后台话术。
3. 本块的核心答题点、题目例子、卷面句是否被误删或变成空泛框架。
4. 是否存在两个独立考题被合并、同一题例被错放、六大要素归桶明显错误。
5. 只指出必须修的 P0/P1/P2 问题；不要提出审美化改写。

## 输出格式

VERDICT: ACCEPT / PATCH_REQUIRED / REJECT

P0:
- 若无，写“无”。

P1:
- 若无，写“无”。

P2:
- 若无，写“无”。

可直接改的句子:
- 用“原句 => 建议句”列出，必须给出所在标题或题号。

## 待审内容

"""


def build_packets(clean_md: str) -> list[Packet]:
    sections = split_top_sections(clean_md)
    ordered_titles = BUCKETS + ["六大要素术语极简速记版"]
    packets: list[Packet] = []
    seq = 1
    for title in ordered_titles:
        section = sections.get(title)
        if not section:
            continue
        chunks = split_by_core_blocks(title, section)
        for part_idx, chunk in enumerate(chunks, start=1):
            part = f"{title}" if len(chunks) == 1 else f"{title} 第{part_idx}块"
            slug = f"{seq:02d}_{title}"
            if len(chunks) > 1:
                slug += f"_part{part_idx:02d}"
            filename = slug + "_CLAUDE_OPUS47_REVIEW_PACKET.md"
            packets.append(Packet(part, filename, packet_header(part) + chunk))
            seq += 1
    return packets


def marker_counts(text: str) -> dict[str, int]:
    return {marker: text.count(marker) for marker in MARKERS}


def write_index(packets: list[Packet], clean_text: str, qa_text: str) -> None:
    lines = [
        "# 选必一纯净送审稿 Claude Opus 4.7 分块审核包",
        "",
        f"- cleaned_markdown: `{CLEAN_MD.name}`",
        f"- packet_count: {len(packets)}",
        "- status: `READY_FOR_REAL_CLAUDE_OPUS47_SUBMISSION`",
        "- note: 本目录只保存分块送审材料；真实模型返回结果应另存为对应 `*_RESULT.md`。",
        "",
        "## Packets",
        "",
    ]
    for pkt in packets:
        lines.append(f"- `{pkt.filename}` — {pkt.title} — {len(pkt.content)} chars")
    lines.extend(["", "## Cleanup QA", "", qa_text])
    (PACKET_DIR / "PACKET_INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_master_prompt(packets: list[Packet]) -> None:
    lines = [
        "# Claude Opus 4.7 总审核指令",
        "",
        "请作为真实 Claude Opus 4.7 Adaptive 外审，审核本目录中的选必一纯净学生版送审稿。",
        "",
        "## 读取顺序",
        "",
        "1. 先读 `PACKET_INDEX.md`。",
        "2. 再按编号逐个读取 `*_CLAUDE_OPUS47_REVIEW_PACKET.md`。",
        "3. 必要时对照 `../选必一_当代国际政治与经济_主观题术语宝典_学生版_FINAL_纯净送审稿_20260526.md`，但不要重写整本。",
        "",
        "## 审核边界",
        "",
        "- 只判断这份纯净学生版是否已经去掉提醒、提示、边界、后台审核、模型名、本地路径、SHA、TODO/debug 等学生版污染。",
        "- 同时检查是否误删核心内容：六大要素、核心答题点、题例、卷面句、同题组和末尾极简速记版是否仍可用。",
        "- 不做个人审美重写，不要求恢复被删除的提示性包装。",
        "- 对每个分块给出独立 verdict。",
        "",
        "## 输出格式",
        "",
        "OVERALL_VERDICT: ACCEPT / PATCH_REQUIRED / REJECT",
        "",
        "PER_PACKET_VERDICTS:",
        "",
    ]
    for pkt in packets:
        lines.append(f"- `{pkt.filename}`: ACCEPT / PATCH_REQUIRED / REJECT")
    lines.extend(
        [
            "",
            "P0:",
            "- 若无，写“无”。",
            "",
            "P1:",
            "- 若无，写“无”。",
            "",
            "P2:",
            "- 若无，写“无”。",
            "",
            "必须改的原句 => 建议句:",
            "- 若无，写“无”。",
            "",
            "最终一句话结论:",
            "- 说明能否作为选必一纯净学生版继续进入最终 Word/PDF 生成。",
        ]
    )
    (PACKET_DIR / "00_MASTER_OPUS47_REVIEW_INSTRUCTIONS.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    raw = SOURCE.read_text(encoding="utf-8")
    clean = clean_markdown(raw)
    CLEAN_MD.write_text(clean, encoding="utf-8")

    packets = build_packets(clean)
    for pkt in packets:
        (PACKET_DIR / pkt.filename).write_text(pkt.content, encoding="utf-8")

    counts = marker_counts(clean)
    fields = {
        "核心答题点": clean.count("## 核心答题点"),
        "题例 H3": len(re.findall(r"(?m)^### ", clean)),
        "什么时候写": clean.count("【什么时候写】"),
        "设问": clean.count("【设问】"),
        "为什么能想到": clean.count("【为什么能想到】"),
        "卷面句": clean.count("【卷面句】"),
        "同题组": clean.count("【同题组】"),
    }
    qa_lines = [
        "# 纯净送审稿清理 QA",
        "",
        f"- source: `{SOURCE}`",
        f"- output: `{CLEAN_MD}`",
        f"- opus47_packet_dir: `{PACKET_DIR}`",
        "",
        "## Remaining Marker Counts",
        "",
    ]
    for marker, count in counts.items():
        qa_lines.append(f"- {marker}: {count}")
    qa_lines.extend(["", "## Structure Counts", ""])
    for key, value in fields.items():
        qa_lines.append(f"- {key}: {value}")
    qa_lines.extend(["", "## Packet Count", "", f"- Claude Opus 4.7 packets: {len(packets)}"])
    qa_text = "\n".join(qa_lines) + "\n"
    (OUT_DIR / "CLEANUP_AND_PACKET_QA_20260526.md").write_text(qa_text, encoding="utf-8")
    write_index(packets, clean, qa_text)
    write_master_prompt(packets)
    print(CLEAN_MD)
    print(PACKET_DIR)


if __name__ == "__main__":
    main()
