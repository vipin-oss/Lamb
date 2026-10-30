import sys; sys.path.insert(0,'/home/user/Lamb/internal/code')
from core import *
E,nu,rho=mp.mpf('70e9'),mp.mpf('0.33'),mp.mpf('2700')
mu=E/(2*(1+nu)); lam=E*nu/((1+nu)*(1-2*nu))
P=dict(lam=lam,mu=mu,rho=rho); cL,cT=iso_speed(P); cR=rayleigh_speed(cL,cT)
print("cL",mp.nstr(cL,9),"cT",mp.nstr(cT,9),"cR",mp.nstr(cR,9))
h=mp.mpf('1e-3')

def pq(k,w):
    return mp.sqrt(w**2/cL**2-k**2), mp.sqrt(w**2/cT**2-k**2)

def FS(k,w):
    p,q=pq(k,w); D=(k**2-q**2)**2
    return D*mp.sin(q*h)*mp.cos(p*h)+4*k**2*p*q*mp.cos(q*h)*mp.sin(p*h)
def FA(k,w):
    p,q=pq(k,w); D=(k**2-q**2)**2
    return 4*k**2*p*q*mp.sin(q*h)*mp.cos(p*h)+D*mp.cos(q*h)*mp.sin(p*h)

def B_mech(k,w):
    p,q=pq(k,w)
    waves=[(I*p,1,0),(-I*p,1,0),(I*q,0,1),(-I*q,0,1)]
    cols=[]
    for eta,A,B in waves:
        ux=I*k*A+eta*B; uz=eta*A-I*k*B
        szz=lam*I*k*ux+(lam+2*mu)*eta*uz
        sxz=mu*(eta*ux+I*k*uz)
        sc=mp.e**(-abs(mp.re(eta))*h)
        cols.append([szz*mp.e**(eta*h)*sc,sxz*mp.e**(eta*h)*sc,szz*mp.e**(-eta*h)*sc,sxz*mp.e**(-eta*h)*sc])
    M=mp.matrix(4,4)
    for j,c in enumerate(cols):
        for i in range(4): M[i,j]=c[i]
    return M

# --- validate the classical equations themselves against two known limits ---
w_lo=2*mp.pi*mp.mpf('1e4')/(2*h)
k_lo=mp.findroot(lambda k: mp.re(FS(k,w_lo)), w_lo/mp.mpf('5400'))
print("thin plate S0 (classical):", mp.nstr(w_lo/k_lo,8), " expected ~ sqrt(E/(rho(1-nu^2)))",
      mp.nstr(mp.sqrt(E/(rho*(1-nu**2))),8))
w_hi=2*mp.pi*mp.mpf('4e6')/(2*h)
k_r=mp.findroot(lambda k: mp.re(FS(k,w_hi)), w_hi/mp.mpf('2950'))
k_a=mp.findroot(lambda k: mp.re(FA(k,w_hi)), w_hi/mp.mpf('2950'))
print("large fd  S:", mp.nstr(w_hi/k_r,8), " A:", mp.nstr(w_hi/k_a,8), " cR:", mp.nstr(cR,8))

def dense(f,w,lo,hi,n=6000):
    out=[];x0=lo;f0=mp.re(f(lo,w))
    for i in range(1,n+1):
        x=lo+(hi-lo)*mp.mpf(i)/n; f1=mp.re(f(x,w))
        if f0*f1<0:
            try: out.append(mp.findroot(lambda z: mp.re(f(z,w)),(x0,x)))
            except Exception: pass
        x0,f0=x,f1
    return out

for fd in [mp.mpf('5e5'),mp.mpf('1e6'),mp.mpf('2e6')]:
    w=2*mp.pi*fd/(2*h)
    lo=w/cL*mp.mpf('0.99'); hi=w/cT*mp.mpf('1.6')
    roots=sorted(dense(FS,w,lo,hi)+dense(FA,w,lo,hi))
    print(f"\nfd={float(fd):.0f}: {len(roots)} classical roots, speeds",
          [f"{float(w/x):.1f}" for x in roots])
    worst=0
    for kk in roots:
        M=B_mech(kk,w); d=abs(mp.det(M)); nrm=max(abs(M[i,j]) for i in range(4) for j in range(4))
        worst=max(worst,float(d/nrm**4))
    print("  max |det B|/||B||^4 at classical roots:", f"{worst:.3e}")
