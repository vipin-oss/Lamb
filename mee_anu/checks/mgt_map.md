# MGT distinguishability — BaTiO₃/CoFe₂O₄ MEE plate (Anu), one table

Same construction as the Sumit and Neha maps: boundary `(2h)* = π√(D τ_q)` from `τ_th = (2h)²/(π²D)`;
band = {B1 `kh ≤ 3`} ∩ {B2 `2h ≥ 10Λ_ph`} ∩ {B3 peak `fd_peak = πD/(2·2h)` inside `fd ∈ [500, 5000]`
Hz·m}.

## Constants (better sourced than Neha's, because two of them are measured)

| constant | value | source | status |
|---|---|---|---|
| BaTiO₃ `ρ` | 5.84 and 5.94 g/cm³ (two suppliers) | *Heat capacity, thermal conductivity and thermal expansion of BaTiO₃-based ceramics*, Elsevier PII S0040603104000942 | **measured**, DOI unresolved (PII link) |
| BaTiO₃ `c_p` | **0.41–0.43 J/(g·K)** at room temperature | same paper | **measured** |
| CoFe₂O₄ `D` | **0.52 mm²/s = 5.2×10⁻⁷ m²/s** at room temperature | *J. Mater. Sci.: Mater. Electron.* (2023) [10.1007/s10854-022-09777-3](https://doi.org/10.1007/s10854-022-09777-3), hot-disk | **measured** |
| CoFe₂O₄ `k_th` | 0.6 W/(m·K) (Cu-doped sample 0.95) | same paper | **measured** |
| CoFe₂O₄ volumetric heat | 0.62–0.72 MJ m⁻³K⁻¹ | same paper | **measured** |
| BaTiO₃ `D` | 1.21×10⁻⁶ m²/s — from `k_th = 3` W/m·K (assumed), the measured `ρ c_p` | `k_th` **not sourced** | `[U]` for `k_th` only |
| `Λ_ph` | not sourced for either phase | — | `[U]` |

## The map

| phase | `D` (m²/s) | `(2h)*` at `τ_q = 10⁻¹³` | `10⁻¹²` | `10⁻¹¹` | `τ_th` at 10 nm | at 50 nm | `fd_peak` at 10 nm |
|---|---|---|---|---|---|---|---|
| CoFe₂O₄ | **5.20×10⁻⁷** (measured) | 0.72 nm | 2.27 nm | 7.16 nm | 1.95×10⁻¹¹ s | 4.87×10⁻¹⁰ s | 82 Hz·m |
| BaTiO₃ | 1.21×10⁻⁶ | 1.09 nm | 3.46 nm | 10.94 nm | 8.35×10⁻¹² s | 2.09×10⁻¹⁰ s | 191 Hz·m |
| composite (mean) | 3.5×10⁻⁷ | 0.59 nm | 1.86 nm | 5.88 nm | 2.89×10⁻¹¹ s | 7.24×10⁻¹⁰ s | 55 Hz·m |

## Verdict — **MGT is outside the trust band**

1. **B3:** to put the thermal peak in `[500, 5000]` Hz·m needs `2h ≈ 0.16–1.6 nm` (CoFe₂O₄) — far
   below any continuum plate, and ~100× thinner than the plate the ridge test uses.
2. **B2:** both oxides are poor conductors with short MFPs (`Λ_ph ~ 1–5 nm`), so `2h ≥ 10Λ_ph ≈ 10–50 nm`,
   where the measured CoFe₂O₄ diffusivity gives `τ_th ≥ 2×10⁻¹¹ s`, i.e. **above the top of the `τ_q`
   range**. MGT is then a correction of order `τ_q/τ_th ≤ 0.5`, and at 50 nm `≤ 0.02`.
3. Both constraints together: the intersection is empty. Note this is *worse* than Neha's case because
   `D` is smaller (measured), not larger.

**Consequence for the paper.** MGT stays in the formulation and leaves every claim. The paper already
carries one major upgrade (the frequency-dependent ME ridge) that does not need MGT to exist — good,
because it does not have it. Recommendation: **one labelled figure at most**, showing that the MGT and
Fourier curves are indistinguishable at the measured `D`; that figure is worth more than a claim,
because it pre-empts the referee question "why is the heat model so elaborate?".

**To be fixed by the scholar:** a sourced `Λ_ph` for BaTiO₃ and CoFe₂O₄ and a sourced `k_th` for
BaTiO₃ (the only `[U]` in the table). Neither is expected to move the verdict; the margin in B2 is
`≥ 2×` and in B3 is `≥ 100×`.
