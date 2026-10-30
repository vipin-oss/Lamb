# Problem v2 — Paper B (Neha): Lamb waves in a 1D hexagonal piezoelectric quasicrystal plate

Status: proposal for the Task-0 gate. Conventions as in `docs/02_workflow_crosscheck.md`
(exp[i(kx−ωt)], thickness 2h, faces z = ±h, plane strain, k = k_r + i k_i, k_i > 0 decays,
fd = f·2h in Hz·m). Unchanged; nothing here asks for a convention change.

## 1. Working title

**Which mechanism damps the wave? A thickness-scaling fingerprint for attenuation in
one-dimensional hexagonal piezoelectric quasicrystal plates with MGT heat and nonlocal strain
gradient elasticity.**

## 2. One-sentence finding (the hook)

> Three dissipation mechanisms can act in a quasicrystal plate — phason relaxation, MGT thermal
> relaxation and the size-effect distortion of the `ω(k)` map — and they scale with plate thickness
> differently (`fd_peak ∝ 1/h`, `∝ h⁰`, `∝ h` respectively), so **a scan of the attenuation-peak
> position against thickness identifies which mechanism dominates without fitting any constant**,
> while the phase-velocity curve cannot distinguish them at all.

Checkable in one sentence: measure `k_i(fd)` at five thicknesses, plot peak `fd` against `h` on a
log–log axis, read the slope. Slope −1 = phason diffusion, 0 = MGT, +1 (through `ω(k)`) = size effect.

**What the hook replaces.** `docs/03_novelty_upgrades.md` proposed "phason wave-like vs diffusive →
exceptional points and coalescence" as the major upgrade. The sweep shows mode-conversion and
attenuation-jump analyses already exist (Wave Motion 2025, doi:10.1016/j.wavemoti.2024.103479;
Acta Mech. Solida Sin. 2026, doi:10.1007/s10338-026-00755-4). Exceptional points are therefore
demoted to a supporting figure, and the phason-model *comparison* — which nobody has done inside one
plate model — becomes the spine, sharpened into a measurable scaling law.

## 3. Three claims

### C1 — The phason kinematics decides whether the plate attenuates at all without heat.
- **Statement.** With a **diffusive** phason (Lubensky–Ramaswamy–Toner hydrodynamics,
  doi:10.1103/physrevb.32.7444) the plate attenuates at zero thermal coupling; with a **wave-like**
  (inertial) phason it does not — the phason branch is real and gapped. The A0 mode is the more
  sensitive of the two families, because its curvature couples to the phason strain differently.
- **Figure F3.** `k_i` vs `fd` for both phason models, A0 and S0, at one `h`, with `k_i ≡ 0`
  marked on the wave-like curves.
- **Limiting cases.** (a) Phason–phonon coupling → 0 must return the pure phonon–electric plate of
  Step 2 to < 1e-6 in both models. (b) Diffusive relaxation rate → ∞ must return the wave-like
  result to < 1e-6 (the two models must merge in that limit — this is the check that the two
  implementations are of the *same* physics).
- **Fails if.** the two models differ by less than the root-finding resolution anywhere in the
  window; then the choice is unobservable and C1 is dropped (paper falls back to Q2).

### C2 — The peak of attenuation carries a thickness fingerprint with three distinct slopes.
- **Statement.** `fd_peak = f_peak·2h` obeys `fd_peak ∝ h^(−1)` for phason-diffusion-dominated
  damping, `∝ h⁰` for MGT-dominated damping (`ωτ_q ≈ 1`), and is dragged with `h` through the
  `ω(k)` map when size effects dominate. The three regimes are separated by crossovers that are
  computable from `D_ph`, `τ_q` and `l/h`.
- **Figure F5.** log–log `fd_peak` vs `h` with the three asymptotes drawn, one curve per dominant
  mechanism, plus the measured-slope table.
- **Limiting cases.** `τ_q → 0` (Fourier) removes the `h⁰` asymptote and must leave the `h^{-1}` one
  untouched; `D_ph → 0` removes the `h^{-1}` asymptote and must leave the thermal one untouched.
