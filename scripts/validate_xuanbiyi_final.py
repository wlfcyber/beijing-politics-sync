from __future__ import annotations

import re
from pathlib import Path


ROOT = Path.cwd()
STUDENT = next(ROOT.rglob("选必一_当代国际政治与经济_主观题术语宝典_学生版.md"))
text = STUDENT.read_text(encoding="utf-8")

current_bucket: str | None = None
locations: dict[str, tuple[str, int]] = {}
for line in text.splitlines():
    if line.startswith("# ") and not line.startswith("## "):
        current_bucket = line[2:].strip()
    m = re.match(r"## 核心答题点：(.+?)（出现(\d+)次）", line)
    if m:
        locations[m.group(1)] = (current_bucket or "", int(m.group(2)))

expected = {
    "促进共同发展、维护持久和平 / 共同推进现代化": "政治多极化",
    "畅通全球供应链产业链，增强经济全球化活力，推动各国合作共赢": "经济全球化",
    "周边工作新局面四定位：发展繁荣的重要基础、维护国家安全的重点、运筹外交全局的首要、推动构建人类命运共同体的关键": "中国",
    "四大全球倡议相互促进、有机统一，系统推动构建人类命运共同体": "中国",
    "严格落实《巴黎协定》要求，每五年向联合国提交国家自主贡献目标，维护全球气候治理多边进程": "中国",
    "促进技术共享和民生改善；为全球可持续发展贡献力量": "中国",
    "联合国是当今世界最具普遍性、代表性和权威性的政府间国际组织，并在维护和平、推动发展、促进人类文明进步中发挥重要作用": "联合国",
    "联合国对中国对外开放和现代化事业作出独特贡献，成为中国开展多边合作的主要舞台": "联合国",
}

bad_core_titles = [
    "合作共赢；实现合作共赢；推动各国合作共赢",
    "优惠政策吸引高新技术企业入驻；降低企业税费成本；助力企业科技创新",
]

failures: list[str] = []
for title, bucket in expected.items():
    actual = locations.get(title)
    print(f"{title} => {actual}")
    if actual is None or actual[0] != bucket:
        failures.append(f"{title}: expected {bucket}, got {actual}")

for title in bad_core_titles:
    exists = title in locations
    print(f"bad_core {title} => {exists}")
    if exists:
        failures.append(f"{title}: should not be a main core node")

print(f"core_count={len(locations)}")
if failures:
    print("FAILURES:")
    for failure in failures:
        print(f"- {failure}")
    raise SystemExit(1)
