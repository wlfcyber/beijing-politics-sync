#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
import shutil
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]

IN_MATRIX = RUN_DIR / "00_control" / "COVERAGE_MATRIX.csv"
OUT_MATRIX = RUN_DIR / "04_module_classification" / "chaoyang_2026_identity_ocr_culture_patched_classification_matrix.csv"
OUT_COVERAGE = RUN_DIR / "00_control" / "CHAOYANG_2026_IDENTITY_OCR_CULTURE_PATCHED_COVERAGE_MATRIX.csv"
OUT_AUDIT = RUN_DIR / "05_reports" / "chaoyang_2026_identity_ocr_culture_patch_audit.csv"
OUT_BLOCKED = RUN_DIR / "05_reports" / "chaoyang_2026_identity_ocr_culture_patch_blocked_queue.csv"
OUT_REPORT = RUN_DIR / "05_reports" / "chaoyang_2026_identity_ocr_culture_patch_report.md"

SOURCE_INVENTORY = RUN_DIR / "01_source_inventory" / "source_inventory.csv"
SOURCE_LEDGER = RUN_DIR / "00_control" / "SOURCE_LEDGER.csv"
CACHE_MANIFEST = RUN_DIR / "02_text_cache" / "cache_manifest.csv"
QUESTION_CANDIDATES = RUN_DIR / "03_question_index" / "question_candidates.csv"
TEXT_DIR = RUN_DIR / "02_text_cache" / "texts"

CHAOYANG_OLD_SUITE = "2026_朝阳_期末"
CHAOYANG_MIDTERM_SUITE = "2026_朝阳_期中"
CHAOYANG_FINAL_SUITE = "2026_朝阳_期末"

CHAOYANG_MIDTERM_NEEDLE = "/2026朝阳期中/"
CHAOYANG_FINAL_NEEDLE = "/2026朝阳期末/"

CHAOYANG_FINAL_PAPER = "/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期末/试卷/试卷.pdf"
CHAOYANG_FINAL_RUBRIC = "/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期末/细则/细则.pdf"
CHAOYANG_PAPER_SHA = "e1a49527cb4c175f3de69c5cb429216b35938f336f1417fd9df9d955c3e98399"
CHAOYANG_RUBRIC_SHA = "487b2d15b3a3ac2b14567989edfb4195dd3f776437ec0853a7bd39a5a700859a"

CHAOYANG_PAPER_OCR = RUN_DIR / "02_text_cache" / "ocr_cache" / "2026_朝阳_期末_试卷" / "试卷.ocr.txt"
CHAOYANG_RUBRIC_OCR = RUN_DIR / "02_text_cache" / "ocr_cache" / "2026_朝阳_期末_细则" / "细则.ocr.txt"
CHAOYANG_PAPER_TEXT = TEXT_DIR / "e1a49527cb4c175f.txt"
CHAOYANG_RUBRIC_TEXT = TEXT_DIR / "487b2d15b3a3ac2b.txt"
CHAOYANG_PAPER_BACKUP = TEXT_DIR / "e1a49527cb4c175f.pre_chaoyang_2026_summary_backup.txt"
CHAOYANG_RUBRIC_BACKUP = TEXT_DIR / "487b2d15b3a3ac2b.pre_chaoyang_2026_summary_backup.txt"

TARGET_MODULES = {"B2_ECONOMICS", "B3_POLITICS_RULE_OF_LAW", "B4_CULTURE"}

SUITE_IDENTITY_SPLITS = [
    {
        "old_suite": "2025_海淀_期末",
        "new_suite": "2025_海淀_期中",
        "needle": "/2025海淀期中/",
        "stage": "期中",
        "district": "海淀",
    },
    {
        "old_suite": "2026_朝阳_期末",
        "new_suite": "2026_朝阳_期中",
        "needle": "/2026朝阳期中/",
        "stage": "期中",
        "district": "朝阳",
    },
]


def load_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader), list(reader.fieldnames or [])


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def text_contains(row: dict[str, str], needle: str) -> bool:
    haystack = " ".join(str(value) for value in row.values())
    return needle in haystack


def patch_suite_identity_file(path: Path) -> Counter:
    rows, fields = load_csv(path)
    stats: Counter = Counter()
    for row in rows:
        for item in SUITE_IDENTITY_SPLITS:
            if row.get("suite_id") == item["old_suite"] and text_contains(row, item["needle"]):
                row["suite_id"] = item["new_suite"]
                if "stage" in row:
                    row["stage"] = item["stage"]
                if "district" in row:
                    row["district"] = item["district"]
                stats[f"{path.name}:{item['old_suite']}->{item['new_suite']}"] += 1
                break
    write_csv(path, rows, fields)
    return stats


