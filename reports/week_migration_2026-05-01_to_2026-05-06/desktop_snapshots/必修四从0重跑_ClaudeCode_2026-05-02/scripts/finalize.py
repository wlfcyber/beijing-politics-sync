#!/usr/bin/env python3
"""一键汇总：fixup → quality_check → synthesize_student → synthesize_word → build_audit_files。"""
from __future__ import annotations
import json, re, subprocess, sys
from pathlib import Path
from collections import defaultdict

ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/必修四从0重跑_ClaudeCode_2026-05-02")
ENTRIES = ROOT / "audit" / "entries"

def fixup_entries():
    """二合一：剥离细则前缀 + 回填同题设问。"""
    PATTERNS = [
        re.compile(r'^(细则[在要明给把列指][^。.！]*[。.！]\s*)+'),
        re.compile(r'^[^。.！]*?细则[在要明给把列指][^。.！]*[。.！]\s*'),
        re.compile(r'^(评[分标][细则要]?[在要明给把][^。.！]*[。.！]\s*)+'),
    ]
    strip_n = setw_n = 0
    for f in sorted(ENTRIES.glob('*.jsonl')):
        parsed = []
        for line in f.read_text(encoding='utf-8').splitlines():
            if not line.strip(): parsed.append(None); continue
            try: parsed.append(json.loads(line))
            except Exception: parsed.append(line)
        for e in parsed:
            if not isinstance(e, dict): continue
            why = e.get('为什么能想到', '')
            orig = why
            for pat in PATTERNS:
                m = pat.match(why)
                if m and len(m.group(0)) < len(why):
                    rem = why[m.end():].strip()
                    if len(rem) > 30:
                        why = rem; break
            if why != orig:
                bn = e.get('boundary_note', '')
                e['boundary_note'] = (bn + ' | ' if bn else '') + '原文细则口径已转入审计：' + orig[:120]
                e['为什么能想到'] = why; strip_n += 1
        by_q = defaultdict(list)
        for e in parsed:
            if isinstance(e, dict):
                by_q[(e.get('question_no',''), e.get('sub_part',''))].append(e)
        for key, group in by_q.items():
            non_empty = [g.get('设问','') for g in group if g.get('设问','') and len(g.get('设问',''))>20]
            if not non_empty: continue
            canonical = max(non_empty, key=len)
            for e in group:
                if not e.get('设问','') or len(e.get('设问',''))<20:
                    e['设问'] = canonical; setw_n += 1
        out = []
        for x in parsed:
            if x is None: out.append('')
            elif isinstance(x, dict): out.append(json.dumps(x, ensure_ascii=False))
            else: out.append(x)
        f.write_text('\n'.join(out)+'\n', encoding='utf-8')
    print(f'修剪前缀 {strip_n} 条；回填设问 {setw_n} 条')

def main():
    fixup_entries()
    print('--- quality_check ---')
    subprocess.run([sys.executable, str(ROOT / 'scripts/quality_check.py')], check=False)
    print('--- synthesize_student ---')
    subprocess.run([sys.executable, str(ROOT / 'scripts/synthesize_student.py')], check=False)
    print('--- synthesize_word ---')
    subprocess.run([sys.executable, str(ROOT / 'scripts/synthesize_word.py')], check=False)
    print('--- build_audit_files ---')
    subprocess.run([sys.executable, str(ROOT / 'scripts/build_audit_files.py')], check=False)
    # 统计
    n = sum(1 for f in ENTRIES.glob('*.jsonl') for line in f.read_text(encoding='utf-8').splitlines() if line.strip())
    files = sum(1 for _ in ENTRIES.glob('*.jsonl'))
    reports = sum(1 for _ in (ROOT / 'suite_reports').glob('*.md'))
    print(f'\n=== 当前 ===\nentries 条目：{n}\nentries 套卷：{files}\nsuite_reports：{reports}')

if __name__ == '__main__':
    main()
