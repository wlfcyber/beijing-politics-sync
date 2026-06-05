#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
VERSION = "v26"
DATE = "20260605"
CHUNK_COUNT = 12

PACKAGE_DIR = ROOT / f"web_app_external_review_{VERSION}_{DATE}"
ZIP_PATH = ROOT / f"web_app_external_review_{VERSION}_{DATE}.zip"
DESKTOP_DIR = Path(f"/Users/wanglifei/Desktop/给网页版应用外审_选必二{VERSION}_{DATE}")
DESKTOP_ZIP = DESKTOP_DIR.with_suffix(".zip")

OUTPUTS = [
    ROOT / "outputs" / f"选必二法律与生活_试题细则汇编_学生可发版_{VERSION}.docx",
    ROOT / "outputs" / f"选必二法律与生活_试题细则汇编_学生可发版_{VERSION}.md",
    ROOT / "outputs" / f"选必二法律与生活_AB双轴学生宝典_学生可发版_{VERSION}.docx",
    ROOT / "outputs" / f"选必二法律与生活_AB双轴学生宝典_学生可发版_{VERSION}.md",
]

QA_FILES = [
    ROOT / "qa" / f"TWO_DOC_CLEAN_DRAFT_QA_{VERSION}_{DATE}.md",
    ROOT / "qa" / f"RENDER_QA_{VERSION}_{DATE}.md",
    ROOT / "qa" / "INVALID_CLI_EXTERNAL_REVIEW_NOTE_20260605.md",
    ROOT / "qa" / f"key_pages_contact_sheet_{VERSION}.png",
    ROOT / "qa" / f"rendered_compilation_{VERSION}" / f"选必二法律与生活_试题细则汇编_学生可发版_{VERSION}.pdf",
    ROOT / "qa" / f"rendered_baodian_{VERSION}" / f"选必二法律与生活_AB双轴学生宝典_学生可发版_{VERSION}.pdf",
]

DOCS = {
    "compilation": {
        "label": "试题和细则汇编",
        "path": ROOT / "outputs" / f"选必二法律与生活_试题细则汇编_学生可发版_{VERSION}.md",
    },
    "baodian": {
        "label": "AB双轴学生宝典",
        "path": ROOT / "outputs" / f"选必二法律与生活_AB双轴学生宝典_学生可发版_{VERSION}.md",
    },
}


