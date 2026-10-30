# Q1 scorecard — Paper B (Neha), after the literature sweep

Scored 30 Oct 2026 against the refocused plan in `problem_v2.md`. 5 = a Q1 referee would not raise
the point; 1 = fatal. Deliberately harsh.

| # | Criterion | Score | Evidence |
|---|---|---|---|
| 1 | **Novelty vs closest papers** | **2 / 5** | The niche is crowded: three 2024–2026 papers do QC-plate Lamb waves with nonlocal size effects, one of them (Acta Mech. Solida Sin. 2026, doi:10.1007/s10338-026-00755-4) already reports thermo-phonon-phason attenuation **including attenuation jumps at mode conversion**, which is the effect `docs/03_novelty_upgrades.md` proposed as the major upgrade; the only remaining delta is MGT-instead-of-fractional-Lord–Shulman plus NSGT-instead-of-integral-nonlocal, and the phason-model comparison (the new spine) has not been published but also has not been shown by anyone to matter. |
| 2 | **Physical insight** | **4 / 5** | The thickness-scaling fingerprint is genuinely physical: three mechanisms with three different length contents give three different exponents (`1/h`, `h⁰`, `h`), which converts a modelling choice into a measurement — and it finally gives a reason for the phason field to be in the paper at all rather than being one more degree of freedom. |
| 3 | **Rigour and verification** | **4 / 5** | The merge test (diffusive relaxation → ∞ must reproduce the wave-like model to 1e-6) is a strong, falsifiable check that most QC papers do not have, and every claim carries a tolerance; the score is held at 4 because the phason boundary condition `∂w/∂z = 0` has no experimental support and the code does not exist yet. |
| 4 | **Validity of the size-effect model** | **2 / 5** | Worse than Paper A: not only are `l_nl, l_g` unsourced, but **applying NSGT to the phason strain has no literature precedent** — the NSGT functional is derived for the phonon strain, so half of C3 may be an unjustified extension, and the phason correlation length (the only length that would justify a phason gradient) has no measured value anywhere in the sweep. |
| 5 | **Device / application relevance** | **2 / 5** | Quasicrystal plates are not devices; the paper's justification is "QC nanostructures operate at high temperature" (the competitor's own words), and the practical payoff of knowing which mechanism damps a wave is diagnostic rather than design. This alone keeps the paper out of the top journals unless the fingerprint is airtight. |
| 6 | **Reproducibility** | **5 / 5** | Both phason kinematics in one code, fixed comparison points, tolerances, sourced parameter table, and the merge test as an executable check — better than any of the 15 papers. |

## Verdict: **REFOCUS** (Q1 stretch, Q2 default)

Not GO: as planned, this paper is the fourth 2025–26 QC-plate Lamb paper and the referee will find
[2] in the first page of search results. Not DOWNGRADE outright, because the phason-model comparison
is a real open question and the fingerprint is a real, cheap, falsifiable law.

### What "refocus" means, concretely
1. **The phason-model comparison is the paper.** Everything else (piezo, MGT, NSGT) is supporting
   infrastructure and must be presented as such, with the MGT/NSGT material compressed into the
   formulation section.
2. **The deliverable is a slope table**, not a set of dispersion curves: `fd_peak` vs `h`, three
   exponents, measured not asserted.
3. **Exceptional points are demoted to one supporting figure**, because [2] and [3] are already
   there.

### GO conditions (cheap, and they must be run early)
1. **Merge test at Step 3/4:** diffusive-relaxation limit must reproduce the wave-like model to
   1e-6. If it does not, the two models are not comparable and the paper has no spine.
2. **Slope-separation test at Step 6:** the three log–log slopes must be separated by more than the
   fit error over the reachable `h` range (state the range and the error in the paper).

### Single biggest risk
**The phason field may be invisible.** If the phonon–phason coupling `R` used by the reference
material set is small, the phason branch barely perturbs the Lamb modes, the two kinematics give
nearly identical curves, and C1 — the paper's spine — evaporates. This is a *known* material-set
risk (the competitor's coupling values are not in the open literature I could reach), and it must be
settled numerically at Step 3 before any writing.

### Second risk
`D_ph` (phason diffusion coefficient) has **no measured value** in the sweep. The whole `1/h` branch
of C2 rests on an assumed constant. The paper must present it as a band and say so; if the band is
wide enough to wash out the slope, C2 dies.

### What I would tell Neha to do first
Compute, on a reduced 1D model (phonon + phason only, no piezo, no heat), the two kinematics side by
side and check whether the A0 attenuation differs by more than 1% at the fixed comparison points.
One day of work; it decides whether this is a Q1 paper or a Q2 paper.
