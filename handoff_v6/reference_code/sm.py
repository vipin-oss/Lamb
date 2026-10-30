import numpy as np
from numpy import pi
I=1j
P0=dict(c11=209.7e9,c13=105.4e9,c33=211.2e9,c44=42.4e9,e31=-0.57,e33=1.32,e15=-0.48,ep11=8.54*8.854e-12,ep33=10.2*8.854e-12,
 b1=4e5,b3=4e5,p3=-1e-5,rho=5680.,lnl=0.,lg=0.,q=1.602e-19,Dn=1e-3,bn=0.01,n0=1e20,vd=0.,bth=1e18,tauR=1e30,T0=300.,rcp=2.8e6,kth=60.,tauq=1e-11,Pi=-1e-3,Eg=0.)
def Mmat(eta,k,w,P):
    g=lambda n:P[n]
    L=eta**2-k**2; G=1-P['lg']**2*L; N=1-P['lnl']**2*L
    c11,c13,c33,c44=P['c11'],P['c13'],P['c33'],P['c44']; e31,e33,e15=P['e31'],P['e33'],P['e15']
    ep11,ep33,b1,b3,p3,rho=P['ep11'],P['ep33'],P['b1'],P['b3'],P['p3'],P['rho']
    # columns ux,uz,phi,n,theta
    # strains per unit amplitude
    M=np.zeros((5,5),complex)
    # stress coefficient rows: sxx,szz,sxz as 5-vectors; Dx,Dz
    sxx=np.array([G*c11*I*k, G*c13*eta, e31*eta, 0, -b1],complex)
    szz=np.array([G*c13*I*k, G*c33*eta, e33*eta, 0, -b3],complex)
    sxz=np.array([G*c44*eta, G*c44*I*k, e15*I*k, 0, 0],complex)
    Dx=np.array([e15*eta, e15*I*k, -ep11*I*k, 0,0],complex)
    Dz=np.array([e31*I*k, e33*eta, -ep33*eta, 0, p3],complex)
    M[0]=-N*rho*w**2*np.array([1,0,0,0,0])-(I*k*sxx+eta*sxz)
    M[1]=-N*rho*w**2*np.array([0,1,0,0,0])-(I*k*sxz+eta*szz)
    M[2]=I*k*Dx+eta*Dz+P['q']*np.array([0,0,0,1,0])
    M[3]=np.array([0,0,0,-I*w,0])-np.array([0,0,P['bn']*P['n0']*(k**2-eta**2),P['Dn']*L+P['vd']*I*k-1/P['tauR'],P['bth']*L])
    f=1-I*w*P['tauq']
    sp_=-I*w
    M[4]=f*(np.array([0,0,0,0,P['rcp']*sp_])+P['T0']*sp_*(b1*np.array([I*k,0,0,0,0])+b3*np.array([0,eta,0,0,0]))
           +P['T0']*p3*sp_*np.array([0,0,-eta,0,0])+P['q']*P['Pi']*sp_*np.array([0,0,0,1,0])+P['Eg']*np.array([0,0,0,1,0])/P['tauR'])-P['kth']*L*np.array([0,0,0,0,1])
    return M
def detpoly(k,w,P,deg=8):
    # det as polynomial in s=eta^2? check parity by sampling
    pts=np.exp(2j*pi*np.arange(32)/32)*1e6*0+0
    return None
def roots(k,w,P):
    # fit det(M(eta)) as polynomial in eta of degree <=16 using sampling on circle radius R
    R=max(abs(k),1e6)
    n=64
    th=np.exp(2j*pi*np.arange(n)/n)
    vals=np.array([np.linalg.det(Mmat(R*t,k,w,P)) for t in th])
    c=np.fft.fft(vals)/n   # coefficient of (R t)^j * R^j ... c_j = a_j R^j
    a=np.array([c[j]/R**j for j in range(n//2)])
    return a
if __name__=="__main__":
    a=roots(3e5,2*pi*1e8,P0)
    nz=[j for j in range(len(a)) if abs(a[j])>1e-9*abs(a).max()]
    print("nonzero powers of eta:",nz)
