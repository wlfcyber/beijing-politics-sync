from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path.cwd()
RUN = next(p for p in (ROOT / "reports").glob("*") if (p / "02_codex_batches").exists())
FINAL_DIR = RUN / "06_final_handbook"
STUDENT = FINAL_DIR / "选必一_当代国际政治与经济_主观题术语宝典_学生版.md"
NAV = FINAL_DIR / "选必一_当代国际政治与经济_主观题术语宝典_考前导航版.md"
AUDIT = FINAL_DIR / "选必一_合并题例_初稿回源拆分审计.md"
BUILD_AUDIT = FINAL_DIR / "选必一_主观题术语宝典_学生版_构建审计.md"
GOVERNOR_AUDIT = FINAL_DIR / "选必一_宝典终稿_GOVERNOR_FINAL_AUDIT.md"


FIELD_MAP_OPUS = {
    "细则术语": "term",
    "参考答案术语": "term",
    "材料触发点": "trigger",
    "设问": "question",
    "为什么能想到": "why",
    "答案落点": "answer",
    "细则位置": "location",
    "来源": "source",
}

FIELD_MAP_DRAFT = {
    "完整设问": "question",
    "细则位置": "location",
    "来源": "source",
    "材料触发": "trigger",
    "答案句": "answer",
}

REQUIRED_FIELDS = {"term", "trigger", "question", "why", "answer", "location", "source"}


@dataclass
class SourceEntry:
    kind: str
    file: Path
    line: int
    title: str
    core_title: str
    fields: dict[str, str]
    keys: list[str]


def read(path: Path) -> str:
    for encoding in ("utf-8-sig", "utf-16", "gb18030"):
        try:
            return path.read_text(encoding=encoding).replace("\r\n", "\n").replace("\r", "\n")
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n").replace("\r", "\n")


def normalize_source_key(text: str) -> str | None:
    text = re.sub(r"[,，].*$", "", text or "")
    text = re.sub(r"\s+", "", text)
    pattern = re.compile(
        r"(20\d{2})([\u4e00-\u9fff]+?)(一模|二模|期中|期末)"
        r"(?:Q|第)?(\d+)(?:题)?(?:第?\(?(\d+)\)?问|\((\d+)\))?"
    )
    match = pattern.search(text)
    if not match:
        return None
    sub = match.group(5) or match.group(6) or ""
    key = f"{match.group(1)}{match.group(2)}{match.group(3)}Q{int(match.group(4))}"
    if sub:
        key += f"({int(sub)})"
    return key


def source_keys(text: str) -> list[str]:
    keys: list[str] = []
    for part in re.split(r"[；;\n]+", text or ""):
        key = normalize_source_key(part)
        if key and key not in keys:
            keys.append(key)
    return keys


def cjk_chars(text: str) -> set[str]:
    return set(re.findall(r"[\u4e00-\u9fff]", text or ""))


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def is_complete(entry: SourceEntry) -> bool:
    return REQUIRED_FIELDS <= set(entry.fields)


def add_entry(entries: list[SourceEntry], entry: SourceEntry) -> None:
    if not entry.keys:
        return
    if is_complete(entry):
        entries.append(entry)


