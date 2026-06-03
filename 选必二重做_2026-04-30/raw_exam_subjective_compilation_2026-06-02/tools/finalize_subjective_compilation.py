#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from copy import deepcopy
from pathlib import Path

RUN_DIR = Path(__file__).resolve().parents[1]
TEXT_DIR = RUN_DIR / "02_extracted_text"
PACKET_DIR = RUN_DIR / "03_source_packets"
CONTROL_DIR = RUN_DIR / "00_control"
OUT_DIR = RUN_DIR / "05_output"

AUTO_PACKETS = PACKET_DIR / "source_packets_auto.jsonl"
FINAL_PACKETS = PACKET_DIR / "source_packets_final.jsonl"
FINAL_CSV = PACKET_DIR / "source_packets_final.csv"
FINAL_MD = OUT_DIR / "选必二法律与生活_习题汇编_2024-2026.md"


def read_packets() -> list[dict]:
    return [json.loads(line) for line in AUTO_PACKETS.read_text(encoding="utf-8").splitlines() if line.strip()]


def clean_lines(lines: list[str]) -> str:
    kept: list[str] = []
    for line in lines:
        s = line.rstrip()
        if re.match(r"^\[PDF_PAGE \d+\]$", s):
            continue
        if re.match(r"^\[PPT_SLIDE \d+\]$", s):
            continue
        if re.match(r"^===== .* page \d+ =====$", s):
            continue
        if s in {"激活 Windows", "Windows", "CS 扫描全能王", "3亿人都在用的扫描App"}:
            continue
        if "扫描全能王" in s:
            continue
        if re.match(r"^高三思想政治 第\d+页", s):
            continue
        kept.append(s)
    return "\n".join(kept).strip()


def source_lines(source_id: str, start: int, end: int) -> str:
    path = next(TEXT_DIR.glob(f"{source_id}*.txt"))
    lines = path.read_text(encoding="utf-8").splitlines()
    return clean_lines(lines[start - 1 : end])


def split_at(text: str, marker: str) -> tuple[str, str]:
    i = text.index(marker)
    return text[:i].strip(), text[i:].strip()


def replace_title(e: dict, suffix: str) -> None:
    e["title"] = f"{e['year']} · {e['district_or_exam']} · {e['paper_type']} · {suffix}"


def make_sub(base: dict, suffix: str, material: str, prompt: str, rubric: str, pending: str | None = None) -> dict:
    e = deepcopy(base)
    replace_title(e, suffix)
    e["material"] = material.strip()
    e["prompt"] = prompt.strip()
    e["rubric"] = rubric.strip()
    e["pending_reason"] = pending or ""
    return e


def extract_between(text: str, start: str, end: str | None = None) -> str:
    i = text.index(start)
    j = text.index(end, i) if end else len(text)
    return text[i:j].strip()


