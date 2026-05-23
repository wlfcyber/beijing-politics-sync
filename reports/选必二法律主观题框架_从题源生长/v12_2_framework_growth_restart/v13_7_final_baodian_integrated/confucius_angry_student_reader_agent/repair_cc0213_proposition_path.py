from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path


AGENT_DIR = Path(__file__).resolve().parent
ROOT = AGENT_DIR.parent
TRACE = ROOT / "traceability" / "TRACEABILITY_MATRIX_v13_7_final.csv"
BUILD_PACK = AGENT_DIR / "build_blind_trial_pack.py"
TARGET_PREFIX = "CC0213_2025_"
TARGET_SUFFIX = "_20"


def find_question_card() -> Path:
    matches = sorted(ROOT.glob("02_*_v13_7.md"))
    if len(matches) != 1:
        raise SystemExit(f"expected one 02_*_v13_7.md file, found {len(matches)}: {matches}")
    return matches[0]


def extract_proposition_path(card: Path) -> str:
    lines = card.read_text(encoding="utf-8").splitlines()
    in_target = False
    fullwidth_colon = chr(0xFF1A)

    for line in lines:
        if line.startswith("### "):
            in_target = TARGET_PREFIX in line and line.rstrip().endswith(TARGET_SUFFIX)
            continue

        if not in_target:
            continue

        if line.startswith("## "):
            break

        if "A8_" in line and "B1_" in line and "v12.2" in line and "->" in line:
            proposition = line.partition(fullwidth_colon)[2].strip()
            if not proposition:
                raise SystemExit(f"matched target line but could not split proposition path: {line}")
            return proposition

    raise SystemExit("could not extract CC0213 proposition path from question card")


def update_trace(proposition_path: str) -> None:
    with TRACE.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames

    if not fieldnames:
        raise SystemExit("traceability CSV has no header")

    changed = 0
    for row in rows:
        qid = row.get("question_id", "")
        if qid.startswith(TARGET_PREFIX) and qid.endswith(TARGET_SUFFIX):
            row["proposition_path"] = proposition_path
            changed += 1

    if changed != 1:
        raise SystemExit(f"expected to update one CC0213 row, updated {changed}")

    with TRACE.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def regenerate_trial_pack() -> None:
    subprocess.run([sys.executable, str(BUILD_PACK)], cwd=str(AGENT_DIR), check=True)


def main() -> None:
    proposition_path = extract_proposition_path(find_question_card())
    update_trace(proposition_path)
    regenerate_trial_pack()
    print(proposition_path)


if __name__ == "__main__":
    main()