def parse_opus_entries() -> list[SourceEntry]:
    entries: list[SourceEntry] = []
    for path in sorted((RUN / "07_claudecode_full_rerun" / "parts").glob("*.md")):
        lines = read(path).splitlines()
        core_title = ""
        current: dict[str, object] | None = None

        def finish() -> None:
            if not current:
                return
            fields = current["fields"]  # type: ignore[index]
            title = str(current["title"])
            keys = source_keys(str(fields.get("source", "")) + "\n" + title)  # type: ignore[union-attr]
            add_entry(
                entries,
                SourceEntry(
                    kind="opus",
                    file=path,
                    line=int(current["line"]),
                    title=title,
                    core_title=str(current["core_title"]),
                    fields=dict(fields),  # type: ignore[arg-type]
                    keys=keys,
                ),
            )

        for idx, line in enumerate(lines, 1):
            core_match = re.match(r"^### 核心答题点：(.+?)(?:（|\()出现\d+次", line)
            if core_match:
                core_title = core_match.group(1).strip()
            entry_match = re.match(r"^\*\*题例[^：:]*[：:](.+?)\*\*$", line)
            if entry_match:
                finish()
                current = {
                    "title": entry_match.group(1).strip(),
                    "line": idx,
                    "core_title": core_title,
                    "fields": {},
                }
                continue
            if current and line.startswith("- "):
                field_match = re.match(r"^-\s*【([^】]+)】\s*(.*)$", line)
                if not field_match:
                    continue
                label = field_match.group(1).strip()
                value = field_match.group(2).strip()
                mapped = FIELD_MAP_OPUS.get(label)
                if mapped:
                    fields = current["fields"]  # type: ignore[index]
                    fields[mapped] = value  # type: ignore[index]
                    if mapped == "term":
                        fields["term_label"] = label  # type: ignore[index]
        finish()
    return entries


def parse_initial_draft_entries() -> list[SourceEntry]:
    entries: list[SourceEntry] = []
    for folder, kind in [("02_codex_batches", "codex"), ("02_claudecode_batches", "claudecode")]:
        for path in sorted((RUN / folder).glob("*.md")):
            lines = read(path).splitlines()
            core_title = ""
            current: dict[str, object] | None = None

            def finish() -> None:
                if not current:
                    return
                fields = current["fields"]  # type: ignore[index]
                title = str(current["title"])
                if "参考答案" in " ".join(str(fields.get(k, "")) for k in ("source", "location")):
                    fields["term_label"] = "参考答案术语"  # type: ignore[index]
                else:
                    fields["term_label"] = "细则术语"  # type: ignore[index]
                keys = source_keys(str(fields.get("source", "")) + "\n" + title)  # type: ignore[union-attr]
                # Early Codex/ClaudeCode drafts did not have a separate why field.
                # Keep them indexed for audit fallback, but do not auto-render them into the final document.
                add_entry(
                    entries,
                    SourceEntry(
                        kind=kind,
                        file=path,
                        line=int(current["line"]),
                        title=title,
                        core_title=str(current["core_title"]),
                        fields=dict(fields),  # type: ignore[arg-type]
                        keys=keys,
                    ),
                )

            for idx, line in enumerate(lines, 1):
                if line.startswith("### "):
                    core_title = line[4:].strip()
                entry_match = re.match(r"^\*\*术语[：:](.+?)\*\*$", line)
                if entry_match:
                    finish()
                    term = entry_match.group(1).strip()
                    current = {
                        "title": term,
                        "line": idx,
                        "core_title": core_title,
                        "fields": {"term": term},
                    }
                    continue
                if current and line.startswith("- "):
                    field_match = re.match(r"^-\s*([^：:]+)[：:]\s*(.*)$", line)
                    if not field_match:
                        continue
                    label = field_match.group(1).strip()
                    value = field_match.group(2).strip()
                    mapped = FIELD_MAP_DRAFT.get(label)
                    if mapped:
                        fields = current["fields"]  # type: ignore[index]
                        fields[mapped] = value  # type: ignore[index]
            finish()
    return entries


def build_source_index() -> dict[str, list[SourceEntry]]:
    entries = parse_opus_entries() + parse_initial_draft_entries()
    index: dict[str, list[SourceEntry]] = {}
    for entry in entries:
        for key in entry.keys:
            index.setdefault(key, []).append(entry)
    return index


def score_entry(entry: SourceEntry, core_title: str, final_example: str) -> float:
    term = entry.fields.get("term", "")
    base = {"opus": 40.0, "codex": 20.0, "claudecode": 15.0}.get(entry.kind, 0.0)
    core_score = 80.0 * jaccard(cjk_chars(core_title), cjk_chars(entry.core_title + term))

    final_term = ""
    term_match = re.search(r"【(?:细则术语|参考答案术语)】([^\n]+)", final_example)
    if term_match:
        final_term = term_match.group(1)
    term_score = 80.0 * jaccard(cjk_chars(final_term), cjk_chars(term))
    exact_bonus = 0.0
    if core_title and (core_title in entry.core_title or core_title in term):
        exact_bonus += 60.0
    if final_term and final_term in term:
        exact_bonus += 30.0
    complete_bonus = 20.0 if is_complete(entry) else 0.0
    return base + core_score + term_score + exact_bonus + complete_bonus


