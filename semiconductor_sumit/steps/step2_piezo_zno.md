# Step 2 (Sumit) — Piezoelectric plate: open/short faces, `K²`, and the coupling-off check

**Goal.** Add the piezoelectric coupling to the Step-1 elastic plate, define the electrical boundary
conditions exactly, and fix the quantity `K²(fd)` that Steps 3–5 will report. The step is passed when
the coupling can be switched off and Step 1 returns bit-for-bit.

Conventions unchanged: `exp[i(kx−ωt)]`, thickness `2h`, faces `z = ±h`, plane strain (`u_y = 0`,
`∂/∂y = 0`), `k = k_r + i k_i`, `k_i > 0` decaying, `fd = f·2h`.

## 1. Geometry and the poling axis — state it, do not assume it

The plate is ZnO wurtzite, **poled along `z`** (the 6-fold `c` axis normal to the faces), propagation
along `x` in the plane of the plate. This is a **thickness-poled** plate: the electrodes are on the
faces and the potential is a function of `(x, z)`, not of `z` alone. Both `E_1` and `E_3` therefore
appear, and the full `6mm` set is needed — the "1D thickness mode" shortcuts are **not** available.

If the group's sample is **in-plane poled** (poling along `x`), the constant matrix is the same but its
indices rotate: `e_31 → e_33`, `e_33 → e_31`, `ε_11 ↔ ε_33`. **This must be confirmed before Step 3**;
it changes `K²` by a factor of several and every later number with it.

## 2. Constitutive equations (`6mm`, poling `z`)

```
σ_1 = c_11 S_1 + c_12 S_2 + c_13 S_3 − e_31 E_3
σ_3 = c_13 S_1 + c_13 S_2 + c_33 S_3 − e_33 E_3
σ_5 = c_44 S_5 − e_15 E_1
D_1 = e_15 S_5 + ε_11 E_1 ,     D_3 = e_31(S_1+S_2) + e_33 S_3 + ε_33 E_3
E_1 = −φ,_x ,   E_3 = −φ,_z ,   σ_ij,j = ρ ü_i
```
(indices 1=x, 2=y, 3=z, 5=xz; `S_2 = 0` for plane strain; `S_1 = u_x,x`, `S_3 = u_z,z`,
`S_5 = u_x,z + u_z,x`.)

With `(u_x, u_z, φ) ∝ e^{i(kx−ωt)}` this is a **6×6 algebraic system in `z`** whose determinant gives
the piezoelectric Rayleigh–Lamb equations. Do **not** try to write one closed-form dispersion equation
in `p`, `q`; the accepted working form is the coupled system.

## 3. Electrical boundary conditions — exactly two, both must be run

| set | condition on the faces `z = ±h` | meaning |
|---|---|---|
| **open circuit** | `D_z(x, ±h) = 0` | charge-free faces, the physically usual case for a free plate |
| **short circuit** | `φ(x, ±h) = 0` | faces metallised and connected, the usual *drive* case |

Mechanical conditions are unchanged: `σ_zz = σ_xz = 0` at `z = ±h`.

**Note on a common error:** "open circuit" is *not* `φ = 0` and it is *not* `D_z = const ≠ 0`. It is
`D_z = 0`, which is what makes the potential respond to the strain and stiffens the plate.

## 4. The coupling coefficient `K²` — definition, once, for every later step

Define the **mode-wise effective coupling** at fixed `fd`:

```
K²(fd) = 1 − [ c_short(fd) / c_open(fd) ]²  =  (c_open² − c_short²) / c_open²                    (2)
```

for the *same* branch (same family, same mode number, followed by continuity — never by sorting).
`K² ≥ 0` because the open-circuit plate is the stiffer one. `K²` is a property of the **mode** at a
given `fd`, not a material constant; the material constants are its limits:

- thin-plate extensional limit, `fd → 0` for S0: `K² → ē₃₁²/(ε̄₃₃ c̄₁₁ + ē₃₁²)`, with
  `c̄₁₁ = c₁₁ − c₁₃²/c₃₃`, `ē₃₁ = e₃₁ − c₁₃e₃₃/c₃₃`, `ε̄₃₃ = ε₃₃ + e₃₃²/c₃₃`;
- thickness-extensional limit: `k_t² = e₃₃²/(c₃₃^D ε₃₃^S)`, `c₃₃^D = c₃₃ + e₃₃²/ε₃₃`.

