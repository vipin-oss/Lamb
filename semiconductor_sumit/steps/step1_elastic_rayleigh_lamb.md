# Step 1 (Sumit) — Classical Rayleigh–Lamb plate: equations, checks and instructions

**Goal:** reproduce the traction-free isotropic elastic plate dispersion, and fix the numerical
machinery that every later step reuses. Nothing here is new physics; the step exists so that a
later mismatch can be attributed to one step only.

Conventions (unchanged, `docs/02_workflow_crosscheck.md`): `exp[i(kx−ωt)]`, thickness `2h`, faces
`z = ±h`, plane strain, `k = k_r + i k_i` with `k_i > 0` decaying along `+x`, `fd = f·2h` in Hz·m.

---

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

```
σ_zz = −μ(q² − k²) Φ cos-type …        (see the assembled forms below)
σ_xz = μ( u_x,z + u_z,x )
```

For the **symmetric** family take `φ = A cos(pz)`, `ψ = B sin(qz)`; for the **antisymmetric**
family `φ = A sin(pz)`, `ψ = B cos(qz)`. Substituting into (2) and then into the constitutive law:

| | `σ_zz / μ` | `σ_xz / μ` |
|---|---|---|
| S | `−(q²−k²) A cos(pz) + 2ikq B cos(qz)` | `−2ikp A sin(pz) + (q²−k²) B sin(qz)` |
| A | `−(q²−k²) A sin(pz) − 2ikq B sin(qz)` | `2ikp A cos(pz) + (q²−k²) B cos(qz)` |

> **Sign convention, stated once.** The sign of the `ψ` terms depends on the direction chosen for
> the `ψ` vector in (2). Both choices give the same physical roots; they give the two equations
> below with the *second* term's sign flipped. Do not "fix" the sign by argument — fix it by the
> `S0` thin-plate check in §5, which is decisive. The forms given below are the ones I verified
> numerically to reproduce `S0 → 5393.91 m/s`.

## 3. Boundary conditions and the dispersion equations

Traction-free faces: `σ_zz = σ_xz = 0` at `z = ±h`. Four equations, four unknowns `(A,B)` per
family, so a `2×2` determinant per family. The **undivided determinants are numerically dangerous**
(see §6), so the working forms are the divided ones:

**Symmetric (S):**
```
(q² − k²)² cos(ph) sin(qh)/q  +  4 k² p sin(ph) cos(qh)  =  0                     (5S)
```

**Antisymmetric (A):**
```
4 k² q sin(qh) cos(ph)  +  (q² − k²)² cos(qh) sin(ph)/p  =  0                     (5A)
```

Written this way, both equations stay real when `p` or `q` is imaginary, because the products
`sin(qh)/q` and `sin(ph)/p` are even functions of their argument. **This is the required working
form** for all later steps.

### Equivalently, the tangent forms (use only as a cross-check)
```
S:  tan(qh)/tan(ph) = − 4 k² p q / (q² − k²)²
A:  tan(ph)/tan(qh) = − (q² − k²)² / (4 k² p q)
```
These fail at `p h` or `q h = mπ/2`; they are for checking algebra, not for root finding.

## 4. Non-dimensionalisation (state it in every check file)

```
ξ = k h ,    Ω = ω h / c_T ,    c̄ = c / c_T ,    fd = f·2h = Ω c_T / π
```
So `c̄ = Ω/ξ` and `fd [Hz·m] = Ω c_T / π`. With aluminium (`c_T = 3121.95 m/s`):
`fd = 993.7 Ω` Hz·m.

## 5. Limiting cases — the pass criteria for this step

