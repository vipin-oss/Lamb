# Workflow: scholar computes, you cross-check with Arena

## Per step
1. **You -> scholar:** `steps/stepN_*.md` = governing equations, boundary conditions, the
   determinant to build, parameter table, the limiting-case check, the plot to send.
2. **Scholar:** implements, sends (a) check plot, (b) a small CSV of numbers at fixed points.
3. **You + Arena:** implement the same step independently (different code path where possible),
   write results into `checks/stepN_compare.md`.
4. **Compare** using the tolerances below. Mismatch -> do not move on; find which side is wrong.

## Fixed comparison points (same for everyone, so numbers can be compared directly)
Save as CSV with columns `mode, fd, c_real, k_imag` (k_imag = 0 until attenuation exists).
- fd values (Hz*m): 500, 1000, 2000, 3000, 5000 (plus step-specific ones in the step file).
- Modes: S0, A0, S1, A1 at least.

## Tolerances
| Quantity | Pass |
|---|---|
| Real phase speed, same model | relative difference < 1e-4 |
| Cutoff frequencies | < 1e-3 |
| Limiting case vs previous step | < 1e-6 (this one is a programming check, should be machine-like) |
| k_imag (attenuation) | < 1e-3 relative; sign must agree |

## Conventions (fix once, same for all three papers)
- Time/space: exp[i(kx - wt)], plate thickness 2h, faces z = +-h, x along the plate, plane strain.
- Attenuation: k = k_r + i k_i with k_i > 0 meaning decay along +x.
- Frequency-thickness: fd = f * 2h in Hz*m (also report omega*h/c_T when comparing to literature).
- Non-dimensionalisation must be stated in every check file.

## Typical failure causes (check in this order)
1. e^{-iwt} vs e^{+iwt}: attenuation sign flips.
2. Missing factor 2 in thickness (h vs 2h).
3. Even/odd split wrongly applied when coupling breaks the symmetry.
4. Branch swap: always compare mode *shapes* or follow by continuity, not by sorting values.
5. NSGT: forgot the higher-order boundary condition -> spurious extra roots.
6. Spurious complex roots from scaling the determinant; use even-in-p,q forms (see common/rayleigh_lamb.py).

## Arena side
`common/rayleigh_lamb.py` is the Step-1 reference. For later steps, every new implementation
you make goes into the scholar's `code_arena/` with a short `NOTES.md` stating the differences
from the scholar's formulation, so a mismatch can be traced.
