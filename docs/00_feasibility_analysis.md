# Feasibility analysis: can these three papers reach a Q1 journal?

Honest short answer: **all three are publishable, but "Q1" is not automatic for any of them.**
The plans are strong on method and verification. The risk is the same for all three:
reviewers can read each as "known plate problem + one more known effect added". A Q1 paper
needs a *finding*, not just a bigger model.

> Basis: the three plan PDFs only. I have not yet done the literature sweep. Quartile of a
> journal changes every year; check SJR for the target journal before submitting.
> Week 1 of the roadmap is exactly the novelty sweep that confirms or kills what is below.

## Common strengths (all three)
- Step-wise build with a limiting-case check after every step. Reviewers trust this.
- Complex branches followed together with attenuation, not only real dispersion curves.
- Honest handling of extra boundary conditions of nonlocal strain gradient theory (NSGT).
- Code and parameter table in the supplement (reproducibility).

## Common weaknesses (fix these in the design, not at revision)
1. **Novelty by combination.** "MGT + NSGT + X plate" must be turned into a statement of the
   form "we show that ... which earlier models cannot show".
2. **NSGT is contested** (Shaat critique is already in the reading lists). For a wave problem
   NSGT gives a dispersion that can *stiffen or soften* with k. Reviewers will ask for a
   physical reason to trust it at high k. Plan: show results only in the k range where the
   continuum model is defensible, and give the Q1-level argument in the paper.
3. **Parameter uncertainty** (length scales, effective constants). Sensitivity ranking is
   already planned; make it a main figure, not an appendix.
4. **MGT thermal relaxation time** is rarely measured. Use ranges and say so.
5. **Too many effects at once** hides which effect does what. Always include a
   "turn-one-effect-on-at-a-time" figure (this is the real scientific content).

## Per-paper assessment

### A. Semiconductor plate (Sumit) — best Q1 chance of the three
- Ingredients: piezo + MGT heat + carriers (drift-diffusion, linearised) + NSGT, Lamb waves.
- Closest work (from the plan): Dhib et al. 2024 (GaAs plate, complex branches, no size
  effect, no MGT), Ray 2019 (strain-gradient plate, no piezo/semiconductor).
- Why it is stronger: carrier screening gives a real physical mechanism (attenuation peaks
  vs carrier density / frequency). Mobile charge + thermal + size effect in one plate model
  has a clear device story (SAW/Lamb-wave amplifiers, acoustoelectric sensors).
- Main risks: (a) the group's own earlier MGT piezo-semiconductor papers are half-space; a
  reviewer will ask "what is new beyond the plate geometry?" -> the answer must be the
  carrier x thickness x size-scale interaction. (b) Linearised carrier model needs a
  stated DC bias/doping and a stated regime of validity.
- **Hook to build the paper around:** where does attenuation peak (carrier density, fd) and
  how do the two length scales shift/suppress that peak.
- Likely targets: Int. J. Solids Struct., Int. J. Eng. Sci., Appl. Math. Model.,
  Wave Motion, J. Sound Vib., Mech. Mater. (verify quartile each year).

### B. Quasicrystal plate (Neha) — moderate chance, needs a sharper hook
- Ingredients: 1D hexagonal piezo quasicrystal + phason + MGT + NSGT.
- Closest work: 2026 thermal quasicrystal nanoplate paper (reading item 5), integral-nonlocal
  quasicrystal nanoplate paper (item 3). The plan already says "state exactly which
  combination is new".
- Weakness: crowded niche; material constants poorly measured; phason model choice
  (wave-like vs diffusive) can change conclusions.
- **Hook to build the paper around:** phason-diffusive vs phason-wave modelling as a
  *source of attenuation*, and how it interacts with MGT heat and the size scales.
  If this comparison is not ready, aim at a good Q2 and keep Q1 as the stretch goal.
- Decision gate (end of Step 3): if phason choice changes the story, make that the paper.

### C. Magneto-electro-elastic plate (Anu) — lowest Q1 probability as planned
- Ingredients: BaTiO3/CoFe2O4 MEE + MGT + NSGT.
- Closest work: Lamb waves in MEE plates (Chen/Pan, Zhang 2025), NSGT MEE plates
  (buckling/vibration, Nanomaterials 2021), thermal MEE plates — each exists separately.
- Weakness: effective constants depend on homogenisation source; most of the paper becomes
  "volume fraction sweep", which is incremental.
- **Hook to build the paper around:** the *magnetoelectric coupling coefficient vs thickness,
  volume fraction and size scale* (open/short electric x open/short magnetic), i.e. a
  design map for sensors. A map with a design rule is a finding.
- Realistic target: strong Q2 to lower Q1 unless the design-map result is clean.

## Ranking and recommendation
| Rank | Paper | Scholar | Q1 chance (my estimate, pre-literature) | Needs |
|---|---|---|---|---|
| 1 | Semiconductor plate | Sumit | decent | attenuation-peak hook, regime of validity |
| 2 | Quasicrystal plate | Neha | moderate | phason-modelling hook |
| 3 | MEE plate | Anu | lower as planned | ME design-map hook |

**Strategy:** do not make all three wait for Step 5. Each plan already yields a *publishable
base* earlier (semiconductor: after Step 4 carriers; quasicrystal: after Step 4 heat; MEE:
after Step 4 heat). If Step 5 (NSGT) turns out heavy, the base paper still goes to a good
journal and NSGT becomes paper 2.

## Errors / things to fix in the plans before the scholars start
- Semiconductor plan: work plan says "after step 3 verified piezo-thermal base; steps 4 and
  5 add new parts" -- consistent, but Step 4 check ("carrier density 0 returns step 3") is
  necessary but not sufficient. Add: **high-carrier-density limit must approach the
  short-circuit-like screened result**.
- MEE plan: Step 2 check says "open/short speed difference gives K^2" -- define K^2 formula
  explicitly (for plates K^2 is mode- and fd-dependent). Same for magnetic K^2.
- Quasicrystal plan: Step 1 check is "phonon only" which is just an elastic plate, so it
  duplicates Step 1 of the others. Keep, but make Step 3 the true gate (published 1D hexagonal
  PQC plate result).
- All plans: Step 5 NSGT adds higher-order terms -> *extra boundary conditions* and spurious
  roots. Specify in advance: which two BCs (classical traction-free + higher-order traction
  = 0), and a root-count check against the classical limit.
- Sign convention: fix e^{i(kx - wt)} once for the whole group; attenuation sign errors are
  the most common cross-check failure.
- Reading item 4 in the MEE list and item 5 in the semiconductor list are
  "confirm exact citation" type entries; verify before citing.
