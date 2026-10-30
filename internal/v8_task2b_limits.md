# Task 2b — single-coupling limits (units fixed, 30 October 2026)

## The units fault and the fix

`rcp_of` returned `rho*cp`, but the three tabulated values of `cp` (2.8e6, 2.6e6, 2.5e6) are
volumetric heat capacities already, J m^-3 K^-1. The heat capacity was therefore 5680 times too
large in the Sumit paper, 5600 in Neha and 5730 in Anu. `rcp_of` now returns `P['cp']`. The three
papers are consistent with each other under this reading, and each is right in magnitude for an
oxide.

Effect on the numbers already reported: every elastic and size-effect number was produced with the
couplings off, so none of them moves. The fully coupled runs move a little, because the thermal
block changes; the coupled A0 baseline at `fd = 1000` is now 2181.9 m/s and at `fd = 100` it is
943.5 m/s.

## Fourier damping, bulk, after the fix

Sub-block `(u_x, theta)` at `eta = 0`, `tau_q = 0`, every other coupling off. The determinant is
quadratic in `k^2`, so the four roots are exact: with `a = c11 kth`,
`A = -i omega rcp c11 - rho omega^2 kth - i omega T0 b1^2` and `B = i rho rcp omega^3`, solve
`a u^2 + A u + B = 0` for `u = k^2` and take the root with `Re k > 0`, `Im k > 0`.

Constants: `rcp = 2.8e6`, `kth = 60`, `kappa = kth/rcp = 2.143e-5` m^2/s, `c_L = 6076.1` m/s,
`Delta_E = T0 b1^2/(rcp c11) = 8.175e-5`, so the peak of the Fourier shape sits at
`1/(2 pi kappa/c_L^2) = 274` GHz.

| f (Hz) | k_r (1/m) | k_i/k_r | (Delta_E/2) wt/(1+wt^2) | ratio |
|---|---|---|---|---|
| 1e8 | 1.034039e5 | 1.4904e-8 | 1.4907e-8 | 1.000 |
| 1e9 | 1.034039e6 | 1.4904e-7 | 1.4906e-7 | 1.000 |
| 1e10 | 1.034039e7 | 1.4884e-6 | 1.4887e-6 | 1.000 |
| 1e11 | 1.034044e8 | 1.3155e-5 | 1.3157e-5 | 1.000 |
| 2.74e11 | 2.833326e8 | 2.0437e-5 | 2.0437e-5 | 1.000 |
| 1e12 | 1.034079e9 | 1.0424e-5 | 1.0424e-5 | 1.000 |
| 1e13 | 1.034082e10 | 1.1200e-6 | 1.1200e-6 | 1.000 |

Agreement to four digits at every frequency, the peak at 274 GHz and `k_i/k_r = Delta_E/2` there.
This is the check the reviewer asked for, and it passes.

The plate version is not run: it needs the complex `k` of a plate mode, not a real-speed singular
value, and that solver is not written.

## Hutson–White, bulk

Sub-block `(u_z, phi, delta n)` at `eta = 0`, only `e15` and the carriers live, `D_n = 0`, no
recombination, `f = 100` kHz, `n0* = eps11 omega/(q b_n) = 2.965e16` m^-3.

| n0 (m^-3) | k_r (1/m) | k_i/k_r |
|---|---|---|
| 1e15 | 2.386959e2 | -1.30e-3 |
| 1e16 | 2.377207e2 | -1.16e-2 |
| 3e16 | 2.340439e2 | -1.86e-2 |
| 1e17 | 2.306072e2 | -9.85e-3 |
| 3e17 | 2.300457e2 | -3.52e-3 |
| 1e18 | 2.299768e2 | -1.06e-3 |

The magnitude peaks at `3e16`, which is `n0*` to within one grid step, as predicted. The sign is
negative in this convention, i.e. growth rather than decay; four different starting guesses all
converge to the same root, so it is not a root-selection artefact. Either the acoustoelectric sign
in the v8 rows is the opposite of what the masters intend, or the masters should say the model
amplifies at `n0 = n0*` with no drift. That question is put to the reviewer and nothing is written
into a master until it is answered.

## Why the plate crossover is not at n0*

Plate S0 at `fd = 100`, piezoelectric plus carriers only, three diffusivities:

| D_n (m^2/s) | n0 = 1e16 | 1e17 | 1e18 | 1e19 |
|---|---|---|---|---|
| 1e-3 | 5508.9 | 5508.7 | 5504.6 | 5474.3 |
| 2.6e-4 | 5508.9 | 5508.7 | 5504.6 | 5474.3 |
| 0 | build degenerates | - | - | - |

The plate result is independent of `D_n` to the last digit, so it is not a diffusion or Debye-length
effect inside the code; and at `D_n = 0` the carrier block loses its roots and the build fails, so
that control cannot be reported. The crossover is set by the ratio of the carrier relaxation
`(-i omega + 1/tauR)` to `omega` together with `q/eps`, and it sits 30 to 300 times above the bulk
`n0*` because the plate test measures the static stiffening at `kh -> 0`, not the dielectric
resonance that produces the bulk peak. That is the reading of the evidence, not a proof, and the
closed-form plate threshold is the next thing to write down.

## Parity

Unchanged and reconfirmed: Sumit none, Sumit with `beta_th = Pi_th = E_g = 0` the pair
`(+,-,-,-,+)` and its negative, Neha and Anu the same pair always.

## Not done

Phason limits (Neha) and magnetoelastic limits (Anu).
