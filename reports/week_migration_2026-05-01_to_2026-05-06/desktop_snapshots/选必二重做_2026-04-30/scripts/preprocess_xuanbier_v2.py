#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import preprocess_xuanbier as old  # reuse raw-file extraction helpers only


BASE = Path("/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30")
RUN = BASE / "preprocess_v2_2026-05-03"
CACHE = RUN / "text_cache"

SOURCE_ROOTS = [
    Path("/Users/wanglifei/Desktop/2024模拟题"),
    Path("/Users/wanglifei/Desktop/2025模拟题"),
    Path("/Users/wanglifei/Desktop/2026模拟题"),
]

DISTRICTS = ["海淀", "西城", "东城", "朝阳", "丰台", "石景山", "门头沟", "房山", "顺义", "通州", "昌平", "延庆"]
SUPPORTED = {".pdf", ".docx", ".doc", ".rtf", ".pptx", ".txt", ".md"}
SKIP_PARTS = {"补充材料", "其他材料", "分题细则", "原目录壳"}

PRIVATE_LAW_TERMS = [
    "法律与生活", "选必二", "选修2", "选修二", "民法典", "民事", "合同", "要约", "承诺", "违约",
    "侵权", "赔偿", "消费者", "经营者", "知情权", "自主选择权", "公平交易权", "劳动合同", "劳动关系",
    "劳动仲裁", "用人单位", "知识产权", "著作权", "专利", "商标", "不正当竞争", "商业秘密", "人格权",
    "名誉权", "肖像权", "隐私权", "所有权", "物权", "债权", "质权", "相邻关系", "继承", "遗嘱",
    "遗赠扶养", "婚姻", "夫妻", "监护", "诉讼", "调解", "仲裁", "司法确认", "举证责任", "法院",
    "人民法院", "裁判", "判决", "民法",
]

NOISE_TERMS = [
    "政治与法治", "依法治国", "法治政府", "人大", "政协", "国家机关", "基层治理", "行政机关",
    "检察机关", "行政公益诉讼", "逻辑与思维", "哲学", "经济与社会", "当代国际政治与经济",
    "全球化", "全过程人民民主", "党的领导",
]

LEGAL_TASK_CUES = [
    "运用《法律与生活》", "运用法律与生活", "运用法律知识", "法律依据", "案件事实", "案情",
    "法院", "人民法院", "判决", "裁判", "诉至法院", "仲裁", "合同纠纷", "侵权", "违约",
    "不正当竞争", "遗赠扶养", "劳动争议", "民法典",
]


@dataclass
class SourceFile:
    path: Path
    role: str
    text: str = ""
    status: str = ""
    cache_path: Path | None = None


@dataclass
class Suite:
    suite_id: str
    year: str
    district: str
    stage: str
    name: str
    path: Path
    paper_files: list[SourceFile] = field(default_factory=list)
    rubric_files: list[SourceFile] = field(default_factory=list)
    support_files: list[SourceFile] = field(default_factory=list)
    status: str = "unscanned"
    notes: str = ""


