from __future__ import annotations

import json
import shutil
from datetime import datetime
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
ACCEPTED = RUN_DIR / "04_fusion_audit" / "student_patch_entries.accepted.jsonl"
FINDINGS = RUN_DIR / "03_claudecode_lane" / "claudecode_after_depth_final_findings_20260524.jsonl"
REPORT = RUN_DIR / "04_fusion_audit" / "claudecode_after_depth_fix_applied_20260524.md"


def load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            # ClaudeCode's row-16 note contains unescaped Chinese quotes.
            # Row 16 is handled below as a deterministic format fix.
            continue
    return rows


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    rows = load_jsonl(ACCEPTED)
    findings = load_jsonl(FINDINGS)
    backup = ACCEPTED.with_name(
        f"{ACCEPTED.stem}.backup_before_claudecode_after_depth_fix_{datetime.now():%Y%m%d_%H%M%S}.jsonl"
    )
    shutil.copy2(ACCEPTED, backup)

    applied: list[str] = []

    # ClaudeCode row ids are 1-based positions in accepted.jsonl.
    by_row_id = {str(i + 1): row for i, row in enumerate(rows)}
    for finding in findings:
        row_id = str(finding.get("row_id", "")).strip()
        if finding.get("verdict") != "REWRITE" or row_id not in by_row_id:
            continue
        rewrite = finding.get("student_rewrite") or {}
        target = by_row_id[row_id]
        for field in ("material_trigger", "why_trigger", "answer_landing"):
            if rewrite.get(field):
                target[field] = rewrite[field]
        applied.append(
            f"- row {row_id}: applied ClaudeCode rewrite for {target.get('source_suite')} {target.get('question_no')} / {target.get('canonical_node')}"
        )

    # Format consistency fix requested by ClaudeCode for row 16.
    if "16" in by_row_id:
        by_row_id["16"]["question_prompt"] = (
            "结合材料，运用《哲学与文化》知识，谈谈你对“守护湿地，就是守护生态之美与文化根脉”的认识。"
        )
        applied.append("- row 16: normalized the wetland question prompt punctuation and book title marks.")

    write_jsonl(ACCEPTED, rows)

    REPORT.write_text(
        "# ClaudeCode after-depth fixes applied\n\n"
        f"- accepted jsonl: `{ACCEPTED}`\n"
        f"- backup: `{backup}`\n"
        f"- findings: `{FINDINGS}`\n\n"
        "## Applied\n\n"
        + "\n".join(applied)
        + "\n",
        encoding="utf-8",
    )

    print(f"applied={len(applied)}")
    print(f"backup={backup}")
    print(f"report={REPORT}")


if __name__ == "__main__":
    main()
