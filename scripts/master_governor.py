#!/usr/bin/env python3
"""Project-wide supervisor report and context compression for Beijing politics.

This script does not judge political content. It scans run-control files, flags
stale or unsafe workflow states, and creates deterministic context capsules for
large text/log files so daily AI workers do not paste over-sized context.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
from collections import defaultdict, deque
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_WORKSPACE = Path("/Users/wanglifei/Desktop/北京高考政治")
DEFAULT_SYNC_ROOT = Path(__file__).resolve().parents[1]
REPORT_REL = Path("reports/master_governor")

CONTROL_NAMES = {
    "TASK_BRIEF.md",
    "DEVELOPMENT_PLAN.md",
    "PROGRESS.md",
    "progress.md",
    "task_plan.md",
    "findings.md",
    "MASTER_REQUIREMENTS.md",
    "USER_FRAMEWORK.md",
    "USER_QUESTIONS.md",
    "DECISION_LOG.md",
    "SOURCE_LEDGER.csv",
    "COVERAGE_MATRIX.csv",
    "QUESTION_COVERAGE_MATRIX.csv",
    "TRACEABILITY_MATRIX.csv",
    "GOVERNOR_CHECKLIST.md",
    "GOVERNOR_GATES.md",
    "FINAL_ACCEPTANCE_REPORT.md",
}

TEXT_EXTENSIONS = {
    ".md",
    ".txt",
    ".csv",
    ".tsv",
    ".json",
    ".jsonl",
    ".log",
    ".yaml",
    ".yml",
}

PRUNE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".docx_render",
    "node_modules",
    "render_samples",
    "renders",
    "rendered",
    "pdf_pages",
    "quicklook",
    "tmp_pdf_render_test",
}

CONTROL_PARENT_NAMES = {
    "00_control",
    "01_source_inventory",
    "02_extraction",
    "03_entries",
    "04_suite_reports",
    "05_coverage",
    "06_conflicts",
    "07_student_doc",
    "08_review",
    "09_delivery",
    "delivery",
    "governor_confucius",
    "codex_lane",
    "claudecode_lane",
    "fusion",
}

RISK_PATTERNS = [
    "BLOCKED",
    "blocked",
    "real_call_pending",
    "blocked_advisor",
    "web_visible_pro_adaptive_call_pending_user_waived",
    "DELIVERED_WITH_GOVERNANCE_GAPS",
    "TODO",
    "待",
    "缺",
    "未完成",
    "无法",
    "pending",
]

FALSE_CLOSURE_MARKERS = [
    "TASK_COMPLETE",
    "所有任务闭合",
    "最终闭环",
    "FINAL PASS",
]

KEY_LINE_RE = re.compile(
    r"(STEP_|TASK_COMPLETE|STEP_DONE|BLOCKED|blocked|pending|real_call_pending|"
    r"governor|Governor|GOVERNOR|Confucius|TRACEABILITY|COVERAGE|SOURCE_LEDGER|"
    r"FINAL_ACCEPTANCE|缺|待|未完成|无法|评分细则|参考答案|rubric|OCR)",
    re.IGNORECASE,
)


@dataclass
class LaneStatus:
    root: Path
    controls: list[Path] = field(default_factory=list)
    last_update: float = 0.0
    completed_steps: int = 0
    pending_steps: int = 0
    has_plan: bool = False
    has_progress: bool = False
    has_governor: bool = False
    has_acceptance: bool = False
    has_source_ledger: bool = False
    has_coverage: bool = False
    has_traceability: bool = False
    risk_hits: list[str] = field(default_factory=list)
    flags: list[str] = field(default_factory=list)
    next_action: str = ""


def now_local() -> datetime:
    return datetime.now().astimezone()


def safe_rel(path: Path, base: Path) -> str:
    try:
        return str(path.relative_to(base))
    except ValueError:
        return str(path)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_sample(path: Path, limit: int = 300_000) -> str:
    try:
        size = path.stat().st_size
        with path.open("rb") as handle:
            if size <= limit * 2:
                data = handle.read()
            else:
                head = handle.read(limit)
                handle.seek(max(0, size - limit))
                tail = handle.read(limit)
                data = head + b"\n\n[...middle omitted...]\n\n" + tail
        return data.decode("utf-8", errors="replace")
    except OSError:
        return ""


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def mirror_file(src: Path, primary_root: Path, mirror_root: Path | None) -> None:
    if mirror_root is None:
        return
    try:
        rel = src.relative_to(primary_root)
    except ValueError:
        return
    dest = mirror_root / rel
    if dest.resolve() == src.resolve():
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)


def is_control_file(path: Path) -> bool:
    name = path.name
    upper = name.upper()
    return (
        name in CONTROL_NAMES
        or "GOVERNOR" in upper
        or "ACCEPTANCE" in upper
        or "TRACEABILITY" in upper
    )


def lane_root_for(control_file: Path, workspace: Path) -> Path:
    parent = control_file.parent
    if parent.name in CONTROL_PARENT_NAMES and parent.parent != workspace:
        return parent.parent
    if parent.parent.name in CONTROL_PARENT_NAMES and parent.parent.parent != workspace:
        return parent.parent.parent
    return parent


def iter_project_files(root: Path, max_depth: int) -> list[Path]:
    files: list[Path] = []
    root = root.resolve()
    for dirpath, dirnames, filenames in os.walk(root):
        current = Path(dirpath)
        rel_parts = current.relative_to(root).parts
        if len(rel_parts) > max_depth:
            dirnames[:] = []
            continue
        dirnames[:] = [
            name
            for name in dirnames
            if name not in PRUNE_DIRS and not name.startswith(".Trash")
        ]
        if REPORT_REL in current.relative_to(root).parents or current.relative_to(root) == REPORT_REL:
            continue
        for filename in filenames:
            files.append(current / filename)
    return files


def discover_lanes(workspace: Path, max_depth: int, stale_days: int, max_context_bytes: int) -> list[LaneStatus]:
    grouped: dict[Path, LaneStatus] = {}
    for path in iter_project_files(workspace, max_depth=max_depth):
        if not is_control_file(path):
            continue
        root = lane_root_for(path, workspace)
        status = grouped.setdefault(root, LaneStatus(root=root))
        status.controls.append(path)
        try:
            status.last_update = max(status.last_update, path.stat().st_mtime)
        except OSError:
            pass

    for status in grouped.values():
        analyze_lane(status, workspace, stale_days, max_context_bytes)

    return sorted(grouped.values(), key=lambda item: item.last_update, reverse=True)


def analyze_lane(status: LaneStatus, workspace: Path, stale_days: int, max_context_bytes: int) -> None:
    combined = []
    names = {p.name for p in status.controls}
    upper_names = {p.name.upper() for p in status.controls}

    status.has_plan = bool({"DEVELOPMENT_PLAN.md", "task_plan.md", "TASK_BRIEF.md"} & names)
    status.has_progress = bool({"PROGRESS.md", "progress.md"} & names)
    status.has_governor = any("GOVERNOR" in name for name in upper_names)
    status.has_acceptance = any("ACCEPTANCE" in name for name in upper_names)
    status.has_source_ledger = "SOURCE_LEDGER.csv" in names
    status.has_coverage = bool({"COVERAGE_MATRIX.csv", "QUESTION_COVERAGE_MATRIX.csv"} & names)
    status.has_traceability = any("TRACEABILITY" in name for name in upper_names)

    for path in status.controls:
        sample = read_sample(path)
        combined.append(sample)
        if path.name in {"DEVELOPMENT_PLAN.md", "PROGRESS.md", "progress.md", "task_plan.md"}:
            status.completed_steps += len(re.findall(r"- \[x\]\s*STEP_", sample))
            status.pending_steps += len(re.findall(r"- \[ \]\s*STEP_", sample))
        try:
            if path.stat().st_size > max_context_bytes:
                status.flags.append(f"oversized_control:{safe_rel(path, workspace)}")
        except OSError:
            pass

    text = "\n".join(combined)
    for pattern in RISK_PATTERNS:
        if pattern in text and pattern not in status.risk_hits:
            status.risk_hits.append(pattern)

    age_days = (now_local().timestamp() - status.last_update) / 86400 if status.last_update else 999
    if age_days > stale_days:
        status.flags.append(f"stale>{stale_days}d")
    if not status.has_progress:
        status.flags.append("missing_progress")
    if not status.has_governor:
        status.flags.append("missing_governor")
    if status.has_acceptance and not status.has_coverage:
        status.flags.append("acceptance_without_coverage")
    if status.has_acceptance and any(marker in text for marker in FALSE_CLOSURE_MARKERS) and status.risk_hits:
        status.flags.append("possible_false_closure")

    if status.risk_hits:
        status.next_action = "resolve visible blockers before content production"
    elif not status.has_progress:
        status.next_action = "create or align PROGRESS.md before executing"
    elif not status.has_governor:
        status.next_action = "add governor check before claiming completion"
    elif status.pending_steps:
        status.next_action = "execute next unchecked STEP only"
    elif status.has_acceptance:
        status.next_action = "verify final report against live artifacts"
    else:
        status.next_action = "refresh lane state and register next step"


def first_line_list(items: list[str], limit: int = 6) -> str:
    if not items:
        return "none"
    shown = items[:limit]
    rest = len(items) - len(shown)
    text = "; ".join(shown)
    if rest:
        text += f"; +{rest} more"
    return text


def build_report(lanes: list[LaneStatus], workspace: Path, sync_root: Path, max_context_bytes: int) -> str:
    generated = now_local()
    flagged = [lane for lane in lanes if lane.flags or lane.risk_hits]
    stale = [lane for lane in lanes if any(flag.startswith("stale") for flag in lane.flags)]
    false_closure = [lane for lane in lanes if "possible_false_closure" in lane.flags]

    lines = [
        "# Beijing Politics Master Governor Report",
        "",
        f"- generated_at: {generated.isoformat(timespec='seconds')}",
        f"- workspace: `{workspace}`",
        f"- sync_root: `{sync_root}`",
        f"- context_threshold_bytes: {max_context_bytes}",
        f"- lane_count: {len(lanes)}",
        f"- flagged_lanes: {len(flagged)}",
        f"- stale_lanes: {len(stale)}",
        f"- possible_false_closure_lanes: {len(false_closure)}",
        "",
        "## Mandatory Three-Layer SOP",
        "",
        "No worker may touch project code, sources, rubrics, generated teaching files, or sync artifacts until it has passed:",
        "",
        "1. Layer 1 Project Master Governor: read this report, `worker_daily_orders.md`, compression manifest, and adaptive ledgers.",
        "2. Layer 2 Skill And Notebook: load the relevant Beijing politics skill and hard-rule notebook.",
        "3. Layer 3 Run Execution: read the lane's plan/progress/ledger/governor files and complete one minimal real step.",
        "",
    ]

    if false_closure:
        lines.extend(["## Critical Alerts", ""])
        for lane in false_closure[:20]:
            lines.append(f"- `{safe_rel(lane.root, workspace)}`: possible false closure. Risk hits: {first_line_list(lane.risk_hits)}")
        lines.append("")

    lines.extend(
        [
            "## Lane Table",
            "",
            "| Lane | Last update | Steps x/pending | Control flags | Risk hits | Next action |",
            "| --- | --- | ---: | --- | --- | --- |",
        ]
    )
    for lane in lanes:
        last = datetime.fromtimestamp(lane.last_update, tz=timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M") if lane.last_update else "unknown"
        lines.append(
            "| "
            + f"`{safe_rel(lane.root, workspace)}` | {last} | {lane.completed_steps}/{lane.pending_steps} | "
            + f"{first_line_list(lane.flags)} | {first_line_list(lane.risk_hits)} | {lane.next_action} |"
        )

    lines.extend(
        [
            "",
            "## Worker Daily Start Card",
            "",
            "Copy this into any subproject AI before it acts:",
            "",
            "```text",
            "你是北京高考政治项目的分项AI。先执行三层SOP，不得直接动资料。",
            "1. 读取 reports/master_governor/latest_master_governor_report.md。",
            "2. 读取 reports/master_governor/worker_daily_orders.md。",
            "3. 找到你负责的 lane 路径；若找不到，先写注册/BLOCKED，不要自己猜。",
            "4. 读取对应 skill、hard-rule notebook、TASK_BRIEF、DEVELOPMENT_PLAN、PROGRESS、ledger、governor/acceptance 文件。",
            "5. 只推进报告允许的下一个最小完整步骤；先写真实产物，再更新 PROGRESS 和 governor。",
            "6. 超过 1MB 的文件只读 context_capsules 摘要；需要精确证据时再定位原文件，不要整文件塞进上下文。",
            "最后只输出 STEP_DONE:<step>、BLOCKED:<reason> 或 TASK_COMPLETE，并写入控制文件。",
            "```",
            "",
            "## Compression Rule",
            "",
            "Files above the threshold are indexed in `context_compression_manifest.csv`. Capsules are context aids only; original files remain the evidence source.",
            "",
        ]
    )
    return "\n".join(lines)


def build_worker_orders(lanes: list[LaneStatus], workspace: Path) -> str:
    generated = now_local().isoformat(timespec="seconds")
    lines = [
        "# Worker Daily Orders",
        "",
        f"- generated_at: {generated}",
        "- rule: 每个分项AI每天先读本文件，再读自己的 lane 控制文件。",
        "",
        "## Global Orders",
        "",
        "1. 不经过三层SOP，不得读取、改写、同步或压缩项目资料。",
        "2. 如果你被分配到某一书目/模块，必须先读对应 skill 和 hard-rule notebook。",
        "3. 如果你的 lane 有 `possible_false_closure`、`real_call_pending`、`blocked_advisor`、缺 governor、缺 coverage、缺 traceability，先修控制闭环，不继续写正文。",
        "4. 如果要处理超过 1MB 的日志/报告/JSON，先读 context capsule 和 manifest，再按需要打开原文局部。",
        "5. 每次只推进一个最小完整步骤，先产出真实文件，再更新 `PROGRESS.md` 和 governor。",
        "",
        "## Lane Orders",
        "",
    ]
    for lane in lanes:
        if lane.flags or lane.risk_hits or lane.pending_steps:
            lines.append(f"### {safe_rel(lane.root, workspace)}")
            lines.append("")
            lines.append(f"- next_action: {lane.next_action}")
            lines.append(f"- flags: {first_line_list(lane.flags)}")
            lines.append(f"- risk_hits: {first_line_list(lane.risk_hits)}")
            lines.append("")
    return "\n".join(lines)


def ensure_learning_files(report_dir: Path) -> None:
    ledger = report_dir / "adaptive_rules_ledger.md"
    if not ledger.exists():
        write_text(
            ledger,
            "\n".join(
                [
                    "# Adaptive Rules Ledger",
                    "",
                    "Self-learning in this project means durable rule capture after a user correction, governor failure, or repeated workflow defect. It never changes evidence hierarchy by itself.",
                    "",
                    "| Date | Trigger | New rule | Validation check | Affected files | Status |",
                    "| --- | --- | --- | --- | --- | --- |",
                    "| 2026-05-18 | Project governor bootstrap | All workers must pass Layer 1 report, Layer 2 skill/notebook, and Layer 3 run controls before touching project data. | latest report plus worker orders exist before execution | reports/master_governor/*, skills/*/SKILL.md | accepted |",
                    "| 2026-05-18 | Context may exceed 1MB | Files above threshold require deterministic context capsules; original remains evidence source. | context_compression_manifest.csv contains oversized files | reports/master_governor/context_capsules/* | accepted |",
                    "",
                ]
            ),
        )

    register = report_dir / "self_learning_register.csv"
    if not register.exists():
        with register.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle, lineterminator="\n")
            writer.writerow(
                [
                    "date",
                    "source",
                    "signal",
                    "proposed_adaptation",
                    "evidence_boundary",
                    "status",
                    "owner",
                ]
            )
            writer.writerow(
                [
                    "2026-05-18",
                    "project-bootstrap",
                    "online-advice-adapted",
                    "project master governor plus daily worker SOP plus context capsules",
                    "workflow rule only, not content evidence",
                    "accepted",
                    "master_governor",
                ]
            )


def sanitize_name(rel: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", rel).strip("_")
    digest = hashlib.sha1(rel.encode("utf-8")).hexdigest()[:10]
    if len(safe) > 90:
        safe = safe[-90:]
    return f"{digest}_{safe}.summary.md"


def clip_line(line: str, limit: int = 500) -> str:
    if len(line) <= limit:
        return line
    return f"{line[:limit]} [...line clipped {len(line) - limit} chars...]"


def iter_large_text_files(workspace: Path, threshold: int, max_depth: int) -> list[Path]:
    result = []
    for path in iter_project_files(workspace, max_depth=max_depth):
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        try:
            if path.stat().st_size > threshold:
                result.append(path)
        except OSError:
            continue
    return sorted(result, key=lambda p: p.stat().st_size if p.exists() else 0, reverse=True)


def create_capsules(
    workspace: Path,
    report_dir: Path,
    threshold: int,
    max_depth: int,
    capsule_limit: int,
) -> list[dict[str, str]]:
    capsule_dir = report_dir / "context_capsules"
    capsule_dir.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, str]] = []
    files = iter_large_text_files(workspace, threshold, max_depth=max_depth)[:capsule_limit]

    for path in files:
        rel = safe_rel(path, workspace)
        capsule = capsule_dir / sanitize_name(rel)
        head: list[str] = []
        tail: deque[str] = deque(maxlen=80)
        key_lines: list[str] = []
        line_count = 0

        try:
            with path.open("r", encoding="utf-8", errors="replace") as handle:
                for line in handle:
                    line_count += 1
                    clean = clip_line(line.rstrip())
                    if len(head) < 80:
                        head.append(clean)
                    tail.append(clean)
                    if len(key_lines) < 120 and KEY_LINE_RE.search(clean):
                        key_lines.append(f"{line_count}: {clean}")
        except OSError as exc:
            key_lines.append(f"read_error: {exc}")

        size = path.stat().st_size
        digest = sha256_file(path)
        text = [
            f"# Context Capsule: {rel}",
            "",
            f"- source_path: `{path}`",
            f"- size_bytes: {size}",
            f"- sha256: {digest}",
            f"- line_count_estimate: {line_count}",
            f"- generated_at: {now_local().isoformat(timespec='seconds')}",
            "- warning: This capsule is an index only. Open the original file for exact evidence.",
            "",
            "## Key Lines",
            "",
            "\n".join(key_lines) if key_lines else "No key lines matched.",
            "",
            "## First Lines",
            "",
            "```text",
            "\n".join(head),
            "```",
            "",
            "## Last Lines",
            "",
            "```text",
            "\n".join(tail),
            "```",
            "",
        ]
        write_text(capsule, "\n".join(text))
        rows.append(
            {
                "path": rel,
                "size_bytes": str(size),
                "sha256": digest,
                "capsule_path": safe_rel(capsule, report_dir),
                "line_count_estimate": str(line_count),
                "policy": "capsule-first-original-for-evidence",
            }
        )

    manifest = report_dir / "context_compression_manifest.csv"
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "path",
                "size_bytes",
                "sha256",
                "capsule_path",
                "line_count_estimate",
                "policy",
            ],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)

    return rows


def write_state(report_dir: Path, lanes: list[LaneStatus], workspace: Path) -> None:
    state = {
        "generated_at": now_local().isoformat(timespec="seconds"),
        "workspace": str(workspace),
        "lanes": [
            {
                "root": safe_rel(lane.root, workspace),
                "last_update": lane.last_update,
                "completed_steps": lane.completed_steps,
                "pending_steps": lane.pending_steps,
                "flags": lane.flags,
                "risk_hits": lane.risk_hits,
                "next_action": lane.next_action,
                "controls": [safe_rel(path, workspace) for path in lane.controls],
            }
            for lane in lanes
        ],
    }
    write_text(report_dir / "PROJECT_GOVERNOR_STATE.json", json.dumps(state, ensure_ascii=False, indent=2))


def command_report(args: argparse.Namespace) -> int:
    workspace = Path(args.workspace).expanduser().resolve()
    sync_root = Path(args.sync_root).expanduser().resolve()
    primary_report_dir = workspace / REPORT_REL
    sync_report_dir = sync_root / REPORT_REL if sync_root else None
    primary_report_dir.mkdir(parents=True, exist_ok=True)

    lanes = discover_lanes(
        workspace=workspace,
        max_depth=args.max_depth,
        stale_days=args.stale_days,
        max_context_bytes=args.max_context_bytes,
    )
    create_capsules(
        workspace=workspace,
        report_dir=primary_report_dir,
        threshold=args.max_context_bytes,
        max_depth=args.max_depth,
        capsule_limit=args.capsule_limit,
    )
    ensure_learning_files(primary_report_dir)

    report = build_report(lanes, workspace, sync_root, args.max_context_bytes)
    latest = primary_report_dir / "latest_master_governor_report.md"
    dated = primary_report_dir / f"master_governor_report_{now_local().strftime('%Y-%m-%d')}.md"
    orders = primary_report_dir / "worker_daily_orders.md"
    write_text(latest, report)
    write_text(dated, report)
    write_text(orders, build_worker_orders(lanes, workspace))
    write_state(primary_report_dir, lanes, workspace)

    sop_src = sync_root / "skills/feige-politics-garden/references/project-governor-three-layer-sop.md"
    if sop_src.exists():
        shutil.copy2(sop_src, primary_report_dir / "PROJECT_GOVERNOR_THREE_LAYER_SOP.md")

    if sync_report_dir:
        for path in primary_report_dir.rglob("*"):
            if path.is_file():
                mirror_file(path, workspace, sync_root)

    print(f"wrote {latest}")
    print(f"wrote {orders}")
    print(f"lanes={len(lanes)}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    report = subparsers.add_parser("report", help="Generate supervision report and context capsules")
    report.add_argument("--workspace", default=str(DEFAULT_WORKSPACE))
    report.add_argument("--sync-root", default=str(DEFAULT_SYNC_ROOT))
    report.add_argument("--max-context-bytes", type=int, default=1_000_000)
    report.add_argument("--max-depth", type=int, default=6)
    report.add_argument("--stale-days", type=int, default=7)
    report.add_argument("--capsule-limit", type=int, default=200)
    report.set_defaults(func=command_report)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
