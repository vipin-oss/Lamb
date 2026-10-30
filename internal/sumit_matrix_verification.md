# Paper A (Sumit): numerical verification of the matrix route

All numbers here are internal. None of them goes into `Lamb_Sumit.tex`.

Code: `internal/code/core.py` (builders, scaled polynomial fit, roots, adjugate null vector),
`internal/code/t1_lamb.py`, `internal/code/t_sumit.py`, `internal/code/t_sumit4.py`. mpmath at 60 digits
(the prompt asks for about 80; 60 was enough for every residual below and mpmath's `polyroots` was run with
`extraprec=800`). Reference for the Rayleigh-Lamb check: `common/rayleigh_lamb.py`, the earlier validated
solver (its own checks: thin-plate limit and Rayleigh limit, see below).

Placeholder constants used for Sumit (ZnO-type, internal only): c11 209.7, c13 105.4, c33 211.2, c44 42.4
GPa; e31 -0.57, e33 1.32, e15 -0.48 C/m^2; eps11 8.54 eps0, eps33 10.2 eps0; beta1 beta3 4e5 Pa/K;
p3 -1e-5 C/(m^2 K); rho 5680 kg/m^3; q 1.602176634e-19 C; Dn 1e-3 m^2/s; bn 0.01 m^2/(V s); n0 1e20 m^-3;
beta_th 1e18 A/(m K); Pi_th -1e-3 V; tau_R 1e30 s (recombination off); T0 300 K; rho c_p 2.8e6 J/(m^3 K);
k_th 60 W/(m K); tau_q 1e-11 s. Wave point used for the algebraic tests: k = 3e5 rad/m,
omega = 2*pi*1e8 rad/s.

## Test 1. Rayleigh-Lamb cross-check of the 4x4 matrix route

Method: the isotropic mechanical matrix (2x2) with the four exact roots eta = +-i p, +-i q is turned into the
4x4 boundary matrix (rows sigma_zz, sigma_xz at +h and -h, columns the four waves, every column scaled by
exp(-|Re eta| h)). The reference roots come from the classical transcendental equations in
`common/rayleigh_lamb.py`. The determinant of the matrix at the reference root is normalised by ||B||^4.

| fd (Hz m) | branch | c_ref (m/s) | det/||B||^4 at c_ref | 0.1 % away | verdict |
|---|---|---|---|---|---|
| 10 | S0 | 5393.905338 | 1.07e-19 | 9.45e-07 | PASS |
| 10 | A0 | 311.637658 | 1.41e-19 | 8.07e-11 | PASS |
| 100 | S0 | 5393.171945 | 4.85e-18 | 8.95e-05 | PASS |
| 100 | A0 | 954.234069 | 3.09e-18 | 3.18e-07 | PASS |
| 1000 | S0 | 5308.588707 | 9.88e-16 | 3.98e-03 | PASS |
| 1000 | A0 | 2326.643110 | 1.98e-17 | 1.10e-04 | PASS |

Reference limits that validate the reference itself: cL 6197.8243, cT 3121.9527, Rayleigh 2909.731393 m/s,
and the thin-plate S0 value at fd = 10 is within 1.4e-6 of sqrt(E/(rho(1-nu^2))) = 5393.9127 m/s.
Tolerance for the test was 1e-5 on the relative distance; the residuals above are far below it. Largest
residual: 9.88e-16 (normalised determinant) at fd = 1000, S0.

## Test 2. Degree of det M(eta)

Coefficients are fitted on a circle of radius R0 = 4 max(|k|, 1) with 25 samples, in the scaled variable
t = eta/R0, so the coefficients stay comparable. A coefficient counts as zero if it is below 1e-25 of the
largest.

| l_g (m) | l_nl (m) | degree found | expected | verdict |
|---|---|---|---|---|
| 0 | 0 | 10 | 10 | PASS |
| 1e-8 | 0 | 14 | 14 | PASS |
| 0 | 1e-8 | 10 | 10 | PASS |
| 1e-8 | 1e-8 | 14 | 14 | PASS |

This confirms both items of section 2 of the supervisor's file: the gradient length raises the degree to 14,
the nonlocal length does not raise it.

## Test 3. Parity of det M in eta

Test: does a diagonal sign vector s exist with M(-eta) = diag(s) M(eta) diag(s)? If it does, det M is even and
the roots pair. Checked at three complex eta with a relative tolerance of 1e-30.

