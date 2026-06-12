# -*- coding: utf-8 -*-
import json, re, html
from weasyprint import HTML

M = json.load(open('/sessions/great-nifty-darwin/mnt/outputs/model.json'))

CN = {1:'一',2:'二',3:'三',4:'四',5:'五',6:'六',7:'七',8:'八',9:'九',10:'十'}

CORE = {
 '材料触发点':'material',
 '设问':'question',
 '为什么能想到':'reason',
 '答案落点':'answer',
}
NOTE = {
 '同题说明':'tongti',
 '答题提醒':'tixing',
 '图示信息':'tushi',
 '术语提示':'shuyu',
 '白话提示':'baihua',
}
NOTE_LABEL = dict(NOTE)  # keep label text

def esc(s): return html.escape(s, quote=False)

def split_qtitle(t):
    m = re.match(r'^(\d+)\.\s*(.*)$', t.strip())
    if m: return m.group(1), m.group(2)
    return '', t.strip()

def strip_chapter(t):
    # '一、科学思维' -> ('一','科学思维')
    m = re.match(r'^([一二三四五六七八九十]+)、\s*(.*)$', t.strip())
    if m: return m.group(1), m.group(2)
    return '', t.strip()

# ---------- build body ----------
parts = []

# COVER
parts.append('''
<section class="cover">
  <div class="cv-frame">
    <div class="cv-kicker">2026 · 北京高考政治 · 选择性必修三</div>
    <div class="cv-rule"></div>
    <div class="cv-main">
      <div class="cv-book">《逻辑与思维》</div>
      <div class="cv-title">思维宝典</div>
      <div class="cv-sub">真题思维拆解 · 材料触发 · 答案落点</div>
    </div>
    <div class="cv-rule cv-rule-b"></div>
    <div class="cv-brand">飞哥正志讲堂</div>
    <div class="cv-meta">逻辑与思维 · 北京一模二模真题精编</div>
  </div>
</section>
''')

# TOC
toc = ['<section class="toc"><div class="toc-head">目　录</div><div class="toc-cap">《逻辑与思维》思维宝典</div>']
for ci, ch in enumerate(M['chapters'], 1):
    cnum, cname = strip_chapter(ch['title'])
    toc.append(f'<a class="t-ch" href="#ch{ci}"><span class="t-ch-t">{esc(ch["title"])}</span></a>')
    for si, sub in enumerate(ch['subtopics'], 1):
        if sub['title']:
            toc.append(f'<a class="t-sub" href="#sub{ci}_{si}"><span class="t-tx">{esc(sub["title"])}</span></a>')
        for qi, q in enumerate(sub['questions'], 1):
            num, ttl = split_qtitle(q['title'])
            toc.append(f'<a class="t-q" href="#q{ci}_{si}_{qi}"><span class="t-tx">{esc(num+". "+ttl)}</span></a>')
toc.append('</section>')
parts.append('\n'.join(toc))

# CHAPTERS
for ci, ch in enumerate(M['chapters'], 1):
    cnum, cname = strip_chapter(ch['title'])
    subs_list = ''.join(
        f'<li>{esc(s["title"])}</li>' for s in ch['subtopics'] if s['title'])
    # divider page
    parts.append(f'''
<section class="divider" id="ch{ci}">
  <div class="dv-part">{ci:02d}</div>
  <div class="dv-kicker">第&#8201;{cnum}&#8201;章</div>
  <div class="dv-name">{esc(cname)}</div>
  <div class="dv-line"></div>
  <ul class="dv-subs">{subs_list}</ul>
</section>''')
    body = [f'<section class="chapter-body"><h1 class="chapter" id="chh{ci}">{esc(ch["title"])}</h1>']
    for si, sub in enumerate(ch['subtopics'], 1):
        if sub['title']:
            body.append(f'<h2 class="sub" id="sub{ci}_{si}"><span class="sub-mark"></span>{esc(sub["title"])}</h2>')
        for qi, q in enumerate(sub['questions'], 1):
            num, ttl = split_qtitle(q['title'])
            body.append(f'<div class="question" id="q{ci}_{si}_{qi}">')
            body.append(f'<div class="q-title"><span class="q-badge">{esc(num)}</span><span class="q-tx">{esc(ttl)}</span></div>')
            for b in q['blocks']:
                lab = b['label']; txt = esc(b['text'])
                if lab in CORE:
                    cls = CORE[lab]
                    body.append(f'<div class="blk blk-{cls}"><span class="lab lab-{cls}">{esc(lab)}</span><span class="bt">{txt}</span></div>')
                elif lab in NOTE:
                    cls = NOTE[lab]
                    body.append(f'<div class="note note-{cls}"><span class="nlab">{esc(lab)}</span><span class="nt">{txt}</span></div>')
                else:
                    body.append(f'<div class="blk blk-plain"><span class="bt">{txt}</span></div>')
            body.append('</div>')
    body.append('</section>')
    parts.append('\n'.join(body))

