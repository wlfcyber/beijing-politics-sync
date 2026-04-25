#!/usr/bin/env python3
"""Sync the Beijing politics research artifacts between a working folder and this skill.

Examples:
  python scripts/sync_artifacts.py export --workspace "C:/Users/Administrator/Desktop" --skill-root .
  python scripts/sync_artifacts.py import --workspace "~/GaokaoPolitics/beijing-politics-sync" --skill-root ~/.codex/skills/feige-politics-garden
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ARTIFACTS = [
    {
        "name": "framework",
        "workspace_candidates": [
            "必修四哲学材料-知识触发总框架_持续更新版_v2.md",
            "artifacts/必修四哲学材料-知识触发总框架_持续更新版_v2.md",
        ],
        "skill_path": "assets/current-artifacts/必修四哲学材料-知识触发总框架_持续更新版_v2.md",
    },
    {
        "name": "wrong_options",
        "workspace_candidates": [
            "北京高考政治错肢库_持续更新版.md",
            "artifacts/北京高考政治错肢库_持续更新版.md",
        ],
        "skill_path": "assets/current-artifacts/北京高考政治错肢库_持续更新版.md",
    },
    {
        "name": "governor",
        "workspace_candidates": [
            "beijing_politics_research/data/reports/governor_board.md",
            "reports/governor_board.md",
        ],
        "skill_path": "assets/current-artifacts/governor_board.md",
    },
]


def expand(path: str) -> Path:
    return Path(path).expanduser().resolve()


def first_existing(base: Path, candidates: list[str]) -> Path | None:
    for rel in candidates:
        path = base / rel
        if path.exists():
            return path
    return None


def copy_file(src: Path, dest: Path, dry_run: bool) -> None:
    if not src.exists():
        raise FileNotFoundError(src)
    print(f"{src} -> {dest}")
    if dry_run:
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("direction", choices=["export", "import"])
    parser.add_argument("--workspace", required=True, help="Desktop workspace or cloned sync repo")
    parser.add_argument("--skill-root", required=True, help="Path to feige-politics-garden")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    workspace = expand(args.workspace)
    skill_root = expand(args.skill_root)

    if args.direction == "export":
        for artifact in ARTIFACTS:
            src = first_existing(workspace, artifact["workspace_candidates"])
            if src is None:
                print(f"skip missing {artifact['name']}: no candidate found under {workspace}")
                continue
            dest = skill_root / artifact["skill_path"]
            copy_file(src, dest, args.dry_run)
    else:
        for artifact in ARTIFACTS:
            src = skill_root / artifact["skill_path"]
            dest_rel = artifact["workspace_candidates"][-1]
            dest = workspace / dest_rel
            copy_file(src, dest, args.dry_run)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
