from __future__ import annotations

import argparse
import csv
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import re


DEFAULT_SOURCE_ROOTS = [
    Path(r"C:\Users\Administrator\Desktop\2025各区模拟题"),
    Path(r"C:\Users\Administrator\Desktop\2026各区模拟题"),
]
DEFAULT_PROJECT_ROOT = Path(r"C:\Users\Administrator\Desktop\beijing_politics_research")

DISTRICTS = [
    "东城",
    "西城",
    "朝阳",
    "海淀",
    "丰台",
    "石景山",
    "门头沟",
    "房山",
    "通州",
    "顺义",
    "昌平",
    "大兴",
    "怀柔",
    "平谷",
    "密云",
    "延庆",
    "燕山",
    "经开",
]

STAGE_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"一模|首模|第一次模拟"), "一模"),
    (re.compile(r"二模|第二次模拟"), "二模"),
    (re.compile(r"三模|第三次模拟"), "三模"),
    (re.compile(r"期中"), "期中"),
    (re.compile(r"期末"), "期末"),
]

CANONICAL_RUBRIC_HINTS = (
    "细则",
    "评分细则",
    "评分标准",
    "评标",
    "阅卷细则",
    "参考答案及评标细则",
    "答案细则",
    "参考答案",
)
REPORT_HINTS = ("报告", "总结", "实录")
LECTURE_HINTS = ("讲评", "研修")
NOISE_HINTS = ("扫描全能王", "chat_file", "勿传")
FULL_HINTS = ("全", "完整", "定稿", "最终", "新")
PAPER_HINTS = ("教师版", "试卷", "政治", "高三")


@dataclass
class SuiteFile:
    path: Path
    file_kind: str
    score: int
    reason: str


def detect_year(text: str) -> str:
    match = re.search(r"(20\d{2})", text)
    return match.group(1) if match else ""


def detect_stage(text: str) -> str:
    for pattern, stage in STAGE_PATTERNS:
        if pattern.search(text):
            return stage
    return ""


def detect_district(text: str) -> str:
    for district in DISTRICTS:
        if district in text:
            return district
    return ""


def classify_file(path: Path) -> SuiteFile:
    name = path.name
    suffix = path.suffix.lower()
    score = 0
    reasons: list[str] = []

    rubric_hits = [hint for hint in CANONICAL_RUBRIC_HINTS if hint in name]
    report_hits = [hint for hint in REPORT_HINTS if hint in name]
    lecture_hits = [hint for hint in LECTURE_HINTS if hint in name]
    noise_hits = [hint for hint in NOISE_HINTS if hint in name]
    full_hits = [hint for hint in FULL_HINTS if hint in name]
    paper_hits = [hint for hint in PAPER_HINTS if hint in name]

    if suffix in {".doc", ".docx", ".pdf", ".ppt", ".pptx"}:
        score += 5
    if rubric_hits:
        score += 35 + 5 * len(rubric_hits)
        reasons.append(f"rubric={','.join(rubric_hits)}")
    if full_hits:
        score += 12
        reasons.append(f"full={','.join(full_hits)}")
    if suffix in {".doc", ".docx", ".pdf"}:
        score += 8
        reasons.append("portable_or_editable")
    if suffix in {".ppt", ".pptx"}:
        score -= 8
        reasons.append("slide_penalty")
    if report_hits:
        score -= 28
        reasons.append(f"report={','.join(report_hits)}")
    if lecture_hits:
        score -= 24
        reasons.append(f"lecture={','.join(lecture_hits)}")
    if noise_hits:
        score -= 20
        reasons.append(f"noise={','.join(noise_hits)}")

    if rubric_hits and score >= 25:
        file_kind = "rubric_candidate"
    elif any(hint in name for hint in PAPER_HINTS) and not rubric_hits:
        file_kind = "paper_candidate"
        score += 10
        reasons.append(f"paper={','.join(paper_hits)}")
    elif report_hits:
        file_kind = "report_like"
    elif lecture_hits or suffix in {".ppt", ".pptx"}:
        file_kind = "lecture_like"
    else:
        file_kind = "other"

    return SuiteFile(path=path, file_kind=file_kind, score=score, reason="; ".join(reasons) or "no_strong_signal")


def suite_directories(source_root: Path) -> list[Path]:
    suites: list[Path] = []
    if not source_root.exists():
        return suites
    for path in source_root.rglob("*"):
        if path.is_dir():
            files = [child for child in path.iterdir() if child.is_file()]
            subdirs = [child for child in path.iterdir() if child.is_dir()]
            if files and not subdirs:
                suites.append(path)
    return sorted(suites)


