# Pre-Step-3 check (Sumit) — thermoelastic attenuation in an infinite medium, Fourier vs MGT

**Why this page exists.** Claim C2 says the thermal attenuation "falls under MGT and saturates under
Fourier". Before any Step-3 code is written, that statement must be derivable. Below is the analytic
high-frequency limit in an *infinite* medium (no plate, no boundary layers, no size effect). The
answer changes C2 — see §5. One page, no code.

Convention: `exp[i(kx−ωt)]`, real `ω`, complex `k`; `k_i > 0` decays.

## 1. Setup

Unbounded coupled thermoelastic medium, longitudinal (P) wave. Momentum and heat:

```
ρ ü_i = (λ+μ) u_j,ji + μ u_i,jj − β θ,i                     (1)
heat:  operator on [ρ c_p θ̇ + T₀ β ε̇_kk]  =  k_th ∇²θ        (2)
```

with `β = (3λ+2μ) α_T`, `κ = k_th/(ρ c_p)`, and the thermoelastic coupling parameter

```
Δ_E = T₀ β² / (ρ c_p (λ+2μ))      (dimensionless; the Zener parameter)
τ_T = κ / c_L²                   (s; thermal relaxation time over one wavelength/2π)
```

For a P wave, `ε_kk = u' = ik u` and (1)–(2) in the frequency domain give, to first order in `Δ_E`,
the correction to the elastic wavenumber. **Fourier case** (2) is `ρ c_p θ̇ + T₀β ε̇ = k_th∇²θ`:

```
k_i^F(ω) = (ω/c_L) (Δ_E/2) · (ω τ_T) / [1 + (ω τ_T)²]                        (3)
```

## 2. MGT case, Gupta form

The Gupta et al. form applies the relaxation to the whole bracket, i.e. (2) becomes

```
(1 + τ_q ∂/∂t) [ρ c_p θ̇ + T₀ β ε̇_kk] = k_th ∇²θ                              (4)
```

In the frequency domain `(1 + τ_q ∂_t) → (1 − i ω τ_q)`, so the *capacity and the coupling are
multiplied by the same factor* `A ≡ 1 − iωτ_q`. Repeating the algebra of §1 with `ρc_p → Aρc_p` and
`T₀β → AT₀β` gives

```
k_i^MGT(ω) = (ω/c_L) (Δ_E/2) · (ω τ_T) / [1 + ω²(τ_T − τ_q)²]                 (5)
```

**Eq. (5) is (3) with `τ_T` replaced by `τ_eff = τ_T − τ_q` in the width of the resonance, and with
the peak height kept proportional to `ωτ_T`.** This is the whole content of MGT in the bulk limit.

## 3. High-frequency limits — the answer to the question

| Model | `ω → ∞` behaviour of `k_i` | Peak position |
|---|---|---|
| Fourier | `→ Δ_E/(2 c_L τ_T)` — **saturates** | `ω = 1/τ_T` |
| MGT, eq. (5) | `→ (Δ_E/2c_L) · τ_T/(τ_T − τ_q)²` — **also saturates**, rescaled | `ω = 1/|τ_T − τ_q|` |

So: **MGT does not switch the thermoelastic floor off. It moves the peak and rescales the plateau.**
The plateau is *larger* than Fourier's when `|τ_T − τ_q| < τ_T`, i.e. `0 < τ_q < 2τ_T`, and returns to
the Fourier value at `τ_q = 2τ_T`. At `τ_q = τ_T` the width vanishes and the expansion diverges — the
second-sound resonance, where the first-order treatment breaks down and the model is not usable.

**Alternative placement, and why it must be rejected.** If instead `τ_q` multiplies only `θ̈`
(leaving the coupling unrelaxed), the same algebra gives
`k_i = (Δ_E/2)(ω/c_L)(τ_T−τ_q)ω/[1+ω²(τ_T−τ_q)²]`, which is **negative for τ_q > τ_T** — an
attenuation that grows the wave in a passive conductor. That placement is therefore physically
inadmissible, and it is the concrete reason to confirm that the Gupta equation is the
`(1 + τ_q∂_t)[…]` form (4) and not the `τ_qθ̈` form. **If Dr. Vipin's copy of Gupta et al. turns out
to be the second form, Step 3 stops and we discuss it.**

## 4. Numbers for ZnO (using the `[U]` constants already flagged in `problem_v2.md` §7)

`τ_T = k_th/(ρ c_p c_L²)` with `ρ = 5680`, `c_p = 500` (assumed), `c_L = 6095`:

| `k_th` | `τ_T` | Fourier peak frequency `1/(2πτ_T)` |
|---|---|---|
| 60 W/m·K (bulk) | `5.69×10⁻¹³` s | 280 GHz |
| 1.2 W/m·K (thin film) | `1.14×10⁻¹⁴` s | 14 THz |

Combined with `τ_q ∈ [10⁻¹³, 10⁻¹¹]` s: with `k_th = 1.2` **every** `τ_q` in the range exceeds `τ_T`
(so `τ_eff < 0`, plateau reduced, peak pushed to `1/|τ_eff|`); with `k_th = 60` the case `τ_q = 10⁻¹³`
is still below `τ_T` (Fourier-like) while `τ_q = 10⁻¹², 10⁻¹¹` are above. The two conductivity ends
therefore give **qualitatively different** MGT scenarios — which is exactly why the 50× spread in
`k_th` is the top-ranked sensitivity in the parameter plan.

## 5. What this does to C2 (it must be restated)

The draft C2 ("MGT falls, Fourier saturates") is **wrong in the bulk limit** and must be replaced by
the statement that the bulk test supports:

> **C2 (revised).** The thermoelastic floor does not disappear at high frequency in either model; it
> *plateaus*. MGT changes two observables: the plateau value,
> `(Δ_E/2c_L)·τ_T/(τ_T−τ_q)²` versus `Δ_E/(2c_Lτ_T)`, and the peak frequency,
> `1/|τ_T−τ_q|` versus `1/τ_T`. In a plate, `τ_T` is replaced by the through-thickness diffusion time
> `τ_th = (2h)²/(π²κ)`, so the peak position becomes a function of thickness and is the quantity to
> measure. The discriminating signature is **the peak shift**, not a change of slope.

Consequence for the paper: C2's figure must plot the *peak position vs thickness* (both models, with
`τ_q` as a parameter) rather than "slope at high fd". Claims about MGT "switching the floor off" are
withdrawn before they reach a draft.

## 6. Gates this page imposes on Step 3

1. Implement (3) and (5) in `code_arena/` as standalone formulae (ten lines) — they are the reference
   against which the plate code's thermal channel is judged.
2. The plate code, in the limit of large `kh` where the lowest modes become bulk-like, must approach
   (3)/(5) in trend; **report the difference and the `kh` at which it was measured**, and do not claim
   a pass unless the `kh` used is stated (the trust window stops near `kh ≈ 3`, so this is a trend
   check, not a tolerance check).
3. Check the low-frequency limit `k_i ∝ ω²` for both models — they must agree there to 1e-6, since
   `τ_q` cannot matter at `ωτ_q ≪ 1`.
4. Confirm the placement in (4) against Gupta et al. before coding.
