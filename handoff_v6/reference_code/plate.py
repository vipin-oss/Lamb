import numpy as np
from numpy import pi
from sm import Mmat,P0
I=1j
def find_roots_old(k,w,P,R=None):
    deg=14 if (P['lg']!=0 or P['lnl']!=0) else 10
    n=128
    R=R or 3e6
    th=np.exp(2j*pi*np.arange(n)/n)
    vals=np.array([np.linalg.det(Mmat(R*t,k,w,P)) for t in th])
    c=np.fft.fft(vals)/n
    a=np.array([c[j]/R**j for j in range(deg+1)])
    r=np.roots(a[::-1])
    out=[]
    for z in r:
        for _ in range(30):
            f=np.linalg.det(Mmat(z,k,w,P)); h=1e-6*max(abs(z),1.0)
            d=(np.linalg.det(Mmat(z+h,k,w,P))-np.linalg.det(Mmat(z-h,k,w,P)))/(2*h)
            if d==0: break
            dz=f/d; z=z-dz
            if abs(dz)<1e-12*max(abs(z),1): break
        out.append(z)
    return np.array(out)
def nullvec(eta,k,w,P):
    u,s,vh=np.linalg.svd(Mmat(eta,k,w,P))
    v=vh[-1].conj()
    return v/ (v[np.argmax(abs(v))])
def bc_rows(eta,v,k,P,thermal='adiabatic'):
    X,Z,Ph,nn,Th=v
    L=eta**2-k**2; G=1-P['lg']**2*L; N=1-P['lnl']**2*L
    c11,c13,c33,c44=P['c11'],P['c13'],P['c33'],P['c44']
    e31,e33,e15=P['e31'],P['e33'],P['e15']
    Sxx=I*k*X; Szz=eta*Z; Sxz=(eta*X+I*k*Z)/2; Ex=-I*k*Ph; Ez=-eta*Ph
    szz=G*(c13*Sxx+c33*Szz)-e33*Ez-P['b3']*Th
    sxz=G*2*c44*Sxz-e15*Ex
    lg2=P['lg']**2
    Px=(sxz-lg2*I*k*eta*(c11*Sxx+c13*Szz))/N
    Pz=(szz-lg2*I*k*eta*(2*c44*Sxz))/N
    Rx=lg2*eta*2*c44*Sxz/N
    Rz=lg2*eta*(c13*Sxx+c33*Szz)/N
    Dz=e31*Sxx+e33*Szz+P['ep33']*Ez+P['p3']*Th
    Gam=-P['Dn']*eta*nn+P['bn']*P['n0']*eta*Ph-P['bth']*eta*Th
    th=eta*Th if thermal=='adiabatic' else Th
    rows=[Pz,Px]
    if P['lg']!=0: rows+=[Rx,Rz]
    rows+=[Dz,Gam,th]
    return np.array(rows)
def Bmat(k,w,P,h,thermal='adiabatic'):
    r=find_roots(k,w,P)
    cols_p=[];cols_m=[]
    for em in r:
        v=nullvec_mp(em,k,w,P); e=complex(em)
        rows=bc_rows(e,v,k,P,thermal)
        a=abs(e.real)*h; cols_p.append(rows*np.exp(e*h-a)); cols_m.append(rows*np.exp(-e*h-a))
    B=np.vstack([np.array(cols_p).T,np.array(cols_m).T])
    return B,np.array([complex(x) for x in r])
from roots3 import roots_mp,nullvec_mp
def find_roots(k,w,P,R=None):
    r=roots_mp(k,w,P)
    return r