## 5. Pass criteria for this step

All values below computed by me from the constants in §6 with the plane-stress reduction above.
**They are my numbers, not literature values** — the two literature cross-checks are in the last column
and are labelled as such.

| # | Check | Expected value | Tolerance |
|---|---|---|---|
| 1 | **coupling off** (`e_ij = 0`): open and short give the *same* root set | identical to < 10⁻⁶ relative | **hard gate** |
| 2 | coupling off, `fd → 0`, S0 | `√(c̄₁₁/ρ)` = **4964.83 m/s** | rel. < 10⁻⁴ |
| 3 | coupling off **and** isotropic constants (aluminium, `λ = μ`-set of Step 1) | **5393.9 m/s** = Step 1's S0 limit (check that the reduction is consistent: `√(c̄₁₁/ρ_Al)` = 5393.93 vs 5393.91, 4×10⁻⁶) | rel. < 10⁻⁴ |
| 4 | `fd → 0`, S0, **short** circuit | **4964.83 m/s** | rel. < 10⁻³ |
| 5 | `fd → 0`, S0, **open** circuit | **5214.83 m/s** | rel. < 10⁻³ |
| 6 | `K²(fd → 0)` for S0 | **0.09358** (⇔ `k₃₁ = 0.3059`) | abs. < 1×10⁻³ |
| 7 | `K² → 0` as `e²` | halving every `e_ij` gives `K²/4` | rel. < 10⁻³ |
| 8 | open velocity > short velocity, on every branch, every `fd` | sign test, all roots | absolute |
| 9 | Thickness-mode limit | `k_t² = 0.0707` (`k_t = 0.2658`) recovered to < 3 % from the cut-off behaviour of the first thickness mode | 3 % (small-`kh` expansion is not exact) |
| 10 | Root counts | record them; they must **not** be assumed to equal Step 1's — the effective stiffness changes, so the cut-offs move. Report the new cut-off list | recorded, not tested |

**Literature cross-checks (not my numbers).** `k₃₁ ≈ 0.30` and `k_t ≈ 0.27` are the commonly quoted
ZnO values; my derived 0.3059 and 0.2658 agree to ~2 %, which is a consistency check on the constants,
**not** a validation of the code. Do not quote a source for these numbers until Sumit supplies one.

## 6. Constants (ZnO, wurtzite)

| constant | value | source | status |
|---|---|---|---|
| `c₁₁, c₁₂, c₁₃, c₃₃, c₄₄` | 206, 118, 118, 211, 44 GPa | arXiv:cond-mat/0507217v2, measured row | sourced (as in v2 §7) |
| `e₃₃, e₃₁, e₁₅` | 1.34, −0.57, −0.48 C/m² | same | `e₁₅` value **to be confirmed** by Sumit |
| `ε₁₁, ε₃₃` | 9.16ε₀, 12.64ε₀ | eFunda ZnO | sourced |
| `ρ` | 5680 kg/m³ | eFunda ZnO | sourced |
| derived `c̄₁₁, ē₃₁, ε̄₃₃` | 140.0095 GPa, −1.31938 C/m², 1.20427×10⁻¹⁰ F/m | §4 reduction | computed |

**Note on `ε`: `ε^S` versus `ε^T`.** The `9.16/12.64` values are the **clamped** (`ε^S`) constants, which
is what the constitutive law above needs. If Sumit's table gives `ε^T`, the `K²` targets shift and we
must agree which set is being used **before** comparing. Say which one is in the code.

## 7. What Sumit sends back

1. The velocity of S0 and A0 at `fd = 20, 100, 1000, 5000` Hz·m for **both** electrical sets, plus
   `K²(fd)` from (2).
2. The coupling-off check: both sets, `e = 0`, against the Step-1 numbers — with the relative
   difference printed, not just "matches".
3. The new cut-off list and the root counts at the same `fd` values as Step 1.
4. Which `ε` set is in the code, and the poling axis.
5. Any root the code finds at `c = c_T` — there must be none (§6 of Step 1, spurious-root test), and
   the piezo coupling must not reintroduce it.

## 8. What this step does **not** do

No heat, no carriers, no size effects. If a number here disagrees with Step 1 in the `e → 0` limit, the
error is in this step's boundary conditions and nowhere else — that is the whole point of running the
switch-off check before anything else is added.
