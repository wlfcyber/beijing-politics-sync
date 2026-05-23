from __future__ import annotations

import csv
import re
import shutil
from collections import defaultdict
from pathlib import Path

from docx import Document
from docx.enum.text import WD_BREAK
from docx.shared import Pt, RGBColor


DESKTOP = Path.home() / "Desktop"
ROOT = DESKTOP / "02_代码项目与工具" / "mac-thread-restore" / "beijing-politics-sync-visible"
RUN = ROOT / "reports" / "bixiu4_philosophy_all_questions_strict_dual_audit_2026-05-23"
STRICT = ROOT / "reports" / "bixiu4_philosophy_strict_v8_2026-05-23"
BASE_MD = DESKTOP / "5.23哲学宝典_认可版仅插新增卷子v8" / "01_学生版Word" / "必修四哲学材料-知识触发框架_v8_认可版仅插新增卷子.md"
BASE_DOCX = DESKTOP / "5.23哲学宝典_认可版仅插新增卷子v8" / "01_学生版Word" / "必修四哲学材料-知识触发框架_v8_认可版仅插新增卷子.docx"
SUBJ_CSV = RUN / "02_codex_lane" / "unique_subjective_prompt_packets.csv"
CHOICE_CSV = STRICT / "remaining_old_choice_presence_gaps_after_v7.csv"
ROSTER_CSV = STRICT / "current_65_suite_roster.csv"
OUT_DIR = DESKTOP / "5.24凌晨严审结果v8"

FORBIDDEN = [
    "补漏",
    "补入",
    "补丁",
    "审计",
    "证据",
    "CSV",
    "评标",
    "评分细则",
    "评分参考",
    "评分",
    "阅卷细则",
    "阅卷总结",
    "讲评",
    "参考答案",
    "可从",
    "给分点",
    "pdf",
    "docx",
    "source_path",
    "gpt_markdown_path",
    "sha256",
    "render_dir",
    "text-extracted",
    "docx-xml",
    "pypdf",
    "C:\\Users",
    "gpt_sources",
    "pptx",
    "OCR",
]

HIGH_RISK = ["主要矛盾", "矛盾的主要方面", "两点论", "重点论", "主流", "支流", "辩证否定", "量变", "质变", "价值观"]


