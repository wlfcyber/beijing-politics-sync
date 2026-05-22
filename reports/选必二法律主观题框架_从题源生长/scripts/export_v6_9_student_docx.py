from pathlib import Path
import importlib.util

ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
base_path = ROOT / "scripts" / "export_v6_7_student_docx.py"

spec = importlib.util.spec_from_file_location("export_v6_7_student_docx", base_path)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)

module.MD = ROOT / "12_final_baodian" / "选必二法律主观题满分训练宝典_v6_9_恢复27核心完整学生使用版_20260521.md"
module.OUT = ROOT / "12_final_baodian" / "选必二法律主观题满分训练宝典_v6_9_恢复27核心完整学生使用版_20260521.docx"
module.REPORT = ROOT / "12_final_baodian" / "DOCX_EXPORT_V6_9_STUDENT_20260521.md"


def main() -> None:
    module.build()
    module.REPORT.write_text(
        "# V6.9 学生使用版 DOCX 导出报告\n\n"
        f"- 输入 Markdown：`{module.MD}`\n"
        f"- 输出 DOCX：`{module.OUT}`\n"
        "- 基于 V6.7 导出器复用样式。\n"
        "- V6.9 相对 V6.8 恢复缺失核心题18，确认 27 核心题均有 1-9 小节。\n"
        "- 后续仍需全页视觉 QA。\n",
        encoding="utf-8",
    )
    print(module.OUT)
    print(module.REPORT)


if __name__ == "__main__":
    main()
