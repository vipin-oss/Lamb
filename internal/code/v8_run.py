"""Task 2 (redo) driver: dips of the scaled determinant of the full B.

The determinant is used rather than the smallest singular value because four roots of the
coupled system are so evanescent (|Re eta| h of order 10^3 and more) that their columns are
one-sided: they force sigma_min down by a constant factor at every speed and hide the dips.
The equilibrated determinant keeps the zeros and loses the level.
"""
import sys
sys.path.insert(0, '.')
import mpmath as mp
mp.mp.dps = 60
import v8_model as VM
import v8_scan as S
import v8_disp as D

I = mp.mpc(0, 1)


def det_eq(B):
    N = B.rows
    M = [[B[i, j] for j in range(N)] for i in range(N)]
    for _ in range(4):
        for i in range(N):
            s = max(abs(x) for x in M[i])
            if s > 0:
                M[i] = [x/s for x in M[i]]
        for j in range(N):
            s = max(abs(M[i][j]) for i in range(N))
            if s > 0:
                for i in range(N):
                    M[i][j] = M[i][j]/s
    A = mp.matrix(N, N)
    for i in range(N):
        for j in range(N):
            A[i, j] = M[i][j]
    d = mp.det(A)
    return abs(d) if d != 0 else mp.mpf('1e-999')


def logdet(sch, c, fd, h, P, closure='variational'):
    w = 2*mp.pi*mp.mpf(fd)/(2*h)
    k = w/mp.mpf(c)
    B, n, ncond = S.build_B(sch, k, w, P, h, closure)
    if B is None:
        return None
    return float(mp.log10(det_eq(B)))


def scan(sch, fd, h, P, cs, closure='variational'):
    return [(c, logdet(sch, c, fd, h, P, closure)) for c in cs]


def refine(sch, fd, h, P, lo, hi, closure='variational', n=40):
    a, b = mp.mpf(lo), mp.mpf(hi)
    gr = (mp.sqrt(5)-1)/2
    f = lambda x: logdet(sch, x, fd, h, P, closure)
    c = b - gr*(b-a); d = a + gr*(b-a)
    fc, fd_ = f(c), f(d)
    for _ in range(n):
        if fc < fd_:
            b, d, fd_ = d, c, fc
            c = b - gr*(b-a); fc = f(c)
        else:
            a, c, fc = c, d, fd_
            d = a + gr*(b-a); fd_ = f(d)
        if b - a < mp.mpf('0.01'):
            break
    return (a+b)/2


def dips(curve, depth=1.0):
    good = [(c, v) for c, v in curve if v is not None]
    out = []
    for i in range(1, len(good)-1):
        c, v = good[i]
        if v < good[i-1][1] and v < good[i+1][1] and (good[i-1][1]-v) > depth:
            out.append((c, v))
    return out
