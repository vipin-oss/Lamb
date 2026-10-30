import sys; sys.path.insert(0,'/home/user/Lamb'); sys.path.insert(0,'/home/user/Lamb/internal/code')
import numpy as np
from common.rayleigh_lamb import F_sym, F_anti, roots_at, speeds
from core import *

# ---------- 1. Rayleigh-Lamb cross-check of the 4x4 matrix route ----------
E,nu,rho=70e9,0.33,2700.
cL,cT=speeds(E,nu,rho)
pL,pM=mp.mpf(cL),mp.mpf(cT)
mu=E/(2*(1+nu)); lam=E*nu/((1+nu)*(1-2*nu))
LA,MU=mp.mpf(lam),mp.mpf(mu)
def B_mech(k,w,h=mp.mpf(1)):
    p=mp.sqrt(w**2/pL**2-k**2); q=mp.sqrt(w**2/pM**2-k**2)
    cols=[]
    for eta,A,B in [(I*p,1,0),(-I*p,1,0),(I*q,0,1),(-I*q,0,1)]:
        ux=I*k*A-eta*B; uz=eta*A+I*k*B
        szz=LA*I*k*ux+(LA+2*MU)*eta*uz
        sxz=MU*(eta*ux+I*k*uz)
        sc=mp.e**(-abs(mp.re(eta))*h)
        cols.append([szz*mp.e**(eta*h)*sc,sxz*mp.e**(eta*h)*sc,szz*mp.e**(-eta*h)*sc,sxz*mp.e**(-eta*h)*sc])
    M=mp.matrix(4,4)
    for j,c in enumerate(cols):
        for i in range(4): M[i,j]=c[i]
    return M

def detnorm(M):
    n=max(abs(M[i,j]) for i in range(M.rows) for j in range(M.cols))
    return abs(mp.det(M))/n**M.rows

print("TEST 1  Rayleigh-Lamb cross-check (4x4 matrix route vs classical equations)")
print(f"  cL {cL:.4f}  cT {cT:.4f}")
rows=[]
for fd in [10.,100.,1000.]:
    w=2*np.pi*fd/2; W=mp.mpf(w)
    for name,F,sel in (('S0',F_sym,'max'),('A0',F_anti,'min')):
        cs=np.linspace(20.0, 40*cT, 400000)
        vals=F(cs,fd,cL,cT)
        idx=np.where(np.sign(vals[:-1])*np.sign(vals[1:])<0)[0]
        rr=[]
        for i in idx:
            a,b=cs[i],cs[i+1]; fa=vals[i]
            for _ in range(60):
                m=0.5*(a+b); fm=F(np.array(m),fd,cL,cT)
                if np.sign(fm)==np.sign(fa): a,fa=m,fm
                else: b=m
            rr.append(0.5*(a+b))
        rr=np.array(rr)
        if rr.size==0: print(f"  fd={fd:6.0f} {name}: no reference root"); continue
        c0=float(rr.max() if sel=='max' else rr.min())
        k0=W/mp.mpf(c0)
        d=detnorm(B_mech(k0,W))
        d2=detnorm(B_mech(k0*mp.mpf('1.001'),W))
        rows.append((fd,name,c0,float(d)))
        print(f"  fd={fd:6.0f} {name}: c_ref={c0:.6f}  |det B|/||B||^4 at c_ref = {float(d):.2e}"
              f"  (0.1% away: {float(d2):.2e})  {'PASS' if d<1e-10 else 'FAIL'}")