def relative_under(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def ensure_state_files(project_root: Path) -> None:
    book_registry = project_root / "data" / "knowledge" / "book_method_registry.md"
    master_summary = project_root / "data" / "knowledge" / "master_rubric_summary.md"
    governor_board = project_root / "data" / "reports" / "governor_board.md"

    if not book_registry.exists():
        ensure_parent(book_registry)
        book_registry.write_text(
            "\n".join(
                [
                    "# Book Method Registry",
                    "",
                    "Use this file to track the user's seven-book methods and the leader's decomposition.",
                    "",
                    "## 中国特色社会主义",
                    "- 用户方法: pending",
                    "- 阶段拆解: pending",
                    "",
                    "## 经济与社会",
                    "- 用户方法: pending",
                    "- 阶段拆解: pending",
                    "",
                    "## 政治与法治",
                    "- 用户方法: pending",
                    "- 阶段拆解: pending",
                    "",
                    "## 哲学与文化",
                    "- 用户方法: pending",
                    "- 阶段拆解: pending",
                    "",
                    "## 法律与生活",
                    "- 用户方法: pending",
                    "- 阶段拆解: pending",
                    "",
                    "## 逻辑与思维",
                    "- 用户方法: pending",
                    "- 阶段拆解: pending",
                    "",
                    "## 当代国际政治与经济",
                    "- 用户方法: pending",
                    "- 阶段拆解: pending",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

    if not master_summary.exists():
        ensure_parent(master_summary)
        master_summary.write_text(
            "\n".join(
                [
                    "# Master Rubric Summary",
                    "",
                    "Append-forward cumulative summary. Do not overwrite valid old structure.",
                    "",
                    "## New This Run",
                    "- pending",
                    "",
                    "## By Book",
                    "- pending",
                    "",
                    "## By Trigger Pattern",
                    "- pending",
                    "",
                    "## By Logic Chain",
                    "- pending",
                    "",
                    "## Unresolved",
                    "- pending",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

    if not governor_board.exists():
        ensure_parent(governor_board)
        governor_board.write_text(
            "\n".join(
                [
                    "# Governor Board",
                    "",
                    "## Current Status",
                    "- organizer: pending",
                    "- mapper: pending",
                    "- summarizer: pending",
                    "- governor_decision: pending",
                    "",
                    "## Failures To Rerun",
                    "- pending",
                    "",
                    "## Remaining Blockers",
                    "- pending",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )


def cleanup_destination(project_root: Path, file_path: Path, source_root: Path) -> Path:
    stamp = datetime.now().strftime("%Y%m%d")
    archive_root = project_root / "data" / "archive" / "temp_cleanup" / stamp
    relative = file_path.resolve().relative_to(source_root.resolve())
    return archive_root / source_root.name / relative


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare the Beijing politics analyst workspace.")
    parser.add_argument("--project-root", type=Path, default=DEFAULT_PROJECT_ROOT)
    parser.add_argument("--source-root", type=Path, action="append", default=[])
    parser.add_argument("--apply-cleanup", action="store_true")
    parser.add_argument("--cleanup-mode", choices=["move", "delete"], default="move")
    args = parser.parse_args()

    project_root = args.project_root.resolve()
    source_roots = [path.resolve() for path in (args.source_root or DEFAULT_SOURCE_ROOTS) if path.exists()]

    ensure_state_files(project_root)

    inventory_rows: list[dict[str, object]] = []
    cleanup_rows: list[dict[str, object]] = []
    suite_count = 0
    cleaned_count = 0

    for source_root in source_roots:
        for suite_dir in suite_directories(source_root):
            suite_count += 1
            suite_label = suite_dir.name
            year = detect_year(str(suite_dir))
            stage = detect_stage(str(suite_dir))
            district = detect_district(str(suite_dir))

            files = [classify_file(path) for path in sorted(suite_dir.iterdir()) if path.is_file()]
            rubric_candidates = sorted(
                [item for item in files if item.file_kind == "rubric_candidate"],
                key=lambda item: (item.score, item.path.suffix.lower() in {".doc", ".docx", ".pdf"}),
                reverse=True,
            )
            paper_candidates = sorted(
                [item for item in files if item.file_kind == "paper_candidate"],
                key=lambda item: item.score,
                reverse=True,
            )
            canonical_rubric = rubric_candidates[0] if rubric_candidates else None
            paper = paper_candidates[0] if paper_candidates else None

            inventory_rows.append(
                {
                    "source_root": source_root.name,
                    "suite_label": suite_label,
                    "suite_path": relative_under(suite_dir, source_root),
                    "year": year,
                    "district": district,
                    "exam_stage": stage,
                    "paper_file": paper.path.name if paper else "",
                    "canonical_rubric": canonical_rubric.path.name if canonical_rubric else "",
                    "canonical_rubric_score": canonical_rubric.score if canonical_rubric else "",
                    "rubric_candidate_count": len(rubric_candidates),
                    "file_count": len(files),
                    "needs_review": "yes" if (not canonical_rubric or not year or not district or not stage) else "no",
                }
            )

            if canonical_rubric:
                for extra in rubric_candidates[1:]:
                    cleanup_rows.append(
                        {
                            "source_root": source_root.name,
                            "suite_label": suite_label,
                            "suite_path": relative_under(suite_dir, source_root),
                            "canonical_rubric": canonical_rubric.path.name,
                            "candidate_file": extra.path.name,
                            "candidate_kind": extra.file_kind,
                            "candidate_score": extra.score,
                            "reason": f"weaker_than_canonical; {extra.reason}",
                            "suggested_action": "archive_or_delete_after_review",
                        }
                    )
                for noncanonical in files:
                    if noncanonical.file_kind in {"report_like", "lecture_like"}:
                        cleanup_rows.append(
                            {
                                "source_root": source_root.name,
                                "suite_label": suite_label,
                                "suite_path": relative_under(suite_dir, source_root),
                                "canonical_rubric": canonical_rubric.path.name,
                                "candidate_file": noncanonical.path.name,
                                "candidate_kind": noncanonical.file_kind,
                                "candidate_score": noncanonical.score,
                                "reason": noncanonical.reason,
                                "suggested_action": "archive_or_delete_after_review",
                            }
                        )

            if args.apply_cleanup and canonical_rubric:
                for row in [r for r in cleanup_rows if r["suite_path"] == relative_under(suite_dir, source_root)]:
                    candidate_path = suite_dir / str(row["candidate_file"])
                    if not candidate_path.exists():
                        continue
                    candidate_path = candidate_path.resolve()
                    if source_root.resolve() not in candidate_path.parents:
                        raise RuntimeError(f"Refusing to clean up outside source root: {candidate_path}")
                    if args.cleanup_mode == "move":
                        destination = cleanup_destination(project_root, candidate_path, source_root).resolve()
                        ensure_parent(destination)
                        if project_root.resolve() not in destination.parents:
                            raise RuntimeError(f"Refusing to move outside project archive: {destination}")
                        shutil.move(str(candidate_path), str(destination))
                    else:
                        candidate_path.unlink()
                    cleaned_count += 1

    reports_root = project_root / "data" / "reports"
    inventory_csv = reports_root / "exam_suite_inventory.csv"
    cleanup_csv = reports_root / "cleanup_candidates.csv"
    status_md = reports_root / "analyst_workspace_status.md"

    write_csv(
        inventory_csv,
        inventory_rows,
        [
            "source_root",
            "suite_label",
            "suite_path",
            "year",
            "district",
            "exam_stage",
            "paper_file",
            "canonical_rubric",
            "canonical_rubric_score",
            "rubric_candidate_count",
            "file_count",
            "needs_review",
        ],
    )
    write_csv(
        cleanup_csv,
        cleanup_rows,
        [
            "source_root",
            "suite_label",
            "suite_path",
            "canonical_rubric",
            "candidate_file",
            "candidate_kind",
            "candidate_score",
            "reason",
            "suggested_action",
        ],
    )

    status_md.write_text(
        "\n".join(
            [
                "# Analyst Workspace Status",
                "",
                f"- source_roots: {', '.join(path.name for path in source_roots)}",
                f"- suite_count: {suite_count}",
                f"- cleanup_candidate_count: {len(cleanup_rows)}",
                f"- cleanup_applied: {'yes' if args.apply_cleanup else 'no'}",
                f"- cleanup_mode: {args.cleanup_mode if args.apply_cleanup else 'review_only'}",
                f"- cleanup_changed_files: {cleaned_count}",
                "",
                "## Key Files",
                f"- inventory: `{inventory_csv}`",
                f"- cleanup: `{cleanup_csv}`",
                f"- book registry: `{project_root / 'data' / 'knowledge' / 'book_method_registry.md'}`",
                f"- master summary: `{project_root / 'data' / 'knowledge' / 'master_rubric_summary.md'}`",
                f"- governor board: `{project_root / 'data' / 'reports' / 'governor_board.md'}`",
                "",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"Prepared workspace at: {project_root}")
    print(f"Suites inventoried: {suite_count}")
    print(f"Cleanup candidates: {len(cleanup_rows)}")
    if args.apply_cleanup:
        print(f"Cleanup changed files: {cleaned_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
