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

## (iv) The alternative closure on the lowest branch at l/h = 0.05, 0.1, 0.2

Set-up. Two rows of the seven per face are replaced by the constitutive conditions of family (b),
written component-wise for the two normal strains of the plane-strain plate:
`d(eps_zz)/dz = s eps_zz / l_nl` and `d(eps_xz)/dz = s eps_xz / l_nl`, with `s = +1` at `z = +h`
and `s = -1` at `z = -h`. That is an instantiation of the literature form for the two strains this
plate carries, not a quotation of a numbered equation, and it is labelled so in the code
(`internal/code/v8_scan.py`, `const_rows`).

Status of the numbers. They are **not reportable yet**. The fourteen-row assembly does not give a
reproducible dip structure at these lengths: with the variational rows the equilibrated
determinant sits between `1e-84` and `1e-91` and a search of 3100 to 3450 m/s in steps of 10 finds
no minimum; with the constitutive rows one minimum appears at 3486 m/s with level `1e-38` at
`l/h = 0.1` and `0.2`, but against the behaviour of the variational rows that single figure cannot
be called a mode. The ten-row assembly of the same code is exact — it reproduces the Rayleigh–Lamb
speeds of all three papers to four figures (`internal/v8_task2_tests.md`, redo section) — so the
fault is in how the fourteen roots enter, and it is being chased. One number, flagged as
unconfirmed, is all that exists: the constitutive closure moves the lowest branch from 3199.6 m/s
(the `l = 0`, variational value) to about 3486 m/s at `l/h = 0.1`.

Verdict in one line for the report: the closure question is real and the constitutive conditions
change the lowest branch once the extra pair of homogeneous solutions is admitted; the size of the
change is not yet established, and the masters should say so rather than implying the seven rows are
sufficient.

## (v) Proposed wording — to propose, not to impose

> The differential form `(1 - l_nl^2 grad^2) t = sigma` is equivalent to the nonlocal integral law
> on a bounded body only if constitutive boundary conditions are added (Barretta and Marotti de
> Sciarra, IJES 130 (2018) 187, Eqs. (18)–(19)). In the form used here the nonlocal operator is
> carried on the inertial term, so it brings no partial wave of its own: the homogeneous solutions
> `t ∝ exp(±z/l_nl)` that the differential law admits are not in the expansion, which amounts to
> setting their amplitudes to zero at both faces. The gradient length does bring partial waves, four
> of them, and they are closed by the two double tractions on each face. The seven rows are
> therefore a modelling choice of ours: they close the gradient part variationally and exclude the
> nonlocal homogeneous solutions by construction. Until the constitutive closure is computed,
> `det B = 0` belongs to this boundary-value problem and to no other.

## Sources read for this section

* Barretta and Marotti de Sciarra, *Int. J. Eng. Sci.* **130** (2018) 187, Eqs. (18)–(19).
* Charalambopoulos, Douka and Mavratzas, arXiv:1909.10776, Sec. 2, Eq. (14), condition b(i).
* Lim, Zhang and Reddy, *J. Mech. Phys. Solids* **78** (2015) 298, Sec. 2, Eqs. (17)–(19) —
  **not opened**; quoted only as Barretta identifies them.
