import sys; sys.path.insert(0,'/home/user/Lamb'); sys.path.insert(0,'/home/user/Lamb/internal/code')
import numpy as np
from common.rayleigh_lamb import F_sym, roots_at, speeds
from core import *
E,nu,rho=70e9,0.33,2700.
cL,cT=speeds(E,nu,rho)
mu=E/(2*(1+nu)); lam=E*nu/((1+nu)*(1-2*nu))
La,Mu=mp.mpf(lam),mp.mpf(mu)
def B_mech(k,w,h=mp.mpf(1)):
    p=mp.sqrt(w**2/mp.mpf(cL)**2-k**2); q=mp.sqrt(w**2/mp.mpf(cT)**2-k**2)
    waves=[(I*p,1,0),(-I*p,1,0),(I*q,0,1),(-I*q,0,1)]
    cols=[]
    for eta,A,B in waves:
        ux=I*k*A-eta*B; uz=eta*A+I*k*B
        szz=La*I*k*ux+(La+2*Mu)*eta*uz
        sxz=Mu*(eta*ux+I*k*uz)
        sc=mp.e**(-abs(mp.re(eta))*h)
        cols.append([szz*mp.e**(eta*h)*sc,sxz*mp.e**(eta*h)*sc,szz*mp.e**(-eta*h)*sc,sxz*mp.e**(-eta*h)*sc])
    M=mp.matrix(4,4)
    for j,c in enumerate(cols):
        for i in range(4): M[i,j]=c[i]
    return M
fd=10.; w=2*np.pi*fd/2; W=mp.mpf(w)
for c in [5300,5350,5390,5393.905,5395,5397.795,5400,5420,5450,5500]:
    k=W/mp.mpf(c); M=B_mech(k,W)
    nrm=max(abs(M[i,j]) for i in range(4) for j in range(4))
    print(f"c={c:10.3f} det/nrm^4={float(abs(mp.det(M))/nrm**4):.3e}")
print("ref roots S:",roots_at(fd,F_sym,cL,cT)[:5])
