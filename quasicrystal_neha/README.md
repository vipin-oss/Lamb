# Paper B (Neha): Lamb waves in a 1D hexagonal piezoelectric quasicrystal plate

Phonon + phason + electric + MGT heat + nonlocal strain gradient.

**Status: Task 0 done (30 Oct 2026), awaiting Dr. Vipin's approval at the gate.**
Scope was re-anchored at Task 0 after the literature sweep — see `paper/problem_v2.md`.

## Hook (rewritten at Task 0)

> Three dissipation mechanisms act in a quasicrystal plate — phason relaxation, MGT thermal
> relaxation, and the size-effect distortion of the ω(k) map — and they scale with plate thickness
> differently (fd_peak ∝ 1/h, ∝ h⁰, ∝ h), so a thickness scan of the attenuation-peak position
> identifies the dominant mechanism with no fitted constant, while phase velocity cannot
> distinguish them at all.

**What changed and why:** the proposed major upgrade (phason wave-like vs diffusive →
exceptional points) is **partly anticipated**: mode conversions/intersections are in *Wave Motion*
134, 103479 (2025), and attenuation jumps at mode conversion are in *Acta Mech. Solida Sin.* (2026,
doi:10.1007/s10338-026-00755-4). The phason-model *comparison* is kept as the spine, sharpened into
a measurable scaling law; exceptional points are demoted to one supporting figure.
Details: `paper/literature_table.md`.

## Tracker

| Step | What | Check | Scholar | Arena cross-check |
|---|---|---|---|---|
| 0 | Literature + novelty sweep, problem v2, scorecard | 15 papers, QC niche mapped | — | [x] |
| 1 | Elastic (phonon only) Rayleigh–Lamb | see common/step1_instructions.md | [ ] | [ ] |
| 2 | + piezoelectricity | coupling off -> Step 1; K² | [ ] | [ ] |
| 3 | + phason field (BOTH kinematics) | coupling off -> Step 2; **merge test: diffusion → ∞ = wave-like, <1e-6**; match Acta Mech. 232 (2021) | [ ] | [ ] |
| 4 | + MGT heat | thermal off -> Step 3; classical limit | [ ] | [ ] |
| 5 | + NSGT | l = 0 returns Step 4; decide phason stress **after Dr. Vipin's ruling** | [ ] | [ ] |
| 6 | Analysis, figures | smooth branches, root counts, **slope table fd_peak vs h** | [ ] | [ ] |
| 7 | **U1** phason-model comparison (spine of the paper) | merge test + slope separation | [ ] | [ ] |
| 7b | **U2** attenuation budget by energy flux | budget closes to <1e-3 | [ ] | [ ] |

## Decisions to write down here

- Quasiperiodic axis **along thickness z**; poling direction to be fixed at Step 2 (write it here).
- **Phason kinematics: do BOTH** (wave-like and diffusive). The plan's instruction "choose one" is
  reversed at Task 0, because the comparison is now the paper's only defensible novelty.
- **SETTLED at the gate (30 Oct 2026):** **NSGT applies to the phonon stress only** in the base
  model; the phason stress is classical. The NSGT-on-phason variant is a **Step-5 sensitivity
  result only** — one labelled figure, never used to support C1–C3.
- **PROVISIONAL:** the thickness-scaling hook (C2) is provisional **pending Dr. Vipin's review**.
  Nothing may be written around it until approved; the two-kinematics work and the merge test (C1)
  can proceed because they are needed either way.
- **Open question (Step 3):** phason traction-free face condition `H_zz = H_zx = 0` and phason flux
  `∂w/∂z = 0` for the diffusive model — the latter has no experimental support; label as assumed.
- Constants: one literature set, source in `params.md`; `D_ph` and `τ_q` are **assumed ranges**, never
  "measured".

## Gate status

Task-0 gate: **reports received; hook provisional.** Verdict in `paper/q1_scorecard.md` is
**REFOCUS** — Q1 only if the merge test and the slope-separation test both pass; otherwise Q2.
Step 1 may start; Step 5 waits on nothing further (the NSGT-on-phason question is settled), but the
C2 hook cannot appear in any text until Dr. Vipin reviews it.

## Folder layout
`paper/` — `steps/` — `checks/` — `code_arena/` — `figures/`
