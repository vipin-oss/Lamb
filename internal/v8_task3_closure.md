# Task 3 — the closure of the nonlocal boundary problem (revised, 30 October 2026)

The earlier verdict in this file — that the constitutive boundary conditions "have nothing to act
on" in these models — is withdrawn. It rested on the observation that `N` appears only in `M_11`
and `M_22`, and on the degree count. That observation is true and the degree count is right, but
the conclusion does not follow, for the reason given in item (iii) below.

## (i) What the literature requires

Two closures are in use, and they answer different questions.

*Variational closure for a gradient solid.* A free face carries the effective traction and the
double traction normal to the face. Read: Charalambopoulos, Douka and Mavratzas,
arXiv:1909.10776, Sec. 2, Eq. (14), condition b(i). This is what closes the four extra roots that
the gradient length produces, and the four double-traction rows `b_3`, `b_4` on the two faces are
those four conditions.

*Constitutive closure for a nonlocal differential law.* The differential form
`(1 - l_nl^2 grad^2) t_ij = sigma_ij` carries homogeneous solutions `t_ij ∝ exp(±z/l_nl)`. The step
from the nonlocal integral law to the differential one is equivalent on a bounded body only if
boundary conditions on the constitutive quantities are added, and those conditions are what fixes
the homogeneous solutions. Read: Barretta and Marotti de Sciarra, IJES 130 (2018) 187,
Eqs. (18)–(19). The equation numbers of Lim, Zhang and Reddy, JMPS 78 (2015) 298, Sec. 2,
Eqs. (17)–(19), are quoted as Barretta identifies them; the Lim paper itself was not opened, and
the three masters say so in their own text.

## (ii) Our seven rows against those closures

| row | what it is | family |
|---|---|---|
| b1, b2 | effective normal and shear traction, surface-gradient term included | (a) variational |
| b3, b4 | the two double tractions `n · mu · n` | (a) variational |
| b5 | `D_z = 0`, electrically open face | ours |
| b6 | `H_zz = 0` (Neha), `B_z = 0` (Anu), zero carrier flux (Sumit) | ours |
| b7 | adiabatic face | ours |

Nothing in the set belongs to family (b).

## (iii) Why the earlier argument was wrong

Our partial-wave basis is `exp(eta_m z)` with `eta_m` the roots of `det M(eta) = 0`. The nonlocal
operator enters the matrix as a factor `N(eta) = 1 - l_nl^2(k^2 - eta^2)` multiplying the inertial
term, and dividing the two momentum equations by `N` moves it to the stiffness. Either way, `N`
never becomes a factor of the determinant, so `eta = ±1/l_nl` is not a root, and the homogeneous
solutions `t ∝ exp(±z/l_nl)` are **not in our solution space at all**. The degree count (14 with
`l_g ≠ 0`, 10 without, unaffected by `l_nl`) measures exactly this: the nonlocal length adds no
partial wave.

That is the point. Absence of those solutions is not innocuous: the differential law has them, and
a displacement-form ansatz that omits them is equivalent to setting their amplitudes to zero at both
faces. Whether that is legitimate is precisely the equivalence question, and it is not settled by
the degree count. The seven rows close the gradient part and the electromagnetic, carrier and
thermal part; they do not address the nonlocal homogeneous solutions, because the ansatz excludes
them.

So the honest statement is: our rows define *a* boundary-value problem, whose dispersion relation is
`det B = 0`; they are not shown to be equivalent to the integral law on `[-h, h]`. The literature's
constitutive conditions (family b) are the missing ingredient, and adopting them means enlarging the
ansatz by the two additional functions `exp(±z/l_nl)`, i.e. going from fourteen to sixteen partial
waves with two extra conditions per face.

## (iv) The alternative closure on the lowest branch, fully coupled

Why the earlier run gave nothing. With `l_nl = l_g` the two length operators coincide,
`N(eta) = G(eta)`, the elastic block of `M` becomes `G` times the classical block, and at the four
gradient roots `G = 0` so `N = 0` and the traction rows degenerate. That is where the equilibrated
singular values of `1e-18` at every speed came from: the configuration, not the closure. Runs with
`l_nl = 0.5 l_g` and `l_nl = 2 l_g` are well conditioned, with median singular values of order
`1e-2` to `1e-1` and dips of depth 87 to 420.

Set-up: Sumit paper, fully coupled, `h = 5e-4` m, `fd = 1000`, seven rows per face against the
constitutive rows in the same two slots, A0 window scanned at 5 m/s and refined by a parabola.
Elastic A0 for reference is 2326.6 m/s. Values in m/s.

