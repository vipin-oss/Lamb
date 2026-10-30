"""Audit: bulk speeds at eta = 0 for every frequency where a dip was quoted.

A dip of sigma_min(c) sitting on a bulk speed is a degenerate zero of det M at eta = 0,
not a plate mode.  The bulk speeds are the zeros of det M(0, k = omega/c, omega) for real c.
Each local minimum of |det| is refined by golden section over +-5 m/s and kept when the refined
value is six orders or more below the median of the scan.
"""
import sys
sys.path.insert(0, '.')
import mpmath as mp
mp.mp.dps = 40
import v8_model as VM

I = mp.mpc(0, 1)


def det_eta0(sch, c, fd, h, P):
    w = 2*mp.pi*mp.mpf(fd)/(2*h)
    k = w/mp.mpf(c)
    return mp.det(VM.BUILDERS[sch](mp.mpf(0), k, w, P))


def _refine(sch, c0, fd, h, P, half=5.0):
    a, b = mp.mpf(c0) - half, mp.mpf(c0) + half
    gr = (mp.sqrt(5) - 1)/2
    f = lambda x: abs(det_eta0(sch, x, fd, h, P))
    c = b - gr*(b - a); d = a + gr*(b - a)
    fc, fd_ = f(c), f(d)
    for _ in range(60):
        if fc < fd_:
            b, d, fd_ = d, c, fc
            c = b - gr*(b - a); fc = f(c)
        else:
            a, c, fc = c, d, fd_
            d = a + gr*(b - a); fd_ = f(d)
        if b - a < mp.mpf('0.001'):
            break
    x = (a + b)/2
    return x, abs(f(x))


def bulk(sch, fd, h, P, lo=150, hi=7200, step=1, rel=1e-6):
    vals = []
    c = lo
    while c <= hi:
        vals.append((c, float(abs(det_eta0(sch, c, fd, h, P)))))
        c += step
    mags = [v for _, v in vals if v > 0]
    scale = sorted(mags)[len(mags)//2] if mags else 1.0
    out = []
    for i in range(1, len(vals) - 1):
        if vals[i][1] < vals[i - 1][1] and vals[i][1] < vals[i + 1][1]:
            x, v = _refine(sch, vals[i][0], fd, h, P)
            if float(v) / scale < rel:
                out.append((float(x), float(v)/scale))
    return out, scale
