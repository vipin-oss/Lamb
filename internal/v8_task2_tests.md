# Task 2 — dispersion tests, round v8

Code: `internal/code/v8_disp.py` (elastic limit), `internal/code/v8_checks.py` (structure),
`internal/code/v8_b.py` and `internal/code/v8_task23.py` (B assembly). Runs are logged in the
files named at the end of each section.

## (a) Couplings off, l_g = l_nl = 0 — Rayleigh–Lamb, both families. PASS

Aluminium: E = 70 GPa, nu = 0.33, rho = 2700, h = 1e-3 so 2h = 2e-3, fd = f·2h.

| quantity | computed | reference | difference |
|---|---|---|---|
| c_L | 6197.8243 m/s | 6197.82 | 7e-6 relative |
| c_T | 3121.9527 m/s | 3121.95 | 9e-7 relative |
| c_R | 2909.7314 m/s | 2909.7 | 1.1e-5 relative |

Mode speeds from the roots of the secular equation, and the assembled determinant evaluated at
each of them:

| fd (Hz m) | S0 (m/s) | |det B|/||B||^4 | A0 (m/s) | |det B|/||B||^4 |
|---|---|---|---|---|
| 10 | 5393.9053 | 7.8e-63 | 311.6377 | 1.2e-62 |
| 100 | 5393.1719 | 6.6e-61 | 954.2341 | 5.1e-61 |
| 1000 | 5308.5887 | 1.6e-59 | 2326.6431 | 7.5e-60 |

Largest residual 1.6e-59 against a tolerance of 1e-5. The same three A0 speeds were also found by
an independent speed scan of the determinant before the refinement (311.638, 954.234, 2326.643),
so the two routes agree.

Note on the route: the elastic limit is checked with the two-amplitude block and its 4 x 4 B
(two tractions on two faces). With the couplings switched off inside the five-amplitude model the
characteristic polynomial loses degrees (the auxiliary rows become constants) and the count of
roots no longer matches seven conditions per face, so that model cannot serve as the elastic
benchmark. This is a property of the coupled system, not an error in the masters.

## (d) Parity with physical constants, each paper. PASS

Entrywise test, every sign vector s with M(-eta) = diag(s) M(eta) diag(s), at eta = 1.13 k,
k = 3e5, omega = 2 pi 1e8.

| paper | all couplings on | what the paper claims |
|---|---|---|
| Sumit | no sign vector | odd powers iff beta_th, Pi_th or E_g non-zero |
| Sumit, beta_th = Pi_th = E_g = 0 | (1,-1,-1,-1,1) and its negative | exactly the claimed vector |
| Sumit, beta_th = Pi_th = 0, E_g kept | no sign vector | E_g alone breaks it |
| Neha | (1,-1,-1,-1,1) and its negative | always, S/A factorisation |
| Anu | (1,-1,-1,-1,1) and its negative | always, S/A factorisation |

The third row is the v8 wording check: the paragraph in Sumit says the parity holds "for generic
values of the other constants, exactly when beta_th = Pi_th = E_g = 0", and the computation
confirms that keeping E_g alone is enough to destroy the sign vector. The earlier wording, which
mentioned only beta_th and Pi_th, was too weak; the v8 text is right.

## Degree, root census, null vectors, l to 0. PASS

k = 3e5, omega = 2 pi 1e8, dps 40.

| paper | degree, l_g > 0 | l_g = 0 | l_nl = 0 | roots found |
|---|---|---|---|---|
| Sumit | 14 | 10 | 14 | 14 |
| Neha | 14 | 10 | 14 | 14 |
| Anu | 14 | 10 | 14 | 14 |

* Roots of the gradient factor, |eta| l_g: Sumit 1.000, 1.000, 1.045, 1.045; Neha 1.000, 1.000,
  1.039, 1.039; Anu 1.000, 1.000, 1.033, 1.033. Four extra roots each, as the degree count says.
* Null-vector residuals of the first three roots: 5.1e-71, 5.1e-71, 2.8e-72 (Sumit);
  1.9e-49, 2.0e-49, 3.4e-57 (Neha); 2.9e-61, 3.6e-61, 2.6e-59 (Anu). All fourteen roots have a
  one-dimensional null space: the largest minor of the adjugate stays above 2e-45 of ||M||^4 at
  every root, so the "largest column of the adjugate" rule is safe here and no null-space basis is
  needed.
* l to 0: the ten local roots against the same roots at l_g = l_nl = 1e-11, largest relative
  shift 1.3e-10 (Sumit), 1.4e-12 (Neha), 6.5e-13 (Anu). The figure is the same at dps 40 and 70,
  so it is the physical small-length shift, not root-finder noise.

## Not done in this round

* **(b) one coupling at a time.** The open-circuit thin-plate speed, the Fourier bulk damping
  k_i/k_r = (Delta_E/2) omega tau/(1+(omega tau)^2), the Hutson–White peak at
  n_0 = epsilon omega/(q b_n), the phason wave-like and diffusive limits and the magnetoelectric
  limits were not recomputed against the v8 entries. The earlier round's numbers are in
  `internal/*_benchmarks.md` and were produced from the v7 entries; the v8 entries agree with the
  rebuild entry by entry, so those numbers are not contradicted, but they are not re-run here.
