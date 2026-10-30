"""Step-1 reference solver: classical Rayleigh-Lamb dispersion, isotropic plate.

Used by all three projects as the first cross-check (all coupling OFF must return this).

Plate thickness 2h, free faces. Frequency-thickness fd = f * 2h.
Characteristic equations (p^2 = w^2/cL^2 - k^2, q^2 = w^2/cT^2 - k^2), written in an
even-in-p, even-in-q form so they stay real when p or q is imaginary:

  symmetric : (q^2-k^2)^2 * sin(qh)/q * cos(ph) + 4 k^2 * p sin(ph) * cos(qh) = 0
  antisym.  : 4 k^2 * q sin(qh) * cos(ph) + (q^2-k^2)^2 * cos(qh) * sin(ph)/p = 0
"""
import numpy as np
from numpy.lib import scimath


def _terms(c, fd, cL, cT):
    h = 1.0
    w = 2 * np.pi * fd / 2.0  # f*2h = fd, take h=1 => f = fd/2
    k = w / c
    p = scimath.sqrt((w / cL) ** 2 - k ** 2)
    q = scimath.sqrt((w / cT) ** 2 - k ** 2)
    return h, k, p, q


def F_sym(c, fd, cL, cT):
    h, k, p, q = _terms(c, fd, cL, cT)
    sinc_q = np.where(np.abs(q) < 1e-12, h, np.sin(q * h) / np.where(q == 0, 1, q))
    psin_p = p * np.sin(p * h)
    return ((q ** 2 - k ** 2) ** 2 * sinc_q * np.cos(p * h)
            + 4 * k ** 2 * psin_p * np.cos(q * h)).real


def F_anti(c, fd, cL, cT):
    h, k, p, q = _terms(c, fd, cL, cT)
    sinc_p = np.where(np.abs(p) < 1e-12, h, np.sin(p * h) / np.where(p == 0, 1, p))
    qsin_q = q * np.sin(q * h)
    return (4 * k ** 2 * qsin_q * np.cos(p * h)
            + (q ** 2 - k ** 2) ** 2 * np.cos(q * h) * sinc_p).real


def rayleigh_speed(cL, cT):
    """Exact Rayleigh surface-wave speed for an isotropic half-space.

    Root of  (2 - c^2/cT^2)^2 = 4 sqrt(1 - c^2/cL^2) sqrt(1 - c^2/cT^2),
    found by bisection on (0.5 cT, cT).  For E=70 GPa, nu=0.33, rho=2700
    this gives 2909.73 m/s, which is the thick-plate limit of both S0 and A0
    and the value used by the Step-1 check (tolerance 1e-3 relative).
    Do NOT use the Viktorov formula for a check: it is ~0.1% low (2906.5).
    """
    def f(c):
        return ((2.0 - c * c / cT ** 2) ** 2
                - 4.0 * np.sqrt(1.0 - c * c / cL ** 2) * np.sqrt(1.0 - c * c / cT ** 2))
    a, b = 0.5 * cT, cT * (1.0 - 1e-12)
    for _ in range(300):
        m = 0.5 * (a + b)
        if f(a) * f(m) <= 0.0:
            b = m
        else:
            a = m
    return 0.5 * (a + b)


def speeds(E=70e9, nu=0.33, rho=2700.0):
    lam = E * nu / ((1 + nu) * (1 - 2 * nu))
    mu = E / (2 * (1 + nu))
    return np.sqrt((lam + 2 * mu) / rho), np.sqrt(mu / rho)


def roots_at(fd, F, cL, cT, cmax_factor=40.0, n=200000):
    """Phase velocities (real) at one fd, by sign-change scan + bisection."""
    cs = np.linspace(0.5 * cT, cmax_factor * cT, n)
    vals = F(cs, fd, cL, cT)
    out = []
    for i in np.where(np.sign(vals[:-1]) * np.sign(vals[1:]) < 0)[0]:
        a, b = cs[i], cs[i + 1]
        fa = vals[i]
        for _ in range(60):
            m = 0.5 * (a + b)
            fm = F(np.array(m), fd, cL, cT)
            if np.sign(fm) == np.sign(fa):
                a, fa = m, fm
            else:
                b = m
        r = 0.5 * (a + b)
        # drop spurious sign flips from poles/zero-crossings of the scaling
        if abs(F(np.array(r), fd, cL, cT)) < 1e3 * max(1.0, np.abs(vals).max()) * 1e-6 + 1e-3 * np.abs(vals).max():
            out.append(r)
    return np.array(out)


def checks():
    cL, cT = speeds()
    nu = 0.33
    cR = rayleigh_speed(cL, cT)                            # exact root: 2909.73 m/s
    cR_viktorov = cT * (0.862 + 1.14 * nu) / (1 + nu)      # approx, ~0.1% low: 2906.5
    c_plate = 2 * cT * np.sqrt(1 - (cT / cL) ** 2)         # S0 low-fd limit
    print(f"cL={cL:.1f}  cT={cT:.1f}  cR(exact)={cR:.1f}  "
          f"cR(Viktorov, do not use for checks)={cR_viktorov:.1f}  S0(fd->0)={c_plate:.1f}")
    assert abs(cR - 2909.7) / 2909.7 < 1e-3, "exact Rayleigh speed drifted from 2909.7 m/s"

    r = roots_at(20.0, F_sym, cL, cT)
    print("S0 thin limit (fd=20) ->", r[:1], " expected", round(c_plate, 1))

    r = roots_at(20e3, F_sym, cL, cT)
    r2 = roots_at(20e3, F_anti, cL, cT)
    # thick-plate check: both lowest branches must approach the exact Rayleigh speed
    # to 1e-3 relative (docs/02_workflow_crosscheck.md tolerance class "large fd")
    for name, rr in (("S0", r), ("A0", r2)):
        assert len(rr) > 0, f"{name} not found at fd=20 kHz*m"
        rel = abs(rr[0] - cR) / cR
        print(f"  very thick plate (fd=20 kHz*m): {name} -> {rr[0]:.2f}  cR={cR:.2f}  "
              f"rel.diff={rel:.2e}  {'PASS' if rel < 1e-3 else 'FAIL'}")
        assert rel < 1e-3, f"{name} thick-plate limit fails the 1e-3 Rayleigh check"

    # first symmetric/antisymmetric cutoffs: fd = n cT (antisym n odd? see below) and n cL
    print("Cutoffs (fd=f*2h): shear n*cT/2 =", [round(n * cT / 2) for n in (1, 2, 3)],
          " longitudinal n*cL/2 =", [round(n * cL / 2) for n in (1, 2)],
          "(S: shear n even, long n odd; A: shear n odd, long n even)")
    for fd in (0.9 * cT / 2, 1.1 * cT / 2, 1.1 * cT, 1.1 * cL / 2):
        print(f" fd={fd:.0f}: #sym modes={len(roots_at(fd, F_sym, cL, cT))}  #anti modes={len(roots_at(fd, F_anti, cL, cT))}")


if __name__ == "__main__":
    checks()
