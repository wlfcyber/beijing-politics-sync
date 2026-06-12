# -*- coding: utf-8 -*-
# Make the watermark lighter by lowering the alpha (CA/ca) of the ExtGStates it uses.
# These gstates are used ONLY by the watermark Do (1 gs per page).
import pikepdf, sys

NEW_ALPHA = float(sys.argv[1]) if len(sys.argv)>1 else 0.23
IN ='/sessions/great-nifty-darwin/mnt/outputs/选必三思维宝典-飞哥正志讲堂(排版优化版).pdf'

pdf=pikepdf.open(IN, allow_overwriting_input=True)
seen=set(); changed=0
for p in pdf.pages:
    res=p.get('/Resources',{})
    eg=res.get('/ExtGState')
    if eg is None: continue
    for name,gs in eg.items():
        key=gs.objgen if hasattr(gs,'objgen') else id(gs)
        if key in seen: continue
        seen.add(key)
        ca=gs.get('/ca'); CA=gs.get('/CA')
        try: caf=float(ca) if ca is not None else None
        except: caf=None
        if caf is not None and abs(caf-0.42)<0.02:
            gs.ca=NEW_ALPHA; gs.CA=NEW_ALPHA
            changed+=1
print('ExtGState objects lightened:',changed,'-> alpha',NEW_ALPHA)
try:
    pdf.save(IN)   # overwrite same deliverable
    print('saved in place ->',IN)
except Exception as e:
    alt=IN.replace('.pdf','_light.pdf')
    pdf.save(alt); print('in-place failed (%s); saved ->'%e, alt)
