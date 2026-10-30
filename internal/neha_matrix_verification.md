# Paper B (Neha): numerical verification of the matrix route

Internal only; nothing here goes into `Lamb_Neha.tex`.

Code: `internal/code/core.py` (`M_neha`, `coeffs_scaled`, `roots_eta`, `nullvec`, `parity_matrix`),
driver `internal/code/t_neha_anu.py`. mpmath at 60 digits.

Placeholder constants (internal only, order-of-magnitude values for a 1D hexagonal piezoelectric
quasicrystal of the Al-Pd-Mn type): c11 165, c13 66, c33 185, c44 47 GPa; R1 1.5, R2 -1.0, R3 0.4 GPa;
K1 0.9, K2 1.2 GPa; e31 -0.5, e33 1.3, e15 -0.4 C/m^2; eps11 9e-11, eps33 1.1e-10 F/m; beta1 beta3 3e5 Pa/K;
beta^w 5e5 Pa/K; p3 -1e-5 C/(m^2 K); rho 5600, rho_p 1.2 kg/m^3; gamma 1e8 kg/(m^3 s); l_g = l_nl = 1e-8 m;
T0 300 K; rho c_p 2.6e6 J/(m^3 K); k_th 50 W/(m K); tau_q 1e-11 s. These are not measured values and are not
used in the paper.

## Test 1. Degree of det M(eta)

Scaled fit in t = eta/R0, R0 = 4 max(|k|,1), 25 samples, zero threshold 1e-25 of the largest coefficient.
Checked at k = 3e5 rad/m and omega = 2 pi fd for fd = 1e6, 1e8, 1e10 rad/s (three frequencies, so three
positions in the spectrum).

| l_g | degree, all three frequencies | expected | verdict |
|---|---|---|---|
| 0 | 10 | 10 | PASS |
| 1e-8 | 14 | 14 | PASS |

The phason equation is second order, so the phason adds no root. Purely nonlocal change (l_nl alone) leaves
the degree at 10, as in Paper A.

## Test 2. Parity in eta

Sign vectors s with M(-eta) = diag(s) M(eta) diag(s), at eta = 1.3 + 0.4 i, tolerance 1e-30.

| case | sign vectors | reading |
|---|---|---|
| all couplings on | (-1,+1,+1,+1,-1) and its negative | det M even, S/A split exists |
| R1 = R2 = R3 = 0, beta^w = 0 | four vectors | split exists; the extra two come from the decoupled phason, whose sign is then free |
| R = 0 only | two vectors | split exists |
| beta^w = 0 only | two vectors | split exists |

**Result, and the answer to the question in section 6 of the prompt.** No coupling in this model breaks the
parity. The phonon-phason constants R1, R2, R3, the thermo-phason coefficient beta^w, the pyroelectric p3 and
the piezoelectric e do not break it. The sign vector is the same as in Papers A and C in its odd/even
pattern: displacement along the plate and temperature odd through the thickness, the other three fields even.

The physical reading: R1 and R2 enter the momentum rows with one z-derivative more than the phason row, which
is exactly the pattern the sign vector needs. What breaks the pairing in Paper A is the carrier density,
which is an even field sitting in a row coupled to a temperature that must be odd. There is no carrier field
in a quasicrystal, so the obstruction does not exist.

Consequence for the matrix: the boundary matrix factorises and the two 7x7 blocks can be solved separately.
This is a stronger statement than the one in the research plan, which did not decide the question.

## Test 3. Roots and the limit l_g -> 0

At k = 3e5, omega = 2 pi 1e8: l_g = 0 gives 10 roots, degree 10; l_g = 1e-8 gives 14 roots, degree 14, of
which 4 have l_g|eta| > 0.5 (the gradient roots). Same structure as Paper A. Verdict: PASS.

## Test 4. Null vector

At the root of smallest |eta|: ||M v|| / max|M| = 8.1e-72. Verdict: PASS.

## Test 5. Number of roots against number of conditions

14 roots, 7 conditions per face (b1..b7 of the master file); 10 roots and 5 conditions at l_g = 0, because
the two double-traction rows vanish with l_g^2. Consistent.

## Not done in this round

1. The phason wave and diffusion limits (c_ph = sqrt(K2/rho_p), D_ph = K2/gamma) are derived in Calculation H
   but not tested numerically; the branch tracking over complex k is not built yet.
2. The thermo-phason damping peak is derived, not computed.
3. The 14x14 boundary assembly for this paper is not built, for the same reason as in Paper A (the
   double-traction moduli of the gradient theory are not fixed by any constant set).

## For the microsite of the paper

The 2026 competitor (doi 10.1007/s10338-026-00755-4) is unread and is flagged in the .bib with a note. Until
it is read, the thermal novelty claim stays provisional and the text says so in the introduction.
