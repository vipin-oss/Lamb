# Paper C (Anu): numerical verification of the matrix route

Internal only; nothing here goes into `Lamb_Anu.tex`.

Code: `internal/code/core.py` (`M_anu`, `coeffs_scaled`, `roots_eta`, `parity_matrix`), driver
`internal/code/t_neha_anu.py`. mpmath at 60 digits.

Placeholder constants (internal only; order-of-magnitude values for a BaTiO3/CoFe2O4 composite, not measured
values and not used in the paper): c11 226, c13 112, c33 216, c44 44 GPa; e31 -2.2, e33 9.3, e15 5.8 C/m^2;
q31 290, q33 350, q15 190 N/(A m); eps11 5.64e-9, eps33 6.35e-9 F/m; mu11 2.97e-4, mu33 1.57e-4 H/m;
alpha11 1.6e-9, alpha33 2.7e-9 s/m; beta1 beta3 3.1e5 Pa/K; p3 -1e-5 C/(m^2 K); lambda3 2e-3 T/K;
rho 5730 kg/m^3; l_g = l_nl = 1e-8 m; T0 300 K; rho c_p 2.5e6 J/(m^3 K); k_th 6 W/(m K); tau_q 1e-11 s.

## Test 1. Degree of det M(eta)

Same method as Paper B, checked at fd = 1e6, 1e8, 1e10 rad/s.

| l_g | degree at all three frequencies | expected | verdict |
|---|---|---|---|
| 0 | 10 | 10 | PASS |
| 1e-8 | 14 | 14 | PASS |

The magnetic Gauss row is second order, like the electric one, so it adds no root.

## Test 2. Parity in eta

| case | sign vectors | reading |
|---|---|---|
| all couplings on | (-1,+1,+1,+1,-1) and its negative | det M even, S/A split exists |
| p3 = lambda3 = alpha11 = alpha33 = 0 | same two | split exists |

**Result.** This plate always splits into symmetric and antisymmetric families, whatever the couplings. The
magnetoelectric coefficient, the pyroelectric constant and the pyromagnetic constant all sit in the two Gauss
rows and the heat row as even entries, which is exactly what the sign vector needs. The odd fields are the
displacement along the plate and the temperature; the even fields are the displacement across it, the
electric potential and the magnetic potential.

Consequence: the 14x14 boundary matrix factorises into two 7x7 blocks, and the same holds at l_g = 0 with
two 5x5 blocks.

## Test 3. Roots and the limit l_g -> 0

l_g = 0: 10 roots, degree 10. l_g = 1e-8: 14 roots, of which 4 are gradient roots. Same structure as Papers
A and B. Verdict: PASS.

## Test 4. Null vector

At the root of smallest |eta|: ||M v|| / max|M| = 7.1e-71. Verdict: PASS.

## Test 5. Number of roots against number of conditions

14 roots, 7 conditions per face (b1..b7: two tractions with surface gradient, two double tractions, electric,
magnetic, thermal). 10 roots and 5 conditions at l_g = 0. Consistent.

## Analytic results that were checked on paper, not numerically

1. Thin-plate modulus
   cbar11 = c11 + (e31^2 mu33 - 2 e31 q31 alpha33 + q31^2 eps33)/(eps33 mu33 - alpha33^2).
   Units check out (Pa). It reduces to the piezoelectric plate value c11 + e31^2/eps33 when q31 = alpha33 = 0
   and to the piezomagnetic value c11 + q31^2/mu33 when e31 = alpha33 = 0. Both limits are the right ones.
2. Field ratio H_z/E_z = (alpha33 e31 - q31 eps33)/(alpha33 q31 - e31 mu33), unit A/V (siemens). It vanishes
   with alpha33, as it must.
3. The volume-fraction limits of the two homogenisation schemes: the rule of mixtures returns the pure phases
   at v = 0 and v = 1 and gives alpha = 0 everywhere. Scheme two gives the product form and vanishes at both
   ends.

## Not done in this round

1. The numerical check of the thin-plate modulus and of the field ratio against the full matrix at small fd.
   Needs the branch tracking tool, as in Papers A and B.
2. The 14x14 boundary assembly: the double-traction moduli of the gradient theory are not fixed by any
   constant set we have. This is the largest open item.
3. The published product formula for the effective magnetoelectric coefficient was not located; the master
   file says so in the text and asks the scholar to replace it with a cited formula.