HEADER = f"""BEGIN_REVIEW_INSTRUCTIONS
# External Review Context
You are GPT-5.5 Pro doing one chunk of a formal web/app review. Do not invent exam evidence, rubric facts, scoring rules, or legal facts. This is a partial chunk review; do not issue the final project verdict unless asked in a final synthesis prompt.

User requires exactly two student-facing DOCX documents for 选必二《法律与生活》:
1. 试题和细则汇编: all 2024-2026 选必二 subjective questions; each entry has 题目来源、材料、设问、细则、答案落点、同题组.
2. AB双轴学生宝典: A-axis legal relation framework + B-axis answer-shape framework; under each A-axis core point, core answer points/knowledge, then all related subjective questions with the same required fields.

Forbidden student-facing noise: 三十秒速记, engineering/production traces, internal E0xx IDs, source_id/SRC_, absolute local paths, TODO/BLOCKED, backend verification chatter, 制作记录, 命题人路径, 判题四步.

Current candidate is {VERSION}. Local QA reports:
- Empty rubric-marker suspects in both Markdown files: 0.
- DOCX XML scan found 0 occurrences of local paths or image-path traces.
- Rendered successfully: 汇编 84 pages, 宝典 93 pages.
- Student-facing DOCX files embed no whole-page source screenshots; source/rubric images remain backend evidence only.
- Rendered-PDF OCR scan found no `元首外交`, paper footer, backend trace, or prior OCR-pollution terms.

Important process constraint: any prior CLI-based Claude/GPT result is invalid for this project and must not be counted. This prompt is for a new valid web/app review pass only.

{VERSION} inherits the v10 fixes for the valid GPT-5.5 Pro web review failure from v9 compilation-01, and additionally fixes the valid GPT-5.5 Pro web review failure from v10 compilation-03:
- 2026 朝阳期末18(1): cleaned material/rubric/answer points for the online consumption contract case.
- 2026 朝阳二模18: restored three legal Q&A blanks and the rights-protection answer points.
- 2026 通州期末19(1): restored Civil Code Article 292 and Article 296 legal basis.
- 2026 通州一模20: cleaned severe OCR damage in parties, court, liability, and public-place text.
- 2026 门头沟一模18(1): removed empty trailing rubric marker.
- 2026 房山二模17: removed duplicated/half scoring language from answer points.
- 2026 西城二模18(1)(2): cleaned AI/court/rubric OCR wording.
- 2026 顺义一模18 and 顺义二模18(2): added shared-value and governance-risk answer angles.
- Render QA also changed the Chinese font to Hiragino Sans GB so E049 `稳步前行` renders without dropped glyphs.

{VERSION} specifically fixes the valid Claude Opus 4.8 Max Safari web/app review failure from v11:
- 2024 朝阳二模17: removed `原答案：`, `辩`, `实社社会` and other OCR/editorial pollution; rewrote answer points as clean student-facing bullets.
- 2026 房山二模18(1): moved the AI legal-risk item from A1 to A5 知识产权与公平竞争, with a note that it also involves 名誉权.

{VERSION} also applies a post-Claude cleanup pass for small nonblocking OCR/text defects:
- 2025 东城二模19: `钱某事限制民事行为能力人` -> `钱某是限制民事行为能力人`.
- 2025 东城期末19(1): `建车栩会占用绿地` -> `建车棚会占用绿地`.
- 2025 丰台二模19(2): `参考答 案` -> `参考答案`.
- 2025 丰台期末19: `法院驳回了尹荣的诉讼请求` -> `法院驳回了尹某的诉讼请求`.
- 2026 丰台一模20: `低头看手机 监控画面` -> `低头看手机。监控画面`.
- 2026 丰台二模18: `予盾化解` -> `矛盾化解`.

{VERSION} additionally fixes the valid GPT-5.5 Pro web/app v13 compilation-01 concerns around screenshot spillover and answer-point residue:
- E002 answer points now expose both the 甲公司 and 乙公司 litigation paths within the visible student-facing answer points.
- Student-facing documents no longer embed full-page `原题图` or `细则图`; this removes whole-page screenshot spillover such as the 2025 东城一模第19题 source image carrying Q20 `元首外交` non-Xuanbier material.
- Backend source-image assets are still retained under QA for local verification, but the two student documents are text-only.

{VERSION} also responds to the GPT-5.5 Pro web/app v16 compilation-01 review:
- Locally verified that the named entries still contain the required `题目来源/材料/设问/细则/答案落点/同题组` fields.
- Rewrote student-facing answer points for 2024 石景山一模17, 2024 西城二模16, 2025 东城期末19(1), 2025 东城二模19, and 2025 房山一模19 so raw `细则/替换/变通` residue does not appear in 答案落点.
- GPT chunks are now smaller to reduce cross-entry conflation in web review.

{VERSION} additionally fixes two issues surfaced while adjudicating the v17 web/app first-chunk result:
- 2024 东城一模19: `李某 郭某出具欠据` -> `李某为郭某出具欠据`, confirmed against the earlier formal accepted source text.
- 2024 东城二模19(1): scoring wording now says `乙公司作出肯定答复（材料表述为“可以”）`, avoiding a visible `可以/好的` mismatch for students.
- The previous v17 first-chunk GPT result is not used for closure because browser input-state evidence showed prompt ordering corruption. This package uses smaller chunks and plain BEGIN/END delimiters instead of Markdown code fences.

{VERSION} also fixes the valid GPT-5.5 Pro web/app v18 compilation-01 review:
- 2024 丰台一模17: restored the full reality-meaning scoring chain, including maintaining social fairness, interpersonal harmony, socialist core values, reducing traffic congestion, and advocating green travel.
- 2024 东城二模19(2): changed the visible rubric score label from whole-question `19.（9分）` to this subquestion `19（2）（2分）`.
- 2024 东城一模19: removed the score label from the student-facing answer points while preserving the formal rubric score line.

{VERSION} additionally repairs issues surfaced while adjudicating the v19 web/app first-chunk result:
- Local source/render/OCR contradicted the v19 GPT blocker about 2024 丰台一模17 material fracture; this is recorded as web-input contamination, not a document defect.
- 2024 朝阳一模19: removed the answer-point score-label residue while preserving the formal rubric score line.
- Applied a global answer-point cleanup layer to remove leading question-number / score shells from student-facing answer-point bullets while preserving formal rubric text.
- 2026 延庆一模18(1): replaced a whole-rubric answer-point dump with seven clean student-facing answer points.
- {VERSION} Markdown and OCR scans found no backend/web prompt traces and no answer-point bullets beginning with score shells.

{VERSION} also fixes the valid GPT-5.5 Pro web/app v23 compilation-06 review:
- 2025 海淀期末20: restored the original table/example/blank-column structure from the source DOCX and removed the editor residue `表格条款补充`; render QA then changed the visible student text to a clear `表格转写` format.
- 2025 海淀一模18: rewrote answer points as clean student-facing bullets while preserving the formal scoring-rule text in `细则`.
- Broader answer-point residue scan then cleaned E010, E035, E048, E050, E053, E054, E057, E062, E063, E066, E067, and E069 so `答案落点` no longer begins with raw score shells, `【细则】`, `评分细则`, or prompt-like headings.

For this chunk, identify only BLOCKING defects or significant NONBLOCKING issues visible in the chunk. If something depends on original exam images not present in this chunk, say what Codex must locally verify; do not invent corrected wording.
END_REVIEW_INSTRUCTIONS
"""


