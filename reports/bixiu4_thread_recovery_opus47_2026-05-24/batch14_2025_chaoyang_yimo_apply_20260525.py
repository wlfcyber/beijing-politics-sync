from __future__ import annotations

import csv
import importlib.util
import json
import re
import shutil
import tempfile
import zipfile
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RECOVERY = ROOT / "reports" / "bixiu4_thread_recovery_opus47_2026-05-24"
RUN = ROOT / "reports" / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
ACCEPTED = RUN / "04_fusion_audit" / "student_patch_entries.accepted.jsonl"
LEDGER = DELIVERY / "docx_insert_ledger.csv"
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH14_2025_CHAOYANG_YIMO_CODEX_20260525.md"
SOURCE_TRANSCRIPTION = RECOVERY / "BATCH14_2025_CHAOYANG_YIMO_SOURCE_TRANSCRIPTION_20260525.md"
BASE_SCRIPT = RECOVERY / "batch13_2026_mentougou_yimo_apply_20260525.py"

SUITE = "2025朝阳一模"
YEAR = "2025"
STAGE = "一模"
SOURCE_BUNDLE = "01_source_inventory/suite_source_bundles/2025朝阳一模.md"
PAPER_PDF = "2025各区模拟题/2025各区一模/2025朝阳一模/试卷/2025北京朝阳高三一模政治（教师版）.pdf"
RULE_PDF = "2025各区模拟题/2025各区一模/2025朝阳一模/细则/2025朝阳一模细则.pdf"
RULE_RENDER_001 = "beijing_politics_research/data/preprocessed_corpus/renders/f5f683a900508fd2/page_001.png"
RULE_RENDER_002 = "beijing_politics_research/data/preprocessed_corpus/renders/f5f683a900508fd2/page_002.png"
RULE_RENDER_003 = "beijing_politics_research/data/preprocessed_corpus/renders/f5f683a900508fd2/page_003.png"
Q17_REVIEW = "2025各区模拟题/2025各区一模/2025朝阳一模/其他材料/20250329高3阅卷总结17 1题 具身智能 任会波组 阐释论证.doc"
Q18_REVIEW = "2025各区模拟题/2025各区一模/2025朝阳一模/其他材料/20250329高3阅卷总结18题 社区治理 汤桃玲组 探究建构.doc"
Q19_REVIEW = "2025各区模拟题/2025各区一模/2025朝阳一模/其他材料/20250329高3阅卷总结19题 合同欺诈  阐释论证.doc"

Q4_SOURCE = f"{SOURCE_BUNDLE}:552-562;818-853"
Q16_SOURCE = f"{SOURCE_BUNDLE}:688-704;855-856;{RULE_RENDER_001}"
Q21_SOURCE = f"{SOURCE_BUNDLE}:800-813;927-948;{RULE_RENDER_003}"
ANSWER_KEY_SOURCE = f"{SOURCE_BUNDLE}:818-853"

Q4_PROMPT = (
    "中文作为公共文化产品，题干列举汉语表达的若干选项。官方答案B："
    "“敌进我退，敌驻我扰，敌疲我打，敌退我追”把握了具体分析方法。"
)
Q16_PROMPT = "结合材料，运用《哲学与文化》知识，说明为什么国产动画电影能够让中华优秀传统文化在新时代绽放新光彩。"
Q21_PROMPT = "结合材料，综合运用所学，谈谈你对中国共产党人的“大事小事观”“为民办事观”“造福人民的政绩观”的理解。"

