# Problem v2 — Paper A (Sumit): Lamb waves in a piezoelectric semiconductor plate

Status: **proposal for Dr. Vipin's approval at the Task-0 gate.** Supersedes the problem
statement in `plan_pdfs/Research_Plan_Guided_Waves_in_a_Smart_Semiconductor_Plate_1.pdf` where
the two differ. Conventions are unchanged from `docs/02_workflow_crosscheck.md`
(exp[i(kx−ωt)], thickness 2h, faces z = ±h, plane strain, k = k_r + i k_i, k_i > 0 decays along
+x, fd = f·2h in Hz·m). If the design below asks for a convention change, that is a stop-and-ask
item; as written it does not.

---

## 1. Working title

**Hidden behind screening: the thermoelastic attenuation floor of Lamb waves in piezoelectric
semiconductor plates, and what Moore–Gibson–Thompson conduction does to it.**

Running title: *Attenuation channels in piezoelectric semiconductor plates.*

## 2. One-sentence finding (the hook)

> In a piezoelectric semiconductor plate the acoustoelectric loss peaks where the wave frequency
> matches the dielectric relaxation rate and is **screened away at higher doping**, so beyond a
> computable doping level the residual Lamb-wave loss is purely thermoelastic — and that residual
> floor **falls with frequency under MGT conduction while it saturates under Fourier conduction**,
> which makes an attenuation measurement, not a velocity measurement, the way to see MGT
> relaxation in a plate.

Why a reader can check it: both sentences are quantitative. The peak locus is
`n₀* = ε ω / (e μ)`; the floor is the Zener/TED attenuation of the plate; the MGT-vs-Fourier
difference is a different high-`fd` slope of the same curve. Nothing in the claim needs a new
material — only the same ZnO/GaAs plate measured at two dopings.

Why this is not "known problem + one more effect": the two loss channels are **not** independent
additions, they are ordered — one screens the other. That ordering is the finding, and it is what
tells the reader which of the three effects (carriers, heat, size) is observable in which regime.
It also answers the reviewer question "why all these effects at once?" with a physical answer
instead of a modelling answer.

**What the hook replaces.** The major upgrade proposed in `docs/03_novelty_upgrades.md`
(§"Paper A", DC drift bias → non-reciprocal Lamb waves with acoustoelectric amplification) is
**already published in a plate by Yang & Zhou (2005)**, doi:10.1016/j.ijsolstr.2004.10.011,
including the `v_d > c` gain threshold, and extended to laminates in 2004. It is now a *tool*
in this paper (§6, U1), never a claim. See `literature_table.md` §1 entry 2.

## 3. Exactly three claims

Each claim has one figure, one limiting case that must pass before the claim is written, and one
explicit failure condition. Tolerance references are those of `docs/02_workflow_crosscheck.md`.

### C1 — The acoustoelectric attenuation is non-monotonic in carrier density, with a computable peak locus.
- **Statement.** At fixed fd, `k_i(n₀)` has a maximum at `n₀*(fd) = ε₃₃ ω /(e μ_n)` (dielectric
  relaxation matching), on both sides of which `k_i` decreases: below because there are too few
  carriers to absorb, above because the field is screened before the carriers can respond. The
  locus `n₀* ∝ fd` is therefore a straight line in the (n₀, fd) plane and is **material-set**:
  doping tunes it, thickness does not.
- **Figure.** F4: `k_i` vs `fd` for a ladder of n₀ (10¹⁸–10²⁴ m⁻³), A0 and S0, with the analytic
  locus `n₀*(fd)` overlaid as a dashed line and the peak positions marked.
- **Limiting cases (must pass, in this order).**
  1. `n₀ → 0` returns Step 3 (piezo-thermoelastic plate) with relative difference < 1e-6 — a
     programming check, machine-like.
  2. Measured peak position vs analytic `n₀*`: relative difference < 5% (5% and not 1e-4, because
     `n₀*` is a leading-order relaxation argument; the 5% is the claim's own honesty budget and
     must appear on the figure).
