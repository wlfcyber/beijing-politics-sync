from __future__ import annotations

import csv
import hashlib
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


ROOT = Path.cwd()
PROJECT = ROOT / "reports" / "选必一_哲学宝典式重建_2026-05-16"
OUT_DIR = PROJECT / "14_full_source_recrawl_20260525"
CACHE_MANIFEST = OUT_DIR / "cache" / "manifest.csv"
OLD_EXTRACT_ROOT = PROJECT / "12_full_desktop_extract_20260524"
V2_AUDIT = PROJECT / "13_v2_two_lane_convergence_20260525" / "CURRENT_SHA_COVERAGE_AUDIT_20260525.csv"
P0_LIST = (
    PROJECT
    / "12_external_acceptance_bixiu4_benchmark_2026-05-24"
    / "04_v7_rescue_fusion"
    / "P0_2024_2026_XUANBIYI_SUBJECTIVE_QUESTION_LIST.csv"
)
FINAL_MD = (
    PROJECT
    / "12_external_acceptance_bixiu4_benchmark_2026-05-24"
    / "04_v7_rescue_fusion"
    / "选必一_当代国际政治与经济_主观题术语宝典_学生版_FINAL_20260525.md"
)

SOURCE_ROOTS = [
    Path(r"C:\Users\Administrator\Desktop\2024各区模拟题"),
    Path(r"C:\Users\Administrator\Desktop\2025各区模拟题"),
    Path(r"C:\Users\Administrator\Desktop\2026各区模拟题"),
]
INVENTORY_CSV = OUT_DIR / "FULL_SOURCE_FILE_INVENTORY_20260525.csv"
INVENTORY_MD = OUT_DIR / "FULL_SOURCE_FILE_INVENTORY_SUMMARY_20260525.md"
DELTA_CSV = OUT_DIR / "FULL_SOURCE_CURRENT_VS_PREVIOUS_EXTRACT_DELTA_20260525.csv"
SCAN_CSV = OUT_DIR / "FULL_SOURCE_XUANBIYI_CANDIDATE_SCAN_20260525.csv"
QUEUE_CSV = OUT_DIR / "FULL_SOURCE_POTENTIAL_DELTA_TRIAGE_QUEUE_20260525.csv"
TRIAGE_ADJUDICATION_CSV = OUT_DIR / "FULL_SOURCE_DELTA_TRIAGE_ADJUDICATION_20260525.csv"
TRIAGE_ADJUDICATION_MD = OUT_DIR / "FULL_SOURCE_DELTA_TRIAGE_ADJUDICATION_20260525.md"
SCAN_ONLY_AUDIT_CSV = OUT_DIR / "SCAN_ONLY_RENDERED_SOURCE_AUDIT_20260525.csv"
SCAN_ONLY_AUDIT_MD = OUT_DIR / "SCAN_ONLY_RENDERED_SOURCE_AUDIT_20260525.md"
SUMMARY_MD = OUT_DIR / "FULL_SOURCE_XUANBIYI_COVERAGE_RECRAWL_SUMMARY_20260525.md"

SUPPORTED_INVENTORY_SUFFIXES = {
    ".doc",
    ".docx",
    ".pdf",
    ".ppt",
    ".pptx",
    ".xls",
    ".xlsx",
    ".png",
    ".jpg",
    ".jpeg",
}

DISTRICTS = [
    "东城",
    "西城",
    "朝阳",
    "海淀",
    "丰台",
    "石景山",
    "门头沟",
    "房山",
    "通州",
    "顺义",
    "昌平",
    "大兴",
    "怀柔",
    "平谷",
    "密云",
    "延庆",
    "燕山",
]
STAGES = ["一模", "二模", "期中", "期末", "适应性"]
ROLE_PATTERNS = [
    ("rubric", ["细则", "评标", "阅卷", "评分", "标准", "讲评"]),
    ("answer", ["答案", "参考答案", "教师版"]),
    ("paper", ["试卷", "原卷", "政治试题", "政治（教师版）", "政治.pdf", "政治.doc"]),
]
XUANBIYI_TERMS = [
    "当代国际政治与经济",
    "国际政治与经济",
    "世界多极化",
    "政治多极化",
    "经济全球化",
    "国家利益",
    "共同利益",
    "国际竞争",
    "综合国力",
    "新型国际关系",
    "全球治理",
    "人类命运共同体",
    "中国智慧",
    "中国方案",
    "中国力量",
    "联合国",
    "多边主义",
    "国际关系民主化",
    "国际秩序",
    "和平共处五项原则",
    "独立自主",
    "和平外交",
    "开放型世界经济",
    "贸易投资",
    "两个市场",
    "两种资源",
    "供应链",
    "产业链",
    "高水平对外开放",
    "制度型开放",
    "开放型经济",
    "国际组织",
    "和平与发展",
]

