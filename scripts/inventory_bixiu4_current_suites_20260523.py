from __future__ import annotations

import csv
import re
from collections import Counter
from datetime import datetime
from pathlib import Path


DESKTOP = Path.home() / "Desktop"
ROOT = DESKTOP / "02_代码项目与工具" / "mac-thread-restore" / "beijing-politics-sync-visible"
RUN = ROOT / "reports" / "bixiu4_philosophy_strict_v8_2026-05-23"

SOURCE_ROOTS = [
    DESKTOP / "2024各区模拟题",
    DESKTOP / "2025各区模拟题",
    DESKTOP / "2026各区模拟题",
]

OLD_ROSTER = ROOT / "artifacts" / "desktop_exports_2026-04-29" / "4.29凌晨跑完的结果v6" / "04_过程日志" / "SUITE_ROSTER.csv"
MAIN_CACHE_MANIFEST = ROOT / "data" / "preprocessed_corpus" / "manifest.csv"
SECOND_MOCK_MANIFEST = ROOT / "reports" / "选必一_哲学宝典式重建_2026-05-16" / "08_2026_second_mock_backfill" / "00_extracted_text" / "manifest.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def count_files(suite_dir: Path) -> dict[str, int]:
    files = [p for p in suite_dir.rglob("*") if p.is_file()]
    return {
        "file_count": len(files),
        "paper_like_files": sum(1 for p in files if "试卷" in str(p) or "教师版" in p.name or "政治" in p.name),
        "rubric_like_files": sum(1 for p in files if any(k in str(p) for k in ["细则", "评标", "阅卷", "答案", "讲评"])),
    }


def collect_source_dirs() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    suite_rows: list[dict[str, object]] = []
    excluded_rows: list[dict[str, object]] = []
    for root in SOURCE_ROOTS:
        if not root.exists():
            continue
        for stage in sorted([p for p in root.iterdir() if p.is_dir()]):
            for suite in sorted([p for p in stage.iterdir() if p.is_dir()]):
                if not re.match(r"^202[456]", suite.name):
                    continue
                info = {
                    "suite_name": suite.name,
                    "year_root": root.name,
                    "stage": stage.name,
                    "full_path": str(suite),
                    **count_files(suite),
                }
                if stage.name == "其他材料" or "试题分类" in suite.name or "按模块" in suite.name:
                    info["exclude_reason"] = "classification_bundle_not_independent_suite"
                    excluded_rows.append(info)
                else:
                    suite_rows.append(info)
    return suite_rows, excluded_rows


