# Check — stress table in potential form, and the `ψ → −ψ` statement (30 Oct 2026)

Question: is the pressure/stress table in `steps/step1_elastic_rayleigh_lamb.md` §2 consistent with
eq. (2) and with the undivided determinant (4S)/(4A), and what does reversing the potential do?

## 1. Analytic check

With (2) `u_x = φ,x − ψ,z`, `u_z = φ,z + ψ,x`, `σ_zz = μ[−(q²−k²)φ + 2ikψ,z]` and
`σ_xz = μ[(q²−k²)ψ + 2ikφ,z]`. For S (`φ = A cos pz`, `ψ = B sin qz`) and A
(`φ = A sin pz`, `ψ = B cos qz`) this reproduces the table in §2 exactly.

Rows at `z = h`, determinant `det = a₁₁a₂₂ − a₁₂a₂₁`:

```
S:  a₁₁ = −(q²−k²)cos(ph)   a₁₂ = +2ikq cos(qh)
    a₂₁ = −2ikp sin(ph)     a₂₂ = +(q²−k²)sin(qh)      det_S = −[ (4S) ]
A:  a₁₁ = +2ikp cos(ph)     a₁₂ = +(q²−k²)cos(qh)
    a₂₁ = −(q²−k²)sin(ph)   a₂₂ = −2ikq sin(qh)        det_A = +[ (4A) ]
```

So the table yields (4S) and (4A) up to the overall factor `−1` on the S family, which does not move
a root. The **reverse direction was checked as well**: the determinant of the table equals `−(4S)`
and `+(4A)` *as an identity in (fd, c)*, not just at roots.

## 2. Numeric check (python, `cmath`, aluminium E = 70 GPa, ν = 0.33, ρ = 2700)

Ratio `det(table) / [(4S) or (4A) as printed]`, over `fd = 10, 100, 1000, 10⁴` Hz·m ×
`c = 500, 1500, 2909.73, 3122, 4500, 6000` m/s (24 points, spanning `c < c_T`, `c_T < c < c_L`,
`c > c_L`, i.e. both real and imaginary `p`, `q`):

```
S: ratio = −1.000000 + 0.0e+00 i     at every point   max |dev| < 1e-16
A: ratio = +1.000000 + 0.0e+00 i     at every point   max |dev| < 1e-16
```

## 3. The `ψ → −ψ` statement

Taking the vector potential along `−y` (equivalently `ψ → −ψ`) flips the sign of **every `B`-column
entry** in both `2×2` systems above, hence multiplies each determinant by `−1` and sends `B → −B`
while `A` is unchanged — so `u` is unchanged and no root can move.

Verified: for 1400 sample points (`fd` × `c`, both families)

```
max | det(+B) + det(−B) | / | det(+B) |  =  0.0        (exact, to machine precision)
```

and the located roots coincide:

| root | `+B` convention | `−B` convention |
|---|---|---|
| S0, fd = 10 | 5393.9053 | 5393.9053 |
| S0, fd = 100 | 5393.1719 | 5393.1719 |
| A (high-order), fd = 10⁴ | 3972.7917 | 3972.7917 |

**Statement for the pack:** reversing the potential changes only the overall sign of the dispersion
determinant; the dispersion relation, the root set and the displacement field are unchanged.

## 4. Independent re-run of the targets from the reverted table

Roots of the (4S)/(4A)-equivalent systems, `h = 1`, `fd` in Hz·m, found by sign change + bisection
(`N = 2×10⁵` points, tan-normalised forms to avoid overflow):

```
fd        S-family                                    A-family
10        5393.9053                                  311.6377
100       5393.1719                                  954.2341
1000      5308.5887                                  2326.6431
3000      3288.0593, 3655.8191                       2801.7666, 3655.8191, 5980.5210
10000     2910.3452, 3160.6977, 3463.3753, ...       2909.1299, 3160.6977, 3207.2314, ...
30000     2909.7314, ...                             2909.7314, ...
```

- S0 thin limit **5393.9053** vs target 5393.91 → relative 8.7e-7 < 1e-4 **PASS**.
- A0 → **2909.1299** at fd = 10⁴ and **2909.7314** at fd = 3×10⁴ vs Rayleigh 2909.73 → relative
  2.1e-4 and 1.4e-7, both < 1e-3 **PASS**.
- A0 ∝ √fd: 311.6377 → 954.2341 → 2326.6431 over fd ×10, ×10 (slope ½ in the intermediate range)
  **PASS**.
- The values at fd ≥ 10⁴ differ slightly from the earlier run (2909.1 vs 2910.3 for the two
  families at fd = 10⁴) because at `kh ≈ 10.8` the finite-thickness correction is still ~0.1 %; both
  settle to 2909.73 by fd = 3×10⁴. This is expected, not a discrepancy.

## 5. What is *not* claimed

The table was checked against (4S)/(4A) and against the limits, i.e. *consistency*. The constitutive
substitution was re-derived by hand on 30 Oct (`σ_zz = μ[−(q²−k²)φ + 2ikψ,z]`,
`σ_xz = μ[(q²−k²)ψ + 2ikφ,z]`) and agrees, but the derivation is now part of the pack (§2 note) so
that it can be checked line by line rather than taken on trust.
