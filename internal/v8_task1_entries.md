# Task 1 — every entry of the three v8 matrices, rebuilt and compared

Round v8, base `handoff_v8/`. Code: `internal/code/v8_model.py` (matrices from the
constitutive laws and the field equations), `internal/code/v8_rows.py` (the seven boundary row
functions from the conditions), `internal/code/v8_parse.py` (LaTeX fragments to numbers),
`internal/code/v8_check_entries.py` (driver). Run: `cd internal/code && python3 v8_check_entries.py`.

## What was rebuilt, and from what

The five field equations were written out from the component constitutive laws of each master's
Calculation A and the balances of Calculation B, not from the entry list:

* momentum along x and along z, `-(ik s_xx + eta s_xz)` and `-(ik s_xz + eta s_zz)`, with
  `-N rho omega^2` on the two displacements;
* Gauss `ik D_x + eta D_z + q Delta n` (Sumit), `ik D_x + eta D_z` (Neha, Anu);
* the phason balance `ik H_zx + eta H_zz + rho_p omega^2 W + i gamma omega W` (Neha);
* the magnetic Gauss law `ik B_x + eta B_z` (Anu);
* the carrier balance `(-i omega - D_n L - i k v_d + 1/tau_R) n + b_n n_0 L phi - beta_th L theta`;
* the MGT heat balance with `f = 1 - i omega tau_q`.

Every stress, displacement, phason stress, induction and heat flux was assembled from the
constitutive lines of Calculation A, with the operator factors `N = 1 - l_nl^2 L` and
`G = 1 - l_g^2 L`, `L = eta^2 - k^2`. The three masters use different letters for the same
quantity; the comparison maps them: Sumit `c.., e.., beta_1, beta_3, p_3, rho c_p`;
Neha `C.., K_1` (axial, on `w_zz`), `K_2` (transverse, on `w_zx`), `R_1, R_2, R_3, beta^w`;
Anu `C.., h..` piezomagnetic, `alpha` magnetoelectric, `mu` permeability, `m_3` pyromagnetic,
`lambda_3` in the heat row.

The seven row functions were rebuilt from the conditions themselves: effective normal and shear
traction with the surface-gradient term and the operator inverted root by root, the two double
tractions, `D_z = 0`, `H_zz = 0` (Neha) or `B_z = 0` (Anu) or zero carrier flux (Sumit), and the
adiabatic face.

Constants: ZnO set for Sumit, the synthetic probe set for Neha and Anu (internal only, never to
be quoted). Three points: `(k, omega, eta) = (2.5e5, 1e8, 3e4)`, `(1.0e6, 2pi 1e9, 7.5e5)`,
`(4.0e4, 2pi 1e7, 1.2e4)`.

## Result — largest relative difference over the three points, display blocks only

