import re
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
RUN = next((REPO / "reports").glob("*2026-05-16/11_strict_final_rebuild_2026-05-23"))


def split_claude_entries(text: str):
    bucket = ""
    node = ""
    entries = []
    current = []
    for line in text.splitlines():
        if line.startswith("## "):
            if current:
                entries.append((bucket, node, "\n".join(current).strip()))
                current = []
            bucket = line[3:].strip()
            node = ""
            continue
        if line.startswith("### "):
            if current:
                entries.append((bucket, node, "\n".join(current).strip()))
                current = []
            node = line[4:].strip()
            continue
        if line.startswith("**术语："):
            if current:
                entries.append((bucket, node, "\n".join(current).strip()))
                current = []
            current.append(f"## {bucket}\n### {node}\n{line}")
        elif current:
            current.append(line)
    if current:
        entries.append((bucket, node, "\n".join(current).strip()))
    return [e for e in entries if e[2].strip()]


def main() -> None:
    out_dir = RUN / "07_gpt_pro_fusion" / "batches"
    out_dir.mkdir(parents=True, exist_ok=True)
    text = (RUN / "06_claudecode_independent_opus47" / "CLAUDECODE_INDEPENDENT_THICK_DRAFT.md").read_text(encoding="utf-8")
    entries = split_claude_entries(text)
    batch_size = 5
    for i in range(0, len(entries), batch_size):
        batch = entries[i:i + batch_size]
        body = "\n\n---\n\n".join(e[2] for e in batch)
        prompt = f"""# GPT Pro 小批次审核融合 {i//batch_size + 1}

请审核下面 5 个以内的选必一单题条目。任务不是重写整本书，只做本批条目的主融合裁决。

输出三部分：
1. `裁决表`：逐条写 `ACCEPT / REVISE / REJECT / NEEDS_EVIDENCE`、归桶、理由。
2. `修正后的可合入条目`：只输出 ACCEPT 或 REVISE 后可直接合入的条目，保留原字段。
3. `风险提示`：是否有错误归桶、证据不足、两题合并、经济全球化宽泛合并等问题。

硬规则：
- 只收有评分细则/评标/阅卷/讲评证据的选必一主观题点。
- 普通参考答案只降级，不能冒充细则。
- 每个条目必须单题独立，绝不合并两道题。
- 新型国际关系/国际关系民主化/真正的多边主义/国际秩序公正合理归政治多极化。
- 独立自主和平外交政策/和平共处五项原则归中国。
- 经济全球化内部按细则表述和卷面可替代性细分。

## 待审核条目

{body}
"""
        path = out_dir / f"GPT_PRO_BATCH_{i//batch_size + 1:02d}_PROMPT.md"
        path.write_text(prompt, encoding="utf-8")
    print(out_dir)
    print(len(entries))
    print((len(entries) + batch_size - 1) // batch_size)


if __name__ == "__main__":
    main()
