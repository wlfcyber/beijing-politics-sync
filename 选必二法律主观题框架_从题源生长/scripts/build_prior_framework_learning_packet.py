# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
import textwrap
import zipfile
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree as ET

import pdfplumber


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
DESKTOP_PRIOR = Path("/Users/wanglifei/Desktop/先前框架")
OUT = ROOT / "05_reasoner_packets" / "prior_framework_learning_gptpro_20260520"
REFS = OUT / "references_md"
CONTROL_FILES = [
    ROOT / "PROGRESS.md",
    ROOT / "governor_board.md",
    ROOT / "DECISIONS.md",
    ROOT / "RISKS.md",
    ROOT / "TODO.md",
]


OLD_MD_SOURCES = [
    Path("/Users/wanglifei/Desktop/5.5 claudecode重跑选必二/选必二《法律与生活》框架版_2026-05-05.md"),
    Path("/Users/wanglifei/Desktop/5.5 claudecode重跑选必二/主干性涵盖性自评.md"),
    Path("/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/delivery/选必二法律与生活零基础上手框架_学生可用版_2026-05-04.md"),
    Path("/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/delivery/选必二法律框架踩分逻辑_主观选择分列版_2026-05-04.md"),
    Path("/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/final_legal_outputs/选必二法律与生活最终进化框架_2026-05-03.md"),
    Path("/Users/wanglifei/Desktop/北京高考政治/选必一_国际政治与经济_框架+三年国政经题链_细则版.md"),
    Path("/Users/wanglifei/Desktop/北京高考政治/选必三_逻辑与思维_思维部分_框架+三年题链_穷尽版.md"),
    Path("/Users/wanglifei/Desktop/北京高考政治/选必一_国际政治与经济_零基础满分课稿.md"),
]

DOCX_STYLE_SOURCES = [
    Path("/Users/wanglifei/Desktop/哲学宝典最终版 5.2学生可读终极版.docx"),
    Path("/Users/wanglifei/Desktop/哲学宝典最终版 5.2双终极融合版_目录页码美化版.docx"),
    Path("/Users/wanglifei/Desktop/4.29飞哥政治庄园选必一凌晨v1版本_阅读版.docx"),
]


def now_stamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def safe_name(name: str) -> str:
    base = re.sub(r"[^\w\u4e00-\u9fff.-]+", "_", name, flags=re.UNICODE)
    return base.strip("_")[:140] or "unnamed"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_csv(path: Path) -> list[dict]:
    for enc in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            with path.open("r", encoding=enc, newline="") as f:
                return list(csv.DictReader(f))
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("unknown", b"", 0, 1, f"cannot decode {path}")


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def trunc(text: str, limit: int) -> str:
    text = re.sub(r"\s+", " ", (text or "")).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 18].rstrip() + " ...[truncated]"


def extract_pdf_text(path: Path) -> tuple[str, int, list[str]]:
    warnings: list[str] = []
    parts: list[str] = []
    pages = 0
    try:
        with pdfplumber.open(path) as pdf:
            pages = len(pdf.pages)
            for i, page in enumerate(pdf.pages, 1):
                try:
                    text = page.extract_text(x_tolerance=1.5, y_tolerance=3) or ""
                except Exception as exc:  # noqa: BLE001
                    text = ""
                    warnings.append(f"page {i} extract failed: {exc}")
                text = text.strip()
                if text:
                    parts.append(f"\n\n## Page {i}\n\n{text}")
                else:
                    parts.append(f"\n\n## Page {i}\n\n[NO_TEXT_LAYER_OR_EXTRACTION_EMPTY]")
    except Exception as exc:  # noqa: BLE001
        warnings.append(f"open failed: {exc}")
    return "\n".join(parts).strip(), pages, warnings


def extract_docx_text(path: Path) -> str:
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    out: list[str] = []
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml")
    root = ET.fromstring(xml)
    for p in root.findall(".//w:p", ns):
        runs = [t.text or "" for t in p.findall(".//w:t", ns)]
        line = "".join(runs).strip()
        if line:
            out.append(line)
    return "\n".join(out)


