#!/usr/bin/env python3
"""
task0_feasibility_scaling.py -- Task-0 sanity check (NOT a step of the paper).

Purpose: before committing the scholar to a hook, check with back-of-envelope
numbers that the proposed two-channel attenuation picture is physically reachable
for a real piezoelectric semiconductor (ZnO). Pure algebra, no dispersion solve.

WHAT THIS IS NOT: this is not the paper model. It uses leading-order textbook
expressions (Zener/Lifshitz-Roukes thermoelastic damping, Hutson-White
acoustoelectric attenuation) to check ORDERS OF MAGNITUDE and the existence of
crossovers. The full determinant in steps/step*.md is the authority.

CONSTANT STATUS (see paper/problem_v2.md section 5):
  SOURCED   = value taken from a cited source
  SPREAD    = sources disagree; both ends used
  UNVERIFIED= no source yet; used only for scaling, must be fixed before Step 3
"""
import math

# ---------------------------------------------------------------- constants
E0 = 8.8541878128e-12
q  = 1.602176634e-19
kB = 1.380649e-23
T  = 300.0

C33 = 211.0e9          # Pa   [S] arXiv:cond-mat/0507217v2, "measured" row
C11 = 206.0e9          # Pa   [S] same
rho = 5680.0           # kg/m3 [S] eFunda ZnO (AZoM 5660, review 5605 -> SPREAD ~1%)
eps33 = 12.64 * E0     # F/m  [S] eFunda ZnO
eps11 = 9.16 * E0      # F/m  [S] eFunda ZnO
e33 = 1.34             # C/m2 [S] arXiv:cond-mat/0507217v2
mu  = 200.0e-4         # m2/Vs (200 cm2/Vs) [S] AZoM / IJEM review
kth_bulk = 60.0        # W/mK [S] AZoM                       \
kth_film = 1.2         # W/mK [S] IJEM review (thin film)     / SPREAD ~50x
cp   = 500.0           # J/kgK  [U] no source yet -> FIX before Step 3
alphaT = 4.0e-6        # 1/K    [U] no source yet -> FIX before Step 3

cph = math.sqrt(C33 / rho)      # ~bar velocity along z, order of magnitude

def k2():
    """1-D piezoelectric coupling factor K^2 = e33^2/(C33 eps33). Computed, not quoted."""
    return e33**2 / (C33 * eps33)

def zener():
    """Zener parameter Delta_E = E alphaT^2 T /(rho cp); Q^-1_max ~ Delta_E/2."""
    return C33 * alphaT**2 * T / (rho * cp)

def sigma(n0):
    return n0 * q * mu

def w_carrier(n0):
    """Dielectric (carrier) relaxation frequency of the acoustoelectric peak."""
    return sigma(n0) / eps33

def alpha_th(kth):
    """Thermal diffusivity."""
    return kth / (rho * cp)

def w_thermal(h, kth):
    """Zener/Lifshitz-Roukes flexural TED peak, plate thickness 2h: w = pi^2 a/(2h)^2."""
    return math.pi**2 * alpha_th(kth) / (2.0 * h)**2

def h_star(n0, kth):
    """Thickness where the two peaks coincide: (2h)^2 = pi^2 a eps/(n0 q mu)
       => h* = (pi/2) sqrt(a eps/(n0 q mu)).  Rewritten: h* = (pi/2) LD sqrt(Le)."""
    a = alpha_th(kth)
    return 0.5 * math.pi * math.sqrt(a * eps33 / (n0 * q * mu))

def debye(n0):
    return math.sqrt(eps33 * kB * T / (n0 * q**2))

def main():
    print(__doc__)
    print("=" * 78)
    print("ZnO, T = 300 K.  c33/rho bar speed = %.0f m/s" % cph)
    print("K^2 = e33^2/(C33 eps33) = %.4f" % k2())
    print("Zener Delta_E = %.3e  -> Q^-1_max ~ %.2e  (k_i/k_r ~ %.1e)"
          % (zener(), zener() / 2, zener() / 2))
    print("Hutson-White max acoustoelectric k_i/k_r ~ K^2/2 = %.2e" % (k2() / 2))
    print("RATIO carrier/TED at their own peaks = %.0f x"
          % ((k2() / 2) / (zener() / 2)))
    print()
    print("A. Carrier peak: n0*(f) = eps w/(q mu),  fd_c = f*(2h)")
    print("   %-10s %-12s %-12s %-14s" % ("f [Hz]", "n0* [m^-3]", "fd_c(2h=1um)", "fd_c(2h=100um)"))
    for f in (1e6, 1e8, 1e9, 1e10):
        n0 = eps33 * 2 * math.pi * f / (q * mu)
        print("   %-10.0e %-12.2e %-12.3e %-14.3e" % (n0, n0, f * 1e-6, f * 1e-4))
    print()
    print("B. Thermal (TED) peak: f_th = pi a/(2(2h)^2);  fd_th = f_th*2h  [k=1.2 and 60 W/mK]")
    print("   %-10s %-14s %-14s %-14s %-14s" % ("2h [m]", "f_th(k=1.2)", "fd_th", "f_th(k=60)", "fd_th"))
    for th in (1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3):
        h = th / 2
        f1 = w_thermal(h, kth_film) / (2 * math.pi)
        f2 = w_thermal(h, kth_bulk) / (2 * math.pi)
        print("   %-10.1e %-14.3e %-14.3e %-14.3e %-14.3e"
              % (th, f1, f1 * th, f2, f2 * th))
    print()
    print("C. Crossing thickness h* (peak-position coincidence) and Debye length")
    print("   %-10s %-14s %-14s %-12s %-12s" % ("n0 [m^-3]", "h*(k=1.2)[m]", "h*(k=60)[m]", "L_D [m]", "sqrt(Le)"))
    for n0 in (1e20, 1e21, 1e22, 1e23):
        D = mu * kB * T / q
        Le1 = alpha_th(kth_film) / D
        Le2 = alpha_th(kth_bulk) / D
        print("   %-10.0e %-14.3e %-14.3e %-12.3e %-12.3e"
              % (n0, h_star(n0, kth_film), h_star(n0, kth_bulk), debye(n0), math.sqrt(Le1)))
    print("   check: h* = (pi/2) L_D sqrt(Le)?  n0=1e21, k=60: formula %.3e"
          % (0.5 * math.pi * debye(1e21) * math.sqrt(alpha_th(kth_bulk) / (mu * kB * T / q))))
    print()
    print("D. Carrier-nulling bias: need v_d = c_ph, so E = c_ph/mu; Joule heat sigma E^2")
    Enull = cph / mu
    print("   E_null = %.3e V/m = %.2f kV/cm" % (Enull, Enull / 1e5))
    print("   %-12s %-14s %-14s" % ("n0 [m^-3]", "sigma [S/m]", "sigma E^2 [W/m^3]"))
    for n0 in (1e19, 1e20, 1e21, 1e22):
        s = sigma(n0)
        print("   %-12.0e %-14.3e %-14.3e" % (n0, s, s * Enull**2))
    print()
    ratio = (zener() / 2) / (k2() / 2)
    print("E. Resolution check: floor TED k_i/k_r vs carrier peak k_i/k_r")
    print("   floor/peak = %.1e  (carrier peak is %.0fx the thermal floor)"
          % (ratio, 1.0 / ratio))
    print("   => the floor is visible only where the carrier channel is suppressed")
    print("      (screened at high n0, or nulled by drift), not near the carrier peak.")

if __name__ == "__main__":
    main()
