# STATUS — three-paper project

**Updated 30 Oct 2026. Branch `arena/beec1abf-lamb`, PR #1 (open, not merged).**

## One-line state

Route A adopted: the thermal channel is an **adiabatic/isothermal bracket**, not a modelled MGT
mechanism. Step 2 (Sumit) is closed; Step 3 (Sumit) is specified and short. Neha and Anu are at Step 2
with their v3 proposals written.

## Paper status

| paper | stage | gate now blocking | verdict |
|---|---|---|---|
| **Sumit** (ZnO PSC plate) | Step 2 **closed** (6×6 factorisation `= 8.000000`, spread 4.3e-13; S0 → 5308.581 vs analytic); Step 3 pack written (`steps/step3_thermal_bracket.md`) | scholar implements Step 3 bracket; C1 monotonicity and C3 identifiability tests at Step 4 | **GO, conditional** |
| **Neha** (QC plate) | Step 1 pack done (1 page); Step 2 not started | phason-kinematics decision gate | **REFOCUS** |
| **Anu** (MEE plate) | Step 1 pack done (1 page); Step 2 not started | ridge test at week 9 | **DOWNGRADE to Q2** |

## What changed this week

1. MGT demoted everywhere: the bulk test shows both Fourier and MGT *saturate*; the distinguishability
   map puts the relaxation time outside the trust band for all three materials.
2. The three-scale overlap window is **empty** for all three (`docs/04_scale_overlap_window.md`).
3. Route A: bracket replaces the heat model; Step 3 shrinks accordingly.
4. Sumit's constants: **Set L** (standard ZnO literature set) adopted as primary —
   `v_short = 5259.13`, `v_open = 5509.57` m/s, `K²(0) = 0.08884`, `k31 = 0.196`. All `k`-values are
   **UNVERIFIED** against measurement.
5. Scorecards re-scored: Sumit 22→20, Neha 19→20, Anu 19→20.

## Open items (owners)

- **[V]** drop the Gupta heat-equation paper into `paper/` (appendix only), and the group's ZnO
  constant table if it exists (would replace Set L).
- **[V]** source (or waive) a literature `k31` for ZnO so the constant check can close.
- **[S]** implement Step 3 bracket; report checks 1–8.
- **[N]** `k_th` and `c_p` at 300 K for the actual composition.
- **[A]** BaTiO₃ `k_th` and `Λ_ph` for both phases.
- **[Arena]** nothing outstanding; next Arena task is the Sumit Step-3 cross-check when the scholar's
  numbers arrive.

## Hard gates still armed

- Sumit Step 4: **C1 monotonicity** and **C3 identifiability** (peak-locus sensitivity to `l/h`).
- Neha: phason-kinematics decision; NSGT-on-phason stays a sensitivity.
- Anu: week-9 ridge test decides Q1 vs Q2.