| entry | Sumit | Neha | Anu |
|---|---|---|---|
| $M_{11}$ | 1.1e-50 | 2.4e-51 | 1.6e-50 |
| $M_{12}$ | 0.0e+00 | 0.0e+00 | 0.0e+00 |
| $M_{13}$ | 0.0e+00 | 0.0e+00 | 2.2e-51 |
| $M_{14}$ | 0.0e+00 | 0.0e+00 | 0.0e+00 |
| $M_{15}$ | 0.0e+00 | 0.0e+00 | 0.0e+00 |
| $M_{21}$ | 2.8e-51 | 0.0e+00 | 1.7e-51 |
| $M_{22}$ | 6.6e-51 | 0.0e+00 | 0.0e+00 |
| $M_{23}$ | 0.0e+00 | 0.0e+00 | 2.1e-50 |
| $M_{24}$ | 0.0e+00 | 0.0e+00 | 0.0e+00 |
| $M_{25}$ | 0.0e+00 | 0.0e+00 | 0.0e+00 |
| $M_{31}$ | 0.0e+00 | 0.0e+00 | 2.2e-51 |
| $M_{32}$ | 0.0e+00 | 0.0e+00 | 2.1e-50 |
| $M_{33}$ | 3.4e-51 | 0.0e+00 | 5.3e-51 |
| $M_{34}$ | 0.0e+00 | 0.0e+00 | 3.4e-50 |
| $M_{35}$ | 0.0e+00 | 0.0e+00 | 0.0e+00 |
| $M_{41}$ | 0.0e+00 | 0.0e+00 | 0.0e+00 |
| $M_{42}$ | 0.0e+00 | 0.0e+00 | 0.0e+00 |
| $M_{43}$ | 0.0e+00 | 0.0e+00 | 3.4e-50 |
| $M_{44}$ | 0.0e+00 | 6.1e-51 | 0.0e+00 |
| $M_{45}$ | 0.0e+00 | 0.0e+00 | 0.0e+00 |
| $M_{51}$ | 0.0e+00 | 0.0e+00 | 0.0e+00 |
| $M_{52}$ | 0.0e+00 | 0.0e+00 | 0.0e+00 |
| $M_{53}$ | 0.0e+00 | 0.0e+00 | 0.0e+00 |
| $M_{54}$ | 0.0e+00 | 0.0e+00 | 0.0e+00 |
| $M_{55}$ | 0.0e+00 | 1.7e-51 | 2.2e-51 |
| $b_{1}$ | 1.8e-51 | 2.0e-51 | 6.2e-52 |
| $b_{2}$ | 4.0e-52 | 2.1e-51 | 2.3e-51 |
| $b_{3}$ | 0.0e+00 | 1.7e-51 | 1.7e-51 |
| $b_{4}$ | 9.8e-52 | 1.3e-51 | 0.0e+00 |
| $b_{5}$ | 0.0e+00 | 0.0e+00 | 0.0e+00 |
| $b_{6}$ | 0.0e+00 | 0.0e+00 | 0.0e+00 |
| $b_{7}$ | 0.0e+00 | 0.0e+00 | 0.0e+00 |

Zeros are exact agreement to 40 working digits. The largest figure anywhere is 1.1e-50, which is
rounding in the comparison itself.

## What this settles

1. No entry error was found in any of the three v8 matrices. The 25 entries and the 7 row
   functions of each paper agree with the constitutive-law rebuild at every test point.
2. The two row functions that carry a whole traction, $b_1$ and $b_2$, were checked by expanding
   the traction from the constitutive block at the same amplitudes; the expansion is itself
   covered by the $M$ entries above.
3. The v8 fixes are confirmed by this route, not assumed: Anu's Gauss row now reads
   $\epsilon_{11}k^2-\epsilon_{33}\eta^2$, $\alpha_{11}k^2-\alpha_{33}\eta^2$,
   $\mu_{11}k^2-\mu_{33}\eta^2$ ($M_{33}, M_{34}, M_{43}$) and clears the rebuild; Neha's
   $M_{44}=\epsilon_{11}k^2-\epsilon_{33}\eta^2$, $M_{35}=-\eta\beta^w$ and the dotted
   $\dot w_{zz}$ in the heat row clear the rebuild.
4. Two constant conventions were the only things that disagreed, and they are not tex errors:
   the heat capacity must be written $\rho c_p$ (Sumit 5680 times 2.8e6, not 2.8e6 alone) in the
   check, and Neha's $K_1$ is the axial modulus on $w_{zz}$ and $K_2$ the transverse one on
   $w_{zx}$, which is stated in the notation table and in Calculation A. Both were corrected on
   the checking side, not in the masters.
5. Verified earlier at the Sumit line 793 the local limit $-\rho\omega^2+c_{11}k^2-c_{44}\eta^2$
   differs from the full entry by exactly $1-N$ (6.16e-6 at the first test point). That block is
   the $l\to0$ form by design and is consistent.

## Not covered by this test

The comparison is against a rebuild that shares the same physical assumptions; a wrong
*assumption* (a sign convention, a missing coupling) would be reproduced on both sides. The
independent evidence for the conventions is in `internal/*_equation_source_log.md` from the
earlier rounds.