def select_entry(
    index: dict[str, list[SourceEntry]], key: str, core_title: str, final_example: str
) -> tuple[SourceEntry | None, float, str]:
    candidates = [entry for entry in index.get(key, []) if is_complete(entry)]
    if not candidates:
        return None, 0.0, "未找到具备七字段的初稿单题条目"
    best = max(candidates, key=lambda entry: score_entry(entry, core_title, final_example))
    score = score_entry(best, core_title, final_example)
    if score < 95.0:
        return None, score, f"候选相似度不足：{best.kind} {best.core_title}"
    return best, score, ""


def render_source_example(entry: SourceEntry) -> str:
    label = entry.fields.get("term_label") or "细则术语"
    lines = [
        f"### 0. {entry.title}",
        "",
        f"【{label}】{entry.fields['term']}",
        "",
        f"【材料触发点】{entry.fields['trigger']}",
        "",
        f"【设问】{entry.fields['question']}",
        "",
        f"【为什么能想到】{entry.fields['why']}",
        "",
        f"【答案落点】{entry.fields['answer']}",
        "",
        f"【细则位置】{entry.fields['location']}",
        "",
        f"【来源】{entry.fields['source']}",
    ]
    return "\n".join(lines)


def split_examples(block_text: str) -> tuple[str, list[str]]:
    matches = list(re.finditer(r"(?m)^### \d+\. .*$", block_text))
    if not matches:
        return block_text.strip(), []
    prefix = block_text[: matches[0].start()].strip("\n")
    examples = []
    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(block_text)
        examples.append(block_text[start:end].strip("\n"))
    return prefix, examples


def renumber_examples(examples: list[str]) -> list[str]:
    out = []
    for idx, example in enumerate(examples, 1):
        out.append(re.sub(r"^### \d+\.", f"### {idx}.", example, count=1, flags=re.M))
    return out


def update_block_counts(core_title: str, prefix: str, examples: list[str]) -> str:
    count = len(examples)
    text = prefix + "\n\n" + "\n\n".join(renumber_examples(examples))
    text = re.sub(
        r"^## 核心答题点：.+?（出现\d+次）",
        f"## 核心答题点：{core_title}（出现{count}次）",
        text,
        count=1,
        flags=re.M,
    )
    text = re.sub(r"【本节点真题】共 \d+ 条。", f"【本节点真题】共 {count} 条。", text, count=1)
    return text.strip()


def transform_student(text: str, index: dict[str, list[SourceEntry]]) -> tuple[str, list[dict[str, object]]]:
    block_pattern = re.compile(
        r"(?ms)^## 核心答题点：(.+?)（出现\d+次）.*?(?=^## 核心答题点：|^# |\Z)"
    )
    records: list[dict[str, object]] = []
    pieces: list[str] = []
    cursor = 0

    for block_match in block_pattern.finditer(text):
        pieces.append(text[cursor : block_match.start()])
        block = block_match.group(0).strip()
        core_title = block_match.group(1)
        prefix, examples = split_examples(block)
        new_examples: list[str] = []
        changed = False

        for example in examples:
            first_line = example.splitlines()[0] if example.splitlines() else ""
            heading_match = re.match(r"^### \d+\. (.+)$", first_line)
            heading = heading_match.group(1) if heading_match else ""
            if "；" not in heading and ";" not in heading:
                new_examples.append(example)
                continue

            parts = [part.strip() for part in re.split(r"[；;]", heading) if part.strip()]
            resolved: list[tuple[str, str, SourceEntry, float]] = []
            unresolved: list[str] = []
            for part in parts:
                key = normalize_source_key(part)
                if not key:
                    unresolved.append(f"{part}：无法识别题号")
                    continue
                entry, score, reason = select_entry(index, key, core_title, example)
                if entry is None:
                    unresolved.append(f"{part}：{reason}（score={score:.1f}）")
                else:
                    resolved.append((part, key, entry, score))

            if unresolved:
                new_examples.append(example)
                records.append(
                    {
                        "status": "unresolved",
                        "core": core_title,
                        "heading": heading,
                        "unresolved": unresolved,
                    }
                )
                continue

            changed = True
            rendered = [render_source_example(entry) for _, _, entry, _ in resolved]
            new_examples.extend(rendered)
            records.append(
                {
                    "status": "split",
                    "core": core_title,
                    "heading": heading,
                    "sources": [
                        {
                            "part": part,
                            "key": key,
                            "kind": entry.kind,
                            "file": str(entry.file.relative_to(ROOT)),
                            "line": entry.line,
                            "source_core": entry.core_title,
                            "term": entry.fields.get("term", ""),
                            "score": round(score, 1),
                        }
                        for part, key, entry, score in resolved
                    ],
                }
            )

        if changed:
            pieces.append(update_block_counts(core_title, prefix, new_examples).rstrip() + "\n\n")
        else:
            pieces.append(block.rstrip() + "\n\n")
        cursor = block_match.end()

    pieces.append(text[cursor:])
    return "".join(pieces).rstrip() + "\n", records


