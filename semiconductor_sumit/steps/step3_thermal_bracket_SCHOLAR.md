# Step 3 (Sumit) — the adiabatic / isothermal bracket
## 1. The two limits, stated exactly

Coupled thermoelasticity, linearised:

```
σ_ij = c_ijkl ε_kl − β_ij θ ,   ρ c_p θ̇ = −T₀ β_ij ε̇_ij − q_i,i ,   q_i = −k_th θ,i          (1)
```

| limit | assumption | consequence in the frequency domain |
|---|---|---|
| **isothermal** | `k_th → ∞`: heat flows instantly, `θ ≡ 0` | the `θ` term drops out; the elastic constants are the **isothermal** `c^T` |
| **adiabatic** | `k_th → 0`: no heat flow between material points, `q_i = 0` | `θ` is slaved to the strain: `ρc_p θ = −T₀β_ij ε_ij`, i.e. **stiffened** constants |

The adiabatic stiffening is exact and rank-one:

```
c^ad_ijkl = c^T_ijkl + (T₀ / ρ c_p) β_ij β_kl                                             (2)
```

For the `6mm` plate this means `c₁₁^ad = c₁₁ + T₀β₁²/(ρc_p)`, `c₃₃^ad = c₃₃ + T₀β₃²/(ρc_p)`,
`c₁₃^ad = c₁₃ + T₀β₁β₃/(ρc_p)`, and **no change to `c₄₄`** (`β₅ = 0`), so shear modes are unaffected.
`β₁ = (c₁₁+c₁₂)α_⊥ + c₁₃α_z`, `β₃ = 2c₁₃α_⊥ + c₃₃α_z`.

**Both limits use the same plate code**, with `c^ad` or `c^T` substituted and the piezoelectric block
untouched. No heat equation is solved anywhere in Step 3.

## 2. Bracket width — what it actually bounds

| quantity | bracket | width |
|---|---|---|
| phase velocity of any mode | `[c_iso, c_ad]` | `δc/c ≈ ½Δ_E` = **3.1×10⁻³** |
| **attenuation** `k_i^th` | **both ends give exactly 0** | the bracket is degenerate here |

The second row matters and must not be glossed over: **the two limits are lossless**. Thermoelastic
damping requires a finite relaxation time, i.e. heat flow that is neither instantaneous nor absent. So
the velocity is bracketed tightly, and the attenuation is bounded instead by the *peak* of the
intermediate regime — the classical Zener value, which §3 computes independently.

`Δ_E` for ZnO with the Set-L constants and `α_⊥ = 6.5×10⁻⁶`, `α_z = 3.0×10⁻⁶ K⁻¹`
(`[U]` — thermal expansion, the one constant that moves `Δ_E`),
`ρc_p = 2.84×10⁶ J m⁻³K⁻¹` (`c_p = 500` also `[U]`):

```
β₁ = 2.466×10⁶ Pa/K ,  β₃ = 2.004×10⁶ Pa/K
Δ_E = T₀β₁²/(ρc_p c₁₁) = 3.06×10⁻³   (2.01×10⁻³ from β₃)
```

## 3. The classical thermoelastic check against the bulk note, eq. (3)

The bulk note gives `k_i(ω) = (ω/c)(Δ_E/2)·ωτ_T/[1+(ωτ_T)²]` (eq. 3 there). For a plate the relaxation
time is not `τ_T = κ/c_L²` but the **through-thickness diffusion time**

```
τ_th = (2h)²/(π²κ)                                                                         (3)
```

so the peak sits at `ω = 1/τ_th`, i.e. `fd_peak = πκ/(2·2h) = 251.4 Hz·m` at `2h = 132 nm`, and

```
k_i^peak = Δ_E / (4 c τ_th) = 1.83×10³ m⁻¹  ⇒  k_i/k_r = 7.7×10⁻⁴                             (4)
```

(c = 5000 m/s at that `fd`). Eq. (4) is the number the Step-3 code must reproduce, and the `k_i/k_r`
ratio 7.7×10⁻⁴ is consistent with the `1.8×10⁻⁴` floor quoted in the scorecard — same order, as it
must be.

**This is a TREND check, not a tolerance check, and `kh` must be stated wherever it is used.** The
plate result approaches (3) only for `kh ≳ 1` in the sense that the mode must "see" the thickness; at
small `kh` the plate is a thin wave-guide and the bulk formula has no meaning. Report, for each point,
`(kh, k_i^plate, k_i^eq3, ratio)` and state the `kh` at which the ratio is within 20 %.

## 4. Fixed comparison points

```
fd [Hz·m] = 20, 100, 250, 500, 1000, 3000, 5000
```

`100` and `250` are mandatory: the thermal peak for `2h = 132 nm` sits at **251 Hz·m**, and a grid
starting at 500 would miss the only place where the thermal effect is largest. At `2h = 132 nm` the
`kh` values span 0.04–9.5; **flag every point with `kh > 3` as outside the trust band** and keep the
numbers anyway, labelled.

## 5. Pass criteria

| # | Check | Expected | Tolerance |
|---|---|---|---|
| 1 | `β = 0` (no thermal coupling): the two limits coincide | identical root sets | **< 1×10⁻⁶** (hard gate) |
| 2 | `k_i` from the bracket at `β = 0` | 0 exactly | absolute |
| 3 | Bracket ordering | `c_iso ≤ c ≤ c_ad` for every mode, every `fd` | sign test, all roots |
| 4 | Bracket width on S0 at `fd = 500` | `δc/c = 3.1×10⁻³` ± 20 % | 20 % |
| 5 | Peak position | `fd_peak = πκ/(2·2h)`; at `2h = 132 nm` → **251 Hz·m** | < 5 % |
| 6 | Peak value | eq. (4): `k_i^peak = 1.83×10³ m⁻¹` at `2h = 132 nm` | trend, `kh` stated |
| 7 | `A0` unaffected by thermal coupling | `c₄₄` has no `β₅`, so the shear-dominated branch moves by < 1×10⁻⁴ | 1×10⁻⁴ |
| 8 | No new roots | root counts identical to Step 2 at each `fd` | exact count |

