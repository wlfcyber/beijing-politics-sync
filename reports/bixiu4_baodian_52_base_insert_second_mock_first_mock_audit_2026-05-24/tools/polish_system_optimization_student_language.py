from __future__ import annotations

import json
import shutil
from datetime import datetime
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
ACCEPTED = RUN_DIR / "04_fusion_audit" / "student_patch_entries.accepted.jsonl"
REPORT = RUN_DIR / "04_fusion_audit" / "system_optimization_language_polish_20260524.md"

WHY_REWRITES = {
    3: "多个场景、任务和资源不是孤立堆放，而是在同一育人目标下相互配合，适合从整体与部分、系统优化的角度分析。只有把课程目标、空间资源、实践任务和数字技术放在同一系统中看，才能说明各部分为什么要协同发力、服务铸魂育人的整体效果。",
    11: "数字中国、健康中国、平安中国、美丽中国不是四件互不相干的任务，而是同一现代化进程中的有机组成部分。材料强调相互支撑、协同发力，就要求从系统优化角度把握整体目标与各战略支柱的关系，说明各部分优化组合才能提升现代化建设的整体效能。",
    15: "“湖内问题湖外解决”“治湖泊转向治流域”说明湿地治理不能只盯住单个湖泊，而要把湖泊、流域、森林、村寨、梯田、水系等要素作为相互影响的系统来把握。用系统优化看，关键在于统筹各环节、优化治理结构，让局部修复服务生态整体稳定。",
    19: "从古代分工体系到新时代完整工业门类，材料强调的不是某一项孤立技艺，而是长期积累、分工协同和体系化制造能力。系统优化角度能够解释：只有把工匠、技术、门类、产业链和国家能力作为整体来统筹，才能形成持续创造的整体优势。",
    22: "全面深化改革和中国式现代化都是复杂系统工程，不能用单点推进替代整体统筹。系统观念要求从整体性、关联性、协同性出发，把不同领域、不同环节、不同举措放在统一目标下协调推进，避免局部政策彼此脱节，形成整体优化效能。",
}

FIELD_REPLACEMENTS = {
    "看到'有字之书'与'无字之书'并列": "看到“有字之书”与“无字之书”并列",
    "题目关键词就是'关联'": "题目关键词就是“关联”",
    "看不到'起点'与'目标'之间": "看不到“起点”与“目标”之间",
}


def main() -> None:
    rows = [json.loads(line) for line in ACCEPTED.read_text(encoding="utf-8").splitlines() if line.strip()]
    backup = ACCEPTED.with_name(
        f"{ACCEPTED.stem}.backup_before_system_language_polish_{datetime.now():%Y%m%d_%H%M%S}.jsonl"
    )
    shutil.copy2(ACCEPTED, backup)

    applied: list[str] = []
    for row_id, why in WHY_REWRITES.items():
        row = rows[row_id - 1]
        row["why_trigger"] = why
        applied.append(f"- row {row_id}: rewrote system-optimization why_trigger for {row.get('source_suite')} {row.get('question_no')}.")

    for row in rows:
        for field in ("material_trigger", "question_prompt", "why_trigger", "answer_landing"):
            value = row.get(field)
            if not isinstance(value, str):
                continue
            for old, new in FIELD_REPLACEMENTS.items():
                value = value.replace(old, new)
            row[field] = value

    ACCEPTED.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n",
        encoding="utf-8",
    )

    REPORT.write_text(
        "# System optimization student-language polish\n\n"
        f"- accepted jsonl: `{ACCEPTED}`\n"
        f"- backup: `{backup}`\n\n"
        + "\n".join(applied)
        + "\n",
        encoding="utf-8",
    )
    print(f"applied={len(applied)}")
    print(f"backup={backup}")
    print(f"report={REPORT}")


if __name__ == "__main__":
    main()
