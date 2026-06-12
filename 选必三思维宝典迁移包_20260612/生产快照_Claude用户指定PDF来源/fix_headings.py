# -*- coding: utf-8 -*-
# Add a section-header band (soft blue + navy left tab) BEHIND each knowledge-point
# heading, drawn first in the page stream so it sits under the text. No reflow.
import pdfplumber, pikepdf

IN ='/sessions/great-nifty-darwin/mnt/outputs/选必三思维宝典-飞哥正志讲堂(水印修复版).pdf'
OUT='/sessions/great-nifty-darwin/mnt/outputs/选必三思维宝典-飞哥正志讲堂(排版优化版).pdf'

BAND=(0.910,0.945,0.984)   # soft blue
NAVY=(0.122,0.306,0.475)   # left tab / accent
RULE=(0.122,0.306,0.475)

def lines(p):
    chs=sorted(p.chars,key=lambda c:(c['top'],c['x0']))
    out=[];cur=[];ct=None
    for c in chs:
        mid=(c['top']+c['bottom'])/2
        if ct is None or abs(mid-ct)<=5: cur.append(c); ct=mid if ct is None else ct*0.6+mid*0.4
        else: out.append(cur);cur=[c];ct=mid
    if cur:out.append(cur)
    res=[]
    for ln in out:
        x0=min(c['x0'] for c in ln); x1=max(c['x1'] for c in ln)
        top=min(c['top'] for c in ln); bot=max(c['bottom'] for c in ln)
        sizes={}
        for c in ln: sizes[round(c['size'],1)]=sizes.get(round(c['size'],1),0)+1
        size=max(sizes,key=sizes.get)
        txt=''.join(c['text'] for c in sorted(ln,key=lambda c:c['x0']))
        res.append(dict(x0=x0,x1=x1,top=top,bot=bot,size=size,txt=txt))
    return res

# collect heading bboxes + page height
headings={}; PHs={}
with pdfplumber.open(IN) as pdf:
    for pi,p in enumerate(pdf.pages):
        PHs[pi]=p.height
        for L in lines(p):
            t=L['txt'].strip()
            if 13.0<=L['size']<15.5 and t and not t.startswith('【') and not t[:1].isdigit():
                headings.setdefault(pi,[]).append((L['top'],L['bot']))

pdf=pikepdf.open(IN)
added=0
for pi,hs in headings.items():
    PH=PHs[pi]
    page=pdf.pages[pi]
    data=page.Contents.read_bytes()
    ops=["/Artifact BMC"]
    x=66.0; w=458.0; pad=3.6; tab=3.5
    for (T,B) in hs:
        y=PH-B-pad; h=(B-T)+2*pad
        # band
        ops.append("q %.4f %.4f %.4f rg %.2f %.2f %.2f %.2f re f Q"%(BAND[0],BAND[1],BAND[2],x,y,w,h))
        # navy left tab
        ops.append("q %.4f %.4f %.4f rg %.2f %.2f %.2f %.2f re f Q"%(NAVY[0],NAVY[1],NAVY[2],x,y,tab,h))
        # thin baseline rule under band (full width)
        ops.append("q %.4f %.4f %.4f RG 0.6 w %.2f %.2f m %.2f %.2f l S Q"%(RULE[0],RULE[1],RULE[2],x,y-0.3,x+w,y-0.3))
        added+=1
    ops.append("EMC")
    prefix=("\n".join(ops)+"\n").encode("latin1")
    page.Contents.write(prefix+data)

pdf.save(OUT, compress_streams=True)
print("heading bands added:",added,"on",len(headings),"pages")
print("saved ->",OUT)
