#!/usr/bin/env python3
"""Create a football video project scaffold."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


EVENT_FIELDS = [
    "event_id",
    "match",
    "date",
    "team_or_player",
    "event_label",
    "source_file",
    "start_time",
    "end_time",
    "evidence_status",
    "claim_for_script",
    "notes",
]

EDL_FIELDS = [
    "clip_id",
    "event_id",
    "source_file",
    "in_time",
    "out_time",
    "visual_action",
    "crop",
    "voiceover",
    "subtitle",
    "sfx_or_music",
    "notes",
]


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9._-]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "football-video"


def write_csv(path: Path, fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a football video workflow project.")
    parser.add_argument("name", help="Project name, for example liverpool-referee-compilation")
    parser.add_argument("--root", default=".", help="Parent output directory")
    args = parser.parse_args()

    project = Path(args.root).expanduser().resolve() / slugify(args.name)
    folders = [
        "assets/raw",
        "assets/source_clips",
        "assets/music",
        "planning",
        "work/cuts",
        "work/audio",
        "work/subtitles",
        "exports",
    ]
    for folder in folders:
        (project / folder).mkdir(parents=True, exist_ok=True)

    write_csv(project / "planning" / "event_ledger.csv", EVENT_FIELDS)
    write_csv(project / "planning" / "edit_decision_list.csv", EDL_FIELDS)

    (project / "planning" / "narration.md").write_text(
        "# Narration\n\n"
        "Write the final narration only after the event ledger and edit decision list are locked.\n",
        encoding="utf-8",
    )
    (project / "planning" / "fact_check.md").write_text(
        "# Fact Check\n\n"
        "- Verified claims:\n"
        "- User-provided claims:\n"
        "- Removed or softened unverified claims:\n",
        encoding="utf-8",
    )
    print(project)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
