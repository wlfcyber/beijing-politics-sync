#!/usr/bin/env python3
"""Search and register stock football video materials for a project."""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

try:
    import tomllib  # type: ignore[import-not-found]
except ModuleNotFoundError:  # macOS system Python may be older than 3.11.
    tomllib = None


FIELDS = [
    "id",
    "provider",
    "query",
    "status",
    "file",
    "bytes",
    "duration",
    "width",
    "height",
    "source_url",
    "credit",
    "license_note",
    "intended_use",
    "notes",
]

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 Chrome/120 Safari/537.36"
)


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9._-]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "material"


def load_pexels_key(config_path: str | None, env_name: str) -> str:
    env_value = os.environ.get(env_name)
    if env_value:
        return env_value.strip()

    candidates: list[Path] = []
    if config_path:
        candidates.append(Path(config_path).expanduser())
    candidates.extend(
        [
            Path("MoneyPrinterTurbo/config.toml"),
            Path("config.toml"),
        ]
    )

    for candidate in candidates:
        if not candidate.exists():
            continue
        text = candidate.read_text(encoding="utf-8")
        if tomllib is not None:
            data = tomllib.loads(text)
            keys = data.get("app", {}).get("pexels_api_keys") or []
        else:
            match = re.search(r"(?m)^\s*pexels_api_keys\s*=\s*\[(.*?)\]", text)
            keys = re.findall(r'"([^"]+)"', match.group(1)) if match else []
        keys = [k for k in keys if isinstance(k, str) and k.strip()]
        if keys:
            return keys[0].strip()

    raise SystemExit(
        f"No Pexels key found. Set {env_name} or pass --config pointing to MoneyPrinterTurbo config.toml."
    )


def pexels_search(query: str, api_key: str, per_page: int, orientation: str) -> dict[str, Any]:
    params = {"query": query, "per_page": per_page}
    if orientation != "any":
        params["orientation"] = orientation
    url = "https://api.pexels.com/videos/search?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, headers={"Authorization": api_key, "User-Agent": UA})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def pick_video_file(video: dict[str, Any], orientation: str) -> dict[str, Any] | None:
    files = [
        f
        for f in video.get("video_files", [])
        if f.get("file_type") == "video/mp4" and f.get("link")
    ]
    if not files:
        return None

    def score(item: dict[str, Any]) -> tuple[int, int, int]:
        width = int(item.get("width") or 0)
        height = int(item.get("height") or 0)
        if orientation == "portrait":
            orient_penalty = 0 if height >= width else 1
            target_penalty = abs(height - 1280)
        elif orientation == "landscape":
            orient_penalty = 0 if width >= height else 1
            target_penalty = abs(width - 1280)
        else:
            orient_penalty = 0
            target_penalty = abs(max(width, height) - 1280)
        resolution_penalty = max(width * height, 0)
        return (orient_penalty, target_penalty, resolution_penalty)

    return sorted(files, key=score)[0]


def download(url: str, dest: Path, max_bytes: int, max_seconds: int) -> int:
    request = urllib.request.Request(url, headers={"User-Agent": UA})
    total = 0
    started = time.monotonic()
    tmp = dest.with_suffix(dest.suffix + ".part")
    try:
        with urllib.request.urlopen(request, timeout=90) as response, tmp.open("wb") as handle:
            length = response.headers.get("Content-Length")
            if length and int(length) > max_bytes:
                raise ValueError(f"remote file exceeds max bytes: {length}")
            while True:
                if time.monotonic() - started > max_seconds:
                    raise TimeoutError(f"download exceeded {max_seconds}s")
                chunk = response.read(1024 * 256)
                if not chunk:
                    break
                total += len(chunk)
                if total > max_bytes:
                    raise ValueError(f"download exceeds max bytes: {max_bytes}")
                handle.write(chunk)
        if total <= 0:
            raise ValueError("empty download")
        tmp.replace(dest)
        return total
    except Exception:
        tmp.unlink(missing_ok=True)
        dest.unlink(missing_ok=True)
        raise