def transform_entry(e: dict) -> list[dict]:
    eid = e["entry_id"]
    out: list[dict] = []

    if eid == "E002":
        p1, p2 = split_at(e["prompt"], "（2）")
        r1 = extract_between(e["rubric"], "（1）", "（2）")
        r2 = extract_between(e["rubric"], "（2）")
        out.append(make_sub(e, "第19题第1问", e["material"], p1, "19.（9分）\n" + r1))
        out.append(make_sub(e, "第19题第2问", e["material"], p2, "19.（9分）\n" + r2))
        return out

    if eid == "E007":
        e = deepcopy(e)
        e["rubric"] = source_lines("SRC_f887d1b620_细则", 326, 327)
        return [e]

    if eid == "E008":
        p = e["prompt"]
        material2 = extract_between(p, "在街道", "（2）")
        prompt2 = extract_between(p, "（2）")
        rubric2 = source_lines("SRC_f887d1b620_细则", 374, 375)
        return [
            make_sub(
                e,
                "第18题第2问【待确认】",
                e["material"] + "\n" + material2,
                prompt2,
                rubric2,
                e.get("pending_reason") or "设问未直接写《法律与生活》，但情境为相邻关系、违约责任、人民调解与司法确认，需人工复核模块边界。",
            )
        ]

    if eid == "E009":
        prompts = re.split(r"(?=（[123]）)", e["prompt"])
        prompts = [x.strip() for x in prompts if x.strip()]
        rub = e["rubric"]
        r1 = extract_between(rub, "（1）", "（2）")
        r2 = extract_between(rub, "（2）", "（3）")
        r3 = extract_between(rub, "（3）")
        for idx, (p, r) in enumerate(zip(prompts, [r1, r2, r3]), 1):
            out.append(make_sub(e, f"第18题第{idx}问【待确认】", e["material"], p, "18．（8分）\n" + r, e.get("pending_reason")))
        return out

    if eid == "E013":
        prompt = extract_between(e["prompt"], "资料卡", "（2）")
        return [make_sub(e, "第19题第1问", e["material"], prompt, e["rubric"])]

    if eid == "E015":
        prompt = extract_between(e["prompt"], "(2)")
        rubric = "\n".join(
            [
                source_lines("SRC_dfa78c60e1_19_2", 5, 7),
                source_lines("SRC_dfa78c60e1_19_2", 16, 25),
            ]
        )
        return [make_sub(e, "第19题第2问", e["material"], prompt, rubric)]

    if eid == "E019":
        material = e["material"]
        parts = e["prompt"].split("（2）")
        p1 = parts[0].strip()
        p2 = "（2）" + parts[1].strip()
        rub = e["rubric"]
        r1 = extract_between(rub, "关于AI作品权利归属问题", "[PPT_SLIDE 14]")
        r2 = extract_between(rub, "双方签订的相关手续", "[PPT_SLIDE 15]")
        out.append(make_sub(e, "第20题第1问", material, p1 + "\n阅读材料，运用《法律与生活》知识，完成裁判理由。", r1))
        out.append(make_sub(e, "第20题第2问", material, p2, r2))
        return out

    if eid == "E021":
        p1, p2 = split_at(e["prompt"], "(2)")
        r1 = source_lines("SRC_436f84dc1e_细则", 148, 177)
        r2 = source_lines("SRC_436f84dc1e_细则", 179, 187)
        out.append(make_sub(e, "第20题第1问", e["material"], p1, "20.（10分）\n" + r1))
        out.append(make_sub(e, "第20题第2问", e["material"], "(2)" + p2.removeprefix("(2)").strip(), "20.（10分）\n" + r2))
        return out

    if eid == "E022":
        e = deepcopy(e)
        e["rubric_source_id"] = "SRC_65f9eb7854_朝阳高三期末2025"
        e["evidence_type"] = "answer_reference"
        e["rubric"] = source_lines("SRC_65f9eb7854_朝阳高三期末2025", 298, 323)
        return [e]

    if eid == "E031":
        p = e["prompt"]
        p1 = extract_between(p, "(1)", "材料二")
        material2 = extract_between(p, "材料二", "(2)")
        p2 = extract_between(p, "(2)")
        r1 = source_lines("SRC_6087ed5408_细则", 46, 49)
        r2 = source_lines("SRC_6087ed5408_细则", 50, 56)
        out.append(make_sub(e, "第19题第1问", e["material"], p1, r1))
        out.append(make_sub(e, "第19题第2问", e["material"] + "\n" + material2, p2, r2))
        return out

    if eid == "E033":
        p1, p2 = split_at(e["prompt"], "（2）")
        r1 = source_lines("SRC_88c6e8f353_细则", 418, 457)
        r2 = source_lines("SRC_88c6e8f353_细则", 492, 505)
        out.append(make_sub(e, "第18题第1问", e["material"], p1, r1))
        out.append(make_sub(e, "第18题第2问", e["material"], "（2）" + p2.removeprefix("（2）").strip(), r2))
        return out

    if eid == "E023":
        e = deepcopy(e)
        e["rubric_source_id"] = "SRC_20820628be_试卷"
        e["evidence_type"] = "answer_reference"
        e["rubric"] = source_lines("SRC_20820628be_试卷", 278, 281)
        return [e]

    if eid == "E036":
        p1, _ = split_at(e["prompt"], "材料二")
        r1 = extract_between(e["rubric"], "18.（15分）", "（2）（7分）")
        return [make_sub(e, "第18题第1问", e["material"], p1, r1)]

    if eid == "E037":
        material = source_lines("SRC_0e98e571e5_试卷", 230, 242)
        p1 = source_lines("SRC_0e98e571e5_试卷", 243, 243)
        r1 = source_lines("SRC_7301f6d3c6_细则", 22, 29)
        p2 = source_lines("SRC_0e98e571e5_试卷", 244, 244)
        r2 = source_lines("SRC_7301f6d3c6_细则", 30, 37)
        base = deepcopy(e)
        base["question_no"] = "17"
        out.append(make_sub(base, "第17题第1问", material, p1, r1))
        out.append(
            make_sub(
                base,
                "第17题第2问【待确认】",
                material,
                p2,
                r2,
                "设问写“法治知识”且涉及最高法典型案例，需人工复核是否归入选必二或政治与法治。",
            )
        )
        return out

    if eid == "E039":
        p1, _ = split_at(e["prompt"], "材料一 方某")
        r1 = e["rubric"]
        return [make_sub(e, "第18题第1问", e["material"], p1, r1)]

    if eid == "E041":
        p = e["prompt"]
        material2 = extract_between(p, "材料二", "（3）")
        p3 = extract_between(p, "（3）")
        r3 = source_lines("SRC_14176e949d_细则", 61, 69)
        return [make_sub(e, "第18题第3问", material2, p3, r3)]

    if eid == "E042":
        p = e["prompt"]
        material2 = extract_between(p, "材料二", "（2）")
        p2 = extract_between(p, "（2）")
        r2 = source_lines("SRC_829ff10080_2026北京海淀高三二模政治_教师版", 153, 153)
        return [make_sub(e, "第18题第2问", material2, p2, r2)]

    if eid == "E035":
        e = deepcopy(e)
        e["rubric"] = source_lines("SRC_44f3b42c2c_细则", 263, 265)
        return [e]

    if eid == "E046":
        p1, _ = split_at(e["prompt"], "（2）")
        r1 = source_lines("SRC_35ef942428_细则", 143, 158)
        return [make_sub(e, "第19题第1问", e["material"], p1, r1)]

    if eid == "E048":
        p1, _ = split_at(e["prompt"], "（2）")
        r1 = extract_between(e["rubric"], "18．（15分）", "（2） （7分）")
        return [make_sub(e, "第18题第1问", e["material"], p1, r1)]

    return [e]