BODY = '\n'.join(parts)

CSS = r'''
:root{
  --ink:#14304c; --ink2:#274a6e; --muted:#5b6573; --rule:#dde2e8; --rule2:#c8d0d9;
  --material:#9a6a22; --question:#2f5ca0; --reason:#6a4d9c; --answer:#2e7d54;
  --tint-material:#f7f1e6; --tint-question:#eef2f9; --tint-reason:#f1edf7; --tint-answer:#eaf4ee;
  --note-bg:#f4f6f8; --note-bar:#9aa6b2;
}
@page{
  size:A4; margin:20mm 18mm 17mm 18mm;
  @top-left{ content:"《逻辑与思维》· 思维宝典"; font-family:'Carlito','Droid Sans Fallback'; font-size:7.6pt; color:#9aa6b2; letter-spacing:.02em;}
  @top-right{ content:string(chap); font-family:'Carlito','Droid Sans Fallback'; font-size:7.6pt; color:#9aa6b2; letter-spacing:.02em;}
  @bottom-center{ content:counter(page); font-family:'Carlito'; font-size:8.5pt; color:#7c8794;}
  @bottom-right{ content:"飞哥正志讲堂"; font-family:'Droid Sans Fallback'; font-size:7.4pt; color:#b7bfc8;}
}
@page:first{ @top-left{content:none} @top-right{content:none} @bottom-center{content:none} @bottom-right{content:none} }
@page cover{ margin:0; @top-left{content:none} @top-right{content:none} @bottom-center{content:none} @bottom-right{content:none} }
@page divider{ @top-left{content:none} @top-right{content:none} }

html{ font-family:'Carlito','Droid Sans Fallback',sans-serif; color:#1c2733; font-size:10.4pt; line-height:1.72; }
body{ margin:0; }
section{ }

/* watermark on every page */
.wm{ position:fixed; top:42%; left:8%; width:84%; text-align:center;
     font-family:'Droid Sans Fallback'; font-size:60pt; color:#16314c;
     opacity:.035; transform:rotate(-26deg); z-index:-1; letter-spacing:.35em; }

/* ---------------- COVER ---------------- */
.cover{ page:cover; height:297mm; box-sizing:border-box; padding:0; position:relative; }
.cv-frame{ position:absolute; top:26mm; bottom:26mm; left:24mm; right:24mm;
  border:1px solid var(--rule2); padding:18mm 16mm; display:flex; flex-direction:column; }
.cv-kicker{ font-family:'Carlito','Droid Sans Fallback'; font-size:11pt; letter-spacing:.18em;
  color:var(--ink2); text-align:center; }
.cv-rule{ height:2px; background:var(--ink); margin:7mm auto 0; width:54mm; }
.cv-rule-b{ width:34mm; height:1px; background:var(--rule2); margin-top:0; }
.cv-main{ flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; }
.cv-book{ font-size:30pt; color:var(--ink); letter-spacing:.06em; font-weight:700; }
.cv-title{ font-size:46pt; color:var(--ink); letter-spacing:.42em; font-weight:700; margin:8mm 0 0 4mm; }
.cv-sub{ margin-top:9mm; font-size:11.5pt; color:var(--muted); letter-spacing:.16em; }
.cv-brand{ text-align:center; font-size:16pt; color:var(--ink); letter-spacing:.22em; margin-top:7mm; font-weight:700; }
.cv-meta{ text-align:center; font-size:9pt; color:#9aa4b0; letter-spacing:.1em; margin-top:3mm; }

/* ---------------- TOC ---------------- */
.toc{ break-before:page; }
.toc-head{ text-align:center; font-size:21pt; color:var(--ink); letter-spacing:.5em; font-weight:700; margin:2mm 0 1mm; }
.toc-cap{ text-align:center; font-size:9.5pt; color:var(--muted); letter-spacing:.12em; margin-bottom:7mm; }
a{ color:inherit; text-decoration:none; }
.t-ch{ display:block; margin:5.5mm 0 2mm; font-size:12pt; font-weight:700; color:var(--ink);
  border-bottom:1.4px solid var(--ink); padding-bottom:1.5mm; letter-spacing:.05em; }
.t-ch::after{ content: leader(' ') target-counter(attr(href), page); font-family:'Carlito'; font-weight:700; }
.t-sub{ display:block; margin:2.9mm 0 .9mm; font-size:10.4pt; font-weight:700; color:var(--ink2); letter-spacing:.02em; }
.t-sub::after{ content: leader('·') ' ' target-counter(attr(href), page); color:var(--muted); font-family:'Carlito'; font-weight:400; }
.t-q{ display:block; margin:1mm 0; padding-left:6mm; font-size:9.3pt; color:#48555f; }
.t-q::after{ content: leader('.') ' ' target-counter(attr(href), page); color:#9aa6b1; font-family:'Carlito'; }

/* ---------------- DIVIDER ---------------- */
.divider{ page:divider; break-before:page; height:257mm; box-sizing:border-box;
  display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; position:relative; }
.dv-part{ font-family:'Carlito'; font-size:96pt; line-height:1; color:var(--ink); opacity:.08; font-weight:700; letter-spacing:.04em; }
.dv-kicker{ font-size:12pt; letter-spacing:.55em; color:var(--ink2); margin-top:5mm; padding-left:.5em;}
.dv-name{ font-size:32pt; color:var(--ink); letter-spacing:.3em; font-weight:700; margin-top:5mm; padding-left:.3em; }
.dv-line{ width:22mm; height:2px; background:var(--ink); margin:9mm 0 8mm; opacity:.5;}
.dv-subs{ list-style:none; padding:0; margin:0; }
.dv-subs li{ font-size:11pt; color:var(--ink2); letter-spacing:.18em; margin:2.6mm 0; padding-left:.36em; }

/* ---------------- CHAPTER BODY ---------------- */
.chapter-body{ break-before:page; }
h1.chapter{ string-set: chap content(text); margin:0 0 4mm; font-size:0; height:0; }  /* hidden anchor carrying running string */
h2.sub{ font-size:13.5pt; color:var(--ink); font-weight:700; letter-spacing:.05em;
  margin:7mm 0 3mm; padding-bottom:1.6mm; border-bottom:1px solid var(--rule);
  break-after:avoid; display:flex; align-items:center; }
h2.sub .sub-mark{ display:inline-block; width:4px; height:15px; background:var(--ink); margin-right:3mm; }

.question{ margin:0 0 4.2mm; padding-bottom:3mm; border-bottom:1px solid var(--rule); break-inside:auto; }
.q-title{ display:flex; align-items:baseline; margin-bottom:2mm; break-after:avoid; }
.q-badge{ flex:none; min-width:5.4mm; height:5.4mm; padding:0 1.4mm; box-sizing:border-box;
  background:var(--ink); color:#fff; font-family:'Carlito'; font-size:9.5pt; font-weight:700;
  border-radius:2px; text-align:center; line-height:5.4mm; margin-right:2.6mm; transform:translateY(1px); }
.q-tx{ font-size:11.4pt; font-weight:700; color:var(--ink); letter-spacing:.02em; }

.blk{ margin:1.6mm 0; padding-left:3mm; border-left:2px solid var(--rule2); break-inside:auto; }
.blk .bt{ }
.lab{ display:inline-block; color:#fff; font-size:8.2pt; font-weight:700; letter-spacing:.04em;
  padding:.3mm 2mm; border-radius:2.5px; margin-right:2mm; transform:translateY(-.6px); white-space:nowrap; }
.blk-material{ border-left-color:var(--material);} .lab-material{ background:var(--material);}
.blk-question{ border-left-color:var(--question);} .lab-question{ background:var(--question);}
.blk-reason{ border-left-color:var(--reason);} .lab-reason{ background:var(--reason);}
.blk-answer{ border-left-color:var(--answer);} .lab-answer{ background:var(--answer);}
.blk-answer .bt{ }
.blk-plain{ border-left-color:var(--rule2); }

.note{ margin:1.6mm 0 1.6mm 3mm; padding:2mm 3mm; background:var(--note-bg);
  border-left:2px solid var(--note-bar); border-radius:0 3px 3px 0; font-size:9pt; color:var(--muted); line-height:1.6; }
.note .nlab{ font-weight:700; color:#48525e; margin-right:1.6mm; }
.note-tixing{ border-left-color:#b08948; background:#faf6ee; }
.note-tixing .nlab{ color:#8a6a2e; }
'''

DOC = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<title>选必三《逻辑与思维》· 思维宝典</title>
<meta name="author" content="飞哥正志讲堂">
<meta name="description" content="2026 北京高考政治 选择性必修三《逻辑与思维》思维宝典 · 真题思维拆解（精排美化版）">
<meta name="keywords" content="逻辑与思维,思维宝典,北京高考政治,选必三,飞哥正志讲堂">
<style>{CSS}</style></head>
<body>
<div class="wm">飞哥正志讲堂</div>
{BODY}
</body></html>'''

open('/sessions/great-nifty-darwin/mnt/outputs/book.html','w').write(DOC)
OUT='/sessions/great-nifty-darwin/mnt/outputs/《逻辑与思维》思维宝典·精排美化版.pdf'
HTML(string=DOC).write_pdf(OUT)
print('PDF written ->', OUT)