def clean(text: str) -> str:
    text = text.replace("\u3000", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def short(text: str, limit: int) -> str:
    text = clean(text)
    return text if len(text) <= limit else text[:limit] + "……"


def score(text: str) -> int:
    return sum((text or "").count(term) for term in PRIVATE_LAW_TERMS)


def explicit_legal(text: str) -> bool:
    return bool(re.search(r"运用《?法律与生活》?", text or "")) or any(t in (text or "") for t in ["法律与生活", "选必二", "选修2", "选修二"])


def infer_year(path: Path) -> str:
    m = re.search(r"20\d{2}", str(path))
    return m.group(0) if m else "unknown"


def infer_district(name: str) -> str:
    return next((d for d in DISTRICTS if d in name), "unknown")


def infer_stage(name: str) -> str:
    for stage in ["期中", "期末", "二模", "一模"]:
        if stage in name:
            return stage
    return "unknown"


def suite_id(year: str, district: str, stage: str, idx: int) -> str:
    return f"{year}_{district}_{stage}_{idx:03d}"


def is_suite_dir(path: Path) -> bool:
    if path.name in SKIP_PARTS:
        return False
    if "分类" in path.name:
        return False
    if "已放弃" in path.parts:
        return False
    return (path / "试卷").is_dir() or (path / "细则").is_dir()


def discover_suites() -> list[Suite]:
    suites: list[Suite] = []
    seen: set[Path] = set()
    for root in SOURCE_ROOTS:
        if not root.exists():
            continue
        dirs = [root] + [p for p in root.rglob("*") if p.is_dir()]
        for path in sorted(dirs):
            if not is_suite_dir(path):
                continue
            if any(part in SKIP_PARTS for part in path.relative_to(root).parts[:-1]):
                continue
            resolved = path.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            name = path.name
            year = infer_year(path)
            district = infer_district(name)
            stage = infer_stage(name)
            suites.append(Suite(suite_id(year, district, stage, len(suites) + 1), year, district, stage, name, path))
    return suites


def iter_supported(root: Path) -> list[Path]:
    if not root.exists():
        return []
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.name.startswith(("~$", ".")):
            continue
        if path.suffix.lower() in SUPPORTED:
            files.append(path)
    return sorted(files)


def attach_files(suite: Suite) -> None:
    paper_root = suite.path / "试卷"
    for path in iter_supported(paper_root):
        rel = path.relative_to(paper_root).parts
        if "补充材料" in rel:
            suite.support_files.append(SourceFile(path, "paper_support"))
        else:
            suite.paper_files.append(SourceFile(path, "paper"))
    for path in iter_supported(suite.path / "细则"):
        suite.rubric_files.append(SourceFile(path, "rubric"))
    for path in iter_supported(suite.path / "其他材料"):
        suite.support_files.append(SourceFile(path, "support"))


def cache_name(path: Path) -> Path:
    key = hashlib.sha1(str(path).encode("utf-8")).hexdigest()[:16]
    return CACHE / f"{key}_{path.stem}.txt"


def extract_file(item: SourceFile) -> None:
    CACHE.mkdir(parents=True, exist_ok=True)
    cache = cache_name(item.path)
    item.cache_path = cache
    if cache.exists():
        raw = cache.read_text(encoding="utf-8", errors="ignore")
        item.status = raw.splitlines()[1].replace("status: ", "") if raw.startswith("source:") and len(raw.splitlines()) > 1 else "cached"
        item.text = raw.split("\n\n", 1)[1] if "\n\n" in raw else raw
        return
    text, status = old.extract_text(item.path)
    item.text = text
    item.status = status
    cache.write_text(f"source: {item.path}\nstatus: {status}\n\n{text}", encoding="utf-8")


def extract_suite(suite: Suite) -> None:
    for item in suite.paper_files + suite.rubric_files + suite.support_files:
        extract_file(item)


def marker_regex() -> re.Pattern[str]:
    return re.compile(r"(?<!\d)([1-9]|1[0-9]|2[0-2])\s*[\.．、]")


def question_blocks(text: str) -> dict[str, str]:
    text = flat(text)
    matches = []
    for m in marker_regex().finditer(text):
        # Do not treat decimal quantities such as "18.4千克" as question 18.
        after = text[m.end():m.end() + 1]
        if after.isdigit():
            continue
        matches.append(m)
    blocks: dict[str, str] = {}
    for idx, m in enumerate(matches):
        qno = m.group(1)
        if qno in blocks and len(blocks[qno]) > 120:
            continue
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        block = text[m.start():end]
        if len(block) >= 70:
            blocks[qno] = block
    return blocks


def option_labels(block: str) -> int:
    return len(set(re.findall(r"([ABCD])\s*[\.．、]", block)))


def stem(block: str) -> str:
    m = re.search(r"[ABCD]\s*[\.．、]|[①②③④]", block)
    return block[:m.start()] if m else block


def nonlegal_noise(block: str) -> bool:
    head = stem(block)
    if explicit_legal(block):
        return False
    if any(t in head for t in ["推理", "三段论", "辩证思维", "创新思维", "经济全球化"]):
        return True
    if any(t in head for t in NOISE_TERMS) and score(head) < 2:
        return True
    return False


def is_legal_choice(block: str) -> bool:
    if option_labels(block) < 2:
        return False
    if nonlegal_noise(block):
        return False
    head = stem(block)
    if explicit_legal(block):
        return True
    if score(head) >= 1 and score(block) >= 2:
        return True
    if any(t in head for t in ["法院", "诉至法院", "赔偿", "合同", "劳动", "消费者", "著作权", "继承"]):
        return True
    return False


def is_legal_subjective(block: str) -> bool:
    if nonlegal_noise(block):
        return False
    if explicit_legal(block):
        return True
    return score(block) >= 3 and any(cue in block for cue in LEGAL_TASK_CUES)


def paper_candidates(suite: Suite) -> dict[str, dict[str, str]]:
    merged = "\n".join(item.text for item in suite.paper_files)
    rows: dict[str, dict[str, str]] = {}
    for qno, block in question_blocks(merged).items():
        n = int(qno)
        if n <= 15 and is_legal_choice(block):
            rows[qno] = {"question_type": "choice", "question_text": short(block, 5000), "source_role": "paper"}
        elif n >= 16 and is_legal_subjective(block):
            rows[qno] = {"question_type": "subjective", "question_text": short(block, 9000), "source_role": "paper"}
    return rows


def rubric_blocks_for_file(item: SourceFile) -> dict[str, str]:
    return question_blocks(item.text)


def evidence_type(item: SourceFile) -> str:
    text = str(item.path)
    name = item.path.name
    if any(k in text for k in ["细则", "评标", "阅卷", "评分"]):
        return "formal_or_scoring_source"
    if "讲评" in name:
        return "support_lecture"
    if any(k in name for k in ["答案", "参考"]):
        return "reference_answer"
    return "unknown"


def find_rubric(qno: str, suite: Suite, qtype: str) -> tuple[str, str, str, str]:
    candidates: list[tuple[int, SourceFile, str, str]] = []
    for item in suite.rubric_files + suite.support_files:
        blocks = rubric_blocks_for_file(item)
        if qno not in blocks:
            continue
        block = blocks[qno]
        ev = evidence_type(item)
        priority = 0
        if ev == "formal_or_scoring_source":
            priority += 100
        elif ev == "support_lecture":
            priority += 60
        elif ev == "reference_answer":
            priority += 40
        if "【细则】" in block or "评分" in block or "层次" in block:
            priority += 20
        if qtype == "subjective" and is_legal_subjective(block):
            priority += 10
        if qtype == "choice" and (f"第{qno}题" in block or "解析" in block):
            priority += 10
        candidates.append((priority, item, block, ev))
    if candidates:
        priority, item, block, ev = sorted(candidates, key=lambda x: x[0], reverse=True)[0]
        return short(block, 6500), str(item.path), ev, f"exact_qno_block_priority_{priority}"
    return "", "", "missing", "no_exact_qno_block"


def answer_key_from_text(text: str) -> dict[str, str]:
    text = flat(text[:2600])
    key: dict[str, str] = {}
    for m in re.finditer(r"(?<!\d)([1-9]|1[0-5])\s*[\.．、:：]?\s*([ABCD])(?=\s|[0-9]|$)", text):
        key.setdefault(m.group(1), m.group(2))
    return key


def choice_answer(qno: str, suite: Suite, rubric_block: str) -> tuple[str, str]:
    for item in suite.rubric_files:
        key = answer_key_from_text(item.text)
        if qno in key:
            return key[qno], str(item.path)
    m = re.search(rf"(?:第\s*{qno}\s*题|{qno}\s*[\.．、]).{{0,220}}?([ABCD])\s*选项正确", rubric_block)
    if m:
        return m.group(1), "rubric_explanation"
    m = re.search(rf"(?:第\s*{qno}\s*题|{qno}\s*[\.．、]).{{0,120}}?答案[:：]?\s*([ABCD])", rubric_block)
    if m:
        return m.group(1), "rubric_explanation"
    return "", ""


def option_map(block: str) -> dict[str, str]:
    matches = list(re.finditer(r"([ABCD])\s*[\.．、]\s*", block))
    opts: dict[str, str] = {}
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else min(len(block), m.end() + 420)
        opts[m.group(1)] = short(block[m.end():end], 300)
    return opts


def scenario(block: str) -> str:
    s = stem(block)
    s = re.sub(r"^\s*\d+\s*[\.．、]\s*", "", s)
    return short(s, 140)


def mistake_hint(text: str) -> str:
    if re.search(r"一律|必然|直接|无需|都|均|只能|立即", text):
        return "条件说绝对或忽略法定前提"
    if any(k in text for k in ["仲裁", "诉讼", "调解", "司法确认", "行政复议"]):
        return "纠纷解决程序或法律效力错位"
    if any(k in text for k in ["劳动", "用人单位", "劳动合同"]):
        return "劳动关系或用人单位责任边界不准"
    if any(k in text for k in ["著作权", "专利", "商标", "商业秘密"]):
        return "知识产权类型或权利边界不准"
    if any(k in text for k in ["消费者", "经营者", "知情权", "自主选择权"]):
        return "消费者权利或经营者义务定位不准"
    if any(k in text for k in ["所有权", "物权", "质权", "相邻"]):
        return "物权变动或相邻权边界不准"
    if any(k in text for k in ["继承", "遗嘱", "遗赠扶养"]):
        return "继承规则或协议效力判断不准"
    return "主体、行为、权利义务或适用条件没有扣准"


def choice_student_text(block: str, answer: str) -> tuple[str, str]:
    opts = option_map(block)
    scene = scenario(block)
    if not answer or answer not in opts:
        return (
            f"在{scene}中，本题暂不写死答案，因为 v2 未从可靠答案表锁定客观答案；先保留题面，等待答案源核验。",
            "答案未锁定，暂不生成错项句。",
        )
    overview = f"在{scene}中，应选{answer}，核心判断是“{short(opts[answer], 120)}”；其他项主要错在没有同时扣准主体关系、行为事实和法律后果。"
    wrongs = []
    for label in ["A", "B", "C", "D"]:
        if label == answer or label not in opts:
            continue
        wrongs.append(f"{label}项不对在{mistake_hint(opts[label])}，因为“{short(opts[label], 90)}”与题面事实或法律规则不匹配。")
    return overview, "；".join(wrongs)


def complete_prompt(block: str) -> str:
    hits = re.findall(r"([^。！？；;]{0,120}(?:运用《?法律与生活》?|运用法律知识|结合材料)[^。！？；;]{0,180}[。！？；;]?)", block)
    return clean(hits[-1]) if hits else short(block[-260:], 260)


def suite_status(suite: Suite, candidates: dict[str, dict[str, str]]) -> tuple[str, str]:
    if "2026石景山期末" in str(suite.path):
        return "excluded", "用户规则排除：2026石景山期末无新可用细则时不纳入。"
    paper_text = "\n".join(item.text for item in suite.paper_files)
    rubric_text = "\n".join(item.text for item in suite.rubric_files + suite.support_files)
    if candidates:
        return "has_xuanbier", f"v2 严格题段锁定 {len(candidates)} 道候选。"
    if len(paper_text.strip()) < 120:
        return "uncertain", "试卷文本层不足，需 OCR/渲染复核。"
    if explicit_legal(rubric_text) or score(rubric_text) >= 5:
        return "uncertain", "题面未锁定候选，但细则/讲评中有法律信号，需人工复核是否 OCR 或切题失败。"
    if score(paper_text) >= 2:
        return "uncertain", "题面有零散私法/程序法信号，但未形成稳定题段。"
    return "no_xuanbier", "未见稳定《法律与生活》题段。"


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for row in rows:
            w.writerow({field: row.get(field, "") for field in fields})


def run() -> int:
    RUN.mkdir(parents=True, exist_ok=True)
    (RUN / "audit").mkdir(exist_ok=True)
    suites = discover_suites()
    source_rows: list[dict] = []
    index_rows: list[dict] = []
    subj_rows: list[dict] = []
    choice_rows: list[dict] = []
    missing: list[str] = []
    old_quarantine = [
        "# 旧预处理隔离说明",
        "",
        "本轮 v2 不读取旧 `LEGAL_QUESTION_INDEX.csv`、`SUBJECTIVE_PREPROCESS.csv`、`CHOICE_PREPROCESS.csv` 作为证据输入。",
        "",
        "隔离原因：",
        "",
        "- 旧表曾把 `2024海淀一模第19题` 误标为 `reference_answer`，本地实际有正式细则层次表。",
        "- 旧 `LEGAL_QUESTION_INDEX.csv` 中选择题的 `rubric_excerpt` 常串入同套主观题细则，不能作为逐题证据。",
        "- 旧 `rubric_position=自动匹配第X题上下文` 只是粗截段，不足以证明题面和细则严格配对。",
        "- 旧选择题错项句存在模板化推断，答案未锁定时不得生成实质错项判断。",
    ]
    (RUN / "OLD_PREPROCESS_QUARANTINE.md").write_text("\n".join(old_quarantine) + "\n", encoding="utf-8")

    for suite in suites:
        attach_files(suite)
        extract_suite(suite)
        candidates = paper_candidates(suite)
        suite.status, suite.notes = suite_status(suite, candidates)
        source_rows.append(
            {
                "suite_id": suite.suite_id,
                "year": suite.year,
                "district": suite.district,
                "stage": suite.stage,
                "suite_name": suite.name,
                "suite_path": str(suite.path),
                "paper_files": "\n".join(str(f.path) for f in suite.paper_files),
                "rubric_files": "\n".join(str(f.path) for f in suite.rubric_files),
                "support_files": "\n".join(str(f.path) for f in suite.support_files),
                "extraction_status": "; ".join(sorted(set(f.status for f in suite.paper_files + suite.rubric_files + suite.support_files))),
                "xuanbier_status": suite.status,
                "notes": suite.notes,
            }
        )
        if suite.status != "has_xuanbier":
            missing.append(f"- `{suite.name}` `{suite.status}`：{suite.notes} 路径：`{suite.path}`")
            continue
        for qno, data in sorted(candidates.items(), key=lambda kv: int(kv[0])):
            qtype = data["question_type"]
            rub_text, rub_file, ev, method = find_rubric(qno, suite, qtype)
            answer, answer_source = ("", "")
            overview, wrongs = ("", "")
            if qtype == "choice":
                answer, answer_source = choice_answer(qno, suite, rub_text)
                overview, wrongs = choice_student_text(data["question_text"], answer)
            if not rub_text:
                missing.append(f"- `{suite.year} {suite.district} {suite.stage} 第{qno}题`：题面已锁定，细则 exact qno block 未锁定。")
            index_rows.append(
                {
                    "suite_id": suite.suite_id,
                    "year": suite.year,
                    "district": suite.district,
                    "stage": suite.stage,
                    "suite_name": suite.name,
                    "question_no": qno,
                    "question_type": qtype,
                    "source_question_file": "\n".join(str(f.path) for f in suite.paper_files),
                    "question_source_role": data["source_role"],
                    "source_rubric_file": rub_file,
                    "evidence_type": ev,
                    "rubric_match_method": method,
                    "answer": answer,
                    "answer_source": answer_source,
                    "question_excerpt": short(data["question_text"], 1200),
                    "rubric_excerpt": short(rub_text, 1200),
                    "notes": "" if rub_text else "missing_exact_rubric_block",
                }
            )
            if qtype == "subjective":
                subj_rows.append(
                    {
                        "suite_id": suite.suite_id,
                        "year": suite.year,
                        "district": suite.district,
                        "stage": suite.stage,
                        "suite_name": suite.name,
                        "question_no": qno,
                        "question_material": short(data["question_text"], 5000),
                        "complete_prompt": complete_prompt(data["question_text"]),
                        "rubric_source": rub_file,
                        "rubric_match_method": method,
                        "evidence_type": ev,
                        "rubric_original_text": short(rub_text, 6500),
                        "notes": "" if ev != "missing" else "需回原细则/OCR 复核",
                    }
                )
            else:
                choice_rows.append(
                    {
                        "suite_id": suite.suite_id,
                        "year": suite.year,
                        "district": suite.district,
                        "stage": suite.stage,
                        "suite_name": suite.name,
                        "question_no": qno,
                        "answer": answer,
                        "answer_source": answer_source,
                        "overview_sentence": overview,
                        "wrong_option_sentences": wrongs,
                        "question_excerpt": short(data["question_text"], 1500),
                        "rubric_source": rub_file,
                        "notes": "" if answer else "答案未从可靠答案表或逐题解析锁定",
                    }
                )

    write_csv(RUN / "SOURCE_MATCH_LEDGER_V2.csv", source_rows, [
        "suite_id", "year", "district", "stage", "suite_name", "suite_path", "paper_files", "rubric_files",
        "support_files", "extraction_status", "xuanbier_status", "notes",
    ])
    write_csv(RUN / "LEGAL_QUESTION_INDEX_V2.csv", index_rows, [
        "suite_id", "year", "district", "stage", "suite_name", "question_no", "question_type",
        "source_question_file", "question_source_role", "source_rubric_file", "evidence_type",
        "rubric_match_method", "answer", "answer_source", "question_excerpt", "rubric_excerpt", "notes",
    ])
    write_csv(RUN / "SUBJECTIVE_SOURCE_PACKS_V2.csv", subj_rows, [
        "suite_id", "year", "district", "stage", "suite_name", "question_no", "question_material",
        "complete_prompt", "rubric_source", "rubric_match_method", "evidence_type", "rubric_original_text", "notes",
    ])
    write_csv(RUN / "CHOICE_LEGAL_KNOWLEDGE_V2.csv", choice_rows, [
        "suite_id", "year", "district", "stage", "suite_name", "question_no", "answer", "answer_source",
        "overview_sentence", "wrong_option_sentences", "question_excerpt", "rubric_source", "notes",
    ])

    no_count = sum(1 for r in source_rows if r["xuanbier_status"] == "no_xuanbier")
    uncertain_count = sum(1 for r in source_rows if r["xuanbier_status"] == "uncertain")
    evidence_counts: dict[str, int] = {}
    for row in index_rows:
        evidence_counts[row["evidence_type"]] = evidence_counts.get(row["evidence_type"], 0) + 1

    report = [
        "# 预处理 v2 质量报告",
        "",
        "状态：v2 已重新从原始三年模拟题目录与原始文件抽取文本生成；旧预处理仅隔离说明，不作为输入证据。",
        "",
        f"- 扫描套卷：{len(source_rows)}",
        f"- has_xuanbier：{sum(1 for r in source_rows if r['xuanbier_status'] == 'has_xuanbier')}",
        f"- no_xuanbier：{no_count}",
        f"- uncertain：{uncertain_count}",
        f"- 候选法律题：{len(index_rows)}",
        f"- 选择题：{len(choice_rows)}",
        f"- 主观题：{len(subj_rows)}",
        f"- 证据类型：{evidence_counts}",
        f"- 选择题答案未锁定：{sum(1 for r in choice_rows if r['notes'])}",
        "",
        "v2 硬规则：",
        "",
        "- 主观题只接受 exact question-number block，不再用 legal-rich fallback 冒充对应细则。",
        "- 选择题没有可靠答案表或逐题解析时，不生成实质错项判断。",
        "- `讲评`、`答案`、`细则/评标/阅卷` 分证据类型保存，不混成 formal。",
        "- 题面锁定与细则锁定分开；任一缺失都进入 missing/uncertain。",
        "",
        "## Missing / Uncertain",
        "",
        *(missing or ["暂无 missing/uncertain。"]),
    ]
    (RUN / "QUALITY_REPORT_V2.md").write_text("\n".join(report) + "\n", encoding="utf-8")

    progress = [
        "# 预处理 v2 进度",
        "",
        "- [x] 隔离旧预处理，不再把旧 CSV/MD 当证据输入。",
        "- [x] 从原始三年模拟题目录重新发现套卷与文件。",
        "- [x] 重新抽取文本并写入 v2 text_cache。",
        "- [x] 重新锁定题面候选、细则 exact qno block、选择题答案来源。",
        "- [x] 输出 v2 CSV 与质量报告。",
        "- [ ] 下一步人工/半自动复核 missing/uncertain 与答案未锁定选择题。",
    ]
    (RUN / "PROGRESS_V2.md").write_text("\n".join(progress) + "\n", encoding="utf-8")
    print(f"run_dir={RUN}")
    print(f"suites={len(source_rows)} questions={len(index_rows)} choice={len(choice_rows)} subjective={len(subj_rows)}")
    print(f"evidence={evidence_counts}")
    print(f"missing_or_uncertain={len(missing)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
