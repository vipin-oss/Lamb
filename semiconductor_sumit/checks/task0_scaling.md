# Task-0 scaling check (feasibility, not a model result)

Script: `code_arena/task0_feasibility_scaling.py` — run `python3 task0_feasibility_scaling.py`.
This is a leading-order algebraic check used **only** to decide whether the proposed hook is
physically reachable before the scholar is committed to it. It is not a dispersion calculation and
it must never be cited in the paper.

Material: ZnO, T = 300 K. Constants and their status are listed in `paper/problem_v2.md` §7.
Three of them (`c_p`, `α_T`, `τ_q`) are still `[U]` (no source); they enter only through the Zener
group and are labelled in the output.

## Results

| Quantity | Value | Comment |
|---|---|---|
| Bar velocity `√(c₃₃/ρ)` | 6095 m/s | consistent with ZnO literature scale |
| Piezoelectric coupling `K² = e₃₃²/(c₃₃ε₃₃)` | **0.076** | computed from sourced constants, not quoted |
| Max acoustoelectric loss `k_i/k_r ≈ K²/2` | **3.8×10⁻²** | Hutson–White estimate |
| Zener parameter `Δ_E = c₃₃α_T²T/(ρc_p)` | 3.6×10⁻⁴ | `[U]` constants — indicative |
| Zener/TED floor `k_i/k_r ≈ Δ_E/2` | **1.8×10⁻⁴** | `[U]` constants — indicative |
| **Ratio carrier peak / thermal floor** | **213×** | the number the hook depends on |

**Carrier peak locus** `n₀*(f) = ε₃₃ω/(eμ_n)`:

| f | n₀* (m⁻³) | fd at 2h = 1 µm | fd at 2h = 100 µm |
|---|---|---|---|
| 1 MHz | 2.2×10¹⁷ | 1 | 100 |
| 100 MHz | 2.2×10¹⁹ | 100 | 10⁴ |
| 1 GHz | 2.2×10²⁰ | 10³ | 10⁵ |
| 10 GHz | 2.2×10²¹ | 10⁴ | 10⁶ |

The locus is material-set and linear in fd — doping tunes it, thickness does not. Note that the
fixed comparison points of `docs/02_workflow_crosscheck.md` (fd = 500…5000) sit on this line at
n₀ ≈ 10²⁰–10²¹ m⁻³, i.e. inside the planned sweep 10¹⁸–10²⁴. **Good: the comparison points are not
in a dead corner.**

**Thermal (TED) peak**, `f_th = πα/(2(2h)²)`, both conductivity ends:

| 2h | f_th (k=1.2) | fd_th | f_th (k=60) | fd_th |
|---|---|---|---|---|
| 10 nm | 6.6 GHz | 66 | 332 GHz | 3319 |
| 100 nm | 66 MHz | 6.6 | 3.3 GHz | 332 |
| 1 µm | 664 kHz | 0.66 | 33 MHz | 33 |
| 10 µm | 6.6 kHz | 0.066 | 332 kHz | 3.3 |

**Crossing thickness** where the two peaks coincide, `h* = (π/2)√(αε/(n₀eμ)) = (π/2)L_D√(Le)`
(verified in the script to 3 digits — the second form is useful in the paper because it says the
crossing thickness *is* the Debye length amplified by the Lewis-number ratio):

| n₀ | h* (k=1.2) | h* (k=60) | L_D |
|---|---|---|---|
| 10²⁰ | 19 nm | 135 nm | 425 nm |
| 10²¹ | 6.0 nm | 43 nm | 134 nm |
| 10²² | 1.9 nm | 13 nm | 42 nm |

**Nulling bias and Joule load:** `E_null = c/μ_n = 3.0×10⁵ V/m = 3.0 kV/cm`;
`σE² = 3.2×10⁹ W/m³` at n₀ = 10¹⁹ (≈ 3 kW/m² through a 1 µm film = 0.3 W/cm²), rising to
3.2×10¹² W/m³ at n₀ = 10²². So the nulling experiment is thermally comfortable at low n₀ and
increasingly unreasonable above ~10²¹ m⁻³ — which is the same regime the floor needs.

## What this changes in the plan

1. The two channels are **not comparable**; the honest claim is ordered (peak vs floor), not
   competitive. `problem_v2.md` is written that way.
2. `h* ≈ 6–135 nm` means the two-peak coincidence lives at nanometre plates — the NSGT domain, but
   also the domain where the MGT continuum heat model is weakest. This is why size-model validity
   is scored 2/5 in `q1_scorecard.md` and why the trust window is a hard requirement on figures.
3. The 50× spread in `k_th` moves `h*` by ≈7×; both ends must be plotted.
4. The fixed comparison points are inside the physically interesting region — no changes to
   `docs/02_workflow_crosscheck.md` are needed.

## Caveats (must travel with these numbers)
- TED formula used is the thin-plate flexural (Zener/Lifshitz–Roukes) peak, `ω = π²α/(2h)²`; the true
  peak for a Lamb mode at finite `kh` differs by an `O(1)` factor and by mode shape. The script
  checks **scaling and existence**, not peak values.
- `c_p` and `α_T` have no source yet, so `Δ_E` (and therefore the 213×) is indicative; the
  *order of magnitude* is what matters and it would need a factor-200 error to disappear.
- No NSGT, no piezoelectric stiffening, no mode structure in this script. Those are Steps 2–6.
