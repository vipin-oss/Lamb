import sys; sys.path.insert(0,'/home/user/Lamb/internal/code')
from core import *
NE=dict(c11=mp.mpf('165e9'),c13=mp.mpf('66e9'),c33=mp.mpf('185e9'),c44=mp.mpf('47e9'),
  c12=mp.mpf('35e9'),R1=mp.mpf('1.5e9'),R2=mp.mpf('-1.0e9'),R3=mp.mpf('0.4e9'),
  K1=mp.mpf('0.9e9'),K2=mp.mpf('1.2e9'),e31=mp.mpf('-0.5'),e33=mp.mpf('1.3'),e15=mp.mpf('-0.4'),
  ep11=mp.mpf('9e-11'),ep33=mp.mpf('1.1e-10'),p3=mp.mpf('-1e-5'),b1=mp.mpf('3e5'),b3=mp.mpf('3e5'),
  bw=mp.mpf('5e5'),rho=mp.mpf('5600'),rhop=mp.mpf('1.2'),gam=mp.mpf('1e8'),lnl=mp.mpf('1e-8'),
  lg=mp.mpf('1e-8'),T0=mp.mpf('300'),rcp=mp.mpf('2.6e6'),kth=mp.mpf('50'),tauq=mp.mpf('1e-11'))
AN=dict(c11=mp.mpf('226e9'),c13=mp.mpf('112e9'),c33=mp.mpf('216e9'),c44=mp.mpf('44e9'),
  e31=mp.mpf('-2.2'),e33=mp.mpf('9.3'),e15=mp.mpf('5.8'),q31=mp.mpf('290'),q33=mp.mpf('350'),q15=mp.mpf('190'),
  ep11=mp.mpf('5.64e-9'),ep33=mp.mpf('6.35e-9'),mu11=mp.mpf('2.97e-4'),mu33=mp.mpf('1.57e-4'),
  a11=mp.mpf('1.6e-9'),a33=mp.mpf('2.7e-9'),b1=mp.mpf('3.1e5'),b3=mp.mpf('3.1e5'),
  p3=mp.mpf('-1e-5'),lam=mp.mpf('2e-3'),rho=mp.mpf('5730'),lnl=mp.mpf('1e-8'),lg=mp.mpf('1e-8'),
  T0=mp.mpf('300'),rcp=mp.mpf('2.5e6'),kth=mp.mpf('6'),tauq=mp.mpf('1e-11'))
eta=mp.mpc('1.3','0.4')
for name,Mfun,Pset in [("Neha",M_neha,NE),("Anu",M_anu,AN)]:
    print("=====",name)
    for fd in ['1e6','1e8','1e10']:
        w=2*mp.pi*mp.mpf(fd); k=mp.mpf('3e5')
        d,rel,R0=degree_scaled(k,w,Pset,Mfun=Mfun)
        print(f"  fd={fd}: degree {d}, coeff ratio to max at power {d}: {max(rel):.2e}, R0 {mp.nstr(R0,3)}")
    for lg in [mp.mpf(0),mp.mpf('1e-8')]:
        Q=dict(Pset); Q['lg']=lg
        et,b,R0=roots_eta(mp.mpf('3e5'),2*mp.pi*mp.mpf('1e8'),Q,Mfun=Mfun)
        print(f"  l_g={float(lg):g}: {len(et)} roots, degree {len(b)-1}; 'gradient' roots with l_g|eta|>0.5: "
              f"{sum(1 for z in et if lg!=0 and abs(z)*lg>0.5)}")
    print("  parity sign vectors, all couplings on:", parity_matrix(Mfun,mp.mpf('3e5'),2*mp.pi*mp.mpf('1e8'),Pset,eta))
    Q=dict(Pset)
    for kk in ['R1','R2','R3']:
        if kk in Q: Q[kk]=mp.mpf(0)
    Q['bw']=mp.mpf(0) if 'bw' in Q else mp.mpf(0)
    print("  parity with all couplings off:", parity_matrix(Mfun,mp.mpf('3e5'),2*mp.pi*mp.mpf('1e8'),Q,eta))
    et,b,R0=roots_eta(mp.mpf('3e5'),2*mp.pi*mp.mpf('1e8'),Pset,Mfun=Mfun)
    e0=min(et,key=abs); v=nullvec(Mfun(e0,mp.mpf('3e5'),2*mp.pi*mp.mpf('1e8'),Pset))
    M=Mfun(e0,mp.mpf('3e5'),2*mp.pi*mp.mpf('1e8'),Pset)
    nrm=max(abs(M[i,j]) for i in range(5) for j in range(5))
    print("  null-vector residual ||M v||/max|M| =", float(max(abs(mp.fsum([M[i,j]*v[j] for j in range(5)])) for i in range(5))/nrm))