def copy_ocr(src: Path, dst: Path, backup: Path) -> int:
    if not src.exists():
        raise SystemExit(f"missing OCR file: {src}")
    if dst.exists() and not backup.exists() and dst.read_text(encoding="utf-8", errors="replace").strip() != src.read_text(encoding="utf-8", errors="replace").strip():
        shutil.copy2(dst, backup)
    shutil.copy2(src, dst)
    return dst.stat().st_size


def patch_cache_manifest() -> Counter:
    rows, fields = load_csv(CACHE_MANIFEST)
    stats = patch_suite_identity_file(CACHE_MANIFEST)
    rows, fields = load_csv(CACHE_MANIFEST)

    paper_size = copy_ocr(CHAOYANG_PAPER_OCR, CHAOYANG_PAPER_TEXT, CHAOYANG_PAPER_BACKUP)
    rubric_size = copy_ocr(CHAOYANG_RUBRIC_OCR, CHAOYANG_RUBRIC_TEXT, CHAOYANG_RUBRIC_BACKUP)

    found = set()
    for row in rows:
        if row.get("suite_id") != CHAOYANG_FINAL_SUITE:
            continue
        if row.get("file_path") == CHAOYANG_FINAL_PAPER or row.get("sha256") == CHAOYANG_PAPER_SHA:
            row["cache_hit"] = "no"
            row["extraction_status"] = "raw-extracted"
            row["char_count"] = str(paper_size)
            row["run_text_path"] = str(CHAOYANG_PAPER_TEXT)
            row["source_text_path"] = str(CHAOYANG_PAPER_OCR)
            row["error"] = "repaired_full_ocr_for_chaoyang_2026_final_identity_patch"
            found.add("paper")
            stats["cache_manifest:chaoyang_final_paper_ocr_repaired"] += 1
        elif row.get("file_path") == CHAOYANG_FINAL_RUBRIC or row.get("sha256") == CHAOYANG_RUBRIC_SHA:
            row["cache_hit"] = "no"
            row["extraction_status"] = "raw-extracted"
            row["char_count"] = str(rubric_size)
            row["run_text_path"] = str(CHAOYANG_RUBRIC_TEXT)
            row["source_text_path"] = str(CHAOYANG_RUBRIC_OCR)
            row["error"] = "repaired_full_ocr_for_chaoyang_2026_final_rubric_identity_patch"
            found.add("rubric")
            stats["cache_manifest:chaoyang_final_rubric_ocr_repaired"] += 1

    if "paper" not in found:
        rows.append(
            {
                "suite_id": CHAOYANG_FINAL_SUITE,
                "year": "2026",
                "district": "朝阳",
                "stage": "期末",
                "source_type": "paper",
                "file_path": CHAOYANG_FINAL_PAPER,
                "sha256": CHAOYANG_PAPER_SHA,
                "cache_hit": "no",
                "extraction_status": "raw-extracted",
                "char_count": str(paper_size),
                "run_text_path": str(CHAOYANG_PAPER_TEXT),
                "source_text_path": str(CHAOYANG_PAPER_OCR),
                "error": "added_missing_cache_manifest_row_for_chaoyang_2026_final_paper_ocr",
            }
        )
        stats["cache_manifest:chaoyang_final_paper_row_added"] += 1
    if "rubric" not in found:
        rows.append(
            {
                "suite_id": CHAOYANG_FINAL_SUITE,
                "year": "2026",
                "district": "朝阳",
                "stage": "期末",
                "source_type": "rubric",
                "file_path": CHAOYANG_FINAL_RUBRIC,
                "sha256": CHAOYANG_RUBRIC_SHA,
                "cache_hit": "no",
                "extraction_status": "raw-extracted",
                "char_count": str(rubric_size),
                "run_text_path": str(CHAOYANG_RUBRIC_TEXT),
                "source_text_path": str(CHAOYANG_RUBRIC_OCR),
                "error": "added_missing_cache_manifest_row_for_chaoyang_2026_final_rubric_ocr",
            }
        )
        stats["cache_manifest:chaoyang_final_rubric_row_added"] += 1

    write_csv(CACHE_MANIFEST, rows, fields)
    return stats


def compact(text: str, limit: int = 950) -> str:
    return re.sub(r"\s+", " ", text or "").strip()[:limit]


