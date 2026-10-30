# problem_v3_proposal.md (Anu) — Route A restatement

**Status: PROPOSAL. `paper/problem_v2.md` is unchanged and remains the document of record.**
Route A ruling (30 Oct 2026): heat enters as an **adiabatic/isothermal bracket**; MGT is an appendix
item. Standing ruling: this paper is **DOWNGRADED to Q2**, lowest priority; Q1-versus-Q2 decided at
**week 9** on the ridge test. Route A does not change that.

## 1. Title (one word changes)

v2 title ended with "...with MGT heat and nonlocal strain gradient elasticity". Under Route A the
thermal model is no longer a modelling claim:

> *The magnetoelectric optimum is not a material constant: a frequency-dependent design ridge for
> BaTiO₃/CoFe₂O₄ plates, with a bracketed thermal correction*

Keeping "MGT" in a title supported by an appendix would be an overclaim; naming the bracket instead is
accurate and still signals that thermal effects were considered.

## 2. Hook (unchanged)

The magnetoelectric coupling of a laminated plate is **not a material constant** — it is set by a
mechanical matching condition that moves with frequency and thickness, and the static optimum quoted in
the materials literature is the `fd → 0` edge of that ridge.

## 3. Claims

### C1 — the ME coupling is non-monotonic in volume fraction and its optimum moves with `fd` *(unchanged)*
- **Statement.** For a BaTiO₃/CoFe₂O₄ laminate, `α_ME(φ)` has an interior maximum whose position
  shifts with `fd`; the static optimum is its `fd → 0` limit.
- **Figure F1.** `α_ME` vs `φ` at three `fd`, static optimum marked.
- **Limiting case.** `fd → 0` reproduces the published static optimum to < 5 % (number recorded).

### C2 — the ridge is a mechanical matching condition *(unchanged — this is the strong claim)*
- **Statement.** The ridge position is set by the ratio of the two phases' acoustic impedances and the
  thickness ratio, not by the ME coefficients; it therefore survives changes of `α_ME` magnitude.
- **Figure F2.** ridge locus with the impedance-matching prediction overlaid.
- **Limiting case.** Equal impedances (hypothetical) must give a degenerate, `φ`-independent ridge.

### C3 — NSGT moves the ridge; the thermal bracket does **not** *(rewritten under Route A)*
- **v2 form:** "NSGT and MGT move the ridge, and the four face conditions give four different ridges."
- **v3 form.** NSGT moves the ridge by an amount that scales with `(l/h)²(kh)²` (Step 2 of the Sumit
  pack gives the identity `δc/c ≈ ½(l/h)²(kh)²`); the four electrical/magnetic face condition sets give
  four ridges. The **thermal** correction is not a ridge-shift at all: it lies between the adiabatic and
  isothermal bounds, whose width is `O(Δ_E) = 10⁻³–10⁻²`, i.e. **below the ridge resolution**.
- **Figure F3.** ridge positions for the four face-condition sets, with the thermal bracket drawn as an
  error bar and NSGT shift as a separate arrow.
- **Limiting case.** `l_nl = l_g = 0` returns the classical ridge; `β = 0` collapses the bracket to a
  point.

## 4. What changes in Steps 3–6

| step | v2 | v3 (Route A) |
|---|---|---|
| 3 | coupled MGT heat | **bracket** (adiabatic / isothermal) + classical thermoelastic check |
| 4 | ME coupling, four face-condition sets | unchanged |
| 5 | NSGT on the two phases | unchanged |
| 6 | ridge test, Q1/Q2 decision at week 9 | unchanged — **the week-9 test is the ridge test, and Route A leaves it intact** |

## 5. Why Route A is a gain for this paper specifically

The ME ridge claim has **never needed the heat equation**. Under v2 the paper had to defend an MGT
form in a paper whose central quantity is a mechanical matching condition — a defence that the MGT map
shows cannot be won (`mee_anu/checks/mgt_map.md`: the thermal relaxation is outside the trust band at
every admissible thickness). Route A removes the weak section and adds a one-line error bar.

## 6. Parameters

`c_p`, `k_th`, `α_T`, `τ_q`, `Λ_ph` leave the table; `Δ_E` replaces them. Measured values already in
hand: BaTiO₃ `ρ = 5.84–5.94 g/cm³`, `c_p = 0.41–0.43 J/(g·K)` (Thin Solid Films 2004, PII
S0040603104000942); CoFe₂O₄ `D = 0.52 mm²/s`, `k_th = 0.6 W/(m·K)` (10.1007/s10854-022-09777-3).

## 7. Journals — unchanged until Dr. Vipin confirms

As v2 §8. Q2 remains the working assumption.

## 8. Risk

**R1.** With MGT out of the title, the paper is "only" an ME-ridge paper. That is what it always was;
the change makes the claim testable rather than weaker.

**R2.** The week-9 decision still hinges on the ridge being resolvable in `φ` at the available
precision. If it is not, the paper falls to a formulation note regardless of the thermal model.
