from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
RUN = next((REPO / "reports").glob("*2026-05-16/11_strict_final_rebuild_2026-05-23"))
REQ = Path(r"C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbiyi\references\current-user-requirements.md")
PROTO = Path(r"C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbiyi\references\xuanbiyi-term-protocol.md")


def read(path: Path, limit: int | None = None) -> str:
    text = path.read_text(encoding="utf-8")
    if limit and len(text) > limit:
        return text[:limit] + f"\n\n[TRUNCATED at {limit} chars; source path: {path}]\n"
    return text


def main() -> None:
    out_dir = RUN / "07_gpt_pro_fusion"
    out_dir.mkdir(parents=True, exist_ok=True)

    codex_draft = RUN / "05_codex_drafts" / "CODEX_INDEPENDENT_THICK_DRAFT.md"
    codex_adj = RUN / "05_codex_drafts" / "CODEX_INDEPENDENT_ADJUDICATION.md"
    claude_dir = RUN / "06_claudecode_independent_opus47"
    claude_draft = claude_dir / "CLAUDECODE_INDEPENDENT_THICK_DRAFT.md"
    claude_adj = claude_dir / "CLAUDECODE_INDEPENDENT_ADJUDICATION.md"
    claude_risk = claude_dir / "CLAUDECODE_INDEPENDENT_RISK_LOG.md"

    missing = [p for p in [codex_draft, codex_adj, claude_draft, claude_adj, claude_risk] if not p.exists()]
    if missing:
        raise SystemExit("Missing required fusion inputs:\n" + "\n".join(str(p) for p in missing))

    prompt = f"""# GPT Pro 主融合任务：选必一严格最终稿

你是 GPT Pro 主融合线。请同时审阅 Codex 独立厚稿与 ClaudeCode Opus 独立厚稿，按原始细则证据、设问和材料触发关系做主融合。你的输出将作为最终宝典合入的主依据；Codex 后续只做证据回查、格式落盘和 Governor 校验。

## 必须遵守的硬规则

1. 只处理选择性必修一《当代国际政治与经济》主观题。
2. 主表必须有同题评分细则、评标、阅卷细则、讲评 PPT/讲评材料或用户确认细则。普通参考答案不能冒充主链细则。
3. 题例层面严禁合并两个题。每道题、每个采分句都要单题独立展示。
4. 术语必须尽量保留评分源原词；若只是你自己的概括，只能当容器标题，不能写进“细则术语”。
5. “合作共赢的新型国际关系 / 新型国际关系 / 国际关系民主化 / 真正的多边主义 / 国际秩序公正合理”归入“政治多极化”，不要放入“理论”。
6. “独立自主和平外交政策 / 和平共处五项原则 / 独立自主的基本立场”归入“中国”。
7. 经济全球化内部必须严格看表述是否接近、是否可在卷面互相替代、是否在同一细则点列为替代表述；不要把开放型世界经济、开放型经济、全球经济治理规则、贸易自由化、普惠包容全球化等远距离术语塞成一个核心点。
8. 对证据不足的题，输出 `NEEDS_EVIDENCE`，不要为了覆盖率硬收。
9. 如果 Codex 和 ClaudeCode 冲突，请按源证据裁决，并说明保留/驳回理由。

## 你需要输出的格式

请输出四部分：

### A. 主融合裁决总表

表格列：`来源题`、`Codex判断`、`ClaudeCode判断`、`GPT Pro裁决`、`归桶`、`理由`。

### B. 可直接合入学生宝典的融合条目

按六桶组织：`时代背景 / 理论 / 经济全球化 / 政治多极化 / 中国 / 联合国`。

每个条目必须是单题独立，并保留以下字段：

`【细则术语】`
`【卷面使用】`（如无必要可省略）
`【材料触发点】`
`【设问】`
`【为什么能想到】`
`【答案落点】`
`【细则位置】`
`【来源】`

### C. 驳回与降级清单

列出你驳回、降级或要求继续回源的题，并给出原因。

### D. 合入注意事项

指出哪些条目要拆点进不同核心，哪些不能合并，哪些归桶容易错。

---

# 固定用户要求摘录

{read(REQ, 12000)}

---

# 选必一术语协议摘录

{read(PROTO, 16000)}

---

# Codex 独立裁决表

{read(codex_adj, 22000)}

---

# Codex 独立厚稿

{read(codex_draft, 38000)}

---

# ClaudeCode 独立裁决表

{read(claude_adj, 30000)}

---

# ClaudeCode 独立厚稿

{read(claude_draft, 60000)}

---

# ClaudeCode 风险日志

{read(claude_risk, 20000)}
"""

    prompt_path = out_dir / "GPT_PRO_FUSION_PROMPT.md"
    prompt_path.write_text(prompt, encoding="utf-8")
    print(prompt_path)
    print(len(prompt))


if __name__ == "__main__":
    main()