PAPER_SNIPPETS = {
    "1": "中国特色社会主义制度始终以中华优秀传统文化滋养，以中国社会的具体实际为依据，在马克思主义中国化时代化的进程中不断焕发新的生命力。",
    "2": "城市更新的北京实践：亮马河水岸共治与东四站站城融合，体现人民群众美好需求和经济社会生态协调发展。",
    "3": "道路积尘负荷走航监测系统通过车载传感器、激光扫描、图像识别、大数据算法，助力道路扬尘污染精准防控和高效治理。",
    "4": "清代画家蒋廷锡《瑞谷图轴》将瑞谷与鹌鹑巧妙融合，构成丰与安的双重祈愿，传递中华文化和谐、朴拙、自然的审美理念。",
    "5": "AI 幻觉指大语言模型编造看似合理的信息，忠实性幻觉可分为指令不一致、上下文不一致和逻辑不一致。",
    "6": "机器人大厨判断题：并非所有机器人厨师都具有人形外观；机器人厨师都内置云端菜谱或离线菜谱；既具备重量传感功能又拥有味觉模拟算法。",
    "7": "坚持全面从严治党，必须紧紧扭住责任制这个牛鼻子，责任落实是管党治党取得实效的关键。",
    "8": "十五五规划编制中，人大专题调研、政协专题议政、企业座谈、公众建言，彰显全过程人民民主。",
    "9": "全民普法教育与依法治理相融合，传承中华法律文化精华，进一步打牢社会治理的文化根基。",
    "10": "北京市物业管理条例规定小区共用设施设备归全体业主共有，物业公司需单独建账、定期公示。",
    "11": "虚拟数字人模型售卖侵权案，乙公司认为孙某售卖虚拟数字人甲模型侵害权益并诉至法院。",
    "12": "民间投资面临市场准入、权益保障、创新支撑、投融资支持不足等问题，要求进一步激发民间投资活力。",
    "13": "某地结合自身资源禀赋和产业基础，在农业领域探索新质生产力发展路径，包括物联网溯源、产学研合作。",
    "14": "金砖国家新开发银行作为新兴市场和发展中国家发起的多边开发机构，成为国际金融治理的新兴力量。",
    "15": "习近平在亚太经合组织领导人非正式会议上强调共建普惠包容的开放型亚太经济，推进普惠包容的经济全球化。",
    "16": "戏曲是中华文化的瑰宝，传统戏曲通过当代化用智慧，在保留戏曲精髓基础上赋予新的时代内涵，焕发新的生命力。",
    "17": "网络生态治理是网络强国建设的重要任务。党中央壮大网上主流价值、主流舆论、主流文化，持续开展净网清朗护苗等专项行动。",
    "18(1)": "网络直播营销中主播宣称手串为正宗小叶紫檀并承诺假一赔十，消费者发现材质不符后诉至法院。",
    "18(2)": "民法典第一千零二十五条与甲乙同学关于新闻报道、舆论监督承担侵权责任条件的推理。",
    "19": "海南自由贸易港启动全岛封关，实施一线放开、二线管住、岛内自由政策制度，助力构建新发展格局。",
    "20": "中国特色大国外交要更有作为：周边命运共同体、全球南方、多边贸易体制、维护国家主权安全发展利益。",
    "21": "四大优势是相互依存、协同赋能的有机整体，包括制度优势、超大规模市场优势、完整产业体系优势、丰富人才资源优势。",
}

RUBRIC_SNIPPETS = {
    "16": "传统戏曲焕发新的生命力，是中华优秀传统文化的传承与创新的统一；戏曲作为中华优秀传统文化的代表，体现中华文化源远流长、博大精深，增强文化自信和民族文化认同感，推动传统文化创造性转化、创新性发展。",
    "17": "坚持党的领导，牢牢掌握网络意识形态工作领导权；科学立法、严格执法监管、坚持人民至上、全民守法，持续加强网络生态治理。",
    "18(1)": "合同依法成立、合同合法生效、违反诚信原则履行合同义务、构成违约并承担违约责任，保护消费者合法权益。",
    "18(2)": "甲乙推理分析：必要条件、充分条件假言推理、肯定前件式、结合民法典第一千零二十五条说明推理是否正确。",
    "19": "海南自贸港政策制度：政府与市场联动、政策赋能与供给提质、区域协调发展与内外联通、消费潜力与供需平衡。",
    "20": "中国特色大国外交更有作为：和平与发展、多极化和全球南方、经济全球化与开放型世界经济、维护国家利益。",
    "21": "四大优势关系：整体与部分、系统优化；制度优势含党的全面领导、以人民为中心、社会主义市场经济；市场、产业、人才优势协同赋能。",
}