def new_entries(template: dict) -> list[dict]:
    entries: list[dict] = []

    e = deepcopy(template)
    e.update(
        {
            "candidate_index": 53,
            "year": "2025",
            "district_or_exam": "海淀",
            "paper_type": "期中",
            "question_no": "21",
            "question_source_id": "SRC_e3da1b6b45_试卷",
            "question_path": "/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025海淀期中/试卷/试卷.pdf",
            "rubric_source_id": "SRC_cda046c2d3_细则",
            "rubric_path": "/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025海淀期中/细则/细则.docx",
            "evidence_type": "rubric_or_marking",
            "pending_reason": "",
        }
    )
    entries.append(
        make_sub(
            e,
            "第21题第1问",
            source_lines("SRC_e3da1b6b45_试卷", 230, 242),
            source_lines("SRC_e3da1b6b45_试卷", 243, 243),
            source_lines("SRC_cda046c2d3_细则", 15, 16),
        )
    )

    e = deepcopy(template)
    e.update(
        {
            "candidate_index": 98,
            "year": "2026",
            "district_or_exam": "西城",
            "paper_type": "二模",
            "question_no": "18",
            "question_source_id": "SRC_c5ed8aa7ef_2026北京西城高三二模政治_教师版",
            "question_path": "/Users/wanglifei/Desktop/2026模拟题/2026各区二模/2026西城二模/试卷/2026北京西城高三二模政治（教师版）.docx",
            "rubric_source_id": "SRC_ccb1c36568_西城二模评标",
            "rubric_path": "/Users/wanglifei/Desktop/2026模拟题/2026各区二模/2026西城二模/细则/西城二模评标.pdf",
            "evidence_type": "rubric_or_marking",
        }
    )
    mat1 = source_lines("SRC_c5ed8aa7ef_2026北京西城高三二模政治_教师版", 120, 124)
    mat2 = source_lines("SRC_c5ed8aa7ef_2026北京西城高三二模政治_教师版", 126, 126)
    entries.append(
        make_sub(
            e,
            "第18题第1问",
            mat1,
            source_lines("SRC_c5ed8aa7ef_2026北京西城高三二模政治_教师版", 125, 125),
            source_lines("SRC_ccb1c36568_西城二模评标", 82, 93),
        )
    )
    entries.append(
        make_sub(
            e,
            "第18题第2问【待确认】",
            mat1 + "\n" + mat2,
            source_lines("SRC_c5ed8aa7ef_2026北京西城高三二模政治_教师版", 127, 127),
            source_lines("SRC_ccb1c36568_西城二模评标", 98, 108),
            "权责边界、法治营商环境与产业发展交叉，需人工复核是否全归入选必二。",
        )
    )
    entries.append(
        make_sub(
            e,
            "第18题第3问【待确认】",
            mat2,
            source_lines("SRC_c5ed8aa7ef_2026北京西城高三二模政治_教师版", 128, 128),
            source_lines("SRC_ccb1c36568_西城二模评标", 130, 143),
            "法治与国家治理能力现代化交叉，需人工复核是否归入选必二或政治与法治。",
        )
    )
    return entries