- **Fails if.** two slopes coincide within the fit error over the accessible `h` range (i.e. the
  window is too narrow to separate them) — then the claim is a statement about a window, not a law,
  and must be written that way or dropped.

### C3 — NSGT enters QC plates through a *second* combination because the phason field has its own
gradient, and this is visible as a split between the phonon-like and phason-like branches.
- **Statement.** In an NSGT quasicrystal the phason stress carries its own length scale, so the
  phonon and phason branches are shifted by *different* combinations of `(l_nl, l_g)`; the resulting
  branch splitting is a signature that a single-scale nonlocal model cannot reproduce.
- **Figure F7.** Branch-splitting map in the `(l_nl, l_g)` plane overlaid with the single-scale
  nonlocal contour that best fits the same data (the difference between the two is the claim).
- **Limiting cases.** `l_nl = l_g = 0` returns Step 4 (MGT, no size effect); nonlocal-only and
  gradient-only give opposite shifts of the same magnitude.
- **Fails if.** the two branches are not split differently by the two scales, i.e. the phason
  length scale carries no independent effect.
- **SETTLED AT THE GATE (Dr. Vipin, 30 Oct 2026).** In the **base model, NSGT is applied to the
  phonon stress only; the phason stress remains classical.** The NSGT-on-phason variant is **not**
  part of the base model: it is added at **Step 5 as a sensitivity result only**, and reported as
  such (one figure, clearly labelled, never used to support C1–C3). C3 must therefore be stated in
  terms of how the *phonon* length scales split the two branches, with the phason-gradient variant
  as a caveat on the size of the effect. I will not extend NSGT to the phason field silently.

## 4. Upgrades: one major, one minor

**U1 (major) — the phason-model comparison as a controlled experiment.** Both kinematics
implemented in the same code, same boundary conditions, same material, with the merge test
(diffusion → ∞ ⇔ wave-like) as the proof that they are comparable. Physics justification: the
phason is the only field in any of these three papers whose *kinematics* is not settled by
thermodynamics alone; comparing them answers a question the field has left open rather than adding
an effect.

**U2 (minor) — attenuation budget by energy flux** (Shared upgrade S1), used to separate the phason
and thermal contributions so C2's slopes can be measured rather than inferred.

**Demoted:** S3 (exceptional points) — supporting figure only, because [2] and [3] are already in
that territory. **Not used:** S4, S5.

## 5. Model definition

### 5.1 Fields
`u_x, u_z` (phonon displacement), `w_x, w_z` (phason displacement — note: with the quasiperiodic
axis along z, the phason vector has components coupled to the phonon field through `R_ij`),
`φ` (electric potential), `θ` (temperature), all in plane strain, wave along x.

### 5.2 Couplings
1D hexagonal (point group 6mm) piezoelectric quasicrystal: phonon elasticity `C_ijkl`, phason
elasticity `K_ijkl`, phonon–phason coupling `R_ijkl`, piezoelectric `e_kij`, dielectric `ε_ik`,
thermal stress `λ_ij`, pyroelectric `p_i`. Constitutive relations in NSGT differential form
(phonon part), and — depending on the answer to the C3 question — either the same form or the
classical form for the phason part. **This choice is the single most important open modelling
question in Paper B and is put to Dr. Vipin in §7.**

Phason kinematics, the two cases to be compared:
- **Wave-like:** `ρ ẅ_i = H_ij,j` (phason inertia `ρ` or a phason-specific density), giving
  propagating phason branches.
- **Diffusive:** `τ_ph ẇ_i + w_i = …` (relaxation form), i.e. the Lubensky et al. overdamped
  kinematics, which produces intrinsic attenuation.

### 5.3 Boundary conditions at z = ±h
`σ_zz = σ_xz = 0`; **phason traction-free** `H_zz = H_zx = 0` (and the phason higher-order traction
if NSGT is applied to phason); NSGT extra higher-order phonon traction (`steps/step5_bcs_nsgt.md`,
approval required before coding); `D_z = 0` (open) or `φ = 0` (short); `∂θ/∂z = 0` or `θ = 0`.
For the diffusive phason: `∂w/∂z = 0` (no phason flux through a free face) — this is a modelling
assumption with no direct experimental support and must be labelled as such.

