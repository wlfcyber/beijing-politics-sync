from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / ".codex" / "advisor-runs" / "20260605_014440-gpt55-final-review-v8"
VERSION = "v8"

DOCS = {
    "compilation": {
        "label": "试题和细则汇编",
        "path": ROOT / "outputs" / f"选必二法律与生活_试题细则汇编_学生可发版_{VERSION}.md",
    },
    "baodian": {
        "label": "AB双轴学生宝典",
        "path": ROOT / "outputs" / f"选必二法律与生活_AB双轴学生宝典_学生可发版_{VERSION}.md",
    },
}


HEADER = """# External Review Context
You are GPT-5.5 Pro doing one chunk of a final review. Do not invent exam evidence, rubric facts, scoring rules, or legal facts. This is a partial chunk review; do not issue the final project verdict unless asked in a final synthesis prompt.

User requires exactly two student-facing DOCX documents for 选必二《法律与生活》:
1. 试题和细则汇编: all 2024-2026 选必二 subjective questions; each entry has 题目来源、材料、设问、细则、答案落点、同题组.
2. AB双轴学生宝典: A-axis legal relation framework + B-axis answer-shape framework; under each A-axis core point, core answer points/knowledge, then all related subjective questions with the same required fields.

Forbidden student-facing noise: 三十秒速记, engineering/production traces, internal E0xx IDs, source_id/SRC_, absolute local paths, TODO/BLOCKED, backend verification chatter, 制作记录, 命题人路径, 判题四步.

Current candidate is v8. Local QA reports: 74 分问, 64 同题组, 宝典核心轴 73 + 1 跨模块背景题, student-doc noise scan all 0 for 三十秒/工程/source_id/SRC_/entry_E/path/TODO/BLOCKED/E编号.

Important process constraint: any prior CLI-based Claude/GPT result is invalid for this project and must not be counted. This prompt is for a new valid web/app review pass only.

v8 specifically fixes the previous web GPT compilation-02 blockers:
- 2025 朝阳二模20(1): answer points no longer truncate; 第1问 and 第2问 are separated.
- 2025 朝阳期末20: 细则/答案落点 no longer leave 案件三裁判结果 as ④; materials still preserve original fill-in blanks ①②③④.
- 2026 东城期末18(2): answer points now include维权途径、证据、权利义务、合理诉求、不告不理原则.

Render QA: v8 DOCX rendered successfully. 汇编 136 pages, 宝典 143 pages. The above repaired pages were visually sampled from rendered PNGs.

For this chunk, identify only BLOCKING defects or significant NONBLOCKING issues visible in the chunk. If something depends on original exam images not present in this chunk, say what Codex must locally verify; do not invent corrected wording.
"""


TASK_TEMPLATE = """

# Chunk Task
Document: {doc_label}
Chunk: {idx}/3

Review this chunk for:
1. Any student-facing noise or backend trace.
2. Missing required fields in entries contained in this chunk.
3. Obvious answer/rubric/material incoherence visible from the text.
4. Any wording or structure issue that should block final delivery.
5. For AB handbook chunks, check whether 框架归位 and A-axis placement are visibly incoherent.

# Required Output
Return Chinese, compact:
- chunk_id: {doc_key}-{idx:02d}
- verdict: PASS / CONDITIONAL_PASS / FAIL for this chunk only
- BLOCKING defects: 无 if none
- NONBLOCKING issues: 无 if none
- Required local verification: 无 if none

# Chunk Content
```markdown
{content}
```
"""


def split_entries(text: str) -> list[str]:
    marker = "\n### "
    if marker not in text:
        return [text]
    pre, rest = text.split(marker, 1)
    parts = [pre.rstrip()]
    for block in rest.split(marker):
        parts.append("### " + block.strip())
    return [p for p in parts if p.strip()]


def chunk_text(text: str, n: int = 3) -> list[str]:
    parts = split_entries(text)
    target = max(1, len(text) // n)
    chunks: list[list[str]] = [[] for _ in range(n)]
    ci = 0
    size = 0
    for part in parts:
        if ci < n - 1 and chunks[ci] and size + len(part) > target:
            ci += 1
            size = 0
        chunks[ci].append(part)
        size += len(part)
    return ["\n\n".join(c).strip() for c in chunks]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for doc_key, meta in DOCS.items():
        text = meta["path"].read_text(encoding="utf-8")
        chunks = chunk_text(text, 3)
        for idx, content in enumerate(chunks, start=1):
            prompt = HEADER + TASK_TEMPLATE.format(
                doc_key=doc_key,
                doc_label=meta["label"],
                idx=idx,
                content=content,
            )
            path = OUT / f"GPT55_CHUNK_PROMPT_{doc_key}_{idx:02d}_of_3_{VERSION}.md"
            path.write_text(prompt, encoding="utf-8")
            print(path, len(prompt.encode("utf-8")))


if __name__ == "__main__":
    main()
