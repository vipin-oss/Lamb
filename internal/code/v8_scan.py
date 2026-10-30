"""Task 2 (redo) and Task 3: the full B, singular-value scans.

The assembled B is a function of the speed c through k = omega/c.  Rows and columns are
equilibrated, then the smallest singular value of the equilibrated matrix is followed; a dip is a
mode.  Dimensions: 10 x 10 with l_g = 0 (five conditions per face, five roots per half) and
14 x 14 with l_g > 0 (seven per face, seven roots).
"""
import sys
sys.path.insert(0, '.')
import mpmath as mp
mp.mp.dps = 60
import core as CORE
import v8_model as VM
import v8_rows as R

I = mp.mpc(0, 1)
ROWS = dict(Sumit=R.rows_sumit, Neha=R.rows_neha, Anu=R.rows_anu)
BUILD = dict(Sumit=VM.build_M_sumit, Neha=VM.build_M_neha, Anu=VM.build_M_anu)


def sigma_min(B, iters=4):
    """smallest and largest singular value of the equilibrated matrix.
    Equilibration is done in mpmath; the singular values come from a complex SVD in
    double precision, which is safe once every entry is of order one."""
    import numpy as np
    n = B.rows
    M = [[B[i, j] for j in range(n)] for i in range(n)]
    for _ in range(iters):                       # Sinkhorn style row and column scaling
        for i in range(n):
            s = max(abs(M[i][j]) for j in range(n))
            if s > 0:
                M[i] = [x/s for x in M[i]]
        for j in range(n):
            s = max(abs(M[i][j]) for i in range(n))
            if s > 0:
                for i in range(n):
                    M[i][j] = M[i][j]/s
    A = np.array([[complex(M[i][j]) for j in range(n)] for i in range(n)])
    sv = np.linalg.svd(A, compute_uv=False)
    return float(sv.min()), float(sv.max())


def alt_rows(rows, ncond):
    """the alternative closure: the two double tractions are replaced by the constitutive
    conditions of the nonlocal law, d(eps)/dz = 0 on the face, in the same two slots"""
    out = list(rows)
    if ncond == 7:
        out[2] = None            # filled by the caller, which knows the amplitudes
        out[3] = None
    return out


def const_rows(sch, eta, k, w, P, lnl, s):
    """the constitutive closure of the nonlocal law, d(eps)/dz = s eps/l_nl on the face,
    written for the two normal strains of the plane-strain plate"""
    f = eta - s/lnl
    return [[0, eta*f, 0, 0, 0], [eta*f, I*k*f, 0, 0, 0]]


def build_B(sch, k, w, P, h, closure='variational', magbc='open'):
    mp.mp.dps = 60
    Mfun, rowfun = BUILD[sch], ROWS[sch]
    roots, b, R0 = CORE.roots_eta(k, w, P, Mfun=Mfun)
    roots = sorted(roots, key=lambda z: (mp.re(z), mp.im(z)))
    lg = P['lg']
    ncond = 7 if abs(lg) > 0 else 5
    if len(roots) != 2*ncond:
        return None, len(roots), ncond
    n = len(roots)
    B = mp.matrix(n, n)
    for m, eta in enumerate(roots):
        M = Mfun(eta, k, w, P)
        v = CORE.nullvec(M)
        rows = rowfun(eta, k, w, P)
        if magbc == 'closed' and len(rows) == 7:
            rows = list(rows)
            # the B_z = 0 row is rows[5]; replacing rows[6] throws away the adiabatic
            # condition instead, which is the fault found in round v8f.
            rows[5] = [0, 0, 0, 1, 0]        # psi = 0 on the face instead of B_z = 0
        if ncond == 5:
            rows = [rows[0], rows[1], rows[4], rows[5], rows[6]]
        elif closure == 'constitutive':
            rows = list(rows)
            top = const_rows(sch, eta, k, w, P, P['lnl'], +1)
            bot = const_rows(sch, eta, k, w, P, P['lnl'], -1)
            rows[2], rows[3] = top
            rows_bot = list(rows)
            rows_bot[2], rows_bot[3] = bot
        cols = [sum(rows[i][j]*v[j] for j in range(5)) for i in range(ncond)]
        if closure == 'constitutive' and ncond == 7:
            cols_bot = [sum(rows_bot[i][j]*v[j] for j in range(5)) for i in range(ncond)]
        else:
            cols_bot = cols
        sc = mp.e**(-abs(mp.re(eta))*h)
        zt = mp.e**(eta*h)*sc
        zb = mp.e**(-eta*h)*sc
        # a root that decays over a length much shorter than the plate is attached to one
        # face only; its entry on the far face is set to zero instead of 1e-700, which keeps
        # the matrix properly scaled and does not change the determinant's zeros.
        if abs(mp.re(eta))*h > 30:
            if mp.re(eta) < 0:
                zt = mp.mpf(0)
            else:
                zb = mp.mpf(0)
        for i in range(ncond):
            B[i, m] = cols[i]*zt
            B[ncond + i, m] = cols_bot[i]*zb
    return B, n, ncond


def point(sch, c, fd, h, P, closure='variational', magbc='open'):
    w = 2*mp.pi*mp.mpf(fd)/(2*h)
    k = w/mp.mpf(c)
    B, n, ncond = build_B(sch, k, w, P, h, closure, magbc)
    if B is None:
        return None, n, ncond
    s0, s1 = sigma_min(B)
    return float(s0), n, ncond


def scan(sch, fd, h, P, cs, closure='variational', verbose=False):
    out = []
    for c in cs:
        s, n, ncond = point(sch, c, fd, h, P, closure)
        if verbose:
            print('    c=%8.1f  sigma_min=%s  roots=%d' % (c, ('%.3e' % s) if s is not None else 'n/a', n))
        out.append((float(c), s))
    return out


def dips(curve, thresh=None):
    """local minima of the sigma_min curve"""
    good = [(c, s) for c, s in curve if s is not None]
    if not good:
        return []
    vals = [s for _, s in good]
    med = sorted(vals)[len(vals)//2]
    out = []
    for i in range(1, len(good)-1):
        c, s = good[i]
        if s <= good[i-1][1] and s <= good[i+1][1]:
            if thresh is None or s < med*thresh:
                out.append((c, s, med))
    return out
