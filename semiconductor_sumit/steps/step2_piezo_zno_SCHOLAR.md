# Step 2 (Sumit) — Piezoelectric ZnO plate: open/short faces, `K²`, parity split, constants

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

## 4. The S/A split is real — parity table and the determinant factorisation (verified)

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

The elastic precursor can be checked directly with both parities in one matrix (aluminium,
`fd = 10…3×10⁴`, `c` spanning `c < c_T`, `c_T < c < c_L`, `c > c_L`):

```
det₄ / (det_S · det_A)  =  −4.000000 + 0.0 i      at every one of the 30 grid points
```

so the union of the two block root sets **is** the root set of the full system, and nothing is lost by
solving two 2×2 blocks. The constant is not 1 — it is the determinant of the row transformation —
so test for `C = const`, **not** for `C = 1`.

**Two numerical warnings.**
1. **Do not evaluate a 4×4 or 6×6 determinant by Leibniz expansion** in floating point. A Leibniz
   expansion produced a "ratio" varying over five orders of magnitude, which looks exactly like a
   broken factorisation. With LU + partial pivoting the ratio is constant to machine precision.
2. The corresponding piezo test is a `6×6`: unknowns `(u_x, u_z, φ)` with both parities, six rows
   `σ_zz(±h), σ_xz(±h), D_z(±h) = 0`. The expected result is `det₆/(det_S^{(3×3)}·det_A^{(3×3)}) = 8`,
   constant in `fd` and `c` (§5a).

## 5. The coupling coefficient `K²` — definition, once, for every later step

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

## 6. Pass criteria for this step

All values below are computed from the constants in §6 with the plane-stress reduction above.
**They are my numbers, not literature values** — the two literature cross-checks are in the last column
and are labelled as such.

| # | Check | Expected value | Tolerance |
|---|---|---|---|
| 1 | **coupling off** (`e_ij = 0`): open and short give the *same* root set | identical to < 10⁻⁶ relative | **hard gate** |
| 2 | coupling off, `fd → 0`, S0 | `√(c̄₁₁/ρ)` = **4964.83 m/s** | rel. < 10⁻⁴ |
| 3 | coupling off **and** isotropic constants (aluminium, `λ = μ`-set of Step 1) | **5393.9 m/s** = Step 1's S0 limit (check that the reduction is consistent: `√(c̄₁₁/ρ_Al)` = 5393.93 vs 5393.91, 4×10⁻⁶) | rel. < 10⁻⁴ |
| 4 | `fd → 0`, S0, **short** circuit | **4964.83 m/s** | rel. < 10⁻³ |
| 5 | `fd → 0`, S0, **open** circuit | **5252.12 m/s** (set B) / 5308.59 (set A) | rel. < 10⁻³ |
| 6 | `K²(fd → 0)` for S0 | **0.10641** (set B) / 0.12532 (set A); band widens to 0.0936–0.1253 for `ε₃₃ ∈ [8.5, 12.6]ε₀` | abs. < 1×10⁻³ |
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

## 7. The `6×6` factorisation — result

Solved with a **propagator** (`y = [u_x, u_z, φ, σ_xz, σ_zz, D_z]`,
`y' = A y`, `Φ = exp(hA)` on the half-plate, state scaled by
`diag(h, h, c₄₄h/e₃₃, c₄₄, c₄₄, e₃₃)` to keep `max|A| = O(1)`). The full determinant is

```
det₆ = det [ B Φ ; B P Φ P ] ,   B = rows (σ_xz, σ_zz, D_z),   P = diag(1,−1,−1,−1,1,1)
```

because `Φ⁻¹ = PΦP` follows from `PAP = −A`, which holds **exactly** (checked to 1e-16). The two
blocks are `det_S = det(BΦ |_{u₁,σ₃,D₃})` and `det_A = det(BΦ |_{u₃,φ,σ_xz})` — the parity subspaces at
the mid-plane are simply coordinate planes.

| quantity | result |
|---|---|
| `det₆/(det_S·det_A)` | **+8.000000**, over 39 `(fd, c)` points with `kh ≤ 6` |
| spread of that ratio | **4.3×10⁻¹³** (machine precision) |
| union of block roots = full-system roots | holds at `fd = 100, 500, 1000, 3000` |

Root sets found (open circuit, ZnO set B below):

```
fd = 500 :  full {1816.86, 5282.40} = S{5282.40} ∪ A{1816.86}
fd = 1000:  full {2214.36, 5194.92} = S{5194.92} ∪ A{2214.36}
fd = 3000:  full {2617.63, 2890.02, 5713.93} = S{2890.02} ∪ A{2617.63, 5713.93}
```

