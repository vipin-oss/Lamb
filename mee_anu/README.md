# Paper C (Anu): Lamb waves in a magneto-electro-elastic plate

BaTiO₃/CoFe₂O₄ + MGT heat + nonlocal strain gradient (2 length scales).

**Status: Task 0 done (30 Oct 2026), awaiting Dr. Vipin's approval at the gate.**
Scope re-anchored at Task 0 — see `paper/problem_v2.md`. **Verdict: DOWNGRADE to Q2** with a Q1
stretch; this matches the pre-literature prediction in `docs/00_feasibility_analysis.md`.

## Hook (rewritten at Task 0)

> The piezomagnetic volume fraction that maximises magnetoelectric coupling is not a material
> constant: it is set by a mechanical matching condition at the working frequency-thickness, so the
> optimum traces a ridge in the (vf, fd) plane whose position moves with the two NSGT length scales
> and the MGT relaxation time — and the static optimum in the materials literature is the fd → 0
> edge of that ridge.

The original hook ("ME coupling vs thickness, vf, size scales: a design map") survives as the map;
the paper's claim is that the map's optimum *moves*, which a map alone does not say.

## Tracker

| Step | What | Check | Scholar | Arena cross-check |
|---|---|---|---|---|
| 0 | Literature + novelty sweep, problem v2, scorecard | 14 papers; empty cell + empty question | — | [x] |
| 1 | Elastic Rayleigh–Lamb | see common/step1_instructions.md | [ ] | [ ] |
| 2 | + piezoelectric (open/short) | coupling off -> Step 1; **K_E² defined explicitly** | [ ] | [ ] |
| 3 | + piezomagnetic + ME link; sweep vf | magnetic off -> Step 2; match Chen/Pan 2007; **K_M², K_ME defined; ridge test** | [ ] | [ ] |
| 4 | + MGT heat (pyroelectric/pyromagnetic) | thermal off -> Step 3; classical limit | [ ] | [ ] |
| 5 | + NSGT | l = 0 returns Step 4; restricted to the mechanical part (stated) | [ ] | [ ] |
| 6 | Analysis, figures | branches, root counts, ridge `vf*(fd)`, **static anchor < 5%** | [ ] | [ ] |
| 7 | **U1** dynamic ME ridge + design rule | four face-condition ridges; symmetric-phase check | [ ] | [ ] |
| 7b | **U2** homogenisation band (minor) | two schemes, band width vs ridge motion | [ ] | [ ] |

## Decisions to write down here

- Poling direction **along thickness z**; electric open/short × magnetic open/short = **four cases**,
  and the chosen case must be printed in every figure caption.
- Effective constants: **name the source and the homogenisation method**; use at least two schemes
  and report the band (U2). Table for vf = 0, 0.2, 0.4, 0.6, 0.8, 1.0 in `params.md`.
- `K_E²`, `K_M²`, `K_ME`: definitions must be written before Step 2 (per mode, per fd).
- `l_nl, l_g`: **dimensionless l/h sweeps only** (Dr. Vipin's ruling for Paper A, applied here).
  They are applied to the mechanical part only; stated, not hidden.
- `τ_q`: assumed range 10⁻¹³–10¹¹ s, labelled assumed, never "measured".

## Gate status

Task-0 gate: **waiting for approval**. First action requested (before any writing): the three-number
ridge test in `paper/q1_scorecard.md` — peak height, peak position, half-width of `K_ME(vf)` at
fd = 500 and 5000.

## Folder layout
`paper/` — `steps/` — `checks/` — `code_arena/` — `figures/`