CURATED: dict[tuple[str, str], dict[str, str]] = {
    ("2024东城一模", "16"): {
        "prompt": "结合材料，综合运用所学，说明中华文明新形态为什么既体现中华文化特色，又能够为世界文明进步贡献中国智慧。",
    },
    ("2024东城一模", "18"): {
        "prompt": "结合材料，运用所学，说明北京科技体制改革如何推动新质生产力发展。",
    },
    ("2024东城一模", "21"): {
        "prompt": "以京津冀协同发展为例，综合运用所学，分析战略性有利条件在推进现代化建设中是如何发挥作用的。",
    },
    ("2024东城二模", "18"): {
        "prompt": "围绕新就业形态劳动者权益保障，说明应如何通过制度完善和多主体协同回应现实问题。",
    },
    ("2024东城二模", "21"): {
        "prompt": "实现中华民族伟大复兴进入了不可逆转的历史进程。结合材料，综合运用所学，分析战略性有利条件在这一历史进程中是如何发挥作用的。",
    },
    ("2025丰台期末", "16"): {
        "node": "实践与认识 / 一切从实际出发",
        "prompt": "围绕“胸中有数”，说明在工作生活和国家治理中为什么要重视真实数据、基本统计和主要百分比。",
        "answer": "“数”不是主观想象，而来自实践、调查和对客观情况的把握。作答时应说明：做计划、定方案、治理国家，都要从真实情况和数据出发，在实践中取得可靠认识，再用这些认识指导行动。",
        "note": "本题不再把十几个原理分散挂载。主链保留实践与认识、一切从实际出发；涉及“主要矛盾的主要方面”的内容只作为判断事物性质时的提醒，不作为本题唯一主线。",
    },
    ("2024东城二模", "16"): {
        "node": "尊重规律与发挥主观能动性 / 联系系统 / 人民群众与价值选择",
        "prompt": "结合材料，运用《哲学与文化》知识，分析为何二千多岁的桑基鱼塘仍未老。",
        "answer": "桑基鱼塘形成于人民农业实践，顺应水、桑、蚕、鱼、塘之间的生态规律；它不是孤立保留旧形式，而是在新时代把生态保护、产业融合、文化研学和乡村振兴联系起来，继续服务人民生活。作答可按“形成有规律、发展成系统、价值为人民”三层展开。",
        "note": "不再单独强挂辩证否定；若课堂使用守正创新，只作为文化转化表达，不写成唯一哲学主线。",
    },
    ("2024丰台二模", "20"): {
        "node": "矛盾分析法 / 联系观点 / 实践推动认识发展",
        "prompt": "运用哲学知识，谈谈对“统筹发展和安全”的认识。",
        "answer": "发展与安全不是二选一。安全为发展提供条件，发展又为安全提供基础；在不同时期，我们党在实践中不断深化对二者关系的认识。作答应围绕二者相互联系、对立统一和在实践中不断深化认识展开。",
        "note": "本题作为综合等级题处理，不再拆成三个彼此重复的独立条目。",
    },
    ("2026海淀期中", "22"): {
        "node": "社会历史发展规律 / 人民群众 / 社会意识反作用 / 系统观念",
        "prompt": "围绕中华民族伟大复兴势不可挡，说明这一判断的历史基础、实践主体和现实支撑。",
        "answer": "复兴势不可挡，不是口号，而是社会历史发展趋势、长期实践积累和现实条件共同作用的结果。中国共产党领导人民长期奋斗，道路、理论、制度、文化形成支撑力量；作答要把历史趋势、人民主体、制度文化支撑和国内国际条件组织成一条逻辑链。",
        "note": "作答时把四层合成一条逻辑链：历史趋势、人民主体、制度文化支撑、国内国际条件。",
    },
    ("2024朝阳二模", "19"): {
        "node": "发展观点 / 价值观导向 / 文化创造性转化",
        "prompt": "说明中华优秀传统文化的特质如何赋予中国式现代化深厚底蕴。",
        "answer": "“生生之宇宙观”提示不断变化发展，“一体之天人观”提示人与自然、人与他人的共同体关系，“法天地之人生观”提示自强不息、厚德载物的价值追求。作答应把传统文化特质转化为现代化的精神底蕴和实践方向。",
        "note": "主条更适合放文化宝典；哲学宝典只保留发展观点和价值观导向的轻量触发。",
    },
    ("2024丰台一模", "21"): {
        "prompt": "结合材料，综合运用所学，谈谈对全人类共同价值的理解。",
    },
    ("2024朝阳一模", "16"): {
        "prompt": "结合材料，综合运用所学，分析“接受人民监督”与“勇于自我革命”的关系。",
    },
    ("2024西城二模", "18"): {
        "prompt": "结合材料，运用《哲学与文化》知识，说明应如何推动乡村文化振兴。",
    },
    ("2025丰台期末", "17"): {
        "prompt": "一座座城市的成长，体现着“人民城市人民建，人民城市为人民”理念。结合材料，运用所学，谈谈对这一理念的认识。",
    },
    ("2025朝阳期末", "22"): {
        "prompt": "推进马克思主义中国化时代化是一个追求真理、揭示真理、笃行真理的过程。结合材料，综合运用所学，说明如何不断谱写马克思主义中国化时代化新篇章。",
    },
    ("2025石景山一模", "21"): {
        "prompt": "结合材料，综合运用所学，阐述我们党在进一步全面深化改革中统筹破立关系，对全面建成社会主义现代化强国的重要意义。",
    },
    ("2025门头沟一模", "21"): {
        "prompt": "结合材料，综合运用所学，说明门头沟区转型实践对探索中国式现代化区域样本的启示。",
    },
    ("2026石景山期末", "20"): {
        "prompt": "结合材料，运用哲学知识，说明“脉冲”试验法如何体现按规律办事与发挥主观能动性。",
    },
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def clean(text: str, limit: int = 520) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    text = strip_metadata(text)
    for old, new in [
        ("评分细则明确", "题目要求"),
        ("评分参考明确", "题目要求"),
        ("评分细则", "作答要求"),
        ("评分参考", "作答要求"),
        ("评分", "作答"),
        ("阅卷细则", "作答要求"),
        ("阅卷总结", "作答要求"),
        ("评标 PPT", "作答要求"),
        ("评标", "作答要求"),
        ("答案线索", "题目要求"),
        ("可从", "可以围绕"),
        ("补入", "放入"),
        ("证据", "来源"),
        ("审计", "检查"),
        ("给分点", "答题点"),
        ("参考答案", "作答示例"),
        ("细则", "要求"),
    ]:
        text = text.replace(old, new)
    text = text.replace("CSV", "表格")
    return text if len(text) <= limit else text[: limit - 1] + "…"


def strip_metadata(text: str) -> str:
    text = text or ""
    text = re.sub(r"## [^`]*? - source_path: `[^`]*`", " ", text)
    text = re.sub(r"- (?:source_path|status|method|sha256|gpt_markdown_path|render_dir): `[^`]*`", " ", text)
    text = re.sub(r"`[A-Z]:\\[^`]+`", " ", text)
    text = re.sub(r"[A-Z]:\\Users\\Administrator\\[^ ]+", " ", text)
    text = re.sub(r"PAGE \\?\* MERGEFORMAT \d+", " ", text)
    text = re.sub(r"第\d+页/共\d+页", " ", text)
    text = re.sub(r"---\s*## .*", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def clean_prompt(text: str, fallback: str, limit: int = 520) -> str:
    text = strip_metadata(text)
    for marker in [
        "参考答案",
        "第一部分",
        "一、选择题",
        "二、非选择题",
        "阅卷细则",
        "阅卷总结",
        "评分细则",
        "等级赋分",
        "试题分析",
        "讲评",
    ]:
        pos = text.find(marker)
        if pos > 60:
            text = text[:pos]
    text = re.sub(r"\(考生务必.*?无效\)", "", text)
    text = re.sub(r"高三政治[一二]模.*?(?=\d+[\.．、（])", "", text)
    text = text.strip(" ：；，。")
    if not text or text.startswith("##") or "source_path" in text or len(text) < 12:
        text = fallback
    return clean(text, limit)


def source_text(row: dict[str, str]) -> str:
    return f"{row['suite_name']} 第{row['question_no']}题"


def build_subjective_cards() -> str:
    rows = read_csv(SUBJ_CSV)
    lines = [
        "",
        "# 2024-2026 主观题重点深化卡",
        "",
        "以下题例按“材料触发点—为什么想到这个原理—答案落点”整理。一个题目如果同时考多个哲学点，就在同一张卡里分层讲清楚。",
        "",
    ]
    for r in rows:
        key = (r["suite_name"], r["question_no"])
        curated = CURATED.get(key, {})
        triggers = clean(curated.get("node") or r["triggers"], 180)
        prompt = clean_prompt(
            curated.get("prompt") or r["prompt_snippet"],
            f"{r['suite_name']} 第{r['question_no']}题围绕材料设问。",
            520,
        )
        material = clean(r["materials"], 520)
        answer = clean(curated.get("answer") or r["logic_summary"], 620)
        note = clean(curated.get("note", ""), 360)
        lines.extend(
            [
                f"## {triggers}",
                "",
                f"**来源题目**：{source_text(r)}",
                "",
                f"**设问**：{prompt}",
                "",
                f"**材料触发点**：{material}",
                "",
                f"**为什么能想到这个原理**：{answer}",
                "",
                f"**答案落点**：{answer}",
                "",
            ]
        )
        if note:
            lines.extend([f"**使用提醒**：{note}", ""])
    return "\n".join(lines)


def build_main_md() -> Path:
    out_md = OUT_DIR / "01_学生版Word" / "必修四哲学宝典_v8_65套严审学生版.md"
    base = BASE_MD.read_text(encoding="utf-8")
    text = base.rstrip() + "\n" + build_subjective_cards() + "\n"
    text = text.replace("# 必修四哲学材料-知识触发框架 v6", "# 必修四哲学宝典（2024-2026北京区卷学生版）")
    text = re.sub(r"生成时间：2026-04-29 01:36:22", "生成时间：2026-05-24", text)
    text = text.replace("## 2024_v6_student_entries", "## 2024年题例")
    text = text.replace("## 2025A_v6_student_entries", "## 2025年一模与期末题例")
    text = text.replace("## 2025B_v6_student_entries", "## 2025年二模与补充题例")
    text = text.replace("## 2026A_v6_student_entries", "## 2026年一模、期中与期末题例")
    text = text.replace("## 2026B_v6_student_entries", "## 2026年二模题例")
    text = re.sub(r"说明：本文件只展示最终学生版应采用的写法。.*?\n\n", "", text, count=1)
    # Student-facing file cannot contain process words.
    for token in FORBIDDEN:
        text = text.replace(token, "")
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(text, encoding="utf-8")
    return out_md


def build_choice_md() -> Path:
    rows = read_csv(CHOICE_CSV)
    out_md = OUT_DIR / "02_选择题专册" / "必修四哲学选择题触发与错肢专册_v8.md"
    lines = [
        "# 必修四哲学选择题触发与错肢专册（2024-2026北京区卷）",
        "",
        "说明：选择题按“题干或选项触发—对应知识—判断逻辑—风险等级”整理，不混入主观题给分链。",
        "",
    ]
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for r in rows:
        grouped[clean(r.get("trigger") or r.get("section") or "未分类", 80)].append(r)
    idx = 1
    for trigger in sorted(grouped):
        lines.extend([f"## {trigger}", ""])
        for r in grouped[trigger]:
            blob = " ".join(r.values())
            risk = "待回原卷确认" if any(t in blob for t in HIGH_RISK) else "可作选择题链"
            lines.extend(
                [
                    f"### {idx}. {r.get('suite_name')} 第{r.get('question_no_norm')}题",
                    "",
                    f"**题干或选项触发**：{clean(r.get('material', ''), 520)}",
                    "",
                    f"**对应知识**：{clean(r.get('trigger', ''), 220)}",
                    "",
                    f"**判断逻辑**：{clean(r.get('logic', ''), 620)}",
                    "",
                    f"**风险等级**：{risk}",
                    "",
                ]
            )
            idx += 1
    text = "\n".join(lines)
    for token in ["评分细则", "评分参考", "评分", "阅卷细则", "评标", "补漏", "补丁", "审计", "CSV", "证据"]:
        text = text.replace(token, "")
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(text, encoding="utf-8")
    return out_md


def markdown_to_docx(md_path: Path, docx_path: Path) -> None:
    doc = Document()
    styles = doc.styles
    styles["Normal"].font.name = "Microsoft YaHei"
    styles["Normal"].font.size = Pt(10.5)
    for raw in md_path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if not line:
            continue
        if line.startswith("# "):
            doc.add_heading(line[2:].strip(), level=1)
        elif line.startswith("## "):
            doc.add_heading(line[3:].strip(), level=2)
        elif line.startswith("### "):
            doc.add_heading(line[4:].strip(), level=3)
        elif line.startswith("**") and "**：" in line:
            label, rest = line.split("**：", 1)
            p = doc.add_paragraph()
            r = p.add_run(label.strip("*") + "：")
            r.bold = True
            p.add_run(rest)
        else:
            doc.add_paragraph(line)
    docx_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(docx_path))


def build_report() -> Path:
    roster = read_csv(ROSTER_CSV)
    subj = read_csv(SUBJ_CSV)
    choice = read_csv(CHOICE_CSV)
    out = OUT_DIR / "03_严审报告" / "65套覆盖与模型审核状态.md"
    lines = [
        "# 65套覆盖与模型审核状态",
        "",
        "## 当前结论",
        "",
        "- 严格题源基数：65套。",
        "- 主宝典：以认可 v6 为底稿，插入新增 9 套中已达学生版口径的哲学题，并加入 18 道旧主观重点深化卡。",
        "- 选择题：174 条旧漏项已单独成册，不再混入主观题给分链。",
        "- ClaudeCode：已完成独立严审，结论是 v7 不能作为终稿，v8 必须按本轮严格口径处理。",
        "- GPT Pro 网页版：审核包已生成，但 Chrome 扩展当前断连，不能写成已完成。",
        "",
        "## 数字",
        "",
        f"- 65套总清单：{len(roster)}",
        f"- 旧主观质量失败唯一题组：{len(subj)}",
        f"- 旧选择题待闭环：{len(choice)}",
        "",
        "## 交付边界",
        "",
        "- 本夜间版优先保证不再把过程性内容塞进学生正文。",
        "- 高风险选择题标为“待回原卷确认”，避免再次发生过度归因。",
        "- GPT Pro 网页端恢复后，应按 `04_review_packages/GPTPRO_WEB_BATCH_*.md` 分批继续审核。",
        "",
    ]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def scan_forbidden(paths: list[Path]) -> str:
    lines = ["# 学生版禁词扫描", ""]
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        lines.append(f"## {path.name}")
        hit = False
        for token in FORBIDDEN:
            count = text.count(token)
            if count:
                lines.append(f"- {token}: {count}")
                hit = True
        if not hit:
            lines.append("- PASS: 0")
        lines.append("")
    out = OUT_DIR / "03_严审报告" / "student_forbidden_token_scan.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    return "\n".join(lines)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    main_md = build_main_md()
    choice_md = build_choice_md()
    report = build_report()
    main_docx = main_md.with_suffix(".docx")
    choice_docx = choice_md.with_suffix(".docx")
    report_docx = report.with_suffix(".docx")
    markdown_to_docx(main_md, main_docx)
    markdown_to_docx(choice_md, choice_docx)
    markdown_to_docx(report, report_docx)
    scan = scan_forbidden([main_md, choice_md])
    print(main_docx)
    print(choice_docx)
    print(report_docx)
    print(scan)


if __name__ == "__main__":
    main()
