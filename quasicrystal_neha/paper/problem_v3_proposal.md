# problem_v3_proposal.md (Neha) — Route A restatement

**Status: PROPOSAL. `paper/problem_v2.md` is unchanged and remains the document of record.** Reason:
the scale-overlap window is empty (`docs/04_scale_overlap_window.md`) and the MGT map puts the thermal
relaxation outside the trust band for this material. Under the project ruling of 30 Oct 2026 the heat
problem is carried as an **adiabatic/isothermal bracket**, not as a coupled MGT mechanism.

## 1. Title (unchanged — the heat model was never in it)

> *Phason kinematics and strain-gradient dispersion in thin quasicrystal plates: what attenuation can
> and cannot measure*

The title survives because it never leaned on the thermal channel. This is the cleanest of the three
papers under Route A: **nothing in the title, the hook or the claims changes.**

## 2. Hook (unchanged, still provisional on the thickness-scaling ruling)

Whether a quasicrystal plate attenuates at all without heat is decided by the **phason kinematics**
(wave-like versus diffusive), not by the thermal constants; and because the phason field brings a
second length-scale combination, a single dispersion curve cannot identify the two NSGT scales while
the attenuation curve can.

## 3. Claims

### C1 — phason kinematics decides whether the plate attenuates without heat *(unchanged)*
- **Statement.** With the phason treated as wave-like the plate supports a propagating phason branch
  that removes energy at a rate set by the phason-phonon coupling; with the phason diffusive the branch
  is overdamped and the loss collapses to the phonon-only value. The two treatments are distinguished
  by a sign/magnitude test on `k_i`, not by a fit.
- **Figure F1.** `k_i` vs `fd` for both kinematic choices, with the phonon-only curve as the reference.
- **Limiting case.** Phason-phonon coupling → 0 returns the phonon-only plate to < 10⁻⁶; the diffusive
  choice must reproduce its own `ω`-scaling (∝ `ω²` at low `fd`).
- **Gate.** This is the week-1 decision gate already in v2; it is untouched by Route A.

### C2 — the attenuation peak carries a thickness fingerprint *(unchanged in form)*
- **Statement.** The peak of `k_i(fd)` has a locus whose slope in `(log 2h, log fd)` takes one of three
  distinct values depending on which of the three channels dominates. The slopes are integers or
  simple fractions, so the test is a slope measurement, not a curve fit.
- **Figure F2.** peak locus with the three predicted slopes; measured points overlaid.
- **Limiting case.** Thermal channel switched off (bracket width → 0) must leave the locus slope
  unchanged on the third branch — this is the one place where Route A touches C2, and it *helps*: the
  bracket replaces an uncertain thermal model with a hard band on the same figure.

### C3 — NSGT enters through a second combination via the phason field *(sharpened)*
- **Statement.** The phonon stress carries NSGT and the phason stress is classical (standing ruling).
  Because the phason field has its own gradient terms, the dispersion constrains one combination
  `(l_nl, l_g)` while the peak locus constrains a second; a velocity curve alone leaves the pair
  degenerate.
- **Figure F3.** identifiability map in `(l_nl/h, l_g/h)`: velocity-consistent stripe ∩ peak-locus curve.
- **Limiting case.** `l_nl = l_g = 0` returns Step 4; nonlocal-only and gradient-only give equal and
  opposite shifts.
- **Out of claims:** NSGT on the **phason** stress remains a Step-5 sensitivity with one labelled
  figure, never supporting C1–C3 (standing ruling, restated).

## 4. What changes in Steps 3–6 under Route A

| step | v2 | v3 (Route A) |
|---|---|---|
| 3 | coupled MGT heat inside the plate | **bracket**: adiabatic and isothermal runs, bracket width = `O(Δ_E)`; classical thermoelastic check at low `fd` |
| 4 | phason kinematics decision + NSGT | unchanged |
| 5 | NSGT on phason as sensitivity | unchanged |
| 6 | analysis with thermal model in the loop | analysis with the bracket drawn on every `k_i` figure |

## 5. Parameters — what leaves the table

`τ_q`, `k_th`, `c_p`, `α_T`, `Λ_ph` **leave the parameter table** and appear only in the bracket
definition (`Δ_E`) and the validity paragraph. `l_nl`, `l_g` remain dimensionless `l/h` sweeps (no
sourced values exist — this is now a documented fact, `docs/04_scale_overlap_window.md` §3).

## 6. Journals — unchanged until Dr. Vipin confirms

As v2 §8 (Eur. J. Mech. A/Solids first, IJSS second). Not re-ranked here.

## 7. Risk

**R1.** The empty scale-overlap window means the paper cannot claim that the *size effect* and the
*thermal effect* are both resolved in one measurement. C2's third branch must therefore be presented as
a prediction with the bracket, not as a resolved observation.

**R2.** (unchanged) If the peak locus is insensitive to `l_nl/h` and `l_g/h` at the 1 % level, C3 falls
and the paper is C1 + C2 alone.
