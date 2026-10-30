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

**Confirmed by ruling (30 Oct 2026): poling along the thickness `z`, `c` axis normal to the faces, plane
strain in the `x–z` plane.** The in-plane-poled variant is not pursued; if it ever is, the index
rotation `e_31 ↔ e_33`, `ε_11 ↔ ε_33` applies.

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

## 3a. The S/A split is real — parity table and the determinant factorisation (verified)

With poling along `z`, each family has **definite parity in `z`**, and the electric potential takes the
parity *opposite* to the acoustic scalar potential of the same family:

| family | `u_x` | `u_z` | `S_1 = u_x,x` | `S_3 = u_z,z` | `φ` (electric) | `E_3 = −φ,z` | `D_3` |
|---|---|---|---|---|---|---|---|
| **S** | even | odd | even | even | **odd** | even | even |
| **A** | odd | even | odd | odd | **even** | odd | odd |

Both face conditions are then consistent in one equation per face: for S, `D_3(±h) = 0` is *one*
condition (even function); for A it is also one (odd function), so the electrical condition never
couples S to A. Mechanical traction-free is the same story: for S, `σ_zz` is even and `σ_xz` odd.

**Consequence, and the test.** Take the *full* system with **both** parities carried at once — four
unknowns `(A_c, B_s | A_s, B_c)` and all **four** face rows `σ_zz(±h) = σ_xz(±h) = 0` — and call its
determinant `det₄`. Then the four rows are not independent: `r₃ − r₁` kills the S columns and
`r₁ + r₃` kills the A columns, etc., so

```
det₄  =  C · det_S · det_A ,     C a constant (independent of fd and c).
```

I verified this explicitly for the elastic precursor with both parities in one matrix (aluminium,
`fd = 10…3×10⁴`, `c` spanning `c < c_T`, `c_T < c < c_L`, `c > c_L`):

```
det₄ / (det_S · det_A)  =  −4.000000 + 0.0 i      at every one of the 30 grid points
```

so the union of the two block root sets **is** the root set of the full system, and nothing is lost by
solving two 2×2 blocks. The constant is not 1 — it is the determinant of the row transformation —
so test for `C = const`, **not** for `C = 1`.

**Two warnings from doing this.**
1. **Do not evaluate a 4×4 or 6×6 determinant by Leibniz expansion** in floating point. My first
   attempt did, and produced a "ratio" varying over five orders of magnitude, which looks exactly like
   a broken factorisation. With LU + partial pivoting the ratio is constant to machine precision.
2. The corresponding **piezo gate** is a `6×6`: unknowns `(u_x, u_z, φ)` with both parities, six rows
   `σ_zz(±h), σ_xz(±h), D_z(±h) = 0`. Sumit must report `det₆/(det_S^{(3×3)} · det_A^{(3×3)})` at
   five `fd` values and show it is constant. **I did not run the `6×6` — I derived the parity table
   above and verified the mechanism exactly on the elastic precursor; the `6×6` is the gate.**

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
| 5 | `fd → 0`, S0, **open** circuit | **5308.59 m/s** | rel. < 10⁻³ |
| 6 | `K²(fd → 0)` for S0 | **0.12532** (= plate-mode `k_eff = 0.3540`), band 0.0936–0.1253 for `ε₃₃ ∈ [8.5, 12.6]ε₀` | abs. < 1×10⁻³ |
| 7 | `K² → 0` as `e²` | halving every `e_ij` gives `K²/4` | rel. < 10⁻³ |
| 8 | open velocity > short velocity, on every branch, every `fd` | sign test, all roots | absolute |
| 9 | Thickness-mode limit | `k_t² = 0.0981` (`k_t = 0.3131`) from `e₃₃²/(c₃₃^D ε₃₃^S)`; recovered to < 3 % from the cut-off behaviour | 3 % (the small-`kh` expansion is not exact) |
| 10 | Root counts | record them; they must **not** be assumed to equal Step 1's — the effective stiffness changes, so the cut-offs move. Report the new cut-off list | recorded, not tested |

**Coupling constants from the stated set — computed, and NOT yet checked against a source.** Using
the compliance inverted from `c^E` and the inferred `ε₃₃^T = ε₃₃^S + e₃₃²/c₃₃ = 9.80ε₀`:

