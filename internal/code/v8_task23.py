"""Task 2e and the Task 3 experiment.

(1) Elastic limit with all couplings switched off: does det B, assembled from the roots and
    the null vectors as in Calculation G, vanish at the Rayleigh-Lamb speeds?
(2) Closure experiment: the seven rows of ours against the constitutive boundary conditions
    used in the nonlocal literature, at l/h = 0.05, 0.1, 0.2 for a plate of thickness 2h.
"""
import sys
sys.path.insert(0, '.')
import mpmath as mp
mp.mp.dps = 40
import core as CORE
import v8_model as VM
import v8_rows as R
import v8_b as VB

I = mp.mpc(0, 1)


def P_elastic_sumit(h):
    E, nu, rho = mp.mpf(70e9), mp.mpf('0.33'), mp.mpf(2700)
    lam = E*nu/((1+nu)*(1-2*nu))
    mu = E/(2*(1+nu))
    P = VM.const_sumit()
    P.update(dict(c11=lam+2*mu, c13=lam, c33=lam+2*mu, c44=mu, rho=rho,
                  e31=mp.mpf(0), e33=mp.mpf(0), e15=mp.mpf(0), p3=mp.mpf(0),
                  b1=mp.mpf(0), b3=mp.mpf(0), bth=mp.mpf(0), Pith=mp.mpf(0),
                  Eg=mp.mpf(0), q=mp.mpf(0), bn=mp.mpf(0), Dn=mp.mpf(0), vd=mp.mpf(0),
                  lg=mp.mpf(0), lnl=mp.mpf(0)))
    return P


def detB(k, w, P, h, ncond=5, alt=False):
    roots, b, R0 = CORE.roots_eta(k, w, P, Mfun=VM.build_M_sumit)
    roots = sorted(roots, key=lambda z: (mp.re(z), mp.im(z)))
    if len(roots) != 2*ncond:
        return None, len(roots)
    B = mp.matrix(2*ncond, len(roots))
    for m, eta in enumerate(roots):
        M = VM.build_M_sumit(eta, k, w, P)
        v = CORE.nullvec(M)
        rows = R.rows_sumit(eta, k, w, P)
        if ncond == 5:
            rows = [rows[0], rows[1], rows[4], rows[5], rows[6]]
        if alt:
            # constitutive closure: the normal strain gradients vanish on the face
            rows = [rows[0], rows[1], rows[4], rows[5], rows[6]]
            rows[2] = [I*k*eta, eta**2, 0, 0, 0]          # d(eps_zz)/dz
            rows[3] = [eta**2, I*k*eta, 0, 0, 0]          # d(eps_xz)/dz
        cols = [sum(rows[i][j]*v[j] for j in range(5)) for i in range(ncond)]
        sc = mp.e**(-abs(mp.re(eta))*h)
        for i in range(ncond):
            B[i, m] = cols[i]*mp.e**(eta*h)*sc
            B[ncond+i, m] = cols[i]*mp.e**(-eta*h)*sc
    return B, len(roots)


def equilibrate(B):
    n = B.rows
    rs = [max(abs(B[i, j]) for j in range(n)) for i in range(n)]
    cs = [max(abs(B[i, j]) for i in range(n)) for j in range(n)]
    Be = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            Be[i, j] = B[i, j]/(rs[i]*cs[j])
    return Be, mp.det(Be)


def detval(c, fd, h, P, ncond, alt=False):
    w = 2*mp.pi*mp.mpf(fd)/(2*h)
    k = w/mp.mpf(c)
    B, n = detB(k, w, P, h, ncond, alt)
    if B is None:
        return None, n
    Be, d = equilibrate(B)
    return d, n


def scan(cs, fd, h, P, ncond, alt=False):
    out = []
    prev = None
    for c in cs:
        d, n = detval(c, fd, h, P, ncond, alt)
        if d is None:
            prev = None
            continue
        val = mp.mpf(mp.re(d))
        if prev is not None and prev[1]*val < 0:
            out.append((0.5*(prev[0]+c), float(min(abs(prev[1]), abs(val)))))
        prev = (c, val)
    return out


def main():
    h = mp.mpf('1e-3')
    P = P_elastic_sumit(h)
    print('--- det B zeros, elastic limit, all couplings off, l_g = l_nl = 0')
    for fd in (10, 100):
        cs = [mp.mpf(x) for x in range(200, 5800, 60)]
        zs = scan(cs, fd, h, P, 5)
        print('  fd = %4d : %s' % (fd, [('%.1f' % c, '%.1e' % r) for c, r in zs]))


if __name__ == '__main__':
    main()