| switch | sign vectors found | reading |
|---|---|---|
| beta_th = Pi_th = 0 | (-1,+1,+1,+1,-1) and its negative | even, roots pair |
| beta_th only (Pi_th = 0) | none | not even |
| Pi_th only (beta_th = 0) | none | not even |
| beta_th only, p3 = 0 | none | not even |
| Pi_th only, p3 = 0 | none | not even |
| beta_th only, e = 0 | none | not even |
| both on (all couplings) | none | not even |

**Correction to the supervisor's item 3.** His file says the determinant is not even when beta_th and Pi_th
are non-zero **and** a polar coupling (e or p3) is non-zero. The algebra and the numbers say the conjunction is
not needed: the parity fails as soon as either thermodiffusion (M45 = -beta_th L) or Peltier (M54) is present,
and it survives every value of e31, e33, e15 and p3. The two entries that fail the sign pattern are M45 and
M54, both even in eta where the pattern needs odd. Reason in words: the carrier density is an even field in a
row that also carries the temperature, and the temperature must be odd for the mechanical family.

With these placeholder constants the deviation from evenness at eta of order one is of relative size 1e-9,
because the Peltier loop gain is small (q*Pi_th is tiny). The deviation is exactly zero (below 1e-25) when
both coefficients are switched off. So a numerical parity test on this matrix must use an exact-zero test,
not a loose tolerance, or it will wrongly report "even" for the full model.

## Test 4. Roots, root count, and the limit l_g, l_nl -> 0

At k = 3e5, omega = 2 pi 1e8:

| l_g = l_nl | roots | degree | note |
|---|---|---|---|
| 0 | 10 | 10 | reference set |
| 1e-11 | 14 | 14 | 10 roots coincide with the reference set to 3.7e-12 relative; 4 extra roots with l_g|eta| = 1.000 and 1.045 |
| 1e-9 | 14 | 14 | same structure |
| 1e-8 | 14 | 14 | same structure |

The four extra roots are the gradient roots: their magnitude scales as 1/l_g, and the product l_g|eta| tends
to 1.000 and 1.045, the two roots of the gradient operator 1 - l_g^2 eta^2 combined with the coupling. This is
the continuity test: the ten physical roots survive the limit, the other four leave it. Verdict: PASS.

## Test 5. Null vectors and the zero of det B

At a physical root (eta = -136145.255546 + 16167.6481 i) the adjugate-column null vector gives
||M v|| / max|M| = 9.4e-102. At eta scaled by 1 + 1e-9 the normalised determinant is 5.6e-85, at 1 + 1e-6 it
is 5.6e-82, at 1.01 it is 5.8e-78 and at 1.1 it is 7.3e-77: a smooth growth away from the root, so the zero is
isolated and of the expected order.

A caution for the report: the smallest singular value of the normalised matrix is useless at these eta
(1e-48 everywhere, including far from the root), because the entries differ by so many orders that forming
M^H M loses everything. The determinant route with column scaling is the reliable one for this matrix. The
singular-value route must be restricted to the physical roots and used with row normalisation.

## Test 6. Roots against conditions

Degree 14 -> 14 partial waves -> 7 conditions per face; degree 10 -> 10 partial waves -> 5 per face. The
seven conditions are b1..b7 of the master file, and (b3), (b4) vanish identically at l_g = 0, which is
exactly the count that is lost. Consistent. 

## Not done in this round

1. Open-circuit S0 speed of the piezoelectric plate at small fd (the 5509.56 against 5509.57 check). The
   five-field matrix is available, but extracting the S0 branch at small fd requires a branch-tracking search
   over the complex k plane that was not built in this round. The physical content of the check (open circuit
   stiffens the plate) is proved analytically in Calculation H of the master file, in the closed form
   c_open^2 = (c11 + e31^2/eps33)/rho.
2. Fourier bulk damping and the Hutson-White peak: both formulas are derived in Calculation H, but the
   numerical scan against them was not run. Reason: same branch-tracking tool, plus the drift velocity is zero
   in the placeholder set, so the Hutson-White scan needs a second parameter sweep.
3. The full 14x14 boundary matrix assembly with all seven rows. The four mechanical rows are built and tested
   (Test 1). The double-traction rows are written in the master file but their numerical form needs the
   double-traction moduli mu_ijkl of the gradient theory, which are not fixed by any constant set we have.
   This is the largest open item for the paper and is flagged in the report.

## Note on the supervisor's matrix

Every entry of the 5x5 in section 3 of `03_Reduced_Equations_and_Matrix_Sumit.tex` was re-derived from the
model set and reproduced exactly, including the row where M51 = f T0 omega k beta1 and M52 = -i omega f T0
beta3 eta. No sign change is needed there. The one change we record is the parity statement of item 3 of his
section 2, above.