All values computed by me (independent of the scholar's code) from the equations above; aluminium
constants in §7. Record scholar-vs-Arena differences in `checks/step1_compare.md`.

| # | Check | Expected value | Tolerance |
|---|---|---|---|
| 1 | `c_L` | 6197.82 m/s | — (definition) |
| 2 | `c_T` | 3121.95 m/s | — |
| 3 | S0 as `fd → 0` | `2c_T√(1 − c_T²/c_L²)` = **5393.91 m/s** | rel. < 1e-4 |
| 4 | A0 as `fd → 0` | `c → 0`, and `c ∝ √fd` (log–log slope ½ ± 0.02 over fd = 10–100) | slope, see below |
| 5 | S0, A0 at large fd | → Rayleigh speed **2909.7 m/s** (my bisection on the Rayleigh cubic at ν = 0.33) | rel. < 1e-3 by fd = 10⁴ Hz·m |
| 6 | Cutoffs (`fd`, k = 0) | A1 = `c_T/2` = 1561.0; S1 = `c_L/2` = 3098.9; S2 = `c_T` = 3122.0; A2 = `c_L` = 6197.8 Hz·m | < 1e-3 relative |
| 7 | Mode count | 1S+1A below 1561; 3S+2A at fd = 3434 Hz·m | exact count |
| 8 | No spurious root | no root at `c = c_T` (see §6) | exact absence |

> **Correction to `common/step1_instructions.md`.** That file quotes "Rayleigh speed about
> 2906 m/s". Solved properly at ν = 0.33 the value is **2909.7 m/s** (≈ 0.9321 `c_T`); 2906 differs
> by 0.13%, i.e. outside the 1e-3 tolerance of check 5. I suggest the number be corrected to 2909.7
> before it is quoted to Sumit. (Also note check 4's `A0 → 0` limit makes the tolerance table in
> `docs/02_workflow_crosscheck.md` unusable for A0 at low fd — compare `c²/fd` instead, which tends
> to a constant.)

## 6. Numerical warnings — three failures I reproduced myself

1. **Spurious root at `c = c_T`.** The undivided determinant
   `(q²−k²)² cos(ph) sin(qh) − 4k²pq sin(ph) cos(qh)` vanishes identically at `q = 0` (i.e. `c = c_T`)
   for *every* `k`, because `sin(qh) = 0` there. A naive grid search returns `c = c_T` at every
   frequency. **This is workflow failure cause 6** ("spurious roots from scaling the determinant").
   Dividing by `q` and `p` as in (5S)/(5A) removes it. Verified: the undivided form returns 3122.0
   at fd = 1, 10, 100; the divided form returns 5393.91, 5393.18, 5308.59.
2. **`p` or `q` imaginary.** Handled by writing everything in `sin/cos`; never call `sqrt` on a
   possibly-negative number without branching on its sign.
3. **Branch identity.** Roots are followed by **continuity in `(fd, c)`**, never by sorting. At each
   `fd`, start from the previous `fd`'s root and use it as the initial guess; record the root count
   along each branch and report any change. Sorting mixes `S1` into `A0` near the A1 cutoff.

## 7. Parameters (aluminium)

| Constant | Value | Source | Status |
|---|---|---|---|
| `E` | 70 GPa | `common/step1_instructions.md`; handbook value for Al | `[S]` (textbook) |
| `ν` | 0.33 | same | `[S]` (textbook) |
| `ρ` | 2700 kg/m³ | same | `[S]` (textbook) |
| Derived `λ`, `μ` | 5.1084e10, 2.6316e10 Pa | from the three above | computed |
| Derived `c_L`, `c_T` | 6197.82, 3121.95 m/s | computed | — |

Aluminium is used for Step 1 **only**, as the neutral verification material. ZnO enters at Step 2.
No value here is called measured.

## 8. What Sumit should send me

1. A one-page derivation of (5S)/(5A) from (1)–(4), done by hand — not copied from
   `common/step1_instructions.md`.
2. A plot: `c` vs `fd`, S0/S1/S2 and A0/A1/A2, `fd ∈ [10, 10⁴]` Hz·m, log `fd` axis, and a second
   panel with `c²/fd` vs `fd` for A0 only.
3. A CSV at the fixed comparison points (`docs/02_workflow_crosscheck.md`),
   `fd = 500, 1000, 2000, 3000, 5000` Hz·m, columns `mode, fd, c_real, k_imag`, for S0, A0, S1, A1.
   For Step 1, `k_imag ≡ 0` — write the zeros, do not omit the column.
4. The root count per branch at five `fd` values.
5. A statement of which sign convention for `ψ` was used, and the `S0` limit obtained.

## 9. Arena cross-check plan (two independent routes)

- **Route A — analytic determinant,** eqs. (5S)/(5A), roots by a bracketing method on
  `c ∈ (0, c_L)` per family with continuity tracking from low `fd`.
- **Route B — Chebyshev collocation in `z`** on the plane-strain operator, `N = 40` and `N = 60`
  (convergence check), wave ansatz `exp(ikx)`; the dispersion relation is `det = 0` of the
  `(2N+2)×(2N+2)` matrix including the four traction conditions, eigenvalues in `ω` at fixed real
  `k`. This route deliberately avoids the potentials entirely, so an algebra slip in (5S)/(5A)
  shows up as a disagreement between A and B.
- **Agreement required:** Route A vs Route B, rel. < 1e-4 in `c`; Route A vs Sumit's CSV,
  rel. < 1e-4 (`docs/02_workflow_crosscheck.md`).
- Recorded in `checks/step1_compare.md` together with the root counts and any branch jump.

## 10. Exit criteria (gate)

Step 1 passes when checks 1–8 of §5 pass for **both** Route A and Sumit's CSV, and the root counts
agree at all five comparison points. Step 2 (piezoelectricity) does not start before that.
