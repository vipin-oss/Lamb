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

## Hutson–White, bulk — the sign was in my test, not in the code

The model is right and the masters are right. Gauss's law reads `M_34 = q` with the row
`i k D_x + eta D_z + q dn = 0`, the carrier row carries `M_43 = b_n n0 L` and
`M_44 = -i omega - D_n L - i k v_d + 1/tauR`, and both match the master's Section "Reduced
equations" line for line (checked against the display in Calculation D and the worked row
derivations). The piezoelectric block is skew: `M_23 = +e15 k^2` and `M_32 = -e15 k^2` at `eta = 0`.

My hand-built 3x3 had `M_23 = M_32 = -e15 k^2`, symmetric, and that is what produced the growth
sign. With the skew entry the sub-block `(u_z, phi, dn)` at `eta = 0`, `D_n = 0`, `v_d = 0`,
`f = 100` kHz, `n0* = eps11 omega/(q b_n) = 2.9654e16`, `K^2 = e15^2/(eps11 c44) = 0.0719`:

| n0 (m^-3) | k_r (1/m) | k_i/k_r |
|---|---|---|
| 1e15 | 2.221350e2 | +1.1293e-3 |
| 1e16 | 2.228563e2 | +1.0219e-2 |
| 2e16 | 2.244076e2 | +1.5869e-2 |
| 3e16 | 2.258900e2 | +1.7343e-2 |
| 4e16 | 2.269985e2 | +1.6758e-2 |
| 1e17 | 2.292724e2 | +9.7364e-3 |
| 3e17 | 2.298858e2 | +3.5148e-3 |
| 1e18 | 2.299623e2 | +1.0645e-3 |

`k_i > 0`, decay, as it must be. The peak is at `3e16`, one grid step from `n0*`, with
`k_i/k_r = 1.73e-2`; `K^2/2 = 3.6e-2` and the resonance halves it, so 1.8e-2 is the expected
magnitude and 1.73e-2 is what comes out. Pass on sign, position and magnitude.

The lesson is worth recording: a symmetric test sub-block looks harmless and inverts the physics.
Nothing in `internal/code` or in the masters changed for this.

## The closed form for the plate threshold

The plate measures the static stiffening at `kh -> 0`, and the piezoelectric term is screened when
the carrier response keeps up with the field. Linearising the pair (Gauss, carriers) gives the
threshold

```
n0_th = eps33 | -i omega + D_n k^2 + 1/tauR | /(q b_n)
```

Three limits follow, and each was tested.

1. Recombination slow, `1/tauR << omega`: `n0_th = eps33 omega/(q b_n) = n0* = 3.0e16`, the same
   number as the bulk peak. That is the consistency the bulk test shows.
2. Recombination fast, `1/tauR >> omega`: `n0_th = eps33/(q b_n tauR)`. With `tauR = 1` ns this is
   5.6e19, and the observed crossover between 1e18 and 1e19 is its lower shoulder. The factor
   against `n0*` is `1/(omega tauR) = 1592`, which is why the plate crossover sits 30 to 300 times
   above the bulk peak.
3. Change `tauR` and the threshold moves: with `tauR = 1` ms at `fd = 100` the screening is already
   complete at `n0 = 1e18`, S0 falling to 5262.7 m/s against the short-circuit 5259.1, and the
   transition sits at or below 1e17. With `tauR = 1` ns at the same frequency the speed is still
   5504.6 at 1e18. So the threshold is recombination-controlled, as the closed form says.

## Phason limit (Neha) and magnetoelastic limit (Anu)

Both at `l_g = l_nl = 0` (with the defaults at 1e-8 the columns collapse as before, giving
singular values of 1e-16 and meaningless dips), `h = 5e-4`, `fd = 1000`, A0 branch.

| case | A0 (m/s) | shift |
|---|---|---|
| Neha full | 2216.6 | - |
| Neha, phason decoupled (`R1 = R2 = R3 = b_w = 0`) | 2222.5 | +5.9 (0.27 per cent) |
| Anu full | 2277.1 | - |
| Anu, magnetoelastic off (`q31 = q33 = q15 = 0`) | 2276.4 | -0.7 (0.03 per cent) |

At this frequency the phason coupling is a small but measurable correction and the magnetoelastic
coupling is essentially absent. The `K1 = K2 = 0` variant of Neha gives 2076.6 with a dip depth of
2, which is not a dip; it is not reported as a limit.

## Parity

Unchanged and reconfirmed: Sumit none, Sumit with `beta_th = Pi_th = E_g = 0` the pair
`(+,-,-,-,+)` and its negative, Neha and Anu the same pair always.

