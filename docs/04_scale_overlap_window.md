# Scale-overlap window — all three papers (one page)

**Question.** For each paper, is there a thickness `2h` at which *all* of the following hold at once?

- **(a) size effect is visible** — the NSGT correction to phase velocity exceeds **5 %** for a
  dimensionless `l/h` taken from a sourced range;
- **(b) the thermoelastic damping peak is within a factor 10 of the thermal diffusion thickness**,
  i.e. the peak is actually inside the measured frequency window;
- **(c) the continuum/trust band holds** — `kh ≤ 3` and `2h ≥ 10Λ_ph`.

**Answer, in one line: the window is empty for all three papers.** Details and the arithmetic follow.
No code beyond the ten lines quoted inline.

## 1. Condition (a), in closed form

NSGT enters the dispersion as `c²/c_el² = (1 + l_g²k²)/(1 + l_nl²k²)`. With `k = (kh)/h` and
`(l/h) ≪ 1`,

```
δc/c ≈ ½ (l_g² − l_nl²) k² = ½ (l/h)² (kh)²                                            (1)
```

(the equal-and-opposite sign for the two scales is C3's premise). Requiring `δc/c ≥ 0.05` at the
**most favourable** point of the trust band, `kh = 3`:

```
(l/h) ≥ √(0.1)/(kh) = 0.316/3 = 0.105          ⇒    2h ≤ 19 l                          (2)
```

At `kh = 1` it is `2h ≤ 6.3 l`, i.e. five times tighter. (2) is therefore a *generous* upper bound.

## 2. Condition (b) is not independent — it is condition (c) plus window access

The damping peak sits at `ω ≈ π²κ/(2h)²`; the thermal diffusion length there is
`δ = √(2κ/ω) = (√2/π)(2h) ≈ 0.45(2h)`. So `δ` is *always* within a factor 10 of `2h` **whenever the
peak exists** — the condition can never fail by itself. What can fail is **access**: the peak frequency
`fd_peak = πκ/(2·2h)` must fall inside the swept window `[500, 5000]` Hz·m. That is the binding part,
and it is already in the MGT map (`fd_peak` at the band floor).

## 3. The numbers, per paper

`Λ_ph` sourced only for ZnO (13.2 nm, Krahl et al. 2020 — see the Sumit MGT map). For the other two it
is `[U]`, so the `10Λ_ph` floor is given as a range and the verdict is stated for both ends.

| paper | `Λ_ph` | (c) floor `2h ≥ 10Λ_ph` | (a) ceiling `2h ≤ 19 l`, `l = 1 nm` | `l` needed for overlap | `fd_peak` at the floor | window |
|---|---|---|---|---|---|---|
| **Sumit** (ZnO, `k_th = 60`) | **13.2 nm** sourced | **132 nm** | 19 nm | **≥ 6.9 nm** | 251 Hz·m (< 500) | **empty**, gap ×7 |
| Sumit (ZnO, `k_th = 1.2`) | 13.2 nm | 132 nm | 19 nm | ≥ 6.9 nm | 5.0 Hz·m (< 500) | **empty**, gap ×7 |
| **Neha** (d-Al–Co–Ni) | 1–2 nm `[U]` | 10–20 nm | 19 nm | ≥ 0.5–1.1 nm | ≪ 500 | **empty** (or marginal at `Λ_ph = 1` nm) |
| **Anu** (BaTiO₃/CoFe₂O₄) | 1–5 nm `[U]` | 10–50 nm | 19 nm | ≥ 0.5–2.6 nm | ≪ 500 | **empty** for `Λ_ph ≥ 2` nm |

**Sourced `l` does not exist.** For all three materials the NSGT length scales are lattice-scale
(`O(1)` nm) and no paper supplies a measured `l_nl`, `l_g`; the earlier ruling stands — **`l` is swept
as `l/h` only, never quoted as a material constant.** Consequently condition (a) cannot be *closed*
from literature at all: the window test above is run at `l = 1 nm` as the optimistic end.

**Verdict.** For Sumit the overlap fails by a factor of ~7, and it fails on two independent axes
(`c`-band floor 132 nm vs 19 nm ceiling; and the peak sits at 251 Hz·m, below the 500 Hz·m sweep
floor). For Neha and Anu it fails unless `Λ_ph ≈ 1` nm *and* `l ≈ 1` nm simultaneously — i.e. only in
the corner of parameter space where neither number is sourced. **Treat the window as empty in all
three.**

## 4. Proposal: replace the heat model by a two-sided bound

Since the thermal relaxation can be neither resolved nor removed by a thickness choice, stop modelling
it as a physical effect and bound it instead. Run each problem **twice**, with the thermal field
eliminated in the two rigorous limits:

| case | condition | what it does |
|---|---|---|
| **adiabatic** | no heat flow between material points, `θ` from the local energy balance | upper bound on `k_i`, stiffest thermal state |
| **isothermal** | infinite conduction, `θ` slaved to the strain instantly | lower bound on `k_i`, no thermal loss |

The true answer lies between them, and the **bracket width is `O(Δ_E)`** with
`Δ_E = T₀β²/(ρ c_p c_L²)` — for oxides/intermetallics `Δ_E = 10⁻³–10⁻²`, so the bracket is narrower
than the line width of any figure the papers plan. No `τ_q`, no `κ`, no `Λ_ph` appears in the result.

## 5. What changes in each `problem_v3`

**Sumit** (`paper/problem_v3_proposal.md`): the comparison section (former C2) becomes *"thermal
bracket"* — two curves, adiabatic and isothermal, with the bracket width annotated, and a sentence
stating that MGT lies inside the bracket and is therefore not an observable. `k_th`, `c_p`, `α_T`,
`τ_q`, `Λ_ph` drop out of the parameter table; `Λ_ph` survives only in the validity paragraph. C1 and
C3 are untouched — **neither needs the heat equation.**

**Neha**: the same substitution; the paper gains a short "thermal effects are bracketed, not modelled"
paragraph and loses the obligation to defend an MGT form. Her phason C-claims are unaffected.

**Anu**: strongest case — the frequency-dependent ME ridge claim does not involve heat at all. The
bracket becomes a one-sentence statement of the error bar on the ridge position. The paper's major
upgrade is untouched.

**Cost/benefit, stated plainly.** All three lose a thermal *claim* they could not have supported, and
all three gain a rigorous, cheap error bound. No paper's major upgrade depends on the thermal model;
that is why this simplification is safe rather than a retreat.