def append_chaoyang_question_candidates() -> Counter:
    rows, fields = load_csv(QUESTION_CANDIDATES)
    stats: Counter = Counter()
    before = len(rows)
    existing = {
        (row.get("suite_id"), row.get("question"), row.get("source_type"), row.get("file_path"))
        for row in rows
    }
    for question, snippet in PAPER_SNIPPETS.items():
        key = (CHAOYANG_FINAL_SUITE, question, "paper", CHAOYANG_FINAL_PAPER)
        if key in existing:
            continue
        qtype = "objective" if question.split("(", 1)[0].isdigit() and int(question.split("(", 1)[0]) <= 15 else "subjective"
        rows.append(
            {
                "suite_id": CHAOYANG_FINAL_SUITE,
                "year": "2026",
                "district": "朝阳",
                "stage": "期末",
                "question": question,
                "question_type": qtype,
                "source_type": "paper",
                "file_path": CHAOYANG_FINAL_PAPER,
                "sha256": CHAOYANG_PAPER_SHA,
                "run_text_path": str(CHAOYANG_PAPER_TEXT),
                "snippet": compact(snippet),
                "segment_char_count": str(len(snippet)),
            }
        )
        stats["question_candidates:chaoyang_final_paper_rows_added"] += 1
    for question, snippet in RUBRIC_SNIPPETS.items():
        key = (CHAOYANG_FINAL_SUITE, question, "rubric", CHAOYANG_FINAL_RUBRIC)
        if key in existing:
            continue
        rows.append(
            {
                "suite_id": CHAOYANG_FINAL_SUITE,
                "year": "2026",
                "district": "朝阳",
                "stage": "期末",
                "question": question,
                "question_type": "subjective",
                "source_type": "rubric",
                "file_path": CHAOYANG_FINAL_RUBRIC,
                "sha256": CHAOYANG_RUBRIC_SHA,
                "run_text_path": str(CHAOYANG_RUBRIC_TEXT),
                "snippet": compact(snippet),
                "segment_char_count": str(len(snippet)),
            }
        )
        stats["question_candidates:chaoyang_final_rubric_rows_added"] += 1
    write_csv(QUESTION_CANDIDATES, rows, fields)
    stats["question_candidates:rows_before"] = before
    stats["question_candidates:rows_after"] = len(rows)
    return stats


def split_evidence_source(value: str) -> str:
    parts = [part.strip() for part in (value or "").split("|")]
    kept = [part for part in parts if CHAOYANG_MIDTERM_NEEDLE in part or CHAOYANG_FINAL_NEEDLE not in part]
    return " | ".join(dict.fromkeys(part for part in kept if part))


def status_for(module: str) -> str:
    return "included" if module in TARGET_MODULES else "module-boundary-excluded"


def qtype_for(question: str) -> str:
    stem = question.split("#", 1)[0].split("(", 1)[0]
    return "objective" if stem.isdigit() and int(stem) <= 15 else "subjective"


def base_row(fields: list[str], *, question: str, module: str, granularity: str = "question", parent: str = "", source_kind: str = "paper") -> dict[str, str]:
    row = {field: "" for field in fields}
    evidence = str(CHAOYANG_RUBRIC_OCR) if source_kind == "rubric" else str(CHAOYANG_PAPER_OCR)
    source_types = "rubric_ocr|paper_ocr" if source_kind == "rubric" else "paper_ocr"
    row.update(
        {
            "suite_id": CHAOYANG_FINAL_SUITE,
            "year": "2026",
            "district": "朝阳",
            "stage": "期末",
            "question": question,
            "parent_question": parent,
            "row_granularity": granularity,
            "book_module": module,
            "question_type": qtype_for(parent or question),
            "evidence_source": evidence,
            "source_types": source_types,
            "status": status_for(module),
            "artifact_location": str(OUT_AUDIT.relative_to(RUN_DIR)),
            "next_action": "future_baodian_intake" if module in TARGET_MODULES else "exclude_from_three_target_lines",
            "integration_status": "chaoyang_2026_identity_ocr_culture_patch",
        }
    )
    return row


