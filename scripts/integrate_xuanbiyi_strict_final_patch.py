import re
import shutil
from collections import defaultdict
from datetime import datetime
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
BASE = next(p for p in (REPO / "reports").glob("*2026-05-16") if (p / "06_final_handbook").exists())
FINAL = BASE / "06_final_handbook"
RUN = BASE / "11_strict_final_rebuild_2026-05-23"
PATCH = RUN / "08_claude_opus_final_review" / "CLAUDE_OPUS_FINAL_FUSION_PATCH.md"

BUCKETS = ["时代背景", "理论", "经济全球化", "政治多极化", "中国", "联合国"]


def find_student_file() -> Path:
    candidates = [p for p in FINAL.glob("*当代国际政治与经济*学生版.md")]
    if not candidates:
        raise FileNotFoundError("student handbook md not found")
    return max(candidates, key=lambda p: p.stat().st_size)


def parse_patch(text: str):
    entries = []
    bucket = ""
    heading = ""
    current = None

    def flush():
        if current and current.get("术语") and current.get("来源"):
            entries.append(current.copy())

    label_re = re.compile(r"^\*\*(.+?)\*\*：(.+)$")
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("## ") and line[3:].strip() in BUCKETS:
            flush()
            current = None
            bucket = line[3:].strip()
            heading = ""
        elif line.startswith("### "):
            flush()
            heading = line[4:].strip()
            current = {"bucket": bucket, "heading": heading}
        elif current:
            m = label_re.match(line)
            if m:
                key, value = m.group(1).strip(), m.group(2).strip()
                current[key] = value
            elif line and current:
                # Preserve wrapped continuation lines on the previous known key.
                for key in ["答案句", "材料触发", "来源", "细则位置", "完整设问", "卷面使用", "术语"]:
                    if key in current and not line.startswith("---"):
                        current[key] += "\n" + line.strip()
                        break
    flush()
    return [e for e in entries if e.get("bucket") in BUCKETS]


def to_student_entry(e, idx: int) -> str:
    term = e.get("术语", "").strip()
    use = e.get("卷面使用", "").strip()
    prompt = e.get("完整设问", "").strip()
    location = e.get("细则位置", "").strip()
    source = e.get("来源", "").strip()
    trigger = e.get("材料触发", "").strip()
    answer = e.get("答案句", "").strip()
    why = f"本题设问与评分细则共同指向“{term}”；材料关系正对应本节点的触发逻辑，作答时应先调用该细则术语，再接本题事实与作用链。"

    parts = [f"### {idx}. {e['heading']}", "", f"【细则术语】{term}", ""]
    if use:
        parts += [f"【卷面使用】{use}", ""]
    parts += [
        f"【材料触发点】{trigger}",
        "",
        f"【设问】{prompt}",
        "",
        f"【为什么能想到】{why}",
        "",
        f"【答案落点】{answer}",
        "",
        f"【细则位置】{location}",
        "",
        f"【来源】{source}",
    ]
    return "\n".join(parts).strip()


def bucket_insert_pos(text: str, bucket: str) -> int:
    start = text.find(f"# {bucket}")
    if start == -1:
        return len(text)
    next_positions = [text.find(f"# {b}", start + 1) for b in BUCKETS if text.find(f"# {b}", start + 1) != -1]
    # Also allow the appendix top-level section after 联合国.
    appendix = text.find("# 附", start + 1)
    if appendix != -1:
        next_positions.append(appendix)
    return min(next_positions) if next_positions else len(text)


def update_toc_counts(text: str, added_counts: dict[str, int]) -> str:
    for bucket, add in added_counts.items():
        if not add:
            continue
        pat = re.compile(rf"- {re.escape(bucket)}（(\d+)条题例）")

        def repl(m):
            return f"- {bucket}（{int(m.group(1)) + add}条题例）"

        text = pat.sub(repl, text, count=1)
    return text


def main():
    student = find_student_file()
    original = student.read_text(encoding="utf-8")
    patch_text = PATCH.read_text(encoding="utf-8")
    entries = parse_patch(patch_text)

    added = []
    skipped = []
    for e in entries:
        source = e.get("来源", "").strip()
        term = e.get("术语", "").strip()
        if source and term and source in original and term in original:
            skipped.append(e)
        else:
            added.append(e)

    grouped = defaultdict(lambda: defaultdict(list))
    for e in added:
        grouped[e["bucket"]][e["术语"]].append(e)

    text = original
    added_counts = defaultdict(int)
    for bucket in BUCKETS:
        if bucket not in grouped:
            continue
        blocks = []
        for term, term_entries in grouped[bucket].items():
            blocks.append(f"## 核心答题点：严格终稿补入：{term}（出现{len(term_entries)}次）")
            blocks.append("")
            blocks.append("【表述积累】")
            blocks.append(f"- {term}")
            blocks.append("")
            blocks.append(f"【本节点真题】共 {len(term_entries)} 条。")
            blocks.append("")
            for idx, e in enumerate(term_entries, 1):
                blocks.append(to_student_entry(e, idx))
                blocks.append("")
            added_counts[bucket] += len(term_entries)
        insert = "\n\n<!-- strict-final-2026-05-24-begin -->\n\n" + "\n".join(blocks).strip() + "\n\n<!-- strict-final-2026-05-24-end -->\n\n"
        pos = bucket_insert_pos(text, bucket)
        text = text[:pos].rstrip() + "\n\n" + insert + text[pos:].lstrip()

    text = update_toc_counts(text, added_counts)

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = student.with_name(student.stem + f"_backup_before_strict_{stamp}" + student.suffix)
    shutil.copy2(student, backup)
    student.write_text(text, encoding="utf-8")

    out = RUN / "09_integration_report.md"
    lines = [
        "# 严格终稿合入报告",
        "",
        f"- 源学生版：{student}",
        f"- 备份：{backup}",
        f"- Claude Opus 补丁：{PATCH}",
        f"- 补丁条目总数：{len(entries)}",
        f"- 已跳过（原文已含同来源+同术语）：{len(skipped)}",
        f"- 新增插入：{len(added)}",
        "",
        "## 新增按桶统计",
        "",
    ]
    for b in BUCKETS:
        lines.append(f"- {b}: {added_counts[b]}")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(out)
    print(f"entries={len(entries)} skipped={len(skipped)} added={len(added)}")


if __name__ == "__main__":
    main()