# ---------- 2. degree counts (placeholder ZnO constants, internal only) ----------
Z=dict(c11=mp.mpf('209.7e9'),c13=mp.mpf('105.4e9'),c33=mp.mpf('211.2e9'),c44=mp.mpf('42.4e9'),
   e31=mp.mpf('-0.57'),e33=mp.mpf('1.32'),e15=mp.mpf('-0.48'),ep11=mp.mpf('8.54')*mp.mpf('8.854e-12'),
   ep33=mp.mpf('10.2')*mp.mpf('8.854e-12'),b1=mp.mpf('4e5'),b3=mp.mpf('4e5'),p3=mp.mpf('-1e-5'),
   rho=mp.mpf('5680'),lnl=mp.mpf(0),lg=mp.mpf(0),q=mp.mpf('1.602176634e-19'),Dn=mp.mpf('1e-3'),
   bn=mp.mpf('0.01'),n0=mp.mpf('1e20'),vd=mp.mpf(0),bth=mp.mpf('1e18'),tauR=mp.mpf('1e30'),
   T0=mp.mpf('300'),rcp=mp.mpf('2.8e6'),kth=mp.mpf('60'),tauq=mp.mpf('1e-11'),Pi=mp.mpf('-1e-3'),Eg=mp.mpf(0))
k=mp.mpf('3e5'); w=2*mp.pi*mp.mpf('1e8')
print("TEST 2  degree of det M in eta (expected 10 without l_g, 14 with l_g)")
for lg,lnl,exp in [(0,0,10),(mp.mpf('1e-8'),0,14),(0,mp.mpf('1e-8'),10),(mp.mpf('1e-8'),mp.mpf('1e-8'),14)]:
    Q=dict(Z); Q['lg']=mp.mpf(lg); Q['lnl']=mp.mpf(lnl)
    d,rel,R0=degree_scaled(k,w,Q)
    print(f"  l_g={float(lg):g} l_nl={float(lnl):g}: degree={d} expected={exp} {'PASS' if d==exp else 'FAIL'}")

# ---------- 3. parity ----------
print("TEST 3  parity of det M in eta  (det(-eta)/det(eta); even => +1)")
for lbl,bth,Pi in [("thermo-piezo coupling off",0,0),("beta_th only",mp.mpf('1e18'),0),("both on",mp.mpf('1e18'),mp.mpf('-1e-3'))]:
    Q=dict(Z); Q['bth']=mp.mpf(bth); Q['Pi']=mp.mpf(Pi)
    vals=[]
    for et in ['0.7','1.3+0.4j','2.2-0.6j']:
        eta=mp.mpc(et) if 'j' in et else mp.mpf(et)
        vals.append(mp.det(M_sumit(-eta,k,w,Q))/mp.det(M_sumit(eta,k,w,Q)))
    ev = all(abs(v-1)<1e-25 for v in vals)
    print(f"  {lbl:28s} det(-eta)/det(eta) = ", ", ".join(f"{complex(v):.9f}" for v in vals),
          "  => EVEN" if ev else "  => not even")

# ---------- 4. root count equals degree, and l -> 0 continuity ----------
print("TEST 4  number of roots and l_g,l_nl -> 0 continuity")
ref=None
for lg,lnl in [(0,0),(mp.mpf('1e-11'),mp.mpf('1e-11')),(mp.mpf('1e-9'),mp.mpf('1e-9')),(mp.mpf('1e-8'),mp.mpf('1e-8'))]:
    Q=dict(Z); Q['lg']=mp.mpf(lg); Q['lnl']=mp.mpf(lnl)
    etas,b,R0=roots_eta(k,w,Q)
    n=len(etas)
    if ref is None:
        ref=sorted(etas,key=lambda z:(mp.re(z),mp.im(z)))
        print(f"  l_g=l_nl={float(lg):g}: {n} roots (degree {len(b)-1})")
    else:
        cur=sorted(etas,key=lambda z:(mp.re(z),mp.im(z)))
        if len(cur)==len(ref) and len(ref)==10:
            d=max(abs(a-b)/max(abs(b),mp.mpf(1)) for a,b in zip(cur,ref))
            print(f"  l_g=l_nl={float(lg):g}: {n} roots (degree {len(b)-1}), max rel shift {float(d):.2e}")
        else:
            print(f"  l_g=l_nl={float(lg):g}: {n} roots (degree {len(b)-1})  [count changes: expected]")
