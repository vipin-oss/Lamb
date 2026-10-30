# MGT distinguishability — quasicrystal plate (Neha), one table

Same construction as `semiconductor_sumit/steps/step3_prerecheck_mgt_map.md`: the models separate only
through the through-thickness diffusion time `τ_th = (2h)²/(π²D)`, `D = k_th/(ρ c_p)`, with boundary
`(2h)* = π√(D τ_q)`. Band = {B1 `kh ≤ 3`} ∩ {B2 `2h ≥ 10Λ_ph`} ∩ {B3 peak `fd_peak = πD/(2·2h)` inside
the swept `fd ∈ [500, 5000]` Hz·m}.

## Constants

| constant | value | source | status |
|---|---|---|---|
| `ρ` (d-Al–Co–Ni) | ≈ 4.1–4.7 g/cm³ | not resolved in this check | `[U]` |
| `c_p` | ≈ 0.5–0.7 J/(g·K) at 300 K | *J. Alloys Compd.* (2002), PII S0925838802001974 — abstract confirms `C_p(5–300 K)` was measured but the value is behind the paywall | `[U]` (value unread) |
| `k_th` (d-Al–Co–Ni, 300 K) | **not resolved**; quasicrystals are poor conductors, `O(1–4)` W/m·K | PRB **58** 3046 (1998) [10.1103/PhysRevB.58.3046](https://doi.org/10.1103/PhysRevB.58.3046) and PRB **68** 104202 (2003) [10.1103/PhysRevB.68.104202](https://doi.org/10.1103/PhysRevB.68.104202) give low-T and 373–873 K transport; **no 300 K number was read** | `[U]` — **must be taken by the scholar** |
| `D` used below | **1×10⁻⁶ m²/s** (central), spread 5×10⁻⁷–2×10⁻⁶ | from `k_th ≈ 1–4`, `ρ c_p ≈ 2–2.5 MJ m⁻³K⁻¹` | `[U]` by construction |

Because `D` is a guess, the table is built to show that **the verdict does not depend on it** over a
4× range of `D`.

## The map (no code beyond these ten lines of arithmetic)

| `D` (m²/s) | `(2h)*` at `τ_q = 10⁻¹³` | `10⁻¹²` | `10⁻¹¹` | `τ_th` at 10 nm | at 100 nm | `fd_peak` at 10 nm |
|---|---|---|---|---|---|---|
| 5×10⁻⁷ | 0.70 nm | 2.22 nm | 7.02 nm | 2.03×10⁻¹¹ s | 2.03×10⁻⁹ s | 79 Hz·m |
| **1×10⁻⁶** | **0.99 nm** | **3.14 nm** | **9.93 nm** | **1.01×10⁻¹¹ s** | **1.01×10⁻⁹ s** | **157 Hz·m** |
| 2×10⁻⁶ | 1.40 nm | 4.44 nm | 14.05 nm | 5.07×10⁻¹² s | 5.07×10⁻¹⁰ s | 314 Hz·m |

## Verdict — **MGT is outside the trust band**

Three independent reasons, each sufficient:

1. **B3 alone excludes it.** The thermal peak sits at `fd_peak = πD/(2·2h)`. To place it inside
   `[500, 5000]` Hz·m requires `2h = 0.3–3.1 nm` (at `D = 10⁻⁶`), i.e. the peak is only reachable at
   thicknesses two orders of magnitude below the plate.
2. **B2 alone excludes it.** With `Λ_ph ≈ 1–2 nm` for a quasicrystal (short MFPs are what make `k_th`
   low), `2h ≥ 10Λ_ph ≈ 10–20 nm`, and at those thicknesses `τ_th ≥ 10⁻¹¹ s ≥ τ_q` for the whole
   literature range: the MGT correction is `O(τ_q/τ_th) ≤ 1`.
3. **The intersection is empty for every `D` in the 4× spread.** `(2h)*` never exceeds 14 nm, while
   B2 demands ≥ 10 nm *and* B3 demands ≲ 3 nm.

**Consequence for the paper.** MGT cannot be the discriminator. The heat equation should be carried as
MGT in the formulation (to match the group's earlier papers) but **no claim, figure title or abstract
may rest on the relaxation time**; one labelled comparison figure at most, exactly like the
"NSGT-on-phason is a Step-5 sensitivity only" ruling. The honest statement is quantitative:
`ωτ_q ≪ 1`, so MGT reduces to Fourier at every admissible point, and the paper should say so with the
numbers above rather than implying a thermal-wave effect.

**To be fixed by the scholar before this table is final:** a sourced `k_th` at 300 K for the actual
composition and `c_p` at 300 K. Neither changes the verdict unless `D` exceeds ~10⁻⁴ m²/s, which no
quasicrystal does.
