import sys; sys.path.insert(0,'/home/user/Lamb/internal/code')
from core import *
Z=dict(c11=mp.mpf('209.7e9'),c13=mp.mpf('105.4e9'),c33=mp.mpf('211.2e9'),c44=mp.mpf('42.4e9'),
   e31=mp.mpf('-0.57'),e33=mp.mpf('1.32'),e15=mp.mpf('-0.48'),ep11=mp.mpf('8.54')*mp.mpf('8.854e-12'),
   ep33=mp.mpf('10.2')*mp.mpf('8.854e-12'),b1=mp.mpf('4e5'),b3=mp.mpf('4e5'),p3=mp.mpf('-1e-5'),
   rho=mp.mpf('5680'),lnl=mp.mpf(0),lg=mp.mpf(0),q=mp.mpf('1.602176634e-19'),Dn=mp.mpf('1e-3'),
   bn=mp.mpf('0.01'),n0=mp.mpf('1e20'),vd=mp.mpf(0),bth=mp.mpf('1e18'),tauR=mp.mpf('1e30'),
   T0=mp.mpf('300'),rcp=mp.mpf('2.8e6'),kth=mp.mpf('60'),tauq=mp.mpf('1e-11'),Pi=mp.mpf('-1e-3'),Eg=mp.mpf(0))
k=mp.mpf('3e5'); w=2*mp.pi*mp.mpf('1e8')
Q0=dict(Z); e0,_ ,_= roots_eta(k,w,Q0)
e0=sorted(e0,key=lambda z:(mp.re(z),mp.im(z)))
print("l_g=0 roots:"); 
for z in e0: print("   ", mp.nstr(z,10))
for lg in ['1e-11','1e-9','1e-8']:
    Q=dict(Z); Q['lg']=mp.mpf(lg); Q['lnl']=mp.mpf(lg)
    es,b,R0=roots_eta(k,w,Q)
    es=sorted(es,key=lambda z:(mp.re(z),mp.im(z)))
    big=[z for z in es if abs(z)*mp.mpf(lg)>1e-3]
    small=[z for z in es if abs(z)*mp.mpf(lg)<=1e-3]
    print(f"\nl_g={lg}: {len(es)} roots; {len(small)} physical, {len(big)} gradient-root")
    if len(small)==10:
        small=sorted(small,key=lambda z:(mp.re(z),mp.im(z)))
        d=max(abs(a-b)/max(abs(b),mp.mpf(1)) for a,b in zip(small,e0))
        print("   max rel shift of the 10 physical roots vs l_g=0:", float(d))
    print("   |eta|*l_g for the extra roots:", [f"{float(abs(z)*mp.mpf(lg)):.3f}" for z in big])
# singular value vs determinant at a root
Q=dict(Z); Q['lg']=mp.mpf('1e-8'); Q['lnl']=mp.mpf('1e-8')
es,_,_=roots_eta(k,w,Q); eta=max(es,key=lambda z: mp.re(z))
for fac in ['1','1+1e-6','1.001']:
    e=eta*(1+mp.mpf(fac)-1 if fac!='1' else 1)
    M=M_sumit(e,k,w,Q)
    n=max(abs(M[i,j]) for i in range(5) for j in range(5))
    Ms=mp.matrix([[M[i,j]/n for j in range(5)] for i in range(5)])
    sv=mp.svd_r(Ms)[1]
    print(f"eta*(x{fac}): |det|/n^5={float(abs(mp.det(M))/n**5):.3e}  smallest singular value={float(min(sv)):.3e}")