FINAL_ROWS = [
    ("1", "B1_EXCLUDED", "CHAOYANG_2026_FINAL_Q1_PARENT_AFTER_CULTURE", "中国特色社会主义制度,中华优秀传统文化滋养", "题干主问中国特色社会主义制度，父题余项按必修一边界关闭；题面文化滋养另抽 B4_CULTURE 组件。", "paper"),
    ("2", "B4_PHILOSOPHY_EXCLUDED", "CHAOYANG_2026_FINAL_Q2_PARENT_AFTER_B2", "城市更新,人民需求,系统观念,经济社会生态协调发展", "选择题同时含哲学系统观念和城市更新发展内容；B2 发展组件另抽，父题余项按哲学边界关闭。", "paper"),
    ("3", "B4_PHILOSOPHY_EXCLUDED", "CHAOYANG_2026_FINAL_Q3_TECH_RECOGNITION", "认识工具,大数据算法,改造客观世界", "道路积尘监测系统主要落在认识工具、技术实践与哲学边界。", "paper"),
    ("4", "B4_CULTURE", "CHAOYANG_2026_FINAL_Q4_RUIGU_CULTURE_AESTHETIC", "瑞谷图轴,中华文化,和谐朴拙自然,审美理念", "《瑞谷图轴》传递中华文化审美理念，整题进入 B4_CULTURE。", "paper"),
    ("5", "XB3_EXCLUDED", "CHAOYANG_2026_FINAL_Q5_AI_HALLUCINATION_LOGIC", "AI幻觉,矛盾律,逻辑不一致", "AI 幻觉与矛盾律/逻辑不一致，属于逻辑与思维边界。", "paper"),
    ("6", "XB3_EXCLUDED", "CHAOYANG_2026_FINAL_Q6_ROBOT_CHEF_LOGIC", "判断,必然为真,云端菜谱,味觉模拟算法", "判断推理题，属于逻辑与思维边界。", "paper"),
    ("7", "B3_POLITICS_RULE_OF_LAW", "CHAOYANG_2026_FINAL_Q7_PARTY_DISCIPLINE", "全面从严治党,责任制,管党治党", "全面从严治党和责任制，进入 B3。", "paper"),
    ("8", "B3_POLITICS_RULE_OF_LAW", "CHAOYANG_2026_FINAL_Q8_WHOLE_PROCESS_DEMOCRACY", "党的领导,人大,政协,全过程人民民主", "十五五规划征求意见过程体现 B3 人民民主制度。", "paper"),
    ("9", "B3_POLITICS_RULE_OF_LAW", "CHAOYANG_2026_FINAL_Q9_RULE_OF_LAW_EDUCATION", "全民普法,依法治国,法治国家,依法治理", "全民普法教育是全面依法治国和法治国家建设内容，整题进入 B3；中华法律文化精华另抽文化组件。", "paper"),
    ("10", "XB2_EXCLUDED", "CHAOYANG_2026_FINAL_Q10_PROPERTY_RIGHTS_LITIGATION", "物业管理条例,业主共有,诉讼,知情权", "物权和诉讼题，属于法律与生活边界。", "paper"),
    ("11", "XB2_EXCLUDED", "CHAOYANG_2026_FINAL_Q11_DIGITAL_PERSON_COPYRIGHT", "虚拟数字人,复制权,信息网络传播权,一审判决", "知识产权/诉讼题，属于法律与生活边界。", "paper"),
    ("12", "B2_ECONOMICS", "CHAOYANG_2026_FINAL_Q12_PRIVATE_INVESTMENT", "民间投资,市场准入,政策性金融工具,市场信用体系", "激发民间投资活力与市场体系建设，进入 B2。", "paper"),
    ("13", "B2_ECONOMICS", "CHAOYANG_2026_FINAL_Q13_NEW_QUALITY_PRODUCTIVE_FORCES", "新质生产力,创新驱动,产学研融合,农业", "因地制宜发展新质生产力，进入 B2。", "paper"),
    ("14", "XB1_EXCLUDED", "CHAOYANG_2026_FINAL_Q14_BRICS_BANK", "金砖国家,国际金融治理,全球治理", "国际组织与全球治理，属于当代国际政治与经济边界。", "paper"),
    ("15", "XB1_EXCLUDED", "CHAOYANG_2026_FINAL_Q15_APEC", "亚太经合组织,经济全球化,区域经济一体化", "APEC 和经济全球化，属于当代国际政治与经济边界。", "paper"),
    ("16", "B4_PHILOSOPHY_EXCLUDED", "CHAOYANG_2026_FINAL_Q16_PARENT_AFTER_CULTURE", "哲学与文化,传统戏曲,辩证否定,中华优秀传统文化", "设问为《哲学与文化》混合题；文化采分点另抽 B4_CULTURE，父题余项按哲学边界关闭。", "rubric"),
    ("17", "B3_POLITICS_RULE_OF_LAW", "CHAOYANG_2026_FINAL_Q17_NETWORK_GOVERNANCE", "党的领导,科学立法,严格执法,人民至上,全民守法", "细则明确政治与法治作答角度，进入 B3。", "rubric"),
    ("18(1)", "XB2_EXCLUDED", "CHAOYANG_2026_FINAL_Q18_1_CONTRACT", "合同成立,合同生效,违约责任,消费者权益", "第18(1)问为法律与生活合同/违约责任。", "rubric"),
    ("18(2)", "XB3_EXCLUDED", "CHAOYANG_2026_FINAL_Q18_2_LOGIC", "必要条件,充分条件假言推理,肯定前件式", "第18(2)问为逻辑与思维推理分析。", "rubric"),
    ("19", "B2_ECONOMICS", "CHAOYANG_2026_FINAL_Q19_HAINAN_FTP", "政府与市场,供给侧结构性改革,区域协调发展,消费潜力", "细则明确经济与社会四个采分角度，进入 B2。", "rubric"),
    ("20", "XB1_EXCLUDED", "CHAOYANG_2026_FINAL_Q20_CHINA_DIPLOMACY", "和平发展,多极化,经济全球化,国家利益", "中国特色大国外交，属于当代国际政治与经济边界。", "rubric"),
    ("21", "B4_PHILOSOPHY_EXCLUDED", "CHAOYANG_2026_FINAL_Q21_PARENT_AFTER_COMPONENTS", "系统优化,整体与部分,制度优势,市场优势,产业体系,人才优势", "综合运用题含哲学关系分析；B2 与 B3 目标采分点另抽组件，父题余项按哲学/综合边界关闭。", "rubric"),
]

