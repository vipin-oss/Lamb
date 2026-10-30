# Step 1 (all three scholars): classical Rayleigh-Lamb plate

**Goal:** reproduce the dispersion of a traction-free isotropic elastic plate. Everything else is built on this.

## Equations
Plate |z| <= h, thickness 2h, wave exp[i(kx - wt)], plane strain.
Displacement potentials: u = grad(phi) + curl(psi), with
- phi'' + p^2 phi = 0, p^2 = w^2/cL^2 - k^2
- psi'' + q^2 psi = 0, q^2 = w^2/cT^2 - k^2
- cL^2 = (lambda + 2 mu)/rho, cT^2 = mu/rho

Traction-free faces: sigma_zz = sigma_xz = 0 at z = +-h. Splitting into even/odd in z gives

- Symmetric:  (q^2 - k^2)^2 * cos(ph) sin(qh)/q + 4 k^2 * p sin(ph) cos(qh) = 0
- Antisymmetric: 4 k^2 * q sin(qh) cos(ph) + (q^2 - k^2)^2 * cos(qh) sin(ph)/p = 0

(These forms stay real when p or q is imaginary.)

## What to do
1. Derive the two equations above yourself (do not copy). Keep a one-page derivation.
2. Solve for c = w/k at each fd = f*2h; track S0, S1, S2, A0, A1, A2 as branches.
3. Use aluminium: E = 70 GPa, nu = 0.33, rho = 2700 kg/m^3.

## Checks to send (plot + numbers)
| Check | Expected (aluminium) |
|---|---|
| S0 as fd -> 0 | 2 cT sqrt(1 - cT^2/cL^2) = 5393.9 m/s |
| A0 as fd -> 0 | c -> 0 like sqrt(fd) |
| Large fd, S0 and A0 | -> Rayleigh speed (about 2906 m/s) |
| Cutoffs (fd = f*2h) | A1: cT/2 = 1561; S1: cL/2 = 3099; S2: cT = 3122; A2: cL = 6198 Hz*m |
| Mode counts | 1S+1A below 1561; 3S+2A at fd = 3434 |

Reference implementation: `common/rayleigh_lamb.py` (run `python3 rayleigh_lamb.py`).
Send the c-vs-fd plot and the CSV of the fixed comparison points (see docs/02_workflow_crosscheck.md).
