import pdfplumber, re, json, sys

SRC='/sessions/great-nifty-darwin/mnt/uploads/选必三思维宝典-飞哥正志讲堂.pdf'

def lines_of(p):
    chs=[c for c in p.chars]
    if not chs: return []
    chs.sort(key=lambda c:(c['top'], c['x0']))
    lines=[]; cur=[]; curtop=None
    for c in chs:
        mid=(c['top']+c['bottom'])/2
        if curtop is None or abs(mid-curtop)<=5:
            cur.append(c); curtop=mid if curtop is None else (curtop*0.6+mid*0.4)
        else:
            lines.append(cur); cur=[c]; curtop=mid
    if cur: lines.append(cur)
    out=[]
    for ln in lines:
        ln.sort(key=lambda c:c['x0'])
        txt=''.join(c['text'] for c in ln)
        sizes={}
        for c in ln: sizes[round(c['size'],1)]=sizes.get(round(c['size'],1),0)+1
        size=max(sizes,key=sizes.get)
        col=ln[0].get('non_stroking_color')
        out.append({'size':size,'col':col,'text':txt})
    return out

def is_footer(t):
    return bool(re.match(r'^—\s*\d+\s*—$', t.strip())) or t.strip() in ('',)
def is_header(t):
    return '思维宝典' in t and '选必三' in t and len(t)<25

LABELS=['材料触发点','设问','为什么能想到','答案落点','同题说明','答题提醒','图示信息','术语提示','白话提示']

def join_para(lines):
    out=''
    for i,l in enumerate(lines):
        if i==0: out=l
        else:
            if out and l and out[-1].isascii() and out[-1].isalnum() and l[0].isascii() and l[0].isalnum():
                out+=' '+l
            else:
                out+=l
    return out

doc={'chapters':[]}
img_count=0
all_lines=[]
with pdfplumber.open(SRC) as pdf:
    for pi,p in enumerate(pdf.pages):
        if pi==0: continue  # cover
        img_count+=len(p.images)
        for L in lines_of(p):
            t=L['text']
            if is_footer(t) or is_header(t): continue
            if re.search(r'\.{6,}', t) or re.search(r'·{6,}', t):
                L['toc']=True
            all_lines.append(L)

# drop TOC lines (dot leaders) and any line that is a TOC-style entry ending in page number with leaders
body=[L for L in all_lines if not L.get('toc')]

# Further drop residual TOC: lines on TOC pages often are subtopic/chapter names without dots but appear before first real chapter.
# We detect start of body: first line with size>=16 (chapter) that is followed shortly by a 【 label.
# Simpler: find index of first occurrence where a size>=16 chapter is followed within 6 lines by a '【材料触发点】'
start=0
for i,L in enumerate(body):
    if L['size']>=16 and re.match(r'^[一二三四五六七八九十]+、', L['text'].strip()):
        # look ahead
        win=''.join(x['text'] for x in body[i:i+8])
        if '【材料触发点】' in win or '【' in win:
            start=i; break
body=body[start:]

cur_ch=None; cur_sub=None; cur_q=None; cur_block=None

def push_block():
    global cur_block
    if cur_block is not None and cur_q is not None:
        cur_block['text']=join_para(cur_block['_lines'])
        del cur_block['_lines']
        cur_q['blocks'].append(cur_block)
    cur_block=None

for L in body:
    t=L['text'].strip()
    if not t: continue
    size=L['size']
    # chapter
    if size>=16 and re.match(r'^[一二三四五六七八九十]+、', t):
        push_block(); cur_q=None
        cur_ch={'title':t,'subtopics':[]}; doc['chapters'].append(cur_ch); cur_sub=None
        continue
    # subtopic (size ~14, not a question, not a label)
    if 13.0<=size<15.5 and not t.startswith('【') and not re.match(r'^\d+\.', t):
        push_block(); cur_q=None
        cur_sub={'title':t,'questions':[]}
        if cur_ch is None:
            cur_ch={'title':'','subtopics':[]}; doc['chapters'].append(cur_ch)
        cur_ch['subtopics'].append(cur_sub)
        continue
    # question title (size ~11.5 starting with number.)
    if 11.0<=size<13.0 and re.match(r'^\d+\.\s', t):
        push_block()
        cur_q={'title':t,'blocks':[]}
        if cur_sub is None:
            cur_sub={'title':'','questions':[]}
            if cur_ch is None:
                cur_ch={'title':'','subtopics':[]}; doc['chapters'].append(cur_ch)
            cur_ch['subtopics'].append(cur_sub)
        cur_sub['questions'].append(cur_q)
        continue
    # label block start
    m=re.match(r'^【([^】]+)】\s*(.*)$', t)
    if m and m.group(1) in LABELS:
        push_block()
        rest=m.group(2)
        cur_block={'label':m.group(1),'_lines':[rest] if rest else []}
        continue
    # continuation
    if cur_block is not None:
        cur_block['_lines'].append(t)
    elif cur_q is not None:
        # stray line before any label -> attach as untitled block
        cur_block={'label':'','_lines':[t]}
push_block()

# stats
nch=len(doc['chapters'])
nsub=sum(len(c['subtopics']) for c in doc['chapters'])
nq=sum(len(s['questions']) for c in doc['chapters'] for s in c['subtopics'])
from collections import Counter
lab=Counter(b['label'] for c in doc['chapters'] for s in c['subtopics'] for q in s['questions'] for b in q['blocks'])
print('images in content pages:', img_count)
print('chapters:',nch,'subtopics:',nsub,'questions:',nq)
print('chapter titles:', [c['title'] for c in doc['chapters']])
print('subtopics per chapter:', [[s['title'] for s in c['subtopics']] for c in doc['chapters']])
print('label counts:', dict(lab))
json.dump(doc, open('/sessions/great-nifty-darwin/mnt/outputs/model.json','w'), ensure_ascii=False, indent=1)
print('saved model.json')
