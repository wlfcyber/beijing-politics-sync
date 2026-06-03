#!/usr/bin/env python3
import csv
import json
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path


DISTRICTS = ["朝阳", "海淀", "丰台", "西城", "东城", "顺义", "石景山", "延庆", "门头沟", "房山", "通州", "昌平"]
EXAM_TYPES = ["期中", "期末", "一模", "二模", "三模"]
PUNCT_RE = re.compile(r"[\s　,，.。:：;；!！?？、'\"“”‘’（）()《》<>【】\\[\\]·—\\-]+")


def norm(text: str) -> str:
    return PUNCT_RE.sub("", text or "")


def parse_label(label: str):
    year = re.search(r"(20\d{2})", label)
    q = re.search(r"Q(\d+)(?:\((\d+)\))?", label)
    district = next((d for d in DISTRICTS if d in label), "")
    exam_type = next((t for t in EXAM_TYPES if t in label), "")
    return {
        "year": year.group(1) if year else "",
        "district": district,
        "exam_type": exam_type,
        "q_no": q.group(1) if q else "",
        "q_sub": q.group(2) if q and q.group(2) else "",
    }


def split_fragments(text: str, min_len=8):
    text = re.sub(r"【[^】]+】", "", text or "")
    parts = re.split(r"[，。；;、：:\n（）()]+", text)
    out = []
    for part in parts:
        n = norm(part)
        if len(n) >= min_len and not re.fullmatch(r"\d+", n):
            out.append(n)
    # Keep longer, information-rich fragments first.
    return sorted(set(out), key=len, reverse=True)


def best_fragment_match(fragments, text_norm):
    if not fragments or not text_norm:
        return "", 0
    for frag in fragments:
        if frag in text_norm:
            return frag, 1.0
    best_frag = ""
    best_score = 0.0
    for frag in fragments[:20]:
        if len(frag) < 12:
            continue
        # Cheap fuzzy score against a coarse search: only compare if several
        # characters overlap, otherwise this would be too slow/noisy.
        anchors = [frag[:6], frag[-6:]]
        if not any(a and a in text_norm for a in anchors):
            continue
        score = SequenceMatcher(None, frag, text_norm).quick_ratio()
        if score > best_score:
            best_frag = frag
            best_score = score
    return best_frag, best_score