**Independent confirmation of the whole Step-2 stack:** the same propagator gives
`S0(fd) = 5308.581, 5308.550, 5308.335, 5307.567` m/s at `fd = 10, 20, 50, 100`, i.e. it converges to
the **analytic open-circuit thin-plate value 5308.59** (§5, check 5) to 1.7×10⁻⁶, and `A0` grows as
`√fd` (308.97 → 435.10 for `fd` 10 → 20). Two independent routes (analytic plane-stress reduction and the
6-state propagator) agree, which is the strongest check available in this step.

**Numerical caution.** The propagator is ill-conditioned at large `kh`
(`Φ` develops `e^{κh}` growth); use it only for `kh ≤ 6`. Beyond that, use the parity-reduced
`3×3` systems rather than the `6×6`.

## 8. Comparison points — the `fd` grid must go below 500

The thermal peak for the floor sits at **`fd = 251 Hz·m`** at `2h = 132 nm`
(`fd_peak = πκ/(2·2h)`, `κ = 2.11×10⁻⁵ m²/s`). A grid starting at 500 Hz·m would miss it. **Fixed
comparison points: `fd = 100, 250, 500, 1000, 3000, 5000` Hz·m**, plus `fd = 20` for the thin-plate
limit. Report every one, both electrical sets, both constant sets.

## 9. Constants (ZnO, wurtzite) — two sets, both tabulated

**What each source actually contains** (checked, not assumed):

| source | contains | does **not** contain |
|---|---|---|
| Gopal & Spaldin, *J. Electron. Mater.* **35** (2006) 538, [10.1007/s11664-006-0096-y](https://doi.org/10.1007/s11664-006-0096-y) (arXiv:cond-mat/0507217) | `c_ij` (Table III), `e_ij` (Table I) — **DFT** | **no dielectric tensor**, no density |
| Landolt–Börnstein tabulation `26s05d49` | `ε₃₃^S = 8.84`, `ε₁₁^S = 8.5–9.26` (constant strain); 8.67 (constant stress) | no `c`, no `e` |
| Özgür et al., *J. Appl. Phys.* **98** 041301 (2005) — review | **measured ranges** `e₃₁ = 0.39–0.66` (mostly ≈0.52), `e₃₃ = 0.92–1.30` (mostly ≈1.20) C/m² | mid-range values are a choice within a published range |

**A single experimental set containing `c`, `e`, `ε`, `ρ` was NOT located.** Hutson (1961), Carlotti et al. (1995) and Kobiakov (1980) were named as candidates; their tables
were not resolved here, so their contents are unverified and they are **not** cited. Consequently:

- **Set A — DFT (sensitivity case).** `c` and `e` from Gopal–Spaldin, `ε^S` and `ρ` as below.
- **Set B — "experimental `e`" (primary, proposed).** Same `c`, but `e₃₁ = −0.52`, `e₃₃ = 1.20`,
  `e₁₅ = −0.48`, i.e. the mid-range of the **measured** values in the review. Set B still borrows `c`
  from the DFT table, so it is only **half** experimental — the `c` column must be replaced from
  Table IV of the review (or another measured table) before the set is called primary. Stated plainly.

Shared: `ρ = 5680 kg/m³` (eFunda), `ε₁₁^S = 8.5ε₀`, `ε₃₃^S = 8.84ε₀` (Landolt).

### Results for both sets

| quantity | **Set A (DFT)** | **Set B (exp. `e`)** | check |
|---|---|---|---|
| `c̄₁₁` | 140.0095 GPa | 140.0095 GPa | same `c` |
| `ē₃₁` | −1.31938 C/m² | −1.19109 C/m² | |
| `v_short` (S0, `fd→0`) | 4964.83 m/s | **4964.83** m/s | independent of `e` |
| `v_open` (S0, `fd→0`) | 5308.59 m/s | **5252.12** m/s | 6-state solver: 5308.581 (set A) |
| `K²(0)` | 0.12532 | **0.10641** | |
| plate-mode `k_eff` | 0.3540 | **0.3262** | not `k₃₁` |
| `d₃₁` | −6.871 pC/N | **−6.203** pC/N | |
| `d₃₃` | 14.036 pC/N | **12.625** pC/N | measured ≈12 → **set B wins** |
| `k₃₁` | 0.2562 | **0.2336** | `UNVERIFIED` vs literature |
| `k₃₃` | 0.5328 | **0.4840** | `UNVERIFIED` |
| `k_t` | 0.3131 | **0.2832** | `UNVERIFIED` |
| `k₁₅` | 0.2550 | **0.2550** | `UNVERIFIED` |

**Set B is adopted as primary** on the strength of `d₃₃ = 12.6 pC/N` against the measured ≈12 pC/N;
set A is kept as the sensitivity case and `K²` carries the A/B spread (0.106 — 0.125) as its band.
The literature `k₃₁/k₃₃/k_t/k₁₅` values stay **`UNVERIFIED`** — I did not source them, and the numbers
above must not be presented as agreeing with experiment. Note that `k₃₁ = 0.23` is still above the
`≈0.18` Dr. Vipin recalled; without a sourced value neither can be called wrong.