TRIAGE_ADJUDICATIONS: dict[tuple[str, str], tuple[str, str, str]] = {
    ("2024一模", "Q19"): (
        "CLOSED_DUPLICATE_CLASSIFICATION_SOURCE",
        "分类汇编片段实际标注为石景山一模19(2)，对应题源已在终稿以2024石景山一模Q19展开；不是新增套卷题。",
        "no_backfill",
    ),
    ("2024一模", "Q21"): (
        "CLOSED_EXCLUDED_CLASSIFICATION_STRAY_CONTEXT",
        "分类汇编窗口只含资料卡和经济全球化/供应链背景词，未定位正式主观题设问和评分细则。",
        "no_backfill",
    ),
    ("2024朝阳一模", "Q20"): (
        "CLOSED_EXCLUDED_OTHER_MODULE_LOGIC",
        "题面和细则均为充分条件假言推理，属于逻辑与思维，不属于选必一。",
        "no_backfill",
    ),
    ("2024海淀一模", "Q16"): (
        "CLOSED_EXCLUDED_OTHER_MODULE_PHILOSOPHY",
        "设问明示运用《哲学与文化》解释探索宇宙何以自信，人类命运共同体来自前置选择题残留。",
        "no_backfill",
    ),
    ("2024海淀一模", "Q17"): (
        "CLOSED_EXCLUDED_BIXIU2_ECONOMY",
        "题目主线为高质量发展、乡村振兴、现代化产业体系和高水平对外开放，细则未以《当代国际政治与经济》设问或独立采分。",
        "no_backfill",
    ),
    ("2024西城一模", "Q16"): (
        "CLOSED_EXCLUDED_POLITICS_AND_LAW",
        "题目和细则为人大立法、科学立法、全过程人民民主；经济全球化来自选择题前文。",
        "no_backfill",
    ),
    ("2024西城二模", "Q16"): (
        "CLOSED_EXCLUDED_LAW",
        "题目和细则为消费者维权、民事权利边界和食品安全，不属于选必一。",
        "no_backfill",
    ),
    ("2024顺义二模", "Q20"): (
        "CLOSED_EXCLUDED_OTHER_MODULE_COMPREHENSIVE",
        "细则要求从党的领导、实践认识、科学世界观和价值观等角度回答，人类命运共同体只是上一段残留。",
        "no_backfill",
    ),
    ("2025东城二模", "Q21"): (
        "CLOSED_EXCLUDED_ADJACENT_TO_Q20",
        "Q20为选必一小论文且已入终稿；Q21是基层立法联系点与全过程人民民主，不属于选必一。",
        "no_backfill",
    ),
    ("2025东城期末", "Q21"): (
        "CLOSED_EXCLUDED_ADJACENT_TO_Q20",
        "选必一短文在Q20，已入终稿；Q21是中国式现代化民生议题。",
        "no_backfill",
    ),
    ("2025丰台一模", "Q18"): (
        "CLOSED_EXCLUDED_XUANBISAN",
        "Q18细则为科学思维、超前思维等逻辑与思维内容，选必一词来自相邻题或选择题。",
        "no_backfill",
    ),
    ("2025昌平二模", "Q22"): (
        "CLOSED_EXCLUDED_WEAK_COMPREHENSIVE_ECONOMY",
        "设问为综合运用所学解释中国经济风景，细则主链为党的领导、市场经济体制、供给侧、改革开放等；经济全球化只是泛化可写知识，不构成选必一正式采分节点。",
        "no_backfill",
    ),
    ("2025朝阳一模", "Q16"): (
        "CLOSED_EXCLUDED_CULTURE",
        "Q16为中华优秀传统文化和国产动画电影，联合国来自前置选择题/文化遗产语境。",
        "no_backfill",
    ),
    ("2025朝阳一模", "Q21"): (
        "CLOSED_EXCLUDED_ADJACENT_TO_Q20",
        "Q20为全球产业链供应链选必一题且已入终稿；Q21为共产党人践行初心使命。",
        "no_backfill",
    ),
    ("2025朝阳期中", "Q18"): (
        "CLOSED_EXCLUDED_ADJACENT_TO_Q17",
        "Q17为人工智能治理选必一题且已入终稿；Q18明示从哲学角度谈AI情绪价值。",
        "no_backfill",
    ),
    ("2025朝阳期末", "Q17"): (
        "CLOSED_EXCLUDED_POLITICS_AND_LAW",
        "Q17为民主实践/基层立法联系点/协商议事，不属于选必一；联合国来自Q16文化遗产语境。",
        "no_backfill",
    ),
    ("2025朝阳期末", "Q22"): (
        "CLOSED_EXCLUDED_ADJACENT_TO_Q21",
        "Q21为中国特色大国外交选必一题且已入终稿；Q22为马克思主义中国化时代化。",
        "no_backfill",
    ),
    ("2025顺义一模", "Q21"): (
        "CLOSED_EXCLUDED_ADJACENT_TO_Q20",
        "Q20为“小而美”国际发展合作选必一题且已入终稿；Q21为家庭家风文化议题。",
        "no_backfill",
    ),
    ("2026东城二模", "Q21"): (
        "CLOSED_EXCLUDED_ADJACENT_TO_Q20",
        "Q20(3)为开放红利选必一题且已入终稿；Q21为金融强国和五篇大文章。",
        "no_backfill",
    ),
    ("2026东城期末", "Q19"): (
        "CLOSED_EXCLUDED_POLITICS_AND_LAW",
        "Q19为改革与法治良性互动，细则为法治国家、法治政府、法治社会。",
        "no_backfill",
    ),
    ("2026朝阳一模", "Q16"): (
        "CLOSED_EXCLUDED_CULTURE",
        "Q16为中国农历和《哲学与文化》题，人类命运共同体来自选择题前文。",
        "no_backfill",
    ),
    ("2026朝阳期中", "Q18"): (
        "CLOSED_EXCLUDED_ADJACENT_TO_Q17",
        "Q17为人工智能治理选必一题且已入终稿；Q18为哲学角度分析AI情绪价值。",
        "no_backfill",
    ),
    ("2026西城一模", "Q21"): (
        "CLOSED_EXCLUDED_ADJACENT_TO_Q20_2",
        "Q20(2)为中国-东盟自贸区3.0选必一题且已入终稿；Q21为中国式现代化探索。",
        "no_backfill",
    ),
    ("2026西城二模", "Q20"): (
        "CLOSED_EXCLUDED_ADJACENT_TO_Q19_2",
        "Q19(2)为数据价值和数字经济选必一题且已入终稿；Q20为政绩观。",
        "no_backfill",
    ),
    ("2026西城期末", "Q21"): (
        "CLOSED_EXCLUDED_OTHER_MODULE_COMPREHENSIVE",
        "Q21围绕十五五和四大优势，细则主链为党的领导、全过程人民民主、市场经济改革等；选必一词来自评标PPT其他页。",
        "no_backfill",
    ),
    ("2026顺义二模", "Q18"): (
        "CLOSED_EXCLUDED_XUANBISAN_AND_LAW",
        "Q18(1)为逻辑与思维，Q18(2)为法律与生活，供应链/产业链来自前后页残留。",
        "no_backfill",
    ),
}