FINAL_COMPONENTS = [
    ("1#B4_CULTURE_COMPONENT", "1", "culture_component", "B4_CULTURE", "CHAOYANG_2026_FINAL_Q1_B4C_COMPONENT_TRADITIONAL_CULTURE", "中华优秀传统文化滋养,文明治理传统", "题干明确中国特色社会主义制度以中华优秀传统文化滋养，作为题目中的文化部分抽离。", "paper"),
    ("2#B2_COMPONENT", "2", "target_component", "B2_ECONOMICS", "CHAOYANG_2026_FINAL_Q2_B2_COMPONENT_URBAN_RENEWAL", "城市更新,经济社会生态协调发展,城市生活圈", "题目中的城市更新、站城融合、经济社会生态协调发展可为必修二发展题源组件。", "paper"),
    ("9#B4_CULTURE_COMPONENT", "9", "culture_component", "B4_CULTURE", "CHAOYANG_2026_FINAL_Q9_B4C_COMPONENT_LEGAL_CULTURE", "中华法律文化精华,文化根基", "题干写全民普法传承中华法律文化精华并打牢社会治理文化根基，按题目中的文化部分抽离。", "paper"),
    ("16#B4_CULTURE_COMPONENT", "16", "culture_component", "B4_CULTURE", "CHAOYANG_2026_FINAL_Q16_B4C_COMPONENT_TRADITIONAL_OPERA", "中华优秀传统文化,文化功能,文化自信,创造性转化,创新性发展", "细则明确戏曲作为中华优秀传统文化代表、增强文化自信和民族文化认同、推动创造性转化创新性发展。", "rubric"),
    ("21#B2_COMPONENT", "21", "target_component", "B2_ECONOMICS", "CHAOYANG_2026_FINAL_Q21_B2_COMPONENT_MARKET_INDUSTRY_TALENT", "社会主义市场经济,超大规模市场,完整产业体系,人才优势,现代化经济体系", "第21题细则列出社会主义市场经济、市场优势、产业体系与人才优势等经济采分点，抽入 B2。", "rubric"),
    ("21#B3_COMPONENT", "21", "target_component", "B3_POLITICS_RULE_OF_LAW", "CHAOYANG_2026_FINAL_Q21_B3_COMPONENT_PARTY_PEOPLE", "党的全面领导,以人民为中心,制度优势", "第21题细则制度优势部分明确党的全面领导和以人民为中心，抽入 B3。", "rubric"),
]


def add_final_row(out_rows: list[dict[str, str]], audit_rows: list[dict[str, str]], fields: list[str], item: tuple[str, str, str, str, str, str]) -> None:
    question, module, rule_id, terms, basis, source_kind = item
    row = base_row(fields, question=question, module=module, source_kind=source_kind)
    row["decision_reason"] = json.dumps(
        {"rule_id": rule_id, "matched_terms": terms, "basis": basis, "source": str(OUT_AUDIT.relative_to(RUN_DIR))},
        ensure_ascii=False,
    )
    out_rows.append(row)
    audit_rows.append(
        {
            "operation": "rebuild_2026_chaoyang_final_row",
            "suite_id": CHAOYANG_FINAL_SUITE,
            "question": question,
            "parent_question": "",
            "row_granularity": "question" if "(" not in question else "subquestion",
            "book_module": module,
            "status": row["status"],
            "rule_id": rule_id,
            "matched_terms": terms,
            "basis": basis,
            "evidence_source": row["evidence_source"],
            "source_types": row["source_types"],
        }
    )


