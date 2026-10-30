# Q1 scorecard — Paper A (Sumit), after the literature sweep

Scored 30 Oct 2026, against the plan in `problem_v2.md` (the *refocused* problem, not the original
plan PDF). Scores are 1–5; 5 = a Q1 referee would not raise the point; 1 = fatal. This is a
self-assessment and it is deliberately harsh — an optimistic score here costs Sumit six months.

| # | Criterion | Score | Evidence (one sentence, with the number) |
|---|---|---|---|
| 1 | **Novelty vs the closest papers** | **3 / 5** | The MGT × NSGT × PSC-plate cell is empty in all 16 swept papers, but that is combination novelty; the one *ordering* statement that is new (carrier screening exposes a thermoelastic floor) has not been published, yet the two 2025 competitors [4, 5] already own "Lamb waves in a PSC plate with attenuation", so our delta is one mechanism wide, not one paper wide. |
| 2 | **Physical insight** | **4 / 5** | The finding is an ordering, not an addition: the acoustoelectric channel peaks at `n₀* = ε₃₃ω/(eμ_n)` and is then screened away, so the residual loss is thermal — and the numbers back it (carrier peak `k_i/k_r ≈ 3.8×10⁻²` vs floor `1.8×10⁻⁴`, ratio 213), which explains *why* MGT was invisible in earlier PSC wave papers and *when* it becomes visible. It loses a point because the underlying physics (Hutson–White screening) is from 1960 — we are re-ordering known physics, not discovering new physics. |
| 3 | **Rigour and verification** | **4 / 5** | Every claim has a named limiting case at a stated tolerance (1e-6 for programming checks, 5% for the `n₀*` locus, 1e-4 for same-model velocity), a second independent formulation (Chebyshev collocation vs analytic determinant) and a root-count record — this is stronger than any of the 16 papers, but the score stays at 4 until the checks actually run and pass. |
| 4 | **Validity of the size-effect model** | **2 / 5** | This is the weak point: the two loss channels only become comparable at `2h ≈ 10–250 nm` (computed `h*` in `checks/task0_scaling.md`), which is exactly where the MGT continuum heat model is least defensible (phonon mean free path comparable to the plate), where the free lengths `l_nl, l_g` have no sourced values, and where Shaat's critique (arXiv:1711.09938) bites hardest — so the size effect is being asked to work in the corner of the map where the rest of the model is shakiest. |
| 5 | **Device / application relevance** | **4 / 5** | The nulling protocol is a real measurable: the required drift field is `E = c_ph/μ_n ≈ 3.0 kV/cm` (attainable), and the Joule load `σE²` falls to ~3×10⁹ W/m³ at n₀ = 10¹⁹ m⁻³, i.e. below 1 W/cm² for a micrometre film — so the experiment proposed is not a thought experiment, though it only works at low doping. |
| 6 | **Reproducibility** | **5 / 5** | Fixed comparison points (`mode, fd, c_real, k_imag`), fixed tolerances, a parameter table with a source column and explicit `[U]` flags, two independent code paths, and the retained CSV/root-count logs — a referee can rerun everything, which none of the 16 papers can offer. |

**Weighted view:** strong on execution (17/20 across 3, 5, 6) and moderate on substance (7/10 across
1, 2), pulled down hard by one criterion (2/5) that is not about effort but about physics.

---

## Verdict: **GO** — conditional, with the refocus in `problem_v2.md` already applied

Not "REFOCUS", because the refocus has been done here: the published 2005 drift-amplification claim
is demoted to a tool, and the paper is re-anchored on screening-ordered attenuation channels.
Not "GO" unconditionally either: the go-ahead is tied to two cheap tests that must be run **before**
the scholar writes a page of the paper.

### GO conditions (both cheap, both at Step 4)
1. **C1 test.** Compute `k_i(n₀)` at fd = 1000 and 3000 Hz·m over n₀ = 10¹⁸–10²⁴ and confirm the
   curve is non-monotonic with the peak within 5% of `n₀* = ε₃₃ω/(eμ_n)`. If it is monotone, the
   ordering argument dies and the paper is a parameter study → **downgrade to Q2**.
