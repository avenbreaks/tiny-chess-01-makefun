import os,json,urllib.request as u
def P(p,d):return json.load(u.urlopen(os.getenv("MAKEFUN_ENV_URL")+p,json.dumps(d).encode()))
V=(100,320,330,500,900,0)
C=[0]
T=("KKKKKKKKUUUUUUUUMMOQQOMMLLMPPMLLKKKOOKKKLJIKKIJLLMMGGMMLKKKKKKKK","ACEEEECACGKKKKGCEKMNNMKEELNOONLEEKNOONKEELMNNMLECGKLLKGCACEEEECA","GIIIIIIGIKKKKKKIIKLMMLKIILLMMLLIIKMMMMKIIMMMMMMIILKKKKLIGIIIIIIG","KKKKKKKKLMMMMMML"+"JKKKKKKJ"*5+"KKKLLKKK","GIIJJIIGIKKKKKKIIKLLLLKIJKLLLLKJKKLLLLKJILLLLLKIIKLKKKKIGIIJJIIG","ECCAACCE"*4+"GEECCEEGIGGGGGGIOOKKKKOOOQMKKMQO")
N=(-33,-31,-18,-14,14,18,31,33);J=(-17,-16,-15,-1,1,15,16,17);D=(-17,-15,15,17);R=(-16,-1,1,16);G=D+R;X=N+J;K=[0]*9
def n(s):return "abcdefgh"[s&7]+str(8-(s>>4))
def F(g):
 b=[0]*128;p=g.split()
 for i,r in enumerate(p[0].split("/")):
  c=0
  for h in r:
   if h<"9":c+=int(h)
   else:b[i*16+c]=("pnbrqk".index(h.lower())+1)*(1 if h<"a" else -1);c+=1
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
    while t&0x88==0:
     x=b[t]
     if x:
      if x*s<0:m.append((f,t,0))
      break
     if not q:m.append((f,t,0))
     t+=o
 return m
def A(b,c,e,m):
 b=b[:];f,t,r=m;p=b[f];b[f]=0
 if abs(p)==1 and t==e and b[t]==0:b[t+16*p//abs(p)]=0
 if abs(p)==6 and abs(t-f)==2:
  x=f+7*(t>f)-4;y=f+2*(t>f)-1;b[y]=b[x];b[x]=0
 b[t]=r*p//abs(p) if r else p
 if abs(p)==6:c&=~(3+9*(p<0))
 for x,z in((112,2),(119,1),(0,8),(7,4)):
  if f==x or t==x:c&=~z
 return b,c,(f+t)//2 if abs(p)==1 and abs(t-f)==32 else -1
def L(b,s,c,e,q=0):
 k=b.index(6*s)
 return [(m,)+d for m in M(b,s,c,e,q) if not H((d:=A(b,c,e,m))[0],m[1] if b[m[0]]==6*s else k,-s)]
def E(b,s,k):
 t=0
 for i,p in enumerate(b):
  if p:
   q=abs(p);j=(i>>4)*8+(i&7);v=V[q-1]+(ord(T[q-1][j if p>0 else j^56])-75)*5
   t+=v if p>0 else -v
 z=b.index(-6*s)
 t+=s*(abs(2*(z&7)-7)*abs(2*(z>>4)-7)+5*(14-abs((k&7)-(z&7))-abs((k>>4)-(z>>4))))
 return t*s
def W(b,y):
 v=b[y[0][1]];return V[abs(v)-1]if v else 100
def S(b,s,c,e,d,a,z):
 C[0]+=1
 if C[0]>6e4:return 1e5
 k=b.index(6*s)
 if d<=0:
  if H(b,k,-s):
   w=L(b,s,c,e)
   if not w:return -99990-d
  else:
   t=E(b,s,k)
   if t>=z:return z
   if t>a:a=t
   w=L(b,s,c,e,1)
  if d==-8:return E(b,s,k)
 else:
  w=L(b,s,c,e)
  if not w:return -99990-d if H(b,k,-s) else 0
 w.sort(key=lambda x:(x[0]==K[d],W(b,x)),reverse=1)
 for m,n,y,v in w:
  r=-S(n,-s,y,v,d-1,-z,-a)
  if r>=z:
   if d>0 and b[m[1]]==0:K[d]=m
   return z
  if r>a:a=r
 return a
def B(b,s,c,e):
 w=L(b,s,c,e)
 if len(w)<2:return w[0][0]
 j=w[0][0];C[0]=0
 w.sort(key=lambda x:W(b,x),reverse=1)
 for d in range(4):
  r=-1e9;k=j
  for m,n,y,v in w:
   t=-S(n,-s,y,v,d,-1e9,-r)
   if t>r:r=t;k=m
  if C[0]<=6e4:j=k
 return j
while 1:
 g=P("/game",{})
 if g["status"]=="done":break
 k=g["game"]
 while g["status"]=="your_move":
  l=g["legal_moves"]
  if not l:P("/resign",{"game":k});break
  b,s,c,e=F(g["fen"]);m=B(b,s,c,e);o=n(m[0])+n(m[1])+"q"[:m[2]]
  if o not in l:o=l[0]
  g=P("/move",{"game":k,"move":o})
