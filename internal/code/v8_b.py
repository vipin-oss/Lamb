"""Assembly of B from the roots of det M(eta) and the null vectors, with column
scaling exp(-|Re eta| h), for the v8 matrices and row functions.
"""
import sys
sys.path.insert(0, '.')
import mpmath as mp
import core as CORE
import v8_model as VM
import v8_rows as R

I = mp.mpc(0, 1)


def roots_eta(Mfun, k, w, P, R0=None, tol=1e-25):
    roots, b, R0 = CORE.roots_eta(k, w, P, Mfun=Mfun, R0=R0, tol=tol)
    return roots, b, R0


def assemble(Mfun, ncond):
    """return a function B(k, w, P, h) -> mp.matrix"""
    def B_of(k, w, P, h, R0=None):
        roots, b, R0 = roots_eta(Mfun, k, w, P, R0)
        roots = sorted(roots, key=lambda z: (mp.re(z), mp.im(z)))
        n = len(roots)
        if n != 2*ncond:
            return None, roots
        B = mp.matrix(2*ncond, n)
        for m, eta in enumerate(roots):
            M = Mfun(eta, k, w, P)
            v = CORE.nullvec(M)
            rows = R.ROWS_FOR(Mfun)(eta, k, w, P)
            if ncond == 5:                      # gradient length zero: rows 3 and 4 vanish
                rows = [rows[0], rows[1], rows[4], rows[5], rows[6]]
            cols = [sum(rows[i][j]*v[j] for j in range(5)) for i in range(ncond)]
            sc = mp.e**(-abs(mp.re(eta))*h)
            for i in range(ncond):
                B[i, m] = cols[i]*mp.e**(eta*h)*sc
                B[ncond+i, m] = cols[i]*mp.e**(-eta*h)*sc
        return B, roots
    return B_of


ROWFUN = {id(VM.build_M_sumit): R.rows_sumit, id(VM.build_M_neha): R.rows_neha,
          id(VM.build_M_anu): R.rows_anu}


def attach_rows():
    """let assemble() find the row functions: keyed by the builder function"""
    R.ROWS_FOR = lambda Mfun: ROWFUN[id(Mfun)]
    return R.ROWS_FOR


attach_rows()