### 5.4 Excluded
Surface elasticity, imperfect interfaces (owned by Compos. Struct. 2025), FG grading (owned by
Results Phys. 2024), nonlinearity, 3D, multi-field optical coupling, memory-dependent derivatives,
magnetoelectric coupling.

## 6. Validity window

Same construction as Paper A: shaded trust band `kh ∈ [0.05, min(1/λ, 2h/10Λ_ph)]` on **every**
dispersion/attenuation figure, hatched beyond it, `h/l_max` in the caption. Additional QC-specific
bound: the continuum phason model is meaningful only when the phason correlation length is much
smaller than the plate thickness — no sourced value exists, so it is stated as an assumption with a
sensitivity sweep, not as a number.

## 7. Parameter plan

**Material set: 1D hexagonal piezoelectric quasicrystal (Al–Ni–Co-type QC elastic constants plus a
piezoelectric QC set).** Sources: to be fixed at Step 1 from the reference set used by
Acta Mech. 232 (2021) doi:10.1007/s00707-020-02811-7 (which the plan already nominates as the Step-3
benchmark) — **I have not verified those constants myself and will not quote a value until the
source table is in `params.md`.**

| Constant group | Symbols | Source | Status |
|---|---|---|---|
| Phonon elastic | `C_11, C_12, C_13, C_33, C_44` | Acta Mech. 232 (2021) set | `[U]` pending |
| Phason elastic | `K_1, K_2` | same | `[U]` |
| Phonon–phason coupling | `R` | same; range quoted in Results Phys. 2024 | `[U]` |
| Piezoelectric/dielectric | `e_ij, ε_ij` | same | `[U]` |
| Phason diffusion coefficient | `D_ph` | **no source found** | `[U]` — sweep range only, labelled "assumed" |
| MGT relaxation | `τ_q` | no measured QC value; range 10⁻¹³–10⁻¹¹ s | `[U]` range |
| `c_p, α_T, k_th` | — | literature, with source | `[U]` |

**Sensitivity ranking.** (i) `D_ph` — it sets the entire `1/h` branch of C2 and has no measured
value; the paper must present it as a band. (ii) `R` (phonon–phason coupling) — controls whether the
phason branch is observable at all. (iii) `τ_q`. (iv) `l/h`. (v) the elastic set, which is a
common-mode rescaling.

## 8. Target journals (SJR 2025 read on scimagojr, 30 Oct 2026)

| Rank | Journal | SJR / quartile | Fit | Comment |
|---|---|---|---|---|
| 1 | **Eur. J. Mech. A/Solids** | 1.023, Q1 (Mechanics of Materials, Mech. Eng., Math. Phys., Mater. Sci. misc.) | Best fit for a *model-comparison* mechanics paper; shorter, faster, and less novelty-hungry than IJSS | Realistic best Q1 shot |
| 2 | **Int. J. Solids Struct.** | 1.002, Q1 (all six categories), H = 216 | Fits if the scaling fingerprint is clean; the QC-plate benchmark [1] is in a sibling journal | Stretch |
| 3 | **Acta Mech. Solida Sin.** | **not checked this session** | The direct competitor [2] appeared here, so the editors know the topic | Would need the quartile verified; do not assume Q1 |

Explicitly **not** targeted: *Wave Motion* (Q2, 0.499 in SJR 2025). *Applied Mathematics and
Mechanics (Engl. Ed.)*, *Composite Structures*, *Results in Physics* — not checked; they are where
neighbours published.

> **PROVISIONAL HOOK (30 Oct 2026).** Dr. Vipin's ruling: the thickness-scaling hook of C2 is
> **provisional, pending his review**. No writing, no figure titles and no abstract may commit to it
> until he has approved it. The work that can proceed meanwhile is the part that is needed either
> way: the two phason kinematics and the merge test (C1), which are also the Step-3 gate.

## 9. What would change this problem again
1. If C1's merge test fails (the two phason models are not implementations of the same physics),
   the comparison is meaningless and the paper collapses to "one more QC plate" → Q2.
2. If C2's slopes cannot be separated in the accessible `h` window, the fingerprint is not a law.
3. If a 2026–27 paper does the phason-model comparison first, the paper needs a new spine.
