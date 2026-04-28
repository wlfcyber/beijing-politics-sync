from __future__ import annotations

import argparse
import csv
from datetime import datetime
from pathlib import Path


def slugify(text: str) -> str:
    keep = []
    for ch in text.strip():
        if ch.isalnum() or "\u4e00" <= ch <= "\u9fff":
            keep.append(ch)
        elif ch in "-_":
            keep.append(ch)
        else:
            keep.append("_")
    slug = "".join(keep).strip("_")
    return slug or "book"


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def write_csv(path: Path, headers: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        csv.writer(f).writerow(headers)


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize a Beijing politics book/module workflow run directory.")
    parser.add_argument("--book", required=True, help="Book/module name, e.g. 经济与社会")
    parser.add_argument("--root", default=None, help="Research root where reports/ will be created. Defaults to Desktop/飞哥的政治庄园")
    parser.add_argument("--project-name", default=None, help="Project folder name. Defaults to 飞哥的政治庄园")
    parser.add_argument("--run-name", default=None, help="Optional run directory name")
    parser.add_argument("--source-root", action="append", default=[], help="Corpus source root; can be repeated")
    parser.add_argument("--deliverable", action="append", default=[], help="Expected deliverable; can be repeated")
    args = parser.parse_args()

    project_name = args.project_name or "飞哥的政治庄园"
    root = Path(args.root).expanduser().resolve() if args.root else (Path.home() / "Desktop" / project_name).resolve()
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    run_name = args.run_name or f"{slugify(args.book)}_{stamp}"
    run_dir = root / "reports" / run_name
    run_dir.mkdir(parents=True, exist_ok=True)
    (root / "threads").mkdir(parents=True, exist_ok=True)
    (root / "artifacts").mkdir(parents=True, exist_ok=True)
    (root / "sources").mkdir(parents=True, exist_ok=True)

    source_roots = args.source_root or [
        r"C:\Users\Administrator\Desktop\2024各区模拟题",
        r"C:\Users\Administrator\Desktop\2025各区模拟题",
        r"C:\Users\Administrator\Desktop\2026各区模拟题",
    ]
    deliverables = args.deliverable or [
        f"{args.book}材料-知识触发总框架",
        f"{args.book}选择题错肢/易错项总结",
        f"{args.book}最终验收报告",
    ]

    write_text(
        run_dir / "TASK_BRIEF.md",
        "# Task Brief\n\n"
        f"- Project: {project_name}\n"
        f"- Book/module: {args.book}\n"
        "- User goal: fill after reading the latest user request.\n"
        "- Source roots:\n"
        + "".join(f"  - `{p}`\n" for p in source_roots)
        + "- Deliverables:\n"
        + "".join(f"  - {d}\n" for d in deliverables)
        + "\n## Evidence Rules\n\n"
        "- Main-question entries require rubric/marking report/lecture scoring/user-confirmed scoring source.\n"
        "- Reference answers are not scoring rubrics.\n"
        "- Choice-question analysis requires reliable objective answer keys.\n"
        "- Every entry needs source suite, question number, and logic chain.\n",
    )

    write_text(
        run_dir / "USER_FRAMEWORK.md",
        "# User Framework\n\nPaste or summarize the user's framework here before processing. Do not replace it with a generic outline.\n",
    )

    steps = [
        "STEP_01: preserve user framework and scope",
        "STEP_02: inventory local and approved external sources",
        "STEP_03: classify every suite/question in coverage matrix",
        "STEP_04: process main-question scoring chains",
        "STEP_05: process choice-question answer keys and wrong-option patterns",
        "STEP_06: merge confirmed findings into cumulative artifacts",
        "STEP_07: run patcher review for one-material-many-points omissions",
        "STEP_08: run governor review and blocker escalation",
        "STEP_09: generate requested deliverables",
        "STEP_10: render/validate deliverables",
        "STEP_11: write final acceptance report",
    ]
    write_text(run_dir / "DEVELOPMENT_PLAN.md", "# Development Plan\n\n" + "\n".join(f"- [ ] {s}" for s in steps) + "\n")
    write_text(run_dir / "PROGRESS.md", "# Progress\n\n" + "\n".join(f"- [ ] {s}" for s in steps) + "\n")

    write_text(
        run_dir / "ROLE_CONTRACTS.md",
        "# Role Contracts\n\n"
        "- 决策者: choose next bottleneck; write directives.\n"
        "- 资料组织者: inventory sources; update source ledger.\n"
        "- 劳动者: process assigned suites/questions; write findings only unless assigned a write scope.\n"
        "- 补丁者: check missed multi-point and cross-framework placements after merge.\n"
        "- 监管者: veto weak evidence, hidden blockers, and fake completion.\n"
        "- 自动化检测者: verify plan/progress/artifacts/render outputs agree; main thread owns this if no subagent slot.\n\n"
        "Each role report ends with `Decision: pass/fail/blocked/needs-merge`.\n",
    )

    write_text(
        root / "PROJECT_MANIFEST.md",
        "# Project Manifest\n\n"
        f"- Project: {project_name}\n"
        f"- Book/module: {args.book}\n"
        f"- Created: {stamp}\n"
        f"- Active run: `reports/{run_name}`\n\n"
        "## Folder Contract\n\n"
        "- `reports/`: run control files and QA reports.\n"
        "- `threads/`: role-thread reports or exported thread notes.\n"
        "- `artifacts/`: cumulative book/module outputs.\n"
        "- `sources/`: project-local source copies or indexes when needed.\n",
    )

    write_text(
        run_dir / "THREAD_REGISTRY.md",
        "# Thread Registry\n\n"
        "| Role | Agent/Thread ID | Assignment | Write scope | Status | Last report |\n"
        "| --- | --- | --- | --- | --- | --- |\n"
        "| 自动化检测者 | main thread | plan/progress/artifact/render consistency | control files only | active | this run directory |\n\n"
        "If independent threads are not available, record `not spawned: reason` in Agent/Thread ID and keep the role's report on disk.\n",
    )

    write_text(
        run_dir / "ROLE_THREAD_PROMPTS.md",
        "# Role Thread Prompts\n\n"
        "Use these prompts if opening visible role threads manually in the app.\n\n"
        "## 决策者\n\n"
        f"你是《{args.book}》研究任务的决策者。只读项目控制台和已有报告，决定下一步瓶颈。输出到 `threads/decision_maker_findings.md`，不要修改 artifacts。结尾写 Decision: pass/fail/blocked/needs-merge。\n\n"
        "## 资料组织者\n\n"
        f"你是《{args.book}》研究任务的资料组织者。盘点试卷、答案、细则、评标、讲评、zip/重复源，更新建议写入报告，不直接删改源文件。输出到 `threads/organizer_findings.md`。\n\n"
        "## 劳动者\n\n"
        f"你是《{args.book}》研究任务的劳动者。按分配套卷/题号处理，必须给来源、题号、证据类型、材料、触发链。只写 findings，不改 shared artifacts。\n\n"
        "## 补丁者\n\n"
        "你是补丁者。检查一个材料对应多个答题点、跨模块漏收、框架只落一处的问题。必须在主线程合并后复查。\n\n"
        "## 监管者\n\n"
        "你是监管者。按证据规则和 coverage matrix 审核。发现普通参考答案冒充细则、未分类题目、隐藏 blocker、Word 未渲染等情况必须 veto。\n",
    )

    write_csv(run_dir / "SOURCE_LEDGER.csv", ["suite_id", "year", "district", "stage", "file_path", "file_type", "source_type", "question_range", "status", "notes"])
    write_csv(run_dir / "COVERAGE_MATRIX.csv", ["suite_id", "question", "book_module", "question_type", "evidence_source", "status", "artifact_location", "decision_reason", "next_action"])

    write_text(run_dir / "DECISION_LOG.md", "# Decision Log\n\n")
    write_text(run_dir / "HANDOFF_QUEUE.md", "# Handoff Queue\n\n- On resume, read TASK_BRIEF, USER_FRAMEWORK, DEVELOPMENT_PLAN, PROGRESS, SOURCE_LEDGER, COVERAGE_MATRIX, and this file before acting.\n")
    write_text(
        run_dir / "GOVERNOR_CHECKLIST.md",
        "# Governor Checklist\n\n"
        "- [ ] No relevant suite/question remains unclassified.\n"
        "- [ ] Every main-question entry has a scoring source.\n"
        "- [ ] Every choice-question entry has a reliable answer key.\n"
        "- [ ] Every merged entry has source suite, question number, and logic chain.\n"
        "- [ ] Exclusions and blockers are explicitly labeled.\n"
        "- [ ] Role blockers received one escalation pass.\n"
        "- [ ] Deliverables were rendered/validated when applicable.\n",
    )
    write_text(
        run_dir / "FINAL_ACCEPTANCE_REPORT.md",
        "# Final Acceptance Report\n\nDo not write TASK_COMPLETE until all gates pass.\n",
    )

    print(run_dir)


if __name__ == "__main__":
    main()
