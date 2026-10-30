# Paper B (Neha): Lamb waves in a 1D hexagonal piezoelectric quasicrystal plate
Phonon + phason + electric + MGT heat + nonlocal strain gradient.

**Hook (to confirm at Step 3 gate):** phason as wave-like vs diffusive and its effect as an attenuation mechanism together with MGT heat and the size scales.
**Base paper available after Step 4.**

## Tracker
| Step | What | Check | Scholar | Arena cross-check |
|---|---|---|---|---|
| 1 | Elastic (phonon only) Rayleigh-Lamb | see common/step1_instructions.md | [ ] | [ ] |
| 2 | + piezoelectricity | coupling off -> Step 1; K^2 | [ ] | [ ] |
| 3 | + phason field | phason coupling off -> Step 2; match published 1D hexagonal PQC plate | [ ] | [ ] |
| 4 | + MGT heat | thermal off -> Step 3; classical limit | [ ] | [ ] |
| 5 | + NSGT (phonon first) | l = 0 returns Step 4; decide phason stress later | [ ] | [ ] |
| 6 | Analysis, figures | smooth branches, consistent root counts | [ ] | [ ] |

## Decisions to write down here
- Quasiperiodic axis along thickness z; polarisation direction (write it here).
- Phason model: wave-like or diffusive (choose after reading items 1-5; test the other).
- Constants: choose one literature set, list source, never call them measured (`params.md`).

## Folder layout
`steps/` - `checks/` - `code_arena/` - `figures/` - `paper/`