def load_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def main() -> int:
    if len(sys.argv) != 5:
        print("usage: automated_source_audit.py ENTRY_INDEX.csv SOURCE_FILE_INVENTORY.csv TEXT_DIR OUTDIR", file=sys.stderr)
        return 2
    entries_path = Path(sys.argv[1])
    inv_path = Path(sys.argv[2])
    text_dir = Path(sys.argv[3])
    out_dir = Path(sys.argv[4])
    out_dir.mkdir(parents=True, exist_ok=True)

    entries = load_csv(entries_path)
    sources = load_csv(inv_path)
    text_cache = {}
    for src in sources:
        tp = Path(src["text_path"])
        try:
            text = tp.read_text(encoding="utf-8")
        except Exception:
            text = ""
        text_cache[src["file_id"]] = {
            "text": text,
            "norm": norm(text),
        }

    rows = []
    for entry in entries:
        meta = parse_label(entry["source_label"])
        candidates = []
        for src in sources:
            if meta["year"] and src["year"] != meta["year"]:
                continue
            if meta["district"] and src["district"] != meta["district"]:
                continue
            if meta["exam_type"] and src["exam_type"] != meta["exam_type"]:
                continue
            candidates.append(src)

        paper = [s for s in candidates if s["kind"] == "试卷"]
        rubric = [s for s in candidates if s["kind"] == "细则"]
        other = [s for s in candidates if s["kind"] not in {"试卷", "细则"}]

        readable = {"OK", "OCR_OK"}
        paper_norm = "\n".join(text_cache[s["file_id"]]["norm"] for s in paper if s["status"] in readable)
        rubric_norm = "\n".join(text_cache[s["file_id"]]["norm"] for s in rubric if s["status"] in readable)
        all_norm = paper_norm + "\n" + rubric_norm + "\n" + "\n".join(text_cache[s["file_id"]]["norm"] for s in other if s["status"] in readable)

        prompt_fragments = split_fragments(entry["prompt"], min_len=8)
        score_fragments = split_fragments(entry["score_layers"], min_len=5)
        surface_fragments = split_fragments(entry["surface_sentence"], min_len=8)

        prompt_exact = norm(entry["prompt"]) in paper_norm if entry["prompt"] and paper_norm else False
        prompt_frag, prompt_score = best_fragment_match(prompt_fragments, paper_norm)
        score_frag, score_score = best_fragment_match(score_fragments, rubric_norm)
        surface_frag, surface_score = best_fragment_match(surface_fragments, all_norm)

        q_forms = []
        if meta["q_no"]:
            n = meta["q_no"]
            sub = meta["q_sub"]
            q_forms = [f"{n}{sub}", f"{n}题", f"第{n}题", f"{n}.", f"{n}．", f"{n}、", f"{n} "]
        q_in_paper = any(norm(qf) in paper_norm for qf in q_forms) if q_forms else False
        q_in_rubric = any(norm(qf) in rubric_norm for qf in q_forms) if q_forms else False

        paper_statuses = sorted(set(s["status"] for s in paper))
        rubric_statuses = sorted(set(s["status"] for s in rubric))
        if not candidates:
            overall = "BLOCKED_NO_CANDIDATE_SOURCE"
        elif paper and all(s["status"] not in readable for s in paper):
            overall = "BLOCKED_PAPER_OCR_OR_EXTRACT"
        elif rubric and all(s["status"] not in readable for s in rubric):
            overall = "BLOCKED_RUBRIC_OCR_OR_EXTRACT"
        elif not paper:
            overall = "BLOCKED_NO_PAPER_FILE"
        elif not rubric:
            overall = "BLOCKED_NO_RUBRIC_FILE"
        elif entry["prompt"] and not (prompt_exact or prompt_frag):
            overall = "ISSUE_PROMPT_NOT_FOUND_AUTO"
        elif entry["score_layers"] and not score_frag:
            overall = "ISSUE_SCORE_LAYER_NOT_FOUND_AUTO"
        elif entry["surface_sentence"] and not surface_frag:
            overall = "NEEDS_MANUAL_SURFACE_CHECK"
        else:
            overall = "AUTO_LOCATED_NEEDS_MANUAL_CONFIRM"

        row = {
            "global_entry_no": entry["global_entry_no"],
            "source_label": entry["source_label"],
            "bucket": entry["bucket"],
            "second_level": entry["second_level"],
            "core_point": entry["core_point"],
            "year": meta["year"],
            "district": meta["district"],
            "exam_type": meta["exam_type"],
            "q_no": meta["q_no"],
            "q_sub": meta["q_sub"],
            "overall_auto_status": overall,
            "paper_count": len(paper),
            "rubric_count": len(rubric),
            "other_count": len(other),
            "paper_statuses": ";".join(paper_statuses),
            "rubric_statuses": ";".join(rubric_statuses),
            "q_in_paper": str(q_in_paper),
            "q_in_rubric": str(q_in_rubric),
            "prompt_exact": str(prompt_exact),
            "prompt_match_fragment": prompt_frag,
            "prompt_match_score": f"{prompt_score:.3f}",
            "score_match_fragment": score_frag,
            "score_match_score": f"{score_score:.3f}",
            "surface_match_fragment": surface_frag,
            "surface_match_score": f"{surface_score:.3f}",
            "paper_paths": " || ".join(s["path"] for s in paper),
            "rubric_paths": " || ".join(s["path"] for s in rubric),
            "other_paths": " || ".join(s["path"] for s in other),
            "prompt": entry["prompt"],
            "score_layers": entry["score_layers"],
            "surface_sentence": entry["surface_sentence"],
        }
        rows.append(row)

    fieldnames = list(rows[0].keys()) if rows else []
    with (out_dir / "AUTOMATED_AUDIT.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    with (out_dir / "AUTOMATED_AUDIT.jsonl").open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    summary = {"entries": len(rows), "by_status": {}}
    for row in rows:
        summary["by_status"][row["overall_auto_status"]] = summary["by_status"].get(row["overall_auto_status"], 0) + 1
    (out_dir / "automated_audit_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