ENTRIES = [
    {
        "canonical_node": "矛盾的特殊性 / 具体问题具体分析",
        "question_no": "Q4",
        "heading_suffix": "2025朝阳一模 第4题（选择题）",
        "material_trigger": "题干B项写“敌进我退，敌驻我扰，敌疲我打，敌退我追”，官方答案为B。",
        "question_prompt": Q4_PROMPT,
        "why_trigger": "“敌进/敌驻/敌疲/敌退”分别对应“我退/我扰/我打/我追”，同一斗争对象在不同具体情境中采取不同策略，直接体现具体问题具体分析。",
        "answer_landing": "本题应选B。作答落点是矛盾具有特殊性，要坚持具体问题具体分析，根据敌情的具体变化采取相应战术，不能用同一种抽象办法处理所有情况。",
        "evidence_level": "选择题官方答案键+正确选项B",
        "source_lines": Q4_SOURCE,
    },
    {
        "canonical_node": "实践与认识（总）",
        "question_no": "Q16",
        "heading_suffix": "2025朝阳一模 第16题（主观题）",
        "material_trigger": "材料写《哪吒之魔童闹海》的关键戏份“历经特效团队九个月努力才完成”，创作团队依托视效技术精心雕琢并取得突破。",
        "question_prompt": Q16_PROMPT,
        "why_trigger": "国产动画让传统文化焕新，不是停留在观念表述中，而是在长期电影制作实践、技术打磨和传播实践中形成新的文化表达方式。",
        "answer_landing": "可写实践与认识的统一：创作团队在动画制作实践中深化对传统文化现代表达的认识，又把这种认识转化为电影画面、情节和人物塑造，推动优秀传统文化获得新的传播形态。",
        "evidence_level": "参考答案列实践+细则创作实践细化",
        "source_lines": Q16_SOURCE,
    },
    {
        "canonical_node": "实践是认识的基础",
        "question_no": "Q16",
        "heading_suffix": "2025朝阳一模 第16题（主观题）",
        "material_trigger": "材料写关键戏份历经九个月努力完成、依托现代视效技术精雕细节，参考答案列“实践”角度。",
        "question_prompt": Q16_PROMPT,
        "why_trigger": "“九个月努力”“精心雕琢”“取得突破性成果”呈现了创作实践推动认识深化和技术突破的过程。",
        "answer_landing": "实践是认识的基础和动力。国产动画的成功来自持续的艺术创作和技术攻关实践，这种实践推动创作者深化对传统文化、现代审美和动画表达方式的认识。",
        "evidence_level": "参考答案列实践+材料和细则创作实践支撑",
        "source_lines": Q16_SOURCE,
    },
    {
        "canonical_node": "辩证否定 / 守正创新",
        "question_no": "Q16",
        "heading_suffix": "2025朝阳一模 第16题（主观题）",
        "material_trigger": "细则第16题写国产动画重视文化传承、借助现代科技推动文化创新，将传统文化与现代传播方式结合。",
        "question_prompt": Q16_PROMPT,
        "why_trigger": "优秀传统文化“绽放新光彩”的关键，是既承载千年故事和文化符号，又借助现代视效技术、电影语言和现代传播方式实现创造性转化。",
        "answer_landing": "坚持辩证否定和守正创新：国产动画保留中华优秀传统文化的精神内核和故事资源，同时用现代技术、叙事和传播方式加以创新表达，使传统文化在新时代获得新的生命力。",
        "evidence_level": "评分细则原文明示文化传承与创新/创造性转化",
        "source_lines": Q16_SOURCE,
    },
    {
        "canonical_node": "尊重客观规律与发挥主观能动性相结合",
        "question_no": "Q16",
        "heading_suffix": "2025朝阳一模 第16题（主观题）",
        "material_trigger": "细则第16题写创作者团队把握社会提供的客观条件，把握个人与社会的统一，弘扬劳动精神、工匠精神、创新精神。",
        "question_prompt": Q16_PROMPT,
        "why_trigger": "导演的话把“好时代”和“心无旁骛投入创作”并列，说明成功既依托经济社会发展、市场空间等客观条件，也离不开创作主体长期投入和能动创造。",
        "answer_landing": "要把尊重客观条件和发挥主观能动性统一起来：国产动画立足新时代经济社会发展、技术条件和人民需求，又通过创作者的劳动、工匠精神和创新精神把条件转化为优秀作品。",
        "evidence_level": "评分细则原文明示客观条件+主观创造",
        "source_lines": Q16_SOURCE,
    },
    {
        "canonical_node": "整体与部分",
        "question_no": "Q16",
        "heading_suffix": "2025朝阳一模 第16题（主观题）",
        "material_trigger": "细则第16题写创作者团队“以局部推动整体”，推动中华优秀传统文化以新形式展现、绽放新光彩。",
        "question_prompt": Q16_PROMPT,
        "why_trigger": "一个创作团队、一部作品、一处关键戏份都不是孤立的；局部的技术突破和内容创新会影响国产动画行业和中华优秀传统文化传播的整体效果。",
        "answer_landing": "部分影响整体，关键部分的功能及其变化甚至会对整体功能起重要作用。国产动画创作团队通过关键戏份打磨和作品创新，以具体作品这一局部带动传统文化整体传播力、影响力提升。",
        "evidence_level": "评分细则原文明示以局部推动整体",
        "source_lines": Q16_SOURCE,
    },
    {
        "canonical_node": "社会存在与社会意识",
        "question_no": "Q16",
        "heading_suffix": "2025朝阳一模 第16题（主观题）",
        "material_trigger": "材料和细则都指向经济社会发展、人民群众艺术生活需求、市场空间和产业平台为国产动画提供条件。",
        "question_prompt": Q16_PROMPT,
        "why_trigger": "导演把作品成功归因于“随着中国经济社会的发展”“人民群众的艺术生活需求达到一定阶段”“好时代”，这是社会存在决定社会意识的链条。",
        "answer_landing": "社会存在决定社会意识。经济社会发展、人民群众艺术生活需求和市场空间，为国产动画承载、传播优秀传统文化提供现实基础，并促成相应文化作品繁荣。",
        "evidence_level": "评分细则原文明示立足国情/满足人民需要+参考答案列社会存在社会意识",
        "source_lines": Q16_SOURCE,
    },
    {
        "canonical_node": "实现人生价值",
        "question_no": "Q16",
        "heading_suffix": "2025朝阳一模 第16题（主观题）",
        "material_trigger": "材料写创作者遇上好时代、心无旁骛投入创作并最终得到相应回报；细则写把握个人与社会的统一、弘扬劳动精神、实现人生价值。",
        "question_prompt": Q16_PROMPT,
        "why_trigger": "创作者在社会提供的条件中，通过长期劳动、工匠精神和创新精神把个人追求同传统文化传承传播结合起来。",
        "answer_landing": "人生价值要在个人与社会的统一中创造和实现。创作者依托新时代条件，把个人创造性劳动投入中华优秀传统文化的现代表达，在创造社会价值中实现自我价值。",
        "evidence_level": "评分细则原文明示个人与社会统一/实现人生价值",
        "source_lines": Q16_SOURCE,
    },
    {
        "canonical_node": "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一",
        "question_no": "Q21",
        "heading_suffix": "2025朝阳一模 第21题（主观题）",
        "material_trigger": "细则第21题“为什么”部分写坚持实事求是、求真务实；材料列举破解“来回跑”、缓解“看病贵”、化解“落户难”等具体民生难题。",
        "question_prompt": Q21_PROMPT,
        "why_trigger": "“把实事办实、把难事办妥”不是口号，而是从群众真实困难出发，针对具体民生问题求真务实地解决。",
        "answer_landing": "坚持一切从实际出发、实事求是。党员干部要从人民群众最关心、最直接、最现实的利益问题出发，找准来回跑、看病贵、落户难等实际难题，求真务实解决问题。",
        "evidence_level": "评分细则原文明示实事求是/求真务实",
        "source_lines": Q21_SOURCE,
    },
    {
        "canonical_node": "人民群众",
        "question_no": "Q21",
        "heading_suffix": "2025朝阳一模 第21题（主观题）",
        "material_trigger": "材料反复出现“人民群众”“老百姓口碑”“把人民群众的小事当作我们的大事”；细则写尊重人民主体地位，坚持群众观点和群众路线。",
        "question_prompt": Q21_PROMPT,
        "why_trigger": "三种观念的共同指向是党同人民群众的关系：人民群众是工作的出发点、服务对象和评价主体。",
        "answer_landing": "人民群众是社会历史的主体，要坚持群众观点和群众路线。中国共产党人把群众小事当大事、为群众办事做服务、以老百姓口碑评价政绩，体现尊重人民主体地位。",
        "evidence_level": "评分细则原文明示群众观+方法论",
        "source_lines": Q21_SOURCE,
    },
    {
        "canonical_node": "价值观的导向作用",
        "question_no": "Q21",
        "heading_suffix": "2025朝阳一模 第21题（主观题）",
        "material_trigger": "细则第21题写重视价值观导向作用，自觉站在最广大人民立场上；材料以造福人民的政绩观评价干部业绩。",
        "question_prompt": Q21_PROMPT,
        "why_trigger": "“大事小事观”“为民办事观”“造福人民的政绩观”本身就是党员干部看待群众、办事和评价政绩的价值导向。",
        "answer_landing": "价值观具有导向作用。党员干部树立以人民为中心的政绩观，才能把工作导向人民利益和民生难题，防止脱离群众、只看表面政绩。",
        "evidence_level": "评分细则原文明示价值观导向作用",
        "source_lines": Q21_SOURCE,
    },
    {
        "canonical_node": "价值判断与价值选择",
        "question_no": "Q21",
        "heading_suffix": "2025朝阳一模 第21题（主观题）",
        "material_trigger": "细则第21题写把人民群众利益作为最高价值标准；材料写抓住人民最关心最直接最现实的利益问题，把丰碑立在人民群众心中。",
        "question_prompt": Q21_PROMPT,
        "why_trigger": "政绩观回答“为谁工作、以什么标准评价工作”，本质是价值判断和价值选择问题，必须以人民利益为最高标准。",
        "answer_landing": "价值判断与价值选择必须自觉站在最广大人民的立场上。造福人民的政绩观要求把人民最关心最直接最现实的利益问题作为工作核心，把老百姓口碑作为评价干部业绩的重要标准。",
        "evidence_level": "评分细则原文明示人民立场/最高价值标准",
        "source_lines": Q21_SOURCE,
    },
]

