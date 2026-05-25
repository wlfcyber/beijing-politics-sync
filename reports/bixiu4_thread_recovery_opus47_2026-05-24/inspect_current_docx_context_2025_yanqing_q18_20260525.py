from __future__ import annotations

from pathlib import Path
from docx import Document


ROOT = Path(__file__).resolve().parent
DELIVERY = ROOT.parent / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24" / "05_delivery"
DOCX = next(p for p in DELIVERY.iterdir() if p.suffix.lower() == ".docx" and "backup" not in p.name)
OUT = ROOT / "CURRENT_DOCX_2025_YANQING_Q18_CONTEXT_20260525.md"

doc = Document(str(DOCX))
paras = [p for p in doc.paragraphs if p.text.strip()]
targets = [i for i, p in enumerate(paras) if "2025延庆一模" in p.text and "第18题" in p.text]

lines = [
    "# Current DOCX Context - 2025 Yanqing Q18",
    "",
    f"- DOCX: `{DOCX}`",
    f"- Target headings: `{len(targets)}`",
    "",
]
for target in targets:
    lines.append(f"## Around paragraph {target}")
    start = max(0, target - 4)
    end = min(len(paras), target + 18)
    for i in range(start, end):
        p = paras[i]
        lines.append(f"- `{i}` style=`{p.style.name}` text={p.text[:500]}")
    lines.append("")

OUT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
print(OUT)