TASK_TEMPLATE = """

# Chunk Task
Document: {doc_label}
Chunk: {idx}/{total}

Review this chunk for:
1. Any student-facing noise or backend trace.
2. Missing required fields in entries contained in this chunk.
3. Obvious answer/rubric/material incoherence visible from the text.
4. Any wording or structure issue that should block final delivery.
5. For AB handbook chunks, check whether 框架归位 and A-axis placement are visibly incoherent.

# Required Output
Return Chinese, compact:
- chunk_id: {doc_key}-{idx:02d}
- verdict: PASS / CONDITIONAL_PASS / FAIL for this chunk only
- BLOCKING defects: 无 if none
- NONBLOCKING issues: 无 if none
- Required local verification: 无 if none

# Chunk Content
BEGIN_CHUNK_CONTENT
{content}
END_CHUNK_CONTENT
"""


def clean_package_dir() -> None:
    if PACKAGE_DIR.exists():
        shutil.rmtree(PACKAGE_DIR)
    (PACKAGE_DIR / "outputs").mkdir(parents=True)
    (PACKAGE_DIR / "qa").mkdir()
    (PACKAGE_DIR / "gpt55_chunks").mkdir()


def copy_files() -> None:
    for path in OUTPUTS:
        shutil.copy2(path, PACKAGE_DIR / "outputs" / path.name)
    for path in QA_FILES:
        if path.exists():
            shutil.copy2(path, PACKAGE_DIR / "qa" / path.name)


def split_entries(text: str) -> list[str]:
    marker = "\n### "
    if marker not in text:
        return [text]
    pre, rest = text.split(marker, 1)
    parts = [pre.rstrip()]
    for block in rest.split(marker):
        parts.append("### " + block.strip())
    return [p for p in parts if p.strip()]


def hide_markdown_image_paths(text: str) -> str:
    return re.sub(
        r"!\[([^\]]*)\]\([^)]+\)",
        r"[图片已在 DOCX/PDF 中内嵌：\1]",
        text,
    )


