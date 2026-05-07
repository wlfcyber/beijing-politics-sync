import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
P2_PATCH = RUN_DIR / "claudecode_lane" / "p2_recheck" / "P2_RECHECK_PATCHES.jsonl"
BACKUP = P2_PATCH.with_suffix(".jsonl.bak_forbidden_recheck_phrase")

REPLACEMENTS = {
    "带'需 Codex 回源复核'前置标签": "带旧稿待核前置标签",
    "带''需 Codex 回源复核''前置标签": "带旧稿待核前置标签",
    "仍标'需 Codex 回源复核'": "仍标旧稿待核",
    "保留'需 Codex 回源复核'前置标签或降级为 source_insufficient": "降级为 source_insufficient",
    "需 Codex 回源复核": "旧稿待核标签",
}


def scrub(value):
    if isinstance(value, str):
        for old, new in REPLACEMENTS.items():
            value = value.replace(old, new)
    return value


def main() -> None:
    rows = [json.loads(line) for line in P2_PATCH.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not BACKUP.exists():
        BACKUP.write_text(P2_PATCH.read_text(encoding="utf-8"), encoding="utf-8")

    changed = 0
    for row in rows:
        for key, value in list(row.items()):
            new_value = scrub(value)
            if new_value != value:
                changed += 1
                row[key] = new_value

    P2_PATCH.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"patched_rows": len(rows), "changed_fields": changed, "backup": str(BACKUP)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
