# Roadmap (14 weeks to submission-ready draft per paper)

Staggered so you are never reviewing three Step-N plots in the same week.
Sumit leads, Neha one week behind, Anu two weeks behind.

> **Task 0 for Sumit is complete (30 Oct 2026) and the scope changed.** The novelty sweep found
> that the planned major upgrade (DC-drift non-reciprocal amplification in a PSC plate) is already
> published (Yang & Zhou 2005, doi:10.1016/j.ijsolstr.2004.10.011), and that two 2025 papers own
> "Lamb waves in a PSC plate with attenuation". The paper is re-anchored on screening-ordered
> attenuation channels (carrier peak vs thermoelastic floor). See
> `semiconductor_sumit/paper/problem_v2.md`. **Timing effect:** Step 7 (U1 nulling map) is now a
> real step, so Sumit's writing weeks 10–13 lose one week to it; the week-14 submission date holds
> only if Steps 2–5 do not slip. Neha and Anu are unaffected.
>
> **Journal note:** `docs/00_feasibility_analysis.md` lists *Wave Motion* as a likely target for
> Sumit. Checked on scimagojr (SJR 2025): **Wave Motion is Q2, SJR 0.499** — it cannot be a Q1
> target. Sumit's targets are now Int. J. Solids Struct. (Q1, 1.002), Int. J. Eng. Sci. (Q1, 1.228)
> and Eur. J. Mech. A/Solids (Q1, 1.023). The same check is still owed to Neha and Anu.

| Week | Sumit (semiconductor) | Neha (quasicrystal) | Anu (MEE) | You / Arena |
|---|---|---|---|---|
| 1 | Literature + novelty sweep, Step 1 equations | Reading items 1-5, decide poling/quasi axis | Reading items 1-3, fix poling axis | Run common solver, send equations pack |
| 2 | Step 1 done -> plot | Step 1 | Reading, Step 1 | Cross-check Step 1 numbers (3 scholars) |
| 3 | Step 2 piezo | Step 1 done / Step 2 | Step 1 | Independent Step 2 in Arena for Sumit |
| 4 | **bulk-medium test (Fourier vs MGT) -> then** Step 3 MGT heat | Step 2 | Step 2 | Cross-check Sumit; start Neha Step 2 check |
| 5 | Step 4 carriers | Step 3 phason (decision gate) | Step 2 done / Step 3 | Arena: carrier limit check |
| 6 | Step 4 done, **base paper figures** | Step 3 done | Step 3 | Cross-check Neha Step 3 vs published |
| 7 | Step 5 NSGT | Step 4 MGT | Step 3 done | Arena NSGT root-count check |
| 8 | Step 5 | Step 4 done | Step 4 MGT | |
| 9 | Step 6 analysis | Step 5 NSGT | Step 4 done | Hook decision for each paper |
| 10 | Figures + writing | Step 5 | Step 5 | |
| 11 | Draft complete | Step 6 | Step 5 | |
| 12 | Internal review | Figures + writing | Step 6 | |
| 13 | Revise, journal choice | Draft | Figures + writing | |
| 14 | **Submit paper A** | Revise | Draft | |
(Neha and Anu submit about weeks 16-18.)

## Gates (stop and decide)
- **Week 2:** novelty sweep for all three. If a near-identical paper exists, change the hook now.
- **Step 3 of Neha:** phason wave-like vs diffusive. Pick, justify, test the other.
- **Step 4 of Sumit:** carriers-off returns Step 3 AND high-density limit sane. This is a base paper.
- **MGT distinguishability gate (Sumit, before Step 3):** `steps/step3_prerecheck_mgt_map.md` gives the
  boundary `2h* = pi sqrt(kappa tau_q)` against the trust band. Rule: MGT stays in the title only if the
  boundary is inside the band for a *sourced* `(k_th, tau_q)` pair with a *sourced* phonon mean free path;
  otherwise the paper is retitled and MGT becomes a sensitivity. At the assumed constants this passes for
  `k_th = 60 W/mK` with `tau_q >= 2e-12 s` and `Lambda_ph <= 2 nm`, and fails outright for the thin-film
  `k_th = 1.2 W/mK`. `Lambda_ph` must be sourced before the title is fixed.
- **Step 3 is blocked** until Dr. Vipin confirms the Gupta heat equation (he is adding it to `paper/`).
- **Provisional retitle (Sumit):** `paper/problem_v3_proposal.md` proposes carrier screening + NSGT as the claims,
  MGT as a comparison section. `problem_v2.md` is untouched pending review.
- **MGT maps, all three scholars:** outside the trust band in every case once `Lambda_ph` is sourced
  (`quasicrystal_neha/checks/mgt_map.md`, `mee_anu/checks/mgt_map.md`).
- **Bulk-medium gate (Sumit, before Step 3):** `steps/step3_prerecheck_bulk_medium.md` shows both Fourier and MGT *saturate* in an infinite medium; MGT only rescales the plateau and moves the peak. C2 was restated accordingly — the observable is peak position vs thickness. Step 3 does not start until Dr. Vipin accepts the restatement and confirms the Gupta equation's placement of tau_q.
- **Step 4 of Sumit, added at Task 0 (cheap, decides the paper):** the **C1 test** — `k_i(n0)` at
  fd = 1000 and 3000 must be non-monotonic with its peak within 5% of `n0* = eps33 w/(e mu)`. If it
  is monotone, the ordering argument dies and the paper goes to a Q2 target. Also the
  **floor-resolution test** — the thermal `k_i` must exceed the solver resolution at the thicknesses
  used. Run both on the reduced model (elastic + carriers) before Step 2 if possible.
- **Before submitting Sumit:** a short "measurability" section with three numbers (nulling field
  3.0 kV/cm, Joule load, solver resolution). No numbers -> not Q1.
- **Before any NSGT step:** fix the extra boundary conditions in writing (see equations pack).
- **Week 9:** for each paper write the one-sentence finding (the hook). No sentence -> reduce target journal.

## Weekly rhythm
1. Monday: scholar sends check plot + one-page note of what changed.
2. Tuesday: you (with Arena) run the same step independently; compare using `docs/02_workflow_crosscheck.md`.
3. Wednesday: feedback + next-step equations to scholar.
4. Rest of week: scholar works; you and Arena only prepare the *next* step.

## Deliverables in the repo as work progresses
`semiconductor_sumit/`, `quasicrystal_neha/`, `mee_anu/` each contain:
`README.md` (status tracker), `steps/stepN_*.md` (equations + instruction for the scholar),
`checks/` (verification results), `code_arena/` (your independent implementation),
`figures/`, `paper/`.