- **Fails if.** `k_i(n₀)` is monotone over the whole 10¹⁸–10²⁴ range for every fd in the window.
  In that case C1 is dropped and the paper is not submitted at Q1 (see `q1_scorecard.md`).

### C2 — Above a threshold doping the residual loss is a thermoelastic floor whose high-frequency behaviour discriminates MGT from Fourier conduction.
- **Statement (REVISED 2026-30-10 after the bulk-medium test — the earlier "MGT removes the floor"
  wording was wrong).** For `n₀ ≫ n₀*(fd)` the carrier channel is screened and `k_i` approaches the
  thermoelastic floor `k_i^th`. In an unbounded medium **both** models saturate at high frequency:
  `k_i^F → Δ_E/(2c_Lτ_T)` and `k_i^MGT → (Δ_E/2c_L)·τ_T/(τ_T−τ_q)²` (derivation:
  `steps/step3_prerecheck_bulk_medium.md`, eqs. 3 and 5). MGT therefore changes **two** observables:
  it rescales the plateau by `τ_T²/(τ_T−τ_q)²`, and it moves the peak from `ω = 1/τ_T` to
  `ω = 1/|τ_T−τ_q|`. In a plate `τ_T` is replaced by the through-thickness diffusion time
  `τ_th = (2h)²/(π²κ)`, so the peak position becomes a function of **thickness**. The discriminating
  observable is the **peak shift with 2h**, not a change of slope.
- **Figure.** F6: peak position (fd at which `k_i^th` is maximal) vs `2h`, for Fourier and for
  τ_q = 10⁻¹³, 10⁻¹², 10⁻¹¹ s at both k_th ends (60 and 1.2 W/m·K); inset: plateau ratio
  `k_i^MGT/k_i^F = τ_T²/(τ_T−τ_q)²`. Carrier channel removed two ways (high doping, drift-nulled).
- **Limiting cases.**
  1. `τ_q → 0` must reproduce the Fourier curve to < 1e-6 (programming check).
  2. Thermal coupling off (λ_ij, p_i → 0) must give `k_i^th = 0` exactly.
  3. Classical coupled thermoelasticity must reproduce the published TED peak condition for a
     plate, `ω ≈ π²α/(2h)²`, to < 5% (order-of-magnitude check, number recorded).
- **Fails if.** The floor is numerically smaller than the root-finding resolution of the solver
  (i.e. the complex root `k_i` is below ~1e-8 `k_r`); **or** the predicted peak shift between τ_q = 0
  and τ_q = 10⁻¹¹ s is smaller than the solver's peak-location resolution at the thicknesses where the
  floor is resolvable; **or** the two k_th ends give the same sign of effect (in which case the k_th
  uncertainty, not MGT, controls the observation). Then C2 is dropped and MGT is demoted from a claim
  to a formulation remark.

### C3 — The two NSGT length scales move the peak locus and the floor cutoff, and a two-point attenuation protocol can separate them where phase velocity cannot.
- **Statement.** NSGT enters wave problems through the ratio `(1 + l_g²k²)/(1 + l_nl²k²)`
  (gradient stiffens, nonlocal softens). At fixed `kh` the phase velocity therefore constrains
  essentially **one** combination of the two scales, so a dispersion curve alone cannot identify
  them; the peak locus `n₀*` and the floor cutoff `ω τ_q ≈ 1` are two further observables, and
  their *shift* with `kh` gives the second equation.
- **Figure.** F8: contours of the peak-locus shift `Δn₀*/n₀*` (panel a) and of the floor-cutoff
  shift `Δfd_cut/fd_cut` (panel b) in the (l_nl, l_g) plane at one `kh`, with the iso-lines of the
  phase-velocity shift (panel c) printed at the same scale. If panel (c) is a family of parallel
  lines and (a)/(b) are not, the identification works.
- **Limiting cases.**
  1. `l_nl = l_g = 0` returns Step 4 to < 1e-6.
  2. Nonlocal-only (`l_g = 0`) and gradient-only (`l_nl = 0`) must reproduce, respectively,
     softening and hardening of the same magnitude with opposite sign.