SECTION_NEXT = {
    "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一": "主观能动性 / 意识的能动作用",
    "尊重客观规律与发挥主观能动性相结合": "规律的客观性",
    "整体与部分": "系统观念 / 系统优化",
    "辩证否定 / 守正创新": "矛盾就是对立统一",
    "矛盾的特殊性 / 具体问题具体分析": "矛盾的普遍性和特殊性",
    "实践与认识（总）": "实践是认识的基础",
    "实践是认识的基础": "认识对实践的反作用",
    "社会存在与社会意识": "社会发展的两大基本规律和基本矛盾",
    "人民群众": "价值观的导向作用",
    "价值观的导向作用": "价值判断与价值选择",
    "价值判断与价值选择": "实现人生价值",
    "实现人生价值": "__END__",
}

KEYS = {
    "id": "matrix_row_id",
    "source": "题源",
    "year": "年份",
    "stage": "阶段",
    "question": "题号",
    "type": "题型或模块判断",
    "in_body": "是否进宝典",
    "node": "宝典节点",
    "principle": "细则支持原理",
    "evidence": "证据等级",
    "misplaced": "是否误放",
    "needs": "是否需补厚",
    "action": "当前处理",
    "note": "备注",
    "artifact": "source_artifact",
}


def load_base():
    spec = importlib.util.spec_from_file_location("batch13_base", BASE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load base script: {BASE_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.ENTRIES = ENTRIES
    module.SECTION_NEXT = SECTION_NEXT
    module.SUITE = SUITE

    def find_section(paras, heading: str) -> tuple[int, int]:
        next_heading = SECTION_NEXT[heading]
        start = next((i for i, p in enumerate(paras) if module.para_text(p).strip() == heading), None)
        if start is None:
            raise RuntimeError(f"section heading not found: {heading}")
        if next_heading == "__END__":
            return start, len(paras)
        end = next((i for i in range(start + 1, len(paras)) if module.para_text(paras[i]).strip() == next_heading), None)
        if end is None:
            raise RuntimeError(f"next heading not found after {heading}: {next_heading}")
        return start, end

    module.find_section = find_section
    return module


def update_docx(base, timestamp: str) -> list[str]:
    docx = base.current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_2025_chaoyang_yimo_batch14_{timestamp}.docx")
    shutil.copy2(docx, backup)
    with zipfile.ZipFile(docx, "r") as zin:
        infos = zin.infolist()
        data = {info.filename: zin.read(info.filename) for info in infos}
    root = base.etree.fromstring(data["word/document.xml"])
    headings = [base.insert_entry(root, entry) for entry in ENTRIES]
    data["word/document.xml"] = base.etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp_path = Path(tmp.name)
    try:
        with zipfile.ZipFile(tmp_path, "w") as zout:
            for info in infos:
                zi = zipfile.ZipInfo(info.filename, date_time=info.date_time)
                zi.compress_type = info.compress_type
                zi.external_attr = info.external_attr
                zout.writestr(zi, data[info.filename])
        shutil.move(tmp_path, docx)
    finally:
        if tmp_path.exists():
            tmp_path.unlink()
    return headings


def accepted_record(entry: dict[str, str], heading: str) -> dict[str, str]:
    student = (
        f"{heading}\n"
        f"【材料触发点】 {entry['material_trigger']}\n"
        f"【设问】 {entry['question_prompt']}\n"
        f"【为什么能想到】 {entry['why_trigger']}\n"
        f"【答案落点】 {entry['answer_landing']}"
    )
    return {
        "source_suite": SUITE,
        "question_no": entry["question_no"],
        "framework_node": entry["canonical_node"],
        "canonical_node": entry["canonical_node"],
        "material_trigger": entry["material_trigger"],
        "question_prompt": entry["question_prompt"],
        "why_trigger": entry["why_trigger"],
        "answer_landing": entry["answer_landing"],
        "student_facing_text": student,
        "evidence_level": entry["evidence_level"],
        "boundary_note": entry["evidence_level"],
        "source_lane": "Codex Batch14 recovery production",
        "source_repair_basis": entry["source_lines"],
        "source_lines": entry["source_lines"],
        "batch": "batch14_2025_chaoyang_yimo",
    }


def update_ledger(timestamp: str, headings: list[str]) -> None:
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_batch14_2025_chaoyang_yimo_{timestamp}{LEDGER.suffix}")
    shutil.copy2(LEDGER, backup)
    with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []
    desired = {
        (e["canonical_node"], SUITE, e["question_no"]): {
            "canonical_node": e["canonical_node"],
            "source_suite": SUITE,
            "question_no": e["question_no"],
            "inserted_heading": h,
        }
        for e, h in zip(ENTRIES, headings)
    }
    out, seen = [], set()
    for row in rows:
        key = (row["canonical_node"], row["source_suite"], row["question_no"])
        if key in desired:
            if key not in seen:
                out.append(desired[key])
                seen.add(key)
            continue
        out.append(row)
    for key, row in desired.items():
        if key not in seen:
            out.append(row)
            seen.add(key)
    with LEDGER.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(out)


def update_accepted(timestamp: str, headings: list[str]) -> None:
    backup = ACCEPTED.with_name(f"{ACCEPTED.stem}_backup_before_batch14_2025_chaoyang_yimo_{timestamp}{ACCEPTED.suffix}")
    shutil.copy2(ACCEPTED, backup)
    records = [json.loads(line) for line in ACCEPTED.read_text(encoding="utf-8").splitlines() if line.strip()]
    desired = {(SUITE, e["question_no"], e["canonical_node"]): accepted_record(e, h) for e, h in zip(ENTRIES, headings)}
    out, seen = [], set()
    for record in records:
        key = (record.get("source_suite"), record.get("question_no"), record.get("canonical_node"))
        if key in desired:
            if key not in seen:
                out.append(desired[key])
                seen.add(key)
            continue
        out.append(record)
    for key, record in desired.items():
        if key not in seen:
            out.append(record)
            seen.add(key)
    ACCEPTED.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in out) + "\n", encoding="utf-8")