def add_component(out_rows: list[dict[str, str]], audit_rows: list[dict[str, str]], fields: list[str], item: tuple[str, str, str, str, str, str, str, str]) -> None:
    question, parent, granularity, module, rule_id, terms, basis, source_kind = item
    row = base_row(fields, question=question, parent=parent, granularity=granularity, module=module, source_kind=source_kind)
    row["next_action"] = "future_baodian_intake_culture_component" if module == "B4_CULTURE" else "future_baodian_intake_target_component"
    row["decision_reason"] = json.dumps(
        {
            "rule_id": rule_id,
            "matched_terms": terms,
            "basis": basis,
            "source": str(OUT_AUDIT.relative_to(RUN_DIR)),
            "user_rule": "题目和细则中的文化部分必须抽离；民族精神、中华优秀传统文化、文化自信等属于 B4_CULTURE。",
        },
        ensure_ascii=False,
    )
    out_rows.append(row)
    audit_rows.append(
        {
            "operation": "add_2026_chaoyang_final_component",
            "suite_id": CHAOYANG_FINAL_SUITE,
            "question": question,
            "parent_question": parent,
            "row_granularity": granularity,
            "book_module": module,
            "status": "included",
            "rule_id": rule_id,
            "matched_terms": terms,
            "basis": basis,
            "evidence_source": row["evidence_source"],
            "source_types": row["source_types"],
        }
    )


def is_chaoyang_patch_row(row: dict[str, str]) -> bool:
    return row.get("integration_status", "").startswith("chaoyang_2026_identity_ocr")


def is_chaoyang_contaminated_final_row(row: dict[str, str]) -> bool:
    if row.get("suite_id") != CHAOYANG_OLD_SUITE:
        return False
    evidence = row.get("evidence_source", "") + " " + row.get("artifact_location", "") + " " + row.get("decision_reason", "")
    return CHAOYANG_MIDTERM_NEEDLE in evidence and not is_chaoyang_patch_row(row)


def write_matrix() -> dict[str, object]:
    rows, fields = load_csv(IN_MATRIX)
    contaminated = [row for row in rows if is_chaoyang_contaminated_final_row(row)]
    out_rows = [
        row for row in rows
        if not is_chaoyang_contaminated_final_row(row)
        and not (row.get("suite_id") == CHAOYANG_MIDTERM_SUITE and row.get("integration_status") == "chaoyang_2026_identity_ocr_patch_midterm_split")
        and not (row.get("suite_id") == CHAOYANG_FINAL_SUITE and is_chaoyang_patch_row(row))
    ]
    audit_rows: list[dict[str, str]] = []

    existing_keys = {(row.get("suite_id"), row.get("question")) for row in out_rows}
    cloned_midterm = 0
    for old in contaminated:
        clone = dict(old)
        clone["suite_id"] = CHAOYANG_MIDTERM_SUITE
        clone["stage"] = "期中"
        clone["evidence_source"] = split_evidence_source(old.get("evidence_source", ""))
        clone["integration_status"] = "chaoyang_2026_identity_ocr_patch_midterm_split"
        clone["decision_reason"] = json.dumps(
            {
                "rule_id": "CHAOYANG_2026_MIDTERM_SPLIT_FROM_CONTAMINATED_SUITE",
                "basis": "原 2026_朝阳_期末 行实际来自 2026 朝阳期中源文件；拆回 2026_朝阳_期中。",
                "prior_suite_id": CHAOYANG_OLD_SUITE,
                "prior_decision_reason": old.get("decision_reason", ""),
            },
            ensure_ascii=False,
        )
        key = (clone.get("suite_id"), clone.get("question"))
        if key not in existing_keys:
            out_rows.append(clone)
            existing_keys.add(key)
            cloned_midterm += 1
        audit_rows.append(
            {
                "operation": "split_midterm_row_from_contaminated_suite",
                "suite_id": CHAOYANG_MIDTERM_SUITE,
                "question": clone.get("question", ""),
                "parent_question": clone.get("parent_question", ""),
                "row_granularity": clone.get("row_granularity", ""),
                "book_module": clone.get("book_module", ""),
                "status": clone.get("status", ""),
                "rule_id": "CHAOYANG_2026_MIDTERM_SPLIT_FROM_CONTAMINATED_SUITE",
                "matched_terms": "",
                "basis": "朝阳期中源文件从错误的 2026_朝阳_期末 suite_id 拆回 2026_朝阳_期中。",
                "evidence_source": clone.get("evidence_source", ""),
                "source_types": clone.get("source_types", ""),
            }
        )

    for item in FINAL_ROWS:
        add_final_row(out_rows, audit_rows, fields, item)
    for item in FINAL_COMPONENTS:
        add_component(out_rows, audit_rows, fields, item)

    dupes = [key for key, count in Counter((row["suite_id"], row["question"]) for row in out_rows).items() if count > 1]
    if dupes:
        raise SystemExit(f"duplicate keys after chaoyang patch: {dupes[:20]}")

    write_csv(OUT_MATRIX, out_rows, fields)
    write_csv(OUT_COVERAGE, out_rows, fields)
    write_csv(RUN_DIR / "00_control" / "COVERAGE_MATRIX.csv", out_rows, fields)
    write_csv(RUN_DIR / "04_module_classification" / "module_classification_matrix.csv", out_rows, fields)

    audit_fields = [
        "operation",
        "suite_id",
        "question",
        "parent_question",
        "row_granularity",
        "book_module",
        "status",
        "rule_id",
        "matched_terms",
        "basis",
        "evidence_source",
        "source_types",
    ]
    write_csv(OUT_AUDIT, audit_rows, audit_fields)
    write_csv(OUT_BLOCKED, [row for row in out_rows if row.get("status") == "blocked"], fields)

    status_counts = Counter(row["status"] for row in out_rows)
    included_counts = Counter(row["book_module"] for row in out_rows if row["status"] == "included")
    granularity_counts = Counter(row["row_granularity"] for row in out_rows)
    suite_counts = Counter(row["suite_id"] for row in out_rows if row["suite_id"] in {CHAOYANG_MIDTERM_SUITE, CHAOYANG_FINAL_SUITE})
    return {
        "rows": out_rows,
        "removed_contaminated": len(contaminated),
        "cloned_midterm": cloned_midterm,
        "status_counts": status_counts,
        "included_counts": included_counts,
        "granularity_counts": granularity_counts,
        "suite_counts": suite_counts,
    }


