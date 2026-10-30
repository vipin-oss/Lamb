# Step 1 (Anu) — Phonon-only elastic plate: the calibration every later step must return to

**This page adds only the material-specific notes to Sumit's pack.** Read
`../../semiconductor_sumit/steps/step1_elastic_rayleigh_lamb.md` first: governing equations,
potentials, stress table, the S/A determinants (5S)/(5A), the non-dimensionalisation, the eight
limiting-case checks with numbers, the parameter table and the numerical warnings (including the
spurious `c = c_T` root of the undivided determinant) all apply verbatim. What follows is what
differs for Paper C.

Conventions unchanged: `exp[i(kx−ωt)]`, thickness `2h`, faces `z = ±h`, plane strain, `k = k_r + ik_i`,
`k_i > 0` decays along `+x`, `fd = f·2h` in Hz·m.

## 1. Axes and field list at this step

- **Poling axis: along the thickness `z`** (the conventional choice; it also decides the sign
  convention for `e` and `q` in Step 2–3, so fix it now and write it in the README).
- **Fields present at Step 1: phonon displacement only, `u_x(x,z,t)`, `u_z(x,z,t)`.**
- **Fields deliberately absent:** electric potential `φ` and magnetic potential `ψ` (Step 2–3),
  temperature `θ` (Step 4). No piezoelectric, piezomagnetic or magnetoelectric constant may appear
  in this step's code or figures — not even with a zero value, because a zero coefficient hides a
  sign error until Step 3.

## 2. Two checks, in this order

**(a) Isotropic calibration against `common/`.** Aluminium `E = 70 GPa, ν = 0.33, ρ = 2700`; run the
eight checks of Sumit's §5 and match the CSV at `fd = 500, 1000, 2000, 3000, 5000` Hz·m for S0, A0,
S1, A1 to rel. < 1e-4, with `k_imag ≡ 0` written as zeros. The Rayleigh value is **2909.7 m/s**
(exact root, tolerance 1e-3) — **not** the Viktorov approximation 2906.5, which is 0.11% low.

**(b) Transversely isotropic phonon-only baseline — the check that matters for Paper C.** The
homogenised BaTiO₃/CoFe₂O₄ composite is transversely isotropic (6mm) with the six-fold axis along
`z`, so the **phonon** part has independent constants `C_11, C_12, C_13, C_33, C_44`. In plane strain
this replaces the two isotropic Lamé constants by four, and the single pair `p, q` of Sumit's §1
**no longer exists**:

> `p` and `q` become the two roots of a **quadratic** from the Christoffel-type condition for the
> `(u_x, u_z)` system, not `p² = ω²/c_L² − k²`, `q² = ω²/c_T² − k²`. Derive the quadratic; do not
> copy the isotropic formulae. Stresses: `σ_zz = C_13 u_x,x + C_33 u_z,z`,
> `σ_xz = C_44 (u_x,z + u_z,x)`.

Report the two cutoff families: the shear one `√(C_44/ρ)/2` (form unchanged) and the extensional one
`√(C_33/ρ)/2` (replaces `c_L/2`). The S/A split survives, because the geometry and the material are
symmetric about `z = 0`.

**The decisive test:** set `C_11 = C_33 = λ + 2μ`, `C_12 = C_13 = λ`, `C_44 = μ` using the aluminium
`λ, μ`; the transversely isotropic code must reproduce the isotropic CSV to rel. < 1e-6. Fix any
mismatch here, because Steps 2–5 inherit it.

Constants: single-phase BaTiO₃ and CoFe₂O₄ sets are transcribed into `params.md` from a named
published MEE table, with at least two homogenisation schemes recorded — **I have not verified
those numbers**, so they must be entered by the scholar from the source, not from this note. At this
step only the *elastic* part of the homogenised set is used, at `vf = 0, 0.2, 0.4, 0.6, 0.8, 1.0`,
with `vf = 0` and `vf = 1` recovered exactly as the two single-phase limits.

## 3. What must not be done yet

No `φ`, no `ψ`, no `θ`, no magnetoelectric tensor, no size effect; the phonon stress is classical
(NSGT enters at Step 5 on the mechanical part only). The four face-condition combinations
(`D_z = 0`/`φ = 0` × `B_z = 0`/`ψ = 0`) belong to Step 3 — do not introduce them early.

## 4. Deliverables and exit criteria

Send: (i) the hand derivation of the transversely isotropic quadratic and the four stress
expressions; (ii) `c` vs `fd` for (a) and (b) on one figure; (iii) the CSV at the five fixed `fd`
for S0, A0, S1, A1 with `k_imag` zeros; (iv) the isotropic degeneracy test of §2(b) with its relative
difference; (v) the `vf = 0` and `vf = 1` elastic limits. Step 1 passes when (a) matches to 1e-4,
(b) reduces to (a) to 1e-6, and the root counts agree with the Arena cross-check.

*Reminder from the gate: Paper C is the lowest-priority paper and Q2 is the accepted outcome; do not
extend this step to chase the Q1 stretch.*
