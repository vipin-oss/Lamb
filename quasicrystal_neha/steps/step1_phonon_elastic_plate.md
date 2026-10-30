# Step 1 (Neha) — Phonon-only elastic plate: the calibration every later step must return to

**This page adds only the material-specific notes to Sumit's pack.** Read
`../../semiconductor_sumit/steps/step1_elastic_rayleigh_lamb.md` first: it contains the governing
equations, the potentials, the stress table, the S/A determinants (5S)/(5A), the
non-dimensionalisation, the eight limiting-case checks with numbers, the parameter table and the
numerical warnings (including the spurious `c = c_T` root of the undivided determinant). All of that
applies verbatim. What follows is what differs for Paper B.

Conventions unchanged: `exp[i(kx−ωt)]`, thickness `2h`, faces `z = ±h`, plane strain, `k = k_r + ik_i`,
`k_i > 0` decays along `+x`, `fd = f·2h` in Hz·m.

## 1. Axes and field list at this step

- **Quasiperiodic axis: along the thickness `z`.** **Poling axis: along `z`.** Both fixed here so
  that no later step has to reopen the geometry.
- **Fields present at Step 1: phonon displacement only, `u_x(x,z,t)`, `u_z(x,z,t)`.**
- **Fields deliberately absent:** phason `w` (Step 3), electric potential `φ` (Step 2), temperature
  `θ` (Step 4). Nothing about them may appear in this step's code or figures.

## 2. Two checks, in this order

**(a) Isotropic calibration against `common/`.** Use aluminium `E = 70 GPa, ν = 0.33, ρ = 2700`, run
the eight checks of Sumit's §5, and match the CSV at `fd = 500, 1000, 2000, 3000, 5000` Hz·m for
S0, A0, S1, A1 to rel. < 1e-4, with `k_imag ≡ 0` written as zeros. The Rayleigh value is
**2909.7 m/s** (exact root; tolerance 1e-3 relative) — **not** the Viktorov approximation 2906.5,
which is 0.11% low and would fail. This check answers only "is the solver right?".

**(b) Transversely isotropic phonon-only baseline — this is the check that matters for Paper B.**
A 1D hexagonal quasicrystal has a transversely isotropic **phonon** stiffness with the sixfold axis
along `z`: independent constants `C_11, C_12, C_13, C_33, C_44`. In plane strain (`x–z`) this
replaces the two isotropic Lamé constants by **four** constants, so the single pair `p, q` of
Sumit's §1 **no longer exists**:

> The potentials still separate, but the two vertical wavenumbers `p` and `q` are now the two roots
> of a **quadratic** arising from the Christoffel-type condition for the `(u_x, u_z)` system, not
> from `p² = ω²/c_L² − k²` and `q² = ω²/c_T² − k²`. Derive that quadratic; do **not** copy the
> isotropic formulae. Same for the stresses: `σ_zz = C_13 u_x,x + C_33 u_z,z`,
> `σ_xz = C_44 (u_x,z + u_z,x)`.

Two consequences to state in the check file: (i) the S/A split survives (the geometry and the
material are symmetric about `z = 0`), and (ii) the `c_L`-type cutoff `S1 = c_L/2` is replaced by
`√(C_33/ρ)/2`, while the shear cutoff `A1 = √(C_44/ρ)/2` is unchanged in form. Report both numbers.

**The decisive test of (b):** set `C_11 = C_33 = λ + 2μ`, `C_12 = C_13 = λ`, `C_44 = μ` with the
aluminium `λ, μ`; the transversely isotropic code must then reproduce the isotropic CSV of (a) to
rel. < 1e-6. If it does not, the quadratic or the stress expressions are wrong — fix that before
Step 2, because every later step inherits it.

Material constants come from the reference set of *Acta Mech.* **232** (2021) 135–151,
doi:10.1007/s00707-020-02811-7, transcribed into `params.md` with the source page — **I have not
verified those numbers**, so they must be entered by the scholar from the paper itself, not from
this note.

## 3. What must not be done yet

No phason, no electric field, no temperature, no size effect. No NSGT: at this step the phonon
stress is classical (the gate ruling — NSGT enters at Step 5 on the phonon stress only, and the
phason-gradient variant is a Step-5 sensitivity only, never part of the base model).

## 4. Deliverables and exit criteria

Send: (i) the hand derivation of the transversely isotropic quadratic and the four stress
expressions; (ii) the `c` vs `fd` plot for both (a) and (b) on one figure, S/A families labelled;
(iii) the CSV at the five fixed `fd` for S0, A0, S1, A1 with `k_imag` zeros; (iv) the isotropic
degeneracy test of §2(b) with its relative difference. Step 1 passes when (a) matches to 1e-4, (b)
reduces to (a) to 1e-6, and both root counts agree with the Arena cross-check.
