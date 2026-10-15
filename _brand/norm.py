import re,sys,json
src=open(sys.argv[1]).read()
d=' '.join(re.findall(r'<path d="([^"]+)"',src,re.S))
toks=re.findall(r'[MmLlCcZz]|-?\d+\.?\d*',d)
S=4*10  # potrace units per ref px (scale .1, 4x upscale)
H=5016*10
segs=[];i=0;cmd=None;cur=(0,0);start=None;sub=[]
def pt(x,y): return (x/S, (H-y)/S)
subs=[]
while i<len(toks):
    t=toks[i]
    if re.match(r'[A-Za-z]',t): cmd=t;i+=1
    if cmd in 'Zz':
        subs.append(sub);sub=[];cur=start;continue
    if cmd in 'Mm':
        x,y=float(toks[i]),float(toks[i+1]);i+=2
        cur=(cur[0]+x,cur[1]+y) if cmd=='m' else (x,y);start=cur
        sub=[('M',[cur])];cmd='l' if cmd=='m' else 'L'
    elif cmd in 'Ll':
        x,y=float(toks[i]),float(toks[i+1]);i+=2
        cur=(cur[0]+x,cur[1]+y) if cmd=='l' else (x,y);sub.append(('L',[cur]))
    elif cmd in 'Cc':
        v=[float(t) for t in toks[i:i+6]];i+=6
        if cmd=='c': ps=[(cur[0]+v[0],cur[1]+v[1]),(cur[0]+v[2],cur[1]+v[3]),(cur[0]+v[4],cur[1]+v[5])]
        else: ps=[(v[0],v[1]),(v[2],v[3]),(v[4],v[5])]
        cur=ps[2];sub.append(('C',ps))
if sub: subs.append(sub)
allp=[pt(*p) for s in subs for _,ps in s for p in ps]
x0=min(p[0] for p in allp);y0=min(p[1] for p in allp)
x1=max(p[0] for p in allp);y1=max(p[1] for p in allp)
# note: bbox from control points (close enough; on-curve extrema for this mark)
ox,oy=float(sys.argv[2]),float(sys.argv[3])
def f(v): s=f"{v:.1f}"; return s[:-2] if s.endswith('.0') else s
out=[]
for s in subs:
    for c,ps in s:
        out.append(c+' '.join(f"{f(pt(*p)[0]-ox)} {f(pt(*p)[1]-oy)}" for p in ps))
    out.append('Z')
print(json.dumps({'bbox':[x0,y0,x1,y1],'d':''.join(out)}))