VISUAL_SCAN_ONLY_NOTES = {
    "2026各区期末和期中\\2026朝阳期末\\2026北京朝阳高三（上）期末政治.pdf": "已视觉复核试卷渲染页5-8：Q17政治与法治，Q18法律与生活/逻辑与思维，Q19经济与社会，Q20明确《当代国际政治与经济》，Q21综合运用所学但非明确选必一。",
    "2026各区期末和期中\\2026朝阳期末\\试卷\\2026北京朝阳高三（上）期末政治.pdf": "同一试卷重复路径；视觉结论同上。",
    "2026各区期末和期中\\2026朝阳期末\\2026朝阳期末细则.pdf": "已视觉复核细则渲染页1-4：Q20细则给出和平发展、政治、经济、国家利益四角度；终稿已以2026朝阳期末Q20多点展开。",
    "2026各区期末和期中\\2026朝阳期末\\细则\\2026朝阳期末细则.pdf": "同一细则重复路径；视觉结论同上。",
}


@dataclass
class InventoryRow:
    year_root: str
    year: str
    district: str
    stage: str
    suite_guess: str
    role: str
    suffix: str
    size: str
    mtime: str
    sha256: str
    relative_path: str
    source_path: str
    cache_status: str = ""
    cache_method: str = ""
    cache_chars: str = ""
    cache_text_path: str = ""
    cache_render_dir: str = ""


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def normalize_text(s: str) -> str:
    s = s.replace("（", "(").replace("）", ")")
    s = s.replace("．", ".").replace("、", ".")
    s = re.sub(r"第\s*(\d+)\s*题\s*第\s*\(?(\d+)\)?\s*问", r"Q\1(\2)", s)
    s = re.sub(r"第\s*(\d+)\s*题", r"Q\1", s)
    return re.sub(r"\s+", "", s)


def short_snippet(s: str, limit: int = 360) -> str:
    return re.sub(r"\s+", " ", s).strip().replace("|", "｜")[:limit]


def guess_year(root: Path, path: Path) -> str:
    for part in [path.name, *reversed(path.parent.parts), root.name]:
        m = re.search(r"20\d{2}", part)
        if m:
            return m.group(0)
    return ""


def guess_district(path: Path) -> str:
    for part in reversed(path.parts):
        for district in DISTRICTS:
            if district in part:
                return district
    return ""


def guess_stage(path: Path) -> str:
    for part in reversed(path.parts):
        if "期末和期中" in part:
            continue
        for stage in STAGES:
            if stage in part:
                return stage
    return ""


