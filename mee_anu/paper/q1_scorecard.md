# Q1 scorecard — Paper C (Anu), after the literature sweep

Scored 30 Oct 2026 against the refocused plan in `problem_v2.md`. 5 = a Q1 referee would not raise
the point; 1 = fatal. Deliberately harsh — `docs/00_feasibility_analysis.md` already predicted this
is the weakest of the three, and the sweep agrees.

| # | Criterion | Score | Evidence |
|---|---|---|---|
| 1 | **Novelty vs closest papers** | **2 / 5** | Each ingredient is individually mature — MEE plate waves (Chen–Pan–Chen 2007; JIMSS 2025), nonlocal/strain-gradient MEE plates (Nanomaterials 2021, ~dozens of buckling/vibration papers), MGT in plates (Thin-Walled Struct. 2022) — and the only genuinely novel statement, that the ME optimum is frequency-dependent, has not been published but is also not yet demonstrated to be large enough to see. |
| 2 | **Physical insight** | **3 / 5** | The argument that strain transfer is a dynamic condition, so the ME optimum must move with `fd`, is correct and has a rigorous static anchor (`fd → 0` must reproduce the published optimum) — but it is an observation about known physics rather than a new mechanism; it gains a point only if the ridge is steep enough to be a design rule. |
| 3 | **Rigour and verification** | **4 / 5** | The static anchor and the symmetric-phases degeneracy (`vf* = 0.5`) are machine-checkable and stronger than anything in the 14 papers; `K_E²`, `K_M²`, `K_ME` are defined per mode and per `fd` before use, which fixes the plan's undefined "K² from open/short". |
| 4 | **Validity of the size-effect model** | **2 / 5** | The homogenised composite is the worst possible host for a strain-gradient theory: NSGT is applied to the *mixture*, but the physical gradients live at the phase boundaries, which the homogenisation has already averaged away — a referee who knows homogenisation will say this, and the size model is therefore doing decorative work unless it is confined to a stated, narrow window. |
| 5 | **Device / application relevance** | **3 / 5** | A design rule for ME sensors is a real application, and the four face conditions map directly onto real open/short circuits; but the payoff is a two-parameter rule, not a device, and the MEE sensor literature already has design charts. |
| 6 | **Reproducibility** | **5 / 5** | Two homogenisation schemes, fixed comparison points, explicit `K` definitions, sourced constant tables and the static anchor test make the paper fully rerunnable. |

**Total: 19/30.**

## Verdict: **DOWNGRADE to Q2** (Q1 stretch kept, but not assumed)

> **ACCEPTED by Dr. Vipin, 30 Oct 2026.** Paper C is the lowest priority of the three; the Q1-vs-Q2
> decision is deferred to **week 9**, taken on the three-number ridge test at the end of this file.
> Work proceeds in roadmap order without any schedule pressure to lift it back to Q1.

This is the honest call and it matches the pre-literature prediction in
`docs/00_feasibility_analysis.md` ("lowest Q1 probability as planned"). The sweep found nothing to
raise it: no thermal MEE Lamb paper exists, so "add MGT" would be an easy sell to a Q2 editor, but
Q1 reviewers in this area have seen a decade of MEE plate papers with one more effect bolted on.

### What would lift it back to Q1 (a stretch, not a plan)
A clean, steep ridge with a design rule that the MEE sensor literature would actually use, plus the
static anchor passed at < 5%. Concretely: `vf*(fd)` must move by more than 0.15 in volume fraction
across the usable band, and the four face-condition ridges must differ by more than the ridge width.
If those two numbers hold, submit to IJSS; if not, submit to a strong Q2 (e.g. *J. Intell. Mater.
Syst. Struct.* or *Acta Mechanica*) and do not delay.

### Single biggest risk
**The ME optimum may be flat.** If `K_ME(vf)` is a broad, shallow curve — which is what the static
materials literature suggests for 2-2 BaTiO₃/CoFe₂O₄ — then `vf*(fd)` is not measurable, the ridge
is noise, and the whole paper reduces to "MGT + NSGT for MEE plates", which the sweep says is not Q1.
This must be tested numerically at Step 3, on a reduced (elastic + electric + magnetic, no heat, no
size effect) model, before any writing.

### Second risk
**Homogenisation mismatch.** Two schemes can give ME coefficients that differ by a factor, which
would move the ridge further than the effect being claimed. U2 (the band) is the mitigation, but if
the band is wider than the ridge's motion, C1 and C3 are both dead and only the band survives.

### What I would tell Anu to do first
Compute `K_ME(vf)` at `fd = 500` and `fd = 5000` on the reduced model and report (a) the peak height,
(b) the peak position, (c) the half-width. Three numbers; they decide Q1 vs Q2 in one day.

---

## v3 rescore — after Route A (30 Oct 2026)

The ME-ridge claim never needed the heat equation. Route A deletes the weakest section and replaces it
with a bracket whose width is `O(Delta_E) = 1e-3..1e-2`, i.e. below the ridge resolution.

**Sweep re-run for the non-MGT cell** — ME ridge x NSGT: no paper in this check plots a *frequency-
dependent* ME optimum, and none treats the ridge position as a mechanical matching condition. The
static optimum remains the only published number, which is the paper's opening.

| # | Criterion | v2 | **v3** | Why |
|---|---|---|---|---|
| 1 | Novelty | 2 | **2** | Unchanged — the ridge is new but the field is not short of ME-plate papers. |
| 2 | Physical insight | 3 | **3** | Unchanged. |
| 3 | Rigour | 4 | **4** | Unchanged. |
| 4 | Validity of the size-effect model | 2 | **3** | The thermal model leaves the corner of the map where it was indefensible; the bracket is rigorous. |
| 5 | Device relevance | 3 | **3** | Unchanged. |
| 6 | Reproducibility | 5 | **5** | Unchanged. |
| | **Total** | **19/30** | **20/30** | |

### Verdict: **DOWNGRADE to Q2** (unchanged, lowest priority)

Week-9 Q1-vs-Q2 decision still rests on the ridge test. Route A does not move that decision either way.

**Single biggest risk:** ridge resolution in volume fraction at the available precision. If the ridge is
not resolvable in `phi`, the paper is a formulation note regardless of the thermal treatment.
