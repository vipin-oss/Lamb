# Paper C (Anu): Lamb waves in a magneto-electro-elastic plate
BaTiO3/CoFe2O4 + MGT heat + nonlocal strain gradient (2 length scales).

**Hook (to confirm in week 9):** magnetoelectric coupling vs thickness, volume fraction and size scales for the four electric x magnetic face conditions: a design map for sensors.
**Base paper available after Step 4.** This is the lowest Q1 probability as planned; the design map is what lifts it.

## Tracker
| Step | What | Check | Scholar | Arena cross-check |
|---|---|---|---|---|
| 1 | Elastic Rayleigh-Lamb | see common/step1_instructions.md | [ ] | [ ] |
| 2 | + piezoelectric (open/short) | coupling off -> Step 1; K^2 | [ ] | [ ] |
| 3 | + piezomagnetic + ME link; sweep volume fraction | magnetic off -> Step 2; match Chen/Pan 2007 | [ ] | [ ] |
| 4 | + MGT heat (pyroelectric/pyromagnetic) | thermal off -> Step 3; classical limit | [ ] | [ ] |
| 5 | + NSGT | l = 0 returns Step 4; nonlocal-only, gradient-only | [ ] | [ ] |
| 6 | Analysis, figures | smooth branches, consistent root counts | [ ] | [ ] |

## Decisions to write down here
- Poling direction along thickness z.
- Effective constants: name source and homogenisation method; table for volume fractions 0, 0.2, 0.4, 0.6, 0.8, 1.0 (`params.md`).
- Define K^2 for electric and magnetic open/short explicitly before Step 2.

## Folder layout
`steps/` - `checks/` - `code_arena/` - `figures/` - `paper/`