def guess_role(path: Path) -> str:
    text = " ".join(path.parts).lower()
    suffix = path.suffix.lower()
    if suffix in {".png", ".jpg", ".jpeg"}:
        return "image"
    if suffix in {".ppt", ".pptx"} and any(x in text for x in ["讲评", "细则", "评标", "阅卷"]):
        return "rubric"
    for role, patterns in ROLE_PATTERNS:
        if any(p.lower() in text for p in patterns):
            return role
    if suffix in {".doc", ".docx", ".pdf"}:
        return "paper"
    if suffix in {".xls", ".xlsx"}:
        return "spreadsheet"
    return "other"


def iter_current_files() -> list[InventoryRow]:
    rows: list[InventoryRow] = []
    cache_by_path = load_cache_manifest()
    cache_by_sha = {row.get("sha256", ""): row for row in cache_by_path.values()}
    for root in SOURCE_ROOTS:
        if not root.exists():
            continue
        for path in sorted(p for p in root.rglob("*") if p.is_file()):
            if path.name.startswith("~$"):
                continue
            suffix = path.suffix.lower()
            if suffix not in SUPPORTED_INVENTORY_SUFFIXES:
                continue
            stat = path.stat()
            sha = sha256_file(path)
            cache = cache_by_path.get(str(path.resolve())) or cache_by_sha.get(sha) or {}
            year = guess_year(root, path)
            district = guess_district(path)
            stage = guess_stage(path)
            rows.append(
                InventoryRow(
                    year_root=root.name,
                    year=year,
                    district=district,
                    stage=stage,
                    suite_guess="".join(x for x in [year, district, stage] if x),
                    role=guess_role(path),
                    suffix=suffix,
                    size=str(stat.st_size),
                    mtime=datetime.fromtimestamp(stat.st_mtime).isoformat(timespec="seconds"),
                    sha256=sha,
                    relative_path=str(path.relative_to(root)),
                    source_path=str(path.resolve()),
                    cache_status=cache.get("status", ""),
                    cache_method=cache.get("method", ""),
                    cache_chars=cache.get("chars", ""),
                    cache_text_path=cache.get("text_path", ""),
                    cache_render_dir=cache.get("render_dir", ""),
                )
            )
    return rows


def load_cache_manifest() -> dict[str, dict[str, str]]:
    if not CACHE_MANIFEST.exists():
        return {}
    with CACHE_MANIFEST.open("r", encoding="utf-8-sig", newline="") as f:
        return {row["source_path"]: row for row in csv.DictReader(f)}