def chunk_text(text: str, n: int = 3) -> list[str]:
    parts = split_entries(text)
    target = max(1, len(text) // n)
    chunks: list[list[str]] = [[] for _ in range(n)]
    ci = 0
    size = 0
    for part in parts:
        if ci < n - 1 and chunks[ci] and size + len(part) > target:
            ci += 1
            size = 0
        chunks[ci].append(part)
        size += len(part)
    return ["\n\n".join(c).strip() for c in chunks]


def write_gpt_chunks() -> None:
    out = PACKAGE_DIR / "gpt55_chunks"
    for doc_key, meta in DOCS.items():
        text = hide_markdown_image_paths(meta["path"].read_text(encoding="utf-8"))
        chunks = chunk_text(text, CHUNK_COUNT)
        for idx, content in enumerate(chunks, start=1):
            prompt = HEADER + TASK_TEMPLATE.format(
                doc_key=doc_key,
                doc_label=meta["label"],
                idx=idx,
                total=CHUNK_COUNT,
                content=content,
            )
            path = out / f"GPT55_CHUNK_PROMPT_{doc_key}_{idx:02d}_of_{CHUNK_COUNT}_{VERSION}.md"
            path.write_text(prompt, encoding="utf-8")
            print(path, len(prompt.encode("utf-8")))


def write_notes() -> None:
    chunk_lines = []
    item_no = 1
    for doc_key in ("compilation", "baodian"):
        for idx in range(1, CHUNK_COUNT + 1):
            chunk_lines.append(f"{item_no}. `GPT55_CHUNK_PROMPT_{doc_key}_{idx:02d}_of_{CHUNK_COUNT}_{VERSION}.md`")
            item_no += 1
    chunk_list = "\n".join(chunk_lines)

    readme = f"""# 选必二 {VERSION} 网页版/应用外审包

本包用于 Claude Opus 4.8 Max 和 GPT-5.5 Pro 网页版/应用复审。CLI 结果无效，不计入正式外审闭环。

## 内容

- `outputs/`: {VERSION} 两份学生稿 DOCX/MD。
- `qa/`: 本地 QA、渲染 QA、关键页截图/拼图、CLI 作废说明，以及 {VERSION} 渲染 PDF。
- `gpt55_chunks/`: GPT-5.5 Pro 分块审稿提示。图片路径已替换为“已内嵌”占位，避免网页审稿误判 Markdown 本地路径。
- `00_CLAUDE_OPUS48MAX_WEB_REVIEW_PROMPT.md`: Claude 网页/应用复审提示。
- `00_GPT55PRO_WEB_REVIEW_SEQUENCE.md`: GPT 网页/应用复审顺序。
"""
    (PACKAGE_DIR / "README_网页版应用外审包.md").write_text(readme, encoding="utf-8")

    sequence = f"""# GPT-5.5 Pro 网页版/应用正式终审顺序 {VERSION}

请在 ChatGPT 网页版或 ChatGPT 应用中选择 GPT-5.5 Pro。本次终审不得使用 `pro-cli` 或任何 CLI 结果；附件中的 `INVALID_CLI_EXTERNAL_REVIEW_NOTE_20260605.md` 仅说明旧 CLI 记录作废。

## 先上传/参考的文件

- `outputs/选必二法律与生活_试题细则汇编_学生可发版_{VERSION}.docx`
- `outputs/选必二法律与生活_试题细则汇编_学生可发版_{VERSION}.md`
- `outputs/选必二法律与生活_AB双轴学生宝典_学生可发版_{VERSION}.docx`
- `outputs/选必二法律与生活_AB双轴学生宝典_学生可发版_{VERSION}.md`
- `qa/TWO_DOC_CLEAN_DRAFT_QA_{VERSION}_{DATE}.md`
- `qa/RENDER_QA_{VERSION}_{DATE}.md`
- `qa/INVALID_CLI_EXTERNAL_REVIEW_NOTE_20260605.md`

## 分块终审

为避免一次性上下文过大，请依次提交 `gpt55_chunks/` 下 {CHUNK_COUNT * 2} 个分块提示：

{chunk_list}

每块返回后，请保留原文结果。若任一块出现 `FAIL` 或 BLOCKING defects，停止终审并回到 Codex 修稿。

## 所有分块都无阻断后提交最终综合提示

把所有分块结果一并给 GPT-5.5 Pro，并要求输出：

1. final_verdict: PASS / CONDITIONAL_PASS / FAIL。
2. 是否可以作为学生可发版交付: YES / NO。
3. 是否仍有 BLOCKING 必改项。
4. 是否仍需本地补图或教师裁决。
5. 若 PASS，请明确写出“无阻断缺陷，可交付”。
"""
    (PACKAGE_DIR / "00_GPT55PRO_WEB_REVIEW_SEQUENCE.md").write_text(sequence, encoding="utf-8")

    claude_prompt = f"""# Claude Opus 4.8 Max 网页版/应用复审提示 {VERSION}

请以 Claude Opus 4.8 Max 在网页版或桌面应用中复审本包，不要使用 CLI 结果。

用户只要两份学生可发文档：

1. `试题和细则汇编`: 2024-2026 选必二主观题，每题含题目来源、材料、设问、细则、答案落点、同题组。
2. `AB双轴学生宝典`: 按 AB 双轴框架组织，A 轴下有核心答题点/必备知识，再列相关主观题，同样保留题目来源、材料、设问、细则、答案落点、同题组。

请重点检查：

- 是否仍有后台/工程痕迹、source_id、entry_id、本机路径、制作记录、三十秒速记等学生不可见内容。
- 是否有题目材料、设问、细则、答案落点不一致或缺失。
- v9 GPT 网页审稿指出的四个阻断项是否已真正修复：东城二模19(1)、海淀一模19、西城一模18(3)、昌平二模20(1)。
- v10 GPT 网页审稿第三段指出的阻断项是否已真正修复：朝阳二模18、通州一模20、通州期末19(1)、朝阳期末18(1)。
- v11 Claude Opus 4.8 Max 网页/应用审稿指出的两个阻断项是否已真正修复：朝阳二模17 OCR/答案落点污染、房山二模18(1) A轴错位。
- v13 的非阻断 OCR 清理是否引入新问题：钱某是、建车棚、参考答案、尹某、低头看手机。监控画面、矛盾化解。
- v26 本地修复是否真正去掉答案落点中的题号/分值壳、`【细则】`和评分结构倒灌，同时保留正式细则原文中的分值。
- v23 GPT 网页第6块指出的 2025 海淀期末20 表格缺失/编辑残留、2025 海淀一模18答案落点细则化，是否已在 v26 修复。
- 2026 延庆一模18(1) 是否已从整段细则倒灌改成可用答案落点。
- 是否有图片替代文字不充分、裁切不清或学生无法使用的问题。
- 学生宝典的 A 轴归位是否明显错位，是否影响学生学习和迁移。

请输出：

1. verdict: PASS / CONDITIONAL_PASS / FAIL。
2. BLOCKING defects: 若无写“无”。
3. NONBLOCKING issues: 若无写“无”。
4. Required Codex local verification: 若无写“无”。
5. 是否可作为学生可发版: YES / NO。
"""
    (PACKAGE_DIR / "00_CLAUDE_OPUS48MAX_WEB_REVIEW_PROMPT.md").write_text(claude_prompt, encoding="utf-8")


def zip_dir(src: Path, dest: Path) -> None:
    if dest.exists():
        dest.unlink()
    with ZipFile(dest, "w", ZIP_DEFLATED) as zf:
        for path in sorted(src.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(src.parent))


def copy_to_desktop() -> None:
    if DESKTOP_DIR.exists():
        shutil.rmtree(DESKTOP_DIR)
    shutil.copytree(PACKAGE_DIR, DESKTOP_DIR)
    if DESKTOP_ZIP.exists():
        DESKTOP_ZIP.unlink()
    shutil.copy2(ZIP_PATH, DESKTOP_ZIP)


def main() -> None:
    clean_package_dir()
    copy_files()
    write_gpt_chunks()
    write_notes()
    zip_dir(PACKAGE_DIR, ZIP_PATH)
    copy_to_desktop()
    print(PACKAGE_DIR)
    print(ZIP_PATH)
    print(DESKTOP_DIR)
    print(DESKTOP_ZIP)


if __name__ == "__main__":
    main()