TYPE_ORDER = {"期中": 0, "期末": 1, "一模": 2, "二模": 3, "统练": 4, "练习": 5, "检测": 6}


def qnum(title: str) -> tuple[int, int]:
    m = re.search(r"第(\d+)题(?:第(\d+)问)?", title)
    if not m:
        return (999, 999)
    return (int(m.group(1)), int(m.group(2) or 0))


def sort_key(e: dict) -> tuple:
    return (e.get("year") or "9999", e.get("district_or_exam") or "", TYPE_ORDER.get(e.get("paper_type") or "", 99), *qnum(e.get("title", "")))


def renumber(entries: list[dict]) -> list[dict]:
    sorted_entries = sorted(entries, key=sort_key)
    for i, e in enumerate(sorted_entries, 1):
        e["entry_id"] = f"E{i:03d}"
        for field in ("material", "prompt", "rubric"):
            e[field] = clean_lines(e.get(field, "").splitlines())
    return sorted_entries


def write_packets(entries: list[dict]) -> None:
    FINAL_PACKETS.write_text("\n".join(json.dumps(e, ensure_ascii=False) for e in entries) + "\n", encoding="utf-8")
    fields = list(entries[0].keys())
    with FINAL_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(entries)


def suite_id_for_entry(e: dict) -> str:
    return f"{e.get('year','')}{e.get('district_or_exam','')}{e.get('paper_type','')}"


def normalize_suite_row(row: dict, source_paths: dict[str, str]) -> dict:
    row = dict(row)
    if not row.get("year"):
        ids = (row.get("question_source_ids") or "").split(";")
        paths = [source_paths.get(i, "") for i in ids]
        if any("/2024模拟题/" in p for p in paths):
            row["year"] = "2024"
    if row.get("year") and not row["suite_id"].startswith(row["year"]):
        row["suite_id"] = row["year"] + row["district_or_exam"]
    return row