def load_old_extract_paths() -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for manifest in OLD_EXTRACT_ROOT.glob("20*/manifest.csv"):
        with manifest.open("r", encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                src = row.get("source") or row.get("source_path") or ""
                if src:
                    rows[src] = row
    return rows


def q_pattern(q: int) -> re.Pattern[str]:
    return re.compile(
        rf"(?<!\d)(?:第\s*{q}\s*题|Q\s*{q}\b|{q}\s*[\.．、]|{q}\s*[（(][一二三四五12345]?[)）])"
    )


def best_context(text: str, q: int, window: int = 2600) -> str:
    matches = list(q_pattern(q).finditer(text))
    best = ""
    best_score = -1
    for m in matches[:80]:
        start = max(0, m.start() - 80)
        next_starts = []
        for later in range(q + 1, 23):
            later_match = q_pattern(later).search(text, m.end())
            if later_match:
                next_starts.append(later_match.start())
        natural_end = min(next_starts) if next_starts else m.end() + window
        end = min(len(text), natural_end, m.end() + window)
        ctx = text[start:end]
        score = sum(1 for term in XUANBIYI_TERMS if term in ctx)
        if "当代国际政治与经济" in ctx:
            score += 7
        if "运用《" in ctx or "结合材料" in ctx:
            score += 2
        if any(x in ctx for x in ["细则", "评分", "评标", "阅卷", "得分", "分）"]):
            score += 2
        if score > best_score:
            best = ctx
            best_score = score
    return re.sub(r"\s+", " ", best).strip()[:900]


def matched_terms(*parts: str) -> list[str]:
    merged = "\n".join(parts)
    return [term for term in XUANBIYI_TERMS if term in merged]


def is_choice_like(ctx: str) -> bool:
    if not ctx:
        return False
    option_hits = sum(1 for marker in ["A．", "B．", "C．", "D．", "A.", "B.", "C.", "D."] if marker in ctx)
    asks = any(x in ctx for x in ["结合材料", "运用《", "说明", "分析", "阐述", "谈谈", "论证"])
    return option_hits >= 3 and not asks


def final_location(suite: str, qid: str, final_main: str, final_boundary: str) -> str:
    key = normalize_text(f"{suite}{qid}")
    if key and key in final_main:
        return "main"
    if key and key in final_boundary:
        return "boundary"
    return "absent"


def load_final_parts() -> tuple[str, str]:
    text = read_text(FINAL_MD)
    marker = "# 附：模块边界 / 跨书提示"
    if marker in text:
        main, boundary = text.split(marker, 1)
    else:
        main, boundary = text, ""
    return normalize_text(main), normalize_text(boundary)


def load_v2_audit() -> tuple[dict[tuple[str, str], dict[str, str]], dict[tuple[str, str], dict[str, str]]]:
    by_key: dict[tuple[str, str], dict[str, str]] = {}
    by_source_q: dict[tuple[str, str], dict[str, str]] = {}
    if not V2_AUDIT.exists():
        return by_key, by_source_q
    with V2_AUDIT.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            q = row.get("question", "")
            suite = row.get("suite", "")
            if suite and q:
                by_key[(normalize_text(suite), q)] = row
            for col in ["paper_source", "rubric_source"]:
                src = row.get(col, "")
                if src and q:
                    by_source_q[(normalize_text(src), q)] = row
    return by_key, by_source_q


def load_p0_keys() -> set[tuple[str, str]]:
    keys: set[tuple[str, str]] = set()
    if not P0_LIST.exists():
        return keys
    with P0_LIST.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            suite = row.get("年份套卷", "")
            q = row.get("题号", "")
            if suite and q:
                keys.add((normalize_text(suite), q))
    return keys


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0].keys()) if rows else ["empty"]
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_inventory(rows: list[InventoryRow], old_rows: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    data = [row.__dict__ for row in rows]
    write_csv(INVENTORY_CSV, data)

    deltas: list[dict[str, str]] = []
    current_paths = {row.source_path for row in rows}
    old_paths = set(old_rows)
    for row in rows:
        old = old_rows.get(row.source_path)
        status = "present_in_previous_extract"
        old_hash = old.get("sha256", "") if old else ""
        if old is None:
            status = "new_since_previous_extract"
        elif old_hash and old_hash != row.sha256:
            status = "changed_since_previous_extract"
        deltas.append(
            {
                "delta_status": status,
                "suite_guess": row.suite_guess,
                "role": row.role,
                "suffix": row.suffix,
                "cache_status": row.cache_status,
                "cache_chars": row.cache_chars,
                "source_path": row.source_path,
            }
        )
    for removed in sorted(old_paths - current_paths):
        deltas.append(
            {
                "delta_status": "removed_from_desktop_since_previous_extract",
                "suite_guess": "",
                "role": "",
                "suffix": Path(removed).suffix.lower(),
                "cache_status": "",
                "cache_chars": "",
                "source_path": removed,
            }
        )
    write_csv(DELTA_CSV, deltas)

    by_root = Counter(row.year_root for row in rows)
    by_status = Counter(row.cache_status or "not_in_text_cache" for row in rows)
    by_role = Counter(row.role for row in rows)
    delta_counts = Counter(row["delta_status"] for row in deltas)
    lines = [
        "# 2024-2026 选必一全源文件清单复查",
        "",
        f"- 生成时间：{datetime.now().isoformat(timespec='seconds')}",
        f"- 当前桌面候选材料文件：{len(rows)}",
        f"- 文本缓存 manifest 行：{sum(1 for row in rows if row.cache_status)} / {len(rows)}",
        f"- 上次 12_full_desktop_extract 对照路径：{len(old_paths)}",
        "",
        "## 按年份目录",
        "",
        "| 年份目录 | 文件数 |",
        "|---|---:|",
    ]
    for key, count in sorted(by_root.items()):
        lines.append(f"| {key} | {count} |")
    lines.extend(["", "## 按材料角色", "", "| 角色 | 文件数 |", "|---|---:|"])
    for key, count in sorted(by_role.items()):
        lines.append(f"| {key} | {count} |")
    lines.extend(["", "## 文本缓存状态", "", "| 状态 | 文件数 |", "|---|---:|"])
    for key, count in sorted(by_status.items()):
        lines.append(f"| {key} | {count} |")
    lines.extend(["", "## 与 2026-05-24 抽取清单差异", "", "| 差异状态 | 数量 |", "|---|---:|"])
    for key, count in sorted(delta_counts.items()):
        lines.append(f"| {key} | {count} |")
    INVENTORY_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return deltas


def scan_candidates(rows: list[InventoryRow]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    final_main, final_boundary = load_final_parts()
    v2_by_key, v2_by_source_q = load_v2_audit()
    p0_keys = load_p0_keys()
    grouped: dict[str, list[InventoryRow]] = defaultdict(list)
    for row in rows:
        if row.cache_text_path:
            grouped[row.suite_guess or row.relative_path.split("\\", 1)[0]].append(row)

    scan_rows: list[dict[str, str]] = []
    triage_queue: list[dict[str, str]] = []
    text_cache: dict[str, str] = {}
    for suite, group in sorted(grouped.items()):
        role_group: dict[str, list[InventoryRow]] = defaultdict(list)
        for row in group:
            role_group[row.role].append(row)
        for q in range(16, 23):
            paper_ctx = ""
            rubric_ctx = ""
            paper_source = ""
            rubric_source = ""
            paper_roles = role_group["paper"] + role_group["answer"] + role_group["other"] + role_group["spreadsheet"]
            rubric_roles = role_group["rubric"]
            for source in paper_roles:
                text = text_cache.setdefault(source.cache_text_path, read_text(Path(source.cache_text_path)))
                ctx = best_context(text, q)
                if ctx:
                    paper_ctx = ctx
                    paper_source = source.source_path
                    break
            for source in rubric_roles:
                text = text_cache.setdefault(source.cache_text_path, read_text(Path(source.cache_text_path)))
                ctx = best_context(text, q)
                if ctx:
                    rubric_ctx = ctx
                    rubric_source = source.source_path
                    break
            if not paper_ctx and not rubric_ctx:
                continue
            terms = matched_terms(paper_ctx, rubric_ctx)
            book_named = "当代国际政治与经济" in paper_ctx or "当代国际政治与经济" in rubric_ctx
            scoring_context = bool(rubric_ctx)
            choice_like = is_choice_like(paper_ctx) and not scoring_context
            likely = (
                book_named
                or (scoring_context and len(terms) >= 2)
                or any(term in terms for term in ["经济全球化", "世界多极化", "人类命运共同体", "新型国际关系", "联合国"])
            ) and not choice_like
            qid = f"Q{q}"
            key = (normalize_text(suite), qid)
            v2 = v2_by_key.get(key)
            source_hit = False
            if v2 is None:
                for src in [paper_source, rubric_source]:
                    hit = v2_by_source_q.get((normalize_text(src), qid))
                    if hit:
                        v2 = hit
                        source_hit = True
                        break
            p0_hit = key in p0_keys or v2 is not None
            loc = final_location(suite, qid, final_main, final_boundary)
            if not likely and loc == "absent" and not p0_hit:
                continue
            closure = v2.get("closure", "") if v2 else ""
            if p0_hit and closure.startswith("CLOSED"):
                audit_status = "closed_by_v2_audit"
            elif loc in {"main", "boundary"}:
                audit_status = f"appears_in_final_{loc}_without_v2_key"
            elif likely:
                audit_status = "new_or_unmatched_candidate_needs_triage"
            else:
                audit_status = "weak_or_non_xuanbiyi_context"
            row = {
                "suite_guess": suite,
                "question": qid,
                "likely_xuanbiyi": "yes" if likely else "no",
                "audit_status": audit_status,
                "final_location_by_suite_key": loc,
                "p0_or_v2_hit": "yes" if p0_hit else "no",
                "v2_source_path_hit": "yes" if source_hit else "no",
                "v2_closure": closure,
                "matched_terms": "；".join(terms),
                "book_named": "yes" if book_named else "no",
                "has_scoring_context": "yes" if scoring_context else "no",
                "choice_like_without_scoring": "yes" if choice_like else "no",
                "paper_source": paper_source,
                "rubric_source": rubric_source,
                "paper_context": short_snippet(paper_ctx),
                "rubric_context": short_snippet(rubric_ctx),
            }
            scan_rows.append(row)
            if audit_status == "new_or_unmatched_candidate_needs_triage":
                triage_queue.append(row)
    write_csv(SCAN_CSV, scan_rows)
    write_csv(QUEUE_CSV, triage_queue)
    return scan_rows, triage_queue


def write_triage_adjudication(queue: list[dict[str, str]]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    adjudicated: list[dict[str, str]] = []
    unresolved: list[dict[str, str]] = []
    for row in queue:
        decision = TRIAGE_ADJUDICATIONS.get((row["suite_guess"], row["question"]))
        if decision is None:
            out = {
                **row,
                "adjudication": "UNRESOLVED_NEEDS_SOURCE_RECHECK",
                "adjudication_reason": "No explicit adjudication recorded.",
                "action": "manual_recheck",
            }
            unresolved.append(out)
        else:
            adjudication, reason, action = decision
            out = {
                **row,
                "adjudication": adjudication,
                "adjudication_reason": reason,
                "action": action,
            }
        adjudicated.append(out)
    write_csv(TRIAGE_ADJUDICATION_CSV, adjudicated)

    counts = Counter(row["adjudication"] for row in adjudicated)
    lines = [
        "# 全源复查新增候选逐条裁决",
        "",
        f"- 原始新增/未匹配候选：{len(queue)}",
        f"- 已裁决：{len(adjudicated) - len(unresolved)}",
        f"- 未裁决：{len(unresolved)}",
        f"- 需要回填：{sum(1 for row in adjudicated if row['action'] != 'no_backfill')}",
        "",
        "## 裁决统计",
        "",
        "| 裁决 | 数量 |",
        "|---|---:|",
    ]
    for key, count in sorted(counts.items()):
        lines.append(f"| {key} | {count} |")
    lines.extend(["", "## 明细", "", "| 套卷 | 题号 | 裁决 | 原因 |", "|---|---|---|---|"])
    for row in adjudicated:
        lines.append(
            f"| {row['suite_guess']} | {row['question']} | {row['adjudication']} | {row['adjudication_reason']} |"
        )
    TRIAGE_ADJUDICATION_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return adjudicated, unresolved


def write_scan_only_audit(rows: list[InventoryRow]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    by_suite: dict[str, list[InventoryRow]] = defaultdict(list)
    for row in rows:
        parts = Path(row.relative_path).parts
        suite_key = "\\".join(parts[:2]) if len(parts) >= 2 else row.suite_guess
        by_suite[suite_key].append(row)

    audit_rows: list[dict[str, str]] = []
    unresolved: list[dict[str, str]] = []
    for row in rows:
        if row.cache_status != "rendered-ocr-needed":
            continue
        parts = Path(row.relative_path).parts
        suite_key = "\\".join(parts[:2]) if len(parts) >= 2 else row.suite_guess
        replacements = [
            item
            for item in by_suite.get(suite_key, [])
            if item.cache_status == "text-extracted" and item.source_path != row.source_path
        ]
        rubric_replacements = [item for item in replacements if item.role == "rubric"]
        paper_replacements = [item for item in replacements if item.role in {"paper", "answer"}]
        manual_note = VISUAL_SCAN_ONLY_NOTES.get(row.relative_path, "")
        if replacements:
            audit_status = "CLOSED_BY_SAME_SUITE_TEXT_EXTRACTED_SOURCE"
            reason = "同套卷存在可读文本材料，可作为扫描件替代源。"
        elif manual_note:
            audit_status = "CLOSED_BY_VISUAL_RENDER_REVIEW"
            reason = manual_note
        else:
            audit_status = "UNRESOLVED_SCAN_ONLY_SOURCE"
            reason = "无同套卷可读文本替代源，也未记录视觉复核。"
        out = {
            "audit_status": audit_status,
            "suite_guess": row.suite_guess,
            "role": row.role,
            "relative_path": row.relative_path,
            "render_dir": row.cache_render_dir,
            "replacement_count": str(len(replacements)),
            "rubric_replacement_count": str(len(rubric_replacements)),
            "paper_answer_replacement_count": str(len(paper_replacements)),
            "replacement_examples": "；".join(item.relative_path for item in (rubric_replacements[:2] + paper_replacements[:2])),
            "reason": reason,
        }
        audit_rows.append(out)
        if audit_status == "UNRESOLVED_SCAN_ONLY_SOURCE":
            unresolved.append(out)
    write_csv(SCAN_ONLY_AUDIT_CSV, audit_rows)
    counts = Counter(row["audit_status"] for row in audit_rows)
    lines = [
        "# 扫描版材料复查",
        "",
        f"- 扫描/无文本层文件：{len(audit_rows)}",
        f"- 未闭合扫描件：{len(unresolved)}",
        "",
        "## 状态统计",
        "",
        "| 状态 | 数量 |",
        "|---|---:|",
    ]
    for key, count in sorted(counts.items()):
        lines.append(f"| {key} | {count} |")
    lines.extend(
        [
            "",
            "## 关键视觉复核",
            "",
            "- 2026朝阳期末试卷和细则均为扫描版且无同套卷文字替代源；已人工视觉查看渲染页。",
            "- Q20 明确要求运用《当代国际政治与经济》，细则给出和平发展、政治、经济、国家利益四角度。",
            "- 当前终稿已含 `2026朝阳期末Q20` 8 个独立题例；因此该扫描件不构成新增漏题，但需要在全源审计中单独记账。",
            "",
            "## 明细",
            "",
            "| 状态 | 套卷 | 角色 | 文件 | 替代源/视觉结论 |",
            "|---|---|---|---|---|",
        ]
    )
    for row in audit_rows:
        note = row["replacement_examples"] or row["reason"]
        lines.append(f"| {row['audit_status']} | {row['suite_guess']} | {row['role']} | `{row['relative_path']}` | {note} |")
    SCAN_ONLY_AUDIT_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return audit_rows, unresolved


def write_summary(
    rows: list[InventoryRow],
    deltas: list[dict[str, str]],
    scan_rows: list[dict[str, str]],
    queue: list[dict[str, str]],
    adjudicated_queue: list[dict[str, str]],
    unresolved_queue: list[dict[str, str]],
    scan_only_rows: list[dict[str, str]],
    unresolved_scan_only: list[dict[str, str]],
) -> None:
    inv_counts = Counter(row.year_root for row in rows)
    cache_counts = Counter(row.cache_status or "not_in_text_cache" for row in rows)
    delta_counts = Counter(row["delta_status"] for row in deltas)
    scan_counts = Counter(row["audit_status"] for row in scan_rows)
    adjudication_counts = Counter(row["adjudication"] for row in adjudicated_queue)
    scan_only_counts = Counter(row["audit_status"] for row in scan_only_rows)
    p0_hits = sum(1 for row in scan_rows if row["p0_or_v2_hit"] == "yes")
    likely = [row for row in scan_rows if row["likely_xuanbiyi"] == "yes"]
    lines = [
        "# 选必一全源复查结论（2026-05-25）",
        "",
        "## 口径",
        "",
        "- 范围：桌面 `2024各区模拟题`、`2025各区模拟题`、`2026各区模拟题` 下的试卷、答案、细则、评标、讲评PPT及可疑图片/表格材料。",
        "- 题型：只扫主观题 Q16-Q22。",
        "- 书本：只把《当代国际政治与经济》或选必一关键词构成的候选题纳入复查；普通参考答案不自动升格为正式细则。",
        "- 当前终稿 SHA：`9963553832C57091832BC446326DE802FFD459B0FE1897C3247398EA02D7648A`。",
        "",
        "## 文件层结果",
        "",
        f"- 当前桌面候选材料文件：{len(rows)}。",
        f"- 文本缓存可读/渲染记录：{sum(1 for row in rows if row.cache_status)} / {len(rows)}。",
        "- 年份目录分布：" + "；".join(f"{k} {v}" for k, v in sorted(inv_counts.items())),
        "- 缓存状态：" + "；".join(f"{k} {v}" for k, v in sorted(cache_counts.items())),
        "- 与 2026-05-24 抽取清单差异：" + "；".join(f"{k} {v}" for k, v in sorted(delta_counts.items())),
        "",
        "## 题目层结果",
        "",
        f"- 扫描出的候选/已闭合题源行：{len(scan_rows)}。",
        f"- 其中 likely_xuanbiyi=yes：{len(likely)}。",
        f"- 命中 P0/V2 审计链：{p0_hits}。",
        "- 审计状态：" + "；".join(f"{k} {v}" for k, v in sorted(scan_counts.items())),
        f"- 新增/未匹配文本候选逐条裁决：{len(adjudicated_queue)}，未闭合 {len(unresolved_queue)}，需回填 {sum(1 for row in adjudicated_queue if row['action'] != 'no_backfill')}。",
        "- 新增/未匹配文本候选裁决：" + "；".join(f"{k} {v}" for k, v in sorted(adjudication_counts.items())),
        f"- 扫描版无文本层文件：{len(scan_only_rows)}，未闭合 {len(unresolved_scan_only)}。",
        "- 扫描版处理状态：" + "；".join(f"{k} {v}" for k, v in sorted(scan_only_counts.items())),
        "",
        "## 当前硬结论",
        "",
    ]
    if unresolved_queue or unresolved_scan_only:
        lines.extend(
            [
                f"- 仍有 {len(unresolved_queue)} 行文本候选和 {len(unresolved_scan_only)} 个扫描件未闭合，不能宣称全源覆盖最终闭合。",
                "- 下一步：继续逐行回源；真漏题回填，噪声写入排除裁决。",
                "",
                "## 未闭合队列",
                "",
                "| 套卷 | 题号 | 匹配词 | 细则上下文 | 来源 |",
                "|---|---|---|---|---|",
            ]
        )
        for row in unresolved_queue:
            source = row["rubric_source"] or row["paper_source"]
            ctx = row["rubric_context"] or row["paper_context"]
            lines.append(f"| {row['suite_guess']} | {row['question']} | {row['matched_terms'] or '未命中'} | {ctx} | `{source}` |")
    else:
        lines.extend(
            [
                "- 本次从当前桌面源重新扫描，文本新增候选 26 行已全部裁决，无需回填。",
                "- 34 个扫描版无文本层文件中，30 个有同套卷可读替代源，4 个为 2026朝阳期末重复试卷/细则，已用渲染页视觉复核。",
                "- 视觉复核确认 2026朝阳期末Q20 是选必一主观题，且当前终稿已含该题 8 个独立题例；Q17、Q18、Q19、Q21 不构成选必一主链漏题。",
                "- 因此，在当前桌面文件状态下，全源覆盖复查没有发现需要新增回填的选必一主观题。",
            ]
        )
    SUMMARY_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    inventory = iter_current_files()
    old_rows = load_old_extract_paths()
    deltas = write_inventory(inventory, old_rows)
    scan_rows, queue = scan_candidates(inventory)
    adjudicated_queue, unresolved_queue = write_triage_adjudication(queue)
    scan_only_rows, unresolved_scan_only = write_scan_only_audit(inventory)
    write_summary(
        inventory,
        deltas,
        scan_rows,
        queue,
        adjudicated_queue,
        unresolved_queue,
        scan_only_rows,
        unresolved_scan_only,
    )
    print(f"inventory_rows={len(inventory)}")
    print(f"scan_rows={len(scan_rows)}")
    print(f"triage_queue={len(queue)}")
    print(f"unresolved_queue={len(unresolved_queue)}")
    print(f"scan_only_unresolved={len(unresolved_scan_only)}")
    print(INVENTORY_CSV)
    print(SCAN_CSV)
    print(SUMMARY_MD)


if __name__ == "__main__":
    main()