def main() -> int:
    identity_stats = Counter()
    identity_stats.update(patch_suite_identity_file(SOURCE_INVENTORY))
    identity_stats.update(patch_suite_identity_file(SOURCE_LEDGER))
    identity_stats.update(patch_suite_identity_file(QUESTION_CANDIDATES))
    identity_stats.update(patch_cache_manifest())
    identity_stats.update(append_chaoyang_question_candidates())
    matrix_stats = write_matrix()

    rows: list[dict[str, str]] = matrix_stats["rows"]
    report = f"""# 2026 朝阳期中/期末身份与 OCR 文化补丁报告

## Scope

- removed contaminated `2026_朝阳_期末` live rows: {matrix_stats['removed_contaminated']}
- rebuilt/split `2026_朝阳_期中` matrix rows from contaminated suite: {matrix_stats['cloned_midterm']}
- rebuilt actual `2026_朝阳_期末` rows: {matrix_stats['suite_counts'][CHAOYANG_FINAL_SUITE]}
- added actual 2026 朝阳期末 parent/subquestion rows: {len(FINAL_ROWS)}
- added actual 2026 朝阳期末 target/culture components: {len(FINAL_COMPONENTS)}
- full OCR paper text: `{CHAOYANG_PAPER_OCR.relative_to(RUN_DIR)}`
- full OCR rubric text: `{CHAOYANG_RUBRIC_OCR.relative_to(RUN_DIR)}`

## Source Identity Repairs

{json.dumps(dict(identity_stats), ensure_ascii=False, indent=2)}

## Matrix Counts

- rows: {len(rows)}
- status counts: {dict(matrix_stats['status_counts'])}
- included module counts: {dict(matrix_stats['included_counts'])}
- row granularity counts: {dict(matrix_stats['granularity_counts'])}
- blocked rows: {matrix_stats['status_counts'].get('blocked', 0)}
- duplicate `(suite_id, question)` keys: 0

## User Rule Applied

- 题目中的中华优秀传统文化滋养、中华法律文化精华、文化根基被抽为 B4_CULTURE 组件。
- 第16题细则中的中华优秀传统文化、文化自信、民族文化认同感、创造性转化和创新性发展被抽为 B4_CULTURE 组件。
- 第21题综合题不整题归入 B2/B3；只抽社会主义市场经济、市场/产业/人才优势为 B2 组件，抽党的全面领导、以人民为中心为 B3 组件。
- 父题余项继续按哲学、必修一、选必一、选必二、选必三边界关闭。

## Deliverables

- `{OUT_AUDIT.relative_to(RUN_DIR)}`
- `{OUT_MATRIX.relative_to(RUN_DIR)}`
- `{OUT_COVERAGE.relative_to(RUN_DIR)}`
- `{OUT_BLOCKED.relative_to(RUN_DIR)}`
"""
    OUT_REPORT.write_text(report, encoding="utf-8")
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