- **Fails if.** The rank of the sensitivity matrix `∂(c, n₀*, fd_cut)/∂(l_nl², l_g²)` is 1 at the
  working point. **This is a declared risk, not a promise:** C3 is a hypothesis to be tested at
  Step 5/6. If it fails, the paper reports the degeneracy explicitly as a limitation and C3 is
  replaced by the attenuation budget (U2). That substitution is pre-approved in this document.

## 4. Upgrades: one major, one minor

### U1 (major) — The nulling protocol: use the acoustoelectric channel as a switch, then read the floor.
A DC drift bias with `v_d → c_ph` cancels the acoustoelectric loss (Hutson–White; in a plate,
Yang & Zhou 2005). Once cancelled, the measured attenuation **is** `k_i^th`. That turns a weak
floor (`k_i/k_r ≈ 1.8×10⁻⁴` for ZnO vs `3.8×10⁻²` at the carrier peak — a factor 213, computed in
`checks/task0_scaling.md`) into the dominant signal, and it turns the MGT relaxation time into a
measurable quantity. Delivered as a map: sign and magnitude of `k_i` in the (`v_d/c_ph`, `fd`)
plane, with the null line `k_i = 0` and the NSGT contours overlaid (Figure F7).
- **Physics justification, not size.** Two channels with *different control knobs* — `n₀` and
  `v_d` for carriers; `τ_q`, `h`, `k` for heat. A knob that switches one channel off without
  touching the other is a measurement, not a parameter study.
- **Check.** `v_d = 0` returns C1/C2; with `τ_q = 0` and `l = 0` the null line must reproduce the
  classical `v_d = c` threshold of Yang & Zhou 2005 (< 1%, digitised from their figure if the
  formula cannot be matched exactly — and if digitisation is needed, the paper says so).

### U2 (minor) — Attenuation budget by energy flux (Shared upgrade S1).
Split `k_i` into carrier and thermal parts by an energy-balance identity on the mode shape, so
that the decomposition is *derived* rather than asserted by switching terms off. This is what
lets F4/F6 be read quantitatively, and it gives the "which channel dominates here" number that
C1/C2 need.

**Not used:** S3 (exceptional points) — the dissipative spectrum here is dominated by one strong
channel, so coalescence is unlikely to be robust; S4 (lattice calibration of l) — kept as future
work; S5 (Sobol) — offered as a supplement if time allows, not a claim.

## 5. Model definition

### 5.1 Fields (plane strain, x along the plate, z through thickness)
| Field | Symbol | Note |
|---|---|---|
| Mechanical displacement | `u_x(x,z,t)`, `u_z(x,z,t)` | plane strain, `u_y = 0`, `∂/∂y = 0` |
| Electric potential | `φ(x,z,t)` | `E_i = −φ,_i` |
| Temperature change | `θ(x,z,t)` | from the stress-free reference |
| Carrier perturbation | `Δn(x,z,t)` | electrons, `n = n₀ + Δn`, `|Δn| ≪ n₀` |

### 5.2 Couplings and constitutive relations
Piezoelectric, with thermal stress and pyroelectricity, in the **NSGT differential form**:

```
(1 − l_nl² ∇²) σ_ij = (1 + l_g² ∇²) [ c_ijkl ε_kl − e_kij E_k − λ_ij θ ]      (1)
(1 − l_nl² ∇²) D_i  = (1 + l_g² ∇²) [ e_ikl ε_kl + ε_ik E_k + p_i θ ]          (2)
```

Material symmetry: hexagonal 6mm, poled along **z** (to be written into the folder README at
Step 2 — the plan leaves it open, and it decides the S/A split). `λ_ij = c_ijkl α_kl`,
`β_ij = λ_ij`, `p_i` pyroelectric.

Equation of motion and Gauss law:

```
σ_ij,j = ρ ü_i ,     D_i,i = −e Δn                                   (3)
```

Linearised carrier transport with a DC drift `v_d` along x:

```
∂Δn/∂t = D_n ∇²Δn + n₀ μ_n ∇²φ + v_d ∂Δn/∂x − Δn/τ_R               (4)
```