def load_fuse_helpers():
    script = ROOT / "scripts" / "fuse_xuanbiyi_opus47_final.py"
    spec = importlib.util.spec_from_file_location("fuse_xuanbiyi_opus47_final", script)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import {script}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def update_navigation(new_text: str) -> None:
    helpers = load_fuse_helpers()
    preface, buckets = helpers.parse_student(new_text)
    NAV.write_text(helpers.make_navigation(buckets), encoding="utf-8", newline="\n")


def refresh_student_preface_counts(new_text: str) -> str:
    helpers = load_fuse_helpers()
    preface, buckets = helpers.parse_student(new_text)
    preface = helpers.update_preface_counts(preface, buckets)
    return helpers.render_student(preface, buckets)


def make_audit(records: list[dict[str, object]], before_text: str, after_text: str) -> str:
    split_records = [r for r in records if r["status"] == "split"]
    unresolved_records = [r for r in records if r["status"] == "unresolved"]
    before_examples = len(re.findall(r"(?m)^### \d+\. ", before_text))
    after_examples = len(re.findall(r"(?m)^### \d+\. ", after_text))
    lines = [
        "# 选必一合并题例初稿回源拆分审计",
        "",
        "- 原则：只从 Codex 初稿、ClaudeCode 初稿、ClaudeCode Opus 4.7 全量重跑稿中抽取已经独立存在的单题条目；不从终稿合并文本望文生义拆分。",
        f"- 拆分前题例数：{before_examples}",
        f"- 拆分后题例数：{after_examples}",
        f"- 成功拆分合并题例：{len(split_records)}",
        f"- 未拆分保留：{len(unresolved_records)}",
        "",
        "## 已拆分",
    ]
    for idx, record in enumerate(split_records, 1):
        lines.extend(
            [
                "",
                f"### {idx}. {record['core']}",
                f"- 原合并标题：{record['heading']}",
            ]
        )
        for source in record["sources"]:  # type: ignore[index]
            lines.append(
                "- 回源条目："
                f"{source['part']} | {source['kind']} | {source['file']}:{source['line']} | "
                f"源节点：{source['source_core']} | score={source['score']} | 术语：{source['term']}"
            )

    lines.extend(["", "## 未拆分保留"])
    if not unresolved_records:
        lines.append("")
        lines.append("- 无。")
    for idx, record in enumerate(unresolved_records, 1):
        lines.extend(
            [
                "",
                f"### {idx}. {record['core']}",
                f"- 原合并标题：{record['heading']}",
            ]
        )
        for item in record["unresolved"]:  # type: ignore[index]
            lines.append(f"- 原因：{item}")
    return "\n".join(lines).rstrip() + "\n"


