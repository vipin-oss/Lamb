import sys; sys.path.insert(0,'/home/user/Lamb/internal/code')
from core import *

# ---------------- isotropic set for test 1 ----------------
E, nu, rho = mp.mpf('70e9'), mp.mpf('0.33'), mp.mpf('2700')
mu = E/(2*(1+nu)); lam = E*nu/((1+nu)*(1-2*nu))
cL = mp.sqrt((lam+2*mu)/rho); cT = mp.sqrt(mu/rho)
PISO = dict(lam=lam, mu=mu, rho=rho)
print("cL", mp.nstr(cL,8), "cT", mp.nstr(cT,8))

def B_mech(k, w, h, P):
    """4x4 boundary matrix for the isotropic elastic plate; rows sigma_zz, sigma_xz at +-h."""
    P2 = dict(P); m = M_mech_iso(0, k, w, P)
    etas, b, R0 = roots_eta(k, w, P, Mfun=M_mech_iso, R0=max(abs(k),mp.mpf(1))*4)
    cols = []
    for eta in etas:
        v = nullvec(M_mech_iso(eta, k, w, P))
        sxx = (P['lam']+2*P['mu'])*I*k*v[0] + P['lam']*eta*v[1]
        szz = P['lam']*I*k*v[0] + (P['lam']+2*P['mu'])*eta*v[1]
        sxz = P['mu']*(eta*v[0] + I*k*v[1])
        cols.append([szz*mp.e**(eta*h), sxz*mp.e**(eta*h), szz*mp.e**(-eta*h), sxz*mp.e**(-eta*h)])
    B = mp.matrix(4,4)
    for j,c in enumerate(cols):
        for i in range(4): B[i,j] = c[i]
    return B

def closed_form(k, w, h, cL, cT):
    p2 = w**2/cL**2 - k**2; q2 = w**2/cT**2 - k**2
    p, q = mp.sqrt(p2), mp.sqrt(q2)
    S = mp.tan(q*h)/mp.tan(p*h) + 4*k**2*p*q/(k**2-q2)**2
    A = mp.tan(q*h)/mp.tan(p*h) + (k**2-q2)**2/(4*k**2*p*q)
    return S, A

def root_k(fun, k0, w, h, P, cL, cT, which):
    def f(k):
        S, A = closed_form(k, w, h, cL, cT)
        return S if which=='S' else A
    k = mp.findroot(f, k0)
    return k

h = mp.mpf(1e-3)
rows = []
for fd in [mp.mpf('0.5e6'), mp.mpf('1e6'), mp.mpf('2e6')]:
    w = 2*mp.pi*fd/(2*h)
    k0 = w/cT*mp.mpf('0.55')
    for which in ['S','A']:
        kc = mp.findroot(lambda k: closed_form(k,w,h,cL,cT)[0 if which=='S' else 1], k0)
        B = B_mech(kc, w, h, PISO)
        detB = mp.det(B)
        # refine numeric zero of det B with k starting from the closed-form root (no info leak in direction)
        kn = mp.findroot(lambda k: mp.det(B_mech(k, w, h, PISO)), kc)
        rel = abs(kn-kc)/abs(kc)
        rows.append((float(fd), which, complex(kc), complex(kn), float(rel)))
        print(f"fd={float(fd):9.0f} {which}  k_closed={complex(kc)}  k_num={complex(kn)}  rel={float(rel):.2e}")
mp.nstr(0,1)
