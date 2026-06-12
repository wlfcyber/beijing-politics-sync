# -*- coding: utf-8 -*-
import pikepdf, re, sys
SRC='/sessions/great-nifty-darwin/mnt/uploads/选必三思维宝典-飞哥正志讲堂.pdf'
OUT='/sessions/great-nifty-darwin/mnt/outputs/选必三思维宝典-飞哥正志讲堂(水印修复版).pdf'

pat=re.compile(rb'/Figure<</MCID \d+>>BDC\s*[0-9.]+ [0-9.]+ [0-9.]+ rg\s*q /EGS\d+ gs /Tr\d+ Do Q\s*EMC')

pdf=pikepdf.open(SRC)
moved=0; skipped=[]
for i,p in enumerate(pdf.pages):
    # only touch content pages 6..end (index>=5); leave cover(1)+TOC(2-5) untouched
    if i < 5:
        continue
    data=p.Contents.read_bytes()
    m=pat.search(data)
    if not m:
        skipped.append(i+1); continue
    block=m.group()
    # remove from original position
    rest=data[:m.start()]+data[m.end():]
    # insert just before the final Q (page-level restore) so watermark paints last = topmost
    s=rest.rstrip()
    assert s.endswith(b'Q'), 'page %d not ending with Q'%(i+1)
    cut=len(s)-1
    newdata=rest[:cut]+b'\n'+block+b'\nQ\n'
    # we re-added a Q above; ensure we removed the old final Q (it was at position cut in `rest` rstripped)
    # rest[:cut] excludes the final Q; we append block then Q.
    p.Contents.write(newdata)
    moved+=1

print('pages with watermark moved to top:', moved)
print('content pages skipped (no match):', skipped)
pdf.save(OUT, compress_streams=True)
print('saved ->', OUT)