with `μ_n` electron mobility, `D_n = μ_n k_B T₀/e` (Einstein), and **`τ_R` the carrier
recombination (lifetime) time** — not a relaxation time of the dielectric response. Resolved at the
gate: `τ_R → ∞` is the **base case** (no recombination over a wave period); a finite-`τ_R`
sensitivity (`τ_R = 10⁻⁹`–`10⁻⁶` s) is run at Step 4 and must show only a shift of the complex
relaxation rate, with the peak locus `n₀*` unmoved. If `n₀*` moves, the base model was wrong and
C1 must be recomputed with `τ_R` as a parameter.

MGT heat conduction with thermoelastic coupling:

```
k_th ∇²θ = ρ c_p (τ_q θ̈ + θ̇) + T₀ β_ij (τ_q ε̈_ij + ε̇_ij)           (5)
```

`τ_q → 0` gives classical coupled thermoelasticity (this is the Step-3 limiting check).

> **Resolved at the Task-0 gate (Dr. Vipin, 30 Oct 2026).** The MGT form to be used is the one in
> **Gupta et al., IJNMHFF 35(9) (2025) 3400–3428, doi:10.1108/HFF-04-2025-0254**, which Dr. Vipin
> will place in `paper/`. Eq. (5) above is therefore provisional: the scholar must transcribe the
> Gupta form, and the **alternative placement of `τ_q` in the thermoelastic term is carried as a
> Step-3 sensitivity case** (not a silent choice). Both placements must reduce to classical coupled
> thermoelasticity as `τ_q → 0`, and that is the check that decides whether a transcription error
> was made.

### 5.3 Boundary conditions at z = ±h — including the NSGT extras
| Condition | Expression | Note |
|---|---|---|
| Mechanical (classical) | `σ_zz = 0`, `σ_xz = 0` | traction-free faces |
| **Mechanical (NSGT, extra)** | `P_izz = 0` for i = x, z, where `P` is the higher-order (double) stress of the NSGT functional | **This is the pair of extra conditions the plan flagged as undefined.** In plane strain only the z-derivative components survive; the exact surviving set is fixed in `steps/step5_bcs_nsgt.md` and **must be approved before any Step-5 code is written** |
| Electric: open circuit | `D_z = 0` | |
| Electric: short circuit | `φ = 0` | |
| Carrier | `J_nz = 0` (no flux through a free face) | with (4) this is `D_n ∂Δn/∂z + n₀μ_n ∂φ/∂z = 0` |
| Thermal: insulated | `∂θ/∂z = 0` | base case |
| Thermal: isothermal | `θ = 0` | second case, for the floor's sensitivity |

### 5.4 S/A split
With 6mm symmetry poled along z and a symmetric plate, the system separates into symmetric (S)
and antisymmetric (A) families in `u_z, φ, θ, Δn`. A uniform DC drift **along x preserves the
z-symmetry**, so the split survives the drift bias — worth stating explicitly in the paper because
most drift papers do not. If any step shows the split breaking, that is a bug, not physics, and
`docs/02_workflow_crosscheck.md` failure cause 3 applies.

### 5.5 Excluded (stated in the paper, not hidden)
Surface elasticity/surface piezoelectricity (competitor [4] has it — we must say why we omit it),
flexoelectricity, non-uniform doping and equilibrium space charge, PN junctions, magnetic fields,
photoexcitation, memory-dependent derivatives, graded/thin-film mismatch, nonlinearity, full 3D,
imperfect interfaces, and carrier trapping.

## 6. Validity window of the model, and how it appears on every figure

The NSGT correction is an expansion in `(k l)²`, and the thermal model is a continuum model with a
mean free path. Both give the same kind of window, and it must be visible, not buried:

| Constraint | Origin | Form used | Gives |
|---|---|---|---|
| NSGT expansion | correction is `O((k l)²)` | `k l_max ≤ 1` | `kh ≤ h/l_max` |
| Continuum mechanics | lattice spacing `a₀ ≈ 0.5 nm` | `2h ≫ a₀` | `kh` upper bound only at absurd k |
| MGT/Fourier conduction | phonon mean free path `Λ_ph` | `2h ≳ 10 Λ_ph` | rules out `2h ≲ 50 nm` for ZnO if `Λ_ph ≈ 5 nm` (`UNVERIFIED` — to be sourced) |
| Long-wave carrier model | drift-diffusion is diffusive | `ω τ_R ≪ 1` and `k λ_D ≪ 1` | low-fd bound |

**Presentation rule.** Every dispersion/attenuation figure carries (i) a shaded band
`kh ∈ [0.05, min(1/λ, 2h/(10Λ_ph))]` labelled "model trust window", (ii) a hatched region beyond it
labelled "shown for continuity only", and (iii) the value of `h/l_max` in the caption. Claims C1–C3
are evaluated **inside** the window only; points outside are drawn but never used in a claim.
This directly answers `docs/00_feasibility_analysis.md` common weakness 2 and buys Shared upgrade S6
for free.

## 7. Parameter plan

Sources are given per constant. `[S]` = sourced, `[SPREAD]` = sources disagree (both ends used),
`[U]` = **no source yet — must be found before the step that needs it**; a `[U]` constant may not
appear in a figure caption until it is sourced. Nothing here is called "measured" except values
explicitly reported as measured in the cited source.

| Constant | Symbol | Value used for scaling | Source | Status |
|---|---|---|---|---|
| Density | ρ | 5680 kg/m³ | eFunda ZnO entry; AZoM 5660; review 5605 | `[SPREAD]` ~1.3% |
| Elastic constants | c₁₁, c₁₂, c₁₃, c₃₃, c₄₄ | 206, 118, 118, 211, 44 GPa | arXiv:cond-mat/0507217v2, "measured" row; c₁₃ = 105 GPa also quoted (RG summary of the same set) | `[S]` with spread |
| Piezoelectric | e₃₃, e₃₁, e₁₅ | 1.34, −0.57 C/m², e₁₅ from the same wurtzite set | arXiv:cond-mat/0507217v2 | `[S]`; e₁₅ `[U]` |
| Permittivity | ε₁₁, ε₃₃ | 9.16 ε₀, 12.64 ε₀ | eFunda ZnO | `[S]` (other tables give 8.5 ε₀ — `[SPREAD]`) |
| Electron mobility | μ_n | 0.02 m²/V·s (200 cm²/V·s) | AZoM ZnO; review table | `[S]` |
| Thermal conductivity | k_th | **1.2 and 60 W/m·K** (both carried) | thin-film (review table) vs bulk (AZoM) | `[SPREAD]` **50×** — this is the single most dangerous constant in the paper, see §7.1 |
| Specific heat | c_p | ~500 J/kg·K | — | `[U]` |
| Thermal expansion | α_T | ~4×10⁻⁶ /K | — | `[U]` |
| MGT relaxation time | τ_q | 10⁻¹³–10⁻¹¹ s (range) | — | `[U]` range only; no measured ZnO value found in the sweep. The paper must say "assumed range", never "measured" |
| Recombination time | τ_R | ∞ (base), 10⁻⁹–10⁻⁶ s (check) | — | `[U]` |
| Nonlocal length | l_nl | **dimensionless `l/h` only** (0, 0.1, 0.3, 0.5, 1.0) | — | gate ruling: **no dimensional value is claimed**; entered as an `l/h` sweep |
| Gradient length | l_g | **dimensionless `l/h` only**, same set | — | gate ruling: same; the ratio `l_g/l_nl` is the second sweep axis |
| Acoustic drift velocity | v_d | 0–1.2 c_ph | derived from the applied field | parameter, not a constant |

**Carrier-density range:** 10¹⁸–10²⁴ m⁻³. The upper end is set by Dhib et al.'s measured
p₀ = 3.54×10²⁵ m⁻³ (p-type GaAs, doi:10.1016/j.mssp.2024.108743), so 10²⁴ is inside the
experimentally demonstrated range; the lower end is set by the requirement that the linearised
model is not noise-limited.