def update_coverage(entries: list[dict]) -> list[dict]:
    source_paths: dict[str, str] = {}
    with (CONTROL_DIR / "SOURCE_LEDGER.csv").open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            source_paths[row["source_id"]] = row["path"]

    count = defaultdict(int)
    pending = defaultdict(int)
    for e in entries:
        sid = suite_id_for_entry(e)
        count[sid] += 1
        if e.get("pending_reason"):
            pending[sid] += 1

    rows: list[dict] = []
    with (CONTROL_DIR / "COVERAGE_MATRIX.csv").open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        for row in reader:
            row = normalize_suite_row(row, source_paths)
            sid = row["suite_id"]
            row["legal_subjective_count"] = str(count.get(sid, 0))
            row["pending_confirm_count"] = str(pending.get(sid, 0))
            if count.get(sid, 0):
                row["status"] = "has_xuanbier"
            elif row["status"] == "has_xuanbier":
                row["status"] = "no_xuanbier_after_subquestion_review"
            elif row["status"] == "no_xuanbier_or_not_selected_initial":
                row["status"] = "no_xuanbier"
            rows.append(row)

    with (CONTROL_DIR / "COVERAGE_MATRIX.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    return rows


def status_label(status: str) -> str:
    if status == "has_xuanbier":
        return "是"
    if status.startswith("no_xuanbier"):
        return "否"
    return status


def write_md(entries: list[dict], coverage: list[dict]) -> None:
    lines: list[str] = ["# 选必二法律与生活_习题汇编_2024-2026", "", "## 覆盖清单", ""]
    lines += ["| 年份 | 区/统考 | 卷型 | 是否含选必二题 | 抽取设问数量 | 待确认 |", "| --- | --- | --- | --- | ---: | ---: |"]
    for row in coverage:
        lines.append(
            f"| {row.get('year','')} | {row.get('district_or_exam','')} | {row.get('paper_type','')} | {status_label(row.get('status',''))} | {row.get('legal_subjective_count','0')} | {row.get('pending_confirm_count','0')} |"
        )
    lines += ["", "## 题目汇编", ""]
    for e in entries:
        title = e["title"]
        if e.get("pending_reason") and "【待确认】" not in title:
            title += "【待确认】"
        lines += [
            f"### {title}",
            "【材料】",
            e["material"].strip(),
            "",
            "【设问】",
            e["prompt"].strip(),
            "",
            "【细则】",
            e["rubric"].strip(),
        ]
        if e.get("pending_reason"):
            lines += ["", f"【待确认理由】{e['pending_reason']}"]
        lines.append("")

    pending_entries = [e for e in entries if e.get("pending_reason")]
    lines += ["## 统计", "", f"总计设问数：{len(entries)}", "", "## 【待确认】条目清单", ""]
    if pending_entries:
        for e in pending_entries:
            lines.append(f"- {e['title']}：{e['pending_reason']}")
    else:
        lines.append("- 无")
    FINAL_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def update_rubric_ledger(entries: list[dict]) -> None:
    fields = ["entry_id", "title", "question_source_id", "rubric_source_id", "evidence_type", "pending_reason"]
    with (CONTROL_DIR / "RUBRIC_SEARCH_LEDGER.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for e in entries:
            writer.writerow({k: e.get(k, "") for k in fields})


def main() -> None:
    base_entries = read_packets()
    transformed: list[dict] = []
    for e in base_entries:
        transformed.extend(transform_entry(e))
    transformed.extend(new_entries(base_entries[-1]))
    final_entries = renumber(transformed)
    write_packets(final_entries)
    coverage = update_coverage(final_entries)
    write_md(final_entries, coverage)
    update_rubric_ledger(final_entries)
    print(f"final_entries={len(final_entries)}")
    print(f"pending={sum(1 for e in final_entries if e.get('pending_reason'))}")
    print(f"wrote {FINAL_MD}")


if __name__ == "__main__":
    main()