def write_md(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def build_prior_sources() -> list[dict]:
    rows: list[dict] = []
    REFS.mkdir(parents=True, exist_ok=True)

    for idx, pdf in enumerate(sorted(DESKTOP_PRIOR.glob("*.pdf")), 1):
        text, pages, warnings = extract_pdf_text(pdf)
        out_name = f"prior_pdf_{idx:02d}_{safe_name(pdf.stem)}.md"
        out_path = REFS / out_name
        md = f"""# 先前框架 PDF 转写：{pdf.name}

> 用途：只学习框架表达、学生可启动结构、版式组织和答题动作设计；不得作为选必二法律题源证据。
> 转写方法：pdfplumber 文本层抽取。若页内标注 NO_TEXT_LAYER_OR_EXTRACTION_EMPTY，说明该页文字层不可用，需要视觉/人工复核。

- 原始路径：`{pdf}`
- 页数：{pages}
- 抽取字符数：{len(text)}
- 警告：{'; '.join(warnings) if warnings else '无'}

{text if text else '[PDF_TEXT_EXTRACTION_EMPTY]'}
"""
        write_md(out_path, md)
        rows.append(
            {
                "source_id": f"PRIOR_PDF_{idx:02d}",
                "source_type": "desktop_prior_framework_pdf",
                "original_path": str(pdf),
                "converted_path": str(out_path),
                "file_name": pdf.name,
                "page_count": pages,
                "char_count": len(text),
                "sha256": sha256(pdf),
                "role_for_gptpro": "style_structure_reference_only",
                "evidence_use_allowed": "no",
                "notes": "; ".join(warnings) if warnings else "text-layer extract available, layout not fully preserved",
            }
        )

    md_idx = 0
    for src in OLD_MD_SOURCES:
        if not src.exists():
            continue
        md_idx += 1
        text = src.read_text(encoding="utf-8", errors="replace")
        out_path = REFS / f"prior_md_{md_idx:02d}_{safe_name(src.stem)}.md"
        content = f"""# 先前框架 Markdown 样本：{src.name}

> 用途：学习框架组织方式、学生版语言、主干/容器关系、逐题运行写法。
> 限制：其中关于选必二法律的旧结论不得直接继承；必须回到 STEP_29 65 题证据核验。

- 原始路径：`{src}`
- 抽取字符数：{len(text)}

{text}
"""
        write_md(out_path, content)
        rows.append(
            {
                "source_id": f"PRIOR_MD_{md_idx:02d}",
                "source_type": "prior_framework_markdown",
                "original_path": str(src),
                "converted_path": str(out_path),
                "file_name": src.name,
                "page_count": "",
                "char_count": len(text),
                "sha256": sha256(src),
                "role_for_gptpro": "style_structure_reference_only",
                "evidence_use_allowed": "no",
                "notes": "legacy framework sample; legal conclusions require re-verification",
            }
        )

    docx_idx = 0
    for src in DOCX_STYLE_SOURCES:
        if not src.exists():
            continue
        docx_idx += 1
        try:
            text = extract_docx_text(src)
            note = "docx text extracted"
        except Exception as exc:  # noqa: BLE001
            text = ""
            note = f"docx extraction failed: {exc}"
        out_path = REFS / f"prior_docx_excerpt_{docx_idx:02d}_{safe_name(src.stem)}.md"
        content = f"""# 先前宝典 DOCX 文字样本：{src.name}

> 用途：学习学生可读性、章节组织、讲义感、逐题示范口吻。
> 限制：只作为写作/组织样本，不作为选必二法律证据。

- 原始路径：`{src}`
- 抽取字符数：{len(text)}
- 备注：{note}

{trunc(text, 50000) if text else '[DOCX_TEXT_EXTRACTION_EMPTY]'}
"""
        write_md(out_path, content)
        rows.append(
            {
                "source_id": f"PRIOR_DOCX_{docx_idx:02d}",
                "source_type": "prior_handbook_docx_excerpt",
                "original_path": str(src),
                "converted_path": str(out_path),
                "file_name": src.name,
                "page_count": "",
                "char_count": len(text),
                "sha256": sha256(src),
                "role_for_gptpro": "student_readability_reference_only",
                "evidence_use_allowed": "no",
                "notes": note,
            }
        )

    write_csv(
        OUT / "prior_framework_source_inventory.csv",
        rows,
        [
            "source_id",
            "source_type",
            "original_path",
            "converted_path",
            "file_name",
            "page_count",
            "char_count",
            "sha256",
            "role_for_gptpro",
            "evidence_use_allowed",
            "notes",
        ],
    )
    return rows


def build_evidence_compact() -> tuple[list[dict], Counter]:
    q_path = ROOT / "04_merge_audit" / "merged_subjective_law_questions.csv"
    r_path = ROOT / "04_merge_audit" / "merged_rubric_atoms_subjective.csv"
    q_rows = read_csv(q_path)
    r_rows = read_csv(r_path)
    rubrics_by_q: dict[str, list[dict]] = defaultdict(list)
    for r in r_rows:
        rubrics_by_q[r.get("question_id", "")].append(r)

    compact: list[dict] = []
    for q in q_rows:
        qid = q.get("question_id", "")
        rubrics = rubrics_by_q.get(qid, [])
        rubric_lines = []
        atom_ids = []
        for r in rubrics[:8]:
            atom_ids.append(r.get("rubric_atom_id", ""))
            phrase = r.get("rubric_or_answer_phrase", "")
            rule = r.get("legal_knowledge_or_rule_if_explicit", "")
            reward = r.get("plain_reward_description", "")
            rubric_lines.append(f"{r.get('rubric_atom_id','')}: {phrase} | {reward} | {rule}")
        compact.append(
            {
                "question_id": qid,
                "year": q.get("year", ""),
                "district": q.get("district", ""),
                "exam_stage": q.get("exam_stage", ""),
                "question_no": q.get("question_no", ""),
                "evidence_type": q.get("evidence_type", ""),
                "evidence_level": q.get("evidence_level", ""),
                "module_boundary_risk": q.get("module_boundary_risk", ""),
                "confidence": q.get("confidence", ""),
                "ask_text": trunc(q.get("ask_text", ""), 500),
                "material_text_compact": trunc(q.get("material_text", ""), 900),
                "answer_text_compact": trunc(q.get("answer_text", ""), 800),
                "rubric_atom_ids_sample": ";".join(atom_ids),
                "rubric_summary_sample": trunc(" || ".join(rubric_lines), 1500),
                "source_locator": q.get("source_locator", ""),
            }
        )

    fields = [
        "question_id",
        "year",
        "district",
        "exam_stage",
        "question_no",
        "evidence_type",
        "evidence_level",
        "module_boundary_risk",
        "confidence",
        "ask_text",
        "material_text_compact",
        "answer_text_compact",
        "rubric_atom_ids_sample",
        "rubric_summary_sample",
        "source_locator",
    ]
    write_csv(OUT / "current_65_legal_evidence_compact.csv", compact, fields)
    stats = Counter(row.get("evidence_level", "") for row in q_rows)
    return compact, stats


STYLE_DIGEST = """# 先前框架学习摘要：给 GPTPro 的结构 DNA

## 使用边界

先前框架只能作为“怎么把难内容讲成学生能上手”的结构样本，不能作为本轮选必二法律证据。本轮法律内容必须回到 STEP_29 回退后的 65 道主观题、362 个细则原子和对应材料原子。

## 可以迁移的 12 条结构原则

1. 先给学生一个总入口：拿到陌生题，第一眼先判断什么，而不是先背目录。
2. 用少数强主干承载全书：主干要能带学生进题，旁支只作容器，不喧宾夺主。
3. 每个节点必须是动作：节点名要告诉学生“圈什么、判什么、写什么句”，不能只是漂亮名词。
4. 材料翻译优先：先把材料中的主体、行为、冲突、权利义务、程序结果翻译成法律语言，再调用知识。
5. 答案结构要有强制句型：学生需要可直接落笔的满分句模板，而不是教师才懂的抽象说明。
6. 价值表达后置：价值必须由规则推出，不能让答案空泛必修三化。
7. 区分题型功能：评析、说明、建议、意义、程序路径题的启动方式不同。
8. 高频情境要落到踩分词：合同、侵权、劳动、消费者、知识产权、家庭继承、纠纷解决等必须有关键词。
9. 开放容器要存在：低频题不能硬塞进主干，但要有“边界刹车”和处理入口。
10. 学生版和教师版分层：学生版短、可背、可执行；教师版解释证据和边界。
11. 错法改法显性化：每个节点要告诉学生最容易写偏到哪里。
12. 框架必须能逐题运行：不能只像目录，要能对每道题生成接近细则的答案句。

## 旧法律框架中值得作为待验证假设的结构

这些结构曾经有效，但本轮不能直接继承，必须用 65 题和细则验证：

- 一核：以事实为根据、以法律为准绳，通过具体法律关系中的规则适用实现定分止争。
- 二线：权利保护与权利边界；规则适用与程序救济。
- 三问：判什么/怎么处理；凭什么；有什么意义。
- 四步：定主体关系 -> 找争点事实 -> 对规则条件 -> 按题型落结果。
- 3 必 + 3 选解释链：关系句、规则句、结论句；争点句、适用句、价值句。
- 六类命题路径：裁判依据题、程序救济题、表格补全题、观点评析题、意义认识题、选择题机制；本轮只取主观题机制。
- 五域学生可背版：合同消费者劳动；物权相邻继承家庭；人格权侵权；知识产权不正当竞争；纠纷解决生态公益与新业态。

## 当前必须避免的失败形态

1. 审计报告式框架：证据很多，但学生看完不会写。
2. 教材目录式框架：合同、侵权、劳动并列罗列，却不给审题入口和句型。
3. 万题一词式框架：每道题都说“定主体关系”，但不讲材料触发和踩分句。
4. 证据标签淹没学生动作：formal、reference_only 等应放在教师/审计层，不应塞满学生首屏。
5. 学生可读性吞掉证据边界：为了顺口而让 reference_only 支撑核心节点，必须禁止。
6. 法考化：把高三主观题变成复杂构成要件分析。
7. 必修三化：法律知识只是背景，答案全写依法治国、法治社会、权力运行。
"""


def build_prompt(stats: Counter, q_count: int, source_count: int) -> None:
    prompt = f"""# GPT-5.5 Pro 任务：学习先前框架，重做选必二《法律与生活》主观题框架 v0

你现在接手的是“选必二《法律与生活》主观题框架从题源生长工程”的重做任务。

用户已经明确否定上一版成品：它像审计报告，学生看完仍然不可能满分。现在需要你学习桌面上的先前优秀框架材料，吸收它们的结构能力、学生可启动性、讲义表达方式，然后基于当前 65 道法律主观题证据，重新做出法律这本书的主观题框架。

## 输入包

1. `PRIOR_FRAMEWORK_STYLE_DIGEST.md`
   - 这是 Codex 对先前框架可迁移结构 DNA 的摘要。
2. `prior_framework_source_inventory.csv`
   - 先前框架来源清单。
3. `references_md/`
   - 桌面先前框架 PDF 的文本层转写。
   - 旧选必二/选必一/选必三/哲学等框架样本。
   - DOCX 宝典样本文字摘录。
4. `current_65_legal_evidence_compact.csv`
   - 当前唯一可用的选必二法律证据底座。
   - 题目数：{q_count}
   - evidence_level 统计：{json.dumps(dict(stats), ensure_ascii=False)}

## 最高边界

1. 先前框架只能学“结构、表达、可学会性”，不能当本轮法律证据。
2. 当前法律框架节点必须回到 `current_65_legal_evidence_compact.csv` 中的 question_id、rubric_atom_id、材料和细则。
3. reference_only 可以帮助理解，但不能单独支撑核心节点。
4. 不要输出最终宝典，本轮只输出“法律主观题框架 v0”，供后续逐题压测。
5. 不要写选择题框架。本轮只研究主观题。
6. 不能法考化，不能必修三化，不能教材目录化。
7. 学生版首屏必须能让“聪明但啥都不会的高三学生”看到陌生题后立刻知道：
   - 先圈什么；
   - 先判断什么；
   - 材料怎么翻译成法律语言；
   - 答案第一句、第二句、第三句怎么写；
   - 哪些价值话能写，哪些不能乱写。

## 你要完成的输出

### 一、你从先前框架学到了什么

请列出你吸收的结构原则，不要泛泛夸。要具体说明这些原则如何改造法律主观题框架。

### 二、旧的“一核二线三问四步五域”怎么处理

请判断：保留、改造、拆散、丢弃。每一项都要说明原因。注意它们是待验证结构，不是证据。

### 三、选必二法律主观题框架 v0

必须包括：

1. 学生首屏版：不超过一页，能背、能用。
2. 教师解释版：解释每个节点为什么存在。
3. 3-7 个主节点。每个节点都必须是动作/判断/生成句，不是教材目录名。
4. 每个节点包含：
   - node_id
   - node_name
   - 学生版一句话
   - 设问触发词
   - 材料触发信号
   - 最小必要判断
   - 材料到法律语言的翻译方式
   - 满分句生成模板
   - 必写关键词
   - 易错偏题路径
   - 支持的 question_id
   - 支持的 rubric_atom_id 样例
   - 不能乱用的边界
   - evidence_strength：strong / medium / weak

### 四、开放容器和边界刹车

低频题、综合题、边界题不能硬塞主干。请设计一个开放容器，告诉学生遇到不典型法律题时如何处理，怎样避免写成必修三或法考。

### 五、抽 5 道题做快速运行

请从 65 题里抽 5 道不同类型的题。每道只写：

- question_id
- 从哪个节点进入
- 圈出的材料触发信号
- 最小必要判断
- 对应 rubric_atom_id
- 2-4 句满分答案骨架
- 这个运行暴露的框架风险

### 六、压测前风险清单

列出你认为 v0 还需要 Codex 回源压测的地方。

## 语言要求

像一个特别会教高三学生的老师。不要写成论文，不要写成审计表，不要堆术语。框架要清楚、狠、能立刻落笔。
"""
    write_md(OUT / "PROMPT_FOR_GPTPRO_PRIOR_FRAMEWORK_LEARNING_LEGAL_V0_20260520.md", prompt)


def build_readme(source_rows: list[dict], stats: Counter, compact: list[dict]) -> None:
    readme = f"""# GPTPro 先前框架学习包：选必二法律主观题 v0

生成时间：{now_stamp()}

## 本包用途

把桌面 `先前框架` 与若干旧框架/宝典样本转成 GPTPro 可读的 Markdown/CSV，让 GPTPro 学习它们的结构表达能力，再基于当前 STEP_29 回退后的 65 道选必二法律主观题证据，重做法律主观题框架 v0。

## 文件

- `PROMPT_FOR_GPTPRO_PRIOR_FRAMEWORK_LEARNING_LEGAL_V0_20260520.md`：发给 GPTPro 的主 prompt。
- `PRIOR_FRAMEWORK_STYLE_DIGEST.md`：先前框架结构 DNA 摘要。
- `prior_framework_source_inventory.csv`：先前框架来源清单，共 {len(source_rows)} 个来源。
- `references_md/`：已转 Markdown 的先前框架材料。
- `current_65_legal_evidence_compact.csv`：当前法律证据压缩表，共 {len(compact)} 道题。
- `PACKET_VALIDATION.md`：本包校验结果。

## 禁令

先前框架不是证据。法律框架节点必须由 65 题和细则支撑。
"""
    write_md(OUT / "README.md", readme)

    validation = f"""# Packet Validation

- 生成时间：{now_stamp()}
- 先前框架来源数：{len(source_rows)}
- 法律证据题数：{len(compact)}
- evidence_level 统计：{dict(stats)}
- 期望基线：65 题，61 formal，4 reference_only，0 missing。
- 当前状态：{"PASS" if len(compact) == 65 and stats.get("formal", 0) == 61 and stats.get("reference_only", 0) == 4 and stats.get("missing", 0) == 0 else "CHECK_REQUIRED"}

## 注意

PDF 转写依赖文本层，可能无法完整保留版式和图像中文字。GPTPro 应优先学习 `PRIOR_FRAMEWORK_STYLE_DIGEST.md`、旧 Markdown 框架样本和 DOCX 摘录中的结构表达。
"""
    write_md(OUT / "PACKET_VALIDATION.md", validation)


def update_controls(stats: Counter, q_count: int, zip_path: Path) -> None:
    stamp = now_stamp()
    progress = f"""

## STEP_62_PRIOR_FRAMEWORK_LEARNING_PACKET - {stamp}

- 已按用户要求读取桌面 `先前框架`，并转写为 GPTPro 可读 Markdown/CSV 包。
- 输出目录：`{OUT}`
- 打包文件：`{zip_path}`
- 先前框架用途：只学习结构、表达、学生可启动性；不得作为选必二法律证据。
- 当前法律证据底座仍为 STEP_29 回退基线：{q_count} 题，evidence_level={dict(stats)}。
- 下一步：把 `PROMPT_FOR_GPTPRO_PRIOR_FRAMEWORK_LEARNING_LEGAL_V0_20260520.md` 与 zip 包提交给 GPTPro，要求生成法律主观题框架 v0。
"""
    (ROOT / "PROGRESS.md").write_text((ROOT / "PROGRESS.md").read_text(encoding="utf-8", errors="replace") + progress, encoding="utf-8")

    governor = f"""

## Governor Update - STEP_62_PRIOR_FRAMEWORK_LEARNING_PACKET - {stamp}

- 当前阶段：回退到 65 题证据底座后，构造“先前框架学习 -> 法律框架 v0”输入包。
- 已完成文件：
  - `{OUT / "README.md"}`
  - `{OUT / "PRIOR_FRAMEWORK_STYLE_DIGEST.md"}`
  - `{OUT / "prior_framework_source_inventory.csv"}`
  - `{OUT / "current_65_legal_evidence_compact.csv"}`
  - `{OUT / "PROMPT_FOR_GPTPRO_PRIOR_FRAMEWORK_LEARNING_LEGAL_V0_20260520.md"}`
  - `{zip_path}`
- 证据数量：{q_count} 题。
- formal/reference_only/missing：{stats.get("formal",0)}/{stats.get("reference_only",0)}/{stats.get("missing",0)}
- 当前是否允许进入下一阶段：允许进入 GPTPro 学习生成 v0，但不得视为最终框架。
- 下一步任务：提交 GPTPro 并保存 GPTPro 输出。
- 责任工具：Codex A -> GPTPro。
"""
    (ROOT / "governor_board.md").write_text((ROOT / "governor_board.md").read_text(encoding="utf-8", errors="replace") + governor, encoding="utf-8")

    decision = f"""

## DECISION - {stamp} - 先前框架作为结构样本而非证据

用户要求学习桌面先前框架。决定：允许旧框架进入 GPTPro 输入包，但仅作为结构 DNA、学生可读性和讲义组织样本；当前法律内容、框架节点和满分句必须由 STEP_29 65 题及细则原子支撑。旧选必二结论不得直接继承。
"""
    (ROOT / "DECISIONS.md").write_text((ROOT / "DECISIONS.md").read_text(encoding="utf-8", errors="replace") + decision, encoding="utf-8")

    risk = f"""

## RISK - {stamp} - 先前框架学习包风险

- PDF 转写依赖文本层，部分页面可能无法保留视觉布局或图片中文字。
- GPTPro 可能把旧框架结论误当证据，prompt 已明确禁止。
- 学生可读性提升不能牺牲 evidence_level 边界：reference_only 不得单独支撑核心节点。
"""
    (ROOT / "RISKS.md").write_text((ROOT / "RISKS.md").read_text(encoding="utf-8", errors="replace") + risk, encoding="utf-8")

    todo = f"""

## TODO Update - {stamp}

- [x] 桌面先前框架转写为 GPTPro 可读包。
- [x] 生成结构 DNA 摘要。
- [x] 生成当前 65 题法律证据 compact CSV。
- [ ] 提交 GPTPro 并保存输出。
- [ ] 用 GPTPro v0 回到 65 题逐题压测。
"""
    (ROOT / "TODO.md").write_text((ROOT / "TODO.md").read_text(encoding="utf-8", errors="replace") + todo, encoding="utf-8")


def make_zip() -> Path:
    zip_path = OUT.with_suffix(".zip")
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for path in sorted(OUT.rglob("*")):
            if path.is_file():
                z.write(path, path.relative_to(OUT.parent))
    return zip_path


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True, exist_ok=True)
    REFS.mkdir(parents=True, exist_ok=True)

    source_rows = build_prior_sources()
    write_md(OUT / "PRIOR_FRAMEWORK_STYLE_DIGEST.md", STYLE_DIGEST)
    compact, stats = build_evidence_compact()
    build_prompt(stats, len(compact), len(source_rows))
    build_readme(source_rows, stats, compact)
    zip_path = make_zip()
    update_controls(stats, len(compact), zip_path)

    print(json.dumps({"out": str(OUT), "zip": str(zip_path), "questions": len(compact), "stats": dict(stats), "sources": len(source_rows)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