def patch_row(row: dict[str, str], **values: str) -> None:
    for key, value in values.items():
        row[KEYS[key]] = value


def row_values(row_id: str, q: str, type_: str, in_body: str, node: str, principle: str, evidence: str, action: str, note: str, artifact: str) -> dict[str, str]:
    return {
        KEYS["id"]: row_id,
        "row_source": "batch14_2025_chaoyang_yimo_missing_boundary_inventory",
        KEYS["source"]: SUITE,
        KEYS["year"]: YEAR,
        KEYS["stage"]: STAGE,
        KEYS["question"]: q,
        KEYS["type"]: type_,
        KEYS["in_body"]: in_body,
        KEYS["node"]: node,
        KEYS["principle"]: principle,
        KEYS["evidence"]: evidence,
        KEYS["misplaced"]: "否",
        KEYS["needs"]: "否",
        KEYS["action"]: action,
        KEYS["note"]: note,
        KEYS["artifact"]: artifact,
    }


def update_matrix(timestamp: str, headings: list[str]) -> None:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch14_2025_chaoyang_yimo_{timestamp}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []
    by_id = {r[KEYS["id"]]: r for r in rows}
    h = dict(zip([(e["question_no"], e["canonical_node"]) for e in ENTRIES], headings))
    q16_note = (
        "Q16已登记/补插："
        f"{h[('Q16', '实践与认识（总）')]}；"
        f"{h[('Q16', '实践是认识的基础')]}；"
        f"{h[('Q16', '辩证否定 / 守正创新')]}；"
        f"{h[('Q16', '尊重客观规律与发挥主观能动性相结合')]}；"
        f"{h[('Q16', '整体与部分')]}；"
        f"{h[('Q16', '社会存在与社会意识')]}；"
        f"{h[('Q16', '实现人生价值')]}。"
    )
    q21_note = (
        "Q21已登记/补插："
        f"{h[('Q21', '一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一')]}；"
        f"{h[('Q21', '人民群众')]}；"
        f"{h[('Q21', '价值观的导向作用')]}；"
        f"{h[('Q21', '价值判断与价值选择')]}。"
    )
    q16_principle = (
        "2025朝阳一模细则第16题：文化载体1分，文化资源/正确价值观2分，借助现代科技推动文化创新2分，"
        "立足国情满足人民需要2分，发挥主观能动性/个人与社会统一/实现人生价值/以局部推动整体1分；"
        "教师版参考答案列文化传承与创新、实践、社会存在社会意识、价值创造与实现。"
    )
    q21_principle = (
        "2025朝阳一模细则第21题：尊重人民主体地位，坚持群众观点和群众路线；重视价值观导向作用，"
        "自觉站在最广大人民立场上，把人民群众利益作为最高价值标准；坚持实事求是、求真务实。"
    )
    decisions = {
        "M0177": dict(question="Q16", in_body="是：已由当前DOCX覆盖/补插并登记ledger/accepted", node="实践与认识（总）/实践是认识的基础/社会存在与社会意识/实现人生价值/辩证否定/尊重客观规律与发挥主观能动性/整体与部分", principle=q16_principle, evidence="评分细则原文明示+教师版参考答案", misplaced="否", needs="否", action="COVERED_AND_REGISTERED_BATCH14", note=q16_note, artifact=Q16_SOURCE),
        "M0209": dict(type="哲学与文化综合-细则闭合", in_body="是：已由当前DOCX覆盖/补插并登记ledger/accepted", node="实践与认识（总）/实践是认识的基础/社会存在与社会意识/实现人生价值/辩证否定/尊重客观规律与发挥主观能动性/整体与部分", principle=q16_principle, evidence="评分细则原文明示+教师版参考答案", misplaced="否", needs="否", action="COVERED_AND_REGISTERED_BATCH14", note=q16_note, artifact=Q16_SOURCE),
        "M0413": dict(in_body="否：中国特色社会主义/党史定位边界题", node="不进入当前哲学宝典正文", principle="Q1官方答案C（②④）：强调中国共产党与时俱进把握世情国情党情变化、把握历史规律和趋势；属于党史/中国特色社会主义政治判断，错误项①不使用。", evidence="官方答案键+正确选项链条+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH14", note="不因材料出现发展、规律字样强行放入哲学节点。", artifact=f"{SOURCE_BUNDLE}:527-534;{ANSWER_KEY_SOURCE}"),
        "M0414": dict(in_body="否：教育强国/法治教育边界题", node="不进入当前哲学宝典正文", principle="Q2官方答案D（③④）：宪法法治教育践行社会主义核心价值观、劳动教育提升实践能力，属于教育政策/德育劳动教育；不是必修四哲学细则题。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH14", note="可作教育素材，不作为哲学宝典正文新增。", artifact=f"{SOURCE_BUNDLE}:535-542;{ANSWER_KEY_SOURCE}"),
        "M0415": dict(in_body="否：逻辑与思维/经济技术边界题", node="不进入当前哲学宝典正文", principle="Q3官方答案C（②④）：分析与综合属于逻辑与思维，解放生产力属于经济/技术发展；①改变物质意识关系为错误项。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH14", note="不把错误项①或技术发展字样转入哲学正文。", artifact=f"{SOURCE_BUNDLE}:543-551;{ANSWER_KEY_SOURCE}"),
        "M0416": dict(in_body="是：已由当前DOCX覆盖并登记ledger/accepted", node="矛盾的特殊性 / 具体问题具体分析", principle="Q4官方答案B：正确选项明确“敌进我退，敌驻我扰，敌疲我打，敌退我追”把握具体分析方法。", evidence="选择题官方答案键+正确选项B", misplaced="否", needs="否", action="COVERED_AND_REGISTERED_BATCH14", note=f"登记条目：{h[('Q4', '矛盾的特殊性 / 具体问题具体分析')]}。", artifact=Q4_SOURCE),
        "M0417": dict(in_body="否：逻辑与思维判断题", node="不进入当前哲学宝典正文", principle="Q5官方答案D（③④）：考查判断的周延、联言判断等逻辑知识；虽出现“认识”字样，但设问本体是逻辑与思维。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH14", note="术语近邻不入必修四哲学正文。", artifact=f"{SOURCE_BUNDLE}:563-569;{ANSWER_KEY_SOURCE}"),
        "M0418": dict(in_body="否：逻辑与思维/创新思维边界题", node="不进入当前哲学宝典正文", principle="Q7官方答案C（②④）：跨越性、形象思维和抽象思维互补，属于逻辑与思维。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH14", note="不使用错误项③“突破客观条件制约”。", artifact=f"{SOURCE_BUNDLE}:576-583;{ANSWER_KEY_SOURCE}"),
        "M0419": dict(in_body="否：政治与法治/人大政协履职边界题", node="不进入当前哲学宝典正文", principle="Q8官方答案C（②④）：人大代表、政协委员履职及建议提案办理机制，属于政治与法治。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH14", note="不因促进经济高质量发展字样转入发展观。", artifact=f"{SOURCE_BUNDLE}:584-600;{ANSWER_KEY_SOURCE}"),
        "M0420": dict(in_body="否：政治与法治/生态法治边界题", node="不进入当前哲学宝典正文", principle="Q9官方答案B（①③）：国家公园保护发展和区域协同立法，属于政治法治/生态治理；不作为系统观念或整体部分新增。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH14", note="正确项①虽含统筹，但本题不是哲学设问，且落点为国家公园法治建设。", artifact=f"{SOURCE_BUNDLE}:601-608;{ANSWER_KEY_SOURCE}"),
        "M0421": dict(in_body="否：经济与社会/绿色发展边界题", node="不进入当前哲学宝典正文", principle="Q12官方答案B（①④）：林下经济、绿水青山、研究市场和多种经营，属于经济与社会/绿色发展。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH14", note="实践字样来自绿色发展实践，不作哲学正文新增。", artifact=f"{SOURCE_BUNDLE}:626-637;{ANSWER_KEY_SOURCE}"),
        "M0422": dict(in_body="否：经济与社会/全国统一大市场边界题", node="不进入当前哲学宝典正文", principle="Q13官方答案A（①②）：就业公共服务、数据交易标准、要素资源市场，属于经济与社会。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH14", note="改革/发展词不替代哲学细则。", artifact=f"{SOURCE_BUNDLE}:638-644;{ANSWER_KEY_SOURCE}"),
        "M0423": dict(in_body="否：当代国际政治与经济边界题", node="不进入当前哲学宝典正文", principle="Q15官方答案B（①③）：联合国、主权平等、多边主义，属于当代国际政治与经济；材料“矛盾越复杂”不是本题正确项的哲学落点。", evidence="官方答案键+模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH14", note="不把国际关系材料中的矛盾字样转入哲学节点。", artifact=f"{SOURCE_BUNDLE}:675-685;{ANSWER_KEY_SOURCE}"),
        "M0424": dict(in_body="是：已由当前DOCX覆盖/补插并登记ledger/accepted", node="实践与认识（总）/实践是认识的基础/社会存在与社会意识/实现人生价值/辩证否定/尊重客观规律与发挥主观能动性/整体与部分", principle=q16_principle, evidence="评分细则原文明示+教师版参考答案", misplaced="否", needs="否", action="COVERED_AND_REGISTERED_BATCH14", note=q16_note, artifact=Q16_SOURCE),
        "M0425": dict(in_body="否：逻辑与思维+经济与社会边界题", node="不进入当前哲学宝典正文", principle="Q17(1)设问明确《逻辑与思维》，阅卷总结细则为充分/必要条件推理；Q17(2)设问明确《经济与社会》。", evidence="评分细则原文明示-模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH14", note="不把阅卷总结中的主流/部分等通用词转入必修四。", artifact=f"{SOURCE_BUNDLE}:705-729;857-888;{Q17_REVIEW}"),
        "M0426": dict(in_body="否：政治与法治边界题", node="不进入当前哲学宝典正文", principle="Q18设问明确《政治与法治》，细则为党建引领、政府履职、基层自治、居民参与、社会组织协同。", evidence="评分细则原文明示-模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH14", note="不把人民群众、整体、联系等泛词从政治法治题误放到哲学宝典。", artifact=f"{SOURCE_BUNDLE}:730-742;890-891;{RULE_RENDER_002};{Q18_REVIEW}"),
        "M0427": dict(in_body="否：法律与生活边界题", node="不进入当前哲学宝典正文", principle="Q19设问明确《法律与生活》，细则为合同成立/可撤销、消费者权益保护法、欺诈、三倍赔偿。", evidence="评分细则原文明示-模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH14", note="末尾社会意义中有核心价值观，但不是必修四哲学主落点。", artifact=f"{SOURCE_BUNDLE}:743-763;892-926;{RULE_RENDER_002};{Q19_REVIEW}"),
        "M0428": dict(in_body="否：当代国际政治与经济边界题", node="不进入当前哲学宝典正文", principle="Q20设问明确《当代国际政治与经济》，细则为全球产业链供应链多元化、区域化、绿色化、数字化及对外开放应对。", evidence="评分细则原文明示-模块边界", misplaced="否", needs="否", action="MODULE_BOUNDARY_EXCLUDED_BATCH14", note="不把产业发展字样转入发展观。", artifact=f"{SOURCE_BUNDLE}:764-797;{RULE_RENDER_002};{RULE_RENDER_003}"),
        "M0429": dict(in_body="是：已由当前DOCX覆盖/补插并登记ledger/accepted", node="一切从实际出发/人民群众/价值观的导向作用/价值判断与价值选择", principle=q21_principle, evidence="评分细则原文明示", misplaced="否", needs="否", action="COVERED_AND_REGISTERED_BATCH14", note=q21_note, artifact=Q21_SOURCE),
        "M0430": dict(in_body="否：抽取残留/阅卷总结泛词", node="不进入当前哲学宝典正文", principle="该行无独立题号，内容来自Q18政治法治阅卷总结中的体系建构/系统性泛词；已在M0426按模块边界关闭。", evidence="抽取残留清理+逐题源包核对", misplaced="否", needs="否", action="EXTRACTION_RESIDUE_CLOSED_BATCH14", note="不保留Qunknown挂起。", artifact=f"{SOURCE_BUNDLE}:1-949;{Q18_REVIEW}"),
        "M0789": dict(in_body="套卷逐题已由Batch14闭合", node="SUITE_LEVEL_SUMMARY", principle="2025朝阳一模Q1-Q21已逐题回源；Q4/Q16/Q21入正文或登记，其他题按答案键/细则模块边界排除。", evidence="Batch14逐题矩阵闭合", misplaced="否", needs="否", action="SUITE_CLOSED_BY_BATCH14", note="套卷级记录不替代逐题记录。", artifact=f"{SOURCE_BUNDLE}:1-949"),
        "M0828": dict(in_body="套卷逐题已由Batch14闭合", node="SUITE_LEVEL_SUMMARY", principle="2025朝阳一模源包、教师版、细则渲染页及17/18/19阅卷总结已核；逐题挂起项已关闭。", evidence="Batch14逐题矩阵闭合", misplaced="否", needs="否", action="SUITE_CLOSED_BY_BATCH14", note="原套卷级挂起项关闭。", artifact=f"{SOURCE_BUNDLE}:1-949;{RULE_RENDER_001};{RULE_RENDER_002};{RULE_RENDER_003}"),
    }
    for row_id, values in decisions.items():
        if row_id not in by_id:
            raise RuntimeError(f"matrix row not found: {row_id}")
        patch_row(by_id[row_id], **values)
    max_id = max(int(r[KEYS["id"]][1:]) for r in rows if re.match(r"^M\d+$", r[KEYS["id"]]))
    additions = [
        row_values(f"M{max_id + 1:04d}", "Q6", "逻辑与思维/书法五体划分边界题", "否：逻辑与思维边界题", "不进入当前哲学宝典正文", "Q6官方答案A，考查换位/分类逻辑规则，属于逻辑与思维。", "官方答案键+模块边界", "MISSING_ROW_ADDED_AND_EXCLUDED_BATCH14", "原矩阵缺独立Q6行，本批补充边界闭合。", f"{SOURCE_BUNDLE}:570-575;{ANSWER_KEY_SOURCE}"),
        row_values(f"M{max_id + 2:04d}", "Q10", "法律与生活/AI著作权边界题", "否：法律与生活边界题", "不进入当前哲学宝典正文", "Q10官方答案D（③④），考查AI生成图片著作权保护和独创性智力投入，属于法律与生活。", "官方答案键+模块边界", "MISSING_ROW_ADDED_AND_EXCLUDED_BATCH14", "原矩阵缺独立Q10行，本批补充边界闭合。", f"{SOURCE_BUNDLE}:609-617;{ANSWER_KEY_SOURCE}"),
        row_values(f"M{max_id + 3:04d}", "Q11", "法律与生活/行政公益诉讼边界题", "否：法律与生活/法治边界题", "不进入当前哲学宝典正文", "Q11官方答案D，区人民检察院当诉则诉，展现以检察职能维护社会公共利益的担当，属于法治/法律与生活。", "官方答案键+模块边界", "MISSING_ROW_ADDED_AND_EXCLUDED_BATCH14", "原矩阵缺独立Q11行，本批补充边界闭合。", f"{SOURCE_BUNDLE}:618-625;{ANSWER_KEY_SOURCE}"),
        row_values(f"M{max_id + 4:04d}", "Q14", "当代国际政治与经济/外贸数据边界题", "否：当代国际政治与经济边界题", "不进入当前哲学宝典正文", "Q14官方答案C（②④），考查外贸顺逆差、机电产品出口和高新技术产品贸易数据，属于当代国际政治与经济/经济统计分析。", "官方答案键+模块边界", "MISSING_ROW_ADDED_AND_EXCLUDED_BATCH14", "原矩阵缺独立Q14行，本批补充边界闭合。", f"{SOURCE_BUNDLE}:645-674;{ANSWER_KEY_SOURCE}"),
    ]
    existing = {(r[KEYS["source"]], r[KEYS["question"]], r[KEYS["action"]]) for r in rows}
    for row in additions:
        key = (row[KEYS["source"]], row[KEYS["question"]], row[KEYS["action"]])
        if key not in existing:
            rows.append(row)
            existing.add(key)
    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_source_transcription(timestamp: str) -> None:
    text = f"""# Batch14 Source Transcription - 2025朝阳一模

timestamp: {timestamp}
operator: Codex recovery thread
suite: 2025朝阳一模
status: SOURCE_PACKET_COMPLETE_FOR_BATCH14

## Source Files Checked

- teacher paper PDF: `{PAPER_PDF}`
- detail rule PDF: `{RULE_PDF}`
- rendered rule pages: `{RULE_RENDER_001}`, `{RULE_RENDER_002}`, `{RULE_RENDER_003}`
- source bundle: `{SOURCE_BUNDLE}`
- marking summaries checked for module boundaries: `{Q17_REVIEW}`, `{Q18_REVIEW}`, `{Q19_REVIEW}`

## Answer Key

Q1-Q15 official answer key from teacher paper:

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|
| answer | C | D | C | B | D | A | C | C | B | D | D | B | A | C | B |

## Rendered Rule Transcription

### Q16

- 作为文化载体，国产动画电影承载千年故事、荟萃文化元素、凸显文化符号，为中华优秀传统文化在新时代绽放光彩提供展示平台。1分。
- 重视文化资源，钩沉千年中华文明独特魅力，传承千年故事，弘扬民族精神，向观众传递正确价值观和奋斗精神，为中华优秀传统文化创造性转化探索路径。2分。
- 借助现代科技推动文化创新，依托关键技术，精雕细节，打造关键戏份，让传统文化与现代传播方式结合，以更加生动、形象、震撼的方式呈现，为优秀传统文化创新性发展增添活力。2分。
- 立足国情，满足人民需要。经济社会发展为国产动画电影产业提供物质基础、市场空间、产业平台；创作团队面向人民需求，使传统文化精神与当代观众情感产生共鸣。2分。
- 创作者团队把握社会提供的客观条件，把握个人与社会的统一，弘扬劳动精神、工匠精神、创新精神，推动行业变革，实现人生价值，以局部推动整体，推动中华优秀传统文化以新形式展现。1分。

### Q21

- 综合运用至少两个模块知识，逻辑清晰：是什么、为什么、怎么样。1分。
- “是什么”部分：大事小事观、为民办事观、造福人民的政绩观都可围绕党和人民关系展开。
- “为什么”部分：端正并践行上述观念，体现坚持以人民为中心的发展思想；坚持党的初心使命、执政理念和不负人民精神；坚持实事求是、求真务实；尊重人民主体地位，坚持群众观点和群众路线；重视价值观导向作用，自觉站在最广大人民立场上，把人民群众利益作为最高价值标准。
- “怎么办”部分：党组织、党员、干部应贯彻新时代中国特色社会主义思想，坚持并发扬上述观念，为人民群众把好事办好、把实事办实、把难事办妥。

## Student-Facing Insert/Register Decisions

- Q4 -> existing `矛盾的特殊性 / 具体问题具体分析`, supported by official answer B.
- Q16 -> existing entries registered plus added entries under `辩证否定 / 守正创新`, `尊重客观规律与发挥主观能动性相结合`, and `整体与部分`.
- Q21 -> existing entries registered plus added entries under `一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一` and `价值观的导向作用`.

## Exclusions

- Q1-Q3, Q5-Q15 except Q4: closed by official answer key and module boundary.
- Q17: Q17(1) is Logic and Thinking; Q17(2) is Economy and Society.
- Q18: Political and Law.
- Q19: Legal Life.
- Q20: Contemporary International Politics and Economy.
- Qunknown: extraction residue from Q18 marking summary.
"""
    SOURCE_TRANSCRIPTION.write_text(text, encoding="utf-8")


