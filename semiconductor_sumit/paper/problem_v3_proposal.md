# problem_v3_proposal.md — proposed retitle and restated claims (Sumit)

**Status: PROPOSAL. `paper/problem_v2.md` is unchanged and remains the document of record until
Dr. Vipin accepts this.** Reason for the proposal: the MGT distinguishability map
(`steps/step3_prerecheck_mgt_map.md` §3a) shows the thermal-relaxation effect is **not resolvable
anywhere in the admissible thickness band** once `Λ_ph` is sourced (`Λ_ph ≳ 13.2 nm` ⇒ `2h ≥ 132 nm` ⇒
the boundary needs `τ_q ≥ 8.4×10⁻¹¹` s, 8× above the top of the literature range). A claim that cannot
be observed cannot carry a Q1 paper; the carrier and size-gradient claims can.

---

## 1. Title

> **Carrier screening and strain-gradient dispersion in thin piezoelectric semiconductor plates:
> a two-observable protocol for separating the nonlocal and gradient length scales**

Alternatives, in order of preference:
1. above (C1 + C3, both measured claim types);
2. *Screening-threshold attenuation in piezo-semiconductor plates: where the thermal relaxation
   cannot be seen and why* — keeps MGT in a subordinate clause, higher risk of being read as a
   negative-result paper;
3. with MGT removed from the title entirely and instead named in the subtitle as a thermal
   sensitivity — safest, but loses the formulation link to the group's earlier work.

**One-sentence checkable hook.** For a thin ZnO plate the attenuation coefficient is not monotone in
carrier density: it peaks once, and the *position* of that peak is set by the elastic-wave velocity,
not by the electron mobility — so a single attenuation curve at fixed thickness determines the product
`σ = n₀eμ_n` while its shift with `kh` separates the two strain-gradient lengths, which no
dispersion-only measurement can do.

## 2. Claims (three, as required)

### C1 — carrier screening produces a resolvable attenuation maximum (unchanged from v2)
- **Statement.** `k_i(n₀)` at fixed `fd` is non-monotone: it rises while the drift channel is active,
  peaks at `n₀*`, and falls once the Debye length falls below the plate half-thickness combined with
  the wave number, leaving the thermoelastic floor.
- **Figure F1.** `k_i` vs `n₀` (10¹⁸–10²⁴ m⁻³) at three `fd`, with `n₀*` marked and the floor dashed.
- **Limiting case.** `n₀ → 0` returns Step 3 to < 10⁻⁶ (relative), and `n₀ → ∞` returns the
  fully-screened limit.
- **Why earlier models cannot show it.** Previous ZnO-plate papers plot `k_i` vs `fd` at one doping, or
  vs doping at one frequency, and never resolve the turning point; the turning point is the observable.

### C3 — two observables, not one, are needed to separate `l_nl` and `l_g` (promoted to a claim)
- **Statement.** NSGT enters through `(1 + l_g²k²)/(1 + l_nl²k²)`. At fixed `kh` a phase-velocity
  curve constrains one combination of `(l_nl, l_g)`; the **peak locus** `n₀*(fd)` and the **floor
  cutoff** supply a second and third equation, so the pair is identifiable from attenuation alone,
  where dispersion alone leaves it degenerate.
- **Figure F5.** Identifiability map in the `(l_nl/h, l_g/h)` plane: the band of values consistent with
  the velocity curve (a stripe) intersected with that from the peak locus (a curve) — the intersection
  is a point.
- **Limiting case.** `l_nl = l_g = 0` returns Step 4 to < 10⁻⁶; `l_nl = 0` and `l_g = 0` individually
  give equal and opposite shifts of the peak locus (a sign test).
- **Why earlier models cannot show it.** Published NSGT plate papers report fits with one length scale
  set to zero; none demonstrates identifiability of the pair.

### The thermal channel — **Route A: an adiabatic/isothermal bracket, not a coupled MGT mechanism**
- **Statement (ruling 30 Oct 2026 — Route A).** The heat problem is solved **twice**, in the two
  rigorous limits — **adiabatic** (no heat flow between material points) and **isothermal**
  (temperature slaved to the strain) — and the true attenuation is *bracketed* between them. The
  bracket width is `O(Δ_E)`, `Δ_E = T₀β²/(ρ c_p c_L²)`, i.e. 10⁻³–10⁻². No `τ_q`, `κ` or `Λ_ph`
  enters the result. MGT appears **only** as a one-page appendix item showing it lies inside the
  bracket, and therefore is not an observable (`docs/04_scale_overlap_window.md`; map in
  `steps/step3_prerecheck_mgt_map.md`).
