from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path.cwd()
RUN = next(p for p in (ROOT / "reports").glob("*") if (p / "02_codex_batches").exists())
FINAL_DIR = RUN / "06_final_handbook"
STUDENT = FINAL_DIR / "选必一_当代国际政治与经济_主观题术语宝典_学生版.md"
NAV = FINAL_DIR / "选必一_当代国际政治与经济_主观题术语宝典_考前导航版.md"


@dataclass
class RemovedExample:
    bucket: str
    core: str
    heading: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")


def write(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def core_title_from_heading(line: str) -> str | None:
    match = re.match(r"^## 核心答题点：(.+?)（出现\d+次）$", line)
    return match.group(1) if match else None


def remove_merged_examples(text: str) -> tuple[str, list[RemovedExample]]:
    lines = text.splitlines()
    out: list[str] = []
    removed: list[RemovedExample] = []
    bucket = ""
    core = ""
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("# ") and not line.startswith("## "):
            bucket = line[2:].strip()
        next_core = core_title_from_heading(line)
        if next_core:
            core = next_core

        if line.startswith("### ") and "；" in line:
            removed.append(RemovedExample(bucket=bucket, core=core, heading=line[4:].strip()))
            i += 1
            while i < len(lines) and not (
                lines[i].startswith("### ")
                or lines[i].startswith("## ")
                or lines[i].startswith("# ")
            ):
                i += 1
            while out and out[-1] == "":
                out.pop()
            out.append("")
            continue

        out.append(line)
        i += 1
    return "\n".join(out).rstrip() + "\n", removed


def count_examples(text: str) -> tuple[dict[str, int], dict[str, int]]:
    core_counts: dict[str, int] = {}
    bucket_counts: dict[str, int] = {}
    bucket = ""
    core = ""
    for line in text.splitlines():
        if line.startswith("# ") and not line.startswith("## "):
            bucket = line[2:].strip()
        next_core = core_title_from_heading(line)
        if next_core:
            core = next_core
            core_counts.setdefault(core, 0)
        if line.startswith("### ") and core:
            core_counts[core] = core_counts.get(core, 0) + 1
            bucket_counts[bucket] = bucket_counts.get(bucket, 0) + 1
    return core_counts, bucket_counts


def update_student_counts(text: str, core_counts: dict[str, int], bucket_counts: dict[str, int]) -> str:
    lines = text.splitlines()
    out: list[str] = []
    core = ""
    for line in lines:
        next_core = core_title_from_heading(line)
        if next_core:
            core = next_core
            out.append(re.sub(r"（出现\d+次）", f"（出现{core_counts.get(core, 0)}次）", line))
            continue
        if line.startswith("【本节点真题】共 ") and core:
            out.append(f"【本节点真题】共 {core_counts.get(core, 0)} 条。")
            continue
        dir_match = re.match(r"^-\s+(.+?)（\d+条题例）$", line)
        if dir_match and dir_match.group(1) in bucket_counts:
            name = dir_match.group(1)
            out.append(f"- {name}（{bucket_counts[name]}条题例）")
            continue
        out.append(line)
    return "\n".join(out).rstrip() + "\n"


def update_nav_counts(text: str, core_counts: dict[str, int]) -> str:
    lines = text.splitlines()
    out: list[str] = []
    for line in lines:
        row_match = re.match(r"^\| ([^|]+?) \| \d+ \| (.*)$", line)
        if row_match:
            core = row_match.group(1).strip()
            if core in core_counts:
                out.append(f"| {core} | {core_counts[core]} | {row_match.group(2)}")
                continue
        out.append(line)
    return "\n".join(out).rstrip() + "\n"


def main() -> None:
    student_text = read(STUDENT)
    cleaned, removed = remove_merged_examples(student_text)
    core_counts, bucket_counts = count_examples(cleaned)
    cleaned = update_student_counts(cleaned, core_counts, bucket_counts)
    nav_text = update_nav_counts(read(NAV), core_counts)
    write(STUDENT, cleaned)
    write(NAV, nav_text)
    print(f"removed={len(removed)}")
    print(f"core_count={len(core_counts)}")
    print(f"main_examples={sum(bucket_counts.values())}")
    for item in removed:
        print(f"{item.bucket} | {item.core} | {item.heading}")


if __name__ == "__main__":
    main()