def write_manifest(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in FIELDS})


def main() -> int:
    parser = argparse.ArgumentParser(description="Search Pexels and register stock football B-roll.")
    parser.add_argument("project", help="Football video project folder")
    parser.add_argument("--queries", required=True, help="Comma-separated search queries")
    parser.add_argument("--limit", type=int, default=8, help="Maximum downloaded/selected clips")
    parser.add_argument("--per-query", type=int, default=10, help="Pexels results per query")
    parser.add_argument(
        "--orientation",
        choices=["portrait", "landscape", "square", "any"],
        default="portrait",
    )
    parser.add_argument("--config", help="MoneyPrinterTurbo config.toml with Pexels key")
    parser.add_argument("--api-key-env", default="PEXELS_API_KEY")
    parser.add_argument("--dry-run", action="store_true", help="Write manifest without downloading files")
    parser.add_argument("--max-mb", type=int, default=80, help="Maximum size per downloaded file")
    parser.add_argument("--download-timeout", type=int, default=90, help="Maximum seconds per file")
    parser.add_argument(
        "--intended-use",
        default="generic football/referee B-roll only; do not present as exact match footage",
    )
    args = parser.parse_args()

    project = Path(args.project).expanduser().resolve()
    out_dir = project / "assets" / "source_clips" / "pexels_stock"
    manifest = project / "planning" / "stock_materials.csv"
    out_dir.mkdir(parents=True, exist_ok=True)

    api_key = load_pexels_key(args.config, args.api_key_env)
    queries = [q.strip() for q in args.queries.split(",") if q.strip()]
    max_bytes = args.max_mb * 1024 * 1024
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()

    for query in queries:
        if len([r for r in rows if r["status"] in {"downloaded", "selected"}]) >= args.limit:
            break
        try:
            data = pexels_search(query, api_key, args.per_query, args.orientation)
        except Exception as exc:
            rows.append(
                {
                    "provider": "pexels",
                    "query": query,
                    "status": "search_failed",
                    "notes": f"{type(exc).__name__}: {exc}",
                }
            )
            continue

        for video in data.get("videos", []):
            if len([r for r in rows if r["status"] in {"downloaded", "selected"}]) >= args.limit:
                break
            vid = str(video.get("id") or "")
            if not vid or vid in seen:
                continue
            seen.add(vid)
            video_file = pick_video_file(video, args.orientation)
            user = video.get("user") or {}
            base_row = {
                "id": vid,
                "provider": "pexels",
                "query": query,
                "duration": video.get("duration", ""),
                "width": video_file.get("width", "") if video_file else "",
                "height": video_file.get("height", "") if video_file else "",
                "source_url": video.get("url", ""),
                "credit": user.get("name", ""),
                "license_note": "Pexels free-use license; attribution not required but appreciated",
                "intended_use": args.intended_use,
            }
            if not video_file:
                rows.append({**base_row, "status": "no_mp4"})
                continue

            filename = f"pexels-{vid}-{slugify(query)}.mp4"
            dest = out_dir / filename
            rel_dest = dest.relative_to(project)
            if args.dry_run:
                rows.append({**base_row, "status": "selected", "file": str(rel_dest)})
                continue

            try:
                size = (
                    dest.stat().st_size
                    if dest.exists() and dest.stat().st_size > 0
                    else download(video_file["link"], dest, max_bytes, args.download_timeout)
                )
                rows.append({**base_row, "status": "downloaded", "file": str(rel_dest), "bytes": size})
            except Exception as exc:
                rows.append(
                    {
                        **base_row,
                        "status": "download_failed",
                        "file": str(rel_dest),
                        "notes": f"{type(exc).__name__}: {exc}",
                    }
                )
        time.sleep(0.25)

    write_manifest(manifest, rows)
    ok = len([r for r in rows if r["status"] in {"downloaded", "selected"}])
    print(f"selected={ok} manifest={manifest}")
    return 0 if ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
