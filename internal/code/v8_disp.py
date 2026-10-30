"""Task 2a: the elastic isotropic limit.  Couplings off, l_g = l_nl = 0, two tractions
free on both faces.  The zeros of det B are checked against the classical Rayleigh-Lamb
secular equations, both families, at three fd values.
"""
import sys
sys.path.insert(0, '.')
import mpmath as mp
mp.mp.dps = 40
import core as CORE

I = mp.mpc(0, 1)


def P_iso(E=mp.mpf(70e9), nu=mp.mpf('0.33'), rho=mp.mpf(2700)):
    lam = E*nu/((1+nu)*(1-2*nu))
    mu = E/(2*(1+nu))
    return dict(lam=lam, mu=mu, rho=rho, lg=mp.mpf(0), lnl=mp.mpf(0))


def B_iso(k, w, P, h):
    """4 x 4: rows sigma_zz, sigma_xz at z=+h and at z=-h; columns = the four roots."""
    roots, b, R0 = CORE.roots_eta(k, w, P, Mfun=CORE.M_mech_iso)
    roots = sorted(roots, key=lambda z: (mp.re(z), mp.im(z)))
    lam, mu = P['lam'], P['mu']
    c13, c33, c44 = lam, lam+2*mu, mu
    B = mp.matrix(4, 4)
    if len(roots) != 4:
        return None, roots
    for m, eta in enumerate(roots):
        v = CORE.nullvec(CORE.M_mech_iso(eta, k, w, P))
        r1 = c13*I*k*v[0] + c33*eta*v[1]
        r2 = c44*eta*v[0] + c44*I*k*v[1]
        sc = mp.e**(-abs(mp.re(eta))*h)
        B[0, m] = r1*mp.e**(eta*h)*sc
        B[1, m] = r2*mp.e**(eta*h)*sc
        B[2, m] = r1*mp.e**(-eta*h)*sc
        B[3, m] = r2*mp.e**(-eta*h)*sc
    return B, roots


def det_residual(c, fd, h, P):
    """|det B| / ||B||^4 at the speed c, fd = f*2h."""
    w = 2*mp.pi*mp.mpf(fd)/(2*h)
    k = w/mp.mpf(c)
    B, roots = B_iso(k, w, P, h)
    if B is None:
        return None, len(roots)
    nrm = max(abs(B[i, j]) for i in range(4) for j in range(4))
    return abs(mp.det(B))/nrm**4, 4


def rl(c, fd, h, P, family):
    """classical Rayleigh-Lamb secular function, zero at the mode speed."""
    w = 2*mp.pi*mp.mpf(fd)/(2*h)
    k = w/mp.mpf(c)
    cL = mp.sqrt((P['lam']+2*P['mu'])/P['rho'])
    cT = mp.sqrt(P['mu']/P['rho'])
    p = mp.sqrt(w**2/cL**2 - k**2)
    q = mp.sqrt(w**2/cT**2 - k**2)
    if family == 'S':
        return mp.tan(q*h) + 4*k**2*p*q/(q**2-k**2)**2*mp.tan(p*h)
    return mp.tan(q*h) + (q**2-k**2)**2/(4*k**2*p*q)*mp.tan(p*h)


def _real(F):
    return mp.mpf(mp.re(F)) if abs(mp.re(F)) >= abs(mp.im(F)) else mp.mpf(mp.im(F))


def solve_rl(fd, h, P, family, bracket):
    f = lambda c: _real(rl(mp.mpf(c), fd, h, P, family))
    a, b = mp.mpf(bracket[0]), mp.mpf(bracket[1])
    fa = f(a)
    for _ in range(400):
        m = (a+b)/2
        fm = f(m)
        if fa*fm <= 0:
            b = m
        else:
            a, fa = m, fm
    return (a+b)/2


def main():
    P = P_iso()
    h = mp.mpf('1e-3')
    cL = mp.sqrt((P['lam']+2*P['mu'])/P['rho'])
    cT = mp.sqrt(P['mu']/P['rho'])
    cR = mp.re(CORE.rayleigh_speed(cL, cT))
    print('cL %.4f  cT %.4f  cR %.4f' % (float(cL), float(cT), float(cR)))
    ref = {10: {'S': [(4000, 5600)], 'A': [(200, 400)]},
           100: {'S': [(4000, 5400)], 'A': [(800, 1100)]},
           1000: {'S': [(4000, 5600)], 'A': [(2000, 2600)]}}
    for fd in (10, 100, 1000):
        print('fd =', fd)
        for fam in ('S', 'A'):
            for lo, hi in ref[fd][fam]:
                try:
                    c = solve_rl(fd, h, P, fam, (lo, hi))
                except Exception as e:
                    print('   %s: no root in %s  (%s)' % (fam, (lo, hi), str(e)[:40]))
                    continue
                res, n = det_residual(c, fd, h, P)
                print('   %s  c = %10.4f   |det B|/||B||^4 = %s   (roots %d)'
                      % (fam, float(mp.re(c)), mp.nstr(res, 3) if res is not None else 'n/a', n))


if __name__ == '__main__':
    main()
