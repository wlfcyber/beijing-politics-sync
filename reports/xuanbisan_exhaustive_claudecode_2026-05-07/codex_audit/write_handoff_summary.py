import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
DELIVERY = RUN_DIR / "delivery"
OUT = RUN_DIR / "HANDOFF_README.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    student_qa = load_json(DELIVERY / "STUDENT_DELIVERY_QA.json")
    governor = load_json(RUN_DIR / "governor_confucius" / "GOVERNOR_CONFUCIUS_PRECHECK.json")
    p2 = load_json(RUN_DIR / "claudecode_lane" / "p2_recheck" / "P2_RECHECK_QA.json")
    p2_fusion = load_json(RUN_DIR / "fusion" / "framework_first_fusion" / "P2_FUSION_PATCH_QA.json")
    overall = load_json(RUN_DIR / "fusion" / "overall_batch_closure" / "OVERALL_COVERAGE_AUDIT.json")

    rendered_dir = DELIVERY / "rendered_docx_pages"
    rendered_pages = len(list(rendered_dir.glob("*.png"))) if rendered_dir.exists() else 0
    files = list(RUN_DIR.rglob("*"))
    file_count = sum(1 for p in files if p.is_file())
    size_mb = round(sum(p.stat().st_size for p in files if p.is_file()) / (1024 * 1024), 2)

    lines = [
        "# 选必三二线闭合交接说明",
        "",
        "## 最重要文件",
        "",
        "- `delivery/选必三_逻辑与思维_学生版_框架闭合稿.md`",
        "- `delivery/选必三_逻辑与思维_学生版_框架闭合稿.docx`",
        "- `delivery/STUDENT_DELIVERY_QA.md`",
        "- `governor_confucius/GOVERNOR_CONFUCIUS_PRECHECK.md`",
        "- `fusion/framework_first_fusion/FRAMEWORK_FIRST_FUSION_P2_PATCHED.md`",
        "",
        "## 当前结论",
        "",
        f"- overall coverage: `{overall.get('verdict')}`",
        f"- P2 total QA: `{p2.get('verdict')}`",
        f"- P2 fusion QA: `{p2_fusion.get('verdict')}`",
        f"- Governor: `{governor.get('governor_verdict')}`",
        f"- student delivery QA: `{student_qa.get('verdict')}`",
        f"- student entries kept/skipped: `{student_qa.get('kept_entries')}` / `{student_qa.get('skipped_entries')}`",
        f"- rendered DOCX pages: `{rendered_pages}`",
        "- PDF: not included; Word COM export timed out, DOCX and rendered PNG QA are included.",
        "",
        "## 边界",
        "",
        "- 本次是用户明确要求二线闭合后的本地交付与 GitHub 同步。",
        "- 未启动四线终极版；未调用 GPT/Claude 网页外审。",
        "- 学生版已去掉内部审计路径、证据等级、P0/P1/P2 证据行、source_insufficient 与不入正文条目。",
        "",
        "## 目录体积",
        "",
        f"- files: `{file_count}`",
        f"- size MB: `{size_mb}`",
    ]
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(str(OUT))


if __name__ == "__main__":
    main()