* **(c) direction of the shifts at mode level.** Not done: it needs a mode, and the mode needs a
  working B.
* **(e) roots against rows of B, singular-value route against determinant route.** The root count
  (14 or 10) is confirmed. The 14 x 14 assembly of Calculation G was built
  (`internal/code/v8_b.py`: all fourteen roots, one null vector each, column scaling
  exp(-|Re eta| h)) and it is numerically singular at every speed tried: after row and column
  equilibration the determinant is of order 1e-160 at 40 digits, i.e. below the noise floor, at
  speeds from 500 to 5500 m/s for l/h = 0.05, 0.1 and 0.2. No mode can be tracked until that is
  understood, so no dispersion curve from the full model is reported. The same code assembles the
  4 x 4 elastic B exactly (1e-59 above), so the fault is in the fourteen-root assembly, not in the
  determinant routine. This is the one open item of Task 2 and it blocks the numerical part of
  Task 3.

## Logs

`/tmp/checks_v8.txt` (structure), `/tmp/entries_v8.txt` (entries), the json files
`internal/v8_*_entries.json`.

# Task 2 redo — full ten-row B, singular-value scan, 30 October 2026

The earlier "the fourteen-row assembly is singular at every speed" was a test-regime error.
Those runs used the default lengths with `h = 1e-3`, i.e. `l/h = 2e-5`, where four roots sit at
`|Re eta| h` of order `1e3` to `1e5`; their columns are one-sided and the equilibrated determinant
loses the level. With `l/h = 0.05 ... 0.2` the same code behaves differently, and the ten-row
matrix is clean.

## (e) Roots of det B are the zeros of the assembled B — full five-field ten-row system. PASS

Method: `internal/code/v8_scan.py` (assembly, equilibration, singular values) and
`internal/code/v8_run.py` (dip scan on the equilibrated determinant). All couplings off, both
lengths zero, isotropic aluminium constants in every paper, `h = 1e-3`, `fd = f 2h`, speeds
scanned 200 to 7000 m/s in steps of 50 to 100 and every dip refined. Five conditions per face
(normal traction, shear traction, `D_z = 0`, carrier flux or `H_zz` or `B_z`, adiabatic).

| paper | fd = 10 | fd = 100 | fd = 1000 |
|---|---|---|---|
| Sumit | 5393.9 (S0) | 954.2 (A0) | 5308.6 (S0) |
| Neha | 311.6 (A0), 5393.9 (S0) | 5393.2 (S0) | - |
| Anu | 311.6 (A0), 5393.9 (S0) | 5393.2 (S0) | - |

These are the Rayleigh–Lamb speeds of `v8_disp.py` to all four figures, so the assembled B and the
row functions agree with the elastic benchmark through a second route, not only through the
four-row block. Neha and Anu also show a dip at 6197.8 m/s, which is `c_L`: at `k = omega/c_L` a
bulk root passes through `eta = 0` and the determinant has a degenerate zero there. That dip is not
a plate mode and should not be counted.

## The fourteen-row system with l_g > 0: still not resolved

What was tried at `l/h = 0.05, 0.1, 0.2` with all five fields coupled, working precision 60
digits, four passes of row and column equilibration:

* smallest singular value of the equilibrated matrix: of order `1e-15` at every speed, i.e. the
  matrix carries a near-null direction that does not move with the speed;
* equilibrated determinant: level between `1e-84` and `1e-91`, wandering smoothly with the speed,
  with no reproducible dip. One excursion to `1e-83` at 3200 m/s appeared before the one-sided
  columns were set to zero and disappeared afterwards, so it was noise;
* the four strongly evanescent roots (`|Re eta| h > 30`) zeroed on the far face, so that each is
  attached to the face it decays from;
* the alternative closure of Task 3 in place of the two double-traction rows.

A search of 3100 to 3450 m/s in steps of 10 found no minimum below the local level for the
variational rows; a minimum at 3486 m/s with level `1e-38` was found for the constitutive rows at
`l/h = 0.1` and `0.2`, but with the variational rows behaving as above that figure cannot yet be
called a mode.

Diagnosis so far: the ten-row case of the same code is exact and well conditioned, so the fault is
in how the fourteen roots enter, not in the determinant, the equilibration or the precision. The
next step is to compare row by row with the reviewer's working matrix at `h = 5e-4`, `fd = 3000`,
`c = 3000`, `l = 5e-6`, where they report an equilibrated smallest singular value of 0.018 while
this code gives `2.2e-16` for a matrix that is entry-for-entry the same as `v8_task23.detB`
(checked: `max |B1 - B2| / scale = 0`). Since the two matrices agree and the singular values do
not, the difference must be in the equilibration or in which rows are used, and that is worth one
exchange before more compute.