| quantity | formula | value |
|---|---|---|
| `d₃₁` | `(s₁₁+s₁₂)e₃₁ + s₁₃e₃₃` | −6.87×10⁻¹² C/N |
| `d₃₃` | `2s₁₃e₃₁ + s₃₃e₃₃` | 1.40×10⁻¹¹ C/N |
| `k₃₁` | `d₃₁/√(s₁₁ε₃₃^T)` | **0.256** |
| `k₃₃` | `d₃₃/√(s₃₃ε₃₃^T)` | **0.533** |
| `k_t` | `e₃₃/√(c₃₃^D ε₃₃^S)` | **0.313** |
| `k₁₅` | `e₁₅/√(c₄₄^D ε₁₁^S)` | **0.255** |

`d₃₃ = 14.0 pC/N` is close to the commonly measured `d₃₃ ≈ 12 pC/N`, which is the one encouraging
number here. But `k₃₃ = 0.533` and `k_t = 0.313` are **higher than the values recalled by
Dr. Vipin (k₃₁ ≈ 0.18)**, and I could not source a defensible ZnO `k₃₁/k₃₃/k_t/k₁₅` table in this
pass, so those literature numbers are **`UNVERIFIED`**. The likely cause is mixing sources: `c` and
`e` are **DFT** (Gopal & Spaldin, which is known to overestimate `e₃₃`), while `ε` is experimental.
**A single self-consistent set is still owed** — either take `c, e, ε` all from one experimental
review table, or take all three from the same DFT calculation (which would give `ε ≈ ε^∞ ≈ 3.8`, and
much larger `k`). Until that is settled the `K²` targets above carry a **±40 % band** and must not be
used as a pass/fail criterion for anything except check 1 (coupling off).

## 6. Constants (ZnO, wurtzite)

| constant | value | source | status |
|---|---|---|---|
| `c₁₁, c₁₂, c₁₃, c₃₃, c₄₄` | 206, 118, 118, 211, 44 GPa | arXiv:cond-mat/0507217v2, measured row | sourced (as in v2 §7) |
| `e₃₃, e₃₁, e₁₅` | 1.34, −0.57, −0.48 C/m² | same | `e₁₅` value **to be confirmed** by Sumit |
| `ε₁₁^S, ε₃₃^S` | 8.5ε₀, 8.84ε₀ | Landolt–Börnstein tabulation `26s05d49` (constant strain) | **clamped values**, read from a tabulation |
| `ρ` | 5680 kg/m³ | eFunda ZnO | sourced |
| derived `c̄₁₁, ē₃₁, ε̄₃₃` | 140.0095 GPa, −1.31938 C/m², 8.6781×10⁻¹¹ F/m | §4 reduction | computed |

**`ε^S` versus `ε^T` — determined, and the earlier numbers were wrong because of it.**
The constitutive law above needs the **clamped (constant-strain) `ε^S`**. The `9.16 / 12.64` values in
the earlier draft behave like `ε^T`-type numbers, and using them as `ε^S` is exactly what produced the
optimistic `K² = 0.0936`. Sourced clamped values: `ε₃₃^S = 8.84`, `ε₁₁^S = 8.5–9.26`
(Landolt–Börnstein tabulation `26s05d49`, "static dielectric tensor, constant strain"; the same entry
gives `8.67` for constant stress). `ε^T` for ZnO is larger (`≈ 9.8–10.4`, the 10.4 being Langton &
Matthews' *colloidal* value, [10.1088/0508-3443/9/11/308](https://doi.org/10.1088/0508-3443/9/11/308) —
not a single-crystal number). **Use `ε^S`; sweep `ε₃₃ ∈ [8.5, 12.6]ε₀` as an uncertainty band.**

## 7. What Sumit sends back

1. The velocity of S0 and A0 at `fd = 20, 100, 1000, 5000` Hz·m for **both** electrical sets, plus
   `K²(fd)` from (2).
2. The coupling-off check: both sets, `e = 0`, against the Step-1 numbers — with the relative
   difference printed, not just "matches".
3. The new cut-off list and the root counts at the same `fd` values as Step 1.
4. Which `ε` set is in the code (must be `ε^S`).
5. The `6×6` factorisation number: `det₆/(det_S^{(3×3)}·det_A^{(3×3)})` at five `fd`, constant to
   machine precision (§3a). Also the `4×4` elastic version, expected `−4.000000`.
6. Any root the code finds at `c = c_T` — there must be none (§6 of Step 1, spurious-root test), and
   the piezo coupling must not reintroduce it.

## 8. What this step does **not** do

No heat, no carriers, no size effects. If a number here disagrees with Step 1 in the `e → 0` limit, the
error is in this step's boundary conditions and nowhere else — that is the whole point of running the
switch-off check before anything else is added.