def manifest_hit_counter(rows: list[dict[str, str]]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for row in rows:
        blob = " ".join(str(v) for v in row.values())
        for match in re.findall(r"202[456][\u4e00-\u9fff]+(?:一模|二模|期中|期末)", blob):
            counter[match] += 1
    return counter


def main() -> None:
    RUN.mkdir(parents=True, exist_ok=True)
    old_roster = read_csv(OLD_ROSTER)
    old_names = {row["suite_name"] for row in old_roster}
    source_dirs, excluded_dirs = collect_source_dirs()
    source_by_name = {row["suite_name"]: row for row in source_dirs}

    main_cache_hits = manifest_hit_counter(read_csv(MAIN_CACHE_MANIFEST))
    second_mock_hits = manifest_hit_counter(read_csv(SECOND_MOCK_MANIFEST))

    new_names = sorted(set(source_by_name) - old_names)
    old_names_not_standalone_dir = sorted(old_names - set(source_by_name))

    formal_rows: list[dict[str, object]] = []
    for row in old_roster:
        suite = row["suite_name"]
        src = source_by_name.get(suite, {})
        formal_rows.append(
            {
                "suite_name": suite,
                "suite_id_old": row.get("suite_id", ""),
                "inventory_status": "old_56_existing",
                "stage": row.get("stage", ""),
                "priority_bucket": row.get("priority_bucket", ""),
                "source_path": src.get("full_path", row.get("bundle_path", "")),
                "source_path_type": "standalone_dir" if src else "old_roster_supplement_or_cache",
                "file_count": src.get("file_count", ""),
                "paper_like_files": src.get("paper_like_files", ""),
                "rubric_like_files": src.get("rubric_like_files", ""),
                "main_cache_manifest_hits": main_cache_hits[suite],
                "second_mock_extract_hits": second_mock_hits[suite],
                "v8_scope_action": "rework_under_strict_gate",
                "notes": row.get("notes", ""),
            }
        )

    next_id = len(old_roster) + 1
    for suite in new_names:
        src = source_by_name[suite]
        is_second_mock = "二模" in str(src["stage"])
        has_backfill = second_mock_hits[suite] > 0
        formal_rows.append(
            {
                "suite_name": suite,
                "suite_id_old": f"S{next_id:03d}",
                "inventory_status": "new_after_old_56",
                "stage": src["stage"],
                "priority_bucket": "new-2026-second-mock" if is_second_mock else "new-2026-first-mock",
                "source_path": src["full_path"],
                "source_path_type": "standalone_dir",
                "file_count": src["file_count"],
                "paper_like_files": src["paper_like_files"],
                "rubric_like_files": src["rubric_like_files"],
                "main_cache_manifest_hits": main_cache_hits[suite],
                "second_mock_extract_hits": second_mock_hits[suite],
                "v8_scope_action": "use_second_mock_backfill_and_full_v8_review" if has_backfill else "must_preprocess_then_full_v8_review",
                "notes": "新增 2026 二模" if is_second_mock else "新增旧 roster 未覆盖套卷",
            }
        )
        next_id += 1

    write_csv(
        RUN / "current_65_suite_roster.csv",
        formal_rows,
        [
            "suite_name",
            "suite_id_old",
            "inventory_status",
            "stage",
            "priority_bucket",
            "source_path",
            "source_path_type",
            "file_count",
            "paper_like_files",
            "rubric_like_files",
            "main_cache_manifest_hits",
            "second_mock_extract_hits",
            "v8_scope_action",
            "notes",
        ],
    )
    write_csv(
        RUN / "raw_source_suite_dirs.csv",
        source_dirs,
        ["suite_name", "year_root", "stage", "full_path", "file_count", "paper_like_files", "rubric_like_files"],
    )
    write_csv(
        RUN / "excluded_non_suite_source_dirs.csv",
        excluded_dirs,
        ["suite_name", "year_root", "stage", "full_path", "file_count", "paper_like_files", "rubric_like_files", "exclude_reason"],
    )

    by_stage = Counter(row["stage"] for row in formal_rows)
    by_status = Counter(row["inventory_status"] for row in formal_rows)
    by_action = Counter(row["v8_scope_action"] for row in formal_rows)

    report = [
        "# 当前必修四哲学宝典题源范围核查：65 套",
        "",
        f"生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## 结论",
        "",
        "**当前不能继续按 56 套验收。严格题源基数应改为 65 套。**",
        "",
        "旧 56 套仍然保留，其中 `2024门头沟一模` 不是独立套卷目录，而是旧流程通过 `202404各区一模试题分类（按模块）` 与补源答案 PDF 建立的 formal suite row。新增范围为 `2026通州一模` + 8 套 `2026各区二模`，共 9 套。",
        "",
        "## 数字核对",
        "",
        f"- 旧 roster：{len(old_roster)} 套。",
        f"- 桌面独立套卷目录：{len(source_dirs)} 个。",
        f"- 排除的非独立套卷目录：{len(excluded_dirs)} 个。",
        f"- 旧 roster 中没有独立目录、但仍应保留的 formal suite：{len(old_names_not_standalone_dir)} 个。",
        f"- 新增 formal suite：{len(new_names)} 套。",
        f"- 当前 formal suite 总数：{len(formal_rows)} 套。",
        "",
        "## 按阶段统计",
        "",
    ]
    for stage, count in sorted(by_stage.items()):
        report.append(f"- {stage}：{count} 套")

    report.extend(["", "## 新增 9 套", ""])
    for suite in new_names:
        row = source_by_name[suite]
        report.append(
            f"- {suite}（{row['stage']}）：文件 {row['file_count']}，试卷类 {row['paper_like_files']}，细则/评标/答案类 {row['rubric_like_files']}；处理动作："
            f"{'使用二模 backfill 后严格复核' if second_mock_hits[suite] else '先预处理再全量复核'}。"
        )

    report.extend(["", "## 旧 roster 特殊边界", ""])
    for suite in old_names_not_standalone_dir:
        report.append(f"- {suite}：旧 roster 中存在，但桌面没有独立同名套卷目录；不得删除，按旧补源边界继续作为 formal suite。")
    for row in excluded_dirs:
        report.append(f"- 不另算套卷：{row['suite_name']}，原因：{row['exclude_reason']}。")

    report.extend(["", "## 缓存状态", ""])
    report.append("- 主缓存 `data/preprocessed_corpus/manifest.csv` 未命中新增 9 套。")
    report.append("- 8 套 2026 二模已在 `08_2026_second_mock_backfill/00_extracted_text/manifest.csv` 中有 24 行提取记录。")
    report.append("- `2026通州一模` 当前只有桌面 PDF 和评标 PDF，未进主缓存，v8 开始前必须先预处理/OCR。")

    report.extend(["", "## 对 v8 的影响", ""])
    report.append("1. `STRICT_GATE_REPORT.md` 里的旧 56 套缺口仍成立，但它只是旧基数审计，不再是总范围。")
    report.append("2. v8 控制矩阵必须扩展到 65 套，新增 9 套不能只做附录。")
    report.append("3. 2026 二模 A/B/C 分级要并入 65 套总清单；`2026通州一模` 要从零走缓存、题目、答案、细则、选择题和主观题边界。")
    report.append("4. 最终 Word 不能叫“56 套全覆盖”，应按“当前 65 套题源范围”验收。")

    report.extend(["", "## 输出文件", ""])
    report.append("- `current_65_suite_roster.csv`：65 套 formal suite 总清单。")
    report.append("- `raw_source_suite_dirs.csv`：桌面独立套卷目录原始清单。")
    report.append("- `excluded_non_suite_source_dirs.csv`：被排除的非独立套卷目录。")
    write_text(RUN / "CURRENT_SUITE_INVENTORY_65.md", "\n".join(report) + "\n")


if __name__ == "__main__":
    main()