def update_count_lines(new_text: str) -> None:
    helpers = load_fuse_helpers()
    preface, buckets = helpers.parse_student(new_text)
    counts = {name: sum(helpers.block_count_from_title(b) for b in bucket.blocks) for name, bucket in buckets.items()}
    core_counts = {name: len(bucket.blocks) for name, bucket in buckets.items()}
    total_main = sum(counts.get(name, 0) for name in helpers.BUCKETS if name != "附：模块边界 / 跨书提示")
    total_all = len(re.findall(r"(?m)^### \d+\. ", new_text))
    boundary_count = total_all - total_main
    total_core = sum(core_counts.get(name, 0) for name in helpers.BUCKETS if name != "附：模块边界 / 跨书提示")

    if BUILD_AUDIT.exists():
        audit = BUILD_AUDIT.read_text(encoding="utf-8")
        audit = re.sub(r"- 输出题例：.+", f"- 输出题例：{total_all}（选必一主链{total_main}条，附录模块边界{boundary_count}条不计入背诵优先级）", audit)
        audit = re.sub(r"- 输出核心节点：\d+", f"- 输出核心节点：{total_core}", audit)
        for name in ["时代背景", "理论", "经济全球化", "政治多极化", "中国", "联合国", "附：总说句 / 兜底加分表达"]:
            audit = re.sub(
                rf"- {re.escape(name)}：\d+个核心节点，\d+条题例",
                f"- {name}：{core_counts[name]}个核心节点，{counts[name]}条题例",
                audit,
            )
        note = "- 2026-05-18 初稿回源拆分补丁：已把可回源的合并题例拆回单题案例；未找到七字段单题初稿的合并项保留并写入审计。"
        if note not in audit:
            audit = audit.rstrip() + "\n" + note + "\n"
        BUILD_AUDIT.write_text(audit, encoding="utf-8", newline="\n")

    if GOVERNOR_AUDIT.exists():
        gov = GOVERNOR_AUDIT.read_text(encoding="utf-8")
        section = "\n".join(
            [
                "## 2026-05-18 合并题例初稿回源拆分",
                "",
                "- 本轮只拆分能在 Codex 初稿、ClaudeCode 初稿或 ClaudeCode Opus 4.7 全量重跑稿中定位到七字段单题条目的合并题例。",
                f"- 拆分后选必一主链题例数：{total_main}；附录模块边界：{boundary_count}。",
                "- 未回源成功的合并题例没有凭终稿文本拆分，详见《选必一_合并题例_初稿回源拆分审计.md》。",
            ]
        )
        if "## 2026-05-18 合并题例初稿回源拆分" in gov:
            gov = re.sub(
                r"(?ms)^## 2026-05-18 合并题例初稿回源拆分.*?(?=^## |\Z)",
                section + "\n\n",
                gov,
            ).rstrip() + "\n"
        else:
            gov = gov.rstrip() + "\n\n" + section + "\n"
        GOVERNOR_AUDIT.write_text(gov, encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write transformed handbook and audit")
    args = parser.parse_args()

    before_text = read(STUDENT)
    index = build_source_index()
    after_text, records = transform_student(before_text, index)
    after_text = refresh_student_preface_counts(after_text)
    audit = make_audit(records, before_text, after_text)

    split_count = sum(1 for r in records if r["status"] == "split")
    unresolved_count = sum(1 for r in records if r["status"] == "unresolved")
    before_examples = len(re.findall(r"(?m)^### \d+\. ", before_text))
    after_examples = len(re.findall(r"(?m)^### \d+\. ", after_text))
    print(f"source_keys={len(index)}")
    print(f"split_records={split_count}")
    print(f"unresolved_records={unresolved_count}")
    print(f"examples_before={before_examples}")
    print(f"examples_after={after_examples}")

    if not args.write:
        print("dry_run=1")
        return

    STUDENT.write_text(after_text, encoding="utf-8", newline="\n")
    update_navigation(after_text)
    AUDIT.write_text(audit, encoding="utf-8", newline="\n")
    update_count_lines(after_text)
    print(f"wrote={STUDENT}")
    print(f"wrote={NAV}")
    print(f"wrote={AUDIT}")


if __name__ == "__main__":
    main()
