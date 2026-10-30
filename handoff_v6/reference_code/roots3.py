import numpy as np, mpmath as mp
from sm import Mmat
mp.mp.dps=80
def Mmp(eta,k,w,P):
    # build with mp by reusing Mmat structure through numpy object arrays
    import sm
    return None
def detpoly(k,w,P,deg):
    # evaluate det with mp using python-number formula: replicate Mmat with mp
    I=mp.mpc(0,1)
    def M(eta):
        g=lambda n: mp.mpf(P[n]) if not isinstance(P[n],complex) else mp.mpc(P[n])
        L=eta**2-k**2; G=1-g('lg')**2*L; N=1-g('lnl')**2*L
        c11,c13,c33,c44=g('c11'),g('c13'),g('c33'),g('c44'); e31,e33,e15=g('e31'),g('e33'),g('e15')
        ep11,ep33,b1,b3,p3,rho=g('ep11'),g('ep33'),g('b1'),g('b3'),g('p3'),g('rho')
        z=mp.mpf(0)
        sxx=[G*c11*I*k,G*c13*eta,e31*eta,z,-b1]
        szz=[G*c13*I*k,G*c33*eta,e33*eta,z,-b3]
        sxz=[G*c44*eta,G*c44*I*k,e15*I*k,z,z]
        Dx=[e15*eta,e15*I*k,-ep11*I*k,z,z]
        Dz=[e31*I*k,e33*eta,-ep33*eta,z,p3]
        Mx=mp.matrix(5,5)
        for j in range(5):
            Mx[0,j]=-(I*k*sxx[j]+eta*sxz[j]); Mx[1,j]=-(I*k*sxz[j]+eta*szz[j])
            Mx[2,j]=I*k*Dx[j]+eta*Dz[j]
        Mx[0,0]+=-N*rho*w**2; Mx[1,1]+=-N*rho*w**2; Mx[2,3]+=g('q')
        Mx[3,3]=-I*w-(g('Dn')*L+g('vd')*I*k-1/g('tauR')); Mx[3,2]=-g('bn')*g('n0')*(k**2-eta**2); Mx[3,4]=-g('bth')*L
        f=1-I*w*g('tauq'); sp_=-I*w
        Mx[4,4]=f*g('rcp')*sp_-g('kth')*L
        Mx[4,0]=f*g('T0')*sp_*b1*I*k; Mx[4,1]=f*g('T0')*sp_*b3*eta
        Mx[4,2]=-f*g('T0')*p3*sp_*eta
        Mx[4,3]=f*(g('q')*g('Pi')*sp_+g('Eg')/g('tauR'))
        return Mx
    return M
def roots_mp(k,w,P):
    deg=14 if P['lg']!=0 else 10
    k=mp.mpf(k);w=mp.mpf(w)
    M=detpoly(k,w,P,deg)
    R=mp.mpf(3e5)
    pts=[R*mp.e**(2j*mp.pi*j/(deg+1)) for j in range(deg+1)]
    vals=[mp.det(M(p)) for p in pts]
    n=deg+1
    coef=[]
    for m in range(n):
        s=sum(vals[j]*mp.e**(-2j*mp.pi*j*m/n) for j in range(n))/n
        coef.append(s/R**m)
    rts=mp.polyroots(coef[::-1],maxsteps=500,extraprec=400)
    return rts

def _det(A,n):
    if n==1: return A[0][0]
    t=0
    for j in range(n):
        if A[0][j]==0: continue
        sub=[[A[i][c] for c in range(n) if c!=j] for i in range(1,n)]
        t+=(-1)**j*A[0][j]*_det(sub,n-1)
    return t
def nullvec_mp(eta,k,w,P):
    M=detpoly(mp.mpf(k),mp.mpf(w),P,0)
    Mx=M(mp.mpc(eta))
    best=None
    for a in range(5):
        v=[]
        for b in range(5):
            ri=[i for i in range(5) if i!=a]; ci=[j for j in range(5) if j!=b]
            sub=[[Mx[rr,cc] for cc in ci] for rr in ri]
            v.append((-1)**(a+b)*_det(sub,4))
        nrm=max(abs(x) for x in v)
        if best is None or nrm>best[0]: best=(nrm,v)
    v=best[1]; m=max(v,key=lambda x:abs(x))
    return np.array([complex(x/m) for x in v])
