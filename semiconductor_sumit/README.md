# Paper A (Sumit): Guided Lamb waves in a piezoelectric semiconductor plate

MGT thermal + linearised carriers + nonlocal strain gradient (2 length scales).

**Status: Task 0 done (30 Oct 2026), awaiting Dr. Vipin's approval at the gate.**
Scope was changed at Task 0 after the literature sweep — see `paper/problem_v2.md`.

## Hook (rewritten at Task 0; was "where does attenuation peak")

> In a piezoelectric semiconductor plate the acoustoelectric loss peaks where the wave frequency
> matches the dielectric relaxation rate (`n₀* = ε₃₃ω/(e μ_n)`) and is screened away at higher
> doping, so beyond a computable doping the residual Lamb-wave loss is purely thermoelastic — and
> that floor falls with frequency under MGT conduction while it saturates under Fourier conduction.

The original hook ("where attenuation peaks and how the size scales move it") survives as
claim C1; it is now the *first* link of an ordering argument rather than the whole paper.

**What changed and why:** the major upgrade proposed in `docs/03_novelty_upgrades.md`
(DC-drift non-reciprocal amplification in a PSC plate) was found to be **already published in
2005** by Yang & Zhou (doi:10.1016/j.ijsolstr.2004.10.011), and two 2025 papers now own
"Lamb waves in a PSC plate with attenuation". Details: `paper/literature_table.md`.
The drift bias is kept, but as a *tool* (U1: null the carrier channel, then read the thermal
floor), never as a claim.

## Tracker

| Step | What | Check | Scholar | Arena cross-check |
|---|---|---|---|---|
| 0 | Literature + novelty sweep, problem v2, scorecard | 16 papers, empty cell identified | — | [x] |
| 1 | Elastic Rayleigh–Lamb | see common/step1_instructions.md | [ ] | [ ] |
| 2 | + piezoelectric (open/short) | coupling off -> Step 1; K² from open/short | [ ] | [ ] |
| 3 | + MGT heat | **prerequisites: bulk-medium test + MGT distinguishability map (`steps/step3_prerecheck_bulk_medium.md`, `steps/step3_prerecheck_mgt_map.md`) accepted, and the Gupta heat equation confirmed from `paper/`**; then thermal off -> Step 2; classical thermoelastic limit | [ ] | [ ] |
| 4 | + carriers | n0 -> 0 returns Step 3; high-n0 limit sane; **C1 monotonicity test** | [ ] | [ ] |
| 5 | + NSGT | l = 0 returns Step 4; nonlocal-only, gradient-only checked; extra BCs approved first | [ ] | [ ] |
| 6 | Analysis, figures | smooth branches, consistent root counts, trust window on every figure | [ ] | [ ] |
| 7 | **U1** nulling protocol (`v_d`, `k_i` sign map) | `v_d = 0` returns Step 6; classical `v_d = c` threshold | [ ] | [ ] |
| 7b | **U2** attenuation budget by energy flux (minor) | budget closes to < 1e-3 | [ ] | [ ] |

## Decisions (fixed at or before Step 2 — write them here, do not leave them open)

- **Material: ZnO** (wurtzite 6mm). GaAs kept only as the cross-check material against
  Dhib et al. 2024. Constants + sources + `[U]` flags: `paper/problem_v2.md` §7.
- **Poling direction: along thickness z.** Fixes the S/A split; a drift bias along x preserves it.
- **DC doping** for the linearised carrier equation: n₀ = 10¹⁸–10²⁴ m⁻³, no equilibrium space charge,
  recombination neglected in the base model (τ_R → ∞) — *confirm at the Step-4 gate*.
- **MGT form (settled at the gate, 30 Oct 2026):** use the equation as in **Gupta et al., IJNMHFF
  35(9) 2025, doi:10.1108/HFF-04-2025-0254** (Dr. Vipin is placing it in `paper/`). The alternative
  placement of τ_q is a **Step-3 sensitivity case**, not a choice; both must reduce to classical
  coupled thermoelasticity as τ_q → 0.
- **Carrier lifetime (settled):** τ_R is the carrier **recombination** time; τ_R → ∞ is the base
  case, with a finite-τ_R sensitivity at Step 4 that must leave the peak locus n₀* unmoved.
- **Length scales (settled):** l_nl and l_g enter **only as dimensionless l/h sweeps** (0, 0.1, 0.3,
  0.5, 1.0) plus the ratio l_g/l_nl. No dimensional value is claimed.
- **cp, αT, τ_q:** literature ranges only, each with a source recorded in `params.md` before the
  step that needs it; τ_q labelled "assumed", never "measured".
- **Open question (Step 5, stop-and-confirm):** the exact surviving set of NSGT higher-order
  boundary conditions in plane strain (`steps/step5_bcs_nsgt.md`, to be written and approved
  before any Step-5 code).

## Gate status

Task-0 gate: **waiting for approval** (see `paper/q1_scorecard.md` — verdict GO, conditional on the
C1 monotonicity test and the floor-resolution test, both cheap and both at Step 4).

## Folder layout
`paper/` problem v2 + literature + scorecard — `steps/` equations per step — `checks/` comparisons —
`code_arena/` — `figures/`
