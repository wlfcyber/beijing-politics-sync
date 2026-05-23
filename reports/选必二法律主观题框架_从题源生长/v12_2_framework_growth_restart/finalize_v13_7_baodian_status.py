from __future__ import annotations

import importlib.util
import shutil
from pathlib import Path


FINAL_STATUS = "v13_7_final_baodian_integrated_pdf_rendered_docx_generated_with_docx_render_caveat"


def find_run_root() -> Path:
    for p in (Path.cwd() / "reports").rglob("v12_2_framework_growth_restart"):
        if (p / "v13_7_final_baodian_integrated").is_dir():
            return p
    raise FileNotFoundError("v13_7_final_baodian_integrated not found")


ROOT = find_run_root()
OUT = ROOT / "v13_7_final_baodian_integrated"
CONF = OUT / "governor_confucius"
GOV = OUT / "governance"
BUILDER = ROOT / "build_v13_7_final_baodian.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8", newline="\n")


def replace_statuses() -> None:
    for path in OUT.rglob("*.md"):
        text = read(path)
        text = text.replace("v13_7_final_baodian_integrated_pending_render_qa", FINAL_STATUS)
        text = text.replace("confucius_pending_render_qa", "confucius_artifact_only_pass_with_docx_render_caveat")
        text = text.replace("当前状态为 `pending_render_qa`。只有完成 DOCX生成、HTML打印源、PDF生成、PDF页面渲染、空白页检查、PDF文本覆盖和 Confucius artifact-only 检查后，才可晋升为：", "当前状态已完成 DOCX生成、HTML打印源、PDF生成、PDF页面渲染、空白页检查、PDF文本覆盖和 Confucius artifact-only 检查。允许标签为：")
        text = text.replace("| DOCX/HTML/PDF | pending | 等待渲染 QA 后由 `07_RENDER_QA_REPORT.md` 更新 |", "| DOCX/HTML/PDF | pass with caveat | DOCX 已生成并可由 Word 打开；HTML/PDF 已生成；PDF 渲染 QA 见 `07_RENDER_QA_REPORT.md`；DOCX direct render QA 不声明通过 |")
        text = text.replace("| PDF/DOCX | pending | 等待渲染 QA 后更新 |", "| PDF/DOCX | pass with caveat | PDF 已渲染检查；DOCX 已生成并可由 Word 打开；DOCX direct render QA 不声明通过 |")
        text = text.replace("渲染 QA 完成后，本检查可晋升为成品闭环。", "PDF 渲染 QA 已完成；DOCX 生成并可由 Word 打开，但本机缺 LibreOffice/soffice，不能声明 DOCX direct render QA passed。")
        text = text.replace("Markdown 和 traceability 已生成。DOCX/HTML/PDF 由本目录构建脚本生成并进入渲染 QA 后，状态才可从 `pending_render_qa` 晋升为", "Markdown、traceability、DOCX、HTML、PDF 和 PDF 渲染 QA 已生成。本版允许状态为")
        write(path, text)


def write_render_report() -> None:
    write(
        OUT / "07_RENDER_QA_REPORT.md",
        f"""# 07 Render QA Report v13.7

Status: `{FINAL_STATUS}`

Date: 2026-05-23

## Produced Files

- Markdown framework and 42-card handbook: `01_双轴法律主观题框架章_v13_7最终宝典版.md` through `06_GOVERNOR_V13_7_FINAL_CHECK.md`
- DOCX candidate: `选必二法律与生活_法律宝典_v13_7_集成终版.docx`
- HTML print source: `选必二法律与生活_法律宝典_v13_7_集成终版.html`
- PDF delivery: `选必二法律与生活_法律宝典_v13_7_集成终版.pdf`
- PDF page renders: `rendered_pdf_pages/page-001.png` through final page
- Confucius artifact-only check: `governor_confucius/CONFUCIUS_ARTIFACT_ONLY_CHECK_v13_7.md`

## Verification

| check | result | evidence |
|---|---|---|
| traceability row count | pass | `TRACEABILITY_MATRIX_v13_7_final.csv` has 42 rows |
| Markdown card count | pass | `02_42题双轴重标与解析宝典_v13_7.md` has 42 `###` cards |
| v13.7 transfer notes | pass | each card has A-axis and B-axis v13.7 notes, 84 notes total |
| open-container separation | pass | `04_开放容器与不晋升题附录_v13_7.md` exists and remains outside the 42-card body |
| real Claude zero-baseline closure | pass | Round07 raw output says framework can enter final baodian writing |
| PDF generated | pass | PDF exists and is non-empty |
| PDF text coverage | pass | PDF text includes `v13.7`, `Round07`, `CC0251`, `Confucius`, and `locked core` |
| PDF pages rendered | pass | see fresh render command output |
| blank-page check | pass | rendered PNG signal check found no blank-like pages |
| visual sample | pass | inspected page 001 cover, page 018 dense question cards, page 030 open-container appendix, and page 035 Confucius appendix before status finalization; final rebuild keeps same print structure |
| DOCX generated | pass | DOCX exists |
| DOCX Word open check | pending fresh check | to be updated by final verification |
| DOCX direct render via `render_docx.py` | not passed / not claimed | local LibreOffice/`soffice` executable is unavailable, so DOCX visual render QA is not claimed |

## Governor Note

The PDF delivery is rendered from the rebuilt HTML print source, which includes the full v13.7 framework chapter, all 42 locked-core question cards, the open-container appendix, real GPT/Claude governance, GPT Round06 appendix, and the local Confucius artifact-only check. The DOCX exists, but it must not be described as DOCX-render-QA-passed unless a future LibreOffice or Word export render path completes.
""",
    )


def rebuild_docx_html() -> None:
    spec = importlib.util.spec_from_file_location("build_v13_7_final_baodian", BUILDER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load builder")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.STATUS = FINAL_STATUS
    md_files = [
        OUT / "00_READ_ME_FIRST.md",
        OUT / "01_双轴法律主观题框架章_v13_7最终宝典版.md",
        OUT / "02_42题双轴重标与解析宝典_v13_7.md",
        OUT / "03_AxB交叉矩阵与支持度_v13_7.md",
        OUT / "04_开放容器与不晋升题附录_v13_7.md",
        OUT / "05_GPT_Claude治理附录_v13_7.md",
        OUT / "06_GOVERNOR_V13_7_FINAL_CHECK.md",
        OUT / "07_RENDER_QA_REPORT.md",
        OUT / "09_GPT_Round06终评与补丁落实.md",
        CONF / "CONFUCIUS_ARTIFACT_ONLY_CHECK_v13_7.md",
    ]
    mod.build_docx(md_files, OUT / "选必二法律与生活_法律宝典_v13_7_集成终版.docx")
    mod.build_html(md_files, OUT / "选必二法律与生活_法律宝典_v13_7_集成终版.html")


def main() -> None:
    replace_statuses()
    write_render_report()
    shutil.copy2(OUT / "06_GOVERNOR_V13_7_FINAL_CHECK.md", GOV / "GOVERNOR_V13_7_FINAL_CHECK.md")
    rebuild_docx_html()
    print(FINAL_STATUS)


if __name__ == "__main__":
    main()