### 7.1 Sensitivity — which constants the finding is sensitive to (ranked, and why)
1. **k_th (thermal conductivity).** Enters the floor amplitude *and* its peak frequency as
   `α = k_th/(ρc_p)`. The 50× spread between thin-film and bulk ZnO moves the floor peak by 50× in
   frequency and the crossing thickness by √50 ≈ 7×. The paper therefore **plots both ends** and
   makes this a figure, not a footnote. If the finding only survives with one end, it is not a
   finding.
2. **n₀ and μ_n** — they enter only as the product `σ = n₀eμ_n` in `n₀*`. So a wrong μ_n is
   *exactly* equivalent to a wrong n₀ and is invisible unless μ_n is measured independently. Say
   this in the paper: `n₀*` identifies `μ_n` only up to the product.
3. **τ_q** — sets where the floor bends over. It is the least measured constant in the paper and
   the one the MGT novelty rests on. Hence the range and the explicit "assumed" label.
4. **l_nl, l_g** — affect C3 only inside the trust window; below `kh ≈ 0.3` they are invisible.
5. **c_p, α_T, ρ** — enter the Zener parameter as one group `Δ_E = Eα_T²T/(ρc_p)`; a common-mode
   error in this group rescales the floor but does not move its frequency.

## 8. Target journals (SJR read on scimagojr.com, 30 Oct 2026, SJR 2025 data)

| Rank | Journal | SJR 2025 / quartile | Scope fit | Article type |
|---|---|---|---|---|
| **1** | **Int. J. Solids Struct.** (Elsevier) | **1.002, Q1** in Applied Mathematics, Condensed Matter Physics, Materials Science (misc.), Mechanical Engineering, Mechanics of Materials, Modeling & Simulation; H = 216 | Scope names *wave propagation* and *thermal effects in solids* explicitly. The paper is a mechanics-of-solids result with a verification table — exactly IJSS style. Competitors [2] and [15] appeared here. | Full-length research article |
| **2** | **Int. J. Eng. Sci.** (Elsevier) | **1.228, Q1** in Engineering (misc.), Mechanical Engineering, Mechanics of Materials, Materials Science (misc.); H = 140 — highest SJR of the three | "Material modeling and response", interdisciplinary welcome, but the guide says purely mathematical work and pure parameter studies are discouraged. Only worth it if C1–C3 land cleanly; otherwise it reads as a model paper and gets desk-rejected. | Full-length research article |
| **3** | **Eur. J. Mech. A/Solids** (Elsevier) | **1.023, Q1** in Mechanics of Materials, Mechanical Engineering, Materials Science (misc.), Mathematical Physics; H = 117 | Solid mechanics from physical basis to applications; shorter and faster than IJSS; a good landing spot if C3 is dropped but C1/C2 hold. | Full-length research article |

**Deliberately excluded.** *Wave Motion* — **Q2, SJR 0.499 (2025)**, despite being the natural
scope match and despite `docs/00_feasibility_analysis.md` listing it. *Smart Mater. Struct.* and
*Appl. Math. Mech. (Engl. Ed.)* — not checked this session; they are where competitors [4] and [5]
published, which is a signal, but I have not verified their quartile and will not assume it.
*J. Sound Vib.*, *Mech. Mater.*, *Appl. Math. Model.* — not checked this session.

Length norms were **not** verified against the current guides for authors; "full-length research
article" is the only claim made. If a length/format constraint matters, it must be read from the
live guide before submission.

## 9. What would make me tell Dr. Vipin to change this problem again

1. If C1 fails (monotone `k_i(n₀)`), the whole ordering argument dies → the paper is a
   parameter study → downgrade to Q2 (`q1_scorecard.md`).
2. If C2's floor is numerically unresolvable, MGT becomes decoration → the paper is [4]/[5] plus
   size effect → reject at IJSS, submit to a Q2 journal.
3. If a paper published between this sweep and submission already plots `k_i` vs n₀ across the
   peak (entry [5] is the closest to doing so), C1 must be re-checked immediately.
