# Pre-Step-3 note (Sumit) — MGT distinguishability map in the (2h, τ_q) plane

**Purpose.** Decide, before any Step-3 code, whether MGT can be distinguished from Fourier conduction
*anywhere in the thickness band the paper is allowed to claim*. If the answer is no, MGT leaves the
title and becomes a formulation remark. One page, analytic, no code.

Companion page: `steps/step3_prerecheck_bulk_medium.md` (the bulk limit that C2 now rests on).

## 1. The single condition

From the bulk/plate analysis, MGT and Fourier differ only through the **plate thermal time**

```
τ_th(2h) = (2h)² / (π² κ) ,      κ = k_th/(ρ c_p)                                   (1)
```

The two models have the same low-frequency behaviour and separate only when
`τ_q ⋍ τ_th` — the boundary being (from `2h*(τ_q)`: set `τ_th = τ_q`)

```
(2h)* = π √(κ τ_q)                                                                 (2)
```

*Above* the curve (2) in the `(2h, τ_q)` plane, `τ_th > τ_q`: Fourier-like, the MGT correction is
`O(τ_q/τ_th)` and is not resolvable. *Below* it, `τ_q > τ_th`: the MGT plateau rescaling
`τ_th²/(τ_th−τ_q)²` and the peak shift `1/τ_th → 1/|τ_th−τ_q|` are both large, and the floor moves
away from the Fourier value by an amount the solver can see. The boundary is a straight line of slope ½
in log–log coordinates, shifted by `√κ`.

## 2. The trust band

A point `(2h, τ_q)` is inside the band only if **all three** hold:

| # | Constraint | Why | Consequence for `2h` |
|---|---|---|---|
| B1 | `kh ≤ 3` (and `kh ≳ 0.1`) | continuum + NSGT validity; trust window stops near `kh ≈ 3` (Step-1 pack §6) | upper bound on `fd` |
| B2 | `2h ≥ 10 Λ_ph` | Fourier conduction requires many phonon mean free paths; below this the nonlocal/ballistic regime voids the heat equation itself | `2h ≥ 10Λ_ph` |
| B3 | the TED peak `fd_peak = πκ/(2·2h)` lies inside the swept window `fd ∈ [500, 5000]` Hz·m | a peak outside the window is not an observable | brackets `2h` from both sides |

**B3 in closed form.** `fd_peak = πκ/(2·2h)`, so the window `[500,5000]` accepts

```
2h ∈ [ πκ/10⁴ , πκ/10³ ]                                                        (3)
```

`πκ = 6.637×10⁻⁵` m²/s at `k_th = 60`, `1.328×10⁻⁶` m²/s at `k_th = 1.2`. Between B1 and B3 there is
a pleasant coincidence worth recording: for ZnO at `k_th = 60` the window (3) maps exactly onto
`kh ∈ [0.26, 2.58]`, i.e. **B3 is inside B1**. So B1 does not bind here; B2 and B3 do.

## 3. The map

`ρ = 5680 kg/m³`, `c_p = 500 J/kg·K` (**assumed, `[U]`** — the scholar must supply a sourced value;
`κ` is linear in `1/c_p`, so a different `c_p` rescales every number below by that ratio).

**Boundary (2), `(2h)*` in nm:**

| `τ_q` (s) | `k_th = 60` W/m·K | `k_th = 1.2` W/m·K |
|---|---|---|
| `1×10⁻¹³` | 4.57 | 0.65 |
| `1×10⁻¹²` | 14.44 | 2.04 |
| `1×10⁻¹¹` | 45.66 | 6.46 |

**Band by B3 (3), `2h` in nm:**

| `k_th` (W/m·K) | `κ` (m²/s) | `2h` from B3 |
|---|---|---|
| 60 | 2.11×10⁻⁵ | **6.6 – 66.4** |
| 1.2 | 4.23×10⁻⁷ | **0.13 – 1.33** |

**Now overlay B2.** `Λ_ph` is **not sourced** — it is carried as a parameter, and the paper must not
quote a number for it without a reference. With `Λ_ph = 2, 5, 10` nm:

| `k_th = 60` | `2h ≥ 10Λ_ph` | surviving `2h` | `τ_th` at the band edges | boundary (2) inside band? |
|---|---|---|---|---|
| `Λ_ph = 2 nm` | ≥ 20 nm | 20 – 66 nm | 1.9×10⁻¹² – 2.1×10⁻¹¹ s | **yes** for `τ_q ≥ 1.9×10⁻¹²` s |
| `Λ_ph = 5 nm` | ≥ 50 nm | 50 – 66 nm | 1.2×10⁻¹¹ – 2.1×10⁻¹¹ s | **only** for `τ_q ≈ 1.2×10⁻¹¹` s |
| `Λ_ph = 10 nm` | ≥ 100 nm | **empty** | — | **no** |

| `k_th = 1.2` | `Λ_ph ≳ 0.013` nm | empty: B3 caps `2h ≤ 1.33` nm, far below `10Λ_ph` | — | **no** |

## 4. Verdicts (this is the decision the note exists to force)

- **`k_th = 1.2` W/m·K (thin film): MGT is not distinguishable anywhere in the band.** B3 caps
  `2h ≤ 1.33` nm, which is below any phonon mean free path and below the continuum limit, and above
  `10Λ_ph` the thermal time is `≥ 10⁻¹⁰` s, i.e. `τ_q/τ_th < 0.1` for every `τ_q` in range. The MGT
  correction is then a few per cent *of the floor*, itself already the smallest term in `k_i`.
- **`k_th = 60` W/m·K (bulk): MGT is distinguishable only if `Λ_ph ≤ 2` nm and `τ_q ≳ 2×10⁻¹²` s**
  (general form: `τ_q ≥ (10Λ_ph)²/(π²κ)`, since B3's upper edge `πκ/10³` never binds inside
  `τ_q ≤ 10⁻¹¹` s),
  both sourced. With `Λ_ph = 5` nm it survives only at the very top of the `τ_q` range
  (`≈1.2×10⁻¹¹` s). With `Λ_ph = 10` nm it is gone.
- Note the direction of the argument: **the thinner the plate, the fewer mean free paths**, so the
  band where MGT matters is exactly the band where Fourier conduction is least defensible. That
  tension is the honest statement of the difficulty, and it belongs in the paper regardless of title.

## 5. The rule, and the proposed retitle

> **Rule.** MGT may appear in the title **only if** the boundary `(2h)* = π√(κ τ_q)` lies inside the
> trust band for at least one **sourced** pair `(k_th, τ_q)` with a **sourced** `Λ_ph`. The pair must
> be quoted with its source in the title's supporting paragraph — not as a range.

Applying the rule to what is currently sourced:

| case | boundary inside band? | title |
|---|---|---|
| `k_th = 60`, `τ_q ≥ 2×10⁻¹²` s, `Λ_ph ≤ 2` nm — **all sourced** | yes | **keep MGT in the title** |
| `k_th = 1.2` (thin film) with any `τ_q` in range | no | **retitle** |
| `k_th = 60` but `Λ_ph` unsourced, or `τ_q ≤ 10⁻¹³` | unresolved | hold; MGT in the subtitle at most |

**Proposed retitle if the rule fails** (C1 and C3 are untouched by it; both survive on their own):

> *Screening-threshold attenuation and strain-gradient dispersion in thin piezoelectric semiconductor
> plates* — with MGT retained as "a thermal-relaxation sensitivity of the residual floor" in a
> closing subsection, and figure F6 demoted to an appendix.

This keeps the two claims that do not depend on `τ_q` (C1 carrier screening, C3 two-observable
separation of the strain-gradient scales) and removes the one that a reviewer would test first.

## 6. What must be sourced before Step 3 starts

1. `c_p` and `α_T` for ZnO, with a reference (currently assumed; `κ ∝ 1/c_p`).
2. `Λ_ph` for ZnO at 300 K, with a reference — **this number alone decides the title.**
3. `k_th` at the actual film thickness, with a reference; if only the bulk value is available, the
   thin-film end cannot be used and the `k_th = 1.2` column becomes a sensitivity, not a case.
4. `τ_q` with a reference; the band `10⁻¹³–10⁻¹¹` s is a range, and the rule above does not accept a
   range as the basis of a title.
