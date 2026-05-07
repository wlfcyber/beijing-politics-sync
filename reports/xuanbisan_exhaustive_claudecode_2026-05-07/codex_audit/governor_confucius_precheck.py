import csv
import json
import subprocess
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
FUSION_DIR = RUN_DIR / "fusion" / "framework_first_fusion"
OVERALL_DIR = RUN_DIR / "fusion" / "overall_batch_closure"
OUT_DIR = RUN_DIR / "governor_confucius"

FORBIDDEN = ["固定分析流程", "FINAL_PASS", "终稿已通过", "最终版", "需 Codex 回源复核"]
AUDIT_MARKERS = ["P0证据", "P1证据", "P2证据", "A-formal", "A-support", "B-choice-signal", "source_insufficient"]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def check_processes() -> list[dict[str, str]]:
    command = (
        "Get-CimInstance Win32_Process | "
        "Where-Object { ($_.CommandLine -match 'run_p2_source_group.py' "
        "-or $_.CommandLine -match 'CLAUDECODE_.*P2' "
        "-or $_.CommandLine -match 'P2_RECHECK') "
        "-and $_.Name -ne 'powershell.exe' } | "
        "Select-Object ProcessId,Name,CommandLine | ConvertTo-Json -Compress"
    )
    result = subprocess.run(
        ["powershell", "-NoProfile", "-Command", command],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=20,
    )
    text = result.stdout.strip()
    if not text:
        return []
    data = json.loads(text)
    if isinstance(data, dict):
        data = [data]
    return data


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)

    required = {
        "overall": (OVERALL_DIR / "OVERALL_COVERAGE_AUDIT.json", "OVERALL_BATCH_CLOSURE_OK_NOT_FINAL"),
        "p0_recheck": (RUN_DIR / "claudecode_lane" / "p0_recheck" / "P0_RECHECK_QA.json", "P0_RECHECK_QA_OK_NOT_FINAL"),
        "p1_recheck": (RUN_DIR / "claudecode_lane" / "p1_recheck" / "P1_RECHECK_QA.json", "P1_RECHECK_QA_OK_NOT_FINAL"),
        "p2_recheck": (RUN_DIR / "claudecode_lane" / "p2_recheck" / "P2_RECHECK_QA.json", "P2_RECHECK_QA_OK_NOT_FINAL"),
        "p0_fusion": (FUSION_DIR / "P0_FUSION_PATCH_QA.json", "P0_FUSION_PATCH_OK_NOT_FINAL"),
        "p1_fusion": (FUSION_DIR / "P1_FUSION_PATCH_QA.json", "P1_FUSION_PATCH_OK_NOT_FINAL"),
        "p2_fusion": (FUSION_DIR / "P2_FUSION_PATCH_QA.json", "P2_FUSION_PATCH_OK_NOT_FINAL"),
    }

    qa_status = {}
    issues = []
    for name, (path, expected) in required.items():
        if not path.exists():
            qa_status[name] = {"exists": False, "expected": expected, "actual": None}
            issues.append({"kind": "missing_qa", "name": name, "path": str(path)})
            continue
        data = load_json(path)
        actual = data.get("verdict")
        qa_status[name] = {"exists": True, "expected": expected, "actual": actual}
        if actual != expected:
            issues.append({"kind": "qa_verdict_mismatch", "name": name, "expected": expected, "actual": actual})

    final_fusion = FUSION_DIR / "FRAMEWORK_FIRST_FUSION_P2_PATCHED.md"
    fusion_text = final_fusion.read_text(encoding="utf-8", errors="replace") if final_fusion.exists() else ""
    forbidden_hits = {token: fusion_text.count(token) for token in FORBIDDEN}
    if any(forbidden_hits.values()):
        issues.append({"kind": "forbidden_or_recheck_text_in_fusion", "hits": forbidden_hits})

    p2_decisions = read_csv(RUN_DIR / "claudecode_lane" / "p2_recheck" / "P2_RECHECK_DECISIONS.csv")
    p2_decision_counts = Counter(row["decision"] for row in p2_decisions)
    p2_enter_counts = Counter(row["can_enter_fusion"] for row in p2_decisions)

    processes = check_processes()
    if processes:
        issues.append({"kind": "claudecode_p2_process_still_running", "processes": processes})

    governor_verdict = "GOVERNOR_P0_P2_EVIDENCE_GATE_OK_NOT_FINAL" if not issues else "GOVERNOR_P0_P2_EVIDENCE_GATE_FAIL"

    audit_marker_hits = {token: fusion_text.count(token) for token in AUDIT_MARKERS}
    student_ready = not any(audit_marker_hits.values())
    confucius_verdict = (
        "CONFUCIUS_ZERO_BASELINE_READY_FOR_STUDENT_DELIVERY"
        if student_ready
        else "CONFUCIUS_PRECHECK_NOT_STUDENT_DELIVERY"
    )

    summary = {
        "governor_verdict": governor_verdict,
        "confucius_verdict": confucius_verdict,
        "issues": issues,
        "qa_status": qa_status,
        "p2_decision_counts": dict(p2_decision_counts),
        "p2_can_enter_fusion_counts": dict(p2_enter_counts),
        "forbidden_hits": forbidden_hits,
        "audit_marker_hits": audit_marker_hits,
        "running_p2_processes": processes,
        "final_fusion": str(final_fusion),
        "word_pdf_delivery_authorized": False,
    }
    (OUT_DIR / "GOVERNOR_CONFUCIUS_PRECHECK.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    md = [
        "# Governor / Confucius Precheck",
        "",
        f"Governor verdict: `{governor_verdict}`",
        f"Confucius verdict: `{confucius_verdict}`",
        "",
        "## Evidence Gate",
        "",
    ]
    for name, status in qa_status.items():
        md.append(f"- {name}: `{status['actual']}` expected `{status['expected']}`")
    md.extend(
        [
            "",
            "## P2 Boundary",
            "",
            f"- P2 decision counts: `{dict(p2_decision_counts)}`",
            f"- P2 can-enter-fusion counts: `{dict(p2_enter_counts)}`",
            f"- forbidden/recheck hits in fusion: `{forbidden_hits}`",
            f"- running P2 ClaudeCode processes: `{len(processes)}`",
            "",
            "## Confucius Note",
            "",
            "- The current artifact is a framework-first fusion draft with audit evidence still visible.",
            "- It is ready for a later student-facing cleanup pass, but it is not a student delivery, Word file, PDF, or final product.",
            f"- audit marker hits: `{audit_marker_hits}`",
            "",
            "## Boundary",
            "",
            "- Word/PDF/delivery authorization: `no`",
            "- Four-line finalization authorization: `no`",
        ]
    )
    if issues:
        md.extend(["", "## Issues", ""])
        for issue in issues:
            md.append(f"- `{issue['kind']}`: `{issue}`")
    (OUT_DIR / "GOVERNOR_CONFUCIUS_PRECHECK.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