- **Figure F6 (kept, demoted).** `k_i` vs `fd` for the adiabatic and isothermal bounds, with the
  bracket shaded and MGT drawn inside it for one `τ_q` value to show it is invisible at that scale.
- **Limiting case.** The two bounds must coincide to < 10⁻⁶ when the thermal coupling is switched
  off (`β = 0`), and the adiabatic curve must reproduce classical thermoelastic damping at the low-`fd`
  edge (programming checks).
- **Honest value.** Pre-empts the obvious referee objection and shows the formulation is complete
  without claiming an effect that the numbers do not support.

## 3. Upgrades (exactly one major, one minor)

- **Major (U1).** The **identifiability protocol**: peak locus + floor cutoff + velocity, three
  observables for two unknowns, with the nulling/drift-nulling measurement that removes the carrier
  channel so the floor is reachable. This is the "we show that … which earlier models cannot show"
  content, and it survives without MGT.
- **Minor (U2).** The **attenuation budget closed by energy flux** (Poynting-like check across the
  plate faces) to < 10⁻³ relative, which also fixes the sign convention for `k_i` unambiguously.
  Unchanged from v2.

## 4. What does **not** change

- **Steps 1 and 2 are unchanged**: isotropic elastic Rayleigh–Lamb (`steps/step1_…md`), then the
  piezoelectric open/short boundary conditions (`steps/step2_piezo_zno.md`). No re-derivation, no
  re-numbering, and the Step-1 targets stand (S0 → 5393.91, A0 → 2909.73 m/s, 1e-3…1e-4 tolerances).
- **Step 3 = bracket + classical thermoelastic check.** Run the adiabatic and isothermal limits, verify
  they bracket a classical coupled-thermoelasticity run at low `fd`, and record the bracket width. No
  MGT solver is built; the MGT one-pager reuses the same code path with `τ_q` as a switch, for the
  appendix only.
- The two Step-4 hard gates stay: C1 monotonicity, and floor resolution.

## 5. Model, boundary conditions, validity window

Unchanged from v2 §4: plane strain, `2h`, faces `z = ±h`, `exp[i(kx−ωt)]`, `k = k_r + i k_i`,
`k_i > 0` decaying. Electrical: open-circuit faces (charge-free) as the base case, short-circuit as the
companion; both implemented as the two limits of the surface charge condition. Mechanical: traction-free
plus the NSGT extra boundary conditions (moment/traction-gradient pairs) — **to be approved before
Step 5**, not before. Validity window `kh ∈ [0.1, 3]` printed on every figure; the `2h ≥ 10Λ_ph = 132 nm`
line is added to the parameter figures as a hard exclusion.

## 6. Parameters

| constant | v3 status |
|---|---|
| `ρ = 5680`, `ε`, `c_ij`, `e_ij`, `μ_n = 200 cm²/Vs` | sourced as in v2 §7, unchanged |
| `c_p = 500 J/kg·K`, `α_T` | still `[U]`; now **not load-bearing**, because the thermal channel is a comparison only |
| `k_th = 60` W/m·K (bulk) | sourced; the thin-film 1.2 W/m·K column becomes a sensitivity |
| `Λ_ph = 13.2 nm` | **new, sourced** — Krahl et al. JPCC 124 (2020) 24731, 10.1021/acs.jpcc.0c06461 |
| `τ_q ∈ [10⁻¹³, 10⁻¹¹] s` | range, `[U]`; no longer decides the title |
| `l_nl, l_g` | dimensionless `l/h` sweeps only, as ruled |

## 7. Journals (unchanged check, re-ranked for the new claim set)

1. **Int. J. Solids Struct.** (SJR 1.002, Q1, six categories) — best fit for an identifiability paper;
   the mechanics community is the audience for a two-observable argument.
2. **Int. J. Eng. Sci.** (1.228, Q1) — takes formulation-heavy work; second choice.
3. **Eur. J. Mech. A/Solids** (1.023, Q1) — faster, accepts shorter papers; use if C3 falls.

## 8. Risks introduced by this proposal

- **R1.** Removing MGT from the title weakens the link to the group's previous papers. Mitigation: the
  comparison section, stated as a positive result about the model's reach rather than as a failure.
- **R2.** C3 is a hypothesis until the Step-4 numerics show the peak locus actually moves with
  `l_nl/h`, `l_g/h`. **Kill criterion carried over:** if the peak locus is insensitive to both lengths
  at the 1 % level, C3 is dropped and the paper becomes C1 + protocol (IJES/EJM-A only).
- **R3.** `Λ_ph` is the one new constant the argument leans on; it is sourced but it is a *derived*
  gray-medium value. The sensitivity line `Λ_ph ∈ [6.6, 26.4] nm` must appear on the exclusion figure.
