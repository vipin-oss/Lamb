# Step 1 (Sumit) — Rayleigh–Lamb plate: equations, stress table, targets, deliverables
## 1. Governing equations

Plane strain in the `x–z` plane: `u_y = 0`, `∂/∂y = 0`. Isotropic, homogeneous, linear elastic:

```
σ_ij,j = ρ ü_i ,    σ_ij = λ ε_kk δ_ij + 2μ ε_ij ,    ε_ij = ½(u_i,j + u_j,i)      (1)
```

Helmholtz decomposition `u = ∇φ + ∇×ψ` with `ψ = (0, ψ, 0)`:

```
u_x = φ,_x − ψ,_z ,      u_z = φ,_z + ψ,_x                                        (2)
```

With the harmonic ansatz `φ = Φ(z) e^{i(kx−ωt)}`, `ψ = Ψ(z) e^{i(kx−ωt)}`, (1)–(2) give

```
Φ'' + p² Φ = 0 ,   p² = ω²/c_L² − k² ,   c_L² = (λ+2μ)/ρ                          (3)
Ψ'' + q² Ψ = 0 ,   q² = ω²/c_T² − k² ,   c_T² = μ/ρ                                (4)
```

`p` and `q` may be real or imaginary; **no step below assumes them real.** Solutions are written
with `cos/sin` (equivalently `cosh/sinh`), never with `exp(±p z)`, so that the even/odd split is
exact and no overflow occurs at large `|p|h`.

## 2. Stresses in potential form

For the **symmetric** family take `φ = A cos(pz)`, `ψ = B sin(qz)`; for the **antisymmetric**
family `φ = A sin(pz)`, `ψ = B cos(qz)`. Substituting into (2) and then into the constitutive law:

| | `σ_zz / μ` | `σ_xz / μ` |
|---|---|---|
| S | `−(q²−k²) A cos(pz) + 2ikq B cos(qz)` | `−2ikp A sin(pz) + (q²−k²) B sin(qz)` |
| A | `−(q²−k²) A sin(pz) − 2ikq B sin(qz)` | `2ikp A cos(pz) + (q²−k²) B cos(qz)` |

These follow from (2) with `σ_zz = μ[−(q²−k²)φ + 2ikψ,_z]` and
`σ_xz = μ[(q²−k²)ψ + 2ikφ,_z]`, using `p² = ω²/c_L² − k²`, `q² = ω²/c_T² − k²` and
`ρω² = μ(k²+q²)`. **Reversing the potential, `ψ → −ψ` (equivalently taking `ψ` along `−y`), flips the
sign of every `B`-column entry, i.e. multiplies each `2×2` determinant by `−1`: it changes only the
overall sign of the dispersion determinant (and `B → −B`, so `u` is unchanged), never a root.

## 3. Limiting cases — the pass criteria for this step

All values computed by me (independent of the scholar's code) from the equations above; aluminium
constants in §4. Record scholar-vs-Arena differences in `checks/step1_compare.md`.

| # | Check | Expected value | Tolerance |
|---|---|---|---|
| 1 | `c_L` | 6197.82 m/s | — (definition) |
| 2 | `c_T` | 3121.95 m/s | — |
| 3 | S0 as `fd → 0` | `2c_T√(1 − c_T²/c_L²)` = **5393.91 m/s** | rel. < 1e-4 |
| 4 | A0 as `fd → 0` | `c → 0`, and `c ∝ √fd` (log–log slope ½ ± 0.02 over fd = 10–100) | slope, see below |
| 5 | S0, A0 at large fd | → Rayleigh speed **2909.7 m/s** (my bisection on the Rayleigh cubic at ν = 0.33) | rel. < 1e-3 by fd = 10⁴ Hz·m |
| 6 | Cutoffs (`fd`, k = 0) | A1 = `c_T/2` = 1561.0; S1 = `c_L/2` = 3098.9; S2 = `c_T` = 3122.0; A2 = `c_L` = 6197.8 Hz·m | < 1e-3 relative |
| 7 | Mode count | 1S+1A below 1561; 3S+2A at fd = 3434 Hz·m | exact count |
| 8 | No spurious root | no root at `c = c_T` (the undivided determinant vanishes there identically for every k) | exact absence |

## 4. Parameters (aluminium)

| Constant | Value | Source | Status |
|---|---|---|---|
| `E` | 70 GPa | `common/step1_instructions.md`; handbook value for Al | `[S]` (textbook) |
| `ν` | 0.33 | same | `[S]` (textbook) |
| `ρ` | 2700 kg/m³ | same | `[S]` (textbook) |
| Derived `λ`, `μ` | 5.1084e10, 2.6316e10 Pa | from the three above | computed |
| Derived `c_L`, `c_T` | 6197.82, 3121.95 m/s | computed | — |

Aluminium is used for Step 1 **only**, as the neutral verification material. ZnO enters at Step 2.
No value here is called measured.

## 5. What Sumit should send me

1. A one-page derivation of (5S)/(5A) from (1)–(4), done by hand — not copied from
   `common/step1_instructions.md`.
2. A plot: `c` vs `fd`, S0/S1/S2 and A0/A1/A2, `fd ∈ [10, 10⁴]` Hz·m, log `fd` axis, and a second
   panel with `c²/fd` vs `fd` for A0 only.
3. A CSV at the fixed comparison points (`docs/02_workflow_crosscheck.md`),
   `fd = 500, 1000, 2000, 3000, 5000` Hz·m, columns `mode, fd, c_real, k_imag`, for S0, A0, S1, A1.
   For Step 1, `k_imag ≡ 0` — write the zeros, do not omit the column.
4. The root count per branch at five `fd` values.
5. A statement of which sign convention for `ψ` was used, and the `S0` limit obtained.

