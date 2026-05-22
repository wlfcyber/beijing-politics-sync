#!/usr/bin/env python3
"""Create guarded framework_v2 documents from framework_v1_2 artifacts."""

from __future__ import annotations

import csv
import shutil
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
FRAMEWORK = ROOT / "09_candidate_frameworks" / "framework_v1_2_guarded.md"
MAP = ROOT / "09_candidate_frameworks" / "framework_v1_2_evidence_map.csv"
TEST = ROOT / "10_framework_validation" / "framework_v1_2_question_by_question_test_20260519.csv"
PASS_REPORT = ROOT / "10_framework_validation" / "framework_v1_2_pass_report_20260519.md"
PARTIAL_POLICY = ROOT / "10_framework_validation" / "framework_v1_2_partial_policy_20260519.csv"

OUT_DIR = ROOT / "11_final_framework"
OUT_FRAMEWORK = OUT_DIR / "framework_v2.md"
OUT_MAP = OUT_DIR / "framework_v2_evidence_map.csv"
OUT_STUDENT = OUT_DIR / "framework_v2_student_one_page.md"
OUT_TEACHER = OUT_DIR / "framework_v2_teacher_guide.md"
OUT_VALIDATION = OUT_DIR / "framework_v2_validation_summary.md"


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader.fieldnames or []), list(reader)


def counts() -> dict[str, int]:
    _, rows = read_csv(TEST)
    pass_rows = [row for row in rows if row["pass_status"] == "PASS"]
    boundary = [row for row in pass_rows if row["framework_entry_node"].startswith("FWV1_2_GATE")]
    partial = [row for row in rows if row["pass_status"] == "PARTIAL"]
    return {
        "total": len(rows),
        "pass": len(pass_rows),
        "core_pass": len(pass_rows) - len(boundary),
        "boundary_pass": len(boundary),
        "partial": len(partial),
        "fail": len([row for row in rows if row["pass_status"] == "FAIL"]),
    }


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(MAP, OUT_MAP)

    c = counts()
    framework_body = FRAMEWORK.read_text(encoding="utf-8")
    framework_body = framework_body.replace(
        "# Framework v1.2 Guarded - 选必二法律主观题启动框架",
        "## Guarded Node Body",
        1,
    )
    header = [
        "# Framework v2 - 选必二《法律与生活》主观题守门框架",
        "",
        "Status: guarded framework. It is ready for teaching the core path, but handbook examples must keep open/reference/boundary labels.",
        "",
        "## Validation Position",
        "",
        f"- corpus: {c['total']} questions",
        "- evidence: 61 formal, 4 reference_only, 0 missing",
        f"- v1.2 pressure: PASS {c['pass']} = core/pass {c['core_pass']} + boundary-gate pass {c['boundary_pass']}; PARTIAL {c['partial']}; FAIL {c['fail']}",
        "- rule: boundary pass is not a selected-compulsory-2 full-score template; PARTIAL rows cannot support new nodes.",
        "",
    ]
    OUT_FRAMEWORK.write_text("\n".join(header) + "\n" + framework_body, encoding="utf-8")

    student = [
        "# Framework v2 Student One Page",
        "",
        "## 先问一句",
        "",
        "这题是不是在处理私人法律关系、权利义务、责任承担或维权程序？如果主语是国家治理、涉外法治建设、依法行政，先别套选必二。",
        "",
        "## 六个入口",
        "",
        "1. 表格题：一格一答，先判断格子要什么。",
        "2. 评析题：先表态，再写法律依据和材料事实。",
        "3. 案例理由题：定性 -> 规则 -> 材料事实 -> 责任/结果。",
        "4. 裁判题：先写以事实为根据、以法律为准绳，再落具体法律规则。",
        "5. 维权建议题：程序路径 + 准备事项 + 实体请求。",
        "6. 意义题：个人合法权益 -> 司法/行业秩序 -> 公平正义或核心价值观。",
        "",
        "## 材料翻译",
        "",
        "- 看到付款、出票、承诺：翻译成合同成立。",
        "- 看到欺诈、隐瞒、搭售：翻译成违背真实意思或消费者权益受侵害。",
        "- 看到损害、过错、因果：翻译成侵权责任判断。",
        "- 看到协商未果、起诉、证据：翻译成程序路径和准备。",
        "- 看到典型案例/意义：先问受益主体是谁，别空写法治口号。",
        "",
        "## 禁止",
        "",
        "- 不把必修三法治建设话术当选必二答案。",
        "- 不写法考式大段构成要件。",
        "- 不用参考答案题支撑核心模板。",
        "- 不把开放容器题当已经稳定的满分套路。",
        "",
    ]
    OUT_STUDENT.write_text("\n".join(student), encoding="utf-8")

    teacher = [
        "# Framework v2 Teacher Guide",
        "",
        "## 讲法",
        "",
        "这套框架不是教材目录，而是从评分细则里抽出的启动顺序。课堂上先训练学生识别设问入口，再训练把材料事实翻译成法律语言，最后训练按细则顺序写句。",
        "",
        "## 核心节点",
        "",
        "- 表格一格一答：格子之间不要串答案。",
        "- 评析先表态：表态缺失会直接丢分。",
        "- 私法案例四链：定性、规则、材料、责任。",
        "- 裁判锚句：判决/裁判理由题先写事实与法律锚句。",
        "- 维权三层：程序、准备、实体请求。",
        "- 意义收束：法律规则推出的权益、秩序、价值。",
        "",
        "## 边界",
        "",
        "`CC0276_2026_房山_二模_17` 与 `RECOVER_2026_西城_二模_18_3` 是 formal，但不进选必二核心。它们用于告诉学生：不是所有带法治、法律、权利、责任的题都能套本框架。",
        "",
        "## 开放容器",
        "",
        "`RECOVER_2026_西城_二模_18_2` 与 `CC0380_2026_顺义_二模_18_2` 暂留 AI 责任/智能体法律风险开放容器。可讲，可压测，但不能当稳定核心节点。",
        "",
        "## 证据纪律",
        "",
        "- 核心节点必须来自 formal 或经过确认的细则原子。",
        "- reference_only 只做弱示范。",
        "- open-container 只做压测和储备。",
        "- 教学反思不是评分细则，不能冒充得分点。",
        "",
    ]
    OUT_TEACHER.write_text("\n".join(teacher), encoding="utf-8")

    partial_fields, partial_rows = read_csv(PARTIAL_POLICY)
    partial_summary = "\n".join(
        f"- {row['question_id']}: {row['partial_policy']}"
        for row in partial_rows
    )
    validation = [
        "# Framework v2 Validation Summary",
        "",
        PASS_REPORT.read_text(encoding="utf-8"),
        "",
        "## Remaining PARTIAL Policy",
        "",
        partial_summary,
        "",
        "## Acceptance",
        "",
        "Framework v2 may be used as the guarded teaching framework for the current 65-question corpus. The final baodian must preserve labels for PARTIAL/open/reference/boundary rows and must not claim those rows are core full-score closures.",
        "",
    ]
    OUT_VALIDATION.write_text("\n".join(validation), encoding="utf-8")

    print(f"Wrote {OUT_FRAMEWORK}")
    print(f"Wrote {OUT_STUDENT}")
    print(f"Wrote {OUT_TEACHER}")
    print(f"Wrote {OUT_VALIDATION}")


if __name__ == "__main__":
    main()