def write_report(timestamp: str, headings: list[str]) -> None:
    inserted = "\n".join(f"- {heading}" for heading in headings)
    text = f"""# Coverage Fusion Batch14 - 2025朝阳一模

timestamp: {timestamp}
operator: Codex recovery thread
suite: 2025朝阳一模
status: CODEX_BATCH14_SOURCE_COVERAGE_APPLIED

## Applied To DOCX / Ledger / Accepted

{inserted}

## Matrix Disposition

- Q4, Q16, and Q21 were registered in `docx_insert_ledger.csv` and `student_patch_entries.accepted.jsonl`.
- Q16 added or confirmed seven student-facing nodes: practice/recognition, practice as basis, dialectical negation, objective law and subjective initiative, whole/part, social existence/social consciousness, and value realization.
- Q21 added or confirmed four student-facing nodes: seeking truth from facts, people as historical subject, value-guidance, and value judgment/choice.
- Q1-Q3, Q5-Q15 except Q4, Q17-Q20, and Qunknown were closed as source-supported module-boundary or extraction-residue decisions.

## Boundary

No Sonnet/Haiku/model-unknown output was used. Ordinary teacher-answer angle support is not treated as detailed scoring support unless the rendered rule page also supports it.
GPTPro web / external Claude Opus full-artifact review remains `real_call_pending`; Batch14 is a local Codex + ClaudeCode production-lane closure only.
"""
    BATCH_REPORT.write_text(text, encoding="utf-8")


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base = load_base()
    headings = update_docx(base, timestamp)
    update_ledger(timestamp, headings)
    update_accepted(timestamp, headings)
    update_matrix(timestamp, headings)
    write_source_transcription(timestamp)
    write_report(timestamp, headings)
    print(f"Batch14 applied at {timestamp}")
    for heading in headings:
        print(heading)


if __name__ == "__main__":
    main()