| l_g/h | l_nl/l_g | seven rows | alternative closure | coupled l=0 baseline |
|---|---|---|---|---|
| 0.05 | 0.5 | 2193.2 | 2211.5 | 2181.9 |
| 0.05 | 2 | 2175.8 | 2170.8 | 2181.9 |
| 0.10 | 0.5 | 2220.2 | 2195.3 | 2181.9 |
| 0.10 | 2 | 2154.4 | 2128.4 | 2181.9 |
| 0.20 | 0.5 | 2300.7 | no reproducible branch | 2181.9 |
| 0.20 | 2 | 1825 | 1825 | 2181.9 |

The baseline of the last column is the same model with both lengths switched off, all couplings
on: A0 = 2181.9 m/s at `fd = 1000` (943.5 m/s at `fd = 100`). It is not 2326.6, which is the elastic
value without the piezoelectric and carrier couplings; comparing against that would have shown a
false softening of 6 per cent from the lengths alone.

The `l = 1e-8` route to the same baseline is not usable: at `l/h = 2e-5` the equilibrated singular
value is of order `1e-17` at every speed and even turns negative in the fourth digit, which is the
same near-degenerate column pair as before. The ten-row system with the lengths set to zero is the
baseline, and it is clean.

Reading against the coupled baseline: the pair of lengths moves the branch from -2.6 per cent
(2154.4 at `l_g/h = 0.1`, `l_nl = 2 l_g`) to +5.4 per cent (2300.7 at `0.2`, `0.5`), so neither
length dominates across the range and the sign of the size effect depends on the ratio
`l_nl/l_g`. Where both closures give a dip in the same window the alternative moves the branch by
at most 26 m/s, 1.1 per cent, with no systematic sign. The closure therefore does not decide the
numbers; it does decide what we may claim, and the masters still need the paragraph that says so.

Two things are worth flagging rather than hiding.

1. The sign of the size effect follows the ratio. At `l_nl = 0.5 l_g` the pair sits above the
   coupled baseline at all three lengths, 2193.2, 2220.2 and 2300.7 against 2181.9, i.e. the
   gradient length wins. At `l_nl = 2 l_g` it sits below at the first two, 2175.8 and 2154.4, and
   well below at the third, 1825, i.e. the nonlocal length wins. So stiffening is reported only when
   `l_nl < l_g`, and the papers must say which ratio they are using.

2. The `l_g/h = 0.2, l_nl = 0.5 l_g` alternative-closure entry was re-run over the whole band
   `800` to `2600` m/s in steps of 25. It shows five shallow minima (950, 1100, 1175, 1225, 1975
   m/s, the deepest `8.3e-4` against a median of `2.6e-2`) and no clean branch, where the same
   configuration with our seven rows gives a single dip at 2300.7 with depth 87. A closure that
   fragments the spectrum is not credible as it stands, so the entry stays held; the likely cause
   is still the near-degenerate column pair, now inside one of the two alternative row sets at the
   larger length.

## (v) Proposed wording — to propose, not to impose

> The differential form `(1 - l_nl^2 grad^2) t = sigma` is equivalent to the nonlocal integral law
> on a bounded body only if constitutive boundary conditions are added (Barretta and Marotti de
> Sciarra, IJES 130 (2018) 187, Eqs. (18)–(19)). In the form used here the nonlocal operator is
> carried on the inertial term, so it brings no partial wave of its own: the homogeneous solutions
> `t ∝ exp(±z/l_nl)` that the differential law admits are not in the expansion, which amounts to
> setting their amplitudes to zero at both faces. The gradient length does bring partial waves, four
> of them, and they are closed by the two double tractions on each face. The seven rows are
> therefore a modelling choice of ours: they close the gradient part variationally and exclude the
> nonlocal homogeneous solutions by construction. Replacing the two double tractions by the
> constitutive conditions moves the lowest branch by at most 1.1 per cent over the lengths
> `l/h = 0.05` to `0.2`, so `det B = 0` belongs to this boundary-value problem and to no other.

## Sources read for this section

* Barretta and Marotti de Sciarra, *Int. J. Eng. Sci.* **130** (2018) 187, Eqs. (18)–(19).
* Charalambopoulos, Douka and Mavratzas, arXiv:1909.10776, Sec. 2, Eq. (14), condition b(i).
* Lim, Zhang and Reddy, *J. Mech. Phys. Solids* **78** (2015) 298, Sec. 2, Eqs. (17)–(19) —
  **not opened**; quoted only as Barretta identifies them.