## Not done

Phason limits (Neha) and magnetoelastic limits (Anu).

## Note for the scholar file: the screening density is not a constant

The density at which the piezoelectric stiffening is screened is
`n0_th = eps33|-i omega + D_n k^2 + 1/tauR|/(q b_n)`, so it depends on the carrier lifetime, not
only on the frequency. The value quoted in the papers, with `tauR = 1` ns, is a placeholder for a
material that has not been characterised: at `tauR = 1` ms the same plate screens by `n0 = 1e18`
instead of `1e19`. Until a measured lifetime is available for the film, any statement of the form
"the crossover lies at such and such a density" must carry the lifetime beside it. This goes into
the scholar notes when the Sumit paper is next opened; it is recorded here first.

## Phason relaxation (Neha), 30 October 2026

Bulk, decoupled phason, closed form from `K1 k^2 = rho_p omega^2 + i omega gamma`:
`c_ph = sqrt(K1/rho_p) = 31622.78` m/s for `gamma -> 0`, `k_i/k_r = gamma/(2 rho_p omega)` while
`gamma << 2 rho_p omega = 1.5e9`, and the diffusive branch `k_r -> sqrt(omega gamma/(2 K1))`,
`k_i/k_r -> 1` for `gamma >> 1.5e9`. At `omega = 2 pi 1e8`:

| gamma | k_r (1/m) | k_i/k_r | omega/k_r (m/s) | closed form |
|---|---|---|---|---|
| 0 | 1.986918e4 | 0 | 31622.8 | 31622.8 |
| 1e2 | 1.986918e4 | 6.6315e-8 | 31622.8 | wave |
| 1e4 | 1.986918e4 | 6.6315e-6 | 31622.8 | wave |
| 1e6 | 1.986918e4 | 6.6315e-4 | 31622.8 | wave |
| 1e8 | 1.991263e4 | 6.6025e-2 | 31553.8 | wave, damping visible |
| 1e10 | 5.313019e4 | 0.927 | 11826 | diffusive, sqrt(w g/(2K1)) = 5.117e4 |
| 1e12 | 5.118563e5 | 0.9993 | 1228 | diffusive, 5.117e5 |

Plate, all couplings on, `l = 0`, `h = 5e-4`, `fd = 1000`, A0 branch; the decoupled-phason value
(`R1 = R2 = R3 = b_w = 0`) is 2222.5 m/s:

| gamma | 1e2 | 1e6 | 1e8 | 1e10 | 1e12 |
|---|---|---|---|---|---|
| A0 (m/s) | 2216.6 | 2216.6 | 2216.6 | 2219.3 | 2222.0 |

The phonon branch recovers the decoupled value as the phason is overdamped, 2222.0 against 2222.5
at `gamma = 1e12`, and the coupling costs 5.9 m/s while the phason is still wave-like. The S0
window tried at 5308 m/s was misplaced: the Neha S0 branch sits near 5050 m/s with a dip depth of
only 12, so no S0 entry is quoted.

## Magnetoelastic coupling against volume fraction (Anu)

Mixing rule, ours: the two-phase ME coefficient is taken as the product property
`alpha(v) = v(1-v) alpha_0`, which vanishes at both ends and peaks at `v = 1/2`. It is put into the
model by scaling the three magnetoelastic constants with `f(v) = 4v(1-v)`, so `alpha^2 ∝ f^2`.

Thin plate, `fd = 100`, S0: the speed is 6280.67 m/s for every `v` to 0.01 m/s. The effect is below
resolution because at small `k` the magnetoelastic terms enter the mechanical rows through
`eta q31`, `eta q33` and `i k q15`, and `q15/c44` is of order `4e-9`.

A0 at `fd = 1000`, fine window of 0.5 m/s, parabola through the three lowest points:

| v | 0 | 0.25 | 0.5 | 0.75 | 1 |
|---|---|---|---|---|---|
| f = 4v(1-v) | 0 | 0.75 | 1 | 0.75 | 0 |
| A0 (m/s) | 2276.17 | 2276.94 | 2277.48 | 2276.94 | 2276.17 |
| dc (m/s) | 0 | +0.775 | +1.310 | +0.775 | 0 |
| dc/f^2 | - | 1.377 | 1.310 | 1.377 | - |

Peak at `v = 1/2`, zero at both ends, `dc/f^2` constant to 5 per cent: `Delta c ∝ alpha^2`, as
asked. The five per cent is the quadratic approximation ending, not scatter — the two symmetric
points 0.25 and 0.75 agree to the last digit.
