# Task 3 — the closure of the nonlocal boundary problem

## (i) What the literature actually does

Two different closures are in use, and they answer different questions.

*Variational closure for a gradient solid.* A free face of a strain-gradient body carries two
conditions, not one: the effective traction vanishes and the double traction normal to the face
vanishes, `n · mu · n = 0`. Read: Charalambopoulos, Douka and Mavratzas, arXiv:1909.10776,
Sec. 2, Eq. (14), condition b(i). This is the closure the three masters use for the gradient
length, and the four double-traction rows `b_3`, `b_4` on the two faces are exactly the four
conditions the four extra roots need.

*Constitutive closure for a nonlocal differential law.* When the nonlocal law is written in
differential form, `(1 - l_nl^2 grad^2) t_ij = sigma_ij`, the step from the integral law to the
differential one is only equivalent on a bounded body if boundary conditions on the constitutive
quantities are added. Read: Barretta and Marotti de Sciarra, IJES 130 (2018) 187, Eqs. (18)-(19).
The equation numbers of Lim, Zhang and Reddy, JMPS 78 (2015) 298, Sec. 2, Eqs. (17)-(19), are
quoted as Barretta identifies them; the Lim paper itself was not opened (no full-text access),
and the masters say so in the text rather than passing the attribution through.

## (ii) Our seven rows against those two closures

| row | what it is | matches the literature? |
|---|---|---|
| b1, b2 | effective normal and shear traction, surface-gradient term included, operator inverted root by root | variational closure, family (a) |
| b3, b4 | the two double tractions `n · mu · n` on the face | variational closure, family (a) |
| b5 | `D_z = 0`, electrically open face | ours, flagged as ours |
| b6 | `H_zz = 0` (Neha), `B_z = 0` (Anu), zero carrier flux (Sumit) | ours for the thermal case; `H_zz = 0` follows the quasicrystal free-surface usage |
| b7 | adiabatic face | ours, flagged as ours |

So our set is a *subset* of family (a), with the electromagnetic, carrier and thermal rows added,
and it contains nothing of family (b). The open point in the masters is stated as: the differential
form needs constitutive boundary conditions, and we have not proved that the seven rows provide
them.

## (iii) Does family (b) bite in this formulation? A numerical answer, and the part that is missing

The question is decided by where the nonlocal operator sits. In all three v8 models `N` multiplies
only the inertial term: `M_11` and `M_22` are the only entries that contain it, and this is
confirmed by the entry comparison (`internal/v8_task1_entries.md`, all entries agree). The
consequence is visible in the degree count:

| | degree of det M |
|---|---|
| l_g > 0, l_nl > 0 | 14 |
| l_g = 0 | 10 |
| l_nl = 0 | 14 |

The nonlocal length adds no root, so it adds no boundary condition to satisfy; the gradient length
adds four roots, and the four double-traction rows close them. In this formulation the constitutive
boundary conditions of family (b) therefore have nothing to act on, *provided* one accepts that
`N` may be carried on the inertia. That acceptance is a modelling choice and should be written
down as one.

What is missing is the number. To compare the two closures one builds the alternative B with rows
`b_3`, `b_4` replaced by the constitutive conditions (for example a vanishing normal derivative of
the two normal strains, the form used for rods in family (b)), and tracks the lowest branch at
`l/h = 0.05, 0.1, 0.2`. That needs the fourteen-root assembly to work, and it does not: at every
speed tried the assembled B is numerically singular (equilibrated determinant of order 1e-160 at
40 digits, `internal/v8_task2_tests.md`, item (e)), while the same code assembles the elastic 4 x 4
case to 1e-59. No verdict on the size of the change is given, because any number produced that way
would be noise. The item is open, and the report says so.

## (iv) Proposed wording — to propose, not to impose

The paragraph "An open point about the closure of the model" now stands at the head of
Calculation F in all three masters. It is correct and it is long. A shorter wording that says the
same thing and adds the degree argument:

> The differential form `(1 - l_nl^2 grad^2) t = sigma` is equivalent to the nonlocal integral law
> on a bounded body only if constitutive boundary conditions are added (Barretta and Marotti de
> Sciarra, IJES 130 (2018) 187, Eqs. (18)-(19)). In the form used here the nonlocal operator
> multiplies the inertial term, so it adds no root to the characteristic polynomial and calls for
> no extra condition; the length that does add roots is the gradient length, four of them, and they
> are closed by the two double tractions on each face. The seven rows are therefore a modelling
> choice of ours in the sense that they close the gradient part variationally and leave the
> nonlocal part to the inertia. Until the alternative closure is computed, `det B = 0` belongs to
> this boundary-value problem and to no other.

The scholar should decide whether to adopt this wording, and if the nonlocal operator is later moved
to the stress, the paragraph has to be rewritten and the constitutive conditions added.

## Sources read for this section

* Barretta and Marotti de Sciarra, *Int. J. Eng. Sci.* **130** (2018) 187, Eqs. (18)-(19).
* Charalambopoulos, Douka and Mavratzas, arXiv:1909.10776, Sec. 2, Eq. (14), condition b(i).
* Lim, Zhang and Reddy, *J. Mech. Phys. Solids* **78** (2015) 298, Sec. 2, Eqs. (17)-(19) —
  **not opened**; quoted only as Barretta identifies them, and the masters say so.