2. **Floor-resolution test.** Confirm the thermal `k_i` is above the solver's resolution (say
   `k_i/k_r > 10⁻⁶`) at the thicknesses used for C2. If it is not, MGT is decoration →
   **downgrade to Q2** and keep MGT as a formulation remark.

### Single biggest risk
**The thermal floor is 213× weaker than the carrier peak, so the entire novel content lives in a
narrow corner of parameter space — high doping *or* a drift bias strong enough to null the carrier
channel, at a thickness where the continuum heat model is already suspect.** If a referee asks
"can you actually measure this?", the answer must be a number (the nulling field, the Joule load,
the resolution), not a promise. It has to appear in the paper as a short "measurability" section,
and if that section cannot be written with three numbers, the paper is not Q1.

### Runner-up risk
Thermal conductivity of ZnO spans **50× (1.2 vs 60 W/m·K)** between thin-film and bulk sources, and
it sets the floor peak frequency and the crossing thickness (`√50 ≈ 7×`). The finding must be shown
to survive both ends; if it only works with one, it is not a finding.

### What I would tell Sumit to do first
Run the C1 test above *before* the piezo step, on a reduced model (elastic + carriers only). It
takes a day and it decides whether this paper is worth three months.

---

## v3 rescore — after Route A (30 Oct 2026)

Re-scored against `paper/problem_v3_proposal.md`, i.e. **without** the thermal claim. The novelty cell
that matters is now **NSGT x carriers x complex `k` in a traction-free PSC plate**, not MGT x NSGT x PSC.

**Sweep re-run for the non-MGT cells.** A fresh check was run for this cell; the two closest neighbours
found are a 2025 *Appl. Math. Modelling* paper on **SH surface waves in a nanoscale PSC layered medium
with flexoelectricity, strain gradient, micro-inertia gradient and carrier-density attenuation**
(PII S0307904X25000034) and a 2025 *Sci. Rep.* NSGT piezoelectric nanoplate dispersion paper
(10.1038/s41598-025-01789-3). Both do size effects + carriers + attenuation; **neither** does a
traction-free Lamb plate, and neither treats the two NSGT lengths as an identifiability problem. The
cell is therefore **occupied at its edges but not at its centre**, which is weaker than v2's claim
("the cell is empty") and must be written that way.

| # | Criterion | v2 | **v3** | Why it moved |
|---|---|---|---|---|
| 1 | Novelty | 3 | **2** | Losing the MGT dimension removes half the empty cell; the 2025 SH-surface-wave paper already couples size effects, carriers and attenuation. |
| 2 | Physical insight | 4 | **3** | The "screening exposes a floor" ordering was the thermal-adjacent insight; what remains is the identifiability argument, which is methodological rather than physical. |
| 3 | Rigour | 4 | **4** | The `6x6` factorisation gate passed (`= 8.000000`, spread 4.3e-13) and S0 reproduces the analytic 5308.59 m/s to 1.7e-6 — but that is *my* code, not the scholar's yet. |
| 4 | Validity of the size-effect model | 2 | **3** | Route A removes the least defensible ingredient (a continuum heat model at 10 nm) from the corner of the map where the size effect must be claimed. `l_nl, l_g` remain unsourced. |
| 5 | Device relevance | 4 | **3** | The nulling/drift protocol survives, but without the thermal floor the "residual loss" story that made it a design target is thinner. |
| 6 | Reproducibility | 5 | **5** | Unchanged; fixed comparison points now include 100 and 250 Hz·m. |
| | **Total** | **22/30** | **20/30** | |

### Verdict: **GO — conditional**

GO, because the two remaining claims are cheap to test and the tests are decisive; not REFOCUS,
because the refocus has already been done (Route A). The conditionality is now entirely on C3.

**Single biggest risk:** C3 is a *hypothesis*, not a result. If the attenuation-peak locus turns out to
be insensitive to `l_nl/h` and `l_g/h` at the 1 % level, C3 collapses, the paper is C1 alone (one
mechanism, one figure), and the honest verdict becomes DOWNGRADE. **That test is the paper.**
