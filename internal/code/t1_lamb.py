import sys; sys.path.insert(0,'/home/user/Lamb'); sys.path.insert(0,'/home/user/Lamb/internal/code')
import numpy as np
from common.rayleigh_lamb import F_sym, F_anti, roots_at, speeds
from core import *
E,nu,rho=70e9,0.33,2700.
cL,cT=speeds(E,nu,rho)
mu=E/(2*(1+nu)); lam=E*nu/((1+nu)*(1-2*nu))
P=dict(lam=mp.mpf(lam),mu=mp.mpf(mu),rho=mp.mpf(rho)); h=mp.mpf(1)
print("cL %.6f cT %.6f cR %.6f"%(cL,cT,float(mp.re(rayleigh_speed(cL,cT)))))

def B_mech(k,w,h=mp.mpf(1)):
    p=mp.sqrt(w**2/cL**2-k**2); q=mp.sqrt(w**2/cT**2-k**2)
    waves=[(I*p,1,0),(-I*p,1,0),(I*q,0,1),(-I*q,0,1)]
    cols=[]
    for eta,A,B in waves:
        ux=I*k*A+eta*B; uz=eta*A-I*k*B
        szz=P['lam']*I*k*ux+(P['lam']+2*P['mu'])*eta*uz
        sxz=P['mu']*(eta*ux+I*k*uz)
        sc=mp.e**(-abs(mp.re(eta))*h)
        cols.append([szz*mp.e**(eta*h)*sc,sxz*mp.e**(eta*h)*sc,szz*mp.e**(-eta*h)*sc,sxz*mp.e**(-eta*h)*sc])
    M=mp.matrix(4,4)
    for j,c in enumerate(cols):
        for i in range(4): M[i,j]=c[i]
    return M

print(f"{'fd':>7} {'branch':>6} {'c_ref':>12} {'c_matrix':>12} {'rel':>10}")
for fd in [10.,100.,1000.]:
    w=2*np.pi*fd/2
    cs=roots_at(fd,F_sym,cL,cT)
    ca=roots_at(fd,F_anti,cL,cT)
    for name,cl in (('S',cs),('A',ca)):
        if not cl: continue
        c0=cl[0]  # fundamental branch (slowest for A, fastest for S)
        c0=cs[-1] if name=='S' else ca[0]
        k0=w/c0
        W=mp.mpf(w); K=mp.mpf(k0)
        f=lambda k: mp.re(mp.det(B_mech(k,W)))
        kn=mp.findroot(f,(K*mp.mpf('0.995'),K*mp.mpf('1.005')))
        cn=W/kn
        print(f"{fd:7.0f} {name:>6} {c0:12.6f} {float(cn):12.6f} {abs(float(cn)-c0)/c0:10.2e}")
