import os,json,urllib.request as u
def P(p,d):return json.load(u.urlopen(os.getenv("MAKEFUN_ENV_URL")+p,json.dumps(d).encode()))
V=(100,320,330,500,900,0)
C=[0]
T=("KKKKKKKKUUUUUUUUMMOQQOMMLLMPPMLLKKKOOKKKLJIKKIJLLMMGGMMLKKKKKKKK","ACEEEECACGKKKKGCEKMNNMKEELNOONLEEKNOONKEELMNNMLECGKLLKGCACEEEECA","GIIIIIIGIKKKKKKIIKLMMLKIILLMMLLIIKMMMMKIIMMMMMMIILKKKKLIGIIIIIIG","KKKKKKKKLMMMMMML"+"JKKKKKKJ"*5+"KKKLLKKK","K"*64)
N=(-33,-31,-18,-14,14,18,31,33);J=(-17,-16,-15,-1,1,15,16,17);D=(-17,-15,15,17);R=(-16,-1,1,16);G=D+R;X=N+J
Y={};LIM=80000
def n(s):return chr(97+(s&7))+str(8-s//16)
def F(g):
 b=[0]*128;p=g.split()
 for i,r in enumerate(p[0].split("/")):
  c=0
  for h in r:
   if h<"9":c+=int(h)
   else:b[i*16+c]=("pnbrqk".index(h.lower())+1)*(2*(h<"a")-1);c+=1
 s=1-2*(p[1]<"w");c=sum(("KQkq"[j] in p[2])<<j for j in range(4));e=-1
 if p[3]!="-":e=(8-int(p[3][1]))*16+ord(p[3][0])-97
 return b,s,c,e
def H(b,s,c):
 for t in(s+17*c,s+15*c):
  if t&0x88==0 and b[t]==c:return 1
 for o in X:
  t=s+o
  if t&0x88==0 and b[t]==(6,2)[o in N]*c:return 1
 for o in G:
  t=s+o
  while t&0x88==0:
   q=b[t]
   if q:
    if q==5*c or q==(3+(o in R))*c:return 1
    break
   t+=o
 return 0
def M(b,s,c,e,q=0):
 m=[]
 for f,p in enumerate(b):
  if p*s<=0:continue
  k=abs(p)
  if k==1:
   d=-16*s;y=(7+5*s)//2;z=(7-7*s)//2;t=f+d
   if t&0x88==0 and b[t]==0:
    u=(t>>4)==z
    if not q or u:m.append((f,t,5*u))
    if not q and (f>>4)==y and b[f+2*d]==0:m.append((f,f+2*d,0))
   for o in(d-1,d+1):
    t=f+o
    if t&0x88==0 and (b[t]*s<0 or t==e):m.append((f,t,5*((t>>4)==z)))
  elif k in(2,6):
   for o in(J,N)[k==2]:
    t=f+o
    if t&0x88==0 and (b[t]*s<0 or (not q and b[t]==0)):m.append((f,t,0))
   if k==6 and not q:
    for K,C,Y,T,Z in ((116,1,(117,118),118,1),(116,2,(115,114,113),114,1),(4,4,(5,6),6,-1),(4,8,(3,2,1),2,-1)):
     if f==K and s==Z and c&C and not any(b[x] for x in Y) and not any(H(b,x,-s) for x in (K,)+Y[:2]):m.append((K,T,0))
  else:
   for o in(D,R,G)[k-3]:
    t=f+o
    while t&0x88==0 and not b[t]:
     if not q:m.append((f,t,0))
     t+=o
    if t&0x88==0 and b[t]*s<0:m.append((f,t,0))
 return m
def A(b,c,e,m):
 b=b[:];f,t,r=m;p=b[f];b[f]=0
 if abs(p)==1 and t==e and b[t]==0:b[t+16*p]=0
 if abs(p)==6 and abs(t-f)==2:
  x=f+7*(t>f)-4;y=f+2*(t>f)-1;b[y]=b[x];b[x]=0
 b[t]=r*p if r else p
 if abs(p)==6:c&=~(3+9*(p<0))
 for x,z in((112,2),(119,1),(0,8),(7,4)):
  if f==x or t==x:c&=~z
 return b,c,(f+t)//2 if abs(p)==1 and abs(t-f)==32 else -1
def L(b,s,c,e,q=0):
 k=b.index(6*s)
 return [(m,)+d for m in M(b,s,c,e,q) if not H((d:=A(b,c,e,m))[0],m[1] if b[m[0]]==6*s else k,-s)]
def E(b,s):
 t=0
 for i,p in enumerate(b):
  if p:
   q=abs(p);j=i-(i>>4)*8;v=V[q-1]+(ord(T[q-1 if q<5 else q-2][j^((p<0)*56)])-75)*5
   t+=(v,-v)[p<0]
 return t*s
def S(b,s,c,e,d,a,z):
 C[0]+=1
 if C[0]>LIM:return 100000
 k=b.index(6*s);mv=0
 if d>0:
  q=(str(b),s,c,e);h=Y.get(q)
  if h and h[0]>=d:
   if h[1]==0 or h[1]==1 and h[2]>=z or h[1]==2 and h[2]<=a:return h[2]
  if h:mv=h[3]
  if d>2 and not H(b,k,-s) and any(1<abs(p)<6 for p in b):
   if -S(b,-s,c,-1,d-3,-z,-z+1)>=z:return z
  w=L(b,s,c,e)
  if not w:return -99990-d if H(b,k,-s) else 0
 else:
  if H(b,k,-s):
   w=L(b,s,c,e)
   if not w:return -99990-d
  else:
   t=E(b,s)
   if t>=z:return z
   if t>a:a=t
   w=L(b,s,c,e,1)
  if d==-8:return E(b,s)
 f=2;r=a;bm=0
 w.sort(key=lambda x:(-(x[0]==mv),-abs(b[x[0][1]])))
 for m,n,y,v in w:
  t=-S(n,-s,y,v,d-1,-z,-r)
  if t>r:
   r=t;bm=m;f=0
   if r>=z:
    f=1
    break
 if d>0 and C[0]<=LIM:Y[q]=(d,f,r,bm)
 return z if f==1 else r
def B(b,s,c,e):
 w=L(b,s,c,e)
 if len(w)<2:return w[0][0]
 j=w[0][0];C[0]=0
 if len(Y)>1e5:Y.clear()
 w.sort(key=lambda x:-abs(b[x[0][1]]))
 for d in range(1,7):
  r=-1e9;k=j
  for m,n,y,v in w:
   t=-S(n,-s,y,v,d,-1e9,-r)
   if t>r:r=t;k=m
  if C[0]<=LIM:j=k
  else:break
 return j
while 1:
 g=P("/game",{})
 if g["status"]=="done":break
 k=g["game"]
 while g["status"]=="your_move":
  l=g["legal_moves"]
  b,s,c,e=F(g["fen"]);m=B(b,s,c,e);o=n(m[0])+n(m[1])+"q"[:m[2]]
  if o not in l:o=l[0]
  g=P("/move",{"game":k,"move":o})
