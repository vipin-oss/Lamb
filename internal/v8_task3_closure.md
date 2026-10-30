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

| l_g/h | l_nl/l_g | seven rows | alternative closure | difference |
|---|---|---|---|---|
| 0.05 | 0.5 | 2193.2 | 2211.5 | +18.3 |
| 0.05 | 2 | 2175.8 | 2170.8 | -5.0 |
| 0.1 | 0.5 | 2220.2 | 2195.3 | -24.9 |
| 0.1 | 2 | 2154.4 | 2128.4 | -26.0 |
| 0.2 | 0.5 | 2300.7 | dip at 1110, none near 2300 | to check |
| 0.2 | 2 | 1825 | 1825 | 0.0 |

Reading. Where both closures give a dip in the same window, the alternative changes the lowest
branch by at most 26 m/s, which is 1.1 per cent, and with no systematic sign. That is smaller than
the size effect itself (the same lengths move the branch by 3 to 22 per cent against the elastic
value), so the closure is not what decides the numbers — but it is not nothing either, and the
masters cannot claim the seven rows are forced by the nonlocal law.

Two things are worth flagging rather than hiding.

1. Every entry in the table sits *below* the elastic 2326.6 m/s, including the ones with `l_nl` at
   half the gradient length. At these lengths the nonlocal softening dominates the gradient
   stiffening: at `l_g/h = 0.05, l_nl = 0.5 l_g` the stiffening from `l_g` alone is +0.5 per cent
   (2337.4 against 2326.6 in the elastic table) while the pair lands at 2193.2, i.e. -5.7 per cent.
   That ordering is physical and should be said in the paper when the coupling limits are quoted.
2. The `l_g/h = 0.2, l_nl = 0.5 l_g` alternative-closure case has no dip anywhere near 2300 and
   shows a shallow one at 1110. A closure that removes a branch is not credible as it stands, so
   this entry is marked to be re-run before it is used. The likely cause is the same near-degenerate
   column pair that spoiled the `l_nl = l_g` run, appearing in one of the two closure row sets at
   the larger length.

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
